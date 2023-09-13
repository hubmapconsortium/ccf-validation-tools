
ASCT+B Validation Reports for Eye (2023-09-13)
==============================================

Table of contents
=================

* [Invalid terms](#invalid-terms)
	* [Terms not found](#terms-not-found)
	* [Typos or punctuation mistakes](#typos-or-punctuation-mistakes)
	* [Different labels](#different-labels)
	* [Blank ontology ID](#blank-ontology-id)
	* [Terms from another ontology](#terms-from-another-ontology)
* [Relationship reports](#relationship-reports)
	* [How to read a table entry](#how-to-read-a-table-entry)
	* [Relationship AS-AS report](#relationship-as-as-report)
	* [Relationship CT-CT report](#relationship-ct-ct-report)
	* [Relationship CT-AS report](#relationship-ct-as-report)
* [New CL terms](#new-cl-terms)
* [New UBERON terms](#new-uberon-terms)
* [Informative reports (valid relationships)](#informative-reports-valid-relationships)
	* [Indirect relationship](#indirect-relationship)
	* [Relationship AS has part CT](#relationship-as-has-part-ct)

# Invalid terms


These are the reports related to issues in the terms found in the ASCT+B table. We validate only [CL](https://www.ebi.ac.uk/ols/ontologies/cl), [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) and [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) terms.
## Terms not found


This report provides a list of terms not found neither in UBERON nor in CL. Please remove these terms from the ASCT+B table - disconsider this message if a term was recently added to the ontology.  
  
- No issues found.


## Typos or punctuation mistakes


This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.  
  
- No issues found.


## Different labels


This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.

If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.

If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.  
  
1. In row _[34](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=34:34)_, the term _[UBERON:0004864](http://purl.obolibrary.org/obo/UBERON_0004864)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _vasculature of retina _ and the one in the **ontology** is _vasculature of retina_. For reference, the given name/label **by SMEs** is _vasculature_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[13](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=13:13)_, no term id was found for the name/label _glutamic acid decarboxylase 65 cell_.

1. In row _[14](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=14:14)_, no term id was found for the name/label _A8 bistratified small-field cell_.

1. In row _[16](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=16:16)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[16](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=16:16)_, no term id was found for the name/label _semilunar type 1 cell_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=17:17)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=17:17)_, no term id was found for the name/label _semilunar type 3 cell_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=18:18)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=18:18)_, no term id was found for the name/label _semilunar cell_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=46:46)_, no term id was found for the name/label _Inner cortex_.

1. In row _[47](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=47:47)_, no term id was found for the name/label _Outer cortex_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=53:53)_, no term id was found for the name/label _Outer cortex_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=64:64)_, no term id was found for the name/label _glial cell_.

1. In row _[65](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=65:65)_, no term id was found for the name/label _glial cell_.

1. In row _[73](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=73:73)_, no term id was found for the name/label _conjuctival epithelium_.

1. In row _[74](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=74:74)_, no term id was found for the name/label _limbal stem cells_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
- No issues found.


# Relationship reports


These reports are other representations of the ASCT+B table. We split each row into pairs with adjacent terms, resulting in a table with two primary columns, object (o), left side and subject (s), right side. The experts' labels for the subject and object are in the columns user_slabel and user_olabel. The other columns are the subject label (s_label) and object label (o_label), the label from the source ontologies.

The report means it could not find a partonomy relationship in the source ontologies, but it doesn't mean this relationship is entirely invalid. In some cases, the pair is in the *inverse order*. In other cases, the relationship is *missing* in the source ontologies. Finally, how it was modelled in the ASCT+B table is not aligned with the ontologies sources and needs a more general discussion.
## How to read a table entry


**In the ASCT+B table**




|AS/2|AS/2/LABEL|AS/2/ID|AS/3|AS/3/LABEL|AS/3/ID|
| :---: | :---: | :---: | :---: | :---: | :---: |
|lens|lens|UBERON:0000965|ciliary zonules|suspensory ligament of lens|UBERON:0006762|






**In the Relationship Report**




|s|slabel|user_slabel|o|olabel|user_olabel|
| :---: | :---: | :---: | :---: | :---: | :---: |
|UBERON:0006762|suspensory ligament of lens|ciliary zonules|UBERON:0000965|lens|lens|





## Relationship AS-AS report


This table contains terms for anatomical structures that are related to each other according to the ASCT+B table but are not related to each other in source ontologies via one of the relation types we consider valid for ASCT+B tables. Valid relationships are: *part_of*, e.g. corneal endothelium part_of cornea; *subClassOf*, e.g. left kidney subClassOf (is_a) kidney; and *overlaps* (has some part in), e.g. ureter overlaps kidney; *connected_to*, e.g. TBA. *part_of* and *subClassOf* relationships should be specific to general, e.g. left kidney (specific) to kidney (general); corneal endothelium (specific) to cornea (general). The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



|    | s              | slabel                                             | user_slabel                                        | o              | olabel                                             | user_olabel                                        | row_number                                                                                                               |       deltaIC |
|----|----------------|----------------------------------------------------|----------------------------------------------------|----------------|----------------------------------------------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------|
|  2 | UBERON:0002203 | vasculature of eye                                 | vasculature of eye                                 | UBERON:0000966 | retina                                             | retina                                             | [32](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=32:32) | 145.309       |
|  4 | UBERON:0004904 | neuron projection bundle connecting eye with brain | optic nerve                                        | UBERON:0000970 | eye                                                | eye                                                | [64](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=64:64) |   5.78978e-12 |
|  5 | UBERON:0004904 | neuron projection bundle connecting eye with brain | optic nerve                                        | UBERON:0000970 | eye                                                | eye                                                | [65](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=65:65) |   5.78978e-12 |
|  6 | UBERON:0004904 | neuron projection bundle connecting eye with brain | optic nerve                                        | UBERON:0000970 | eye                                                | eye                                                | [66](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=66:66) |   5.78978e-12 |
|  7 | UBERON:0004904 | neuron projection bundle connecting eye with brain | optic nerve                                        | UBERON:0000970 | eye                                                | eye                                                | [67](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=67:67) |   5.78978e-12 |
|  8 | UBERON:0004904 | neuron projection bundle connecting eye with brain | optic nerve                                        | UBERON:0000970 | eye                                                | eye                                                | [68](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=68:68) |   5.78978e-12 |
|  9 | UBERON:0004904 | optic nerve                                        | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye                                                | eye                                                | [70](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=70:70) |   5.78978e-12 |
| 11 | UBERON:0000482 | basal lamina of epithelium                         | basal epithelium                                   | UBERON:0006761 | corneo-scleral junction                            | corneoscleral limbus                               | [74](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=74:74) |   2.06914e-14 |
| 12 | UBERON:0002276 | lamina of spiral limbus                            | lamina of spiral limbus                            | UBERON:0000970 | eye                                                | eye                                                | [74](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=74:74) |   2.8026e-45  |
| 32 | UBERON:0035966 | scleral lamina cribrosa                            | scleral lamina cribrosa                            | UBERON:0004904 | neuron projection bundle connecting eye with brain | optic nerve                                        | [65](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=65:65) | nan           |
| 33 | UBERON:0001773 | sclera                                             | sclera                                             | UBERON:0004904 | neuron projection bundle connecting eye with brain | optic nerve                                        | [66](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=66:66) | nan           |
| 34 | UBERON:0003902 | retinal neural layer                               | retinal neural layer                               | UBERON:0004904 | neuron projection bundle connecting eye with brain | optic nerve                                        | [67](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=67:67) | nan           |
| 35 | UBERON:0034713 | cranial neuron projection bundle                   | nerve bundle                                       | UBERON:0004904 | neuron projection bundle connecting eye with brain | optic nerve                                        | [68](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=68:68) | nan           |
| 36 | UBERON:0006136 | unmyelinated nerve fiber                           | unmyelinated nerve bundles                         | UBERON:0004904 | optic nerve                                        | neuron projection bundle connecting eye with brain | [70](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=70:70) | nan           |
| 37 | UBERON:0006761 | corneo-scleral junction                            | corneoscleral limbus                               | UBERON:0002276 | lamina of spiral limbus                            | lamina of spiral limbus                            | [74](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=74:74) | nan           |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



|    | s          | slabel                           | user_slabel           | o          | olabel                             | user_olabel       | row_number                                                                                                               |   deltaIC |
|----|------------|----------------------------------|-----------------------|------------|------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
| 13 | CL:0011005 | GABAergic interneuron            | GABAergic interneuron | CL:0000561 | Amacrine Cell                      | Amacrine cell     | [13](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=13:13) |       nan |
| 15 | CL:0004253 | wide field retinal amacrine cell | wide field cell       | CL:0004252 | medium field retinal amacrine cell | medium-field cell | [15](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=15:15) |       nan |
| 26 | CL:0000129 | microglial cell                  | microglial cell       | CL:0000540 | neuron                             | Neuron            | [48](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=48:48) |       nan |
| 27 | CL:0000636 | Mueller cell                     | Muller glia           | CL:0000540 | neuron                             | Neuron            | [49](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=49:49) |       nan |




## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                | user_slabel               | o              | olabel                        | user_olabel                 | row_number                                                                                                               |       deltaIC |
|----|------------|---------------------------------------|---------------------------|----------------|-------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------|
|  0 | CL:0000669 | pericyte                              | Pericyte                  | UBERON:0004864 | vasculature of retina         | vasculature                 | [50](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=50:50) |   2.19717e+13 |
|  1 | CL:0002585 | retinal blood vessel endothelial cell | Endothelial Cell          | UBERON:0004864 | vasculature of retina         | vasculature                 | [34](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=34:34) |   2.19717e+13 |
|  3 | CL:0000129 | microglial cell                       | microglial cell           | UBERON:0000966 | retina                        | retina                      | [48](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=48:48) | 145.309       |
| 10 | CL:0002228 | primary lens fiber                    | primary lens fiber        | UBERON:0002444 | lens fiber                    | lens Fibers                 | [38](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=38:38) |   5.77623e-12 |
| 14 | CL:4030028 | glycinergic amacrine cell             | Glycinergic Amacrine Cell | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [14](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=14:14) | nan           |
| 16 | CL:0004253 | wide field retinal amacrine cell      | wide field cell           | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [15](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=15:15) | nan           |
| 17 | CL:0004219 | A2 amacrine cell                      | A2 cell                   | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [18](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=18:18) | nan           |
| 18 | CL:0004232 | starburst amacrine cell               | starburst amacrine cell   | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [19](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=19:19) | nan           |
| 19 | CL:0000573 | retinal cone cell                     | retinal cone cell         | UBERON:0001789 | outer nuclear layer of retina | outer nuclear layer         | [33](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=33:33) | nan           |
| 20 | CL:4023188 | Midget ganglion cell of retina        | Midget cell               | UBERON:0001792 | ganglionic layer of retina    | retinal ganglion cell layer | [35](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=35:35) | nan           |
| 21 | CL:4023189 | Parasol ganglion cell of retina       | Parasol cell              | UBERON:0001792 | ganglionic layer of retina    | retinal ganglion cell layer | [36](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=36:36) | nan           |
| 22 | CL:0002225 | secondary lens fiber                  | mature fiber cell         | UBERON:0000390 | lens nucleus                  | Fetal nucleus               | [44](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=44:44) | nan           |
| 23 | CL:0011004 | lens fiber cell                       | lens fiber cell           | UBERON:0000390 | lens nucleus                  | Adult nucleus               | [45](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=45:45) | nan           |
| 24 | CL:0011004 | lens fiber cell                       | lens fiber cell           | UBERON:0000389 | lens cortex                   | cortex                      | [46](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=46:46) | nan           |
| 25 | CL:0011004 | lens fiber cell                       | lens fiber cell           | UBERON:0000389 | lens cortex                   | cortex                      | [47](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=47:47) | nan           |
| 28 | CL:0000636 | Mueller cell                          | Muller glia               | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [49](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=49:49) | nan           |
| 29 | CL:0000604 | retinal rod cell                      | retinal rod cell          | UBERON:0001789 | outer nuclear layer of retina | outer nuclear layer         | [51](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=51:51) | nan           |
| 30 | CL:0002363 | keratocyte                            | keratocyte                | UBERON:0003952 | anterior stroma of cornea     | anterior stroma of cornea   | [56](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=56:56) | nan           |
| 31 | CL:0017004 | telocyte                              | telocyte                  | UBERON:0003952 | anterior stroma of cornea     | anterior stroma of cornea   | [57](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=57:57) | nan           |




# New CL terms
[**Report**](new_cl_terms_Eye.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Eye.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Eye_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Eye_AS_has_part_CT_log.tsv)