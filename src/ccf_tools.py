import pandas as pd
import rdflib

def parse_CCF_tsv(path):
    ccf_tsv = pd.read_csv(path, sep='\t', skipinitialspace=True)
    lookup = ccf_tsv[['ID', 'Label (indented)']]
    part_cols = ccf_tsv.drop(columns=['ID', 'Label (indented)'])
    out = pd.DataFrame(columns=['o', 's', 'olabel', 'slabel'])
    col_pairs = []
    for current, nekst in zip(part_cols.columns, part_cols.columns[1:]):
        col_pair = part_cols[[current, nekst]].drop_duplicates().dropna().rename(columns={current: 'olabel', nekst: 'slabel'})
        col_pairs.append(col_pair)
    out = pd.concat(col_pairs, ignore_index=True)
    fu = out.merge(lookup, left_on=['olabel'], right_on='Label (indented)').drop(columns=['Label (indented)']).rename(columns={'ID': 'o'})
    bar = fu.merge(lookup, left_on=['slabel'], right_on='Label (indented)').drop(columns=['Label (indented)']).rename(columns={'ID': 's'})
    return bar

def get_ccf_owl():
    g = rdflib.Graph()
    g.parse('http://purl.org/ccf/latest/ccf.owl')
    return g

def ccf_owl_2_part_rels():
    g = get_ccf_owl()
    ccf_po_query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX ccf: <https://purl.org/ccf/latest/ccf.owl#> 
SELECT DISTINCT ?o ?s ?olabel ?slabel
   WHERE { ?s ccf:ccf_part_of ?o . 
           ?o rdfs:label ?olabel .
           ?s rdfs:label ?slabel .
       FILTER(STRSTARTS(STR(?o), "http://purl.obolibrary.org/obo/UBERON_")) 
       FILTER(STRSTARTS(STR(?s), "http://purl.obolibrary.org/obo/UBERON_")) 
    }"""
    return g.query(ccf_po_query)


def invalid_relationship_report(row, relations):
    return "No valid relationshp between %s ; %s and %s %s (checked for: %s) " \
          "" % (row['slabel'], row['s'], row['olabel'], row['o'], str(relations))