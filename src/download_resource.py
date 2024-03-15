"""
Download ASCT+B table as JSON and extract its date and version
"""
import argparse
import json
from ast import literal_eval

import requests

API_URL = "https://apps.humanatlas.io/asctb-api/v2/{sheetId}/{gid}"


def get_config() -> list:
    """
    Load config file where list all sheet id and gid per table
    """
    with open("config_asct.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def get_sheet_gid(job: str, old_version: str) -> dict:
    """
    Search config by table name
    """
    data = get_config()

    element = next(
        (element for element in data if element["name"] == job),
        None
    )
    if element:
        return element["old"] if literal_eval(old_version) else element["new"]
    return {}


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

    data = requests.get(
        API_URL.format(sheetId=version["sheetId"], gid=version["gid"]),
        timeout=600
    ).json()

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
