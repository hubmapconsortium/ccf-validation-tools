import argparse, requests, json, datetime
from urllib.parse import quote_plus

JOB_SHEET_GID_MAPPING = {
    'Blood': {
      'new': {
        'sheetId': '1LRgU3VGi7Jlxh4EtHZaQiHtzcPYvvxYLGXrMB6oxdvQ', # Blood_v1.2 DRAFT
        'gid': '543201897',
      },
      'old': {
        'sheetId': '1ZYcSWnFHmzR9XKy_002f_oA4PfzokiW4IxkaZZOusvg',
        'gid': '360436225'
      } 
    },
    'Blood_vasculature': {
      'new': {
        'sheetId': '1pBO70FENOlSyPJukxHYjeMXW0SYTLj4lbcw2oGsjuf0', # Blood_Vasculature_v1.2 DRAFT
        'gid': '1789898267', 
      },
      'old': {
        'sheetId': '1IlELzPwpWoHUcDAmNBWofXfislAaF_oR8yVpwy-zl18', # Blood_Vasculature_v1.1
        'gid': '997949803',
      }
    },
    'Bone-Marrow': {
      'new': {
        'sheetId': '16MUBNsMrE1kAyoY1sjCKsGSIHCRw7TnwTys8DHM17j0', # Bone Marrow_v1.2 DRAFT
        'gid': '771476671',
      },
      'old': {
        'sheetId': '1tnqtCAWSA6atiUBUOOjAHdOrjDw_fsIoCd5RkAmw310', # Bone Marrow_v1.1
        'gid': '771476671',
      }
    },
    'Brain': {
      'new': {
        'sheetId': '1Dzbu_yNfQ-AyOgiScZq7rcoG4oINqO1qEU-MnEE4mPw', # Brain_v1.2 DRAFT
        'gid': '2056967441',
      },
      'old': {
        'sheetId': '1TiwW1NZJ5kdCzJ4zwCpY3Gzv3WE5WUoBDWIAkU5gXd0', # Brain_v1.1
        'gid': '2056967441',
      }
    },
    'Breast': {
      'new': {
        'sheetId': '1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/', # Breast_v1.0 DRAFT
        'gid': '928286522',
      },
    },
    'Eye': {
      'new': {
        'sheetId': '1SFGfjkZeDxY_9FaQqNERzq4XRjWDUpwKC9FCqONlbuk', # Eye_v1.1 DRAFT
        'gid': '695483621',
      },
      'old': {
        'sheetId': '1u7IbxnPABRpYL5rFxOba8cmlvG1yGp-dwD3TV3V26K4', # Eye_v1.0
        'gid': '44026578',
      }
    },
    'Fallopian_tube': {
      'new': {
        'sheetId': '1DFGmDSU75eMF6Fgwzk7W2u20DGJRdXN00TP7sO3kTug', # Fallopian_Tube_v1.1 DRAFT
        'gid': '991519552',
      },
      'old': {
        'sheetId': '16tAvAmjwKwbq5SDz7UZ-T1N_KUHRGqPDbMqffFuInMI', # Fallopian_Tube_v1.0
        'gid': '1739942440',
      }
    },
    'Heart': {
      'new': {
        'sheetId': '1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk', # Heart_v1.2 DRAFT
        'gid': '1759721736',
      },
      'old': {
        'sheetId': '1UhEZpDxQLCJLLx0gnWYDMQP8M-dwjZo_vIyPfjBCcVM', # Heart_v1.1
        'gid': '1759721736',
      }

    },
    'Kidney': {
      'new': {
        'sheetId': '1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw', # Kidney_v1.2 DRAFT
        'gid': '949267305',
      },
      'old': {
        'sheetId': '1PgjYp4MEWANfbxGIxFsJ9vkfEU90MP-v3p5oVlH8U-E', # Kidney_v1.1
        'gid': '949267305',
      }
    },
    'Knee': {
      'new': {
        'sheetId': '1zDCnaoMdSx09OGxjeeG2Sxokw4c_0bnNyDOJC6IMPCw', # Knee_v1.1 DRAFT
        'gid': '1815525900',
      },
      'old': {
        'sheetId': '1QidDho8DxBYjsxaqApiIZA__Z7aWnB61KvC422g2kx8', # Knee_v1.0
        'gid': '1824489301',
      }
    },
    'Large_intestine': {
      'new': {
        'sheetId': '1d_KWKnQq3HT5nzDmfhlvFG4P_qdviu0vyhGZ6QHgNIk', # Large_Intestine_v1.2 DRAFT
        'gid': '2043181688',
      },
      'old': {
        'sheetId': '1vU6mQmnzAAxctbNYPoFxJ8NvbUql8pbipsGdt7YCOQQ', # Large_Intestine_v1.0
        'gid': '2043181688',
      }
    },
    'Liver': {
      'new': {
        'sheetId': '1F8ZXt1naE1pJFjfsAd6wK7x22D3qRW5O0E2d9gUKAik', # Liver_v1.1 DRAFT
        'gid': '1694828397',
      },
      'old': {
        'sheetId': '1tPDKw_znxqWhZYPTeVN4AN2_F4-JecsdeUgp2lj4P8g', # Liver_v1.0
        'gid': '1460762432',
      }
    },
    'Lung': {
      'new': {
        'sheetId': '1iF4vx9EuQ2tQMBOm6awd9sf-2e_EHsPlcgzrF_YDtis', # Lung_v1.2 DRAFT
        'gid': '1523836586',
      },
      'old': {
        'sheetId': '1tK916JyG5ZSXW_cXfsyZnzXfjyoN-8B2GXLbYD6_vF0', # Lung_v1.1
        'gid': '1824552484',
      }
    },
    'Lymph_node': {
      'new': {
        'sheetId': '1_VWj_dD1dbmnBf8t0wptXvpy1oyyllZ1tXc0aKo2MSA', # Lymph_Node_v1.2 DRAFT
        'gid': '1223566381',
      },
      'old': {
        'sheetId': '1aK9gJ2_kMb2B8zrQgScDgxpEWAcCs7kl-gnQGwV3LHM', # Lymph_Node_v1.1
        'gid': '1223566381',
      }
    },
    'Lymph_vasculature': {
      'new': {
        'sheetId': '1FNoQthhgP0OXEZuwIVL0XZA8SVYzCcVPm4_n20dt--8', # Lymph_Vasculature_v1.1 DRAFT
        'gid': '2087685463',
      },
      'old': {
        'sheetId': '1SILRNUI71BEVWl1fpsi_32DSuSA-bAPgXv5pTfKnrOE', # Lymph_Vasculature_v1.0
        'gid': '1700987638',
      }
    },
    'Ovary': {
      'new': {
        'sheetId': '1K5LWhMaT_IryNxuK1Vko0Ud49VUB8RnMltL5jYhJUak', # Ovary_v1.1 DRAFT
        'gid': '756296951',
      },
      'old': {
        'sheetId': '1FE2XufrruExUWqcai3XRFqtMjeEdzoLKJ-YNa-nRZ1M', # Ovary_v1.0
        'gid': '1997082517',
      }
    },
    'Pancreas': {
      'new': {
        'sheetId': '1_cmA0CWUzVz1lNMpNOXqzrnmWgXv3GANqN7W18N4crA', # Pancreas_v1.1 DRAFT
        'gid': '439021026',
      },
      'old': {
        'sheetId': '1CIWqIygz2OzxMECIvhudFN14Kt7-JFUBLpzn5uuH5Xs', # Pancreas_v1.0
        'gid': '801179416',
      }
    },
    'Peripheral_nervous_system': {
      'new': {
        'sheetId': '1TQsd657v-Jfcme4ftmpq7Zaegu0HxHOmGJKUPL8QqyU', # Peripheral_Nervous_System_v1.1 DRAFT
        'gid': '917578386',
      },
      'old': {
        'sheetId': '1KifiEDn3PpJ8pjz9_ka4TWkT085wLIzIQP5NKSvb2Ac', # Peripheral_Nervous_System_v1.0
        'gid': '714133140',
      }
    },
    'Placenta': {
      'new': {
        'sheetId': '1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY', # Placenta_v1.0 DRAFT
        'gid': '231591207',
      }
    },
    'Prostate': {
      'new': {
        'sheetId': '1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU', # Prostate_v1.1 DRAFT
        'gid': '1239199370',
      },
      'old': {
        'sheetId': '1_O5yXOesG93dobMHRSIvVAt9xj7mDnEAYdRJcHYJ84U', # Prostate_v1.0
        'gid': '1757780481',
      }
    },
    'Skin': {
      'new': {
        'sheetId': '16E07Ia3opnjBzBVswS7iQccd2Y_fw7m8-mNUNjwv80E', # Skin_v1.2 DRAFT
        'gid': '269383687',
      },
      'old': {
        'sheetId': '1Pmi3g26vhbg9HU6GDpIvxKbIP985JM-5eytOHxJUdZs', # Skin_v1.1
        'gid': '269383687',
      }
    },
    'Small_intestine': {
      'new': {
        'sheetId': '1pZDLDiAHD-QDi-OTF4GtUHf6bkKkDc2qc0eIFnIqS_s', # Small_Intestine_v1.1 DRAFT
        'gid': '247140941',
      },
      'old': {
        'sheetId': '1Xlds8FzZ8ecmy3cxYJt1ijQC9FifamZRZ5KzH4Yt-MQ', # Small_Intestine_v1.0
        'gid': '1762589435',
      }
    },
    'Spleen': {
      'new': {
        'sheetId': '1bairJs37srg0hF4MGIfsdtb000YtrA1hI45D8KI5Gxc', # Sleen_v1.2 DRAFT
        'gid': '69626346',
      },
      'old': {
        'sheetId': '1HL7aHx5A2KOa1KsJ0PIagqxdshVavFIEJZP6_YDtUww', # Sleen_v1.1
        'gid': '69626346',
      }
    },
    'Spinal_Cord': {
      'new': {
        'sheetId': '1tK916JyG5ZSXW_cXfsyZnzXfjyoN-8B2GXLbYD6_vF0', # Spinal_Cord_v1.0 DRAFT
        'gid': '1106564583',
      }
    },
    'Thymus': {
      'new': {
        'sheetId': '14KY4dp6YwVf0GSiCOcxhuy9L_aJ8FjTX_jidrIq7E_c', # Thymus_v1.2 DRAFT
        'gid': '863370556',
      },
      'old': {
        'sheetId': '1nSiz2yFDMJSqIXbnAP_EXIQZfN6ZflOs-WBdZ6LVhUY', # Thymus_v1.1
        'gid': '863370556',
      }
    },
    'Ureter': {
      'new': {
        'sheetId': '1ZUmHX22NYMfBgFoni4zK6bsEYFn4rGSk9oYBNPcebZQ', # Ureter_v1.1 DRAFT
        'gid': '73126811',
      },
      'old': {
        'sheetId': '1tK916JyG5ZSXW_cXfsyZnzXfjyoN-8B2GXLbYD6_vF0', # Ureter_v1.0
        'gid': '1106564583',
      }
    },
    'Urinary_bladder': {
      'new': {
        'sheetId': '1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo', # Urinary_Bladder_v1.1 DRAFT
        'gid': '1057183099',
      },
      'old': {
        'sheetId': '1ohOG5jMf9d9eqjbVK6_u3CvgfG3wcLfs_pxB2838wOo', # Urinary_Bladder_v1.0
        'gid': '1342577957',
      }
    },
    'Uterus': {
      'new': {
        'sheetId': '1RasOQCB4oP_1kvZL7Xv40TID6_365FQ-cgX2fGR54gw', # Uterus_v1.1 DRAFT
        'gid': '603441642',
      },
      'old': {
        'sheetId': '1yEcbJMrUIzJY-4JNtF1Y_eUpAQsgKF6DX2-5Z3UXBeE', # Uterus_v1.0
        'gid': '1434605386',
      }
    }
}

