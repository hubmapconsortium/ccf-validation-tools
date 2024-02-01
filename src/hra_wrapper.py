import pandas as pd
from SPARQLWrapper import JSON, RDFXML, SPARQLWrapper


class HRAWrapper():
    def __init__(self):
        self.sparql = SPARQLWrapper("https://lod.humanatlas.io/sparql")
        self.construct_images_uberon = """
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX obo: <http://purl.obolibrary.org/obo/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX ccf: <http://purl.org/ccf/>
            PREFIX anatomical_entity: <http://purl.obolibrary.org/obo/UBERON_0001062>

            CONSTRUCT {
            ?uberon foaf:depiction ?url_uri .
            }
            WHERE {
            ?uberon rdfs:subClassOf anatomical_entity: .
            ?x a owl:NamedIndividual .
            ?x rdf:type ccf:SpatialEntity .
            ?x rdf:type ?uberon .
            ?x ccf:representation_of ?uberon .
            ?x ccf:has_object_reference [
                ccf:file_url ?url
            ] .
            FILTER (CONTAINS(STR(?url), "https://cdn.humanatlas.io/digital-objects/ref-organ/"))
            FILTER (!CONTAINS(STR(?url), "https://cdn.humanatlas.io/digital-objects/ref-organ/united"))
            BIND(STRDT(STR(?url), xsd:anyURI) as ?url_uri) .
            }
        """
        self.reference_organ_spatial_entity = """
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX obo: <http://purl.obolibrary.org/obo/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX ccf: <http://purl.org/ccf/>
            PREFIX anatomical_entity: <http://purl.obolibrary.org/obo/UBERON_0001062>

            SELECT ?representation_of ?glb_file
            WHERE {
                ?uberon rdfs:subClassOf anatomical_entity: .
                ?x a owl:NamedIndividual .
                ?x rdf:type ccf:SpatialEntity .
                ?x rdf:type ?uberon .
                ?x ccf:representation_of ?uberon .
                ?x ccf:has_object_reference [
                    ccf:file_url ?url
                ] .
                FILTER (CONTAINS(STR(?url), "https://cdn.humanatlas.io/digital-objects/ref-organ/"))
                FILTER (!CONTAINS(STR(?url), "https://cdn.humanatlas.io/digital-objects/ref-organ/united"))
                BIND(?uberon as ?representation_of) .
                BIND(?url as ?glb_file) .
            }
            ORDER BY ?representation_of
        """
    
    def query_hra(self, query, format):
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(format=format)
        result = self.sparql.query().convert()
        
        return result
    
    def extract_result(self, results):
        results_simplified = []
        for res in results:
            r = {}
            for key, value in res.items():
                r[key] = value["value"]
            results_simplified.append(r)
        return results_simplified


if __name__ == '__main__':
    hra = HRAWrapper()
    images_link = hra.query_hra(hra.construct_images_uberon, RDFXML)
    images_link_table = hra.extract_result(
        hra.query_hra(
            hra.reference_organ_spatial_entity, JSON
        )["results"]["bindings"]
    )

    images_link.serialize('../owl/hra_uberon_3d_images.owl', format='xml')
    pd.DataFrame.from_records(images_link_table).to_csv("../logs/hra_uberon_3d_ref_objects.csv", index=False)
