import pandas as pd
from rdflib.graph import ConjunctiveGraph
from uberongraph_tools import UberonGraph
from ccf_tools import invalid_relationship_report, chunks
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
    # Add declarations and labels for entity
    for i, r in ccf_tools_df.iterrows():
        records.append({'ID': r['s'], 'Label': r['slabel'], 'User_label': r['user_slabel']})
        records.append({'ID': r['o'], 'Label': r['olabel'], 'User_label': r['user_olabel']})
    for i, r in ccf_tools_df.iterrows():
        rec = dict()
        rec['ID'] = r['s']
        terms.add(r['s'])
        terms.add(r['o'])
        if ug.ask_uberon(r, ug.ask_uberon_subclassof, urls=False):
            rec['Parent_class'] = r['o']
            rec['OBO_Validated_isa'] = True
            rec['validation_date_isa'] = datetime.now().isoformat()
        elif ug.ask_uberon(r, ug.ask_uberon_po, urls=False):
            rec['part_of'] = r['o']
            rec['OBO_Validated_po'] = True
            rec['validation_date_po'] = datetime.now().isoformat()
        elif ug.ask_uberon(r, ug.ask_uberon_overlaps, urls=False):
            rec['overlaps'] = r['o']
            rec['OBO_Validated_overlaps'] = True
            rec['validation_date_overlaps'] = datetime.now().isoformat()
        elif ug.ask_uberon(r, ug.ask_uberon_ct, urls=False):
            rec['connected_to'] = r['o']
            rec['OBO_Validated_ct'] = True
            rec['validation_date_ct'] = datetime.now().isoformat()
        else:
            uberon_slabel = ug.get_label_from_uberon(r['s'])
            uberon_olabel = ug.get_label_from_uberon(r['o'])

            if uberon_slabel != r['slabel']:
              logger.warning(f"Different labels found for {r['s']}. Uberongraph: {uberon_slabel} ; ASCT+b table: {r['slabel']}")

            if uberon_olabel != r['olabel']:
              logger.warning(f"Different labels found for {r['o']}. Uberongraph: {uberon_olabel} ; ASCT+b table: {r['olabel']}")

            r['slabel'] = uberon_slabel
            r['olabel'] = uberon_olabel
            error_log = error_log.append(r)

        records.append(rec)
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



