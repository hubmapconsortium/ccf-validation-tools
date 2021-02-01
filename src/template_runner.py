from template_generation_tools import generate_class_graph_template, generate_ind_graph_template
from ccf_tools import parse_ASCTb
import argparse
import os
print(os.getcwd())
parser = argparse.ArgumentParser()
parser.add_argument('--test', help='Run in test mode.',
                    action="store_true") # Not doing anything with this yet.
parser.add_argument("target_file")

args = parser.parse_args()

generate_class_graph_template(parse_ASCTb(args.target_file)).to_csv(
    "../templates/class_template_" + args.target_file.split('/')[-1], sep='\t', index=False)
generate_ind_graph_template(parse_ASCTb(args.target_file)).to_csv(
    "../templates/ind_template_" + args.target_file.split('/')[-1], sep='\t', index=False)




