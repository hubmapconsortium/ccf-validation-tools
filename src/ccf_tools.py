import pandas as pd
import rdflib
import re
import logging
import sys
import json

from uberongraph_tools import UberonGraph

class DuplicateFilter(logging.Filter):
    def filter(self, record):
        current_log = record.msg
        if current_log != getattr(self, "last_log", None):
            self.last_log = current_log
            return True
        return False

logger = logging.getLogger('ASCT-b Tables Log')
logger.setLevel(logging.WARN)  
formatter = logging.Formatter('%(levelname)s - %(message)s')
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.WARN)  
handler.setFormatter(formatter) 
handler.addFilter(DuplicateFilter())             
logger.addHandler(handler)
  

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



def parse_asctb(path):
    """Takes ASCT-b JSON as input;
    Processes only AS (anatomy) and CT (cell type) columns.
    RETURN pandas dataframe of with columns ['o', 's', 'olabel', 'slabel', user_olabel, user_slabel]
    where each pair of adjacent columns => a subject-object pair for testing"""

    def is_valid_id(content):
        if re.match("(CL|UBERON)\:[0-9]+", content['id']):
            return content
        else:
            logger.warning(f"No valid ID provided for '{content['id']}', label: {content['name']}, user_label: {content['rdfs_label']}")
            return False
    def check_id(id):
      return re.match("(CL|UBERON)\:[0-9]+", id)

    asct_b_tab = json.load(open(path))
    as_invalid_terms = set()
    ct_invalid_terms = set()
    unique_terms = set()
    as_valid_terms = set()
    ct_valid_terms = set()
    rt = []

    #   out = pd.DataFrame(columns=['o', 's', 'olabel', 'slabel', 'user_olabel', 'user_slabel'])
    dl = []

    for row in asct_b_tab:
      # AS-AS RELATIONSHIP
      anatomical_structures = row['anatomical_structures']
      for current, next in zip(anatomical_structures, anatomical_structures[1:]):
        unique_terms.add(current['id'])
        unique_terms.add(next['id'])
        if is_valid_id(current) and is_valid_id(next):
          d = {}
          d['s'] = next['id']
          d['slabel'] = next['name']
          d['user_slabel'] = next['rdfs_label']
          d['o'] = current['id']
          d['olabel'] = current['name']
          d['user_olabel'] = current['rdfs_label']
          dl.append(d)
          as_valid_terms.add(current['id'])
          as_valid_terms.add(next['id'])
        else:
          if not check_id(current['id']) and current['rdfs_label'] != '':
            as_invalid_terms.add(current['rdfs_label'])
          elif not check_id(current['id']) and current['name']:
            as_invalid_terms.add(current['name'])
          elif not check_id(next['id']) and next['rdfs_label'] != '':
            as_invalid_terms.add(next['rdfs_label'])
          elif not check_id(next['id']) and next['name'] != '':
            as_invalid_terms.add(next['name'])
      
      # CT-CT RELATIONSHIP
      cell_types = row['cell_types']
      for current, next in zip(cell_types, cell_types[1:]):
        unique_terms.add(current['id'])
        unique_terms.add(next['id'])
        if is_valid_id(current) and is_valid_id(next):
          d = {}
          d['s'] = next['id']
          d['slabel'] = next['name']
          d['user_slabel'] = next['rdfs_label']
          d['o'] = current['id']
          d['olabel'] = current['name']
          d['user_olabel'] = current['rdfs_label']
          dl.append(d)
          ct_valid_terms.add(current['id'])
          ct_valid_terms.add(next['id'])
        else:
          if not check_id(current['id']) and current['rdfs_label'] != '':
            ct_invalid_terms.add(current['rdfs_label'])
          elif not check_id(current['id']) and current['name'] != '':
            ct_invalid_terms.add(current['name'])
          elif not check_id(next['id']) and next['rdfs_label'] != '':
            ct_invalid_terms.add(next['rdfs_label'])
          elif not check_id(next['id']) and next['name'] != '':
            ct_invalid_terms.add(next['name'])

      # CT-AS RELATIONSHIP
      if len(cell_types) > 0:
        last_as = anatomical_structures[-1]
        if not check_id(last_as['id']) and len(anatomical_structures) > 1:
          last_as = anatomical_structures[-2]
        last_ct = cell_types[-1]
        if not check_id(last_ct['id']) and len(cell_types) > 1:
          last_ct = cell_types[-2]
        if is_valid_id(last_as) and is_valid_id(last_ct):
          d = {}
          d['s'] = last_ct['id']
          d['slabel'] = last_ct['name']
          d['user_slabel'] = last_ct['rdfs_label']
          d['o'] = last_as['id']
          d['olabel'] = last_as['name']
          d['user_olabel'] = last_as['rdfs_label']
          dl.append(d)
          as_valid_terms.add(last_as['id'])
          ct_valid_terms.add(last_ct['id'])
        else:
          if not check_id(last_as['id']) and last_as['rdfs_label'] != '':
            as_invalid_terms.add(last_as['rdfs_label'])
            unique_terms.add(last_as['rdfs_label'])
          elif not check_id(last_as['id']) and last_as['name'] != '':
            as_invalid_terms.add(last_as['name'])
          elif not check_id(last_ct['id']) and last_ct['rdfs_label'] != '':
            ct_invalid_terms.add(last_ct['rdfs_label'])
            unique_terms.add(last_ct['rdfs_label'])
          elif not check_id(last_ct['id']) and last_ct['name'] != '':
            ct_invalid_terms.add(last_ct['name'])
            unique_terms.add(last_ct['name'])
      
        # REPORT OF NEW CL TERMS
        for cl in cell_types:
          if cl['id'] == '' and cl['name'] != '':
            r = {}
            r['Terminal AS/ID'] = last_as['id']
            r['Terminal AS/label'] = last_as['name']
            r['Terminal AS/user_label'] = last_as['rdfs_label']
            r['CL Name'] = cl['name']

            refs_id = [ref['id'] for ref in row['references']]
            refs_doi = [ref['doi'] for ref in row['references'] if ref.get('doi')]
            r['References/ID'] = " ; ".join(refs_id)
            r['References/DOI'] = " ; ".join(refs_doi)
            rt.append(r)

    as_invalid_term_percent = round((len(as_invalid_terms)*100)/len(unique_terms), 2)
    ct_invalid_terms_percent = round((len(ct_invalid_terms)*100)/len(unique_terms), 2)

    report_terms = {
      'Table': '',
      'AS_valid_term_number': [len(as_valid_terms)], 
      'AS_invalid_term_number': [len(as_invalid_terms)], 
      'AS_invalid_term_percent': [as_invalid_term_percent],
      'CT_valid_term_number': [len(ct_valid_terms)],
      'CT_invalid_term_number': [len(ct_invalid_terms)],
      'CT_invalid_term_percent': [ct_invalid_terms_percent]    
    }


    out = pd.DataFrame.from_records(dl).drop_duplicates()
    new_terms = pd.DataFrame.from_records(rt).drop_duplicates()
    return out, report_terms, new_terms


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

def transform_to_str(list):
    terms_pairs = set()

    for s, o in list:
      terms_pairs.add(f"({s} {o})")
    return terms_pairs

def split_terms(list):
    terms_s = []
    terms_o = []

    for pairs in list:
      s, o = pairs.split(" ")
      terms_s.append(s[1:])
      terms_o.append(o[:-1])

    return terms_s, terms_o
