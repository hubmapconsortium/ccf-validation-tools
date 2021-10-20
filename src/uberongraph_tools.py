from SPARQLWrapper import SPARQLWrapper, JSON, RDFXML

class UberonGraph():
    def __init__(self):
        self.sparql = SPARQLWrapper('https://stars-app.renci.org/uberongraph/sparql')
        self.select_po = """
          PREFIX part_of: <http://purl.obolibrary.org/obo/BFO_0000050> 
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/ontology>
          FROM <http://reasoner.renci.org/redundant>
          { 
            VALUES (?subject ?object) {
              %s
            }
            ?subject part_of: ?object .
          }
        """

        self.select_overlaps = """PREFIX overlaps: <http://purl.obolibrary.org/obo/RO_0002131> 
PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
SELECT ?subject ?object
FROM <http://reasoner.renci.org/ontology>
FROM <http://reasoner.renci.org/redundant>
{ 
  VALUES (?subject ?object) {
    %s
  }
  ?subject overlaps: ?object .
}"""

        self.select_subclass = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
SELECT ?subject ?object
FROM <http://reasoner.renci.org/ontology/closure>
{ 
  VALUES (?subject ?object) {
    %s
  }
  ?subject rdfs:subClassOf ?object .
}"""

        # self.select_class = """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        #   PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
        #   PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
        #   SELECT ?subject
        #   FROM <http://reasoner.renci.org/ontology>
        #   { 
        #     VALUES ?subject {
        #       %s
        #     }
        #     ?subject a owl:Class .
        #   }"""

        self.ask_uberon_class = """
          PREFIX owl: <http://www.w3.org/2002/07/owl#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          ASK 
          FROM <http://reasoner.renci.org/ontology>
          { %s a owl:Class . }
        """

        self.select_ct = """PREFIX connected_to: <http://purl.obolibrary.org/obo/RO_0002170> 
PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
SELECT ?subject ?object
FROM <http://reasoner.renci.org/ontology>
FROM <http://reasoner.renci.org/redundant> 
{ 
  VALUES (?subject ?object) {
    %s
  }
  ?subject connected_to: ?object .
}"""

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
        return results["results"]["bindings"][0]["label"]["value"]

    def query_uberon(self, terms, query):
      query = query % terms
      self.sparql.setReturnFormat(JSON)
      self.sparql.setQuery(query)
      
      results = self.sparql.query().convert()
      if results["results"]["bindings"]:
        return results["results"]["bindings"]
      else:
        return set()

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
            SELECT ?label 
            WHERE {{ {term} rdfs:label ?label . }}
        """.format(term = term)

        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        result = self.sparql.query().convert()
        return result["results"]["bindings"][0]["label"]["value"]

