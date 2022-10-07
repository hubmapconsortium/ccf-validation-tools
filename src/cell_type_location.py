from argparse import ArgumentParser
import re
import pandas as pd
import os
import json

def get_ct_loc_marker(file):
  def is_valid_id(content):
    if re.match("(CL|UBERON|HGNC)\:[0-9]+", content):
      return content
    else:
      return False

  asct_b = json.load(open(file))

  out = []

  for row in asct_b:
    anatomical_structures = row["anatomical_structures"]
    cell_types = row["cell_types"]
    biomarkers = row["biomarkers"]

    if len(biomarkers) == 0 or len(anatomical_structures) == 0 or len(cell_types) == 0:
      continue

    last_as = anatomical_structures[-1]
    last_ct = cell_types[-1]

    if last_ct["id"] == '' or last_as["id"] == '':
      continue

    if not is_valid_id(last_ct["id"]) or not is_valid_id(last_as["id"]):
      continue

    markers_group = [marker["id"] for marker in biomarkers if is_valid_id(marker["id"])]

    r = {}
    r["Terminal AS/ID"] = last_as["id"]
    r["Terminal AS/label"] = last_as["rdfs_label"]
    r["Terminal AS/user_label"] = last_as["name"]
    r["Terminal CT/ID"] = last_ct["id"]
    r["Terminal CT/label"] = last_ct["rdfs_label"]
    r["Terminal CT/user_label"] = last_ct["name"]
    r["Markers"] = ', '.join(markers_group)
    out.append(r)

  report = None
  if out:
    report = pd.DataFrame.from_records(out).drop_duplicates().sort_values("Terminal CT/ID")

  return report

def merge_csv(path):
  dir_path = os.path.dirname(path)
  csv_files = os.listdir(os.path.dirname(path))

  df = pd.concat([pd.read_csv(f'{dir_path}/{f}', sep='\t') for f in csv_files ], ignore_index=True).drop_duplicates().sort_values("Terminal CT/ID")

  df.to_csv(path, sep='\t', index=False)
  

def main(args):
  report = get_ct_loc_marker(args.input)

  if report is not None:
    report.to_csv(args.output, sep='\t', index=False)


if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument('input', help='input json file')
  parser.add_argument('output', help='output csv file')
  parser.add_argument('mode', help='two modes to deal with report: generate or merge')

  args = parser.parse_args()
  if args.mode == 'generate':
    main(args)
  elif args.mode == 'merge':
    merge_csv(args.output)