
ASCT+B Validation Reports for Trachea (2023-08-29)
==================================================

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
  
1. In row _[20](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=20:20)_, the term _[UBERON:8600011](http://purl.obolibrary.org/obo/UBERON_8600011)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _terminal ciliated ducts for tracheal submucosal gland_ and the one in the **ontology** is _tracheal submucosal gland ciliated duct_. For reference, the given name/label **by SMEs** is _terminal ciliated ducts for tracheal submucosal gland_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[18](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=18:18)_, the term _[UBERON:8600012](http://purl.obolibrary.org/obo/UBERON_8600012)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _submucosal gland acini_ and the one in the **ontology** is _submucosal gland acinus_. For reference, the given name/label **by SMEs** is _submucosal gland acini_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
- No issues found.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[20](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=20:20)_, the term _LMHA:00142_ is from another ontology that is not validated in this process.


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



|    | s              | slabel                                  | user_slabel                           | o              | olabel               | user_olabel               | row_number                                                                                                       |   deltaIC |
|----|----------------|-----------------------------------------|---------------------------------------|----------------|----------------------|---------------------------|------------------------------------------------------------------------------------------------------------------|-----------|
|  6 | UBERON:0005203 | trachea gland                           | tracheal submucosal gland             | UBERON:0002202 | submucosa of trachea | submucosa of trachea      | [18](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=18:18) |       nan |
|  7 | UBERON:8600012 | submucosal gland acinus                 | submucosal gland acini                | UBERON:0005203 | trachea gland        | tracheal submucosal gland | [18](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=18:18) |       nan |
|  9 | UBERON:0005203 | trachea gland                           | tracheal submucosal gland             | UBERON:0002202 | submucosa of trachea | submucosa of trachea      | [19](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=19:19) |       nan |
| 10 | UBERON:8600013 | submucosal gland collecting duct        | submucosal gland collecting duct      | UBERON:0005203 | trachea gland        | tracheal submucosal gland | [19](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=19:19) |       nan |
| 12 | UBERON:0005203 | trachea gland                           | tracheal submucosal gland             | UBERON:0002202 | submucosa of trachea | submucosa of trachea      | [20](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=20:20) |       nan |
| 13 | UBERON:0005203 | trachea gland                           | tracheal submucosal gland             | UBERON:0002202 | submucosa of trachea | submucosa of trachea      | [21](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=21:21) |       nan |
| 14 | UBERON:8600013 | submucosal gland collecting duct        | submucosal gland collecting duct      | UBERON:0005203 | trachea gland        | tracheal submucosal gland | [21](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=21:21) |       nan |
| 16 | UBERON:0005203 | trachea gland                           | tracheal submucosal gland             | UBERON:0002202 | submucosa of trachea | submucosa of trachea      | [22](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=22:22) |       nan |
| 17 | UBERON:8600012 | submucosal gland acinus                 | submucosal gland acini                | UBERON:0005203 | trachea gland        | tracheal submucosal gland | [22](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=22:22) |       nan |
| 19 | UBERON:0005203 | trachea gland                           | tracheal submucosal gland             | UBERON:0002202 | submucosa of trachea | submucosa of trachea      | [23](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=23:23) |       nan |
| 20 | UBERON:8600012 | submucosal gland acinus                 | submucosal gland acini                | UBERON:0005203 | trachea gland        | tracheal submucosal gland | [23](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=23:23) |       nan |
| 23 | UBERON:0004849 | respiratory system venous endothelium   | respiratory system venous endothelium | UBERON:0001592 | bronchial vein       | bronchial vein            | [29](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=29:29) |       nan |
| 25 | UBERON:0012418 | respiratory system venous smooth muscle | venous system smooth muscle           | UBERON:0001592 | bronchial vein       | bronchial vein            | [30](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=30:30) |       nan |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                                  | user_slabel                                             | o              | olabel                                    | user_olabel                             | row_number                                                                                                       |
|----|------------|---------------------------------------------------------|---------------------------------------------------------|----------------|-------------------------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------|
|  0 | CL:0002145 | ciliated columnar cell of tracheobronchial tree         | ciliated columnar cell of tracheobronchial tree         | UBERON:0001901 | epithelium of trachea                     | tracheal epithelium                     | [12](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=12:12) |
|  1 | CL:0019002 | tracheobronchial chondrocyte                            | tracheobronchial chondrocyte                            | UBERON:0006679 | carina of trachea                         | carina of trachea                       | [24](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=24:24) |
|  2 | CL:0019002 | tracheobronchial chondrocyte                            | tracheobronchial chondrocyte                            | UBERON:0003604 | trachea cartilage                         | trachea cartilage                       | [25](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=25:25) |
|  3 | CL:0019018 | blood vessel smooth muscle cell                         | blood vessel smooth muscle cell                         | UBERON:0012418 | respiratory system venous smooth muscle   | venous system smooth muscle             | [30](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=30:30) |
|  4 | CL:0019018 | blood vessel smooth muscle cell                         | blood vessel smooth muscle cell                         | UBERON:0012416 | respiratory system arterial smooth muscle | arterial system smooth muscle           | [32](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=32:32) |
|  5 | CL:0019019 | tracheobronchial smooth muscle cell                     | tracheobronchial smooth muscle cell                     | UBERON:0006680 | trachealis                                | trachealis                              | [17](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=17:17) |
|  6 | CL:1000223 | lung neuroendocrine cell                                | lung neuroendocrine cell                                | UBERON:0001901 | epithelium of trachea                     | tracheal epithelium                     | [13](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=13:13) |
|  7 | CL:1000330 | serous cell of epithelium of trachea                    | serous cell of epithelium of trachea                    | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acini                  | [18](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=18:18) |
|  8 | CL:1000413 | endothelial cell of artery                              | endothelial cell of artery                              | UBERON:0004848 | respiratory system arterial endothelium   | respiratory system arterial endothelium | [31](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=31:31) |
|  9 | CL:4033008 | vein endothelial cell of respiratory system             | vein endothelial cell of respiratory system             | UBERON:0004849 | respiratory system venous endothelium     | respiratory system venous endothelium   | [29](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=29:29) |
| 10 | CL:4033020 | mucus secreting cell of trachea gland                   | mucus secreting cell of trachea gland                   | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acini                  | [22](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=22:22) |
| 11 | CL:4033021 | myoepithelial cell of trachea gland                     | myoepithelial cell of trachea gland                     | UBERON:8600012 | submucosal gland acinus                   | submucosal gland acini                  | [23](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=23:23) |
| 12 | CL:4033023 | airway submucosal gland collecting duct epithelial cell | airway submucosal gland collecting duct epithelial cell | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct        | [19](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=19:19) |
| 13 | CL:4033024 | airway submucosal gland duct basal cell                 | airway submucosal gland duct basal cell                 | UBERON:8600013 | submucosal gland collecting duct          | submucosal gland collecting duct        | [21](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=21:21) |
| 14 | CL:4033025 | perichondrial fibroblast                                | perichondrial fibroblast                                | UBERON:0003571 | trachea connective tissue                 | trachea connective tissue               | [28](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=28:28) |




# New CL terms
[**Report**](new_cl_terms_Trachea.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Trachea.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Trachea_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Trachea_AS_has_part_CT_log.tsv)