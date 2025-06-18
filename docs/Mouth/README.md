
ASCT+B Validation Reports for Mouth (2025-06-18)
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
  
- No issues found.


## Typos or punctuation mistakes


This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.  
  
- No issues found.


## Different labels


This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.

If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.

If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.  
  
1. The term _[UBERON:0004923](http://purl.obolibrary.org/obo/UBERON_0004923)_ has a different name/label in the source ontology in the following 1 row _[15](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=15:15)_. The name/label in the **ASCT+B table** is _mucosa of the lip_ and the one in the **ontology** is _organ component layer_. For reference, the given name/label **by SMEs** is _mucosa of the lip_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols4/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
1. No term id was found for the name/label _tongue_ in the following 1 row _[12](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=12:12)_.

1. No term id was found for the name/label _basal ductal cell_ in the following 3 rows _[18](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=18:18)_, _[36](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=36:36)_, _[53](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=53:53)_.

1. No term id was found for the name/label _excretory duct epithelial cell_ in the following 2 rows _[21](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=21:21)_, _[57](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=57:57)_.

1. No term id was found for the name/label _helper T_ in the following 3 rows _[22](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=22:22)_, _[40](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=40:40)_, _[58](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=58:58)_.

1. No term id was found for the name/label _ionocyte_ in the following 3 rows _[25](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=25:25)_, _[43](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=43:43)_, _[61](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=61:61)_.

1. No term id was found for the name/label _myoepithelial cell_ in the following 3 rows _[28](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=28:28)_, _[47](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=47:47)_, _[65](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=65:65)_.

1. No term id was found for the name/label _periacinar fibroblast_ in the following 3 rows _[29](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=29:29)_, _[48](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=48:48)_, _[66](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=66:66)_.

1. No term id was found for the name/label _periductal fibroblast_ in the following 3 rows _[31](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=31:31)_, _[50](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=50:50)_, _[68](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=68:68)_.

1. No term id was found for the name/label _serous acinar cell_ in the following 1 row _[32](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=32:32)_.

1. No term id was found for the name/label _tuft cell_ in the following 2 rows _[35](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=35:35)_, _[72](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=72:72)_.

1. No term id was found for the name/label _demilune acinar cell_ in the following 2 rows _[37](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=37:37)_, _[54](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=54:54)_.

1. No term id was found for the name/label _mucous acinar cell_ in the following 2 rows _[46](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=46:46)_, _[64](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=64:64)_.

1. No term id was found for the name/label _seromucosal acinar cell_ in the following 2 rows _[51](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=51:51)_, _[69](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=69:69)_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
1. The term _basal ductal cell_ without ontology ID has no parent that is from the CL ontology in the following 3 rows _[18](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=18:18)_, _[36](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=36:36)_, _[53](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=53:53)_.

1. The term _excretory duct epithelial cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[21](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=21:21)_, _[57](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=57:57)_.

1. The term _helper T_ without ontology ID has no parent that is from the CL ontology in the following 3 rows _[22](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=22:22)_, _[40](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=40:40)_, _[58](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=58:58)_.

1. The term _ionocyte_ without ontology ID has no parent that is from the CL ontology in the following 3 rows _[25](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=25:25)_, _[43](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=43:43)_, _[61](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=61:61)_.

1. The term _myoepithelial cell_ without ontology ID has no parent that is from the CL ontology in the following 3 rows _[28](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=28:28)_, _[47](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=47:47)_, _[65](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=65:65)_.

1. The term _periacinar fibroblast_ without ontology ID has no parent that is from the CL ontology in the following 3 rows _[29](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=29:29)_, _[48](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=48:48)_, _[66](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=66:66)_.

1. The term _periductal fibroblast_ without ontology ID has no parent that is from the CL ontology in the following 3 rows _[31](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=31:31)_, _[50](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=50:50)_, _[68](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=68:68)_.

1. The term _serous acinar cell_ without ontology ID has no parent that is from the CL ontology in the following 1 row _[32](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=32:32)_.

1. The term _tuft cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[35](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=35:35)_, _[72](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=72:72)_.

1. The term _demilune acinar cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[37](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=37:37)_, _[54](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=54:54)_.

1. The term _mucous acinar cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[46](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=46:46)_, _[64](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=64:64)_.

1. The term _seromucosal acinar cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[51](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=51:51)_, _[69](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=69:69)_.


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



|    | s                                                               | slabel                | user_slabel       | o                                                               | olabel       | user_olabel   | row_number                                                                                                                |   deltaIC |
|----|-----------------------------------------------------------------|-----------------------|-------------------|-----------------------------------------------------------------|--------------|---------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  2 | [UBERON:0004923](http://purl.obolibrary.org/obo/UBERON_0004923) | organ component layer | mucosa of the lip | [UBERON:0003729](http://purl.obolibrary.org/obo/UBERON_0003729) | mouth mucosa | mouth mucosa  | [15](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=15:15) |   23.1326 |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                              | user_slabel                       | o                                                               | olabel              | user_olabel         | row_number                                                                                                                |   deltaIC |
|----|---------------------------------------------------------|-------------------------------------|-----------------------------------|-----------------------------------------------------------------|---------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                    | endothelial cell                  | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland    | sublingual gland    | [39](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=39:39) |  24.0656  |
|  1 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                    | endothelial cell                  | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland | submandibular gland | [56](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=56:56) |  24.0656  |
|  3 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                    | endothelial cell                  | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland       | parotid gland       | [20](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=20:20) |  20.8561  |
|  4 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                  | smooth muscle cell                | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland    | sublingual gland    | [52](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=52:52) |  15.0772  |
|  5 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                  | smooth muscle cell                | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland | submandibular gland | [70](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=70:70) |  15.0772  |
|  6 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                      | dendritic cell                    | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland    | sublingual gland    | [38](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=38:38) |  12.5872  |
|  7 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                      | dendritic cell                    | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland | submandibular gland | [55](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=55:55) |  12.5872  |
|  8 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                          | macrophage                        | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland | submandibular gland | [62](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=62:62) |  12.2159  |
|  9 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                          | macrophage                        | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland    | sublingual gland    | [44](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=44:44) |  12.2159  |
| 10 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                  | smooth muscle cell                | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland       | parotid gland       | [33](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=33:33) |  11.8677  |
| 11 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                      | dendritic cell                    | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland       | parotid gland       | [19](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=19:19) |   9.37768 |
| 12 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                          | macrophage                        | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland       | parotid gland       | [26](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=26:26) |   9.00643 |
| 13 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                            | pericyte                          | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland    | sublingual gland    | [49](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=49:49) |   6.50147 |
| 14 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                            | pericyte                          | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland | submandibular gland | [67](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=67:67) |   6.50147 |
| 15 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                           | mast cell                         | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland    | sublingual gland    | [45](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=45:45) |   5.10265 |
| 16 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                           | mast cell                         | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland | submandibular gland | [63](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=63:63) |   5.10265 |
| 17 | [CL:0000136](http://purl.obolibrary.org/obo/CL_0000136) | adipocyte                           | adipocyte                         | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland       | parotid gland       | [17](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=17:17) |   5.00778 |
| 18 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                            | pericyte                          | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland       | parotid gland       | [30](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=30:30) |   3.292   |
| 19 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                           | mast cell                         | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland       | parotid gland       | [27](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=27:27) |   1.89317 |
| 20 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                     | IgA secreting plasma cell         | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland       | parotid gland       | [23](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=23:23) | nan       |
| 21 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland | intercalated duct epithelial cell | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland       | parotid gland       | [24](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=24:24) | nan       |
| 22 | [CL:4052049](http://purl.obolibrary.org/obo/CL_4052049) | striated cell of salivary gland     | striated duct epithelial cell     | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland       | parotid gland       | [34](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=34:34) | nan       |
| 23 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                     | IgA secreting plasma cell         | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland    | sublingual gland    | [41](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=41:41) | nan       |
| 24 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland | intercalated duct epithelial cell | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland    | sublingual gland    | [42](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=42:42) | nan       |
| 25 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                     | IgA secreting plasma cell         | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland | submandibular gland | [59](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=59:59) | nan       |
| 26 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland | intercalated duct epithelial cell | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland | submandibular gland | [60](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=60:60) | nan       |
| 27 | [CL:4052049](http://purl.obolibrary.org/obo/CL_4052049) | striated cell of salivary gland     | striated duct epithelial cell     | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland | submandibular gland | [71](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=71:71) | nan       |




# New CL terms
[**Report**](new_cl_terms_Mouth.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Mouth.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Mouth_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Mouth_AS_has_part_CT_log.tsv)