
ASCT+B Validation Reports for Eye (2025-01-01)
==============================================

Table of contents
=================

* [Invalid terms](#invalid-terms)
	* [Terms not found](#terms-not-found)
	* [Typos or punctuation mistakes](#typos-or-punctuation-mistakes)
	* [Different labels](#different-labels)
	* [Blank ontology ID](#blank-ontology-id)
	* [Blank ontology ID missing parent](#blank-ontology-id-missing-parent)
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


These are the reports related to issues in the terms found in the ASCT+B table. We validate only [CL](https://www.ebi.ac.uk/ols4/ontologies/cl), [UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon) and [PCL](https://www.ebi.ac.uk/ols4/ontologies/pcl) terms.
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
  
- No issues found.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols4/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
1. No term id was found for the name/label _limbal stem cells_ in the following 1 row _[28](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=28:28)_.

1. No term id was found for the name/label _Inner cortex_ in the following 1 row _[36](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=36:36)_.

1. No term id was found for the name/label _Outer cortex_ in the following 2 rows _[37](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=37:37)_, _[38](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=38:38)_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
- No issues found.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Same case for Anatomic Ontology for Human Lung Maturation (LMHA) and Interlex IDs (ILX) from Stimulating Peripheral Activity to Relieve Conditions (SPARC). You can request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols4/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols4/ontologies/pcl).  
  
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



|    | s                                                               | slabel                           | user_slabel                | o                                                               | olabel                  | user_olabel             | row_number                                                                                                               |   deltaIC |
|----|-----------------------------------------------------------------|----------------------------------|----------------------------|-----------------------------------------------------------------|-------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
|  4 | [UBERON:0034713](http://purl.obolibrary.org/obo/UBERON_0034713) | cranial neuron projection bundle | nerve bundle               | [UBERON:0000941](http://purl.obolibrary.org/obo/UBERON_0000941) | cranial nerve II        | optic nerve             | [24](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=24:24) |  11.2345  |
| 10 | [UBERON:0003902](http://purl.obolibrary.org/obo/UBERON_0003902) | retinal neural layer             | retinal neural layer       | [UBERON:0000941](http://purl.obolibrary.org/obo/UBERON_0000941) | cranial nerve II        | optic nerve             | [23](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=23:23) |   3.54736 |
| 11 | [UBERON:0000482](http://purl.obolibrary.org/obo/UBERON_0000482) | basal lamina of epithelium       | basal epithelium           | [UBERON:0006761](http://purl.obolibrary.org/obo/UBERON_0006761) | corneo-scleral junction | corneoscleral limbus    | [28](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=28:28) |   2.21665 |
| 14 | [UBERON:0035966](http://purl.obolibrary.org/obo/UBERON_0035966) | scleral lamina cribrosa          | scleral lamina cribrosa    | [UBERON:0000941](http://purl.obolibrary.org/obo/UBERON_0000941) | cranial nerve II        | optic nerve             | [21](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=21:21) | nan       |
| 15 | [UBERON:0001773](http://purl.obolibrary.org/obo/UBERON_0001773) | sclera                           | sclera                     | [UBERON:0000941](http://purl.obolibrary.org/obo/UBERON_0000941) | cranial nerve II        | optic nerve             | [22](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=22:22) | nan       |
| 16 | [UBERON:0006136](http://purl.obolibrary.org/obo/UBERON_0006136) | unmyelinated nerve fiber         | unmyelinated nerve bundles | [UBERON:0000941](http://purl.obolibrary.org/obo/UBERON_0000941) | cranial nerve II        | optic nerve             | [25](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=25:25) | nan       |
| 17 | [UBERON:0002276](http://purl.obolibrary.org/obo/UBERON_0002276) | lamina of spiral limbus          | lamina of spiral limbus    | [UBERON:0000970](http://purl.obolibrary.org/obo/UBERON_0000970) | eye                     | eye                     | [28](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=28:28) | nan       |
| 18 | [UBERON:0006761](http://purl.obolibrary.org/obo/UBERON_0006761) | corneo-scleral junction          | corneoscleral limbus       | [UBERON:0002276](http://purl.obolibrary.org/obo/UBERON_0002276) | lamina of spiral limbus | lamina of spiral limbus | [28](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=28:28) | nan       |
| 21 | [UBERON:0002203](http://purl.obolibrary.org/obo/UBERON_0002203) | vasculature of eye               | vasculature of eye         | [UBERON:0000966](http://purl.obolibrary.org/obo/UBERON_0000966) | retina                  | retina                  | [61](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=61:61) | nan       |
| 30 | [UBERON:0000054](http://purl.obolibrary.org/obo/UBERON_0000054) | macula                           | macula                     | [UBERON:0000966](http://purl.obolibrary.org/obo/UBERON_0000966) | retina                  | retina                  | [75](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=75:75) | nan       |
| 31 | [UBERON:0018107](http://purl.obolibrary.org/obo/UBERON_0018107) | foveola of retina                | foveola of retina          | [UBERON:0000054](http://purl.obolibrary.org/obo/UBERON_0000054) | macula                  | macula                  | [75](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=75:75) | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



|    | s                                                       | slabel          | user_slabel     | o                                                       | olabel   | user_olabel   | row_number                                                                                                               |   deltaIC |
|----|---------------------------------------------------------|-----------------|-----------------|---------------------------------------------------------|----------|---------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
| 25 | [CL:0000129](http://purl.obolibrary.org/obo/CL_0000129) | microglial cell | microglial cell | [CL:0000540](http://purl.obolibrary.org/obo/CL_0000540) | neuron   | Neuron        | [68](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=68:68) |       nan |
| 27 | [CL:0000636](http://purl.obolibrary.org/obo/CL_0000636) | Mueller cell    | Muller glia     | [CL:0000540](http://purl.obolibrary.org/obo/CL_0000540) | neuron   | Neuron        | [69](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=69:69) |       nan |




## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                                | user_slabel               | o                                                               | olabel                        | user_olabel                 | row_number                                                                                                               |   deltaIC |
|----|---------------------------------------------------------|---------------------------------------|---------------------------|-----------------------------------------------------------------|-------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | [CL:0000125](http://purl.obolibrary.org/obo/CL_0000125) | glial cell                            | glial cell                | [UBERON:0035966](http://purl.obolibrary.org/obo/UBERON_0035966) | scleral lamina cribrosa       | scleral lamina cribrosa     | [21](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=21:21) |  49.0072  |
|  1 | [CL:0000125](http://purl.obolibrary.org/obo/CL_0000125) | glial cell                            | glial cell                | [UBERON:0018107](http://purl.obolibrary.org/obo/UBERON_0018107) | foveola of retina             | foveola of retina           | [75](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=75:75) |  49.0072  |
|  2 | [CL:0000036](http://purl.obolibrary.org/obo/CL_0000036) | epithelial fate stem cell             | epithelial fate stem cell | [UBERON:0000482](http://purl.obolibrary.org/obo/UBERON_0000482) | basal lamina of epithelium    | basal epithelium            | [28](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=28:28) |  19.0936  |
|  3 | [CL:0000125](http://purl.obolibrary.org/obo/CL_0000125) | glial cell                            | glial cell                | [UBERON:0000941](http://purl.obolibrary.org/obo/UBERON_0000941) | cranial nerve II              | optic nerve                 | [20](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=20:20) |  15.6972  |
|  5 | [CL:0000573](http://purl.obolibrary.org/obo/CL_0000573) | retinal cone cell                     | retinal cone cell         | [UBERON:0001789](http://purl.obolibrary.org/obo/UBERON_0001789) | outer nuclear layer of retina | outer nuclear layer         | [62](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=62:62) |  10.8188  |
|  6 | [CL:0000604](http://purl.obolibrary.org/obo/CL_0000604) | retinal rod cell                      | retinal rod cell          | [UBERON:0001789](http://purl.obolibrary.org/obo/UBERON_0001789) | outer nuclear layer of retina | outer nuclear layer         | [71](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=71:71) |   6.66433 |
|  7 | [CL:0011004](http://purl.obolibrary.org/obo/CL_0011004) | lens fiber cell                       | lens fiber cell           | [UBERON:0000390](http://purl.obolibrary.org/obo/UBERON_0000390) | lens nucleus                  | Adult nucleus               | [35](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=35:35) |   6.03643 |
|  8 | [CL:0011004](http://purl.obolibrary.org/obo/CL_0011004) | lens fiber cell                       | lens fiber cell           | [UBERON:0000389](http://purl.obolibrary.org/obo/UBERON_0000389) | lens cortex                   | cortex                      | [36](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=36:36) |   4.56639 |
|  9 | [CL:0011004](http://purl.obolibrary.org/obo/CL_0011004) | lens fiber cell                       | lens fiber cell           | [UBERON:0000389](http://purl.obolibrary.org/obo/UBERON_0000389) | lens cortex                   | cortex                      | [37](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=37:37) |   4.56639 |
| 12 | [CL:0002363](http://purl.obolibrary.org/obo/CL_0002363) | keratocyte                            | keratocyte                | [UBERON:0003952](http://purl.obolibrary.org/obo/UBERON_0003952) | anterior stroma of cornea     | anterior stroma of cornea   | [17](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=17:17) | nan       |
| 13 | [CL:0017004](http://purl.obolibrary.org/obo/CL_0017004) | telocyte                              | telocyte                  | [UBERON:0003952](http://purl.obolibrary.org/obo/UBERON_0003952) | anterior stroma of cornea     | anterior stroma of cornea   | [18](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=18:18) | nan       |
| 19 | [CL:0002228](http://purl.obolibrary.org/obo/CL_0002228) | primary lens fiber                    | primary lens fiber        | [UBERON:0002444](http://purl.obolibrary.org/obo/UBERON_0002444) | lens fiber                    | lens Fibers                 | [29](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=29:29) | nan       |
| 20 | [CL:0002225](http://purl.obolibrary.org/obo/CL_0002225) | secondary lens fiber                  | mature fiber cell         | [UBERON:0000390](http://purl.obolibrary.org/obo/UBERON_0000390) | lens nucleus                  | Fetal nucleus               | [34](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=34:34) | nan       |
| 22 | [CL:0002585](http://purl.obolibrary.org/obo/CL_0002585) | retinal blood vessel endothelial cell | Endothelial Cell          | [UBERON:0004864](http://purl.obolibrary.org/obo/UBERON_0004864) | vasculature of retina         | vasculature                 | [63](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=63:63) | nan       |
| 23 | [CL:4023188](http://purl.obolibrary.org/obo/CL_4023188) | Midget ganglion cell of retina        | Midget cell               | [UBERON:0001792](http://purl.obolibrary.org/obo/UBERON_0001792) | ganglionic layer of retina    | retinal ganglion cell layer | [64](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=64:64) | nan       |
| 24 | [CL:4023189](http://purl.obolibrary.org/obo/CL_4023189) | Parasol ganglion cell of retina       | Parasol cell              | [UBERON:0001792](http://purl.obolibrary.org/obo/UBERON_0001792) | ganglionic layer of retina    | retinal ganglion cell layer | [65](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=65:65) | nan       |
| 26 | [CL:0000129](http://purl.obolibrary.org/obo/CL_0000129) | microglial cell                       | microglial cell           | [UBERON:0000966](http://purl.obolibrary.org/obo/UBERON_0000966) | retina                        | retina                      | [68](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=68:68) | nan       |
| 28 | [CL:0000636](http://purl.obolibrary.org/obo/CL_0000636) | Mueller cell                          | Muller glia               | [UBERON:0001791](http://purl.obolibrary.org/obo/UBERON_0001791) | inner nuclear layer of retina | inner nuclear layer         | [69](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=69:69) | nan       |
| 29 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                              | Pericyte                  | [UBERON:0004864](http://purl.obolibrary.org/obo/UBERON_0004864) | vasculature of retina         | vasculature                 | [70](https://docs.google.com/spreadsheets/d/1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA/edit#gid=695483621&range=70:70) | nan       |




# New CL terms
[**Report**](new_cl_terms_Eye.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Eye.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Eye_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Eye_AS_has_part_CT_log.tsv)