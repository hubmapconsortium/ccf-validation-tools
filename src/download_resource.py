import argparse
import urllib.request

SHEET_ID = "1tK916JyG5ZSXW_cXfsyZnzXfjyoN-8B2GXLbYD6_vF0"

JOB_SHEET_GID_MAPPING = {
    'Brain': '1379088218', # Brain_v1.1
    'Bone-Marrow_Blood': '1845311048', # Bone Marrow_Blood_v1.1 
    'Heart': '2133445058', # Heart_v1.1
    'Kidney': '2137043090', # Kidney_v1.1
    'Large_intestine': '512613979', # Large_Intestine_v1.1 
    'Lung': '1824552484', # Lung_v1.1
    'Lymph_node': '1440276882', # Lymph_Node_v1.1
    'Skin': '1158675184', # Skin_v1.1
    'Spleen': '984946629', # Sleen_v1.1
    'Thymus': '1823527529', # Thymus_v1.1
    'Vasculature': '361657182' # Vasculature_v1.1
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