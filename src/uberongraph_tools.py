from SPARQLWrapper import SPARQLWrapper, JSON

class UberonGraph():
    def __init__(self):
        self.sparql = SPARQLWrapper('https://stars-app.renci.org/uberongraph/sparql')
        self.sparql.setReturnFormat(JSON)
        self.ask_uberon_po = """
PREFIX part_of: <http://purl.obolibrary.org/obo/BFO_0000050> 
PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
ASK
FROM <http://reasoner.renci.org/ontology>
FROM <http://reasoner.renci.org/redundant>
{ %s part_of: %s }"""
        self.ask_uberon_overlaps = """
PREFIX overlaps: <http://purl.obolibrary.org/obo/RO_0002131> 
PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
ASK
FROM <http://reasoner.renci.org/ontology>
FROM <http://reasoner.renci.org/redundant>
 { %s overlaps: %s }"""

        self.ask_uberon_subclassof = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
ASK FROM <http://reasoner.renci.org/ontology/closure>
    { %s rdfs:subClassOf %s }"""

    def ask_uberon(self, r, q, urls=True):
        """"""
        start = ''
        end = ''
        if urls:
            start = '<'
            end = '>'
        q = q % (start + r['s'] + end, start + r['o'] + end)
        self.sparql.setQuery(q)
        results = self.sparql.query().convert()
        return results['boolean']