
ASCT+B Validation Reports for Lung (2023-05-24)
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
  
1. CL:4033043

1. CL:4033048

1. UBERON:8600013

1. UBERON:8600010

1. CL:4033042

1. CL:4033039

1. CL:4033038

1. CL:4033041

1. UBERON:8600012

1. CL:4033040

1. CL:4033045

1. CL:4033044


## Typos or punctuation mistakes


This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.  
  
- No issues found.


## Different labels


This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.

If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.

If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.  
  
1. In row _[13](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=13:13)_, the term _[UBERON:8410043](http://purl.obolibrary.org/obo/UBERON_8410043)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _bronchial submucosal gland_ and the one in the **ontology** is _bronchus submucosal gland_. For reference, the given name/label **by SMEs** is _bronchial submucosal gland_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[21](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=21:21)_, the term _[CL:0019002](http://purl.obolibrary.org/obo/CL_0019002)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _lung perichondrial fibroblast_ and the one in the **ontology** is _tracheobronchial chondrocyte_. For reference, the given name/label **by SMEs** is _lung perichondrial fibroblast_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
- No issues found.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[13](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=13:13)_, the term _LMHA:00142_ is from another ontology that is not validated in this process.

1. In row _[45](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=45:45)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[46](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=46:46)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[47](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=47:47)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[47](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=47:47)_, the term _LMHA:00142_ is from another ontology that is not validated in this process.

1. In row _[48](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=48:48)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[49](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=49:49)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[50](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=50:50)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[51](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=51:51)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[52](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=52:52)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[53](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=53:53)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[54](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=54:54)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[55](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=55:55)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[56](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=56:56)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[57](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=57:57)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[58](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=58:58)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[59](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=59:59)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[60](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=60:60)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[61](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=61:61)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[62](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=62:62)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[63](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=63:63)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[64](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=64:64)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[64](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=64:64)_, the term _FMA:323213_ is from another ontology that is not validated in this process.

1. In row _[65](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=65:65)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[65](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=65:65)_, the term _FMA:323213_ is from another ontology that is not validated in this process.

1. In row _[66](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=66:66)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[66](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=66:66)_, the term _FMA:323213_ is from another ontology that is not validated in this process.

1. In row _[67](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=67:67)_, the term _FMA:7312_ is from another ontology that is not validated in this process.

1. In row _[67](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=67:67)_, the term _FMA:323213_ is from another ontology that is not validated in this process.

1. In row _[86](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=86:86)_, the term _FMA:84472_ is from another ontology that is not validated in this process.

1. In row _[86](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=86:86)_, the term _FMA:76965_ is from another ontology that is not validated in this process.

1. In row _[87](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=87:87)_, the term _FMA:84472_ is from another ontology that is not validated in this process.

1. In row _[87](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=87:87)_, the term _FMA:76965_ is from another ontology that is not validated in this process.

1. In row _[88](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=88:88)_, the term _FMA:84472_ is from another ontology that is not validated in this process.


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



|     | s              | slabel                                          | user_slabel                                     | o              | olabel                           | user_olabel                        | row_number                                                                                                                   |   deltaIC |
|-----|----------------|-------------------------------------------------|-------------------------------------------------|----------------|----------------------------------|------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-----------|
|   0 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [82](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=82:82)    |  22.0725  |
|   1 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [76](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=76:76)    |  22.0725  |
|   2 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [74](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=74:74)    |  22.0725  |
|   3 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [73](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=73:73)    |  22.0725  |
|   4 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [72](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=72:72)    |  22.0725  |
|   5 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [71](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=71:71)    |  22.0725  |
|   6 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [70](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=70:70)    |  22.0725  |
|   7 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [69](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=69:69)    |  22.0725  |
|   8 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [68](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=68:68)    |  22.0725  |
|   9 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [77](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=77:77)    |  22.0725  |
|  10 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [78](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=78:78)    |  22.0725  |
|  11 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [79](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=79:79)    |  22.0725  |
|  12 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [75](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=75:75)    |  22.0725  |
|  13 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [80](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=80:80)    |  22.0725  |
|  14 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [81](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=81:81)    |  22.0725  |
|  15 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [83](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=83:83)    |  22.0725  |
|  16 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [84](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=84:84)    |  22.0725  |
|  17 | UBERON:0002187 | terminal bronchiole                             | terminal/ transitional Bronchioles              | UBERON:0010369 | secondary pulmonary lobule       | secondary pulmonary lobule         | [85](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=85:85)    |  22.0725  |
|  20 | UBERON:0001956 | cartilage of bronchus                           | cartilage of bronchus                           | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [46](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=46:46)    |  15.8836  |
|  21 | UBERON:0002299 | alveolus of lung                                | alveolus of lung                                | UBERON:0002173 | pulmonary alveolar duct          | pulmonary alveolar duct            | [79](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=79:79)    |  13.1746  |
|  22 | UBERON:0002299 | alveolus of lung                                | alveolus of lung                                | UBERON:0002173 | pulmonary alveolar duct          | pulmonary alveolar duct            | [80](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=80:80)    |  13.1746  |
|  23 | UBERON:0002299 | alveolus of lung                                | alveolus of lung                                | UBERON:0002173 | pulmonary alveolar duct          | pulmonary alveolar duct            | [78](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=78:78)    |  13.1746  |
|  24 | UBERON:0002299 | alveolus of lung                                | alveolus of lung                                | UBERON:0002173 | pulmonary alveolar duct          | pulmonary alveolar duct            | [77](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=77:77)    |  13.1746  |
|  25 | UBERON:0002299 | alveolus of lung                                | alveolus of lung                                | UBERON:0002173 | pulmonary alveolar duct          | Alveolar Ducts                     | [93](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=93:93)    |  13.1746  |
|  26 | UBERON:0002299 | alveolus of lung                                | alveolus of lung                                | UBERON:0002173 | pulmonary alveolar duct          | Alveolar Ducts                     | [94](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=94:94)    |  13.1746  |
|  27 | UBERON:0002299 | alveolus of lung                                | alveolus of lung                                | UBERON:0002173 | pulmonary alveolar duct          | Alveolar Ducts                     | [95](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=95:95)    |  13.1746  |
|  28 | UBERON:0002299 | alveolus of lung                                | alveolus of lung                                | UBERON:0002173 | pulmonary alveolar duct          | pulmonary alveolar duct            | [76](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=76:76)    |  13.1746  |
|  29 | UBERON:0002299 | alveolus of lung                                | alveolus of lung                                | UBERON:0002173 | pulmonary alveolar duct          | pulmonary alveolar duct            | [75](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=75:75)    |  13.1746  |
|  30 | UBERON:0002299 | alveolus of lung                                | alveolus of lung                                | UBERON:0002173 | pulmonary alveolar duct          | Alveolar Ducts                     | [96](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=96:96)    |  13.1746  |
|  31 | UBERON:0002299 | alveolus of lung                                | alveolus of lung                                | UBERON:0002173 | pulmonary alveolar duct          | pulmonary alveolar duct            | [74](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=74:74)    |  13.1746  |
|  32 | UBERON:0004884 | lobar bronchus mesenchyme                       | bronchial mesenchyme                            | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [63](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=63:63)    |  12.8897  |
|  33 | UBERON:0004242 | bronchus smooth muscle                          | bronchial smooth muscle                         | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [45](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=45:45)    |  11.8686  |
|  34 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [104](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=104:104) |  10.9671  |
|  35 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [121](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=121:121) |  10.9671  |
|  36 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [98](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=98:98)    |  10.9671  |
|  37 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [120](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=120:120) |  10.9671  |
|  38 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [99](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=99:99)    |  10.9671  |
|  39 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [119](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=119:119) |  10.9671  |
|  40 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [100](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=100:100) |  10.9671  |
|  41 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [101](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=101:101) |  10.9671  |
|  42 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [118](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=118:118) |  10.9671  |
|  43 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [102](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=102:102) |  10.9671  |
|  44 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [103](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=103:103) |  10.9671  |
|  45 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [105](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=105:105) |  10.9671  |
|  46 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [117](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=117:117) |  10.9671  |
|  47 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [116](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=116:116) |  10.9671  |
|  48 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [106](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=106:106) |  10.9671  |
|  49 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [115](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=115:115) |  10.9671  |
|  50 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [114](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=114:114) |  10.9671  |
|  51 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [113](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=113:113) |  10.9671  |
|  52 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [112](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=112:112) |  10.9671  |
|  53 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [111](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=111:111) |  10.9671  |
|  54 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [110](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=110:110) |  10.9671  |
|  55 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [109](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=109:109) |  10.9671  |
|  56 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [108](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=108:108) |  10.9671  |
|  57 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [107](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=107:107) |  10.9671  |
|  58 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [97](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=97:97)    |  10.9671  |
|  59 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [122](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=122:122) |  10.9671  |
|  60 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [96](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=96:96)    |  10.9671  |
|  61 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [95](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=95:95)    |  10.9671  |
|  62 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [94](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=94:94)    |  10.9671  |
|  63 | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | UBERON:0002048 | lung                             | lung                               | [93](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=93:93)    |  10.9671  |
|  64 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002341 | epithelium of segmental bronchus | segmental bronchial epithelium     | [47](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=47:47)    |   9.18281 |
|  65 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002341 | epithelium of segmental bronchus | segmental bronchial epithelium     | [48](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=48:48)    |   9.18281 |
|  66 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002341 | epithelium of segmental bronchus | segmental bronchial epithelium     | [49](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=49:49)    |   9.18281 |
|  67 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002341 | epithelium of segmental bronchus | segmental bronchial epithelium     | [50](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=50:50)    |   9.18281 |
|  68 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002341 | epithelium of segmental bronchus | segmental bronchial epithelium     | [51](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=51:51)    |   9.18281 |
|  69 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002341 | epithelium of segmental bronchus | segmental bronchial epithelium     | [52](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=52:52)    |   9.18281 |
|  80 | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | UBERON:0002173 | pulmonary alveolar duct          | pulmonary alveolar duct            | [81](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=81:81)    |   3.77929 |
|  81 | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | UBERON:0002173 | pulmonary alveolar duct          | pulmonary alveolar duct            | [82](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=82:82)    |   3.77929 |
|  82 | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | UBERON:0002173 | pulmonary alveolar duct          | pulmonary alveolar duct            | [83](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=83:83)    |   3.77929 |
|  83 | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | UBERON:0002173 | pulmonary alveolar duct          | pulmonary alveolar duct            | [84](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=84:84)    |   3.77929 |
|  86 | UBERON:0002009 | pulmonary nerve plexus                          | pulmonary nerve plexus                          | UBERON:0007196 | tracheobronchial tree            | tracheobronchial tree              | [12](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=12:12)    | nan       |
|  87 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002183 | lobar bronchus                   | secondary bronchus                 | [13](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=13:13)    | nan       |
|  88 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002183 | lobar bronchus                   | secondary bronchus                 | [14](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=14:14)    | nan       |
|  90 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002183 | lobar bronchus                   | secondary bronchus                 | [15](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=15:15)    | nan       |
|  92 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002183 | lobar bronchus                   | secondary bronchus                 | [16](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=16:16)    | nan       |
|  94 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002183 | lobar bronchus                   | secondary bronchus                 | [17](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=17:17)    | nan       |
|  96 | UBERON:8410043 | bronchus submucosal gland                       | bronchial submucosal gland                      | UBERON:0002183 | lobar bronchus                   | secondary bronchus                 | [18](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=18:18)    | nan       |
|  97 | UBERON:0003592 | bronchus connective tissue                      | bronchus connective tissue                      | UBERON:0002183 | lobar bronchus                   | secondary bronchus                 | [19](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=19:19)    | nan       |
|  98 | UBERON:0004242 | bronchus smooth muscle                          | bronchial smooth muscle                         | UBERON:0002183 | lobar bronchus                   | secondary bronchus                 | [20](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=20:20)    | nan       |
| 100 | UBERON:0001956 | cartilage of bronchus                           | cartilage of bronchus                           | UBERON:0002183 | lobar bronchus                   | secondary bronchus                 | [21](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=21:21)    | nan       |
| 106 | UBERON:0004242 | bronchus smooth muscle                          | bronchial smooth muscle                         | UBERON:0002184 | segmental bronchus               | tertiary bronchus                  | [32](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=32:32)    | nan       |
| 108 | UBERON:0001956 | cartilage of bronchus                           | cartilage of bronchus                           | UBERON:0002184 | segmental bronchus               | tertiary bronchus                  | [33](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=33:33)    | nan       |
| 114 | UBERON:0004884 | lobar bronchus mesenchyme                       | bronchial mesenchyme                            | UBERON:0002184 | segmental bronchus               | tertiary bronchus                  | [44](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=44:44)    | nan       |
| 118 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [47](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=47:47)    | nan       |
| 119 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [48](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=48:48)    | nan       |
| 121 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [49](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=49:49)    | nan       |
| 123 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [50](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=50:50)    | nan       |
| 125 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [51](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=51:51)    | nan       |
| 127 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [52](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=52:52)    | nan       |
| 128 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [53](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=53:53)    | nan       |
| 129 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [54](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=54:54)    | nan       |
| 131 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [55](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=55:55)    | nan       |
| 133 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [56](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=56:56)    | nan       |
| 134 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [57](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=57:57)    | nan       |
| 136 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [58](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=58:58)    | nan       |
| 137 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [59](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=59:59)    | nan       |
| 139 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [60](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=60:60)    | nan       |
| 140 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [61](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=61:61)    | nan       |
| 141 | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [62](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=62:62)    | nan       |
| 143 | UBERON:0012067 | primary bronchiole                              | proximal bronchiole                             | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [64](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=64:64)    | nan       |
| 146 | UBERON:0012067 | primary bronchiole                              | proximal bronchiole                             | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [65](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=65:65)    | nan       |
| 149 | UBERON:0012067 | primary bronchiole                              | proximal bronchiole                             | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [66](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=66:66)    | nan       |
| 150 | UBERON:0012067 | primary bronchiole                              | proximal bronchiole                             | UBERON:8600009 | subsegmental bronchus            | subsegmental bronchus              | [67](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=67:67)    | nan       |
| 157 | UBERON:0002173 | pulmonary alveolar duct                         | pulmonary alveolar duct                         | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [74](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=74:74)    | nan       |
| 158 | UBERON:0016405 | pulmonary capillary                             | pulmonary capillary                             | UBERON:0008870 | pulmonary alveolar parenchyma    | pulmonary alveolar duct parenchyma | [74](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=74:74)    | nan       |
| 160 | UBERON:0002173 | pulmonary alveolar duct                         | pulmonary alveolar duct                         | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [75](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=75:75)    | nan       |
| 161 | UBERON:0016405 | pulmonary capillary                             | pulmonary capillary                             | UBERON:0008870 | pulmonary alveolar parenchyma    | pulmonary alveolar duct parenchyma | [75](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=75:75)    | nan       |
| 163 | UBERON:0002173 | pulmonary alveolar duct                         | pulmonary alveolar duct                         | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [76](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=76:76)    | nan       |
| 164 | UBERON:0002173 | pulmonary alveolar duct                         | pulmonary alveolar duct                         | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [77](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=77:77)    | nan       |
| 166 | UBERON:0002173 | pulmonary alveolar duct                         | pulmonary alveolar duct                         | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [78](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=78:78)    | nan       |
| 168 | UBERON:0002173 | pulmonary alveolar duct                         | pulmonary alveolar duct                         | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [79](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=79:79)    | nan       |
| 170 | UBERON:0002173 | pulmonary alveolar duct                         | pulmonary alveolar duct                         | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [80](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=80:80)    | nan       |
| 172 | UBERON:0002173 | pulmonary alveolar duct                         | pulmonary alveolar duct                         | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [81](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=81:81)    | nan       |
| 174 | UBERON:0002173 | pulmonary alveolar duct                         | pulmonary alveolar duct                         | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [82](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=82:82)    | nan       |
| 176 | UBERON:0002173 | pulmonary alveolar duct                         | pulmonary alveolar duct                         | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [83](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=83:83)    | nan       |
| 177 | UBERON:0002173 | pulmonary alveolar duct                         | pulmonary alveolar duct                         | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [84](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=84:84)    | nan       |
| 182 | UBERON:0003529 | respiratory system lymphatic vessel endothelium | respiratory system lymphatic vessel endothelium | UBERON:0018227 | pulmonary lymphatic vessel       | pulmonary lymphatic vessel         | [88](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=88:88)    | nan       |
| 186 | UBERON:0008874 | Pulmonary Acinus                                | Pulmonary Acinus defined by terminal bronchiole | UBERON:0002405 | immune system                    | immune system of respiratory tract | [93](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=93:93)    | nan       |
| 187 | UBERON:0002173 | pulmonary alveolar duct                         | Alveolar Ducts                                  | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [93](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=93:93)    | nan       |
| 188 | UBERON:0008874 | Pulmonary Acinus                                | Pulmonary Acinus defined by terminal bronchiole | UBERON:0002405 | immune system                    | immune system of respiratory tract | [94](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=94:94)    | nan       |
| 189 | UBERON:0002173 | pulmonary alveolar duct                         | Alveolar Ducts                                  | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [94](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=94:94)    | nan       |
| 190 | UBERON:0008874 | Pulmonary Acinus                                | Pulmonary Acinus defined by terminal bronchiole | UBERON:0002405 | immune system                    | immune system of respiratory tract | [95](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=95:95)    | nan       |
| 191 | UBERON:0002173 | pulmonary alveolar duct                         | Alveolar Ducts                                  | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [95](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=95:95)    | nan       |
| 192 | UBERON:0008874 | Pulmonary Acinus                                | Pulmonary Acinus defined by terminal bronchiole | UBERON:0002405 | immune system                    | immune system of respiratory tract | [96](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=96:96)    | nan       |
| 193 | UBERON:0002173 | pulmonary alveolar duct                         | Alveolar Ducts                                  | UBERON:0002188 | respiratory bronchiole           | Respiratory bronchioles            | [96](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=96:96)    | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



|     | s          | slabel                                                  | user_slabel                                             | o          | olabel                                   | user_olabel                              | row_number                                                                                                                   |   deltaIC |
|-----|------------|---------------------------------------------------------|---------------------------------------------------------|------------|------------------------------------------|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-----------|
|  89 | CL:4033024 | airway submucosal gland duct basal cell                 | airway submucosal gland duct basal cell                 | CL:0002202 | epithelial cell of tracheobronchial tree | epithelial cell of tracheobronchial tree | [14](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=14:14)    |       nan |
|  91 | CL:1000331 | serous cell of epithelium of bronchus                   | serous cell of epithelium of bronchus                   | CL:0002202 | epithelial cell of tracheobronchial tree | epithelial cell of tracheobronchial tree | [15](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=15:15)    |       nan |
|  93 | CL:4033023 | airway submucosal gland collecting duct epithelial cell | airway submucosal gland collecting duct epithelial cell | CL:0002202 | epithelial cell of tracheobronchial tree | epithelial cell of tracheobronchial tree | [16](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=16:16)    |       nan |
|  95 | CL:4033022 | mucus secreting cell of bronchus submucosal gland       | mucus secreting cell of bronchus submucosal gland       | CL:0002202 | epithelial cell of tracheobronchial tree | epithelial cell of tracheobronchial tree | [17](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=17:17)    |       nan |
| 101 | CL:0019002 | tracheobronchial chondrocyte                            | lung perichondrial fibroblast                           | CL:0002241 | pulmonary interstitial fibroblast        | pulmonary interstitial fibroblast        | [21](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=21:21)    |       nan |
| 110 | CL:0000158 | club cell                                               | club cell                                               | CL:0000082 | epithelial cell of lung                  | epithelial cell of lung                  | [35](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=35:35)    |       nan |
| 111 | CL:1000143 | lung goblet cell                                        | bronchial goblet cell                                   | CL:0002202 | epithelial cell of tracheobronchial tree | epithelial cell of tracheobronchial tree | [38](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=38:38)    |       nan |
| 120 | CL:4033024 | airway submucosal gland duct basal cell                 | airway submucosal gland duct basal cell                 | CL:0002202 | epithelial cell of tracheobronchial tree | epithelial cell of tracheobronchial tree | [48](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=48:48)    |       nan |
| 122 | CL:1000331 | serous cell of epithelium of bronchus                   | serous cell of epithelium of bronchus                   | CL:0002202 | epithelial cell of tracheobronchial tree | epithelial cell of tracheobronchial tree | [49](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=49:49)    |       nan |
| 124 | CL:4033023 | airway submucosal gland collecting duct epithelial cell | airway submucosal gland collecting duct epithelial cell | CL:0002202 | epithelial cell of tracheobronchial tree | epithelial cell of tracheobronchial tree | [50](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=50:50)    |       nan |
| 126 | CL:4033022 | mucus secreting cell of bronchus submucosal gland       | mucus secreting cell of bronchus submucosal gland       | CL:0002202 | epithelial cell of tracheobronchial tree | epithelial cell of tracheobronchial tree | [51](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=51:51)    |       nan |
| 135 | CL:0000158 | club cell                                               | club cell                                               | CL:0000082 | epithelial cell of lung                  | epithelial cell of lung                  | [57](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=57:57)    |       nan |
| 138 | CL:1000143 | lung goblet cell                                        | bronchial goblet cell                                   | CL:0002202 | epithelial cell of tracheobronchial tree | epithelial cell of tracheobronchial tree | [59](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=59:59)    |       nan |
| 144 | CL:1000271 | lung ciliated cell                                      | lung ciliated cell                                      | CL:0000082 | epithelial cell of lung                  | epithelial cell of lung                  | [64](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=64:64)    |       nan |
| 147 | CL:0000158 | club cell                                               | club cell                                               | CL:0000082 | epithelial cell of lung                  | epithelial cell of lung                  | [65](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=65:65)    |       nan |
| 153 | CL:1000271 | lung ciliated cell                                      | lung ciliated cell                                      | CL:0000082 | epithelial cell of lung                  | epithelial cell of lung                  | [69](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=69:69)    |       nan |
| 155 | CL:0000158 | club cell                                               | club cell                                               | CL:0000082 | epithelial cell of lung                  | epithelial cell of lung                  | [70](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=70:70)    |       nan |
| 156 | CL:0000158 | club cell                                               | club cell                                               | CL:0000082 | epithelial cell of lung                  | epithelial cell of lung                  | [72](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=72:72)    |       nan |
| 180 | CL:4033008 | vein endothelial cell of respiratory system             | vein endothelial cell of respiratory system             | CL:1001567 | lung endothelial cell                    | lung endothelial cell                    | [87](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=87:87)    |       nan |
| 183 | CL:0009086 | endothelial cell of respiratory system lymphatic vessel | endothelial cell of respiratory system lymphatic vessel | CL:1001567 | lung endothelial cell                    | lung endothelial cell                    | [88](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=88:88)    |       nan |
| 185 | CL:0000186 | myofibroblast cell                                      | myofibroblast cell                                      | CL:0002320 | connective tissue cell                   | connective tissue cell                   | [91](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=91:91)    |       nan |
| 194 | CL:0000784 | plasmacytoid dendritic cell                             | plasmacytoid dendritic cell                             | CL:0000782 | myeloid dendritic cell                   | myeloid dendritic cell                   | [97](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=97:97)    |       nan |
| 195 | CL:0000556 | megakaryocyte                                           | megakaryocyte                                           | CL:0000766 | myeloid leukocyte                        | myeloid leukocyte                        | [113](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=113:113) |       nan |




## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                                  | user_slabel                                             | o              | olabel                                          | user_olabel                                     | row_number                                                                                                                   |
|----|------------|---------------------------------------------------------|---------------------------------------------------------|----------------|-------------------------------------------------|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
|  0 | CL:0000158 | club cell                                               | club cell                                               | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [57](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=57:57)    |
|  1 | CL:0000158 | club cell                                               | club cell                                               | UBERON:0002051 | epithelium of bronchiole                        | epithelium of bronchiole                        | [65](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=65:65)    |
|  2 | CL:0000158 | club cell                                               | club cell                                               | UBERON:0001958 | terminal bronchiole epithelium                  | terminal bronchiole epithelium                  | [70](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=70:70)    |
|  3 | CL:0000158 | club cell                                               | club cell                                               | UBERON:0001955 | epithelium of respiratory bronchiole            | epithelium of respiratory bronchiole            | [72](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=72:72)    |
|  4 | CL:0000158 | club cell                                               | club cell                                               | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [35](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=35:35)    |
|  5 | CL:0002062 | type I pneumocyte                                       | alveolar type I cell                                    | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | [77](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=77:77)    |
|  6 | CL:0002062 | type I pneumocyte                                       | alveolar type I cell                                    | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | [81](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=81:81)    |
|  7 | CL:0002063 | type II pneumocyte                                      | alveolar type II cell                                   | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | [83](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=83:83)    |
|  8 | CL:0002063 | type II pneumocyte                                      | alveolar type II cell                                   | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | [76](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=76:76)    |
|  9 | CL:0002208 | brush cell of bronchus                                  | tuft cell                                               | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [37](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=37:37)    |
| 10 | CL:0002208 | brush cell of bronchus                                  | tuft cell                                               | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [58](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=58:58)    |
| 11 | CL:0002329 | basal epithelial cell of tracheobronchial tree          | basal epithelial cell of tracheobronchial tree          | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [42](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=42:42)    |
| 12 | CL:0002329 | basal epithelial cell of tracheobronchial tree          | basal epithelial cell of tracheobronchial tree          | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [62](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=62:62)    |
| 13 | CL:0002329 | basal epithelial cell of tracheobronchial tree          | basal epithelial cell of tracheobronchial tree          | UBERON:0002339 | epithelium of lobar bronchus                    | lobar bronchial epithelium                      | [28](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=28:28)    |
| 14 | CL:0002332 | ciliated cell of the bronchus                           | ciliated cell of the bronchus                           | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [43](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=43:43)    |
| 15 | CL:0002332 | ciliated cell of the bronchus                           | ciliated cell of the bronchus                           | UBERON:0002339 | epithelium of lobar bronchus                    | lobar bronchial epithelium                      | [26](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=26:26)    |
| 16 | CL:0002332 | ciliated cell of the bronchus                           | ciliated cell of the bronchus                           | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [55](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=55:55)    |
| 17 | CL:0002598 | bronchial smooth muscle cell                            | bronchial smooth muscle cell                            | UBERON:0004242 | bronchus smooth muscle                          | bronchial smooth muscle                         | [32](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=32:32)    |
| 18 | CL:0002598 | bronchial smooth muscle cell                            | bronchial smooth muscle cell                            | UBERON:0004242 | bronchus smooth muscle                          | bronchial smooth muscle                         | [45](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=45:45)    |
| 19 | CL:0002598 | bronchial smooth muscle cell                            | bronchial smooth muscle cell                            | UBERON:0004242 | bronchus smooth muscle                          | bronchial smooth muscle                         | [20](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=20:20)    |
| 20 | CL:0002619 | adult endothelial progenitor cell                       | adult endothelial progenitor cell                       | UBERON:0004849 | respiratory system venous endothelium           | respiratory system venous endothelium           | [86](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=86:86)    |
| 21 | CL:0009086 | endothelial cell of respiratory system lymphatic vessel | endothelial cell of respiratory system lymphatic vessel | UBERON:0003529 | respiratory system lymphatic vessel endothelium | respiratory system lymphatic vessel endothelium | [88](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=88:88)    |
| 22 | CL:0009089 | lung pericyte                                           | lung pericyte                                           | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | [78](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=78:78)    |
| 23 | CL:0011103 | sympathetic neuron                                      | sympathetic neuron                                      | UBERON:0002009 | pulmonary nerve plexus                          | pulmonary nerve plexus                          | [12](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=12:12)    |
| 24 | CL:0017000 | pulmonary ionocyte                                      | pulmonary ionocyte                                      | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [54](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=54:54)    |
| 25 | CL:0017000 | pulmonary ionocyte                                      | pulmonary ionocyte                                      | UBERON:0002339 | epithelium of lobar bronchus                    | lobar bronchial epithelium                      | [23](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=23:23)    |
| 26 | CL:0017000 | pulmonary ionocyte                                      | pulmonary ionocyte                                      | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [40](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=40:40)    |
| 27 | CL:0019002 | tracheobronchial chondrocyte                            | lung perichondrial fibroblast                           | UBERON:0001956 | cartilage of bronchus                           | cartilage of bronchus                           | [21](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=21:21)    |
| 28 | CL:0019002 | tracheobronchial chondrocyte                            | tracheobronchial chondrocyte                            | UBERON:0001956 | cartilage of bronchus                           | cartilage of bronchus                           | [33](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=33:33)    |
| 29 | CL:0019002 | tracheobronchial chondrocyte                            | tracheobronchial chondrocyte                            | UBERON:0001956 | cartilage of bronchus                           | cartilage of bronchus                           | [46](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=46:46)    |
| 30 | CL:0019019 | tracheobronchial smooth muscle cell                     | tracheobronchial smooth muscle                          | UBERON:0004884 | lobar bronchus mesenchyme                       | bronchial mesenchyme                            | [63](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=63:63)    |
| 31 | CL:0019019 | tracheobronchial smooth muscle cell                     | tracheobronchial smooth muscle                          | UBERON:0004884 | lobar bronchus mesenchyme                       | bronchial mesenchyme                            | [44](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=44:44)    |
| 32 | CL:1000143 | lung goblet cell                                        | bronchial goblet cell                                   | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [59](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=59:59)    |
| 33 | CL:1000143 | lung goblet cell                                        | bronchial goblet cell                                   | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [38](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=38:38)    |
| 34 | CL:1000223 | lung neuroendocrine cell                                | lung neuroendocrine cell                                | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [61](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=61:61)    |
| 35 | CL:1000223 | lung neuroendocrine cell                                | lung neuroendocrine cell                                | UBERON:0002341 | epithelium of segmental bronchus                | segmental bronchial epithelium                  | [36](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=36:36)    |
| 36 | CL:1000271 | lung ciliated cell                                      | lung ciliated cell                                      | UBERON:0001958 | terminal bronchiole epithelium                  | terminal bronchiole epithelium                  | [69](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=69:69)    |
| 37 | CL:1000271 | lung ciliated cell                                      | lung ciliated cell                                      | UBERON:0002051 | epithelium of bronchiole                        | epithelium of bronchiole                        | [64](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=64:64)    |
| 38 | CL:4028002 | alveolar capillary type 1 endothelial cell              | CAP1 general capillary gCap                             | UBERON:0016405 | pulmonary capillary                             | pulmonary capillary                             | [75](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=75:75)    |
| 39 | CL:4028003 | alveolar capillary type 2 endothelial cell              | CAP2 aerocyte capillary aCap                            | UBERON:0016405 | pulmonary capillary                             | pulmonary capillary                             | [74](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=74:74)    |
| 40 | CL:4028004 | alveolar type 1 fibroblast cell                         | alveolar type 1 fibroblast cell                         | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | [80](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=80:80)    |
| 41 | CL:4028004 | alveolar type 1 fibroblast cell                         | alveolar type 1 fibroblast cell                         | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | [84](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=84:84)    |
| 42 | CL:4028006 | alveolar type 2 fibroblast cell                         | alveolar type 2 fibroblast cell                         | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | [79](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=79:79)    |
| 43 | CL:4028006 | alveolar type 2 fibroblast cell                         | alveolar type 2 fibroblast cell                         | UBERON:0008870 | pulmonary alveolar parenchyma                   | pulmonary alveolar duct parenchyma              | [82](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=82:82)    |
| 44 | CL:4033008 | vein endothelial cell of respiratory system             | vein endothelial cell of respiratory system             | UBERON:0004849 | respiratory system venous endothelium           | respiratory system venous endothelium           | [87](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=87:87)    |
| 45 | CL:4033017 | bronchiolar smooth muscle cell                          | bronchiolar smooth muscle cell                          | UBERON:0004516 | smooth muscle tissue of terminal bronchiole     | smooth muscle tissue of terminal bronchiole     | [68](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=68:68)    |
| 46 | CL:4033017 | bronchiolar smooth muscle cell                          | bronchiolar smooth muscle cell                          | UBERON:0004515 | smooth muscle tissue of bronchiole              | smooth muscle tissue of bronchiole              | [67](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=67:67)    |
| 47 | CL:4033017 | bronchiolar smooth muscle cell                          | bronchiolar smooth muscle cell                          | UBERON:0004517 | smooth muscle tissue of respiratory bronchiole  | smooth muscle tissue of respiratory bronchiole  | [85](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=85:85)    |
| 48 | CL:4033018 | lung megakaryocyte                                      | lung megakaryocyte                                      | UBERON:0002405 | immune system                                   | immune system of respiratory tract              | [113](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1109843030&range=113:113) |




# New CL terms
[**Report**](new_cl_terms_Lung.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Lung.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Lung_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Lung_AS_has_part_CT_log.tsv)