"""
Download ASCT+B table as JSON and extract its date and version
"""

import argparse
import json
from ast import literal_eval

import requests

API_SHEET_CONFIG = "https://apps.humanatlas.io/api/v1/asctb-sheet-config"
API_URL_GSHEET_CSV = (
    "https://docs.google.com/spreadsheets/d/{sheetId}/export?format=csv"
)
API_URL_CSV = "https://apps.humanatlas.io/asctb-api/v2/csv?csvUrl={csv}"


def get_config() -> list:
    """
    Download the latest ASCT+B sheet config from the HRA API
    """
    data = requests.get(API_SHEET_CONFIG).json()

    return data


def normalize_name(name: str) -> str:
    """
    Normalize string for matching purposes
    """
    return name.upper().replace("-", "_")


def get_sheet_gid(job: str, old_version: str) -> dict:
    """
    Search config by table name
    """
    data = get_config()

    name = normalize_name(job)
    element = next(
        (element for element in data if normalize_name(element["name"]) == name), None
    )
    if not element:
        return {}
    elif len(element["version"]) == 1 or not literal_eval(old_version):
        return element["version"][-1]
    else:
        return element["version"][-2]


def get_table_version_n_date(metadata: dict):
    """
    Return table version and date
    """
    table_date = "NA"
    table_version = "NA"

    if metadata["date"]:
        table_date = metadata["date"]
    if metadata["version"]:
        table_version = metadata["version"]

    return table_date, table_version


def main(params: dict):
    """
    Search for config, download table and add date and version into
    tables_version.txt
    """
    version = get_sheet_gid(params.job, params.old_version)

    if "csvUrl" in version:
        csv_url = version["csvUrl"]
    else:
        csv_url = API_URL_GSHEET_CSV.format(sheetId=version["sheetId"])

    data = requests.get(API_URL_CSV.format(csv=csv_url), timeout=600).json()

    table_date, table_version = get_table_version_n_date(data["metadata"])

    with open("tables_version.txt", "a+", encoding="utf-8") as t:
        t.write(f"{params.job};{table_version};{table_date}\n")

    with open(params.output_file, "w", encoding="utf-8") as f:
        json.dump(data["data"], f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("job", help="job to download")
    parser.add_argument("output_file", help="output file path")
    parser.add_argument("old_version", help="is old version?")

    args = parser.parse_args()
    main(args)
