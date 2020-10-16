# CCF_tools [![Build Status](https://travis-ci.com/obophenotype/CCF_tools.svg?branch=master)](https://travis-ci.com/obophenotype/CCF_tools)

Some simple wrapper code for testing the part relationships implicit in ASCT-b tables for validity against Uberon and CL and using these to produce OWL via [ROBOT templates](http://robot.obolibrary.org/template).  Two OWL files are produced - one OWL file following OBO standards, and one simple RDF representation with 


![image](https://user-images.githubusercontent.com/112839/95355967-0ecc2380-08be-11eb-85ab-6dea787e43a5.png)


To run, you will need [ROBOT](http://robot.obolibrary.org/) installed + a python 3.8 environment with the contents of requirements.txt installed.  From the command line run:

$ cd src 
$ make all

Example output files:
  - [class_template_Kidney_partonomy.tsv](https://github.com/obophenotype/CCF_tools/blob/master/src/class_template_Kidney_partonomy.tsv)
  - [ccf_spleen_classes.owl](https://github.com/obophenotype/CCF_tools/blob/master/src/ccf_spleen_classes.owl)
  - [ind_template_Kidney_partonomy.tsv](https://github.com/obophenotype/CCF_tools/blob/master/src/ind_template_Kidney_partonomy.tsv)
  - [ccf_spleen_ind.owl](https://github.com/obophenotype/CCF_tools/blob/master/src/ccf_spleen_ind.owl)









