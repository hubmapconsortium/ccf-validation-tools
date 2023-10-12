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
                ?uberon foaf:depiction ?url_uri .
            
            }
            WHERE {
                ?x rdf:type ccf:spatial_entity, ?uberon .
                ?x ccf:has_object_reference [
                    ccf:file_url ?url
                ]
                FILTER (STRSTARTS(STR(?uberon), "http://purl.obolibrary.org/obo/UBERON_")) .
                BIND(STRDT(STR(?url), xsd:anyURI) as ?url_uri) .
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

if __name__ == '__main__':
    images_link = get_images_link()

    images_link.serialize('../owl/hra_uberon_3d_images.owl', format='xml')            
