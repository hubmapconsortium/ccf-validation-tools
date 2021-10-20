import pandas as pd
from rdflib.graph import ConjunctiveGraph
from uberongraph_tools import UberonGraph
from ccf_tools import invalid_relationship_report, chunks, transform_results
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
            'validation_date_ct': '>A dc:date'}
    ug = UberonGraph()
    records = [seed]
    terms = set()
    terms_pairs = set()
    # Add declarations and labels for entity
    for i, r in ccf_tools_df.iterrows():
        records.append({'ID': r['s'], 'Label': r['slabel'], 'User_label': r['user_slabel']})
        records.append({'ID': r['o'], 'Label': r['olabel'], 'User_label': r['user_olabel']})
        terms_pairs.add(f"({r['s']} {r['o']})")
        terms.add(r['s'])
        terms.add(r['o'])
    # TODO: get results with namespace and split in two values
    valid_subclass = transform_results(ug.query_uberon(" ".join(list(terms_pairs)), ug.select_subclass))

    for s, o in valid_subclass:
      rec = dict()
      rec['ID'] = s
      rec['Parent_class'] = o
      rec['OBO_Validated_isa'] = True
      rec['validation_date_isa'] = datetime.now().isoformat()
      records.append(rec)

    terms_pairs = terms_pairs - valid_subclass

    valid_po = transform_results(ug.query_uberon(" ".join(list(terms_pairs)), ug.select_po))

    for s, o in valid_po:
      rec = dict()
      rec['ID'] = s
      rec['part_of'] = o
      rec['OBO_Validated_po'] = True
      rec['validation_date_po'] = datetime.now().isoformat()
      records.append(rec)

    terms_pairs = terms_pairs - valid_po

    valid_overlaps = transform_results(ug.query_uberon(" ".join(list(terms_pairs)), ug.select_overlaps))

    for s, o in valid_overlaps:
      rec = dict()
      rec['ID'] = s
      rec['overlaps'] = o
      rec['OBO_Validated_overlaps'] = True
      rec['validation_date_overlaps'] = datetime.now().isoformat()
      records.append(rec)

    terms_pairs = terms_pairs - valid_overlaps

    valid_ct = transform_results(ug.query_uberon(" ".join(list(terms_pairs)), ug.select_ct))

    for s, o in valid_ct:
      rec = dict()
      rec['ID'] = s
      rec['connected_to'] = r['o']
      rec['OBO_Validated_ct'] = True
      rec['validation_date_ct'] = datetime.now().isoformat()
      records.append(rec)

    # TODO: split string to 2 values
    terms_pairs = terms_pairs - valid_ct

    no_valid_relation = ccf_tools_df[ccf_tools_df['s'].isin(list(terms_pairs))]

    for _, r in no_valid_relation.iterrows():
      uberon_slabel = ug.get_label_from_uberon(r['s'])
      uberon_olabel = ug.get_label_from_uberon(r['o'])

      if uberon_slabel != r['slabel']:
        logger.warning(f"Different labels found for {r['s']}. Uberongraph: {uberon_slabel} ; ASCT+b table: {r['slabel']}")

      if uberon_olabel != r['olabel']:
        logger.warning(f"Different labels found for {r['o']}. Uberongraph: {uberon_olabel} ; ASCT+b table: {r['olabel']}")

      r['slabel'] = uberon_slabel
      r['olabel'] = uberon_olabel
      error_log = error_log.append(r)

      
    annotations = ConjunctiveGraph()
    terms = list(terms)
    if len(terms) > 90:
      for chunk in chunks(terms, 90):
        annotations += ug.construct_annotation("\n".join(chunk))
    else:
      terms = "\n".join(terms)
      annotations = ug.construct_annotation(terms)
    return (pd.DataFrame.from_records(records), error_log, annotations)


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



