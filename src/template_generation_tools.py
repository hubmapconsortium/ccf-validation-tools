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
  has_part_log = pd.DataFrame(columns=ccf_tools_df.columns)
  report_relationship = {
    'Table': '', 
    'number_of_AS-AS_relationships': [0], 
    'percent_invalid_AS-AS_relationship': [0],
    'percent_indirect_AS-AS_relationship': [0],
    'number_of_CT-CT_relationships': [0],
    'percent_invalid_CT-CT_relationship': [0],
    'percent_indirect_CT-CT_relationship': [0],
    'number_of_CT-AS_relationships': [0],
    'percent_invalid_CT-AS_relationship': [0]
  }
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
          'validation_date_df': '>A dc:date',
          'has_part': 'SC has_part some %',
          'OBO_Validated_hp': '>A CCFH:IN_OBO',
          'validation_date_hp': '>A dc:date'}

  seed_sub = {'ID': 'ID', 'in_subset': 'AI in_subset', 'present_in_taxon': 'AI present_in_taxon'}
  ug = UberonGraph()
  records = [seed]
  records_ub_sub = [seed_sub]
  records_cl_sub = [seed_sub]
  if ccf_tools_df.empty:
    return (pd.DataFrame.from_records(records), error_log, ConjunctiveGraph(), valid_error_log, strict_log, 
            has_part_log, pd.DataFrame.from_records(records_ub_sub), pd.DataFrame.from_records(records_cl_sub))

  terms = set()
  terms_pairs = set()
  terms_ct_as = set()  
  relation_as = set()
  relation_ct = set()
  nb_indirect_as = 0
  nb_indirect_ct = 0
  nb_valid_as = 0
  nb_valid_ct = 0
  nb_invalid_as = 0
  nb_invalid_ct = 0
  nb_invalid_ct_as = 0
  terms_ct_as_start = 0
 
  # Add declarations and labels for entity
  for i, r in ccf_tools_df.iterrows():
    records.append({'ID': r['s'], 'User_label': r['user_slabel']})
    records.append({'ID': r['o'], 'User_label': r['user_olabel']})

    if 'UBERON' in r['s']:
      records_ub_sub.append({'ID': r['s'], 'present_in_taxon': 'NCBITaxon:9606', 'in_subset': 'HubMAP_ASCT'})
    if 'UBERON' in r['o']:
      records_ub_sub.append({'ID': r['o'], 'present_in_taxon': 'NCBITaxon:9606', 'in_subset': 'HubMAP_ASCT'})
    if 'CL' in r['s']:
      records_cl_sub.append({'ID': r['s'], 'present_in_taxon': 'NCBITaxon:9606', 'in_subset': 'HubMAP_ASCT'})
    if 'CL' in r['o']:
      records_cl_sub.append({'ID': r['o'], 'present_in_taxon': 'NCBITaxon:9606', 'in_subset': 'HubMAP_ASCT'})

    if 'CL' in r['s'] and 'UBERON' in r['o']:
      terms_ct_as.add(f"({r['s']} {r['o']})")
    elif 'UBERON' in r['s'] and 'UBERON' in r['o']:
      relation_as.add(f"({r['s']} {r['o']})")
      terms_pairs.add(f"({r['s']} {r['o']})")
    elif 'CL' in r['s'] and 'CL' in r['o']:
      relation_ct.add(f"({r['s']} {r['o']})")
      terms_pairs.add(f"({r['s']} {r['o']})")

    terms.add(r['s'])
    terms.add(r['o'])

  terms_ct_as_start = len(terms_ct_as)    

  terms_labels = set()
  if len(terms) > 90:
    for chunk in chunks(list(terms), 90):
      terms_labels = terms_labels.union(ug.query_uberon(" ".join(chunk), ug.select_label))
  else:
    terms_labels = ug.query_uberon(" ".join(list(terms)), ug.select_label)

  for term, label in terms_labels:
    row = ccf_tools_df[(ccf_tools_df['s'] == term) | (ccf_tools_df['o'] == term)].iloc[0]
    if row['s'] == term and row['slabel'].lower() != label.lower():
      logger.warning(f"Different labels found for {term}. Uberongraph: {label} ; ASCT+b table: {row['slabel']}")
      ccf_tools_df.loc[(ccf_tools_df['s'] == term), 'slabel'] = label
      ccf_tools_df.loc[(ccf_tools_df['o'] == term), 'olabel'] = label
        
    if row['o'] == term and row['olabel'].lower() != label.lower():
      logger.warning(f"Different labels found for {term}. Uberongraph: {label} ; ASCT+b table: {row['olabel']}")
      ccf_tools_df.loc[(ccf_tools_df['o'] == term), 'olabel'] = label
      ccf_tools_df.loc[(ccf_tools_df['s'] == term), 'slabel'] = label
      
  # SUBCLASS CHECK
  valid_subclass = set()
  if len(terms_pairs) > 90:
    for chunk in chunks(list(terms_pairs), 90):
      valid_subclass = valid_subclass.union(ug.query_uberon(" ".join(chunk), ug.select_subclass))
  else:
    valid_subclass = ug.query_uberon(" ".join(list(terms_pairs)), ug.select_subclass)
  

  for s, o in valid_subclass:
    rec = dict()
    rec['ID'] = s
    rec['Parent_class'] = o
    rec['OBO_Validated_isa'] = True
    rec['validation_date_isa'] = datetime.now().isoformat()
    records.append(rec)

    if 'UBERON' in s and 'UBERON' in o:
      nb_valid_as += 1
    elif 'CL' in s and 'CL' in o:
      nb_valid_ct += 1

  # INDIRECT SUBCLASS CHECK
  terms_valid_subclass = transform_to_str(valid_subclass)

  valid_subclass_onto = ug.query_uberon(" ".join(list(terms_valid_subclass)), ug.select_subclass_ontology)

  terms_s, terms_o = split_terms(transform_to_str(valid_subclass - valid_subclass_onto))

  rows_nvso = ccf_tools_df[ccf_tools_df['s'].isin(terms_s) & ccf_tools_df['o'].isin(terms_o)]

  for _, r in rows_nvso.iterrows():
    valid_error_log = valid_error_log.append(r)

    if 'UBERON' in r['s'] and 'UBERON' in r['o']:
      nb_indirect_as += 1
    elif 'CL' in r['s'] and 'CL' in r['o']:
      nb_indirect_ct += 1
  
  terms_pairs = terms_pairs - terms_valid_subclass

  # PART OF CHECK
  valid_po = set()
  if len(terms_pairs) > 90:
    for chunk in chunks(list(terms_pairs), 90):
      valid_po = valid_po.union(ug.query_uberon(" ".join(chunk), ug.select_po))
  else:
    valid_po = ug.query_uberon(" ".join(list(terms_pairs)), ug.select_po)

  valid_ct_as_po = set()
  if len(terms_ct_as) > 90:
    for chunk in chunks(list(terms_ct_as), 90):
      valid_ct_as_po = valid_ct_as_po.union(ug.query_uberon(" ".join(chunk), ug.select_po))
  else:
    valid_ct_as_po = ug.query_uberon(" ".join(list(terms_ct_as)), ug.select_po)

  for s, o in valid_po.union(valid_ct_as_po):
    rec = dict()
    rec['ID'] = s
    rec['part_of'] = o
    rec['OBO_Validated_po'] = True
    rec['validation_date_po'] = datetime.now().isoformat()
    records.append(rec)

    if 'UBERON' in s and 'UBERON' in o:
      nb_valid_as += 1
    elif 'CL' in s and 'CL' in o:
      nb_valid_ct += 1

  # INDIRECT PART OF CHECK
  terms_valid_po = transform_to_str(valid_po)

  valid_po_nr = set()
  if len(terms_valid_po) > 90:
    for chunk in chunks(list(terms_valid_po), 90):
      valid_po_nr = valid_po_nr.union(ug.query_uberon(" ".join(chunk), ug.select_po_nonredundant))
  else:
    valid_po_nr = ug.query_uberon(" ".join(list(terms_valid_po)), ug.select_po_nonredundant)

  terms_s, terms_o = split_terms(transform_to_str(valid_po - valid_po_nr))

  rows_nvponr = ccf_tools_df[ccf_tools_df['s'].isin(terms_s) & ccf_tools_df['o'].isin(terms_o)]

  for _, r in rows_nvponr.iterrows():
    valid_error_log = valid_error_log.append(r)

    if 'UBERON' in r['s'] and 'UBERON' in r['o']:
      nb_indirect_as += 1
    elif 'CL' in r['s'] and 'CL' in r['o']:
      nb_indirect_ct += 1

  terms_pairs = terms_pairs - terms_valid_po

  terms_ct_as = terms_ct_as - transform_to_str(valid_ct_as_po)

  # OVERLAPS CHECK
  valid_overlaps = ug.query_uberon(" ".join(list(terms_pairs)), ug.select_overlaps)

  valid_ct_as_overlaps = set()
  if len(terms_ct_as) > 90:
    for chunk in chunks(list(terms_ct_as), 90):
      valid_ct_as_overlaps = valid_ct_as_overlaps.union(ug.query_uberon(" ".join(chunk), ug.select_overlaps))
  else:
    valid_ct_as_overlaps = ug.query_uberon(" ".join(list(terms_ct_as)), ug.select_overlaps)

  for s, o in valid_overlaps.union(valid_ct_as_overlaps):
    rec = dict()
    rec['ID'] = s
    rec['overlaps'] = o
    rec['OBO_Validated_overlaps'] = True
    rec['validation_date_overlaps'] = datetime.now().isoformat()
    records.append(rec)

    if 'UBERON' in s and 'UBERON' in o:
      nb_valid_as += 1
    elif 'CL' in s and 'CL' in o:
      nb_valid_ct += 1
  
  # INDIRECT OVERLAPS CHECK
  terms_valid_overlaps = transform_to_str(valid_overlaps)

  valid_o_nr = ug.query_uberon(" ".join(list(terms_valid_overlaps)), ug.select_overlaps_nonredundant)

  terms_s, terms_o = split_terms(transform_to_str(valid_overlaps - valid_o_nr))

  rows_nvonr = ccf_tools_df[ccf_tools_df['s'].isin(terms_s) & ccf_tools_df['o'].isin(terms_o)]

  for _, r in rows_nvonr.iterrows():
    valid_error_log = valid_error_log.append(r)

    if 'UBERON' in r['s'] and 'UBERON' in r['o']:
      nb_indirect_as += 1
    elif 'CL' in r['s'] and 'CL' in r['o']:
      nb_indirect_ct += 1

  terms_pairs = terms_pairs - transform_to_str(valid_overlaps)

  terms_ct_as = terms_ct_as - transform_to_str(valid_ct_as_overlaps)

  # STRICT CT-AS REPORT
  terms_ct, terms_as = split_terms(terms_ct_as)

  no_valid_ct_as = ccf_tools_df[ccf_tools_df['s'].isin(terms_ct) & ccf_tools_df['o'].isin(terms_as)]

  for _, r in no_valid_ct_as.iterrows():
    strict_log = strict_log.append(r)

  # CONNECTED TO CHECK
  valid_conn_to = ug.query_uberon(" ".join(list(terms_pairs)), ug.select_ct)

  for s, o in valid_conn_to:
    rec = dict()
    rec['ID'] = s
    rec['connected_to'] = o
    rec['OBO_Validated_ct'] = True
    rec['validation_date_ct'] = datetime.now().isoformat()
    records.append(rec)

    if 'UBERON' in s and 'UBERON' in o:
      nb_valid_as += 1
    elif 'CL' in s and 'CL' in o:
      nb_valid_ct += 1

  terms_pairs = terms_pairs - transform_to_str(valid_conn_to)

  # DEVELOPS FROM CHECK
  valid_dev_from = ug.query_uberon(" ".join(list(terms_pairs)), ug.select_develops_from)

  for s, o in valid_dev_from:
    rec = dict()
    rec['ID'] = s
    rec['develops_from'] = o
    rec['OBO_Validated_df'] = True
    rec['validation_date_df'] = datetime.now().isoformat()
    records.append(rec)

    if 'UBERON' in s and 'UBERON' in o:
      nb_valid_as += 1
    elif 'CL' in s and 'CL' in o:
      nb_valid_ct += 1

  # CT-AS SUBCLASS PART OF
  valid_subclass_ct_as_po = set()
  if len(terms_ct_as) > 90:
    for chunk in chunks(list(terms_ct_as), 90):
      valid_subclass_ct_as_po = valid_subclass_ct_as_po.union(ug.query_uberon(" ".join(chunk), ug.select_subclass_po))
  else:
    valid_subclass_ct_as_po = ug.query_uberon(" ".join(list(terms_ct_as)), ug.select_subclass_po)

  for s, o in valid_subclass_ct_as_po:
    rec = dict()
    rec['ID'] = s
    rec['part_of'] = o
    rec['OBO_Validated_po'] = True
    rec['validation_date_po'] = datetime.now().isoformat()
    records.append(rec)

  terms_ct_as = terms_ct_as - transform_to_str(valid_subclass_ct_as_po)

  # CT-AS SUBCLASS OVERLAPS
  valid_subclass_ct_as_o = set()
  if len(terms_ct_as) > 90:
    for chunk in chunks(list(terms_ct_as), 90):
      valid_subclass_ct_as_o = valid_subclass_ct_as_o.union(ug.query_uberon(" ".join(chunk), ug.select_subclass_o))
  else:
    valid_subclass_ct_as_o = ug.query_uberon(" ".join(list(terms_ct_as)), ug.select_subclass_o)

  for s, o in valid_subclass_ct_as_o:
    rec = dict()
    rec['ID'] = s
    rec['overlaps'] = o
    rec['OBO_Validated_overlaps'] = True
    rec['validation_date_overlaps'] = datetime.now().isoformat()
    records.append(rec)

  terms_ct_as = terms_ct_as - transform_to_str(valid_subclass_ct_as_o)

  # AS-CT HAS PART
  valid_has_part = set()
  if len(terms_ct_as) > 90:
    for chunk in chunks(list(terms_ct_as), 90):
      valid_has_part = valid_has_part.union(ug.query_uberon(" ".join(chunk), ug.select_has_part))
  else:
    valid_has_part = ug.query_uberon(" ".join(list(terms_ct_as)), ug.select_has_part)

  for s, o in valid_has_part:
    rec = dict()
    rec['ID'] = o
    rec['has_part'] = s
    rec['OBO_Validated_hp'] = True
    rec['validation_date_hp'] = datetime.now().isoformat()
    records.append(rec)

  terms_ct, terms_as = split_terms(transform_to_str(valid_has_part))

  has_part_report = ccf_tools_df[ccf_tools_df['s'].isin(terms_ct) & ccf_tools_df['o'].isin(terms_as)]

  for _, r in has_part_report.iterrows():
    has_part_log = has_part_log.append(r)

  terms_ct, terms_as = split_terms(terms_ct_as - transform_to_str(valid_has_part))

  terms_s, terms_o = split_terms(terms_pairs - transform_to_str(valid_dev_from))

  # ENTITY CHECK
  no_valid_class_s = ug.query_uberon(" ".join(terms_s), ug.select_class)
  no_valid_class_ct = ug.query_uberon(" ".join(terms_ct), ug.select_class)

  for t in no_valid_class_s.union(no_valid_class_ct):
    logger.warning(f"Unrecognised UBERON/CL entity '{t}'")

  no_valid_class_o = ug.query_uberon(" ".join(terms_o), ug.select_class)
  no_valid_class_as = ug.query_uberon(" ".join(terms_as), ug.select_class)

  for t in no_valid_class_o.union(no_valid_class_as):
    logger.warning(f"Unrecognised UBERON/CL entity '{t}'")

  terms_s = set(terms_s) - no_valid_class_s
  terms_ct = set(terms_ct) - no_valid_class_ct

  terms_s = list(terms_s.union(terms_ct))

  terms_o = set(terms_o) - no_valid_class_o
  terms_as = set(terms_as) - no_valid_class_as

  terms_o = terms_o.union(terms_as)

  no_valid_relation = ccf_tools_df[ccf_tools_df['s'].isin(terms_s) & ccf_tools_df['o'].isin(terms_o)].drop_duplicates()

  for _, r in no_valid_relation.iterrows():
    error_log = error_log.append(r)

    if 'UBERON' in r['s'] and 'UBERON' in r['o']:
      nb_invalid_as += 1
    elif 'CL' in r['s'] and 'CL' in r['o']:
      nb_invalid_ct += 1
    elif 'CL' in r['s'] and 'UBERON' in r['o']:
      nb_invalid_ct_as += 1

  nb_relation_as = len(relation_as)
  perc_inv_as = 0
  if nb_relation_as != 0: perc_inv_as = round((nb_invalid_as*100)/nb_relation_as, 2)

  perc_ind_as = 0
  if nb_valid_as != 0: perc_ind_as = round((nb_indirect_as*100)/nb_valid_as, 2)

  nb_relation_ct = len(relation_ct)
  perc_inv_ct = 0
  if nb_relation_ct != 0: perc_inv_ct = round((nb_invalid_ct*100)/nb_relation_ct, 2)
  
  perc_ind_ct = 0
  if nb_valid_ct != 0: perc_ind_ct = round((nb_indirect_ct*100)/nb_valid_ct, 2)

  perc_inv_ct_as = 0
  if terms_ct_as_start != 0: perc_inv_ct_as = round((nb_invalid_ct_as*100)/terms_ct_as_start, 2)

  report_relationship = {
    'Table': '', 
    'number_of_AS-AS_relationships': [nb_relation_as], 
    'percent_invalid_AS-AS_relationship': [perc_inv_as],
    'percent_indirect_AS-AS_relationship': [perc_ind_as],
    'number_of_CT-CT_relationships': [nb_relation_ct],
    'percent_invalid_CT-CT_relationship': [perc_inv_ct],
    'percent_indirect_CT-CT_relationship': [perc_ind_ct],
    'number_of_CT-AS_relationships': [terms_ct_as_start],
    'percent_invalid_CT-AS_relationship': [perc_inv_ct_as]
  }

  annotations = ConjunctiveGraph()
  terms = list(terms)
  if len(terms) > 30:
    for chunk in chunks(terms, 30):
      annotations += ug.construct_annotation("\n".join(chunk))
  else:
    terms = "\n".join(terms)
    annotations = ug.construct_annotation(terms)
  return (pd.DataFrame.from_records(records), error_log, annotations, valid_error_log, report_relationship, strict_log, 
          has_part_report, pd.DataFrame.from_records(records_ub_sub).drop_duplicates(), pd.DataFrame.from_records(records_cl_sub).drop_duplicates())


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

def generate_vasculature_template(ccf_tools_df):
  seed = {'SUBJECT': 'ID', 'OBJECT': "SC 'connected to' some %"} 
  records = [seed]
  ug = UberonGraph()

  as_as = ccf_tools_df[ccf_tools_df['s'].str.startswith('UBERON') & ccf_tools_df['o'].str.startswith('UBERON')]
  terms_pairs = set(f"({r['s']} {r['o']})" for _, r in as_as.iterrows())

  _, terms_pairs = ug.verify_relationship(terms_pairs, ug.select_subclass)
  
  _, terms_pairs = ug.verify_relationship(terms_pairs, ug.select_po)

  _, terms_pairs = ug.verify_relationship(terms_pairs, ug.select_overlaps)

  _, terms_pairs = ug.verify_relationship(terms_pairs, ug.select_ct)

  terms_as_sub, terms_as_obj = split_terms(terms_pairs)

  for i, sub in enumerate(terms_as_sub):
    rec = dict()
    rec['SUBJECT'] = sub
    rec['OBJECT'] = terms_as_obj[i]
    records.append(rec)
    
  return pd.DataFrame.from_records(records)



