import argparse, json
from datetime import datetime
from mdutils.fileutils.fileutils import MarkDownFile
from mdutils.mdutils import MdUtils

def generate_template_readme(file_name, table):
  date = datetime.today().strftime('%Y-%m-%d')

  markers_dict = {}
  template = MdUtils(file_name=file_name, title=f'ASCT+B Validation Reports for {table} ({date})')

  template.new_header(level=1, title="Invalid terms", add_table_of_contents='y')
  template.new_paragraph(text="These are the reports related to issues in the terms found in the ASCT+B table. We validate only [CL](https://www.ebi.ac.uk/ols/ontologies/cl), [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) and [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) terms.")
  
  template.new_header(level=2, title="Terms not found", add_table_of_contents='y')
  template.new_paragraph(text="This report provides a list of terms not found neither in UBERON nor in CL. Please remove these terms from the ASCT+B table.")
  template.new_line()
  template.new_line()

  m_nfound = template.create_marker(text_marker="nfound")
  markers_dict["nfound"] = m_nfound
  
  template.new_header(level=2, title="Typos or punctuation mistakes", add_table_of_contents='y')
  template.new_paragraph(text="This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.")
  template.new_line()
  template.new_line()

  m_typos = template.create_marker(text_marker="typos")
  markers_dict["typos"] = m_typos

  template.new_header(level=2, title="Different labels", add_table_of_contents='y')
  template.new_paragraph(text="This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.")
  template.new_paragraph(text="If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.")
  template.new_paragraph(text="If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.")
  template.new_line()
  template.new_line()

  m_label = template.create_marker(text_marker="diff_label")
  markers_dict["diff_label"] = m_label

  template.new_header(level=2, title="Blank ontology ID", add_table_of_contents='y')
  template.new_paragraph(text="This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).")
  template.new_line()
  template.new_line()
  

  m_blank = template.create_marker(text_marker="blank")
  markers_dict["blank"] = m_blank

  template.new_header(level=2, title="Terms from another ontology")
  template.new_paragraph(text="This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request.")
  template.new_line()
  template.new_line()
  
  m_ext = template.create_marker(text_marker="external")
  markers_dict["external"] = m_ext

  template.new_header(level=1, title="Relationship reports", add_table_of_contents='y')

  template.new_header(level=2, title="Relationship AS-AS report", add_table_of_contents='y')

  m_as = template.create_marker(text_marker="as-as_report")
  markers_dict["as-as_report"] = m_as

  template.new_header(level=2, title="Relationship CT-CT report", add_table_of_contents='y')

  m_ct = template.create_marker(text_marker="ct-ct_report")
  markers_dict["ct-ct_report"] = m_ct

  template.new_header(level=2, title="Relationship CT-AS report", add_table_of_contents='y')

  m_ctas = template.create_marker(text_marker="ct-as_report")
  markers_dict["ct-as_report"] = m_ctas

  template.new_header(level=1, title="New CL terms", add_table_of_contents='y')

  m_ncl = template.create_marker(text_marker="new_cl")
  markers_dict["new_cl"] = m_ncl

  template.new_header(level=1, title="New UBERON terms", add_table_of_contents='y')

  m_nub = template.create_marker(text_marker="new_uberon")
  markers_dict["new_uberon"] = m_nub

  template.new_header(level=1, title="Informative reports (valid relationships)", add_table_of_contents='y')

  template.new_header(level=2, title="Indirect relationship", add_table_of_contents='y')

  m_ind = template.create_marker(text_marker="indirect")
  markers_dict["indirect"] = m_ind

  template.new_header(level=2, title="Relationship AS has part CT", add_table_of_contents='y')

  m_hp = template.create_marker(text_marker="has_part")
  markers_dict["has_part"] = m_hp

  template.new_table_of_contents(table_title="Table of contents", depth=2)
  return template, markers_dict

