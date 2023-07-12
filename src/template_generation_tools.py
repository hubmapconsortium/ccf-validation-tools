import pandas as pd
from rdflib.graph import ConjunctiveGraph
from uberongraph_tools import UberonGraph
from ccf_tools import chunks, split_terms, transform_to_str, add_rows
import logging

# logger = logging.getLogger('ASCT-b Tables Log')

#    olabel            slabel               o               s
# 0  kidney      right kidney  UBERON:0002113  UBERON:0004539

def generate_class_graph_template(ccf_tools_df :pd.DataFrame, log_dict: dict):
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
          'isa': 'SC %',
          'OBO_Validated_isa': '>A CCFH:IN_OBO',
          'validation_date_isa': '>A dc:date',
          'part_of': 'SC part_of some %',
          'OBO_Validated_part_of': '>A CCFH:IN_OBO',
          'validation_date_part_of': '>A dc:date',
          'overlaps': 'SC overlaps some %',
          'OBO_Validated_overlaps': '>A CCFH:IN_OBO',
          'validation_date_overlaps': '>A dc:date',
          'connected_to': 'SC connected_to some %',
          'OBO_Validated_connected_to': '>A CCFH:IN_OBO',
          'validation_date_connected_to': '>A dc:date',
          'develops_from': 'SC develops_from some %',
          'OBO_Validated_develops_from': '>A CCFH:IN_OBO',
          'validation_date_develops_from': '>A dc:date',
          'has_part': 'SC has_part some %',
          'OBO_Validated_has_part': '>A CCFH:IN_OBO',
          'validation_date_has_part': '>A dc:date',
          'located_in': 'SC located_in some %',
          'OBO_Validated_located_in': '>A CCFH:IN_OBO',
          'validation_date_located_in': '>A dc:date',
          'continuous_with': 'SC continuous_with some %',
          'OBO_Validated_continuous_with': '>A CCFH:IN_OBO',
          'validation_date_continuous_with': '>A dc:date'}

  seed_sub = {'ID': 'ID', 'in_subset': 'AI in_subset', 'present_in_taxon': 'AI present_in_taxon'}
  seed_no_valid = {'ID': 'ID', 'ccf_part_of': 'SC ccf_part_of some %', 'ccf_located_in': 'SC ccf_located_in some %'}
  image_report = []
  ug = UberonGraph()
  records = [seed]
  records_ub_sub = [seed_sub]
  records_cl_sub = [seed_sub]
  no_valid_records = [seed_no_valid]
  if ccf_tools_df.empty:
    return (pd.DataFrame.from_records(records), pd.DataFrame.from_records(no_valid_records), error_log, ConjunctiveGraph(), valid_error_log, report_relationship, strict_log, 
            has_part_log, pd.DataFrame.from_records(records_ub_sub), pd.DataFrame.from_records(records_cl_sub), pd.DataFrame(columns=['term', 'image_url']), ConjunctiveGraph(), log_dict)

  terms = set()
  all_as = set()
  all_ct = set()
  terms_pairs = set()
  terms_ct_as = set()  
  relation_as = set()
  relation_ct = set()
  indirect_as = set()
  indirect_ct = set()
  valid_as = set()
  valid_ct = set()
  invalid_as = set()
  invalid_ct = set()
  invalid_ct_as = set()
  terms_ct_as_start = 0
 
  for _, r in ccf_tools_df.iterrows():
    terms.add(r['s'])
    terms.add(r['o'])

  # ENTITY CHECK
  no_valid_class = ug.query_uberon(" ".join(terms), ug.select_class)

  del_index = []
  for t in no_valid_class:
    log_dict["no_found_id"].append({"id": t})
    #logger.warning(f"Unrecognised UBERON/CL/PCL entity '{t}'")
    del_index.extend(ccf_tools_df[(ccf_tools_df['s'] == t) | (ccf_tools_df['o'] == t)].index)
   
  # Drop rows with unrecognized UBERON/CL terms 
  ccf_tools_df = ccf_tools_df.drop(del_index)

  terms = set()
  
  # Add declarations and labels for entity
  for i, r in ccf_tools_df.iterrows():
    records.append({'ID': r['s'], 'User_label': r['user_slabel']})
    records.append({'ID': r['o'], 'User_label': r['user_olabel']})

    if 'UBERON' in r['s']:
      records_ub_sub.append({'ID': r['s'], 'present_in_taxon': 'NCBITaxon:9606', 'in_subset': 'human_reference_atlas'})
    if 'UBERON' in r['o']:
      records_ub_sub.append({'ID': r['o'], 'present_in_taxon': 'NCBITaxon:9606', 'in_subset': 'human_reference_atlas'})
    if 'CL' in r['s'] and not 'PCL' in r['s']:
      records_cl_sub.append({'ID': r['s'], 'present_in_taxon': 'NCBITaxon:9606', 'in_subset': 'human_reference_atlas'})
    if 'CL' in r['o'] and not 'PCL' in r['o']:
      records_cl_sub.append({'ID': r['o'], 'present_in_taxon': 'NCBITaxon:9606', 'in_subset': 'human_reference_atlas'})

    if ('CL' in r['s'] or 'PCL' in r['s']) and 'UBERON' in r['o']:
      terms_ct_as.add(f"({r['s']} {r['o']})")
      all_ct.add(r['s'])
      all_as.add(r['o'])
    elif 'UBERON' in r['s'] and 'UBERON' in r['o']:
      relation_as.add(f"({r['s']} {r['o']})")
      terms_pairs.add(f"({r['s']} {r['o']})")
      all_as.add(r['s'])
      all_as.add(r['o'])
    elif ('CL' in r['s'] or 'PCL' in r['s']) and ('CL' in r['o'] or 'PCL' in r['o']):
      relation_ct.add(f"({r['s']} {r['o']})")
      terms_pairs.add(f"({r['s']} {r['o']})")
      all_ct.add(r['s'])
      all_ct.add(r['o'])

    terms.add(r['s'])
    terms.add(r['o'])

  terms_ct_as_start = len(terms_ct_as)    

  # LABEL CHECK AND GET IMAGES ATTACHED TO EACH TERM
  terms_labels = set()
  terms_images = set()
  if len(terms) > 90:
    for chunk in chunks(list(terms), 90):
      terms_labels = terms_labels.union(ug.query_uberon(" ".join(chunk), ug.select_label))
      terms_images = terms_images.union(ug.query_uberon(" ".join(chunk), ug.select_image))
  else:
    terms_labels = ug.query_uberon(" ".join(list(terms)), ug.select_label)
    terms_images = ug.query_uberon(" ".join(list(terms)), ug.select_image)

  for term, label in terms_labels:
    row = ccf_tools_df[(ccf_tools_df['s'] == term) | (ccf_tools_df['o'] == term)].iloc[0]
    if row['s'] == term and row['slabel'].lower() != label.lower():
      log_dict["diff_label"].append({"id": term, "label": label, "asct_label": row['slabel'], "user_label": row['user_slabel'], "rowNumber": int(row['row_number'])})
      # logger.warning(f"Different labels found for {term}. Uberongraph: {label} ; ASCT+b table: {row['slabel']}")
      ccf_tools_df.loc[(ccf_tools_df['s'] == term), 'slabel'] = label
      ccf_tools_df.loc[(ccf_tools_df['o'] == term), 'olabel'] = label
        
    if row['o'] == term and row['olabel'].lower() != label.lower():
      log_dict["diff_label"].append({"id": term, "label": label, "asct_label": row['olabel'], "user_label": row['user_olabel'], "rowNumber": int(row['row_number'])})
      # logger.warning(f"Different labels found for {term}. Uberongraph: {label} ; ASCT+b table: {row['olabel']}")
      ccf_tools_df.loc[(ccf_tools_df['o'] == term), 'olabel'] = label
      ccf_tools_df.loc[(ccf_tools_df['s'] == term), 'slabel'] = label

  # CREATE IMAGE REPORT
  if len(terms_images) > 0:
    for term, image in terms_images:
      rep_im = dict()
      rep_im['term'] = term
      rep_im['image_url'] = image
      image_report.append(rep_im)
  else:
    image_report.append({'term': '', 'image_url': ''})
      
  # SUBCLASS CHECK
  valid_subclass, terms_pairs = ug.verify_relationship(terms_pairs, ug.select_subclass)
  valid_ct_as_subclass, terms_ct_as = ug.verify_relationship(terms_ct_as, ug.select_subclass)
  
  records, valid_as, valid_ct = add_rows(records, valid_as, valid_ct, valid_subclass.union(valid_ct_as_subclass), 'isa')

  # INDIRECT SUBCLASS CHECK
  valid_subclass_onto, _ = ug.verify_relationship(transform_to_str(valid_subclass), ug.select_subclass_ontology)

  terms_s, terms_o = split_terms(transform_to_str(valid_subclass - valid_subclass_onto))

  rows_nvso = ccf_tools_df[ccf_tools_df[["s","o"]].apply(tuple, 1).isin(zip(terms_s, terms_o))]

  # ADD RESULTS TO INDIRECT LOG
  valid_error_log = pd.concat([valid_error_log, rows_nvso])

  for _, r in rows_nvso.iterrows():
    if 'UBERON' in r['s'] and 'UBERON' in r['o']:
      indirect_as.add((r['s'], r['o']))
    elif ('CL' in r['s'] or 'PCL' in r['s']) and ('CL' in r['o'] or 'PCL' in r['o']):
      indirect_ct.add((r['s'], r['o']))

  # PART OF CHECK
  valid_po, terms_pairs = ug.verify_relationship(terms_pairs, ug.select_po)
  valid_ct_as_po, terms_ct_as = ug.verify_relationship(terms_ct_as, ug.select_po)

  records, valid_as, valid_ct = add_rows(records, valid_as, valid_ct, valid_po.union(valid_ct_as_po), 'part_of')

  # INDIRECT PART OF CHECK
  terms_valid_po = transform_to_str(valid_po)

  valid_po_nr, _ = ug.verify_relationship(terms_valid_po, ug.select_po_nonredundant)
  
  terms_s, terms_o = split_terms(transform_to_str(valid_po - valid_po_nr))

  rows_nvponr = ccf_tools_df[ccf_tools_df[["s","o"]].apply(tuple, 1).isin(zip(terms_s, terms_o))]

  # ADD RESULTS TO INDIRECT LOG
  valid_error_log = pd.concat([valid_error_log, rows_nvponr])

  for _, r in rows_nvponr.iterrows():
    if 'UBERON' in r['s'] and 'UBERON' in r['o']:
      indirect_as.add((r['s'], r['o']))
    elif ('CL' in r['s'] or 'PCL' in r['s']) and ('CL' in r['o'] or 'PCL' in r['o']):
      indirect_ct.add((r['s'], r['o']))

  # OVERLAPS CHECK
  valid_overlaps, terms_pairs = ug.verify_relationship(terms_pairs, ug.select_overlaps)
  valid_ct_as_overlaps, terms_ct_as = ug.verify_relationship(terms_ct_as, ug.select_overlaps)

  records, valid_as, valid_ct = add_rows(records, valid_as, valid_ct, valid_overlaps.union(valid_ct_as_overlaps), 'overlaps')
  
  # INDIRECT OVERLAPS CHECK
  valid_o_nr, _ = ug.verify_relationship(transform_to_str(valid_overlaps), ug.select_overlaps_nonredundant)

  terms_s, terms_o = split_terms(transform_to_str(valid_overlaps - valid_o_nr))

  rows_nvonr = ccf_tools_df[ccf_tools_df[["s","o"]].apply(tuple, 1).isin(zip(terms_s, terms_o))]

  # ADD RESULTS TO INDIRECT LOG
  valid_error_log = pd.concat([valid_error_log, rows_nvonr])

  for _, r in rows_nvonr.iterrows():
    if 'UBERON' in r['s'] and 'UBERON' in r['o']:
      indirect_as.add((r['s'], r['o']))
    elif ('CL' in r['s'] or 'PCL' in r['s']) and ('CL' in r['o'] or 'PCL' in r['o']):
      indirect_ct.add((r['s'], r['o']))

  # LOCATED IN CHECK
  valid_ct_as_locatedin, terms_ct_as = ug.verify_relationship(terms_ct_as, ug.select_located_in)
  records, valid_as, valid_ct = add_rows(records, valid_as, valid_ct, valid_ct_as_locatedin, 'located_in')

  terms_ct_as = terms_ct_as - transform_to_str(valid_ct_as_locatedin)

  # CONNECTED TO CHECK
  valid_conn_to, terms_pairs = ug.verify_relationship(terms_pairs, ug.select_ct)
  valid_ct_as_conn_to, terms_ct_as = ug.verify_relationship(terms_ct_as, ug.select_ct)

  records, valid_as, valid_ct = add_rows(records, valid_as, valid_ct, valid_conn_to.union(valid_ct_as_conn_to), 'connected_to')

  # CONTINUOUS WITH CHECK
  valid_cont_with, terms_pairs = ug.verify_relationship(terms_pairs, ug.select_continuous_with)

  records, valid_as, valid_ct = add_rows(records, valid_as, valid_ct, valid_cont_with, 'continuous_with')

  # STRICT CT-AS REPORT
  terms_s, terms_o = split_terms(terms_ct_as)
  
  no_valid_ct_as = ccf_tools_df[ccf_tools_df[["s","o"]].apply(tuple, 1).isin(zip(terms_s, terms_o))]

  strict_log = pd.concat([strict_log,no_valid_ct_as])

  # DEVELOPS FROM CHECK
  valid_dev_from, terms_pairs = ug.verify_relationship(terms_pairs, ug.select_develops_from)
  records, valid_as, valid_ct = add_rows(records, valid_as, valid_ct, valid_dev_from, 'develops_from')

  # AS-CT HAS PART
  valid_has_part, terms_ct_as = ug.verify_relationship(terms_ct_as, ug.select_has_part)
  records, valid_as, valid_ct = add_rows(records, valid_as, valid_ct, valid_has_part, 'has_part', True)
  
  # AS-AS HAS PART
  valid_as_as_has_part, terms_pairs = ug.verify_relationship(terms_pairs, ug.select_has_part)
  records, valid_as, valid_ct = add_rows(records, valid_as, valid_ct, valid_as_as_has_part, 'has_part')

  # CT-AS SUBCLASS PART OF
  valid_subclass_ct_as_po, terms_ct_as = ug.verify_relationship(terms_ct_as, ug.select_subclass_po)
  records, valid_as, valid_ct = add_rows(records, valid_as, valid_ct, valid_subclass_ct_as_po, 'has_part', True)

  terms_s, terms_o = split_terms(transform_to_str(valid_has_part.union(valid_subclass_ct_as_po).union(valid_as_as_has_part)))

  has_part_report = ccf_tools_df[ccf_tools_df[["s","o"]].apply(tuple, 1).isin(zip(terms_s, terms_o))]

  has_part_log = pd.concat([has_part_log,has_part_report])

  terms_ct, terms_as = split_terms(terms_ct_as - transform_to_str(valid_has_part.union(valid_subclass_ct_as_po)))

  terms_s, terms_o = split_terms(terms_pairs - transform_to_str(valid_dev_from))

  terms_as_d = set(t for t in terms_s if "UBERON" in t)
  terms_ct_d = set(t for t in terms_s if "CL" in t)

  sec_graph = ug.get_suggestion_graph(all_as, terms_as_d, all_ct, terms_ct, terms_ct_d)

  terms_set = zip(terms_ct + terms_s, terms_as + terms_o)

  # NOT VALID LOG
  no_valid_relation = ccf_tools_df[ccf_tools_df[["s","o"]].apply(tuple, 1).isin(terms_set)]

  for _, r in no_valid_relation.iterrows():
    if 'UBERON' in r['s'] and 'UBERON' in r['o']:
      invalid_as.add((r['s'], r['o']))
      no_v_rec = dict()
      no_v_rec['ID'] = r['s']
      no_v_rec['ccf_part_of'] = r['o']
      no_valid_records.append(no_v_rec)
    elif 'CL' in r['s'] and 'CL' in r['o']:
      invalid_ct.add((r['s'], r['o']))
      no_v_rec = dict()
      no_v_rec['ID'] = r['s']
      no_v_rec['ccf_part_of'] = r['o']
      no_valid_records.append(no_v_rec)
    elif 'CL' in r['s'] and 'UBERON' in r['o']:
      invalid_ct_as.add((r['s'], r['o']))
      no_v_rec = dict()
      no_v_rec['ID'] = r['s']
      no_v_rec['ccf_located_in'] = r['o']
      no_valid_records.append(no_v_rec)
  
  error_log = pd.concat([error_log,no_valid_relation])

  # ADD DELTA IC TO NOT VALIDATED REPORT
  error_log["deltaIC"] = None
  all_terms = set(error_log["s"]).union(set(error_log["o"]))

  norm_ic_list = ug.query_uberon(" ".join(all_terms), ug.select_normalized_ic)
  
  for _, r in error_log.iterrows():
    subj_ic = norm_ic_term(norm_ic_list, r["s"])
    obj_ic = norm_ic_term(norm_ic_list, r["o"])
    if subj_ic < obj_ic:
      r["deltaIC"] = abs(subj_ic - obj_ic)
    

  # RELATIONSHIP REPORT
  nb_relation_as = len(relation_as)
  perc_inv_as = 0
  if nb_relation_as != 0: perc_inv_as = round((len(invalid_as)*100)/nb_relation_as, 2)

  perc_ind_as = 0
  if len(valid_as) != 0: perc_ind_as = round((len(indirect_as)*100)/len(valid_as), 2)

  nb_relation_ct = len(relation_ct)
  perc_inv_ct = 0
  if nb_relation_ct != 0: perc_inv_ct = round((len(invalid_ct)*100)/nb_relation_ct, 2)
  
  perc_ind_ct = 0
  if len(valid_ct) != 0: perc_ind_ct = round((len(indirect_ct)*100)/len(valid_ct), 2)

  perc_inv_ct_as = 0
  if terms_ct_as_start != 0: perc_inv_ct_as = round((len(invalid_ct_as)*100)/terms_ct_as_start, 2)

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

  # ANNOTATION 
  annotations = ug.get_annotations(terms)
  

  return (pd.DataFrame.from_records(records), pd.DataFrame.from_records(no_valid_records), error_log.sort_values('deltaIC', ascending=False), annotations, valid_error_log.sort_values('s'), report_relationship, strict_log.sort_values('s'), 
          has_part_report.sort_values('s'), pd.DataFrame.from_records(records_ub_sub).drop_duplicates(), pd.DataFrame.from_records(records_cl_sub).drop_duplicates(), pd.DataFrame.from_records(image_report).sort_values('term'), sec_graph, log_dict)

def norm_ic_term(normalized_ic_list, term):
  for t, ic in normalized_ic_list:
    if t == term:
      return float(ic)

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
  seed = {'SUBJECT': 'ID', 'OBJECT': "SC 'connected_to' some %", 'in_subset': 'AI in_subset'} 
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
    rec['in_subset'] = 'human_reference_atlas'
    records.append(rec)
    
  return pd.DataFrame.from_records(records).sort_values(by=['SUBJECT'])



