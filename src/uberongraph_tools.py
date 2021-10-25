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

        self.select_overlaps = """
          PREFIX overlaps: <http://purl.obolibrary.org/obo/RO_0002131> 
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

        self.select_subclass = """
          PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
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

        self.select_class = """
          PREFIX owl: <http://www.w3.org/2002/07/owl#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          SELECT ?subject
          FROM <http://reasoner.renci.org/ontology>
          { 
            VALUES ?subject {
              %s
            }
            FILTER NOT EXISTS { ?subject a owl:Class . }
          }"""

        self.select_ct = """
          PREFIX connected_to: <http://purl.obolibrary.org/obo/RO_0002170> 
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
        
        self.select_label = """
          PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
          PREFIX owl: <http://www.w3.org/2002/07/owl#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          SELECT ?subject ?object 
          {
            VALUES ?subject {
              %s
            }
            ?subject rdfs:label ?object . 
          }
        """

        self.select_po_nonredundant = """
          PREFIX part_of: <http://purl.obolibrary.org/obo/BFO_0000050> 
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/nonredundant>
          { 
            VALUES (?subject ?object) {
              %s
            }
            ?subject part_of: ?object .
          }
        """

        self.select_overlaps_nonredundant = """
          PREFIX overlaps: <http://purl.obolibrary.org/obo/RO_0002131> 
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/nonredundant>
          { 
            VALUES (?subject ?object) {
              %s
            }
            ?subject overlaps: ?object .
          }
        """

        self.select_subclass_ontology = """
          PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/ontology>
          { 
            VALUES (?subject ?object) {
              %s
            }
            ?subject rdfs:subClassOf ?object .
          }
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
        return results["boolean"]

    def query_uberon(self, terms, query):
      query = query % terms
      self.sparql.setReturnFormat(JSON)
      self.sparql.setQuery(query)
      
      results = self.sparql.query().convert()
      if results["results"]["bindings"]:
        return self.extract_results(results["results"]["bindings"])
      else:
        return set()

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

    def extract_results(self, list):
      results = set()
      for r in list:
        if r.get("object"):
          results.add((self.add_prefix(r["subject"]["value"]), self.add_prefix(r["object"]["value"])))
        else:
          results.add(self.add_prefix(r["subject"]["value"]))
      return results

    def add_prefix(self, term):
      return term.replace("http://purl.obolibrary.org/obo/UBERON_", "UBERON:").replace("http://purl.obolibrary.org/obo/CL_", "CL:")

