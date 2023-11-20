import argparse, json
from datetime import datetime
from mdutils.fileutils.fileutils import MarkDownFile
from mdutils.mdutils import MdUtils
from tabulate import tabulate
import pandas as pd

from download_resource import get_sheet_gid

def generate_template_readme(file_name, table):
  date = datetime.today().strftime('%Y-%m-%d')

  markers_dict = {}
  template = MdUtils(file_name=file_name, title=f'ASCT+B Validation Reports for {table} ({date})')

  template.new_header(level=1, title="Invalid terms", add_table_of_contents='y')
  template.new_paragraph(text="These are the reports related to issues in the terms found in the ASCT+B table. We validate only [CL](https://www.ebi.ac.uk/ols4/ontologies/cl), [UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon) and [PCL](https://www.ebi.ac.uk/ols4/ontologies/pcl) terms.")
  
  template.new_header(level=2, title="Terms not found", add_table_of_contents='y')
  template.new_paragraph(text="This report provides a list of terms not found neither in UBERON nor in CL. Please remove these terms from the ASCT+B table - disconsider this message if a term was recently added to the ontology.")
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
  template.new_paragraph(text="This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols4/index).")
  template.new_paragraph(text="You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.")
  template.new_line()
  template.new_line()
  
  m_blank = template.create_marker(text_marker="blank")
  markers_dict["blank"] = m_blank
  
  template.new_header(level=2, title="Blank ontology ID missing parent", add_table_of_contents="y")
  template.new_paragraph(text="This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.")
  template.new_line()
  template.new_line()
  
  m_parent = template.create_marker(text_marker="no_parent")
  markers_dict["no_parent"] = m_parent

  template.new_header(level=2, title="Terms from another ontology")
  template.new_paragraph(text="This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Same case for Anatomic Ontology for Human Lung Maturation (LMHA) and Interlex IDs (ILX) from Stimulating Peripheral Activity to Relieve Conditions (SPARC). You can request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols4/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols4/ontologies/pcl).")
  template.new_line()
  template.new_line()
  
  m_ext = template.create_marker(text_marker="external")
  markers_dict["external"] = m_ext

  template.new_header(level=1, title="Relationship reports", add_table_of_contents='y')
  template.new_paragraph(text="These reports are other representations of the ASCT+B table. We split each row into pairs with adjacent terms, resulting in a table with two primary columns, object (o), left side and subject (s), right side. The experts' labels for the subject and object are in the columns user_slabel and user_olabel. The other columns are the subject label (s_label) and object label (o_label), the label from the source ontologies.")
  template.new_paragraph(text="The report means it could not find a partonomy relationship in the source ontologies, but it doesn't mean this relationship is entirely invalid. In some cases, the pair is in the *inverse order*. In other cases, the relationship is *missing* in the source ontologies. Finally, how it was modelled in the ASCT+B table is not aligned with the ontologies sources and needs a more general discussion.")

  template.new_header(level=2, title="How to read a table entry")
  template.new_paragraph(text="**In the ASCT+B table**")
  template.new_paragraph(text="\n\n")
  template.new_table(columns=6, rows=2, text=["AS/2","AS/2/LABEL","AS/2/ID","AS/3","AS/3/LABEL","AS/3/ID", "lens","lens","UBERON:0000965","ciliary zonules","suspensory ligament of lens","UBERON:0006762"])
  template.new_paragraph(text="\n\n")

  template.new_paragraph(text="**In the Relationship Report**")
  template.new_paragraph(text="\n\n")
  template.new_table(columns=6, rows=2, text=["s","slabel","user_slabel","o","olabel","user_olabel","UBERON:0006762","suspensory ligament of lens","ciliary zonules","UBERON:0000965","lens","lens"])
  template.new_paragraph(text="\n\n")
  
  template.new_header(level=2, title="Relationship AS-AS report", add_table_of_contents='y')
  template.new_paragraph(text="This table contains terms for anatomical structures that are related to each other according to the ASCT+B table but are not related to each other in source ontologies via one of the relation types we consider valid for ASCT+B tables. Valid relationships are: *part_of*, e.g. corneal endothelium part_of cornea; *subClassOf*, e.g. left kidney subClassOf (is_a) kidney; and *overlaps* (has some part in), e.g. ureter overlaps kidney; *connected_to*, e.g. TBA. *part_of* and *subClassOf* relationships should be specific to general, e.g. left kidney (specific) to kidney (general); corneal endothelium (specific) to cornea (general). The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.")
  
  template.new_paragraph(text="\n\n")
  m_as = template.create_marker(text_marker="as-as_report")
  markers_dict["as-as_report"] = m_as
  template.new_paragraph(text="\n\n")

  template.new_header(level=2, title="Relationship CT-CT report", add_table_of_contents='y')
  template.new_paragraph(text="In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.")

  template.new_paragraph(text="\n\n")
  m_ct = template.create_marker(text_marker="ct-ct_report")
  markers_dict["ct-ct_report"] = m_ct
  template.new_paragraph(text="\n\n")

  template.new_header(level=2, title="Relationship CT-AS report", add_table_of_contents='y')
  template.new_paragraph(text="In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.")

  template.new_paragraph(text="\n\n")
  m_ctas = template.create_marker(text_marker="ct-as_report")
  markers_dict["ct-as_report"] = m_ctas
  template.new_paragraph(text="\n\n")

  template.new_header(level=1, title="New CL terms", add_table_of_contents='y')

  m_ncl = template.create_marker(text_marker="new_cl")
  markers_dict["new_cl"] = m_ncl
  template.new_paragraph(text="\n\n")

  template.new_header(level=1, title="New UBERON terms", add_table_of_contents='y')

  m_nub = template.create_marker(text_marker="new_uberon")
  markers_dict["new_uberon"] = m_nub
  template.new_paragraph(text="\n\n")

  template.new_header(level=1, title="Informative reports (valid relationships)", add_table_of_contents='y')

  template.new_header(level=2, title="Indirect relationship", add_table_of_contents='y')

  m_ind = template.create_marker(text_marker="indirect")
  markers_dict["indirect"] = m_ind

  template.new_header(level=2, title="Relationship AS has part CT", add_table_of_contents='y')

  m_hp = template.create_marker(text_marker="has_part")
  markers_dict["has_part"] = m_hp

  template.new_table_of_contents(table_title="Table of contents", depth=2)
  return template, markers_dict

