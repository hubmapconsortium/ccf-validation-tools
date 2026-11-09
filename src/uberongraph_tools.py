import json
import os
import subprocess
import tempfile

from SPARQLWrapper import SPARQLWrapper, JSON, RDFXML
from rdflib.graph import ConjunctiveGraph, Graph
from ccf_tools import chunks, transform_to_str

UBERGRAPH_ENDPOINT = 'https://ubergraph.apps.renci.org/sparql'
_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_JOURNAL = os.path.join(_SRC_DIR, '..', 'ubergraph', 'ubergraph-subset.jnl')
DEFAULT_RUNNER = os.path.join(_SRC_DIR, 'tools', 'blazegraph-runner-1.7', 'bin', 'blazegraph-runner')

# Effectively "no chunking" when querying a local journal: chunking only exists
# to keep HTTP requests to the public endpoint small.
_NO_CHUNKING = 10 ** 9


def _chunked(items, size):
  """Split items into lists of at most `size` elements."""
  return list(chunks(list(items), size))


class UberonGraph():
    """
    Queries Ubergraph either through the public SPARQL endpoint ("remote") or
    against a local copy of the Ubergraph Blazegraph journal using
    blazegraph-runner ("local").

    Environment variables:
      UBERGRAPH_BACKEND  local | remote (default: local if the journal exists)
      UBERGRAPH_JOURNAL  path to the journal (default: ../ubergraph/ubergraph-subset.jnl,
                       built by build_ubergraph_subset.sh)
      BLAZEGRAPH_RUNNER  path to the blazegraph-runner executable
    """
    def __init__(self):
        self.journal = os.path.abspath(os.environ.get('UBERGRAPH_JOURNAL', DEFAULT_JOURNAL))
        self.runner = os.environ.get('BLAZEGRAPH_RUNNER', DEFAULT_RUNNER)
        default_backend = 'local' if os.path.exists(self.journal) else 'remote'
        self.backend = os.environ.get('UBERGRAPH_BACKEND', default_backend)
        if self.backend not in ('local', 'remote'):
          raise ValueError(f"UBERGRAPH_BACKEND must be 'local' or 'remote', not {self.backend!r}")
        if self.backend == 'local' and not os.path.exists(self.journal):
          raise FileNotFoundError(f"Ubergraph journal not found: {self.journal} (run 'make ubergraph-journal')")

        if self.backend == 'local':
          self.chunk_pairs = self.chunk_terms = self.chunk_construct = self.chunk_construct_ct = _NO_CHUNKING
        else:
          self.chunk_pairs = 90         # VALUES pairs/terms per SELECT
          self.chunk_terms = 90
          self.chunk_construct = 30     # subjects/objects per CONSTRUCT
          self.chunk_construct_ct = 20  # CT subjects in the CT suggestion CONSTRUCT

        self.sparql = SPARQLWrapper(UBERGRAPH_ENDPOINT)
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
        if self.backend == 'local':
          raise NotImplementedError("ASK queries are not supported by blazegraph-runner")
        self.sparql.setReturnFormat(JSON)
        self.sparql.setQuery(q)
        results = self.sparql.query().convert()
        return results["boolean"]

    def query_uberon(self, terms, query):
      query = query % terms

      print(query)

      results = self._select(query)
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

      return self._construct(construct_query)

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
        return self._construct(construct_query)

    def _run_local(self, command, query, outformat, suffix):
      """Run a blazegraph-runner command against the local journal and return the output file's text."""
      with tempfile.TemporaryDirectory(prefix='ubergraph-') as tmp:
        query_file = os.path.join(tmp, 'query.rq')
        output_file = os.path.join(tmp, 'result' + suffix)
        with open(query_file, 'w', encoding='utf-8') as f:
          f.write(query)
        # Capture Blazegraph's startup banner/log4j noise; show it only on failure.
        proc = subprocess.run([self.runner, f'--journal={self.journal}', f'--outformat={outformat}',
                               command, query_file, output_file],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if proc.returncode != 0:
          raise RuntimeError(f"blazegraph-runner {command} failed ({proc.returncode}):\n{proc.stdout}")
        with open(output_file, encoding='utf-8') as f:
          return f.read()

    def _select(self, query):
      """Run a SPARQL SELECT; returns SPARQL 1.1 JSON results as a dict."""
      if self.backend == 'local':
        return json.loads(self._run_local('select', query, 'json', '.json'))
      self.sparql.setReturnFormat(JSON)
      self.sparql.setQuery(query)
      return self.sparql.query().convert()

    def _construct(self, query):
      """Run a SPARQL CONSTRUCT; returns an rdflib Graph."""
      if self.backend == 'local':
        graph = Graph()
        graph.parse(data=self._run_local('construct', query, 'rdfxml', '.rdf'), format='xml')
        return graph
      self.sparql.setReturnFormat(RDFXML)
      self.sparql.setQuery(query)
      return self.sparql.query().convert()

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
      for chunk in _chunked(terms_pairs, self.chunk_pairs):
        valid_relationship = valid_relationship.union(self.query_uberon(" ".join(chunk), relationship))

      non_valid_relationship = terms_pairs - transform_to_str(valid_relationship)

      return valid_relationship, non_valid_relationship

    def get_suggestion_graph(self, all_as, terms_as_d, all_ct, terms_ct, terms_ct_d):
      sec_graph = ConjunctiveGraph()
      for chunk_all in _chunked(all_as, self.chunk_construct):
        objects = "\n".join(chunk_all)
        for chunk in _chunked(terms_as_d, self.chunk_construct):
          subjects = "\n".join(chunk)
          sec_graph += self.construct_relation(subject=subjects, objects=objects, property="rdfs:subClassOf")
          sec_graph += self.construct_relation(subject=subjects, objects=objects, property="part_of:")
          sec_graph += self.construct_relation(subject=subjects, objects=objects, property="connected_to:")
        for chunk in _chunked(terms_ct, self.chunk_construct):
          sec_graph += self.construct_relation(subject="\n".join(chunk), objects=objects, property="part_of:")

      for chunk in _chunked(terms_ct_d, self.chunk_construct_ct):
        for chunk_all in _chunked(all_ct, self.chunk_pairs):
          sec_graph += self.construct_relation(subject="\n".join(chunk), objects="\n".join(chunk_all), property="rdfs:subClassOf")

      return sec_graph

    def get_annotations(self, terms):
      annotations = ConjunctiveGraph()
      for chunk in _chunked(terms, self.chunk_construct):
        annotations += self.construct_annotation("\n".join(chunk))

      return annotations
