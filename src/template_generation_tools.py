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
    seed = {'ID': 'ID', 'Label': 'LABEL',
            'Parent_class': 'SC %', 'part_of': 'SC part_of some %',
            'OBO_Validated': '>A CCFH:IN_OBO',
            'validation_date': '>A dc:date'}
    ug = UberonGraph()
    records = [seed]
    for i, r in ccf_tools_df.iterrows():
        rec = dict()
        rec['ID'] = r['s']
        rec['Label'] = r['slabel']
        if ug.ask_uberon(r, ug.ask_uberon_subclassof, urls=False):
            rec['Parent_class'] = r['o']
            rec['OBO_Validated'] = True
            rec['validation_date'] = datetime.now().isoformat()
        elif ug.ask_uberon(r, ug.ask_uberon_po, urls=False):
            rec['part_of'] = r['o']
            rec['OBO_Validated'] = True
            rec['validation_date'] = datetime.now().isoformat()
        # TODO - add overlaps
        else:
            warnings.warn(invalid_relationship_report(r, ['is_a', 'part_of']))
        records.append(rec)
    return pd.DataFrame.from_records(records)


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

