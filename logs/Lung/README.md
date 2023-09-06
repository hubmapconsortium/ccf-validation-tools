
ASCT+B Validation Reports for Lung (2023-09-06)
===============================================

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
  
1. In row _[116](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=116:116)_, the term _[UBERON:0003920](http://purl.obolibrary.org/obo/UBERON_0003920)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _venous blood vessel _ and the one in the **ontology** is _venous blood vessel_. For reference, the given name/label **by SMEs** is _venous blood vessel _. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[85](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=85:85)_, the term _[CL:4028006](http://purl.obolibrary.org/obo/CL_4028006)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _adventitial fibroblast_ and the one in the **ontology** is _alveolar type 2 fibroblast cell_. For reference, the given name/label **by SMEs** is _adventitial fibroblast_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[13](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=13:13)_, the term _[UBERON:8600010](http://purl.obolibrary.org/obo/UBERON_8600010)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _ciliated ducts of bronchial submucosal gland_ and the one in the **ontology** is _bronchial submucosal gland ciliated duct_. For reference, the given name/label **by SMEs** is _ciliated ducts of bronchial submucosal gland_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[13](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=13:13)_, no term id was found for the name/label _airway submucosal gland ciliated duct cell_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=22:22)_, no term id was found for the name/label _airway deuterosomal cell_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=24:24)_, no term id was found for the name/label _respiratory suprabasal cell_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=31:31)_, no term id was found for the name/label _airway submucosal gland ciliated duct cells_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=39:39)_, no term id was found for the name/label _respiratory suprabasal cell_.

1. In row _[44](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=44:44)_, no term id was found for the name/label _airway deuterosomal cell_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=51:51)_, no term id was found for the name/label _airway submucosal gland ciliated duct cells_.

1. In row _[57](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=57:57)_, no term id was found for the name/label _airway deuterosomal cell_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=60:60)_, no term id was found for the name/label _respiratory suprabasal cell_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=64:64)_, no term id was found for the name/label _airway deuterosomal cell_.

1. In row _[118](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=118:118)_, no term id was found for the name/label _alveolar macrophage CCL3+_.

1. In row _[120](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=120:120)_, no term id was found for the name/label _alveolar macrophage proliferating_.

1. In row _[121](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=121:121)_, no term id was found for the name/label _alveolar macrophage MT-positive_.

1. In row _[122](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=122:122)_, no term id was found for the name/label _Interstitial macrophage_.

1. In row _[135](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=135:135)_, no term id was found for the name/label _CD4+ T cell resident memory_.

1. In row _[139](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=139:139)_, no term id was found for the name/label _CD8+ T cell resident memory_.

1. In row _[143](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=143:143)_, no term id was found for the name/label _migratory dendritic cell_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[49](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=49:49)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[50](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=50:50)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[51](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=51:51)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[52](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=52:52)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[53](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=53:53)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[54](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=54:54)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[55](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=55:55)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[56](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=56:56)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[57](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=57:57)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[58](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=58:58)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[59](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=59:59)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[60](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=60:60)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[61](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=61:61)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[62](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=62:62)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[63](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=63:63)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[64](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=64:64)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[65](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=65:65)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[66](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=66:66)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[67](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=67:67)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[68](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=68:68)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[69](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=69:69)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[70](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=70:70)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[71](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=71:71)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[101](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=101:101)_, the term _FMA:84472_ is from another ontology that is not validated in this process.

1. In row _[102](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=102:102)_, the term _FMA:84472_ is from another ontology that is not validated in this process.

1. In row _[103](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=103:103)_, the term _FMA:84472_ is from another ontology that is not validated in this process.


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



