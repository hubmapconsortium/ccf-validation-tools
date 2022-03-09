import argparse, requests, json, datetime
from urllib.parse import quote_plus

JOB_SHEET_GID_MAPPING = {
    'Blood': { 
      'sheetId': '1LRgU3VGi7Jlxh4EtHZaQiHtzcPYvvxYLGXrMB6oxdvQ', # Blood_v1.2 DRAFT
      'gid': '543201897',
      'version': 'v1.2' 
    },
    'Blood_vasculature': {
      'sheetId': '1pBO70FENOlSyPJukxHYjeMXW0SYTLj4lbcw2oGsjuf0', # Blood_Vasculature_v1.2 DRAFT
      'gid': '1789898267', 
      'version': 'v1.2',
    },
    'Bone-Marrow': {
      'sheetId': '16MUBNsMrE1kAyoY1sjCKsGSIHCRw7TnwTys8DHM17j0', # Bone Marrow_v1.2 DRAFT
      'gid': '771476671',
      'version': 'v1.2'
    },
    'Brain': {
      'sheetId': '1Dzbu_yNfQ-AyOgiScZq7rcoG4oINqO1qEU-MnEE4mPw', # Brain_v1.2 DRAFT
      'gid': '2056967441',
      'version': 'v1.2'
    },
    'Breast': {
      'sheetId': '1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/', # Breast_v1.0 DRAFT
      'gid': '928286522',
      'version': 'v1.0'
    },
    'Eye': {
      'sheetId': '1SFGfjkZeDxY_9FaQqNERzq4XRjWDUpwKC9FCqONlbuk', # Eye_v1.1 DRAFT
      'gid': '695483621',
      'version': 'v1.1'
    },
    'Fallopian_tube': {
      'sheetId': '1DFGmDSU75eMF6Fgwzk7W2u20DGJRdXN00TP7sO3kTug', # Fallopian_Tube_v1.1 DRAFT
      'gid': '991519552',
      'version': 'v1.1'
    },
    'Heart': {
      'sheetId': '1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk', # Heart_v1.2 DRAFT
      'gid': '1759721736',
      'version': 'v1.2'
    },
    'Kidney': {
      'sheetId': '1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw', # Kidney_v1.2 DRAFT
      'gid': '949267305',
      'version': 'v1.2'
    },
    'Knee': {
      'sheetId': '1zDCnaoMdSx09OGxjeeG2Sxokw4c_0bnNyDOJC6IMPCw', # Knee_v1.1 DRAFT
      'gid': '1815525900',
      'version': 'v1.1'
    },
    'Large_intestine': {
      'sheetId': '1d_KWKnQq3HT5nzDmfhlvFG4P_qdviu0vyhGZ6QHgNIk', # Large_Intestine_v1.2 DRAFT
      'gid': '2043181688',
      'version': 'v1.2'
    },
    'Liver': {
      'sheetId': '1F8ZXt1naE1pJFjfsAd6wK7x22D3qRW5O0E2d9gUKAik', # Liver_v1.1 DRAFT
      'gid': '1694828397',
      'version': 'v1.1'
    },
    'Lung': {
      'sheetId': '1iF4vx9EuQ2tQMBOm6awd9sf-2e_EHsPlcgzrF_YDtis', # Lung_v1.2 DRAFT
      'gid': '1523836586',
      'version': 'v1.2'
    },
    'Lymph_node': {
      'sheetId': '1_VWj_dD1dbmnBf8t0wptXvpy1oyyllZ1tXc0aKo2MSA', # Lymph_Node_v1.2 DRAFT
      'gid': '1223566381',
      'version': 'v1.2'
    },
    'Lymph_vasculature': {
      'sheetId': '1FNoQthhgP0OXEZuwIVL0XZA8SVYzCcVPm4_n20dt--8', # Lymph_Vasculature_v1.1 DRAFT
      'gid': '2087685463',
      'version': 'v1.1'
    },
    'Ovary': {
      'sheetId': '1K5LWhMaT_IryNxuK1Vko0Ud49VUB8RnMltL5jYhJUak', # Ovary_v1.1 DRAFT
      'gid': '756296951',
      'version': 'v1.1'
    },
    'Pancreas': {
      'sheetId': '1_cmA0CWUzVz1lNMpNOXqzrnmWgXv3GANqN7W18N4crA', # Pancreas_v1.1 DRAFT
      'gid': '439021026',
      'version': 'v1.1'
    },
    'Peripheral_nervous_system': {
      'sheetId': '1TQsd657v-Jfcme4ftmpq7Zaegu0HxHOmGJKUPL8QqyU', # Peripheral_Nervous_System_v1.1 DRAFT
      'gid': '917578386',
      'version': 'v1.1'
    },
    'Placenta': {
      'sheetId': '1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY', # Placenta_v1.0 DRAFT
      'gid': '231591207',
      'version': 'v1.0'
    },
    'Prostate': {
      'sheetId': '1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU', # Prostate_v1.1 DRAFT
      'gid': '1239199370',
      'version': 'v1.1'
    },
    'Skin': {
      'sheetId': '16E07Ia3opnjBzBVswS7iQccd2Y_fw7m8-mNUNjwv80E', # Skin_v1.2 DRAFT
      'gid': '269383687',
      'version': 'v1.2'
    },
    'Small_intestine': {
      'sheetId': '1pZDLDiAHD-QDi-OTF4GtUHf6bkKkDc2qc0eIFnIqS_s', # Small_Intestine_v1.1 DRAFT
      'gid': '247140941',
      'version': 'v1.1'
    },
    'Spleen': {
      'sheetId': '1bairJs37srg0hF4MGIfsdtb000YtrA1hI45D8KI5Gxc', # Sleen_v1.2 DRAFT
      'gid': '69626346',
      'version': 'v1.2'
    },
    'Spinal_Cord': {
      'sheetId': '1tK916JyG5ZSXW_cXfsyZnzXfjyoN-8B2GXLbYD6_vF0', # Spinal_Cord_v1.0 DRAFT
      'gid': '1106564583',
      'version': 'v1.0'
    },
    'Thymus': {
      'sheetId': '14KY4dp6YwVf0GSiCOcxhuy9L_aJ8FjTX_jidrIq7E_c', # Thymus_v1.2 DRAFT
      'gid': '863370556',
      'version': 'v1.2'
    },
    'Ureter': {
      'sheetId': '1ZUmHX22NYMfBgFoni4zK6bsEYFn4rGSk9oYBNPcebZQ', # Ureter_v1.1 DRAFT
      'gid': '73126811',
      'version': 'v1.1'
    },
    'Urinary_bladder': {
      'sheetId': '1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo', # Urinary_Bladder_v1.1 DRAFT
      'gid': '1057183099',
      'version': 'v1.1'
    },
    'Uterus': {
      'sheetId': '1RasOQCB4oP_1kvZL7Xv40TID6_365FQ-cgX2fGR54gw', # Uterus_v1.1 DRAFT
      'gid': '603441642',
      'version': 'v1.1'
    }
}

def main(args):
  API_URL = 'https://asctb-api.herokuapp.com/v2/csv?output=json&expanded=true&subclasses=false&csvUrl={0}'
  GOOGLE_SHEET = f'https://docs.google.com/spreadsheets/d/{JOB_SHEET_GID_MAPPING[args.job]["sheetId"]}/export?format=csv&gid={JOB_SHEET_GID_MAPPING[args.job]["gid"]}'
  DATA_URL=API_URL.format(quote_plus(GOOGLE_SHEET))

  data = requests.get(DATA_URL).text
  data = json.loads(data)

  table_date = datetime.datetime.now().strftime('%Y-%m-%d')
  table_version = JOB_SHEET_GID_MAPPING[args.job]["version"]
    
  with open('tables_version.txt', 'a+', encoding='utf-8') as t:
    t.write(args.job + "," + table_version + "," + table_date + "\n")

  with open(args.output_file, 'w', encoding='utf-8') as f:
    json.dump(data['data'], f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('job', help='job to download')
  parser.add_argument('output_file', help='output file path')

  args = parser.parse_args()
  main(args)