def get_row_link(table, row):
  table_config = get_sheet_gid(table, "False")

  URL = f'https://docs.google.com/spreadsheets/d/{table_config["sheetId"]}/edit#gid={table_config["gid"]}&range={row}:{row}'

  return URL

def compact_issues(items: list, element: str):
    compacted_items = {}
    
    for item in items:
        key = item[element]
        
        if key not in compacted_items:
            compacted_items[key] = item.copy()
            compacted_items[key]["rows"] = [item["row_number"]]
            compacted_items[key].pop("row_number")
        else:
            compacted_items[key]["rows"].append(item["row_number"])
    
    return list(compacted_items.values())

def list_rows_link(table: str, rows: list):
    return (", ").join(list(map(lambda x: f'_[{x}]({get_row_link(table, x)})_', rows)))

def generate_invalid_terms_report(log_dict, table):
    terms_report = {
        "no_found_id": "",
        "typos": "",
        "diff_label": "",
        "blank": "",
        "external": "",
        "no_parent": ""
    }
    
    blank = []
    typos = []
    external = []

    def add_issue_to_report(issue_list, report_key, message_template):
        if issue_list:
            compacted_issues = compact_issues(issue_list, "id" if report_key == "typos" or report_key == "external" else "user_label")
            for issue in compacted_issues:
                rows = list_rows_link(table, issue["rows"])
                terms_report[report_key] += message_template.format(
                    issue_id=issue.get("id", ""),
                    user_label=issue.get("user_label", ""),
                    asct_label=issue.get("asct_label", ""),
                    label=issue.get("label", ""),
                    rows_count=len(issue["rows"]),
                    rows_s_or_p="rows" if len(issue["rows"]) > 1 else "row",
                    rows=rows
                )
        else:
            terms_report[report_key] = "- No issues found.\n\n"
    
    for issue in log_dict["no_valid_id"]:
        if issue["id"] == "":
            blank.append(issue)
        elif 'uberon' in issue["id"] or 'UBERON' in issue["id"] or 'cl' in issue["id"] or 'CL' in issue["id"]:
            typos.append(issue)
        elif 'FMA' in issue["id"] or 'fma' in issue["id"] or 'LMHA' in issue["id"] or 'lmha' in issue["id"] or 'ILX' in issue["id"]:
            external.append(issue)
        else:
            typos.append(issue)

    add_issue_to_report(blank, "blank",
                        "1. No term id was found for the name/label _{user_label}_ in the following {rows_count} {rows_s_or_p} {rows}.\n\n")
    
    add_issue_to_report(typos, "typos",
                        "1. It might have a typo in the term _{issue_id}_ in the following {rows_count} {rows_s_or_p} {rows}. The term id should have this pattern: UBERON:NNNNNNN or CL:NNNNNNN or PCL:NNNNNNN. The ontology name in upper case. N is a number, and it should have exactly 7 numbers after the colon. Please change it in the ASCT+B table.\n\n")
    
    add_issue_to_report(external, "external",
                        "1. The term _{issue_id}_ in the following {rows_count} {rows_s_or_p} {rows} is from another ontology that is not validated in this process.\n\n")

    add_issue_to_report(log_dict["diff_label"], "diff_label",
                        "1. The term _{issue_id}_ has a different name/label in the source ontology in the following {rows_count} {rows_s_or_p} {rows}. The name/label in the **ASCT+B table** is _{asct_label}_ and the one in the **ontology** is _{label}_. For reference, the given name/label **by SMEs** is _{user_label}_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.\n\n")

    add_issue_to_report(log_dict["no_parent"], "no_parent",
                        "1. The term _{user_label}_ without ontology ID has no parent that is from the CL ontology in the following {rows_count} {rows_s_or_p} {rows}.\n\n")
    
    for issue in log_dict["no_found_id"]:
        terms_report["no_found_id"] += f'1. {issue["id"]}\n\n'

    return terms_report


