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





