import pandas as pd
from rdflib.graph import ConjunctiveGraph
from uberongraph_tools import UberonGraph
from ccf_tools import chunks, split_terms, transform_to_str
from datetime import datetime
import logging

logger = logging.getLogger('ASCT-b Tables Log')

#    olabel            slabel               o               s
# 0  kidney      right kidney  UBERON:0002113  UBERON:0004539

def generate_class_graph_template(ccf_tools_df :pd.DataFrame):
  """Takes a ccf tools dataframe as input;
  Validates relationships against OBO;
  Adds relationships to template, tagged with OBO status"""
  error_log = pd.DataFrame(columns=ccf_tools_df.columns)
  valid_error_log = pd.DataFrame(columns=ccf_tools_df.columns)
  strict_log = pd.DataFrame(columns=ccf_tools_df.columns)
  seed = {'ID': 'ID', 'Label': 'LABEL', 'User_label': 'A skos:prefLabel',
          'Parent_class': 'SC %',
          'OBO_Validated_isa': '>A CCFH:IN_OBO',
          'validation_date_isa': '>A dc:date',
          'part_of': 'SC part_of some %',
          'OBO_Validated_po': '>A CCFH:IN_OBO',
          'validation_date_po': '>A dc:date',
          'overlaps': 'SC overlaps some %',
          'OBO_Validated_overlaps': '>A CCFH:IN_OBO',
          'validation_date_overlaps': '>A dc:date',
          'connected_to': 'SC connected_to some %',
          'OBO_Validated_ct': '>A CCFH:IN_OBO',
          'validation_date_ct': '>A dc:date',
          'develops_from': 'SC develops_from some %',
          'OBO_Validated_df': '>A CCFH:IN_OBO',
          'validation_date_df': '>A dc:date'}
  ug = UberonGraph()
  records = [seed]
  if ccf_tools_df.empty:
    return (pd.DataFrame.from_records(records), error_log, ConjunctiveGraph(), valid_error_log, strict_log)

  terms = set()
  terms_pairs = set()
  terms_ct_as = set()
  nb_indirect = 0
  nb_validate = 0
  
  # Add declarations and labels for entity
  for i, r in ccf_tools_df.iterrows():
    records.append({'ID': r['s'], 'User_label': r['user_slabel']})
    records.append({'ID': r['o'], 'User_label': r['user_olabel']})
    if 'CL' in r['s'] and 'UBERON' in r['o']:
      terms_ct_as.add(f"({r['s']} {r['o']})")
    else:
      terms_pairs.add(f"({r['s']} {r['o']})")

    terms.add(r['s'])
    terms.add(r['o'])

  terms_pairs_start = len(terms_pairs)

  terms_labels = ug.query_uberon(" ".join(list(terms)), ug.select_label)

  for term, label in terms_labels:
    row = ccf_tools_df[(ccf_tools_df['s'] == term) | (ccf_tools_df['o'] == term)].iloc[0]
    if row['s'] == term and row['slabel'] != label:
      logger.warning(f"Different labels found for {term}. Uberongraph: {label} ; ASCT+b table: {row['slabel']}")
      ccf_tools_df.loc[(ccf_tools_df['s'] == term), 'slabel'] = label
      ccf_tools_df.loc[(ccf_tools_df['o'] == term), 'olabel'] = label
        
    if row['o'] == term and row['olabel'] != label:
      logger.warning(f"Different labels found for {term}. Uberongraph: {label} ; ASCT+b table: {row['olabel']}")
      ccf_tools_df.loc[(ccf_tools_df['o'] == term), 'olabel'] = label
      ccf_tools_df.loc[(ccf_tools_df['s'] == term), 'slabel'] = label
      
  valid_subclass = ug.query_uberon(" ".join(list(terms_pairs)), ug.select_subclass)

  for s, o in valid_subclass:
    rec = dict()
    rec['ID'] = s
    rec['Parent_class'] = o
    rec['OBO_Validated_isa'] = True
    rec['validation_date_isa'] = datetime.now().isoformat()
    records.append(rec)

  terms_valid_subclass = transform_to_str(valid_subclass)

  valid_subclass_onto = ug.query_uberon(" ".join(list(terms_valid_subclass)), ug.select_subclass_ontology)

  terms_s, terms_o = split_terms(transform_to_str(valid_subclass - valid_subclass_onto))

  rows_nvso = ccf_tools_df[ccf_tools_df['s'].isin(terms_s) & ccf_tools_df['o'].isin(terms_o)]

  nb_indirect += len(rows_nvso)

  for _, r in rows_nvso.iterrows():
    valid_error_log = valid_error_log.append(r)
  
  terms_pairs = terms_pairs - terms_valid_subclass

  valid_po = ug.query_uberon(" ".join(list(terms_pairs)), ug.select_po)

  valid_ct_as_po = ug.query_uberon(" ".join(list(terms_ct_as)), ug.select_po)
  print(len(valid_ct_as_po))

  for s, o in valid_po.union(valid_ct_as_po):
    rec = dict()
    rec['ID'] = s
    rec['part_of'] = o
    rec['OBO_Validated_po'] = True
    rec['validation_date_po'] = datetime.now().isoformat()
    records.append(rec)

  terms_valid_po = transform_to_str(valid_po)

  valid_po_nr = ug.query_uberon(" ".join(list(terms_valid_po)), ug.select_po_nonredundant)

  terms_s, terms_o = split_terms(transform_to_str(valid_po - valid_po_nr))

  rows_nvponr = ccf_tools_df[ccf_tools_df['s'].isin(terms_s) & ccf_tools_df['o'].isin(terms_o)]

  nb_indirect += len(rows_nvponr)

  for _, r in rows_nvponr.iterrows():
    valid_error_log = valid_error_log.append(r)

  terms_pairs = terms_pairs - terms_valid_po

  terms_ct_as = terms_ct_as - transform_to_str(valid_ct_as_po)

  valid_overlaps = ug.query_uberon(" ".join(list(terms_pairs)), ug.select_overlaps)

  valid_ct_as_overlaps = ug.query_uberon(" ".join(list(terms_ct_as)), ug.select_overlaps)
  print(len(valid_ct_as_overlaps))

  for s, o in valid_overlaps.union(valid_ct_as_overlaps):
    rec = dict()
    rec['ID'] = s
    rec['overlaps'] = o
    rec['OBO_Validated_overlaps'] = True
    rec['validation_date_overlaps'] = datetime.now().isoformat()
    records.append(rec)
  
  terms_valid_overlaps = transform_to_str(valid_overlaps)

  valid_o_nr = ug.query_uberon(" ".join(list(terms_valid_overlaps)), ug.select_overlaps_nonredundant)

  terms_s, terms_o = split_terms(transform_to_str(valid_overlaps - valid_o_nr))

  rows_nvonr = ccf_tools_df[ccf_tools_df['s'].isin(terms_s) & ccf_tools_df['o'].isin(terms_o)]

  nb_indirect += len(rows_nvonr)

  for _, r in rows_nvonr.iterrows():
    valid_error_log = valid_error_log.append(r)

  terms_pairs = terms_pairs - transform_to_str(valid_overlaps)

  terms_ct_as = terms_ct_as - transform_to_str(valid_ct_as_overlaps)

  valid_ct = ug.query_uberon(" ".join(list(terms_pairs)), ug.select_ct)

  for s, o in valid_ct:
    rec = dict()
    rec['ID'] = s
    rec['connected_to'] = o
    rec['OBO_Validated_ct'] = True
    rec['validation_date_ct'] = datetime.now().isoformat()
    records.append(rec)

  terms_pairs = terms_pairs - transform_to_str(valid_ct)

  valid_df = ug.query_uberon(" ".join(list(terms_pairs)), ug.select_develops_from)

  for s, o in valid_df:
    rec = dict()
    rec['ID'] = s
    rec['develops_from'] = o
    rec['OBO_Validated_df'] = True
    rec['validation_date_df'] = datetime.now().isoformat()
    records.append(rec)

  terms_s, terms_o = split_terms(terms_pairs - transform_to_str(valid_df))

  no_valid_class_s = ug.query_uberon(" ".join(terms_s), ug.select_class)

  terms_s = set(terms_s) - no_valid_class_s

  for t in no_valid_class_s:
    logger.warning(f"Unrecognised UBERON/CL entity '{t}'")

  no_valid_class_o = ug.query_uberon(" ".join(terms_o), ug.select_class)

  terms_o = set(terms_o) - no_valid_class_o

  for t in no_valid_class_o:
    logger.warning(f"Unrecognised UBERON/CL entity '{t}'")

  no_valid_relation = ccf_tools_df[ccf_tools_df['s'].isin(terms_s) & ccf_tools_df['o'].isin(terms_o)]

  for _, r in no_valid_relation.iterrows():
    error_log = error_log.append(r)

  terms_ct, terms_as = split_terms(terms_ct_as)

  no_valid_ct_as = ccf_tools_df[ccf_tools_df['s'].isin(terms_ct) & ccf_tools_df['o'].isin(terms_as)]

  for _, r in no_valid_ct_as.iterrows():
    strict_log = strict_log.append(r)

  nb_validate = len(valid_subclass) + len(valid_po) + len(valid_overlaps) + len(valid_ct) + len(valid_df) 

  report_relationship = {
    'Table': '', 
    'number_of_relationships': [terms_pairs_start], 
    'percent_invalid_relationship': [round((len(terms_s)*100)/terms_pairs_start, 2)],
    'percent_indirect_relationship': [round((nb_indirect*100)/nb_validate, 2)]
  }

  annotations = ConjunctiveGraph()
  terms = list(terms)
  if len(terms) > 90:
    for chunk in chunks(terms, 90):
      annotations += ug.construct_annotation("\n".join(chunk))
  else:
    terms = "\n".join(terms)
    annotations = ug.construct_annotation(terms)
  return (pd.DataFrame.from_records(records), error_log, annotations, valid_error_log, report_relationship, strict_log)


def generate_ind_graph_template(ccf_tools_df :pd.DataFrame):
    seed = {'ID': 'ID', 'LABEL': 'A rdfs:label', 'TYPE': 'TYPE',
            'Parent': 'I ccf_part_of'}
    records = [seed]
    for i, r in ccf_tools_df.iterrows():
        rec = dict()
        rec['TYPE'] = 'owl:NamedIndividual'
        rec['ID'] = r['s']
        rec['LABEL'] = r['slabel']
        rec['Parent'] = r['o']
        records.append(rec)
    return pd.DataFrame.from_records(records)

def generate_vasculature_template(ccf_tools_df: pd.DataFrame):
    seed = {'SUBJECT': 'ID', 'OBJECT': "SC 'connected to' some %"}  # Work needed on relation
    records = [seed]
    for i, r in ccf_tools_df.iterrows():
        rec = dict()
        rec['SUBJECT'] = r['s']
        rec['OBJECT'] = r['o']
        records.append(rec)
    return pd.DataFrame.from_records(records)



