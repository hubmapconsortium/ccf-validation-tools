
ASCT+B Validation Reports for Mouth (2026-08-12)
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
  
1. CL:9900008

1. CL:9900005

1. CL:9900004

1. CL:9900002

1. CL:9900003

1. CL:9900006

1. CL:9900007

1. CL:9900001


## Typos or punctuation mistakes


This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.  
  
- No issues found.


## Different labels


This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.

If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.

If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.  
  
1. The term _[CL:0000057](http://purl.obolibrary.org/obo/CL_0000057)_ has a different name/label in the source ontology in the following 3 rows _[43](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=43:43)_, _[62](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=62:62)_, _[79](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=79:79)_. The name/label in the **ASCT+B table** is _periductal fibroblast of salivary gland_ and the one in the **ontology** is _fibroblast_. For reference, the given name/label **by SMEs** is _periacinar fibroblast_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. The term _[UBERON:0004923](http://purl.obolibrary.org/obo/UBERON_0004923)_ has a different name/label in the source ontology in the following 1 row _[31](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=31:31)_. The name/label in the **ASCT+B table** is _mucosa of the lip_ and the one in the **ontology** is _organ component layer_. For reference, the given name/label **by SMEs** is _mucosa of the lip_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols4/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
1. No term id was found for the name/label _excretory duct epithelial cell_ in the following 2 rows _[49](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=49:49)_, _[85](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=85:85)_.

1. No term id was found for the name/label _mucous acinar cell_ in the following 2 rows _[60](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=60:60)_, _[77](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=77:77)_.

1. No term id was found for the name/label _excretory duct_ in the following 1 row _[85](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=85:85)_.

1. No term id was found for the name/label _intercalated duct_ in the following 1 row _[86](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=86:86)_.

1. No term id was found for the name/label _striated duct_ in the following 1 row _[87](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=87:87)_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
1. The term _excretory duct epithelial cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[49](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=49:49)_, _[85](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=85:85)_.

1. The term _mucous acinar cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[60](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=60:60)_, _[77](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=77:77)_.


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



|    | s                                                               | slabel                          | user_slabel                         | o                                                               | olabel                             | user_olabel                   | row_number                                                                                                       |   deltaIC |
|----|-----------------------------------------------------------------|---------------------------------|-------------------------------------|-----------------------------------------------------------------|------------------------------------|-------------------------------|------------------------------------------------------------------------------------------------------------------|-----------|
| 40 | [UBERON:0004923](http://purl.obolibrary.org/obo/UBERON_0004923) | organ component layer           | mucosa of the lip                   | [UBERON:0003729](http://purl.obolibrary.org/obo/UBERON_0003729) | mouth mucosa                       | mouth mucosa                  | [31](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=31:31) |  23.2065  |
| 42 | [UBERON:0001838](http://purl.obolibrary.org/obo/UBERON_0001838) | sublingual duct                 | intercalated duct                   | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit | sublingual gland ducto-acinar | [67](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=67:67) |  16.8893  |
| 43 | [UBERON:0035048](http://purl.obolibrary.org/obo/UBERON_0035048) | parotid gland excretory duct    | excretory duct                      | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit    | parotid gland ducto-acinar    | [49](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=49:49) |  12.8132  |
| 44 | [UBERON:0035046](http://purl.obolibrary.org/obo/UBERON_0035046) | parotid gland intercalated duct | intercalated duct                   | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit    | parotid gland ducto-acinar    | [50](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=50:50) |   4.56414 |
| 45 | [UBERON:0035047](http://purl.obolibrary.org/obo/UBERON_0035047) | parotid gland striated duct     | striated duct                       | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit    | parotid gland ducto-acinar    | [51](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=51:51) |   4.56414 |
| 58 | [UBERON:0013475](http://purl.obolibrary.org/obo/UBERON_0013475) | gustatory gland                 | gustatory gland (Von Ebner's gland) | [UBERON:0001830](http://purl.obolibrary.org/obo/UBERON_0001830) | minor salivary gland               | minor salivary gland          | [92](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=92:92) | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                                   | user_slabel                       | o                                                               | olabel                                | user_olabel                      | row_number                                                                                                       |   deltaIC |
|----|---------------------------------------------------------|------------------------------------------|-----------------------------------|-----------------------------------------------------------------|---------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                         | endothelial cell                  | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [36](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=36:36) |   47.7055 |
|  1 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                         | endothelial cell                  | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [16](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=16:16) |   47.7055 |
|  2 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                         | endothelial cell                  | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [71](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=71:71) |   47.7055 |
|  3 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                         | endothelial cell                  | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [54](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=54:54) |   47.7055 |
|  4 | [CL:0000084](http://purl.obolibrary.org/obo/CL_0000084) | T cell                                   | T cell                            | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [14](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=14:14) |   44.4306 |
|  5 | [CL:0000236](http://purl.obolibrary.org/obo/CL_0000236) | B cell                                   | B cell (non-plasma)               | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [19](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=19:19) |   44.3294 |
|  6 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057) | fibroblast                               | fibroblast                        | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [13](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=13:13) |   42.3905 |
|  7 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057) | fibroblast                               | periacinar fibroblast             | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [79](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=79:79) |   42.3905 |
|  8 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057) | fibroblast                               | periacinar fibroblast             | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [62](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=62:62) |   42.3905 |
|  9 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057) | fibroblast                               | periacinar fibroblast             | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [43](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=43:43) |   42.3905 |
| 10 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                       | smooth muscle cell                | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [83](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=83:83) |   38.4395 |
| 11 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                       | smooth muscle cell                | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [66](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=66:66) |   38.4395 |
| 12 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                       | smooth muscle cell                | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [47](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=47:47) |   38.4395 |
| 13 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                           | dendritic cell                    | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [35](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=35:35) |   35.808  |
| 14 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                           | dendritic cell                    | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [53](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=53:53) |   35.808  |
| 15 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                           | dendritic cell                    | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [22](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=22:22) |   35.808  |
| 16 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                           | dendritic cell                    | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [70](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=70:70) |   35.808  |
| 17 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                               | macrophage                        | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [75](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=75:75) |   35.6044 |
| 18 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                               | macrophage                        | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [18](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=18:18) |   35.6044 |
| 19 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                               | macrophage                        | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [40](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=40:40) |   35.6044 |
| 20 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                               | macrophage                        | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [58](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=58:58) |   35.6044 |
| 21 | [CL:0000148](http://purl.obolibrary.org/obo/CL_0000148) | melanocyte                               | melanocyte                        | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [17](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=17:17) |   34.5499 |
| 22 | [CL:0000312](http://purl.obolibrary.org/obo/CL_0000312) | keratinocyte                             | keratinocyte                      | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [21](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=21:21) |   32.6325 |
| 23 | [CL:0001065](http://purl.obolibrary.org/obo/CL_0001065) | innate lymphoid cell                     | innate lymphoid cell              | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [28](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=28:28) |   32.1016 |
| 24 | [CL:0000136](http://purl.obolibrary.org/obo/CL_0000136) | adipocyte                                | adipocyte                         | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [33](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=33:33) |   31.6329 |
| 25 | [CL:0000623](http://purl.obolibrary.org/obo/CL_0000623) | natural killer cell                      | NK (natural killer) cells         | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [24](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=24:24) |   31.1283 |
| 26 | [CL:0000775](http://purl.obolibrary.org/obo/CL_0000775) | neutrophil                               | neutrophil                        | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [25](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=25:25) |   30.389  |
| 27 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                                 | pericyte                          | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [80](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=80:80) |   29.7745 |
| 28 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                                 | pericyte                          | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [63](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=63:63) |   29.7745 |
| 29 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                                 | pericyte                          | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [44](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=44:44) |   29.7745 |
| 30 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                | mast cell                         | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [15](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=15:15) |   28.5164 |
| 31 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                | mast cell                         | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [76](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=76:76) |   28.5164 |
| 32 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                | mast cell                         | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [41](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=41:41) |   28.5164 |
| 33 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                | mast cell                         | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [59](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=59:59) |   28.5164 |
| 34 | [CL:0000786](http://purl.obolibrary.org/obo/CL_0000786) | plasma cell                              | plasma cell                       | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [26](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=26:26) |   26.2661 |
| 35 | [CL:0000815](http://purl.obolibrary.org/obo/CL_0000815) | regulatory T cell                        | regulatory T cell (Treg)          | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [27](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=27:27) |   26.0176 |
| 36 | [CL:0000912](http://purl.obolibrary.org/obo/CL_0000912) | helper T cell                            | helper T                          | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [55](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=55:55) |   25.3519 |
| 37 | [CL:0000912](http://purl.obolibrary.org/obo/CL_0000912) | helper T cell                            | helper T                          | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [37](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=37:37) |   25.3519 |
| 38 | [CL:0000912](http://purl.obolibrary.org/obo/CL_0000912) | helper T cell                            | helper T                          | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [72](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=72:72) |   25.3519 |
| 39 | [CL:0000453](http://purl.obolibrary.org/obo/CL_0000453) | Langerhans cell                          | Langerhans cell                   | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [23](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=23:23) |   23.2199 |
| 41 | [CL:0000242](http://purl.obolibrary.org/obo/CL_0000242) | Merkel cell                              | Merkel cell                       | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [20](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=20:20) |   17.3773 |
| 46 | [CL:0002621](http://purl.obolibrary.org/obo/CL_0002621) | gingival epithelial cell                 | gingival epithelial cell          | [UBERON:8000014](http://purl.obolibrary.org/obo/UBERON_8000014) | dentogingival junction                | gingival attachment              | [12](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=12:12) |  nan      |
| 47 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                          | IgA secreting plasma cell         | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [38](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=38:38) |  nan      |
| 48 | [CL:4052065](http://purl.obolibrary.org/obo/CL_4052065) | serous acinar cell of salivary gland     | serous acinar cell                | [UBERON:8000011](http://purl.obolibrary.org/obo/UBERON_8000011) | parotid gland ducto-acinar unit       | parotid gland ducto-acinar       | [46](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=46:46) |  nan      |
| 49 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland      | intercalated duct epithelial cell | [UBERON:0035046](http://purl.obolibrary.org/obo/UBERON_0035046) | parotid gland intercalated duct       | intercalated duct                | [50](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=50:50) |  nan      |
| 50 | [CL:4052049](http://purl.obolibrary.org/obo/CL_4052049) | striated cell of salivary gland          | striated duct epithelial cell     | [UBERON:0035047](http://purl.obolibrary.org/obo/UBERON_0035047) | parotid gland striated duct           | striated duct                    | [51](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=51:51) |  nan      |
| 51 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                          | IgA secreting plasma cell         | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [56](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=56:56) |  nan      |
| 52 | [CL:4052067](http://purl.obolibrary.org/obo/CL_4052067) | seromucous acinar cell of salivary gland | seromucosal acinar cell           | [UBERON:8000012](http://purl.obolibrary.org/obo/UBERON_8000012) | sublingual gland ducto-acinar unit    | sublingual gland ducto-acinar    | [65](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=65:65) |  nan      |
| 53 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland      | intercalated duct epithelial cell | [UBERON:0001838](http://purl.obolibrary.org/obo/UBERON_0001838) | sublingual duct                       | intercalated duct                | [67](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=67:67) |  nan      |
| 54 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                          | IgA secreting plasma cell         | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [73](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=73:73) |  nan      |
| 55 | [CL:4052067](http://purl.obolibrary.org/obo/CL_4052067) | seromucous acinar cell of salivary gland | seromucosal acinar cell           | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [82](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=82:82) |  nan      |
| 56 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland      | intercalated duct epithelial cell | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [86](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=86:86) |  nan      |
| 57 | [CL:4052049](http://purl.obolibrary.org/obo/CL_4052049) | striated cell of salivary gland          | striated duct epithelial cell     | [UBERON:8000013](http://purl.obolibrary.org/obo/UBERON_8000013) | submandibular gland ducto-acinar unit | submandibular gland ducto-acinar | [87](https://docs.google.com/spreadsheets/d/1ZkqakhVKIZ-xkM1N-oOu9QNPt5GBDnguLoX9QQSZXEo/edit#gid=0&range=87:87) |  nan      |




# New CL terms
[**Report**](new_cl_terms_Mouth.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Mouth.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Mouth_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Mouth_AS_has_part_CT_log.tsv)