import argparse
from datetime import date

import pandas as pd
from mdutils.mdutils import MdUtils

from readme_reports_generation import tsv2md


def clean_up(report):
    return report.drop(columns=["percent_indirect_AS-AS_relationship","percent_indirect_CT-CT_relationship"])

def add_link(report):
    for row in report.itertuples():
        row_table = row.Table
        report.at[row.Index, "Table"] = f"[{row_table}]({row_table}/README.md)"

    return report

def check_number_n_get_color(number):
    PASS = "<font color='green'>"
    FAIL = "<font color='red'>"
    CLOSE_TAG = "</font>"
    if float(number) < 50.0:
        return f"{PASS}{number}{CLOSE_TAG}"
    else:
        return f"{FAIL}{number}{CLOSE_TAG}"
    

def add_color(report, report_type):
    if report_type == "terms":
        for row in report.itertuples():
            report.at[row.Index, "AS_invalid_term_percent"] = check_number_n_get_color(row.AS_invalid_term_percent)
            report.at[row.Index, "CT_invalid_term_percent"] = check_number_n_get_color(row.CT_invalid_term_percent)
    elif report_type == "relations":
        for row in report.itertuples():
            report.at[row.Index, "percent_invalid_AS-AS_relationship"] = check_number_n_get_color(row._3)
            report.at[row.Index, "percent_invalid_CT-CT_relationship"] = check_number_n_get_color(row._5)
            report.at[row.Index, "percent_invalid_CT-AS_relationship"] = check_number_n_get_color(row._7)
            
    return report

def get_reports(date):
    BASE_PATH = "../reports/report_"
    
    ter_report = pd.read_csv(f"{BASE_PATH}terms_{date}.tsv", sep='\t')
    ter_report.sort_values(by=["Table"], inplace=True)
    ter_report = add_color(ter_report.reset_index(drop=True), "terms")
    ter_report.rename(columns={
        "AS_valid_term_number": "# VALID AS TERMS",
        "AS_invalid_term_number": "# INVALID AS TERMS",
        "AS_invalid_term_percent": "% INVALID AS TERMS",
        "CT_valid_term_number": "# VALID CT TERMS",
        "CT_invalid_term_number": "# INVALID CT TERMS",
        "CT_invalid_term_percent": "% INVALID CT TERMS"
    }, inplace=True)
    ter_report = add_link(ter_report)
    ter_report_md = tsv2md(ter_report)
    
    rel_report = pd.read_csv(f"{BASE_PATH}relationship_{date}.tsv", sep='\t')
    rel_report.sort_values(by=["Table"], inplace=True)
    rel_report = clean_up(rel_report.reset_index(drop=True))
    rel_report = add_color(rel_report, "relations")
    rel_report.rename(columns={
        "number_of_AS-AS_relationships": "# AS-AS RELATIONS",
        "percent_invalid_AS-AS_relationship": "% INVALID AS-AS RELATIONS",
        "number_of_CT-CT_relationships": "# CT-CT RELATIONS",
        "percent_invalid_CT-CT_relationship": "% INVALID CT-CT RELATIONS",
        "number_of_CT-AS_relationships": "# CT-AS RELATIONS",
        "percent_invalid_CT-AS_relationship": "% INVALID CT-AS RELATIONS"
    }, inplace=True) 
    rel_report = add_link(rel_report)
    rel_report_md = tsv2md(rel_report)
    
    return ter_report_md, rel_report_md

def generate_dashboard(output):
    DATE_FILE = date.today().strftime("%Y%m%d")
    DATE = date.today().strftime('%Y-%m-%d')

    template = MdUtils(file_name=output, title=f'Validation Dashboard ({DATE})')
    
    terms_report, rel_report = get_reports(DATE_FILE)
    
    template.new_header(level=1, title="Terms")
    template.new_paragraph(text="Invalid AS or CT terms include terms not from UBERON or CL ontologies. Also, it includes terms without ID.")
    template.new_paragraph(text=terms_report)

    template.new_paragraph(text="\n\n")

    template.new_header(level=1, title="Relationships")
    template.new_paragraph(text=rel_report)

    template.new_paragraph(text="\n\n")
        
    template.create_md_file()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="output file path")
    
    args = parser.parse_args()
    generate_dashboard(args.output)