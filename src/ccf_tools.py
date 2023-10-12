import pandas as pd
import re
import logging
import sys
import json
from datetime import datetime

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

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def parse_asctb(path):
    """Takes ASCT-b JSON as input;
    Processes only AS (anatomy) and CT (cell type) columns.
    RETURN pandas dataframe of with columns ['o', 's', 'olabel', 'slabel', user_olabel, user_slabel]
    where each pair of adjacent columns => a subject-object pair for testing"""

    def is_valid_id(log_dict, content, row_number, terms_set):
        if not re.match("(CL|UBERON|PCL)\:[0-9]+", content['id']):
            if (content['name'], row_number) not in terms_set:
              log_dict["no_valid_id"].append({"id": content['id'], "label": content['rdfs_label'], "user_label": content['name'], "row_number": row_number})
              terms_set.add((content['name'], row_number))
            #logger.warning(f"No valid ID provided for '{content['id']}', label: {content['rdfs_label']}, user_label: {content['name']}")
            return log_dict, terms_set
        return log_dict, terms_set
    def check_id(id):
      return re.match("(CL|UBERON|PCL)\:[0-9]+", id)
  
    def no_parent(log_dict, cell_type, row_number):
      if not check_id(cell_type["id"]):
        log_dict["no_parent"].append({"id": cell_type["id"], "label": cell_type["rdfs_label"], "user_label": cell_type["name"], "row_number": row_number})
      return log_dict

    asct_b_tab = json.load(open(path))
    as_invalid_terms = set()
    ct_invalid_terms = set()
    unique_terms = set()
    as_valid_terms = set()
    ct_valid_terms = set()
    rt = []
    rut = []
    log_dict = {"no_valid_id": [], "no_found_id": [], "diff_label": [], "no_parent": []}
    terms_set = set()

    #   out = pd.DataFrame(columns=['o', 's', 'olabel', 'slabel', 'user_olabel', 'user_slabel', 'row_number'])
    dl = []

    for row in asct_b_tab:
      # AS-AS RELATIONSHIP
      anatomical_structures = row['anatomical_structures']
      for current, next in zip(anatomical_structures, anatomical_structures[1:]):
        log_dict, terms_set = is_valid_id(log_dict, current, row["rowNumber"], terms_set)
        log_dict, terms_set = is_valid_id(log_dict, next, row["rowNumber"], terms_set)
        if current['id'] != '':
          unique_terms.add(current['id'])
        if next['id'] != '':
          unique_terms.add(next['id'])
        if check_id(current['id']) and check_id(next['id']):
          d = {}
          d['s'] = next['id']
          d['slabel'] = next['rdfs_label']
          d['user_slabel'] = next['name']
          d['o'] = current['id']
          d['olabel'] = current['rdfs_label']
          d['user_olabel'] = current['name']
          d['row_number'] = row['rowNumber']
          dl.append(d)
          as_valid_terms.add(current['id'])
          as_valid_terms.add(next['id'])
        else:
          if not check_id(current['id']) and current['rdfs_label'] != '':
            as_invalid_terms.add(current['rdfs_label'])
            unique_terms.add(current['rdfs_label'])
          elif not check_id(current['id']) and current['name'] != '':
            as_invalid_terms.add(current['name'])
            unique_terms.add(current['name'])

          if not check_id(next['id']) and next['rdfs_label'] != '':
            as_invalid_terms.add(next['rdfs_label'])
            unique_terms.add(next['rdfs_label'])
          elif not check_id(next['id']) and next['name'] != '':
            as_invalid_terms.add(next['name'])
            unique_terms.add(next['name'])
      
      # CT-CT RELATIONSHIP
      cell_types = row['cell_types']
      if len(cell_types) == 1:
        log_dict = no_parent(log_dict, cell_types[0], row["rowNumber"])
      for current, next in zip(cell_types, cell_types[1:]):
        log_dict, terms_set = is_valid_id(log_dict, current, row["rowNumber"], terms_set)
        log_dict, terms_set = is_valid_id(log_dict, next, row["rowNumber"], terms_set)
        if current['id'] != '':
          unique_terms.add(current['id'])
        if next['id'] != '':
          unique_terms.add(next['id'])
        if check_id(current['id']) and check_id(next['id']):
          d = {}
          d['row_number'] = row['rowNumber']
          d['s'] = next['id']
          d['slabel'] = next['rdfs_label']
          d['user_slabel'] = next['name']
          d['o'] = current['id']
          d['olabel'] = current['rdfs_label']
          d['user_olabel'] = current['name']
          dl.append(d)
          ct_valid_terms.add(current['id'])
          ct_valid_terms.add(next['id'])
        else:
          if not check_id(current['id']) and current['rdfs_label'] != '':
            ct_invalid_terms.add(current['rdfs_label'])
            unique_terms.add(current['rdfs_label'])
          elif not check_id(current['id']) and current['name'] != '':
            ct_invalid_terms.add(current['name'])
            unique_terms.add(current['name'])
          
          if not check_id(next['id']) and next['rdfs_label'] != '':
            ct_invalid_terms.add(next['rdfs_label'])
            unique_terms.add(next['rdfs_label'])
          elif not check_id(next['id']) and next['name'] != '':
            ct_invalid_terms.add(next['name'])
            unique_terms.add(next['name'])
            
          if not check_id(current['id']) and (check_id(next['id']) or not check_id(next['id'])):
            log_dict = no_parent(log_dict, next, row['rowNumber'])

      # CT-AS RELATIONSHIP
      if len(anatomical_structures) > 0 and len(cell_types) > 0:
        last_as = anatomical_structures[-1]
        if not check_id(last_as['id']) and len(anatomical_structures) > 1:
          last_as = anatomical_structures[-2]
        last_ct = cell_types[-1]
        if not check_id(last_ct['id']) and len(cell_types) > 1:
          last_ct = cell_types[-2]
        log_dict, terms_set = is_valid_id(log_dict, last_as, row["rowNumber"], terms_set)
        log_dict, terms_set = is_valid_id(log_dict, last_ct, row["rowNumber"], terms_set)
        if check_id(last_as['id']) and check_id(last_ct['id']):
          d = {}
          d['row_number'] = row['rowNumber']
          d['s'] = last_ct['id']
          d['slabel'] = last_ct['rdfs_label']
          d['user_slabel'] = last_ct['name']
          d['o'] = last_as['id']
          d['olabel'] = last_as['rdfs_label']
          d['user_olabel'] = last_as['name']
          dl.append(d)
          as_valid_terms.add(last_as['id'])
          ct_valid_terms.add(last_ct['id'])
          unique_terms.add(last_as['id'])
          unique_terms.add(last_ct['id'])
        else:
          if check_id(last_as['id']):
            as_valid_terms.add(last_as['id'])
          if check_id(last_ct['id']):
            ct_valid_terms.add(last_ct['id'])
          if not check_id(last_as['id']) and last_as['rdfs_label'] != '':
            as_invalid_terms.add(last_as['rdfs_label'])
            unique_terms.add(last_as['rdfs_label'])
          elif not check_id(last_as['id']) and last_as['name'] != '':
            as_invalid_terms.add(last_as['name'])
            unique_terms.add(last_as['name'])
          
          if not check_id(last_ct['id']) and last_ct['rdfs_label'] != '':
            ct_invalid_terms.add(last_ct['rdfs_label'])
            unique_terms.add(last_ct['rdfs_label'])
          elif not check_id(last_ct['id']) and last_ct['name'] != '':
            ct_invalid_terms.add(last_ct['name'])
            unique_terms.add(last_ct['name'])
      
      # NEW CL TERMS REPORT
      for cl in cell_types:
        if cl['id'] == '' and cl['name'] != '':
          r = {}
          r['Terminal AS/ID'] = last_as['id']
          r['Terminal AS/label'] = last_as['rdfs_label']
          r['Terminal AS/user_label'] = last_as['name']
          r['CL Name'] = cl['name']

          refs_id = [ref['id'] for ref in row['references'] if ref.get('id')]
          refs_doi = [ref['doi'] for ref in row['references'] if ref.get('doi')]
          r['References/ID'] = " ; ".join(refs_id)
          r['References/DOI'] = " ; ".join(refs_doi)
          rt.append(r)

      # NEW UBERON TERMS REPORT
      for i, term in enumerate(anatomical_structures):
        if term['id'] == '' and term['name'] != '':
          r = {}
          r['Upper AS'] = anatomical_structures[i-1]['name']
          r['Upper AS/label'] = anatomical_structures[i-1]['rdfs_label']
          r['Upper AS/ID'] = anatomical_structures[i-1]['id']
          r['AS Name'] = term['name']

          refs_id = [ref['id'] for ref in row['references'] if ref.get('id')]
          refs_doi = [ref['doi'] for ref in row['references'] if ref.get('doi')]
          r['References/ID'] = " ; ".join(refs_id)
          r['References/DOI'] = " ; ".join(refs_doi)
          rut.append(r)

        

    as_invalid_term_percent = 0
    ct_invalid_terms_percent = 0
    if len(as_valid_terms) + len(ct_invalid_terms) > 0:
      as_invalid_term_percent = round((len(as_invalid_terms)*100)/(len(as_valid_terms)+len(as_invalid_terms)), 2)
    if len(ct_valid_terms) + len(ct_invalid_terms) > 0:
      ct_invalid_terms_percent = round((len(ct_invalid_terms)*100)/(len(ct_valid_terms)+len(ct_invalid_terms)), 2)
    if len(unique_terms) > 0:
      invalid_terms_percent = round((len(as_invalid_terms)+len(ct_invalid_terms))*100/len(unique_terms), 2)

    report_terms = {
      'Table': '',
      'AS_valid_term_number': [len(as_valid_terms)], 
      'AS_invalid_term_number': [len(as_invalid_terms)], 
      'AS_invalid_term_percent': [as_invalid_term_percent],
      'CT_valid_term_number': [len(ct_valid_terms)],
      'CT_invalid_term_number': [len(ct_invalid_terms)],
      'CT_invalid_term_percent': [ct_invalid_terms_percent],
      'invalid_terms_percent': [invalid_terms_percent]    
    }


    out = pd.DataFrame.from_records(dl).drop_duplicates()
    new_terms = pd.DataFrame.from_records(rt).drop_duplicates()
    new_uberon_terms = pd.DataFrame.from_records(rut).drop_duplicates()
    return out, report_terms, new_terms, new_uberon_terms, log_dict

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

def add_rows(records, valid_as, valid_ct, pairs, relation, inverse=False):
  for s, o in pairs:
    rec = dict()
    if inverse:
      rec['ID'] = o
      rec[relation] = s
    else:
      rec['ID'] = s
      rec[relation] = o
    rec['OBO_Validated_' + relation] = True
    rec['validation_date_' + relation] = datetime.now().isoformat()
    records.append(rec)

    if 'UBERON' in s and 'UBERON' in o:
      valid_as.add((s,o))
    elif 'CL' in s and 'CL' in o:
      valid_ct.add((s,o))
  return records, valid_as, valid_ct
