import time
from ccf_tools import ccf_owl_2_part_rels, parse_CCF_tsv
from uberongraph_tools import UberonGraph
import pandas as pd


def validate_ccf_po(ccf_po, urls=True):
    ug = UberonGraph()
    passing = len(ccf_po)
    for r in ccf_po:
        fillers = (r['slabel'], r['s'], r['olabel'], r['o'])
        if ug.ask_uberon(r, ug.ask_uberon_po, urls):
            r['part_of'] = True
        else:
            passing -= 1
            r['part_of'] = False
            if ug.ask_uberon(r, ug.ask_uberon_subclassof, urls):
                print('Uberon supports [%s](%s) subClassOf [%s](%s), not part_of' % fillers)
                r['subClassOf'] = True
            elif ug.ask_uberon(r, ug.ask_uberon_overlaps, urls):
                print('Uberon supports [%s](%s) overlaps [%s](%s), but not part_of' % fillers)
                r['overlaps'] = True
                r['subClassOf'] = False

            else:
                print('Uberon does not (currently) support [%s](%s) part_of [%s](%s).' % fillers)
                r['part_of'] = False
                r['subClassOf'] = False
        time.sleep(0.02)  # Seems the server doesn't like  to be hit too often
    print("%d ccf_part_of relationship validated by Uberon" % passing)
    return ccf_po


#validate_ccf_po(ccf_owl_2_part_rels())
ccf_tab = parse_CCF_tsv('./resources/Kidney_partonomy.tsv')
input = [r for i, r in ccf_tab.iterrows()]
report = pd.DataFrame.from_records(validate_ccf_po(input, urls=False)).fillna(False)
report.to_excel('kidney_partonomy_report.xlsx', index=False)
ccf_tab = parse_CCF_tsv('./resources/Spleen_partonomy.tsv')
input = [r for i, r in ccf_tab.iterrows()]
report = pd.DataFrame.from_records(validate_ccf_po(input, urls=False)).fillna(False)
report.to_excel('spleen_partonomy_report.xlsx', index=False)