def main(args):
  if eval(args.old_version):
    version = JOB_SHEET_GID_MAPPING[args.job]["old"]
  else:
    version = JOB_SHEET_GID_MAPPING[args.job]["new"]

  API_URL = 'https://asctb-api.herokuapp.com/v2/csv?output=json&expanded=true&subclasses=false&csvUrl={0}'
  GOOGLE_SHEET = f'https://docs.google.com/spreadsheets/d/{version["sheetId"]}/export?format=csv&gid={version["gid"]}'
  DATA_URL=API_URL.format(quote_plus(GOOGLE_SHEET))

  data = requests.get(DATA_URL).text
  data = json.loads(data)

  table_date = data["parsed"][6][1]
  table_version = data["parsed"][7][1]

  if table_date != '':
    try:
      table_date = datetime.datetime.strptime(data["parsed"][6][1], '%m/%d/%Y').strftime('%Y-%m-%d')
    except:
      try:
        table_date = datetime.datetime.strptime(data["parsed"][7][1], '%m/%d/%Y').strftime('%Y-%m-%d')
        table_version = data["parsed"][8][1]
      except:
        table_date = "NA"
  else:
    table_date = "NA"

  if table_version == '':
    table_version = "NA"
      
  with open('tables_version.txt', 'a+', encoding='utf-8') as t:
    t.write(args.job + "," + table_version + "," + table_date + "\n")

  with open(args.output_file, 'w', encoding='utf-8') as f:
    json.dump(data['data'], f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('job', help='job to download')
  parser.add_argument('output_file', help='output file path')
  parser.add_argument("old_version", help="is old version")

  args = parser.parse_args()
  main(args)