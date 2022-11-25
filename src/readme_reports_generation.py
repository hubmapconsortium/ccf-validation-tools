import argparse
from mdutils.fileutils.fileutils import MarkDownFile
from mdutils.mdutils import MdUtils

def generate_template(file_name):
  markers_dict = {}
  template = MdUtils(file_name=file_name, title='ASCT+B Validation Reports')

  template.new_header(level=1, title="Invalid terms", add_table_of_contents="n")

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
  markers_dict["indirects"] = m_ind

  template.new_header(level=2, title="Relationship AS has part CT", add_table_of_contents='y')

  m_hp = template.create_marker(text_marker="has_part")
  markers_dict["has_part"] = m_hp

  template.new_table_of_contents(table_title="Table of contents", depth=2)
  return template, markers_dict

def main(args):
  report, markers_dict = generate_template(f'{args.job}')

  report.file_data_text = report.place_text_using_marker(text=report.new_inline_link(f'../logs/{args.job}/{args.job}_AS_has_part_CT_log.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["has_part"])

  report.create_md_file()

  

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('job', help='job to download')
  # parser.add_argument('output_file', help='output file path')
  # parser.add_argument("old_version", help="is old version")

  args = parser.parse_args()
  main(args)