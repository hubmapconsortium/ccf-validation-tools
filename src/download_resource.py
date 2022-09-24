import argparse, requests, json, datetime
from urllib.parse import quote_plus

JOB_SHEET_GID_MAPPING = {
    'Blood': {
      'new': {
        'sheetId': '1wx2y8_t7NsAs8hPnr6u_N1QK8y_lC3t1G0DnD3LNUnQ', # Blood_v1.3 DRAFT
        'gid': '543201897',
      },
      'old': {
        'sheetId': '1LRgU3VGi7Jlxh4EtHZaQiHtzcPYvvxYLGXrMB6oxdvQ', # Blood_v1.2 DRAFT
        'gid': '543201897',
      }
    },
    'Blood_vasculature': {
      'new': {
        'sheetId': '1N2_rZBJEJHuy_pVgZUdGRbXHwz9rdRp2U-rLpVN7n3w', # Blood_Vasculature_v1.3 DRAFT
        'gid': '1789898267',
      },
      'old': {
        'sheetId': '1pBO70FENOlSyPJukxHYjeMXW0SYTLj4lbcw2oGsjuf0', # Blood_Vasculature_v1.2 DRAFT
        'gid': '1789898267', 
      }
    },
    'Bone-Marrow': {
      'new': {
        'sheetId': '1prDIvvQF0akXKCfLv6FqjtQgZ_oKbIfSfMZt9twrfd0', # Bone Marrow_v1.3 DRAFT
        'gid': '771476671',
      },
      'old': {
        'sheetId': '16MUBNsMrE1kAyoY1sjCKsGSIHCRw7TnwTys8DHM17j0', # Bone Marrow_v1.2 DRAFT
        'gid': '771476671',
      }
    },
    'Brain': {
      'new': {
        'sheetId': '1Hdd-llGhPZ4zFUq5nUyhTeDaPFgQYmEqk-Ch3E6xr-Q', # Brain_v1.3 DRAFT
        'gid': '2056967441',
      },
      'old': {
        'sheetId': '1Dzbu_yNfQ-AyOgiScZq7rcoG4oINqO1qEU-MnEE4mPw', # Brain_v1.2 DRAFT
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
        'sheetId': '1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs', # Eye_v1.2 DRAFT
        'gid': '695483621',
      },
      'old': {
        'sheetId': '1SFGfjkZeDxY_9FaQqNERzq4XRjWDUpwKC9FCqONlbuk', # Eye_v1.1 DRAFT
        'gid': '695483621',
      }
    },
    'Fallopian_tube': {
      'new': {
        'sheetId': '16DHu7R9MC2B_fP7uRiDYcDIUvFs6SwHmZWgwpzuJwfI', # Fallopian_Tube_v1.2 DRAFT
        'gid': '991519552',
      },
      'old': {
        'sheetId': '1DFGmDSU75eMF6Fgwzk7W2u20DGJRdXN00TP7sO3kTug', # Fallopian_Tube_v1.1 DRAFT
        'gid': '991519552',
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
        'sheetId': '1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg', # Kidney_v1.3 DRAFT
        'gid': '949267305',
      },
      'old': {
        'sheetId': '1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw', # Kidney_v1.2 DRAFT
        'gid': '949267305',
      }
    },
    'Knee': {
      'new': {
        'sheetId': '1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc', # Knee_v1.2 DRAFT
        'gid': '1815525900',
      },
      'old': {
        'sheetId': '1zDCnaoMdSx09OGxjeeG2Sxokw4c_0bnNyDOJC6IMPCw', # Knee_v1.1 DRAFT
        'gid': '1815525900',
      }
    },
    'Large_intestine': {
      'new': {
        'sheetId': '1DgN9i72VFDmGwynStGbhkpHfas_RA9ccIrDgI77ULJA', # Large_Intestine_v1.3 DRAFT
        'gid': '2043181688',
      },
      'old': {
        'sheetId': '1d_KWKnQq3HT5nzDmfhlvFG4P_qdviu0vyhGZ6QHgNIk', # Large_Intestine_v1.2 DRAFT
        'gid': '2043181688',
      }
    },
    'Liver': {
      'new': {
        'sheetId': '1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ', # Liver_v1.2 DRAFT
        'gid': '1694828397',
      },
      'old': {
        'sheetId': '1F8ZXt1naE1pJFjfsAd6wK7x22D3qRW5O0E2d9gUKAik', # Liver_v1.1 DRAFT
        'gid': '1694828397',
      }
    },
    'Lung': {
      'new': {
        'sheetId': '1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY', # Lung_v1.3 DRAFT
        'gid': '1523836586',
      },
      'old': {
        'sheetId': '1iF4vx9EuQ2tQMBOm6awd9sf-2e_EHsPlcgzrF_YDtis', # Lung_v1.2 DRAFT
        'gid': '1523836586',
      }
    },
    'Lymph_node': {
      'new': {
        'sheetId': '15iuKGfnSjBbLd--873MKX2N0GgGKbXXk2dfzisiS-wg', # Lymph_Node_v1.3 DRAFT
        'gid': '1223566381',
      },
      'old': {
        'sheetId': '1_VWj_dD1dbmnBf8t0wptXvpy1oyyllZ1tXc0aKo2MSA', # Lymph_Node_v1.2 DRAFT
        'gid': '1223566381',
      }
    },
    'Lymph_vasculature': {
      'new': {
        'sheetId': '1x2U09QKAkxGFI4d24JN6YSzEZruYHJi96PlDIT3c1pU', # Lymph_Vasculature_v1.2 DRAFT
        'gid': '2087685463',
      },
      'old': {
        'sheetId': '1FNoQthhgP0OXEZuwIVL0XZA8SVYzCcVPm4_n20dt--8', # Lymph_Vasculature_v1.1 DRAFT
        'gid': '2087685463',
      }
    },
    'Ovary': {
      'new': {
        'sheetId': '1bPMrORa7CQa2JpVkRF_jHmA_GdS1qBryXl9riMZUBJU', # Ovary_v1.2 DRAFT
        'gid': '756296951',
      },
      'old': {
        'sheetId': '1K5LWhMaT_IryNxuK1Vko0Ud49VUB8RnMltL5jYhJUak', # Ovary_v1.1 DRAFT
        'gid': '756296951',
      }
    },
    'Pancreas': {
      'new': {
        'sheetId': '1Ksn6FuMqIcZFXorMfM5gsuZugKESabQmwvIAwYksdRE', # Pancreas_v1.2 DRAFT
        'gid': '439021026',
      },
      'old': {
        'sheetId': '1_cmA0CWUzVz1lNMpNOXqzrnmWgXv3GANqN7W18N4crA', # Pancreas_v1.1 DRAFT
        'gid': '439021026',
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
        'sheetId': '1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4', # Placenta_v1.1 DRAFT
        'gid': '231591207',
      },
      'old': {
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
        'sheetId': '1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw', # Skin_v1.3 DRAFT
        'gid': '269383687',
      },
      'old': {
        'sheetId': '16E07Ia3opnjBzBVswS7iQccd2Y_fw7m8-mNUNjwv80E', # Skin_v1.2 DRAFT
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
    'Spinal_Cord': {
      'new': {
        'sheetId': '1B8Yacpa0S_KuNqGGtKb83HTodKY_XGnIMy8tFCEIEdE', # Spinal_Cord_v1.0 DRAFT
        'gid': '243784891',
      }
    },
    'Spleen': {
      'new': {
        'sheetId': '1AEKYXAKP1oRM2krnbU_Un89JfxYEm_gjjwwJTEt1SiI', # Sleen_v1.3 DRAFT
        'gid': '69626346',
      },
      'old': {
        'sheetId': '1bairJs37srg0hF4MGIfsdtb000YtrA1hI45D8KI5Gxc', # Sleen_v1.2 DRAFT
        'gid': '69626346',
      }
    },
    'Thymus': {
      'new': {
        'sheetId': '13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM', # Thymus_v1.3 DRAFT
        'gid': '863370556',
      },
      'old': {
        'sheetId': '14KY4dp6YwVf0GSiCOcxhuy9L_aJ8FjTX_jidrIq7E_c', # Thymus_v1.2 DRAFT
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
        'sheetId': '1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig', # Uterus_v1.2 DRAFT
        'gid': '603441642',
      },
      'old': {
        'sheetId': '1RasOQCB4oP_1kvZL7Xv40TID6_365FQ-cgX2fGR54gw', # Uterus_v1.1 DRAFT
        'gid': '603441642',
      }
    }
}

def main(args):
  if eval(args.old_version):
    version = JOB_SHEET_GID_MAPPING[args.job]["old"]
  else:
    version = JOB_SHEET_GID_MAPPING[args.job]["new"]

  API_URL = f'https://asctb-api.herokuapp.com/v2/{version["sheetId"]}/{version["gid"]}'

  data = requests.get(API_URL).text
  data = json.loads(data)


  table_date = "NA"
  table_version = "NA"

  if data["metadata"]["date"] != '':
    try:
      table_date = datetime.datetime.strptime(data["metadata"]["date"], '%m/%d/%Y').strftime('%Y-%m-%d')
    except:
      table_date = data["metadata"]["date"]
  if data["metadata"]["version"] != '':
    table_version = data["metadata"]["version"]
      
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