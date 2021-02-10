from template_generation_tools import generate_class_graph_template, generate_ind_graph_template
from ccf_tools import parse_ASCTb
import argparse
import os
print(os.getcwd())
parser = argparse.ArgumentParser()
parser.add_argument('--test', help='Run in test mode.',
                    action="store_true")  # Not doing anything with this yet.
parser.add_argument("target_file", help='input file path')
parser.add_argument("output_file", help='output file path')
parser.add_argument("--ind", help='write ind template',
                    action="store_true", default=False)


args = parser.parse_args()

if args.ind:
    generate_ind_graph_template(parse_ASCTb(args.target_file)).to_csv(args.output_file,
                                                                      sep='\t',
                                                                      index=False)
else:
    class_graph_template_dfs = generate_class_graph_template(parse_ASCTb(args.target_file))
    class_graph_template_dfs[0].to_csv(args.output_file,
                                       sep='\t',
                                       index=False)

    class_graph_template_dfs[1].to_csv(args.output_file + ".log",
                                       sep='\t',
                                       index=False)




