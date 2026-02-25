
ASCT+B Validation Reports for Trachea (2026-02-25)
==================================================

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
  
1. The term _[UBERON:8600011](http://purl.obolibrary.org/obo/UBERON_8600011)_ has a different name/label in the source ontology in the following 1 row _[19](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=19:19)_. The name/label in the **ASCT+B table** is _terminal ciliated ducts for tracheal submucosal gland_ and the one in the **ontology** is _tracheal submucosal gland ciliated duct_. For reference, the given name/label **by SMEs** is _terminal ciliated ducts for tracheal submucosal gland_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. The term _[CL:0002145](http://purl.obolibrary.org/obo/CL_0002145)_ has a different name/label in the source ontology in the following 1 row _[11](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=11:11)_. The name/label in the **ASCT+B table** is _ciliated columnar cell of tracheobronchial tree_ and the one in the **ontology** is _multiciliated columnar cell of tracheobronchial tree_. For reference, the given name/label **by SMEs** is _ciliated columnar cell of tracheobronchial tree_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. The term _[CL:4033055](http://purl.obolibrary.org/obo/CL_4033055)_ has a different name/label in the source ontology in the following 1 row _[19](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=19:19)_. The name/label in the **ASCT+B table** is _airway submucosal gland duct ciliated cell _ and the one in the **ontology** is _airway submucosal gland duct multiciliated cell_. For reference, the given name/label **by SMEs** is _airway submucosal gland duct ciliated cell _. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. The term _[CL:1000223](http://purl.obolibrary.org/obo/CL_1000223)_ has a different name/label in the source ontology in the following 1 row _[12](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=12:12)_. The name/label in the **ASCT+B table** is _lung neuroendocrine cell_ and the one in the **ontology** is _pulmonary neuroendocrine cell_. For reference, the given name/label **by SMEs** is _lung neuroendocrine cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. The term _[UBERON:8600012](http://purl.obolibrary.org/obo/UBERON_8600012)_ has a different name/label in the source ontology in the following 3 rows _[17](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=17:17)_, _[21](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=21:21)_, _[22](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=22:22)_. The name/label in the **ASCT+B table** is _submucosal gland acini_ and the one in the **ontology** is _submucosal gland acinus_. For reference, the given name/label **by SMEs** is _submucosal gland acini_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols4/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
- No issues found.


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



|    | s                                                               | slabel                                  | user_slabel                           | o                                                               | olabel               | user_olabel               | row_number                                                                                                       |   deltaIC |
|----|-----------------------------------------------------------------|-----------------------------------------|---------------------------------------|-----------------------------------------------------------------|----------------------|---------------------------|------------------------------------------------------------------------------------------------------------------|-----------|
|  5 | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203) | trachea gland                           | tracheal submucosal gland             | [UBERON:0002202](http://purl.obolibrary.org/obo/UBERON_0002202) | submucosa of trachea | submucosa of trachea      | [17](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=17:17) |   1.65636 |
|  6 | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203) | trachea gland                           | tracheal submucosal gland             | [UBERON:0002202](http://purl.obolibrary.org/obo/UBERON_0002202) | submucosa of trachea | submucosa of trachea      | [18](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=18:18) |   1.65636 |
|  7 | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203) | trachea gland                           | tracheal submucosal gland             | [UBERON:0002202](http://purl.obolibrary.org/obo/UBERON_0002202) | submucosa of trachea | submucosa of trachea      | [19](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=19:19) |   1.65636 |
|  8 | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203) | trachea gland                           | tracheal submucosal gland             | [UBERON:0002202](http://purl.obolibrary.org/obo/UBERON_0002202) | submucosa of trachea | submucosa of trachea      | [20](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=20:20) |   1.65636 |
|  9 | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203) | trachea gland                           | tracheal submucosal gland             | [UBERON:0002202](http://purl.obolibrary.org/obo/UBERON_0002202) | submucosa of trachea | submucosa of trachea      | [21](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=21:21) |   1.65636 |
| 10 | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203) | trachea gland                           | tracheal submucosal gland             | [UBERON:0002202](http://purl.obolibrary.org/obo/UBERON_0002202) | submucosa of trachea | submucosa of trachea      | [22](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=22:22) |   1.65636 |
| 14 | [UBERON:8600012](http://purl.obolibrary.org/obo/UBERON_8600012) | submucosal gland acinus                 | submucosal gland acini                | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203) | trachea gland        | tracheal submucosal gland | [17](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=17:17) | nan       |
| 16 | [UBERON:8600013](http://purl.obolibrary.org/obo/UBERON_8600013) | submucosal gland collecting duct        | submucosal gland collecting duct      | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203) | trachea gland        | tracheal submucosal gland | [18](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=18:18) | nan       |
| 19 | [UBERON:8600013](http://purl.obolibrary.org/obo/UBERON_8600013) | submucosal gland collecting duct        | submucosal gland collecting duct      | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203) | trachea gland        | tracheal submucosal gland | [20](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=20:20) | nan       |
| 21 | [UBERON:8600012](http://purl.obolibrary.org/obo/UBERON_8600012) | submucosal gland acinus                 | submucosal gland acini                | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203) | trachea gland        | tracheal submucosal gland | [21](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=21:21) | nan       |
| 23 | [UBERON:8600012](http://purl.obolibrary.org/obo/UBERON_8600012) | submucosal gland acinus                 | submucosal gland acini                | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203) | trachea gland        | tracheal submucosal gland | [22](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=22:22) | nan       |
| 26 | [UBERON:0004849](http://purl.obolibrary.org/obo/UBERON_0004849) | respiratory system venous endothelium   | respiratory system venous endothelium | [UBERON:0001592](http://purl.obolibrary.org/obo/UBERON_0001592) | bronchial vein       | bronchial vein            | [28](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=28:28) | nan       |
| 28 | [UBERON:0012418](http://purl.obolibrary.org/obo/UBERON_0012418) | respiratory system venous smooth muscle | venous system smooth muscle           | [UBERON:0001592](http://purl.obolibrary.org/obo/UBERON_0001592) | bronchial vein       | bronchial vein            | [29](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=29:29) | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                                                  | user_slabel                                             | o                                                               | olabel                                    | user_olabel                                           | row_number                                                                                                       |   deltaIC |
|----|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------------|-------------------------------------------|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | [CL:0019019](http://purl.obolibrary.org/obo/CL_0019019) | tracheobronchial smooth muscle cell                     | tracheobronchial smooth muscle cell                     | [UBERON:0006680](http://purl.obolibrary.org/obo/UBERON_0006680) | trachealis                                | trachealis                                            | [16](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=16:16) |  22.1932  |
|  1 | [CL:0019018](http://purl.obolibrary.org/obo/CL_0019018) | blood vessel smooth muscle cell                         | blood vessel smooth muscle cell                         | [UBERON:0012418](http://purl.obolibrary.org/obo/UBERON_0012418) | respiratory system venous smooth muscle   | venous system smooth muscle                           | [29](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=29:29) |  20.6654  |
|  2 | [CL:0019002](http://purl.obolibrary.org/obo/CL_0019002) | tracheobronchial chondrocyte                            | tracheobronchial chondrocyte                            | [UBERON:0006679](http://purl.obolibrary.org/obo/UBERON_0006679) | carina of trachea                         | carina of trachea                                     | [23](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=23:23) |  19.4062  |
|  3 | [CL:0019018](http://purl.obolibrary.org/obo/CL_0019018) | blood vessel smooth muscle cell                         | blood vessel smooth muscle cell                         | [UBERON:0012416](http://purl.obolibrary.org/obo/UBERON_0012416) | respiratory system arterial smooth muscle | arterial system smooth muscle                         | [31](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=31:31) |  16.097   |
|  4 | [CL:1000413](http://purl.obolibrary.org/obo/CL_1000413) | endothelial cell of artery                              | endothelial cell of artery                              | [UBERON:0004848](http://purl.obolibrary.org/obo/UBERON_0004848) | respiratory system arterial endothelium   | respiratory system arterial endothelium               | [30](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=30:30) |  11.2357  |
| 11 | [CL:0019002](http://purl.obolibrary.org/obo/CL_0019002) | tracheobronchial chondrocyte                            | tracheobronchial chondrocyte                            | [UBERON:0003604](http://purl.obolibrary.org/obo/UBERON_0003604) | trachea cartilage                         | trachea cartilage                                     | [24](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=24:24) |   1.13263 |
| 12 | [CL:0002145](http://purl.obolibrary.org/obo/CL_0002145) | multiciliated columnar cell of tracheobronchial tree    | ciliated columnar cell of tracheobronchial tree         | [UBERON:0001901](http://purl.obolibrary.org/obo/UBERON_0001901) | epithelium of trachea                     | tracheal epithelium                                   | [11](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=11:11) | nan       |
| 13 | [CL:1000223](http://purl.obolibrary.org/obo/CL_1000223) | pulmonary neuroendocrine cell                           | lung neuroendocrine cell                                | [UBERON:0001901](http://purl.obolibrary.org/obo/UBERON_0001901) | epithelium of trachea                     | tracheal epithelium                                   | [12](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=12:12) | nan       |
| 15 | [CL:1000330](http://purl.obolibrary.org/obo/CL_1000330) | serous cell of epithelium of trachea                    | serous cell of epithelium of trachea                    | [UBERON:8600012](http://purl.obolibrary.org/obo/UBERON_8600012) | submucosal gland acinus                   | submucosal gland acini                                | [17](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=17:17) | nan       |
| 17 | [CL:4033023](http://purl.obolibrary.org/obo/CL_4033023) | airway submucosal gland collecting duct epithelial cell | airway submucosal gland collecting duct epithelial cell | [UBERON:8600013](http://purl.obolibrary.org/obo/UBERON_8600013) | submucosal gland collecting duct          | submucosal gland collecting duct                      | [18](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=18:18) | nan       |
| 18 | [CL:4033055](http://purl.obolibrary.org/obo/CL_4033055) | airway submucosal gland duct multiciliated cell         | airway submucosal gland duct ciliated cell              | [UBERON:8600011](http://purl.obolibrary.org/obo/UBERON_8600011) | tracheal submucosal gland ciliated duct   | terminal ciliated ducts for tracheal submucosal gland | [19](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=19:19) | nan       |
| 20 | [CL:4033024](http://purl.obolibrary.org/obo/CL_4033024) | airway submucosal gland duct basal cell                 | airway submucosal gland duct basal cell                 | [UBERON:8600013](http://purl.obolibrary.org/obo/UBERON_8600013) | submucosal gland collecting duct          | submucosal gland collecting duct                      | [20](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=20:20) | nan       |
| 22 | [CL:4033020](http://purl.obolibrary.org/obo/CL_4033020) | mucus secreting cell of trachea gland                   | mucus secreting cell of trachea gland                   | [UBERON:8600012](http://purl.obolibrary.org/obo/UBERON_8600012) | submucosal gland acinus                   | submucosal gland acini                                | [21](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=21:21) | nan       |
| 24 | [CL:4033021](http://purl.obolibrary.org/obo/CL_4033021) | myoepithelial cell of trachea gland                     | myoepithelial cell of trachea gland                     | [UBERON:8600012](http://purl.obolibrary.org/obo/UBERON_8600012) | submucosal gland acinus                   | submucosal gland acini                                | [22](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=22:22) | nan       |
| 25 | [CL:4033025](http://purl.obolibrary.org/obo/CL_4033025) | perichondrial fibroblast                                | perichondrial fibroblast                                | [UBERON:0003571](http://purl.obolibrary.org/obo/UBERON_0003571) | trachea connective tissue                 | trachea connective tissue                             | [27](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=27:27) | nan       |
| 27 | [CL:4033008](http://purl.obolibrary.org/obo/CL_4033008) | vein endothelial cell of respiratory system             | vein endothelial cell of respiratory system             | [UBERON:0004849](http://purl.obolibrary.org/obo/UBERON_0004849) | respiratory system venous endothelium     | respiratory system venous endothelium                 | [28](https://docs.google.com/spreadsheets/d/1GhOK8hoAE56CxSscEvqLD8-jAa_3SMbTVNF9gt9oI5M/edit#gid=0&range=28:28) | nan       |




# New CL terms
[**Report**](new_cl_terms_Trachea.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Trachea.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Trachea_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Trachea_AS_has_part_CT_log.tsv)