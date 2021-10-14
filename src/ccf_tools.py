import pandas as pd
import rdflib
import re
import logging
import sys

from uberongraph_tools import UberonGraph

class DuplicateFilter(logging.Filter):
    def filter(self, record):
        current_log = record.msg
        if current_log != getattr(self, "last_log", None):
            self.last_log = current_log
            return True
        return False
def get_logger():
    logger = logging.getLogger('ASCT-b Tables Log')
    logger.setLevel(logging.WARN)  
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.WARN)  
    handler.setFormatter(formatter) 
    handler.addFilter(DuplicateFilter())             
    logger.addHandler(handler)
    return logger 

def parse_CCF_tsv(path):
    ccf_tsv = pd.read_csv(path, sep='\t', skipinitialspace=True)
    lookup = ccf_tsv[['ID', 'Label (indented)']]
    part_cols = ccf_tsv.drop(columns=['ID', 'Label (indented)'])
    out = pd.DataFrame(columns=['o', 's', 'olabel', 'slabel'])
    col_pairs = []
    for current, nekst in zip(part_cols.columns, part_cols.columns[1:]):
        col_pair = part_cols[[current, nekst]].drop_duplicates().dropna().rename(
            columns={current: 'olabel', nekst: 'slabel'})
        col_pairs.append(col_pair)
    out = pd.concat(col_pairs, ignore_index=True)
    fu = out.merge(lookup, left_on=['olabel'], right_on='Label (indented)').drop(columns=['Label (indented)']).rename(
        columns={'ID': 'o'})
    bar = fu.merge(lookup, left_on=['slabel'], right_on='Label (indented)').drop(columns=['Label (indented)']).rename(
        columns={'ID': 's'})
    return bar


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]



def parse_ASCTb(path):
    """Takes ASCT-b CSV table as input;
    Processes only AS (anatomy) and CT (cell type) columns.
    RETURN pandas dataframe of with columns ['o', 's', 'olabel', 'slabel', user_olabel, user_slabel]
    where each pair of adjacent columns => a subject-object pair for testing"""

    def is_valid_id(content):
        if re.match("(CL|UBERON)\:[0-9]+", content):
            return content
        else:
            get_logger().warning("Unrecognised cell content '%s'" % content)
            return False

    def is_valid_class(ug, entity):
        if ug.is_valid_class(ug.ask_uberon_class, entity):
            return True
        else:
            get_logger().warning("Unrecognised UBERON entity '%s'" % entity)
            return False


    asct_b_tab = pd.read_csv(path, sep=',', header=10)
    asct_b_tab.fillna('', inplace=True)
    ### Make a processed table with only ID columns - use this to generate tuples
    ### Drop all columns that do not have match regex .+/._+/ID$
    columns_to_drop = [c for c in asct_b_tab.columns if not (re.match("(AS)/.+/ID$", c))] # Excluding cell types for now
    asct_IDs_only = asct_b_tab.drop(columns=columns_to_drop)

    ### Make lookup of ID -> label and user_label
    # dict[ID] = { label: label, user_label: user_label }
    relevant_columns = [c for c in asct_b_tab.columns if re.match("(AS)/.+", c)]  # Excluding cell types for now
    
    ug = UberonGraph()
    lookup = dict()
    for i, r in asct_b_tab.iterrows():
        for chunk in chunks(relevant_columns, 3):
            for c in chunk:
                components = c.split('/')
                if len(components) == 2:
                    ul = r[c]
                if len(components) == 3:
                    if components[2] == 'LABEL':
                        l = r[c]
                    if components[2] == 'ID':
                        ID = r[c]
            #if is_valid_id(ID) and is_valid_class(ug, ID):
            if is_valid_id(ID):
                lookup[ID] = {"label": l, "user_label": ul}

    #   out = pd.DataFrame(columns=['o', 's', 'olabel', 'slabel', 'user_olabel', 'user_slabel'])
    dl = []

    for i, r in asct_IDs_only.iterrows():
        for current, nekst in zip(r, r[1:]):
            d = {}
            # if (is_valid_id(current) and is_valid_class(ug, current)) and (is_valid_id(nekst) and is_valid_class(ug, nekst)):
            if is_valid_id(current) and is_valid_id(nekst):
                d['s'] = nekst
                d['slabel'] = lookup[nekst]['label']
                d['user_slabel'] = lookup[nekst]["user_label"]
                d['o'] = current
                d['olabel'] = lookup[current]['label']
                d['user_olabel'] = lookup[current]["user_label"]
            if d:
                dl.append(d)
    out = pd.DataFrame.from_records(dl)
    return out.drop_duplicates()


def get_ccf_owl():
    g = rdflib.Graph()
    g.parse('http://purl.org/ccf/latest/ccf.owl')
    return g


def ccf_owl_2_part_rels():
    g = get_ccf_owl()
    ccf_po_query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX ccf: <https://purl.org/ccf/latest/ccf.owl#> 
SELECT DISTINCT ?o ?s ?olabel ?slabel
   WHERE { ?s ccf:ccf_part_of ?o . 
           ?o rdfs:label ?olabel .
           ?s rdfs:label ?slabel .
       FILTER(STRSTARTS(STR(?o), "http://purl.obolibrary.org/obo/UBERON_")) 
       FILTER(STRSTARTS(STR(?s), "http://purl.obolibrary.org/obo/UBERON_")) 
    }"""
    return g.query(ccf_po_query)


def invalid_relationship_report(row, relations):
    return "No valid relationshp between '%s ; %s' and '%s ; %s' (checked for: %s) " \
          "" % (row['slabel'], row['s'], row['olabel'], row['o'], str(relations))