
ASCT+B Validation Reports for Main_Bronchus (2023-10-03)
========================================================

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
  
- No issues found.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
- No issues found.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
1. In row _[15](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=15:15)_, the term _ciliated cell of terminal ciliated ducts of submucosal glands_ without ontology ID has no parent that is from the CL ontology.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[15](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=15:15)_, the term _LMHA:00142_ is from another ontology that is not validated in this process.


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



|    | s              | slabel                                  | user_slabel                           | o              | olabel                    | user_olabel                | row_number                                                                                                       |   deltaIC |
|----|----------------|-----------------------------------------|---------------------------------------|----------------|---------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------|-----------|
|  3 | UBERON:8410043 | bronchus submucosal gland               | bronchial submucosal gland            | UBERON:0002182 | main bronchus             | extrapulmonary bronchus    | [15](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=15:15) |       nan |
|  4 | UBERON:8410043 | bronchus submucosal gland               | bronchial submucosal gland            | UBERON:0002182 | main bronchus             | extrapulmonary bronchus    | [16](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=16:16) |       nan |
|  5 | UBERON:8600013 | submucosal gland collecting duct        | submucosal gland collecting duct      | UBERON:8410043 | bronchus submucosal gland | bronchial submucosal gland | [16](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=16:16) |       nan |
|  7 | UBERON:8410043 | bronchus submucosal gland               | bronchial submucosal gland            | UBERON:0002182 | main bronchus             | extrapulmonary bronchus    | [17](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=17:17) |       nan |
|  8 | UBERON:8600012 | submucosal gland acinus                 | submucosal gland acinus               | UBERON:8410043 | bronchus submucosal gland | bronchial submucosal gland | [17](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=17:17) |       nan |
| 10 | UBERON:8410043 | bronchus submucosal gland               | bronchial submucosal gland            | UBERON:0002182 | main bronchus             | extrapulmonary bronchus    | [18](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=18:18) |       nan |
| 11 | UBERON:8600012 | submucosal gland acinus                 | submucosal gland acinus               | UBERON:8410043 | bronchus submucosal gland | bronchial submucosal gland | [18](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=18:18) |       nan |
| 13 | UBERON:8410043 | bronchus submucosal gland               | bronchial submucosal gland            | UBERON:0002182 | main bronchus             | extrapulmonary bronchus    | [19](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=19:19) |       nan |
| 14 | UBERON:8600012 | submucosal gland acinus                 | submucosal gland acinus               | UBERON:8410043 | bronchus submucosal gland | bronchial submucosal gland | [19](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=19:19) |       nan |
| 16 | UBERON:8410043 | bronchus submucosal gland               | bronchial submucosal gland            | UBERON:0002182 | main bronchus             | extrapulmonary bronchus    | [20](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=20:20) |       nan |
| 17 | UBERON:8600013 | submucosal gland collecting duct        | submucosal gland collecting duct      | UBERON:8410043 | bronchus submucosal gland | bronchial submucosal gland | [20](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=20:20) |       nan |
| 19 | UBERON:0001956 | cartilage of bronchus                   | cartilage of bronchus                 | UBERON:0002182 | main bronchus             | extrapulmonary bronchus    | [21](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=21:21) |       nan |
| 29 | UBERON:0004849 | respiratory system venous endothelium   | respiratory system venous endothelium | UBERON:0001592 | bronchial vein            | bronchial vein             | [33](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=33:33) |       nan |
| 31 | UBERON:0012418 | respiratory system venous smooth muscle | venous system smooth muscle           | UBERON:0001592 | bronchial vein            | bronchial vein             | [34](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=34:34) |       nan |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                                  | user_slabel                                             | o              | olabel                                    | user_olabel                             | row_number                                                                                                       |     deltaIC |
|----|------------|---------------------------------------------------------|---------------------------------------------------------|----------------|-------------------------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------|
|  0 | CL:0019018 | blood vessel smooth muscle cell                         | blood vessel smooth muscle cell                         | UBERON:0012418 | respiratory system venous smooth muscle   | venous system smooth muscle             | [34](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=34:34) | 100         |
|  1 | CL:0019002 | lung perichondrial fibroblast                           | lung perichondrial fibroblast                           | UBERON:0002182 | main bronchus                             | extrapulmonary bronchus                 | [22](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=22:22) |   0.0710073 |
|  2 | CL:0002329 | basal epithelial cell of tracheobronchial tree          | basal epithelial cell of tracheobronchial tree          | UBERON:0002340 | epithelium of main bronchus               | epithelium of main bronchus             | [30](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=30:30) |   2.252e-14 |
|  6 | CL:4033023 | airway submucosal gland collecting duct epithelial cell | airway submucosal gland collecting duct epithelial cell | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct        | [16](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=16:16) | nan         |
|  9 | CL:1000331 | serous cell of epithelium of bronchus                   | serous cell of epithelium of bronchus                   | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                 | [17](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=17:17) | nan         |
| 12 | CL:4033022 | mucus secreting cell of bronchus submucosal gland       | mucus secreting cell of bronchus submucosal gland       | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                 | [18](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=18:18) | nan         |
| 15 | CL:4033003 | myoepithelial cell of bronchus submucosal gland         | myoepithelial cell of bronchus submucosal gland         | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acinus                 | [19](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=19:19) | nan         |
| 18 | CL:4033024 | airway submucosal gland duct basal cell                 | airway submucosal gland duct basal cell                 | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct        | [20](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=20:20) | nan         |
| 20 | CL:0017000 | pulmonary ionocyte                                      | pulmonary ionocyte                                      | UBERON:0002340 | epithelium of main bronchus               | epithelium of main bronchus             | [23](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=23:23) | nan         |
| 21 | CL:4033010 | neuroendocrine cell of epithelium of lobar bronchus     | neuroendocrine cell of epithelium of lobar bronchus     | UBERON:0002340 | epithelium of main bronchus               | epithelium of main bronchus             | [24](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=24:24) | nan         |
| 22 | CL:4033048 | respiratory suprabasal cell                             | respiratory suprabasal cell                             | UBERON:0002340 | epithelium of main bronchus               | epithelium of main bronchus             | [25](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=25:25) | nan         |
| 23 | CL:0002332 | ciliated cell of the bronchus                           | ciliated cell of the bronchus                           | UBERON:0002340 | epithelium of main bronchus               | epithelium of main bronchus             | [26](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=26:26) | nan         |
| 24 | CL:4033007 | brush cell of epithelium of lobar bronchus              | tuft cell                                               | UBERON:0002340 | epithelium of main bronchus               | epithelium of main bronchus             | [27](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=27:27) | nan         |
| 25 | CL:4033044 | deuterosomal cell                                       | airway deuterosomal cell                                | UBERON:0002340 | epithelium of main bronchus               | epithelium of main bronchus             | [28](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=28:28) | nan         |
| 26 | CL:4033009 | goblet cell of epithelium of lobar bronchus             | goblet cell of epithelium of lobar bronchus             | UBERON:0002340 | epithelium of main bronchus               | epithelium of main bronchus             | [29](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=29:29) | nan         |
| 27 | CL:1000413 | endothelial cell of artery                              | endothelial cell of artery                              | UBERON:0004848 | respiratory system arterial endothelium   | respiratory system arterial endothelium | [31](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=31:31) | nan         |
| 28 | CL:0019018 | blood vessel smooth muscle cell                         | blood vessel smooth muscle cell                         | UBERON:0012416 | respiratory system arterial smooth muscle | arterial system smooth muscle           | [32](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=32:32) | nan         |
| 30 | CL:4033008 | vein endothelial cell of respiratory system             | vein endothelial cell of respiratory system             | UBERON:0004849 | respiratory system venous endothelium     | respiratory system venous endothelium   | [33](https://docs.google.com/spreadsheets/d/13O5Bb5_ki6uj4NcrFYoZPCHbYwrsPcyPJtdamUeZWZA/edit#gid=0&range=33:33) | nan         |




# New CL terms
[**Report**](new_cl_terms_Main_Bronchus.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Main_Bronchus.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Main_Bronchus_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Main_Bronchus_AS_has_part_CT_log.tsv)