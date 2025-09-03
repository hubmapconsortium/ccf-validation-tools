
ASCT+B Validation Reports for Skin (2025-09-03)
===============================================

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
  
1. The term _[CL:0000317](http://purl.obolibrary.org/obo/CL_0000317)_ has a different name/label in the source ontology in the following 1 row _[35](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=35:35)_. The name/label in the **ASCT+B table** is _sebum secreting cell_ and the one in the **ontology** is _sebocyte_. For reference, the given name/label **by SMEs** is _Germinative (epithelial) cell, Sebocyte_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. The term _[CL:0000649](http://purl.obolibrary.org/obo/CL_0000649)_ has a different name/label in the source ontology in the following 1 row _[15](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=15:15)_. The name/label in the **ASCT+B table** is _prickle cell_ and the one in the **ontology** is _spinous cell of epidermis_. For reference, the given name/label **by SMEs** is _Keratinocytes (Spinous)_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols4/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
1. No term id was found for the name/label _connective tissue sheath_ in the following 1 row _[32](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=32:32)_.


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



|    | s                                                               | slabel                    | user_slabel      | o                                                               | olabel        | user_olabel    | row_number                                                                                                               |   deltaIC |
|----|-----------------------------------------------------------------|---------------------------|------------------|-----------------------------------------------------------------|---------------|----------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
|  7 | [UBERON:0008974](http://purl.obolibrary.org/obo/UBERON_0008974) | apocrine gland            | Apocrine glands  | [UBERON:0001820](http://purl.obolibrary.org/obo/UBERON_0001820) | sweat gland   | sweat gland    | [37](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=37:37) |   1.71819 |
|  8 | [UBERON:0035549](http://purl.obolibrary.org/obo/UBERON_0035549) | vasculature of integument | Blood vessels    | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis    | Subcutaneous   | [82](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=82:82) |   1.21759 |
| 16 | [UBERON:0000412](http://purl.obolibrary.org/obo/UBERON_0000412) | dermal papilla            | Hair papilla     | [UBERON:0002073](http://purl.obolibrary.org/obo/UBERON_0002073) | hair follicle | Hair follicles | [25](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=25:25) | nan       |
| 17 | [UBERON:0005184](http://purl.obolibrary.org/obo/UBERON_0005184) | hair medulla              | medulla          | [UBERON:0002074](http://purl.obolibrary.org/obo/UBERON_0002074) | hair shaft    | Hair shaft     | [30](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=30:30) | nan       |
| 18 | [UBERON:0001821](http://purl.obolibrary.org/obo/UBERON_0001821) | sebaceous gland           | Sebaceous glands | [UBERON:0002073](http://purl.obolibrary.org/obo/UBERON_0002073) | hair follicle | Hair follicles | [35](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=35:35) | nan       |
| 38 | [UBERON:0035549](http://purl.obolibrary.org/obo/UBERON_0035549) | vasculature of integument | Blood vessels    | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis        | Dermis         | [62](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=62:62) | nan       |
| 43 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [68](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=68:68) | nan       |
| 45 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [69](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=69:69) | nan       |
| 46 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [70](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=70:70) | nan       |
| 48 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [71](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=71:71) | nan       |
| 49 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [72](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=72:72) | nan       |
| 50 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [73](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=73:73) | nan       |
| 52 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [74](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=74:74) | nan       |
| 54 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [75](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=75:75) | nan       |
| 56 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [76](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=76:76) | nan       |
| 57 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [77](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=77:77) | nan       |
| 58 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [78](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=78:78) | nan       |
| 60 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [79](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=79:79) | nan       |
| 61 | [UBERON:0007121](http://purl.obolibrary.org/obo/UBERON_0007121) | skin nerve field          | nerve            | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis    | Subcutaneous   | [79](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=79:79) | nan       |
| 62 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [80](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=80:80) | nan       |
| 64 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [81](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=81:81) | nan       |
| 66 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [82](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=82:82) | nan       |
| 67 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [83](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=83:83) | nan       |
| 69 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                | Subcutaneous     | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) | skin of body  | skin           | [84](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=84:84) | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                                 | user_slabel                                  | o                                                               | olabel                          | user_olabel             | row_number                                                                                                               |    deltaIC |
|----|---------------------------------------------------------|----------------------------------------|----------------------------------------------|-----------------------------------------------------------------|---------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------|------------|
|  0 | [CL:0000540](http://purl.obolibrary.org/obo/CL_0000540) | Neuron                                 | Neuron                                       | [UBERON:0007121](http://purl.obolibrary.org/obo/UBERON_0007121) | skin nerve field                | nerve                   | [59](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=59:59) |  68.5753   |
|  1 | [CL:0000540](http://purl.obolibrary.org/obo/CL_0000540) | Neuron                                 | Neuron                                       | [UBERON:0007121](http://purl.obolibrary.org/obo/UBERON_0007121) | skin nerve field                | nerve                   | [79](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=79:79) |  68.5753   |
|  2 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                       | Endothelial cell                             | [UBERON:0035549](http://purl.obolibrary.org/obo/UBERON_0035549) | vasculature of integument       | Blood vessels           | [62](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=62:62) |  18.0257   |
|  3 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                       | Endothelial cell                             | [UBERON:0035549](http://purl.obolibrary.org/obo/UBERON_0035549) | vasculature of integument       | Blood vessels           | [82](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=82:82) |  18.0257   |
|  4 | [CL:0000236](http://purl.obolibrary.org/obo/CL_0000236) | B cell                                 | B cell                                       | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [76](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=76:76) |  16.0417   |
|  5 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                             | Macrophage                                   | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [71](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=71:71) |   7.2474   |
|  6 | [CL:0000775](http://purl.obolibrary.org/obo/CL_0000775) | neutrophil                             | Neutrophil                                   | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [77](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=77:77) |   2.05199  |
|  9 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                              | Mast cell                                    | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [72](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=72:72) |   0.175927 |
| 10 | [CL:0002457](http://purl.obolibrary.org/obo/CL_0002457) | epidermal Langerhans cell              | Langerhans cell                              | [UBERON:0002069](http://purl.obolibrary.org/obo/UBERON_0002069) | stratum granulosum of epidermis | Stratum granulosum (SG) | [14](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=14:14) | nan        |
| 11 | [CL:0002457](http://purl.obolibrary.org/obo/CL_0002457) | epidermal Langerhans cell              | Langerhans cell                              | [UBERON:0002026](http://purl.obolibrary.org/obo/UBERON_0002026) | stratum spinosum of epidermis   | Stratum spinosum (SS)   | [16](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=16:16) | nan        |
| 12 | [CL:0000242](http://purl.obolibrary.org/obo/CL_0000242) | Merkel cell                            | Merkel cell                                  | [UBERON:0002026](http://purl.obolibrary.org/obo/UBERON_0002026) | stratum spinosum of epidermis   | Stratum spinosum (SS)   | [17](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=17:17) | nan        |
| 13 | [CL:0002457](http://purl.obolibrary.org/obo/CL_0002457) | epidermal Langerhans cell              | Langerhans cell                              | [UBERON:0002025](http://purl.obolibrary.org/obo/UBERON_0002025) | stratum basale of epidermis     | Stratum basale (SB)     | [19](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=19:19) | nan        |
| 14 | [CL:1000458](http://purl.obolibrary.org/obo/CL_1000458) | melanocyte of skin                     | Melanocyte                                   | [UBERON:0002025](http://purl.obolibrary.org/obo/UBERON_0002025) | stratum basale of epidermis     | Stratum basale (SB)     | [21](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=21:21) | nan        |
| 15 | [CL:0002483](http://purl.obolibrary.org/obo/CL_0002483) | hair follicle melanocyte               | Melanocyte                                   | [UBERON:0005932](http://purl.obolibrary.org/obo/UBERON_0005932) | bulb of hair follicle           | Hair bulb               | [24](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=24:24) | nan        |
| 19 | [CL:1000417](http://purl.obolibrary.org/obo/CL_1000417) | myoepithelial cell of sweat gland      | myoepithelial cell                           | [UBERON:0000423](http://purl.obolibrary.org/obo/UBERON_0000423) | eccrine sweat gland             | Eccrine (sweat) glands  | [36](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=36:36) | nan        |
| 20 | [CL:1000417](http://purl.obolibrary.org/obo/CL_1000417) | myoepithelial cell of sweat gland      | myoepithelial cell                           | [UBERON:0008974](http://purl.obolibrary.org/obo/UBERON_0008974) | apocrine gland                  | Apocrine glands         | [37](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=37:37) | nan        |
| 21 | [CL:0002337](http://purl.obolibrary.org/obo/CL_0002337) | keratinocyte stem cell                 | keratinocyte stem cell                       | [UBERON:0002073](http://purl.obolibrary.org/obo/UBERON_0002073) | hair follicle                   | Hair follicles          | [38](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=38:38) | nan        |
| 22 | [CL:1000417](http://purl.obolibrary.org/obo/CL_1000417) | myoepithelial cell of sweat gland      | myoepithelial cell                           | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [40](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=40:40) | nan        |
| 23 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                              | Mast cell                                    | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [42](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=42:42) | nan        |
| 24 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                             | Macrophage                                   | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [47](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=47:47) | nan        |
| 25 | [CL:0000545](http://purl.obolibrary.org/obo/CL_0000545) | T-helper 1 cell                        | T helper                                     | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [48](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=48:48) | nan        |
| 26 | [CL:0000910](http://purl.obolibrary.org/obo/CL_0000910) | cytotoxic T cell                       | T killer                                     | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [49](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=49:49) | nan        |
| 27 | [CL:0000815](http://purl.obolibrary.org/obo/CL_0000815) | regulatory T cell                      | T reg                                        | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [50](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=50:50) | nan        |
| 28 | [CL:0000623](http://purl.obolibrary.org/obo/CL_0000623) | natural killer cell                    | Natural killer cell                          | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [51](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=51:51) | nan        |
| 29 | [CL:0001067](http://purl.obolibrary.org/obo/CL_0001067) | group 1 innate lymphoid cell           | Natural killer cell / Innate lymphoid cell 1 | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [52](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=52:52) | nan        |
| 30 | [CL:0001069](http://purl.obolibrary.org/obo/CL_0001069) | group 2 innate lymphoid cell           | Innate lymphoid cell 2                       | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [53](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=53:53) | nan        |
| 31 | [CL:0001071](http://purl.obolibrary.org/obo/CL_0001071) | group 3 innate lymphoid cell           | Innate lymphoid cell 3                       | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [54](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=54:54) | nan        |
| 32 | [CL:0000236](http://purl.obolibrary.org/obo/CL_0000236) | B cell                                 | B cell                                       | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [55](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=55:55) | nan        |
| 33 | [CL:0000786](http://purl.obolibrary.org/obo/CL_0000786) | plasma cell                            | Plasma cell                                  | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [56](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=56:56) | nan        |
| 34 | [CL:0000775](http://purl.obolibrary.org/obo/CL_0000775) | neutrophil                             | Neutrophil                                   | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [57](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=57:57) | nan        |
| 35 | [CL:0000771](http://purl.obolibrary.org/obo/CL_0000771) | eosinophil                             | Eosinophil                                   | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [58](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=58:58) | nan        |
| 36 | [CL:0002573](http://purl.obolibrary.org/obo/CL_0002573) | Schwann cell                           | Schwann cell                                 | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [60](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=60:60) | nan        |
| 37 | [CL:0002576](http://purl.obolibrary.org/obo/CL_0002576) | perineurial cell                       | perineurial cells                            | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [61](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=61:61) | nan        |
| 39 | [CL:0000359](http://purl.obolibrary.org/obo/CL_0000359) | vascular associated smooth muscle cell | Perivascular smooth muscle cell              | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [63](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=63:63) | nan        |
| 40 | [CL:0002292](http://purl.obolibrary.org/obo/CL_0002292) | type I cell of carotid body            | Glomus cell                                  | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [64](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=64:64) | nan        |
| 41 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                               | pericyte                                     | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [65](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=65:65) | nan        |
| 42 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                               | Pericyte                                     | [UBERON:0002067](http://purl.obolibrary.org/obo/UBERON_0002067) | dermis                          | Dermis                  | [66](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=66:66) | nan        |
| 44 | [CL:0002138](http://purl.obolibrary.org/obo/CL_0002138) | endothelial cell of lymphatic vessel   | Lymphatic                                    | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [68](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=68:68) | nan        |
| 47 | [CL:0002620](http://purl.obolibrary.org/obo/CL_0002620) | skin fibroblast                        | Fibroblast                                   | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [70](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=70:70) | nan        |
| 51 | [CL:0000545](http://purl.obolibrary.org/obo/CL_0000545) | T-helper 1 cell                        | T helper                                     | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [73](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=73:73) | nan        |
| 53 | [CL:0000910](http://purl.obolibrary.org/obo/CL_0000910) | cytotoxic T cell                       | T killer                                     | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [74](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=74:74) | nan        |
| 55 | [CL:0000815](http://purl.obolibrary.org/obo/CL_0000815) | regulatory T cell                      | T reg                                        | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [75](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=75:75) | nan        |
| 59 | [CL:0000771](http://purl.obolibrary.org/obo/CL_0000771) | eosinophil                             | Eosinophil                                   | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [78](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=78:78) | nan        |
| 63 | [CL:0002573](http://purl.obolibrary.org/obo/CL_0002573) | Schwann cell                           | Schwann cell                                 | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [80](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=80:80) | nan        |
| 65 | [CL:0002576](http://purl.obolibrary.org/obo/CL_0002576) | perineurial cell                       | Perineural cell                              | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [81](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=81:81) | nan        |
| 68 | [CL:0000359](http://purl.obolibrary.org/obo/CL_0000359) | vascular associated smooth muscle cell | Perivascular smooth muscle cell              | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [83](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=83:83) | nan        |
| 70 | [CL:0002292](http://purl.obolibrary.org/obo/CL_0002292) | type I cell of carotid body            | Glomus cell                                  | [UBERON:0002072](http://purl.obolibrary.org/obo/UBERON_0002072) | hypodermis                      | Subcutaneous            | [84](https://docs.google.com/spreadsheets/d/1_xLnPyGyQy9fae7DrWkeyEN-iLTP8JQMxTL7HHkxG6o/edit#gid=269383687&range=84:84) | nan        |




# New CL terms
[**Report**](new_cl_terms_Skin.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Skin.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Skin_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Skin_AS_has_part_CT_log.tsv)