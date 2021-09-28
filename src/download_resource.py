import argparse
import urllib.request

SHEET_ID = "1tK916JyG5ZSXW_cXfsyZnzXfjyoN-8B2GXLbYD6_vF0"

JOB_SHEET_GID_MAPPING = {
    'Brain': '345174398', # Brain_v1
    'Heart': '1240281363', # Heart_v1
    'Kidney': '1760639962', # Kidney_v1
    'Large_intestine': '1687995716', # Large_Intestine_v1 
    'Lung': '925712902', # Lung_v1
    'Lymph_node': '272157091', # Lymph_Node_v1
    'Skin': '104836770', # Skin_v1
    'Spleen': '22580074', # Sleen_v1
    'Thymus': '314238819', # Thymus_v1
    'Vasculature': '1896956438' # Vasculature_v1
}

parser = argparse.ArgumentParser()
parser.add_argument('job', help='job to download')
parser.add_argument('output_file', help='output file path')

args = parser.parse_args()

file = urllib.request.urlopen(f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={JOB_SHEET_GID_MAPPING[args.job]}')

content = file.read()
f = open(args.output_file, 'wb')
f.write(content)
f.close()