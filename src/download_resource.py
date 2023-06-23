import argparse, requests, json, datetime
from urllib.parse import quote_plus

def get_config():
  with open("config_asct.json", "r") as f:
    data = json.load(f)
  
  return data

def get_sheet_gid(job, old_version):
  data = get_config()

  for element in data:
    if element["name"] == job:
      if eval(old_version):
        return element["old"]
      else:
        return element["new"]

def get_table_version_n_date(metadata):
  table_date = "NA"
  table_version = "NA"

  if metadata["date"] != '':
    table_date = metadata["date"]
  if metadata["version"] != '':
    table_version = metadata["version"]
  
  return table_date, table_version

def main(args):
  version = get_sheet_gid(args.job, args.old_version)

  API_URL = f'https://mmpyikxkcp.us-east-2.awsapprunner.com/v2/{version["sheetId"]}/{version["gid"]}'

  data = requests.get(API_URL).text
  data = json.loads(data)

  table_date, table_version = get_table_version_n_date(data["metadata"])
      
  with open('tables_version.txt', 'a+', encoding='utf-8') as t:
    t.write(args.job + ";" + table_version + ";" + table_date + "\n")

  with open(args.output_file, 'w', encoding='utf-8') as f:
    json.dump(data['data'], f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('job', help='job to download')
  parser.add_argument('output_file', help='output file path')
  parser.add_argument("old_version", help="is old version")

  args = parser.parse_args()
  main(args)