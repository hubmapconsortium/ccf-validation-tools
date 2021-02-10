# CCF_tools [![Build Status](https://github.com/obophenotype/CCF_tools/workflows/CI/badge.svg)](https://github.com/obophenotype/CCF_tools/actions?query=workflow%3ACI)

Some simple wrapper code for testing the part/is_a relationships implicit in ASCT-b tables for validity against Uberon and CL and using these to produce OWL via [ROBOT templates](http://robot.obolibrary.org/template).  Two OWL files are produced - one OWL file following OBO standards, and one simple RDF representation with CCF_part_of triples. 


![image](https://user-images.githubusercontent.com/112839/95355967-0ecc2380-08be-11eb-85ab-6dea787e43a5.png)


To run, you will need [ROBOT](http://robot.obolibrary.org/) installed + a python 3.8 environment with the contents of requirements.txt installed.  From the command line run:

```sh
$ cd src 
$ make all
```

### Example output files:
  - [class_template_Kidney_partonomy.tsv](https://github.com/obophenotype/CCF_tools/blob/master/src/templates/class_template_Kidney_partonomy.tsv)
  - [ccf_spleen_classes.owl](https://github.com/obophenotype/CCF_tools/blob/master/src/owl/ccf_spleen_classes.owl)
  - [ind_template_Kidney_partonomy.tsv](https://github.com/obophenotype/CCF_tools/blob/master/src/templates/ind_template_Kidney_partonomy.tsv)
  - [ccf_spleen_ind.owl](https://github.com/obophenotype/CCF_tools/blob/master/src/owl/ccf_spleen_ind.owl)
  
#### Example heirarchy in OWL (classes)
![image](https://user-images.githubusercontent.com/112839/96257807-f1304580-0fb2-11eb-8f94-90ca0891bfc7.png)

#### Example axiom in OWL
![image](https://user-images.githubusercontent.com/112839/96257876-0ad18d00-0fb3-11eb-8062-8449cb2c7dc7.png)

#### Example annotation of OWL axiom - showing confirmed status as valid in Uberon
![image](https://user-images.githubusercontent.com/112839/96257915-19b83f80-0fb3-11eb-9c0d-dcd97e50eb4d.png)


### [Reports](https://github.com/obophenotype/CCF_tools/blob/master/templates/)


Example 
https://github.com/obophenotype/CCF_tools/blob/master/templates/class_template_Kidney.tsv.log


s	| slabel	| user_slabel	| o	| olabel	| user_olabel
--|--|--|--|--|--
UBERON:0001284	| renal column (column of Bertin)	| renal column	| UBERON:0000362	| renal medulla	| renal medulla
UBERON:0001232	| collecting duct of renal tubule |	Collecting Duct (Medulla) |	UBERON:0001231	 |nephron tubule	| Tubules


Translation: There is no valid (part_of or is_a) relationship between 'renal column' and 'renal tubule' or between 'collecting duct of renal tubule' and 'renal tubule'.  




