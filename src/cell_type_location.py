from argparse import ArgumentParser
from itertools import product
import re
import pandas as pd
import os
import json

from uberongraph_tools import UberonGraph
from ccf_tools import split_terms, transform_to_str

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

    if len(markers_group) == 0:
      continue

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

def create_template(input, relationship):
  output = [{'ID': 'ID', 
             'Label': 'LABEL',
             'Equivalent axioms': 'EC %',
             'Equivalent relationship axioms': f'EC {relationship} some %',
            }]

  for _, row in input.iterrows():
    d = {}
    d['Label'] = f'{row["Terminal CT/label"]} of {row["Terminal AS/label"]}'
    d['Equivalent axioms'] = row["Terminal CT/ID"]
    d['Equivalent relationship axioms'] = row["Terminal AS/ID"]
    output.append(d)
  return pd.DataFrame.from_records(output)
  
def template(args):
  ug = UberonGraph()

  report = pd.read_csv(args.input, sep='\t')

  clean_report = report.groupby(['Terminal AS/ID','Terminal CT/ID']).filter(lambda x: len(x)>1)
  clean_report.to_csv('clean_report.tsv', sep='\t')
                    # leukocyte    myeloid cell
  parent_classes = ["CL:0000738", "CL:0000763"]
  ct_list = list(clean_report["Terminal CT/ID"].drop_duplicates())
  combine = list(product(ct_list, parent_classes))

  terms_pairs = transform_to_str(combine)

  valid_subclass, not_valid_subclass = ug.verify_relationship(terms_pairs=terms_pairs, relationship=ug.select_subclass)

  terms_ct_i, _ = split_terms(transform_to_str(valid_subclass))
  ccf_input_temp = clean_report.loc[clean_report["Terminal CT/ID"].isin(terms_ct_i)]
  
  ccf_template = create_template(ccf_input_temp, "located in")
  ccf_template.to_csv(args.output, sep='\t')

  terms_ct_ni, _ = split_terms(not_valid_subclass)
  terms_ct = set(terms_ct_ni) - set(terms_ct_i)
  cl_input_temp = clean_report.loc[clean_report["Terminal CT/ID"].isin(terms_ct)]

  cl_template = create_template(cl_input_temp, "part of")
  cl_template.to_csv('../templates/cl_compound.tsv', sep='\t')


def generate(args):
  report = get_ct_loc_marker(args.input)

  if report is not None:
    report.to_csv(args.output, sep='\t', index=False)


if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument('input', help='input json file')
  parser.add_argument('output', help='output csv file')
  parser.add_argument('mode', help='three modes to deal with report: generate, merge or template')

  args = parser.parse_args()
  if args.mode == 'generate':
    generate(args)
  elif args.mode == 'merge':
    merge_csv(args.output)
  elif args.mode == 'template':
    template(args)