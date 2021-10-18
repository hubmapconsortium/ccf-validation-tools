from SPARQLWrapper import SPARQLWrapper, JSON, RDFXML

class UberonGraph():
    def __init__(self):
        self.sparql = SPARQLWrapper('https://stars-app.renci.org/uberongraph/sparql')
        self.ask_uberon_po = """
PREFIX part_of: <http://purl.obolibrary.org/obo/BFO_0000050> 
PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
PREFIX FMA: <http://purl.obolibrary.org/obo/FMA_>
ASK
FROM <http://reasoner.renci.org/ontology>
FROM <http://reasoner.renci.org/redundant>
{ %s part_of: %s }"""
        self.ask_uberon_overlaps = """
PREFIX overlaps: <http://purl.obolibrary.org/obo/RO_0002131> 
PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
PREFIX FMA: <http://purl.obolibrary.org/obo/FMA_>
ASK
FROM <http://reasoner.renci.org/ontology>
FROM <http://reasoner.renci.org/redundant>
 { %s overlaps: %s }"""

        self.ask_uberon_subclassof = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
PREFIX FMA: <http://purl.obolibrary.org/obo/FMA_>
ASK FROM <http://reasoner.renci.org/ontology/closure>
    { %s rdfs:subClassOf %s }"""

        self.ask_uberon_class = """
          PREFIX owl: <http://www.w3.org/2002/07/owl#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          ASK 
          FROM <http://reasoner.renci.org/ontology>
          { %s a owl:Class . }
        """

    def ask_uberon(self, r, q, urls=True):
        """"""
        start = ''
        end = ''
        if urls:
            start = '<'
            end = '>'
        q = q % (start + r['s'] + end, start + r['o'] + end)
        self.sparql.setReturnFormat(JSON)
        self.sparql.setQuery(q)
        results = self.sparql.query().convert()
        return results['boolean']

    def is_valid_class(self, query, entity):
        query = query % (entity)
        self.sparql.setReturnFormat(JSON)
        self.sparql.setQuery(query)
        results = self.sparql.query().convert()
        return results['boolean']

    def construct_annotation(self, terms):
        construct_query = """
              PREFIX owl: <http://www.w3.org/2002/07/owl#>
              PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
              PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
              PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
              CONSTRUCT 
              {{
                ?term rdf:type owl:Class; ?APT ?APVT .
                ?APT rdf:type owl:AnnotationProperty .
                ?AP rdf:type owl:AnnotationProperty; ?APP ?APPV .
                ?APP rdf:type owl:AnnotationProperty .
                ?a a owl:Axiom; owl:annotatedProperty ?AP; owl:annotatedSource ?term; owl:annotatedTarget ?APV; ?p ?o .
                ?p rdf:type owl:AnnotationProperty .
              }}
                WHERE {{
                  VALUES ?term {{
                    {terms}    
                  }}
                  ?term rdf:type owl:Class; ?APT ?APVT .
                  ?APT rdf:type owl:AnnotationProperty .
                  ?AP rdf:type owl:AnnotationProperty; ?APP ?APPV .
                  ?APP rdf:type owl:AnnotationProperty .
                  OPTIONAL {{
                    ?a a owl:Axiom; owl:annotatedProperty ?AP; owl:annotatedSource ?term; owl:annotatedTarget ?APV; ?p ?o .
                    ?p rdf:type owl:AnnotationProperty .
                }}
              }}
            """.format(terms = terms)
        self.sparql.setQuery(construct_query)
        self.sparql.setReturnFormat(RDFXML)
        result = self.sparql.query().convert()
        return result

    def get_label_from_uberon(self, term):
        query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
            PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
            SELECT ?label 
            WHERE {{ {term} rdfs:label ?label . }}
        """.format(term = term)

        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        result = self.sparql.query().convert()

        if len(result["results"]["bindings"]) > 0:
            return result["results"]["bindings"][0]["label"]["value"]
        else:
            return "Label not found"

