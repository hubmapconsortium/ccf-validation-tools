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
        report.at[row.Index, "Table"] = f"[{row_table}](../docs/{row_table}/README.md)"

    return report

def generate_dashboard(output):
    # DATE_FILE = date.today().strftime("%Y%m%d")
    DATE_FILE = "20230810"
    # DATE = date.today().strftime('%Y-%m-%d')
    DATE = "2023-08-10"
    BASE_PATH = f"../reports/report_"

    template = MdUtils(file_name=output, title=f'Validation Dashboard ({DATE})')
    
    ter_report = pd.read_csv(f"{BASE_PATH}terms_{DATE_FILE}.tsv", sep='\t') 
    ter_report = add_link(ter_report).reset_index(drop=True)
    #report_md = tsv2html(report)
    report_md = tsv2md(ter_report)
    template.new_header(level=1, title="Term")
    template.new_paragraph(text=report_md)

    template.new_paragraph(text="\n\n")

    rel_report = pd.read_csv(f"{BASE_PATH}relationship_{DATE_FILE}.tsv", sep='\t') 
    rel_report = add_link(clean_up(rel_report)).reset_index(drop=True)
    #report_md = tsv2html(report)
    report_md = tsv2md(rel_report)
    template.new_header(level=1, title="Relationship")
    template.new_paragraph(text=report_md)

    template.new_paragraph(text="\n\n")
        
    template.create_md_file()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="output file path")
    
    args = parser.parse_args()
    generate_dashboard(args.output)