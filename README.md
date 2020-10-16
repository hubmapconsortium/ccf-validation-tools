# CCF_tools [![Build Status](https://travis-ci.com/obophenotype/CCF_tools.svg?branch=master)](https://travis-ci.com/obophenotype/CCF_tools)

Some simple wrapper code for testing the part/is_a relationships implicit in ASCT-b tables for validity against Uberon and CL and using these to produce OWL via [ROBOT templates](http://robot.obolibrary.org/template).  Two OWL files are produced - one OWL file following OBO standards, and one simple RDF representation with 


![image](https://user-images.githubusercontent.com/112839/95355967-0ecc2380-08be-11eb-85ab-6dea787e43a5.png)


To run, you will need [ROBOT](http://robot.obolibrary.org/) installed + a python 3.8 environment with the contents of requirements.txt installed.  From the command line run:

```sh
$ cd src 
$ make all
```

### Example output files:
  - [class_template_Kidney_partonomy.tsv](https://github.com/obophenotype/CCF_tools/blob/master/src/class_template_Kidney_partonomy.tsv)
  - [ccf_spleen_classes.owl](https://github.com/obophenotype/CCF_tools/blob/master/src/ccf_spleen_classes.owl)
  - [ind_template_Kidney_partonomy.tsv](https://github.com/obophenotype/CCF_tools/blob/master/src/ind_template_Kidney_partonomy.tsv)
  - [ccf_spleen_ind.owl](https://github.com/obophenotype/CCF_tools/blob/master/src/ccf_spleen_ind.owl)
  
![image](https://user-images.githubusercontent.com/112839/96257807-f1304580-0fb2-11eb-8f94-90ca0891bfc7.png)
![image](https://user-images.githubusercontent.com/112839/96257876-0ad18d00-0fb3-11eb-8062-8449cb2c7dc7.png)
![image](https://user-images.githubusercontent.com/112839/96257915-19b83f80-0fb3-11eb-9c0d-dcd97e50eb4d.png)


### Example report


```
template_generation_tools.py:32: UserWarning: Not adding olabel            kidney
slabel            ureter
o         UBERON:0002113
s         UBERON:0000056
Name: 9, dtype: object - relationship not valid in Uberon/CL
  warnings.warn("Not adding %s - relationship not valid in Uberon/CL" % str(r))
  
/template_generation_tools.py:32: UserWarning: Not adding olabel            kidney
slabel      renal tubule
o         UBERON:0002113
s         UBERON:0009773

Name: 13, dtype: object - relationship not valid in Uberon/CL
  warnings.warn("Not adding %s - relationship not valid in Uberon/CL" % str(r))

template_generation_tools.py:32: UserWarning: Not adding olabel                       renal tubule
slabel    collecting duct of renal tubule
o                          UBERON:0009773
s                          UBERON:0001232
Name: 22, dtype: object - relationship not valid in Uberon/CL
  warnings.warn("Not adding %s - relationship not valid in Uberon/CL" % str(r))
```

Translation: There is no valid (part_of or is_a) relationship between ureter and kidney, between 'renal tubule' and kidney or between 'collecting duct of renal tubule' and 'renal tubule'.  The first one makes obvious sense - not all parts of the ureter are part of the kidney.  We could request that uberon includes this  overlaps relationship.  The second 2 are odd, but a quick look at Uberon makes the reason clear: 

![image](https://user-images.githubusercontent.com/112839/96254209-d4910f00-0fac-11eb-9faa-8aa07c121423.png)

renal tubule is too general (used for species with no kidney!).  This can be fixed instead by mapping to 'nephron tubule'





