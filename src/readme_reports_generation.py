import argparse
from mdutils.fileutils.fileutils import MarkDownFile
from mdutils.mdutils import MdUtils

def generate_template_readme(file_name):
  markers_dict = {}
  template = MdUtils(file_name=file_name, title='ASCT+B Validation Reports')

  template.new_header(level=1, title="Invalid terms", add_table_of_contents='y')

  template.new_paragraph(text="These are the reports related to issues in the terms found in the ASCT+B table. We validate only [CL](https://www.ebi.ac.uk/ols/ontologies/cl) and [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) terms.")

  template.new_header(level=2, title="Typos or punctuation mistakes", add_table_of_contents='y')

  template.new_paragraph(text="This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.")

  template.new_header(level=2, title="Blank ontology ID", add_table_of_contents='y')

  template.new_paragraph(text="This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index)")

  template.new_header(level=2, title="Different labels", add_table_of_contents='y')

  template.new_paragraph(text="This report provides a list of terms having different names found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name in the column AS/N/LABEL or CT/N/LABEL. ")

  template.new_header(level=2, title="Foundational models of anatomy ontology")

  template.new_paragraph(text="This report provides a list of foundational models of anatomy ontology IDs provided when an adequate term is not found in Uberon. You can also request cross-database requests the same way a new term requests.")

  m_inv = template.create_marker(text_marker="invalid_terms")
  markers_dict["invalid_terms"] = m_inv

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
  return True

def add_base(content):
  UBERON_BASE = "http://purl.obolibrary.org/obo/UBERON_"
  CL_BASE = "http://purl.obolibrary.org/obo/CL_"

  return content.replace("UBERON:", UBERON_BASE).replace("CL:", CL_BASE)

def main(args):
  readme, markers_dict = generate_template_readme(f'{args.output_file}')

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'../logs/{args.table}/{args.table}_AS__CT_strict_log.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["ct-as_report"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'../logs/{args.table}/class_{args.table}_indirect_log.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["indirect"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'../logs/{args.table}/{args.table}_AS_has_part_CT_log.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["has_part"])
  
  readme.create_md_file()

  

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('table', help='table to generate readme')
  parser.add_argument("log_dict", help="log in json")
  parser.add_argument('output_file', help='output file path')

  args = parser.parse_args()
  main(args)