def generate_invalid_terms_report(log_dict):

  terms_report = {"no_found_id": "", "typos": "", "diff_label": "", "blank": "", "external": ""}

  for issue in log_dict["no_valid_id"]:
    if issue["id"] == "":
      terms_report["blank"] += f'1. In row _{issue["row_number"]}_, no term id was found for the name/label _{issue["user_label"]}_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).\n\n'
    elif 'uberon' in issue["id"] or 'UBERON' in issue["id"] or 'cl' in issue["id"] or 'CL' in issue["id"]:
      terms_report["typos"] += f'1. In row _{issue["row_number"]}_, it might have a typo in the term _{issue["id"]}_. The term id should have this pattern: UBERON:NNNNNNN or CL:NNNNNNN or PCL:NNNNNNN. The ontology name in upper case. N is a number and it should have exact 7 numbers after the colon. Please change it in the ASCT+B table.\n\n'
    elif 'FMA' in issue["id"] or 'fma' in issue["id"] or 'LMHA' in issue["id"] or 'lmha' in issue["id"]:
      terms_report["external"] += f'1. In row _{issue["row_number"]}_, the term _{issue["id"]}_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.\n\n'
  
  if terms_report["blank"] == "":
    terms_report["blank"] = "- No issues found.\n\n"

  if terms_report["typos"] == "":
    terms_report["typos"] = "- No issues found.\n\n"

  if terms_report["external"] == "":
    terms_report["external"] = "- No issues found.\n\n"
  
  for issue in log_dict["no_found_id"]:
    terms_report["no_found_id"] += f'1. {issue["id"]}\n\n'

  if terms_report["no_found_id"] == "":
    terms_report["no_found_id"] = "- No issues found.\n\n"
  
  for issue in log_dict["diff_label"]:
    terms_report["diff_label"] += f'1. In row _{issue["rowNumber"]}_, the term _{add_base_iri(issue["id"])}_ has different name/label in the source ontology. The name/label in the ASCT+B table is _{issue["asct_label"]}_ and the one in the ontology is _{issue["label"]}_. For reference, the given name/label by SMEs is _{issue["user_label"]}_. Please correct it in the ASCT+B table.\n\n'
  
  if terms_report["diff_label"] == "":
    terms_report["diff_label"] = "- No issues found.\n\n"

  return terms_report

def add_base_iri(content):
  UBERON_BASE = "http://purl.obolibrary.org/obo/UBERON_"
  CL_BASE = "http://purl.obolibrary.org/obo/CL_"

  content_uri = content.replace("UBERON:", UBERON_BASE).replace("CL:", CL_BASE)

  return f'[{content}]({content_uri})'

def main(args):
  readme, markers_dict = generate_template_readme(args.output_file, args.table)
  
  terms_report = generate_invalid_terms_report(log)

  readme.file_data_text = readme.place_text_using_marker(text=terms_report["no_found_id"], marker=markers_dict["nfound"])

  readme.file_data_text = readme.place_text_using_marker(text=terms_report["typos"], marker=markers_dict["typos"])

  readme.file_data_text = readme.place_text_using_marker(text=terms_report["diff_label"], marker=markers_dict["diff_label"])

  readme.file_data_text = readme.place_text_using_marker(text=terms_report["blank"], marker=markers_dict["blank"])

  readme.file_data_text = readme.place_text_using_marker(text=terms_report["external"], marker=markers_dict["external"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'class_{args.table}_log.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["as-as_report"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'class_{args.table}_log.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["ct-ct_report"])
  
  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'{args.table}_AS_CT_strict_log.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["ct-as_report"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'new_cl_terms_{args.table}.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["new_cl"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'new_uberon_terms_{args.table}.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["new_uberon"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'class_{args.table}_indirect_log.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["indirect"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'{args.table}_AS_has_part_CT_log.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["has_part"])
  
  readme.create_md_file()

  

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('table', help='table to generate readme')
  parser.add_argument("log_dict", help="log in json")
  parser.add_argument('output_file', help='output file path')

  args = parser.parse_args()
  log = json.load(open(args.log_dict))
  args.log_dict = log
  main(args)