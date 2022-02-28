# CCF_tools [![Build Status](https://github.com/obophenotype/CCF_tools/workflows/CI/badge.svg)](https://github.com/obophenotype/CCF_tools/actions?query=workflow%3ACI)

Some simple wrapper code for testing the part/is_a relationships implicit in ASCT-b tables for validity against Uberon and CL and using these to produce OWL via [ROBOT templates](http://robot.obolibrary.org/template). One OWL file is produced following OBO standards.


![image](https://user-images.githubusercontent.com/112839/95355967-0ecc2380-08be-11eb-85ab-6dea787e43a5.png)


To run, you will need [ROBOT](http://robot.obolibrary.org/) installed + a python 3.8 environment with the contents of requirements.txt installed.  From the command line run:

```sh
$ cd src 
$ make all
```

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





