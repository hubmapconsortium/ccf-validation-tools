import pandas as pd
from datetime import date
from readme_reports_generation import tsv2md
from mdutils.mdutils import MdUtils


# DATE_FILE = date.today().strftime("%Y%m%d")
DATE_FILE = "20230810"
# DATE = date.today().strftime('%Y-%m-%d')
DATE = "2023-08-10"
BASE_PATH = f"../reports/report_"

reports = ["terms", "relationship"]

template = MdUtils(file_name="../docs/dashboard.md", title=f'Validation Dashboard ({DATE})')

for report_type in reports:
    report = pd.read_csv(f"{BASE_PATH}{report_type}_{DATE_FILE}.tsv", sep='\t')
    #report_md = tsv2html(report)
    report_md = tsv2md(report)
    template.new_header(level=1, title=f"{report_type.capitalize()}")
    template.new_paragraph(text=report_md)
    
    template.new_paragraph(text="\n\n")
    
template.create_md_file()