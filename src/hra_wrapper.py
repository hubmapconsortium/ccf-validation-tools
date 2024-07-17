"""
Description: This script is used to query the Human Reference Atlas (HRA)
SPARQL endpoint to get the 3D images of the reference organs.
"""
import pandas as pd
from rdflib.graph import ConjunctiveGraph
from SPARQLWrapper import JSON, RDFXML, SPARQLWrapper

REF_ORGAN_BASE_URI = "https://purl.humanatlas.io/ref-organ/"
GRAPH_NAME_LIST = [
    "brain-female",
    "brain-male",
    "blood-vasculature-female",
    "blood-vasculature-male",
    "eye-female-left",
    "eye-female-right",
    "eye-male-left",
    "eye-male-right",
    "fallopian-tube-female-left",
    "fallopian-tube-female-right",
    "heart-female",
    "heart-male",
    "kidney-female-left",
    "kidney-female-right",
    "kidney-male-left",
    "kidney-male-right",
    "knee-female-left",
    "knee-female-right",
    "knee-male-left",
    "knee-male-right",
    "large-intestine-female",
    "large-intestine-male",
    "larynx-female",
    "larynx-male",
    "liver-female",
    "liver-male",
    "lung-female",
    "lung-male",
    "lymph-node-female",
    "lymph-node-male",
    "main-bronchus-female",
    "main-bronchus-male",
    "mammary-gland-female-left",
    "mammary-gland-female-right",
    "ovary-female-left",
    "ovary-female-right",
    "palatine-tonsil-female-left",
    "palatine-tonsil-female-right",
    "palatine-tonsil-male-left",
    "palatine-tonsil-male-right",
    "pancreas-female",
    "pancreas-male",
    "pelvis-female",
    "pelvis-male",
    "placenta-full-term-female",
    "prostate-male",
    "skin-female",
    "skin-male",
    "small-intestine-female",
    "small-intestine-male",
    "spinal-cord-female",
    "spinal-cord-male",
    "spleen-female",
    "spleen-male",
    "thymus-female",
    "thymus-male",
    "trachea-female",
    "trachea-male",
    "ureter-female-left",
    "ureter-female-right",
    "ureter-male-left",
    "ureter-male-right",
    "urinary-bladder-female",
    "urinary-bladder-male",
    "uterus-female"
]


class HRAWrapper():
    """
    Class to query the Human Reference Atlas (HRA) SPARQL endpoint.
    """
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

            CONSTRUCT {{
                ?uberon foaf:depiction ?url_uri .
            }}
            WHERE {{
                GRAPH {graph_name} {{
                    ?uberon rdfs:subClassOf* anatomical_entity: .
                    ?x rdf:type ccf:SpatialEntity .
                    ?x rdf:type ?uberon .
                    ?x ccf:representation_of ?uberon .
                    ?x ccf:has_object_reference [
                        ccf:file_url ?url
                    ] .
                    BIND(STRDT(STR(?url), xsd:anyURI) as ?url_uri) .
                }}
            }}
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

            SELECT DISTINCT ?representation_of ?glb_file
            WHERE {{
                GRAPH {graph_name} {{
                    ?uberon rdfs:subClassOf* anatomical_entity: .
                    ?x rdf:type ccf:SpatialEntity .
                    ?x rdf:type ?uberon .
                    ?x ccf:representation_of ?uberon .
                    ?x ccf:has_object_reference [
                        ccf:file_url ?url
                    ] .
                    BIND(?uberon as ?representation_of) .
                    BIND(?url as ?glb_file) .
                }}
            }}
        """

    def query_hra(self, query, format_result):
        """
        Query the HRA SPARQL endpoint and return the results.
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(format=format_result)
        result = self.sparql.query().convert()

        return result

    def extract_result(self, results):
        """
        Extract the results from the query in a simplified format.
        """
        results_simplified = []
        for res in results:
            r = {}
            for key, value in res.items():
                r[key] = value["value"]
            results_simplified.append(r)
        return results_simplified


if __name__ == '__main__':
    hra = HRAWrapper()
    images_link = ConjunctiveGraph()
    images_link_table = []
    for graph_name in GRAPH_NAME_LIST:
        graph_iri = f"<{REF_ORGAN_BASE_URI}{graph_name}>"

        images_link += hra.query_hra(
            hra.construct_images_uberon.format(graph_name=graph_iri),
            RDFXML
        )
        ilt = hra.extract_result(
                hra.query_hra(
                    hra.reference_organ_spatial_entity.format(
                        graph_name=graph_iri
                    ),
                    JSON
                )["results"]["bindings"]
            )
        if ilt:
            images_link_table.extend(ilt)

    images_link.serialize("../owl/hra_uberon_3d_images.owl", format="xml")
    pd.DataFrame.from_records(images_link_table)\
        .sort_values(by="representation_of")\
        .to_csv("../reports/hra_uberon_3d_ref_objects.csv", index=False)
