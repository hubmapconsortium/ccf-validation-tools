"""
This script generates a markdown file with the dashboard of the validation
reports. The dashboard includes the terms and relationships reports.
"""
import argparse
from datetime import date

import pandas as pd
from mdutils.mdutils import MdUtils

from readme_reports_generation import tsv2md

PASS = "<font color='green'>"
FAIL = "<font color='red'>"
CLOSE_TAG = "</font>"
BASE_PATH = "../reports/report_"
DATE_FILE = date.today().strftime("%Y%m%d")
DATE = date.today().strftime("%Y-%m-%d")


def clean_up(report):
    """
    Cleans up the report by dropping unnecessary columns.

    Args:
        report (pandas.DataFrame): The report to clean up.

    Returns:
        pandas.DataFrame: The cleaned up report.
    """
    return report.drop(
        columns=[
            "percent_indirect_AS-AS_relationship",
            "percent_indirect_CT-CT_relationship"
        ]
    )


def add_link(report):
    """
    Adds links to the report.

    Args:
        report (pandas.DataFrame): The report to add links to.

    Returns:
        pandas.DataFrame: The report with links added.
    """
    for row in report.itertuples():
        row_table = row.Table
        if row_table != "Total":
            report.at[row.Index, "Table"] = (
                f"[{row_table}]({row_table}/README.md)"
            )

    return report


def check_number_n_get_color(number):
    """
    Checks the number and returns the corresponding color tag.

    Args:
        number (int or float): The number to check.

    Returns:
        str: The color tag.
    """
    if isinstance(number, int):
        if number > 0:
            return f"{FAIL}{number}{CLOSE_TAG}"
        return f"{PASS}{number}{CLOSE_TAG}"
    if isinstance(number, float):
        if number < 50.0:
            return f"{PASS}{number}{CLOSE_TAG}"

        return f"{FAIL}{number}{CLOSE_TAG}"
    return number


def add_color(report, report_type):
    """
    Adds color tags to the report based on the report type.

    Args:
        report (pandas.DataFrame): The report to add color tags to.
        report_type (str): The type of report ("terms" or "relations").

    Returns:
        pandas.DataFrame: The report with color tags added.
    """
    if report_type == "terms":
        for row in report.itertuples():
            report.at[row.Index, "AS_invalid_term_percent"] = (
                check_number_n_get_color(row.AS_invalid_term_percent)
            )
            report.at[row.Index, "CT_invalid_term_percent"] = (
                check_number_n_get_color(row.CT_invalid_term_percent)
            )
            report.at[row.Index, "invalid_terms_percent"] = (
                check_number_n_get_color(row.invalid_terms_percent)
            )
    elif report_type == "relations":
        for row in report.itertuples():
            report.at[row.Index, "percent_invalid_AS-AS_relationship"] = (
                check_number_n_get_color(row._3)
            )
            report.at[row.Index, "percent_invalid_CT-CT_relationship"] = (
                check_number_n_get_color(row._5)
            )
            report.at[row.Index, "percent_invalid_CT-AS_relationship"] = (
                check_number_n_get_color(row._7)
            )
            report.at[row.Index, "number_of_no_parent_relationships"] = (
                check_number_n_get_color(row.number_of_no_parent_relationships)
            )
            report.at[row.Index, "unique_no_parent_relationships"] = (
                check_number_n_get_color(
                    int(row.unique_no_parent_relationships)
                )
            )

    return report


def get_reports():
    """
    Retrieves the terms and relationships reports for the given date.

    Args:
        date (str): The date in the format "YYYYMMDD".

    Returns:
        tuple: A tuple containing the terms report and the relationships
                report.
    """
    ter_report = pd.read_csv(f"{BASE_PATH}terms_{DATE_FILE}.tsv", sep="\t")
    ter_report.sort_values(by=["Table"], inplace=True)
    ter_report.loc["Total"] = ter_report.sum()
    ter_report.loc[ter_report.index[-1], "Table"] = "Total"
    ter_report.loc[ter_report.index[-1], "AS_invalid_term_percent"] = ""
    ter_report.loc[ter_report.index[-1], "CT_invalid_term_percent"] = ""
    ter_report.loc[ter_report.index[-1], "invalid_terms_percent"] = ""
    ter_report = add_color(ter_report.reset_index(drop=True), "terms")
    ter_report.rename(columns={
        "AS_valid_term_number": "# VALID AS TERMS",
        "AS_temp_term_number": "# AS TEMP TERMS",
        "AS_out_ub": "# AS NOT UBERON TERMS",
        "AS_invalid_term_number": "# INVALID AS TERMS",
        "AS_invalid_term_percent": "% INVALID AS TERMS",
        "CT_valid_term_number": "# VALID CT TERMS",
        "CT_temp_term_number": "# CT TEMP TERMS",
        "CT_out_ub": "# CT NOT CL TERMS",
        "CT_invalid_term_number": "# INVALID CT TERMS",
        "CT_invalid_term_percent": "% INVALID CT TERMS",
        "invalid_terms_percent": "% INVALID TERMS"
    }, inplace=True)
    ter_report = add_link(ter_report)
    ter_report_md = tsv2md(ter_report)

    rel_report = pd.read_csv(
        f"{BASE_PATH}relationship_{DATE_FILE}.tsv", sep="\t"
    )
    rel_report.sort_values(by=["Table"], inplace=True)
    rel_report.loc["Total"] = rel_report.sum()
    rel_report.loc[rel_report.index[-1], "Table"] = "Total"
    rel_report.loc[
        rel_report.index[-1], "percent_invalid_AS-AS_relationship"
    ] = ""
    rel_report.loc[
        rel_report.index[-1], "percent_invalid_CT-CT_relationship"
    ] = ""
    rel_report.loc[
        rel_report.index[-1], "percent_invalid_CT-AS_relationship"
    ] = ""
    rel_report = clean_up(rel_report.reset_index(drop=True))
    rel_report = add_color(rel_report, "relations")
    rel_report.rename(columns={
        "number_of_AS-AS_relationships": "# AS-AS RELATIONS",
        "percent_invalid_AS-AS_relationship": "% INVALID AS-AS RELATIONS",
        "number_of_CT-CT_relationships": "# CT-CT RELATIONS",
        "percent_invalid_CT-CT_relationship": "% INVALID CT-CT RELATIONS",
        "number_of_CT-AS_relationships": "# CT-AS RELATIONS",
        "percent_invalid_CT-AS_relationship": "% INVALID CT-AS RELATIONS",
        "number_of_no_parent_relationships": "# CASES NO PARENT LINK TO CL",
        "unique_no_parent_relationships": "# UNIQUE NO PARENT LINK TO CL"
    }, inplace=True)
    rel_report = add_link(rel_report)
    rel_report_md = tsv2md(rel_report)

    return ter_report_md, rel_report_md


def generate_dashboard(output):
    """
    Generates the validation dashboard.

    Args:
        output (str): The output file path.
    """
    template = MdUtils(
        file_name=output, title=f"Validation Dashboard ({DATE})"
    )

    terms_report, rel_report = get_reports()

    template.new_header(level=1, title="Terms")
    template.new_paragraph(
        text=(
            """Invalid AS or CT terms include terms not from UBERON or CL
                ontologies. Also, it includes terms without ID."""
        )
    )
    template.new_paragraph(text=terms_report)

    template.new_paragraph(text="\n\n")

    template.new_header(level=1, title="Relationships")
    template.new_paragraph(text=rel_report)

    template.new_paragraph(text="\n\n")

    template.create_md_file()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="output file path")

    args = parser.parse_args()
    generate_dashboard(args.output)
