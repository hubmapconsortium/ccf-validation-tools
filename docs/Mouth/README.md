
ASCT+B Validation Reports for Mouth (2026-09-23)
================================================

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
  
1. CL:9900005

1. CL:9900003

1. CL:9900001

1. CL:9900002

1. CL:9900006

1. CL:9900007

1. CL:9900008


## Typos or punctuation mistakes


This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.  
  
- No issues found.


## Different labels


This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.

If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.

If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.  
  
1. The term _[CL:0000057](http://purl.obolibrary.org/obo/CL_0000057)_ has a different name/label in the source ontology in the following 3 rows _[54](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=54:54)_, _[73](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=73:73)_, _[90](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=90:90)_. The name/label in the **ASCT+B table** is _periductal fibroblast of salivary gland_ and the one in the **ontology** is _fibroblast_. For reference, the given name/label **by SMEs** is _periacinar fibroblast_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. The term _[CL:0000798](http://purl.obolibrary.org/obo/CL_0000798)_ has a different name/label in the source ontology in the following 1 row _[43](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=43:43)_. The name/label in the **ASCT+B table** is _gamma delta T cell_ and the one in the **ontology** is _gamma-delta T cell_. For reference, the given name/label **by SMEs** is _gamma delta T cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols4/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
1. No term id was found for the name/label _excretory duct epithelial cell_ in the following 2 rows _[60](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=60:60)_, _[96](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=96:96)_.

1. No term id was found for the name/label _mucous acinar cell_ in the following 2 rows _[71](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=71:71)_, _[88](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=88:88)_.

1. No term id was found for the name/label _excretory duct_ in the following 1 row _[96](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=96:96)_.

1. No term id was found for the name/label _intercalated duct_ in the following 1 row _[97](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=97:97)_.

1. No term id was found for the name/label _striated duct_ in the following 1 row _[98](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=98:98)_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
1. The term _excretory duct epithelial cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[60](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=60:60)_, _[96](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=96:96)_.

1. The term _mucous acinar cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[71](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=71:71)_, _[88](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=88:88)_.


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



|    | s                                                               | slabel                          | user_slabel                         | o                                                               | olabel                             | user_olabel                   | row_number                                                                                                          |   deltaIC |
|----|-----------------------------------------------------------------|---------------------------------|-------------------------------------|-----------------------------------------------------------------|------------------------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------|
| 49 | [UBERON:0001838](http://purl.obolibrary.org/obo/UBERON_0001838) | sublingual duct                 | intercalated duct                   | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit | sublingual gland ducto-acinar | [78](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=78:78)    |  16.861   |
| 52 | [UBERON:0035048](http://purl.obolibrary.org/obo/UBERON_0035048) | parotid gland excretory duct    | excretory duct                      | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit    | parotid gland ducto-acinar    | [60](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=60:60)    |  12.7917  |
| 54 | [UBERON:0035046](http://purl.obolibrary.org/obo/UBERON_0035046) | parotid gland intercalated duct | intercalated duct                   | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit    | parotid gland ducto-acinar    | [61](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=61:61)    |   4.55648 |
| 55 | [UBERON:0035047](http://purl.obolibrary.org/obo/UBERON_0035047) | parotid gland striated duct     | striated duct                       | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit    | parotid gland ducto-acinar    | [62](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=62:62)    |   4.55648 |
| 72 | [UBERON:0013475](http://purl.obolibrary.org/obo/UBERON_0013475) | gustatory gland                 | gustatory gland (Von Ebner's gland) | [UBERON:0001830](http://purl.obolibrary.org/obo/UBERON_0001830) | minor salivary gland               | minor salivary gland          | [103](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=103:103) | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                                     | user_slabel                                     | o                                                               | olabel                                | user_olabel                      | row_number                                                                                                       |   deltaIC |
|----|---------------------------------------------------------|--------------------------------------------|-------------------------------------------------|-----------------------------------------------------------------|---------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                           | endothelial cell                                | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [16](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=16:16) |  47.6301  |
|  1 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                           | endothelial cell                                | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [82](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=82:82) |  47.6301  |
|  2 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                           | endothelial cell                                | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [65](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=65:65) |  47.6301  |
|  3 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                           | endothelial cell                                | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [47](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=47:47) |  47.6301  |
|  4 | [CL:0000084](http://purl.obolibrary.org/obo/CL_0000084) | T cell                                     | T cell                                          | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [14](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=14:14) |  44.4934  |
|  5 | [CL:0000236](http://purl.obolibrary.org/obo/CL_0000236) | B cell                                     | B cell (non-plasma)                             | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [19](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=19:19) |  44.048   |
|  6 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057) | fibroblast                                 | fibroblast                                      | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [13](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=13:13) |  42.3193  |
|  7 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057) | fibroblast                                 | periacinar fibroblast                           | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [90](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=90:90) |  42.3193  |
|  8 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057) | fibroblast                                 | periacinar fibroblast                           | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [73](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=73:73) |  42.3193  |
|  9 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057) | fibroblast                                 | periacinar fibroblast                           | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [54](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=54:54) |  42.3193  |
| 10 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                         | smooth muscle cell                              | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [77](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=77:77) |  38.375   |
| 11 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                         | smooth muscle cell                              | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [58](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=58:58) |  38.375   |
| 12 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                         | smooth muscle cell                              | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [94](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=94:94) |  38.375   |
| 13 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                                 | macrophage                                      | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [86](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=86:86) |  35.9726  |
| 14 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                                 | macrophage                                      | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [18](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=18:18) |  35.9726  |
| 15 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                                 | macrophage                                      | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [69](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=69:69) |  35.9726  |
| 16 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                                 | macrophage                                      | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [51](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=51:51) |  35.9726  |
| 17 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                             | dendritic cell                                  | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [46](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=46:46) |  35.7478  |
| 18 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                             | dendritic cell                                  | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [81](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=81:81) |  35.7478  |
| 19 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                             | dendritic cell                                  | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [64](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=64:64) |  35.7478  |
| 20 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                             | dendritic cell                                  | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [22](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=22:22) |  35.7478  |
| 21 | [CL:0000148](http://purl.obolibrary.org/obo/CL_0000148) | melanocyte                                 | melanocyte                                      | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [17](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=17:17) |  34.4919  |
| 22 | [CL:0000312](http://purl.obolibrary.org/obo/CL_0000312) | keratinocyte                               | keratinocyte                                    | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [21](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=21:21) |  32.5777  |
| 23 | [CL:0001065](http://purl.obolibrary.org/obo/CL_0001065) | innate lymphoid cell                       | innate lymphoid cell                            | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [28](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=28:28) |  32.0477  |
| 24 | [CL:0000136](http://purl.obolibrary.org/obo/CL_0000136) | adipocyte                                  | adipocyte                                       | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [44](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=44:44) |  31.5798  |
| 25 | [CL:0000623](http://purl.obolibrary.org/obo/CL_0000623) | natural killer cell                        | NK (natural killer) cells                       | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [24](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=24:24) |  31.076   |
| 26 | [CL:0000775](http://purl.obolibrary.org/obo/CL_0000775) | neutrophil                                 | neutrophil                                      | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [25](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=25:25) |  30.338   |
| 27 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                                   | pericyte                                        | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [91](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=91:91) |  29.7245  |
| 28 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                                   | pericyte                                        | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [74](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=74:74) |  29.7245  |
| 29 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                                   | pericyte                                        | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [55](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=55:55) |  29.7245  |
| 30 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                                   | pericyte                                        | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [36](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=36:36) |  29.7245  |
| 31 | [CL:0000798](http://purl.obolibrary.org/obo/CL_0000798) | gamma-delta T cell                         | gamma delta T cell                              | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [43](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=43:43) |  29.1265  |
| 32 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                  | mast cell                                       | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [70](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=70:70) |  28.4686  |
| 33 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                  | mast cell                                       | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [52](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=52:52) |  28.4686  |
| 34 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                  | mast cell                                       | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [15](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=15:15) |  28.4686  |
| 35 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                  | mast cell                                       | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [87](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=87:87) |  28.4686  |
| 36 | [CL:0000814](http://purl.obolibrary.org/obo/CL_0000814) | mature NK T cell                           | NK T cell                                       | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [32](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=32:32) |  26.4611  |
| 37 | [CL:0000786](http://purl.obolibrary.org/obo/CL_0000786) | plasma cell                                | plasma cell                                     | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [26](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=26:26) |  26.222   |
| 38 | [CL:0002573](http://purl.obolibrary.org/obo/CL_0002573) | Schwann cell                               | Schwann cell                                    | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [38](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=38:38) |  26.0992  |
| 39 | [CL:0000815](http://purl.obolibrary.org/obo/CL_0000815) | regulatory T cell                          | regulatory T cell (Treg)                        | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [27](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=27:27) |  25.9739  |
| 40 | [CL:0000912](http://purl.obolibrary.org/obo/CL_0000912) | helper T cell                              | helper T                                        | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [48](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=48:48) |  25.3094  |
| 41 | [CL:0000912](http://purl.obolibrary.org/obo/CL_0000912) | helper T cell                              | helper T                                        | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [66](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=66:66) |  25.3094  |
| 42 | [CL:0000912](http://purl.obolibrary.org/obo/CL_0000912) | helper T cell                              | helper T                                        | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [83](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=83:83) |  25.3094  |
| 43 | [CL:0000359](http://purl.obolibrary.org/obo/CL_0000359) | vascular associated smooth muscle cell     | vascular smooth muscle cell                     | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [37](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=37:37) |  24.7247  |
| 44 | [CL:0000453](http://purl.obolibrary.org/obo/CL_0000453) | Langerhans cell                            | Langerhans cell                                 | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [23](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=23:23) |  23.1809  |
| 45 | [CL:0002138](http://purl.obolibrary.org/obo/CL_0002138) | endothelial cell of lymphatic vessel       | lymphatic endothelial cell                      | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [42](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=42:42) |  23.1809  |
| 46 | [CL:0002144](http://purl.obolibrary.org/obo/CL_0002144) | capillary endothelial cell                 | capillary vascular endothelial cell             | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [34](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=34:34) |  19.6928  |
| 47 | [CL:0000899](http://purl.obolibrary.org/obo/CL_0000899) | T-helper 17 cell                           | Th17 cell                                       | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [40](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=40:40) |  17.3481  |
| 48 | [CL:0000242](http://purl.obolibrary.org/obo/CL_0000242) | Merkel cell                                | Merkel cell                                     | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [20](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=20:20) |  17.3481  |
| 50 | [CL:1000413](http://purl.obolibrary.org/obo/CL_1000413) | endothelial cell of artery                 | arterial vascular endothelial cell              | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [33](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=33:33) |  15.7628  |
| 51 | [CL:0000910](http://purl.obolibrary.org/obo/CL_0000910) | cytotoxic T cell                           | cytotoxic T cell (Tc)                           | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [41](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=41:41) |  15.7628  |
| 53 | [CL:1000414](http://purl.obolibrary.org/obo/CL_1000414) | endothelial cell of venule                 | post-capillary venule vascular endothelial cell | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [35](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=35:35) |   9.11296 |
| 56 | [CL:0002621](http://purl.obolibrary.org/obo/CL_0002621) | gingival epithelial cell                   | gingival epithelial cell                        | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [12](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=12:12) | nan       |
| 57 | [CL:0020062](http://purl.obolibrary.org/obo/CL_0020062) | junctional epithelial cell                 | junctional epithelium cell                      | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [29](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=29:29) | nan       |
| 58 | [CL:0002337](http://purl.obolibrary.org/obo/CL_0002337) | keratinocyte stem cell                     | basal keratinocyte                              | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [30](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=30:30) | nan       |
| 59 | [CL:4033013](http://purl.obolibrary.org/obo/CL_4033013) | suprabasal keratinocyte                    | suprabasal keratinocyte                         | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [31](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=31:31) | nan       |
| 60 | [CL:0020002](http://purl.obolibrary.org/obo/CL_0020002) | mucosal-associated invariant T cell, human | mucosal-associated invariant T cell             | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [39](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=39:39) | nan       |
| 61 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                            | IgA secreting plasma cell                       | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [49](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=49:49) | nan       |
| 62 | [CL:4052065](http://purl.obolibrary.org/obo/CL_4052065) | serous acinar cell of salivary gland       | serous acinar cell                              | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [57](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=57:57) | nan       |
| 63 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland        | intercalated duct epithelial cell               | [UBERON:0035046](http://purl.obolibrary.org/obo/UBERON_0035046) | parotid gland intercalated duct       | intercalated duct                | [61](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=61:61) | nan       |
| 64 | [CL:4052049](http://purl.obolibrary.org/obo/CL_4052049) | striated cell of salivary gland            | striated duct epithelial cell                   | [UBERON:0035047](http://purl.obolibrary.org/obo/UBERON_0035047) | parotid gland striated duct           | striated duct                    | [62](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=62:62) | nan       |
| 65 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                            | IgA secreting plasma cell                       | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [67](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=67:67) | nan       |
| 66 | [CL:4052067](http://purl.obolibrary.org/obo/CL_4052067) | seromucous acinar cell of salivary gland   | seromucosal acinar cell                         | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [76](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=76:76) | nan       |
| 67 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland        | intercalated duct epithelial cell               | [UBERON:0001838](http://purl.obolibrary.org/obo/UBERON_0001838) | sublingual duct                       | intercalated duct                | [78](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=78:78) | nan       |
| 68 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                            | IgA secreting plasma cell                       | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [84](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=84:84) | nan       |
| 69 | [CL:4052067](http://purl.obolibrary.org/obo/CL_4052067) | seromucous acinar cell of salivary gland   | seromucosal acinar cell                         | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [93](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=93:93) | nan       |
| 70 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland        | intercalated duct epithelial cell               | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [97](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=97:97) | nan       |
| 71 | [CL:4052049](http://purl.obolibrary.org/obo/CL_4052049) | striated cell of salivary gland            | striated duct epithelial cell                   | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [98](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=98:98) | nan       |




# New CL terms
[**Report**](new_cl_terms_Mouth.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Mouth.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Mouth_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Mouth_AS_has_part_CT_log.tsv)