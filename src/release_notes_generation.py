from mdutils.mdutils import MdUtils
from uberongraph_tools import UberonGraph
#from download_resource import JOB_SHEET_GID_MAPPING

ug = UberonGraph()

ont_version = ug.add_prefix_ont(ug.query_uberon([], ug.select_ontology_version))

tables_version = []
with open('tables_version.txt', 'r', encoding='utf-8') as t:
  content_list = [line.rstrip('\n') for line in t]
  for table in content_list:
    tables_version.extend(table.split(","))

mdFile = MdUtils(file_name='../NOTES', title='Release Notes')

mdFile.new_header(3, "Ontology release", add_table_of_contents='n')

ontology_data = ["Ontology", "Version"]
ontology_data.extend(ont_version)

mdFile.new_table(columns=2, rows=3, text=ontology_data, text_align='center')

mdFile.new_header(3, "ASCT+b Tables", add_table_of_contents='n')

asct_data = ["Organ", "Version", "Date"]
asct_data.extend(tables_version)

mdFile.new_table(columns=3, rows=len(content_list)+1, text=asct_data)

mdFile.create_md_file()