|     | s              | slabel                                    | user_slabel                                | o              | olabel                        | user_olabel                                | row_number                                                                                                                   |       deltaIC |
|-----|----------------|-------------------------------------------|--------------------------------------------|----------------|-------------------------------|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------|
|   0 | UBERON:0016405 | pulmonary capillary                       | pulmonary capillary                        | UBERON:0008870 | pulmonary alveolar parenchyma | pulmonary alveolar parenchyma              | [95](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=95:95)    |   3.55322e+13 |
|   1 | UBERON:0016405 | pulmonary capillary                       | pulmonary capillary                        | UBERON:0008870 | pulmonary alveolar parenchyma | pulmonary alveolar parenchyma              | [94](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=94:94)    |   3.55322e+13 |
|   4 | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [91](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=91:91)    |   2.78988e+08 |
|   5 | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [92](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=92:92)    |   2.78988e+08 |
|   6 | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [93](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=93:93)    |   2.78988e+08 |
|   7 | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [87](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=87:87)    |   2.78988e+08 |
|   8 | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [88](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=88:88)    |   2.78988e+08 |
|   9 | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [89](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=89:89)    |   2.78988e+08 |
|  10 | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [90](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=90:90)    |   2.78988e+08 |
|  14 | UBERON:8600000 | lobular bronchiole                        | lobular bronchiole                         | UBERON:0012067 | primary bronchiole            | proximal bronchiole                        | [71](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=71:71)    | 100           |
|  15 | UBERON:8600000 | lobular bronchiole                        | lobular bronchiole                         | UBERON:0012067 | primary bronchiole            | proximal bronchiole                        | [70](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=70:70)    | 100           |
|  16 | UBERON:8600000 | lobular bronchiole                        | lobular bronchiole                         | UBERON:0012067 | primary bronchiole            | proximal bronchiole                        | [69](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=69:69)    | 100           |
|  17 | UBERON:8600000 | lobular bronchiole                        | lobular bronchiole                         | UBERON:0012067 | primary bronchiole            | proximal bronchiole                        | [68](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=68:68)    | 100           |
|  18 | UBERON:0004884 | lobar bronchus mesenchyme                 | bronchial mesenchyme                       | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [67](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=67:67)    | 100           |
|  21 | UBERON:0004848 | respiratory system arterial endothelium   | respiratory system arterial endothelium    | UBERON:0002012 | pulmonary artery              | pulmonary artery                           | [109](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=109:109) |  16.0188      |
|  22 | UBERON:0012416 | respiratory system arterial smooth muscle | arterial system smooth muscle              | UBERON:0002012 | pulmonary artery              | pulmonary artery                           | [110](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=110:110) |  16.0188      |
|  24 | UBERON:0002009 | pulmonary nerve plexus                    | pulmonary nerve plexus                     | UBERON:0007196 | tracheobronchial tree         | tracheobronchial tree                      | [12](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=12:12)    | nan           |
|  25 | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | UBERON:8410043 | bronchus submucosal gland     | bronchial submucosal gland                 | [14](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=14:14)    | nan           |
|  27 | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | UBERON:8410043 | bronchus submucosal gland     | bronchial submucosal gland                 | [15](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=15:15)    | nan           |
|  29 | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | UBERON:8410043 | bronchus submucosal gland     | bronchial submucosal gland                 | [16](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=16:16)    | nan           |
|  31 | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | UBERON:8410043 | bronchus submucosal gland     | bronchial submucosal gland                 | [17](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=17:17)    | nan           |
|  33 | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | UBERON:8410043 | bronchus submucosal gland     | bronchial submucosal gland                 | [18](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=18:18)    | nan           |
|  36 | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | UBERON:8410043 | bronchial submucosal gland    | bronchial submucosal gland                 | [32](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=32:32)    | nan           |
|  38 | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | UBERON:8410043 | bronchial submucosal gland    | bronchial submucosal gland                 | [33](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=33:33)    | nan           |
|  40 | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | UBERON:8410043 | bronchial submucosal gland    | bronchial submucosal gland                 | [34](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=34:34)    | nan           |
|  42 | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | UBERON:8410043 | bronchial submucosal gland    | bronchial submucosal gland                 | [35](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=35:35)    | nan           |
|  44 | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | UBERON:8410043 | bronchial submucosal gland    | bronchial submucosal gland                 | [36](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=36:36)    | nan           |
|  46 | UBERON:0004884 | lobar bronchus mesenchyme                 | bronchial mesenchyme                       | UBERON:0002184 | segmental bronchus            | tertiary bronchus                          | [48](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=48:48)    | nan           |
|  47 | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | UBERON:8410043 | bronchial submucosal gland    | bronchial submucosal gland                 | [52](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=52:52)    | nan           |
|  49 | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | UBERON:8410043 | bronchial submucosal gland    | bronchial submucosal gland                 | [53](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=53:53)    | nan           |
|  51 | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | UBERON:8410043 | bronchial submucosal gland    | bronchial submucosal gland                 | [54](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=54:54)    | nan           |
|  53 | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | UBERON:8410043 | bronchial submucosal gland    | bronchial submucosal gland                 | [55](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=55:55)    | nan           |
|  55 | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | UBERON:8410043 | bronchial submucosal gland    | bronchial submucosal gland                 | [56](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=56:56)    | nan           |
|  57 | UBERON:0002341 | epithelium of segmental bronchus          | subsegmental bronchial epithelium          | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [57](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=57:57)    | nan           |
|  58 | UBERON:0002341 | epithelium of segmental bronchus          | subsegmental bronchial epithelium          | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [58](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=58:58)    | nan           |
|  59 | UBERON:0002341 | epithelium of segmental bronchus          | subsegmental bronchial epithelium          | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [59](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=59:59)    | nan           |
|  60 | UBERON:0002341 | epithelium of segmental bronchus          | subsegmental bronchial epithelium          | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [60](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=60:60)    | nan           |
|  61 | UBERON:0002341 | epithelium of segmental bronchus          | subsegmental bronchial epithelium          | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [61](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=61:61)    | nan           |
|  62 | UBERON:0002341 | epithelium of segmental bronchus          | subsegmental bronchial epithelium          | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [62](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=62:62)    | nan           |
|  63 | UBERON:0002341 | epithelium of segmental bronchus          | subsegmental bronchial epithelium          | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [63](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=63:63)    | nan           |
|  64 | UBERON:0002341 | epithelium of segmental bronchus          | subsegmental bronchial epithelium          | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [64](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=64:64)    | nan           |
|  65 | UBERON:0002341 | epithelium of segmental bronchus          | subsegmental bronchial epithelium          | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [65](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=65:65)    | nan           |
|  66 | UBERON:0002341 | epithelium of segmental bronchus          | subsegmental bronchial epithelium          | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [66](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=66:66)    | nan           |
|  67 | UBERON:0012067 | primary bronchiole                        | proximal bronchiole                        | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [68](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=68:68)    | nan           |
|  68 | UBERON:0002051 | epithelium of bronchiole                  | epithelium of bronchiole                   | UBERON:8600000 | lobular bronchiole            | lobular bronchiole                         | [68](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=68:68)    | nan           |
|  69 | UBERON:0012067 | primary bronchiole                        | proximal bronchiole                        | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [69](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=69:69)    | nan           |
|  70 | UBERON:0002051 | epithelium of bronchiole                  | epithelium of bronchiole                   | UBERON:8600000 | lobular bronchiole            | lobular bronchiole                         | [69](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=69:69)    | nan           |
|  71 | UBERON:0012067 | primary bronchiole                        | proximal bronchiole                        | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [70](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=70:70)    | nan           |
|  72 | UBERON:0002051 | epithelium of bronchiole                  | epithelium of bronchiole                   | UBERON:8600000 | lobular bronchiole            | lobular bronchiole                         | [70](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=70:70)    | nan           |
|  73 | UBERON:0012067 | primary bronchiole                        | proximal bronchiole                        | UBERON:8600009 | subsegmental bronchus         | subsegmental bronchus                      | [71](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=71:71)    | nan           |
|  74 | UBERON:0004515 | smooth muscle tissue of bronchiole        | smooth muscle tissue of bronchiole         | UBERON:8600000 | lobular bronchiole            | lobular bronchiole                         | [71](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=71:71)    | nan           |
|  75 | UBERON:0002299 | alveolus of lung                          | alveolus of lung on respiratory bronchiole | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [80](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=80:80)    | nan           |
|  76 | UBERON:0016405 | pulmonary capillary                       | pulmonary capillary                        | UBERON:0002299 | alveolus of lung              | alveolus of lung on respiratory bronchiole | [80](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=80:80)    | nan           |
|  77 | UBERON:0002299 | alveolus of lung                          | alveolus of lung on respiratory bronchiole | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [81](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=81:81)    | nan           |
|  78 | UBERON:0016405 | pulmonary capillary                       | pulmonary capillary                        | UBERON:0002299 | alveolus of lung              | alveolus of lung on respiratory bronchiole | [81](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=81:81)    | nan           |
|  79 | UBERON:0002299 | alveolus of lung                          | alveolus of lung on respiratory bronchiole | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [82](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=82:82)    | nan           |
|  80 | UBERON:0002299 | alveolus of lung                          | alveolus of lung on respiratory bronchiole | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [83](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=83:83)    | nan           |
|  81 | UBERON:0002299 | alveolus of lung                          | alveolus of lung on respiratory bronchiole | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [84](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=84:84)    | nan           |
|  82 | UBERON:0002299 | alveolus of lung                          | alveolus of lung on respiratory bronchiole | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [85](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=85:85)    | nan           |
|  83 | UBERON:0002299 | alveolus of lung                          | alveolus of lung on respiratory bronchiole | UBERON:0002188 | respiratory bronchiole        | respiratory bronchiole                     | [86](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=86:86)    | nan           |
|  84 | UBERON:0016405 | pulmonary capillary                       | pulmonary capillary                        | UBERON:0002173 | pulmonary alveolar duct       | pulmonary alveolar duct                    | [87](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=87:87)    | nan           |
|  85 | UBERON:0016405 | pulmonary capillary                       | pulmonary capillary                        | UBERON:0002173 | pulmonary alveolar duct       | pulmonary alveolar duct                    | [88](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=88:88)    | nan           |
|  91 | UBERON:0004849 | respiratory system venous endothelium     | respiratory system venous endothelium      | UBERON:0014904 | intersegmental pulmonary vein | intersegmental pulmonary vein              | [101](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=101:101) | nan           |
|  92 | UBERON:0004849 | respiratory system venous endothelium     | respiratory system venous endothelium      | UBERON:0014904 | intersegmental pulmonary vein | intersegmental pulmonary vein              | [102](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=102:102) | nan           |
|  96 | UBERON:0004849 | respiratory system venous endothelium     | respiratory system venous endothelium      | UBERON:0002012 | pulmonary vein                | pulmonary vein                             | [112](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=112:112) | nan           |
|  98 | UBERON:0012418 | respiratory system venous smooth muscle   | venous system smooth muscle                | UBERON:0002012 | pulmonary vein                | pulmonary vein                             | [113](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=113:113) | nan           |
| 101 | UBERON:0004849 | respiratory system venous endothelium     | respiratory system venous endothelium      | UBERON:0001592 | bronchial vein                | bronchial vein                             | [116](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=116:116) | nan           |
| 103 | UBERON:0012418 | respiratory system venous smooth muscle   | venous system smooth muscle                | UBERON:0001592 | bronchial vein                | bronchial vein                             | [117](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=117:117) | nan           |
| 104 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [118](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=118:118) | nan           |
| 105 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [119](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=119:119) | nan           |
| 106 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [120](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=120:120) | nan           |
| 107 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [121](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=121:121) | nan           |
| 108 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [122](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=122:122) | nan           |
| 109 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [123](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=123:123) | nan           |
| 110 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [124](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=124:124) | nan           |
| 111 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [125](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=125:125) | nan           |
| 112 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [126](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=126:126) | nan           |
| 113 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [127](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=127:127) | nan           |
| 114 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [128](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=128:128) | nan           |
| 115 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [129](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=129:129) | nan           |
| 116 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [130](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=130:130) | nan           |
| 117 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [131](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=131:131) | nan           |
| 118 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [132](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=132:132) | nan           |
| 119 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [133](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=133:133) | nan           |
| 120 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [134](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=134:134) | nan           |
| 121 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [135](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=135:135) | nan           |
| 122 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [136](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=136:136) | nan           |
| 123 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [137](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=137:137) | nan           |
| 124 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [138](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=138:138) | nan           |
| 125 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [139](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=139:139) | nan           |
| 126 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [140](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=140:140) | nan           |
| 127 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [141](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=141:141) | nan           |
| 128 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [142](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=142:142) | nan           |
| 129 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [143](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=143:143) | nan           |
| 130 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [144](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=144:144) | nan           |
| 131 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [145](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=145:145) | nan           |
| 132 | UBERON:0002405 | immune system                             | immune system of respiratory tract         | UBERON:0002048 | lung                          | lung                                       | [146](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=146:146) | nan           |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|     | s          | slabel                                                  | user_slabel                                             | o              | olabel                                    | user_olabel                                | row_number                                                                                                                   |       deltaIC |
|-----|------------|---------------------------------------------------------|---------------------------------------------------------|----------------|-------------------------------------------|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------|
|   2 | CL:4028004 | alveolar type 1 fibroblast cell                         | alveolar type 1 fibroblast cell                         | UBERON:0008870 | pulmonary alveolar parenchyma             | pulmonary alveolar parenchyma              | [100](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=100:100) |   3.55322e+13 |
|   3 | CL:4028006 | alveolar type 2 fibroblast cell                         | adventitial fibroblast                                  | UBERON:0008870 | pulmonary alveolar parenchyma             | pulmonary alveolar parenchyma              | [99](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=99:99)    |   3.55322e+13 |
|  11 | CL:0002619 | adult endothelial progenitor cell                       | adult endothelial progenitor cell                       | UBERON:0004849 | respiratory system venous endothelium     | respiratory system venous endothelium      | [101](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=101:101) | 100           |
|  12 | CL:0019003 | tracheobronchial goblet cell                            | tracheobronchial goblet cell                            | UBERON:0002341 | epithelium of segmental bronchus          | segmental bronchial epithelium             | [43](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=43:43)    | 100           |
|  13 | CL:0019003 | tracheobronchial goblet cell                            | tracheobronchial goblet cell                            | UBERON:0002341 | epithelium of segmental bronchus          | subsegmental bronchial epithelium          | [63](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=63:63)    | 100           |
|  19 | CL:0019018 | blood vessel smooth muscle cell                         | blood vessel smooth muscle cell                         | UBERON:0012418 | respiratory system venous smooth muscle   | venous system smooth muscle                | [113](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=113:113) | 100           |
|  20 | CL:0019018 | blood vessel smooth muscle cell                         | blood vessel smooth muscle cell                         | UBERON:0012418 | respiratory system venous smooth muscle   | venous system smooth muscle                | [117](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=117:117) | 100           |
|  23 | CL:0009089 | lung pericyte                                           | lung pericyte                                           | UBERON:0002299 | alveolus of lung                          | alveolus of lung on respiratory bronchiole | [84](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=84:84)    |   2.05518e-38 |
|  26 | CL:4033024 | airway submucosal gland duct basal cell                 | airway submucosal gland duct basal cell                 | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | [14](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=14:14)    | nan           |
|  28 | CL:4033023 | airway submucosal gland collecting duct epithelial cell | airway submucosal gland collecting duct epithelial cell | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | [15](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=15:15)    | nan           |
|  30 | CL:4033005 | serous secreting cell of bronchus submucosal gland      | serous secreting cell of bronchus submucosal gland      | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | [16](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=16:16)    | nan           |
|  32 | CL:4033022 | mucus secreting cell of bronchus submucosal gland       | mucus secreting cell of bronchus submucosal gland       | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | [17](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=17:17)    | nan           |
|  34 | CL:4033003 | myoepithelial cell of bronchus submucosal gland         | myoepithelial cell of bronchus submucosal gland         | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | [18](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=18:18)    | nan           |
|  35 | CL:4033026 | lung perichondrial fibroblast                           | lung perichondrial fibroblast                           | UBERON:0001956 | cartilage of bronchus                     | cartilage of bronchus                      | [21](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=21:21)    | nan           |
|  37 | CL:4033024 | airway submucosal gland duct basal cell                 | airway submucosal gland duct basal cell                 | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | [32](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=32:32)    | nan           |
|  39 | CL:4033023 | airway submucosal gland collecting duct epithelial cell | airway submucosal gland collecting duct epithelial cell | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | [33](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=33:33)    | nan           |
|  41 | CL:4033005 | serous secreting cell of bronchus submucosal gland      | serous secreting cell of bronchus submucosal gland      | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | [34](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=34:34)    | nan           |
|  43 | CL:4033022 | mucus secreting cell of bronchus submucosal gland       | mucus secreting cell of bronchus submucosal gland       | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | [35](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=35:35)    | nan           |
|  45 | CL:4033003 | myoepithelial cell of bronchus submucosal gland         | myoepithelial cell of bronchus submucosal gland         | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | [36](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=36:36)    | nan           |
|  48 | CL:4033024 | airway submucosal gland duct basal cell                 | airway submucosal gland duct basal cell                 | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | [52](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=52:52)    | nan           |
|  50 | CL:4033023 | airway submucosal gland collecting duct epithelial cell | airway submucosal gland collecting duct epithelial cell | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct           | [53](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=53:53)    | nan           |
|  52 | CL:4033005 | serous secreting cell of bronchus submucosal gland      | serous secreting cell of bronchus submucosal gland      | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | [54](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=54:54)    | nan           |
|  54 | CL:4033022 | mucus secreting cell of bronchus submucosal gland       | mucus secreting cell of bronchus submucosal gland       | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | [55](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=55:55)    | nan           |
|  56 | CL:4033003 | myoepithelial cell of bronchus submucosal gland         | myoepithelial cell of bronchus submucosal gland         | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                    | [56](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=56:56)    | nan           |
|  86 | CL:0002063 | type II pneumocyte                                      | alveolar type II cell                                   | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | [89](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=89:89)    | nan           |
|  87 | CL:0002062 | type I pneumocyte                                       | alveolar type I cell                                    | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | [90](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=90:90)    | nan           |
|  88 | CL:0009089 | lung pericyte                                           | lung pericyte                                           | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | [91](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=91:91)    | nan           |
|  89 | CL:4028006 | alveolar type 2 fibroblast cell                         | adventitial fibroblast                                  | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | [92](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=92:92)    | nan           |
|  90 | CL:4028004 | alveolar type 1 fibroblast cell                         | alveolar type 1 fibroblast cell                         | UBERON:0002173 | pulmonary alveolar duct                   | pulmonary alveolar duct                    | [93](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=93:93)    | nan           |
|  93 | CL:4033008 | vein endothelial cell of respiratory system             | vein endothelial cell of respiratory system             | UBERON:0004849 | respiratory system venous endothelium     | respiratory system venous endothelium      | [102](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=102:102) | nan           |
|  94 | CL:1001568 | pulmonary artery endothelial cell                       | pulmonary artery endothelial cell                       | UBERON:0004848 | respiratory system arterial endothelium   | respiratory system arterial endothelium    | [109](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=109:109) | nan           |
|  95 | CL:0002591 | smooth muscle cell of the pulmonary artery              | smooth muscle cell of the pulmonary artery              | UBERON:0012416 | respiratory system arterial smooth muscle | arterial system smooth muscle              | [110](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=110:110) | nan           |
|  97 | CL:4033008 | vein endothelial cell of respiratory system             | vein endothelial cell of respiratory system             | UBERON:0004849 | respiratory system venous endothelium     | respiratory system venous endothelium      | [112](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=112:112) | nan           |
|  99 | CL:1000413 | endothelial cell of artery                              | endothelial cell of artery                              | UBERON:0004848 | respiratory system arterial endothelium   | respiratory system arterial endothelium    | [114](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=114:114) | nan           |
| 100 | CL:0019018 | blood vessel smooth muscle cell                         | blood vessel smooth muscle cell                         | UBERON:0012416 | respiratory system arterial smooth muscle | arterial system smooth muscle              | [115](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=115:115) | nan           |
| 102 | CL:4033008 | vein endothelial cell of respiratory system             | vein endothelial cell of respiratory system             | UBERON:0004849 | respiratory system venous endothelium     | respiratory system venous endothelium      | [116](https://docs.google.com/spreadsheets/d/1StCXeg1J9YZaxRb-nnKsso3Dfv5pkH0DxF_8sz_DVMA/edit#gid=1109843030&range=116:116) | nan           |




# New CL terms
[**Report**](new_cl_terms_Lung.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Lung.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Lung_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Lung_AS_has_part_CT_log.tsv)