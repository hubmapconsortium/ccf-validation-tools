# CCF_tools [![Build Status](https://github.com/obophenotype/CCF_tools/workflows/CI/badge.svg)](https://github.com/obophenotype/CCF_tools/actions?query=workflow%3ACI)

Some simple wrapper code for testing the part/is_a relationships implicit in ASCT-b tables for validity against Uberon and CL and using these to produce OWL via [ROBOT templates](http://robot.obolibrary.org/template). One OWL file is produced following OBO standards.


![image](https://user-images.githubusercontent.com/112839/95355967-0ecc2380-08be-11eb-85ab-6dea787e43a5.png)


To run, you will need [ROBOT](http://robot.obolibrary.org/) installed + a python 3.8 environment with the contents of requirements.txt installed.  From the command line run:

```sh
$ cd src 
$ make all
```

### Ubergraph queries (local subset journal)

Validation queries run against a local subset of [Ubergraph](https://github.com/INCATools/ubergraph) using
[blazegraph-runner](https://github.com/balhoff/blazegraph-runner) instead of the public SPARQL endpoint.
The subset (`ubergraph/ubergraph-subset.jnl`, ~1.5 GB) holds only what the queries need: UBERON/CL/PCL terms,
the inferred edges between them, their annotations and information content. It is built by
`src/build_ubergraph_subset.sh`, which downloads Ubergraph's N-Quads dump (~4 GB), filters it with
`src/ubergraph_subset.py` and loads the result into the same named graphs Ubergraph uses, so query results match.

- `make ubergraph-journal` builds the subset if it is missing (Java 11 + `pip install rapidgzip`)
- `make refresh-ubergraph` rebuilds it from the latest Ubergraph release

In GitHub Actions the journal is cached (`.github/actions/ubergraph-subset`) and only rebuilt when Ubergraph
publishes a new dump or the build scripts change.

Environment variables: `UBERGRAPH_BACKEND=local|remote` (`remote` uses `https://ubergraph.apps.renci.org/sparql`
and skips the build), `UBERGRAPH_JOURNAL`, `BLAZEGRAPH_RUNNER`. Blazegraph opens the journal
read-write and locks it, so it must be writable and local builds can't run in parallel (`make -j`).

#### What the subset contains

| Named graph | Contents |
|---|---|
| `http://reasoner.renci.org/ontology` | Triples whose subject is a UBERON/CL/PCL term: labels, `rdfs:subClassOf`, information content, ... |
| `http://reasoner.renci.org/redundant` | Inferred relations (all predicates) where both subject and object are UBERON/CL/PCL terms |
| `http://reasoner.renci.org/nonredundant` | The same, for non-redundant relations |
| `http://purl.org/ccf/ubergraph-subset/union` | Everything else the queries without `FROM` read from Ubergraph's union of all graphs: term triples from the per-ontology graphs (e.g. `foaf:depicted_by`), `owl:Axiom` annotations on terms, annotation property declarations, and the `owl:versionInfo` of the UBERON/CL/PCL base ontologies |

Triples whose object is a blank node (OWL restrictions) are left out, except inside `owl:Axiom` annotations.

**When changing queries:** a query that only uses UBERON/CL/PCL terms and the graphs above works unchanged. A query
that needs anything else, such as another ontology prefix or OWL restriction structure, needs a matching change to
`src/ubergraph_subset.py`. Changing that file (or `build_ubergraph_subset.sh`) changes the CI cache key, so the next
CI run rebuilds the journal. To check that the subset still gives the same results as Ubergraph itself:

```
cd src
python compare_ubergraph_backends.py ../resources/ASCT-b_tables/Kidney.json --a local --b remote
```

`--b` can also be a path to the full Ubergraph journal
([ubergraph.jnl.gz](https://ubergraph.apps.renci.org/downloads/current/), 79 GB uncompressed), which is a better
reference when the public endpoint runs a different Ubergraph release than the subset.

### Example output file:
  - [ccf_Spleen_classes.owl](https://github.com/hubmapconsortium/ccf-validation-tools/blob/master/owl/ccf_Spleen_classes.owl)
 
 
#### Example heirarchy in OWL (classes)
![image](https://user-images.githubusercontent.com/112839/96257807-f1304580-0fb2-11eb-8f94-90ca0891bfc7.png)

#### Example axiom in OWL
![image](https://user-images.githubusercontent.com/112839/96257876-0ad18d00-0fb3-11eb-8062-8449cb2c7dc7.png)

#### Example annotation of OWL axiom - showing confirmed status as valid in Uberon
![image](https://user-images.githubusercontent.com/112839/96257915-19b83f80-0fb3-11eb-9c0d-dcd97e50eb4d.png)


### Reports

Example report listing not valid relationships
https://github.com/hubmapconsortium/ccf-validation-tools/blob/master/logs/class_Kidney_log.tsv


s | slabel | user_slabel | o | olabel | user_olabel
-- | -- | -- | -- | -- | --
  | UBERON:0001284 | renal column | renal column (column of Bertin) | UBERON:0000362 | renal medulla | renal medulla
  | CL:0000653 | glomerular visceral epithelial cell | glomerular visceral epithelial cell | UBERON:0006852 | glomerular visceral epithelium | glomerular visceral epithelium

Translation: There is no valid (part_of or is_a) relationship between 'renal column' and 'renal medulla' or between 'glomerular visceral epithelial cell' and 'glomerular visceral epithelium'.  





