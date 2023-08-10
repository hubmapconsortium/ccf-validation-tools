from SPARQLWrapper import SPARQLWrapper, RDFXML
from rdflib.graph import ConjunctiveGraph

class HRAWrapper():
    def __init__(self):
        self.sparql = SPARQLWrapper("https://lod.humanatlas.io/sparql")
        self.construct_images_uberon = """
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX obo: <http://purl.obolibrary.org/obo/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX ccf: <http://purl.org/ccf/>

            CONSTRUCT {
                ?uberon foaf:depiction ?url .
            
            }
            WHERE {
                ?x rdf:type ccf:spatial_entity, ?uberon .
                ?x ccf:has_object_reference [
                    ccf:file_url ?url
                ]
                FILTER (STRSTARTS(STR(?uberon), "http://purl.obolibrary.org/obo/UBERON_"))
            }
        """
    
    def query_hra(self, query) -> ConjunctiveGraph:
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(RDFXML)
        result = self.sparql.query().convert()
        
        return result
    
def get_images_link():
    hra = HRAWrapper()
    return hra.query_hra(hra.construct_images_uberon)
            
