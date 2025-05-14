from SPARQLWrapper import SPARQLWrapper, JSON, RDFXML
from rdflib.graph import ConjunctiveGraph
from ccf_tools import chunks, transform_to_str

class UberonGraph():
    def __init__(self):
        self.sparql = SPARQLWrapper('https://ubergraph.apps.renci.org/sparql')
        self.sparql.setMethod('POST')
        self.select_po = """
          PREFIX part_of: <http://purl.obolibrary.org/obo/BFO_0000050> 
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
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
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
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
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/redundant>
          { 
            VALUES (?subject ?object) {
              %s
            }
            ?subject rdfs:subClassOf ?object .
            FILTER (?subject != ?object)
          }"""

        self.select_class = """
          PREFIX owl: <http://www.w3.org/2002/07/owl#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
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
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
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
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
          SELECT ?subject ?object 
          {
            VALUES ?subject {
              %s
            }
            ?subject rdfs:label ?object . 
          }
        """

        self.select_develops_from = """
          PREFIX develops_from: <http://purl.obolibrary.org/obo/RO_0002202>
          PREFIX owl: <http://www.w3.org/2002/07/owl#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
          SELECT ?subject ?object 
          FROM <http://reasoner.renci.org/redundant> 
          {
            VALUES (?subject ?object) {
              %s
            }
            ?subject develops_from: ?object .
          }
        """
         
        self.select_po_nonredundant = """
          PREFIX part_of: <http://purl.obolibrary.org/obo/BFO_0000050> 
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
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
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
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
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/ontology>
          { 
            VALUES (?subject ?object) {
              %s
            }
            ?subject rdfs:subClassOf ?object .
            FILTER (?subject != ?object)
          }
        """

        self.select_subclass_po = """
          PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
          PREFIX part_of: <http://purl.obolibrary.org/obo/BFO_0000050>
          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/ontology>
          FROM <http://reasoner.renci.org/redundant>
          { 
            VALUES (?subject ?object) {
              %s
            }
            ?sub rdfs:subClassOf ?subject .
            ?sub part_of: ?object .
            FILTER (?sub != ?subject)
          }
        """
        
        self.select_has_part = """
          PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
          PREFIX has_part: <http://purl.obolibrary.org/obo/BFO_0000051>
          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/ontology>
          FROM <http://reasoner.renci.org/redundant>
          { 
            VALUES (?subject ?object) {
              %s
            }
            ?object has_part: ?subject .
          }
        """         

        self.select_image = """
          PREFIX foaf: <http://xmlns.com/foaf/0.1/>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
          SELECT ?subject ?object
          { 
            VALUES ?subject {
              %s
            }
            ?subject foaf:depicted_by ?object .
          }
        """

        self.select_ontology_version = """
          PREFIX owl: <http://www.w3.org/2002/07/owl#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/uberon/uberon-base.owl>
          PREFIX CL: <http://purl.obolibrary.org/obo/cl/cl-base.owl>
          PREFIX PCL: <http://purl.obolibrary.org/obo/pcl/pcl-base.owl>
          SELECT ?subject ?object
          WHERE {
            VALUES ?subject { UBERON: CL: PCL: }
            ?subject owl:versionInfo ?object
          }
        """

        self.select_located_in = """
          PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
          PREFIX located_in: <http://purl.obolibrary.org/obo/RO_0001025>
          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/ontology>
          FROM <http://reasoner.renci.org/redundant>
          { 
            VALUES (?subject ?object) {
              %s
            }
            ?subject located_in: ?object .
          }
        """     
        self.select_normalized_ic = """
          PREFIX normalizedIC: <http://reasoner.renci.org/vocab/normalizedInformationContent>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>

          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/ontology>
          {
            VALUES ?subject {
              %s
            }
            ?subject normalizedIC: ?object .
          }
        """
        self.select_continuous_with = """
          PREFIX continuous_with: <http://purl.obolibrary.org/obo/RO_0002150>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>

          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/redundant>
          {
            VALUES (?subject ?object) {
              %s
            }
            ?subject continuous_with: ?object .
          }
        """
        self.select_connects = """
          PREFIX connects: <http://purl.obolibrary.org/obo/RO_0002176>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>

          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/redundant>
          {
            VALUES (?subject ?object) {
              %s
            }
            ?subject connects: ?object .
          }
        """
        self.select_surrounds = """
          PREFIX surrounds: <http://purl.obolibrary.org/obo/RO_0002221>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>

          SELECT ?subject ?object
          FROM <http://reasoner.renci.org/redundant>
          {
            VALUES (?subject ?object) {
              %s
            }
            ?subject surrounds: ?object .
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

      print(query)
      
      results = self.sparql.query().convert()
      if results["results"]["bindings"]:
        return self.extract_results(results["results"]["bindings"])
      else:
        return set()

    def construct_relation(self, subject, objects, property):
      extential_rel = """
        rdfs:subClassOf [
            rdf:type owl:Restriction;
            owl:onProperty {property} ;
            owl:someValuesFrom ?object
          ]
      """.format(property=property)

      subclass_rel = """
        rdfs:subClassOf ?object .
      """

      construct_query = """
          PREFIX owl: <http://www.w3.org/2002/07/owl#>
          PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
          PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
          PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
          PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
          PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
          PREFIX part_of: <http://purl.obolibrary.org/obo/BFO_0000050> 
          PREFIX connected_to: <http://purl.obolibrary.org/obo/RO_0002170>
          PREFIX develops_from: <http://purl.obolibrary.org/obo/RO_0002202>
          PREFIX overlaps: <http://purl.obolibrary.org/obo/RO_0002131> 
          CONSTRUCT 
          {{
            ?subject rdf:type owl:Class; 
              {relationship}
          }}
            WHERE {{
              GRAPH <http://reasoner.renci.org/redundant> {{ 
                VALUES ?subject {{
                  {subject}    
                }}
                VALUES ?object {{
                  {objects}
                }}
                ?subject {property} ?object .
              }}
              FILTER(?subject != ?object)
            }}
      """.format(subject = subject, objects = objects, relationship = subclass_rel if property == "rdfs:subClassOf" else extential_rel, property = property)

      self.sparql.setQuery(construct_query)
      self.sparql.setReturnFormat(RDFXML)
      result = self.sparql.query().convert()

      return result

    def construct_annotation(self, terms):
        construct_query = """
              PREFIX owl: <http://www.w3.org/2002/07/owl#>
              PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
              PREFIX UBERON: <http://purl.obolibrary.org/obo/UBERON_>
              PREFIX CL: <http://purl.obolibrary.org/obo/CL_>
              PREFIX PCL: <http://purl.obolibrary.org/obo/PCL_>
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
                  OPTIONAL {{
                    ?AP rdf:type owl:AnnotationProperty; ?APP ?APPV .
                    ?APP rdf:type owl:AnnotationProperty .
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
      return term.replace("http://purl.obolibrary.org/obo/UBERON_", "UBERON:").replace("http://purl.obolibrary.org/obo/CL_", "CL:").replace("http://purl.obolibrary.org/obo/PCL_", "PCL:")

    def add_prefix_ont(self, list_ontology):
      results = []
      for ont, version in list_ontology:
        ont = ont.replace("http://purl.obolibrary.org/obo/uberon/uberon-base.owl", "UBERON").replace("http://purl.obolibrary.org/obo/cl/cl-base.owl", "CL").replace("http://purl.obolibrary.org/obo/pcl/pcl-base.owl", "PCL")
        results.extend([ont, version])
      return results

    def verify_relationship(self, terms_pairs, relationship):
      valid_relationship = set()
      if len(terms_pairs) > 90:
        for chunk in chunks(list(terms_pairs), 90):
          valid_relationship = valid_relationship.union(self.query_uberon(" ".join(chunk), relationship))
      else:
        valid_relationship = self.query_uberon(" ".join(list(terms_pairs)), relationship)
      
      non_valid_relationship = terms_pairs - transform_to_str(valid_relationship)

      return valid_relationship, non_valid_relationship

    def get_suggestion_graph(self, all_as, terms_as_d, all_ct, terms_ct, terms_ct_d):
      sec_graph = ConjunctiveGraph()
      if len(all_as) > 30:
        for chunk_all in chunks(list(all_as), 30):
          if len(terms_as_d) > 30:
            for chunk in chunks(list(terms_as_d), 30):
              sec_graph += self.construct_relation(subject="\n".join(chunk), objects="\n".join(chunk_all), property="rdfs:subClassOf")
              sec_graph += self.construct_relation(subject="\n".join(chunk), objects="\n".join(chunk_all), property="part_of:")
              sec_graph += self.construct_relation(subject="\n".join(chunk), objects="\n".join(chunk_all), property="connected_to:")
          else:
            sec_graph += self.construct_relation(subject="\n".join(list(terms_as_d)), objects="\n".join(chunk_all), property="rdfs:subClassOf")
            sec_graph += self.construct_relation(subject="\n".join(list(terms_as_d)), objects="\n".join(chunk_all), property="part_of:")
            sec_graph += self.construct_relation(subject="\n".join(list(terms_as_d)), objects="\n".join(chunk_all), property="connected_to:")

          if len(terms_ct) > 30:
            for chunk in chunks(list(terms_ct), 30):
              sec_graph += self.construct_relation(subject="\n".join(chunk), objects="\n".join(chunk_all), property="part_of:")
          else:
            sec_graph += self.construct_relation(subject="\n".join(terms_ct), objects="\n".join(chunk_all), property="part_of:")
      else:
        if len(terms_as_d) > 30:
          for chunk in chunks(list(terms_as_d), 30):
            sec_graph += self.construct_relation(subject="\n".join(chunk), objects="\n".join(list(all_as)), property="rdfs:subClassOf")
            sec_graph += self.construct_relation(subject="\n".join(chunk), objects="\n".join(list(all_as)), property="part_of:")
            sec_graph += self.construct_relation(subject="\n".join(chunk), objects="\n".join(list(all_as)), property="connected_to:")
        else:
          sec_graph += self.construct_relation(subject="\n".join(list(terms_as_d)), objects="\n".join(list(all_as)), property="rdfs:subClassOf")
          sec_graph += self.construct_relation(subject="\n".join(list(terms_as_d)), objects="\n".join(list(all_as)), property="part_of:")
          sec_graph += self.construct_relation(subject="\n".join(list(terms_as_d)), objects="\n".join(list(all_as)), property="connected_to:")
        
        if len(terms_ct) > 30:
          for chunk in chunks(list(terms_ct), 30):
            sec_graph += self.construct_relation(subject="\n".join(chunk), objects="\n".join(list(all_as)), property="part_of:")
        else:
          sec_graph += self.construct_relation(subject="\n".join(terms_ct), objects="\n".join(list(all_as)), property="part_of:")
        

      if len(terms_ct_d) > 20:
        for chunk in chunks(list(terms_ct_d), 20):
          if len(all_ct) > 90:
            for chunck in chunks(list(all_ct), 90):
              sec_graph += self.construct_relation(subject="\n".join(chunk), objects="\n".join(list(chunck)), property="rdfs:subClassOf")
          else:
            sec_graph += self.construct_relation(subject="\n".join(chunk), objects="\n".join(list(all_ct)), property="rdfs:subClassOf")
      else:
        if len(all_ct) > 90:
            for chunck in chunks(list(all_ct), 90):
              sec_graph += self.construct_relation(subject="\n".join(terms_ct_d), objects="\n".join(list(chunck)), property="rdfs:subClassOf")
        else:
          sec_graph += self.construct_relation(subject="\n".join(terms_ct_d), objects="\n".join(list(all_ct)), property="rdfs:subClassOf")
        

      return sec_graph

    def get_annotations(self, terms):
      annotations = ConjunctiveGraph()
      terms = list(terms)
      if len(terms) > 30:
        for chunk in chunks(terms, 30):
          annotations += self.construct_annotation("\n".join(chunk))
      else:
        terms = "\n".join(terms)
        annotations = self.construct_annotation(terms)

      return annotations
