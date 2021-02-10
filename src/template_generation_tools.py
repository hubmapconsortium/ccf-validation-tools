import pandas as pd
from uberongraph_tools import UberonGraph
from ccf_tools import invalid_relationship_report
from datetime import datetime
import warnings

#    olabel            slabel               o               s
# 0  kidney      right kidney  UBERON:0002113  UBERON:0004539

def generate_class_graph_template(ccf_tools_df :pd.DataFrame):
    """Takes a ccf tools dataframe as input;
    Validates relationships against OBO;
    Adds relationships to template, tagged with OBO status"""
    error_log = pd.DataFrame(columns=ccf_tools_df.columns)
    seed = {'ID': 'ID', 'Label': 'LABEL',
            'Parent_class': 'SC %',
            'OBO_Validated_isa': '>A CCFH:IN_OBO',
            'validation_date_isa': '>A dc:date',
            'part_of': 'SC part_of some %',
            'OBO_Validated_po': '>A CCFH:IN_OBO',
            'validation_date_po': '>A dc:date'}
    ug = UberonGraph()
    records = [seed]
    # Add declarations and labels for entity
    for i, r in ccf_tools_df.iterrows():
        records.append({'ID': r['s'], 'Label': r['slabel']})
        records.append({'ID': r['o'], 'Label': r['olabel']})
    for i, r in ccf_tools_df.iterrows():
        rec = dict()
        rec['ID'] = r['s']
        if ug.ask_uberon(r, ug.ask_uberon_po, urls=False):
            rec['part_of'] = r['o']
            rec['OBO_Validated_po'] = True
            rec['validation_date_po'] = datetime.now().isoformat()
        elif ug.ask_uberon(r, ug.ask_uberon_subclassof, urls=False):
            rec['Parent_class'] = r['o']
            rec['OBO_Validated_isa'] = True
            rec['validation_date_isa'] = datetime.now().isoformat()
        # TODO - add overlaps
        else:
            warnings.warn(invalid_relationship_report(r, ['is_a', 'part_of']))
            error_log = error_log.append(r)
        records.append(rec)
    return (pd.DataFrame.from_records(records), error_log)


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