def add_base_iri(content):
  UBERON_BASE = "http://purl.obolibrary.org/obo/UBERON_"
  CL_BASE = "http://purl.obolibrary.org/obo/CL_"

  content_uri = content.replace("UBERON:", UBERON_BASE).replace("CL:", CL_BASE)

  return f'[{content}]({content_uri})'

def generate_readme(file, data, table):
  readme, markers_dict = generate_template_readme(file, table)
  
  terms_report = generate_invalid_terms_report(data, table)

  rel_report = generate_relationship_md(table)

  readme.file_data_text = readme.place_text_using_marker(text=terms_report["no_found_id"], marker=markers_dict["nfound"])

  readme.file_data_text = readme.place_text_using_marker(text=terms_report["typos"], marker=markers_dict["typos"])

  readme.file_data_text = readme.place_text_using_marker(text=terms_report["diff_label"], marker=markers_dict["diff_label"])

  readme.file_data_text = readme.place_text_using_marker(text=terms_report["blank"], marker=markers_dict["blank"])
  
  readme.file_data_text = readme.place_text_using_marker(text=terms_report["no_parent"], marker=markers_dict["no_parent"])

  readme.file_data_text = readme.place_text_using_marker(text=terms_report["external"], marker=markers_dict["external"])

  readme.file_data_text = readme.place_text_using_marker(text=rel_report["as-as"], marker=markers_dict["as-as_report"])

  readme.file_data_text = readme.place_text_using_marker(text=rel_report["ct-ct"], marker=markers_dict["ct-ct_report"])
  
  readme.file_data_text = readme.place_text_using_marker(text=rel_report["ct-as"], marker=markers_dict["ct-as_report"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'new_cl_terms_{args.table}.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["new_cl"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'new_uberon_terms_{args.table}.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["new_uberon"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'class_{args.table}_indirect_log.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["indirect"])

  readme.file_data_text = readme.place_text_using_marker(text=readme.new_inline_link(f'{args.table}_AS_has_part_CT_log.tsv', text="Report", bold_italics_code='b'), marker=markers_dict["has_part"])
  
  readme.create_md_file()

def generate_graph_template(file, table):
  date = datetime.today().strftime('%Y-%m-%d')

  template = MdUtils(file_name=file, title=f'ASCT+B Validation Reports for {table} ({date})')

  template.new_header(level=1, title="ASCT+B as Graph")

  template.new_paragraph(text="This is the representation of the ASCT+B table as a graph. The UBERON (AS) terms are represented in cream colour, and CL (CT) terms are represented in light blue colour.")

  template.new_paragraph(text="The red edges in the graph indicate relationships present in the ASCT+B table but are not currently found in the CL or Uberon ontologies. We use the relationship *ccf_located_in* to link CL to UBERON terms and *ccf_part_of* to link UBERON terms. **They are non-validated relationships.**")

  template.new_paragraph(text="The blue, black, or dark green edges are relationships in the CL or Uberon ontologies. **They are valid relationships.**")

  template.new_paragraph(text="The light green edges are relationships in the CL or Uberon ontologies. There is at least one light green edge as a **suggestion relationship** when there's a red edge. If there isn't a light green edge for a red edge, there isn't in the ontology a relationship between the original term and any other term in the graph.")

  template.new_paragraph(text="Please ensure that all terms have a relationship that is part of the path to the leading term in the ASCT+B table. Verify if there isn't a gap between the two levels without UBERON or CL terms in the ASCT+B table.")

  template.new_paragraph(text="Please ensure that there isn't the same term in two levels on the same row. In the graph, it is represented as a red-edge relationship to the term itself.")

  template.new_paragraph(text=template.new_inline_link(f"assets/ccf_{table}_graph.pdf", text="View image as PDF", bold_italics_code='i'))

  template.new_paragraph(template.new_inline_image (text=f"{table} ASCT+B table in graph", path=f"assets/ccf_{table}_graph.png"))

  return template

def generate_graph_page(file, table):
  graph_page = generate_graph_template(file, table)

  graph_page.create_md_file()

def add_row_link(report, table):
  for row in report.itertuples():
    row_n = row.row_number
    report.at[row.Index, "row_number"] = f'[{row_n}]({get_row_link(table, row_n)})'

  return report

def split_report(report):
  report_as = report[report['s'].str.contains('UBERON') & report['o'].str.contains('UBERON')]
  report_ct = report[report['s'].str.contains('CL') & report['o'].str.contains('CL')]
  report_ct_as = report[report['s'].str.contains('CL') & report['o'].str.contains('UBERON')]

  return report_as, report_ct, report_ct_as

def tsv2md(report):
  return tabulate(report, headers=report.columns, tablefmt="github")


def generate_relationship_md(table):
  reports = {"as-as": "", "ct-ct": "", "ct-as": ""}
  BASE_PATH = f"../docs/{table}/"
  try:
    report = pd.read_csv(f"{BASE_PATH}class_{table}_log.tsv", sep='\t')
    report_as, report_ct, report_ct_as = split_report(add_row_link(report, table))
  except:
    report_as = report_ct = report_ct_as = []
  

  if len(report_as):
    reports["as-as"] = tsv2md(report_as)
  else:
    reports["as-as"] = "- No issues found.\n\n"
  
  if len(report_ct):
    reports["ct-ct"] = tsv2md(report_ct)
  else:
    reports["ct-ct"] = "- No issues found.\n\n"

  if len(report_ct_as):
    reports["ct-as"] = tsv2md(report_ct_as)
  else:
    reports["ct-as"] = "- No issues found.\n\n"

  return reports



if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--table", help="table to generate readme")
  parser.add_argument("-o", "--output", help="output file path")
  parser.add_argument("-m", "--mode", help="readme or graph")
  parser.add_argument("-d", "--data", help="log in json")

  args = parser.parse_args()
  if args.mode == "readme":
    log = json.load(open(args.data))
    args.data = log
    generate_readme(args.output, args.data, args.table)
  elif args.mode == "graph":
    generate_graph_page(args.output, args.table)