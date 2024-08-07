
ASCT+B Validation Reports for Bone-Marrow (2024-08-07)
======================================================

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



- No issues found.






## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



|    | row_number                                                                                                               | s                                                       | slabel                                                | user_slabel                 | o                                                       | olabel                                    | user_olabel                                  |    deltaIC |
|----|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|-------------------------------------------------------|-----------------------------|---------------------------------------------------------|-------------------------------------------|----------------------------------------------|------------|
|  0 | [19](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=19:19) | [CL:0000990](http://purl.obolibrary.org/obo/CL_0000990) | conventional dendritic cell                           | dendritic cell type 1       | [CL:0001056](http://purl.obolibrary.org/obo/CL_0001056) | dendritic cell, human                     | dendritic cell                               |  22.75     |
|  1 | [20](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=20:20) | [CL:0000990](http://purl.obolibrary.org/obo/CL_0000990) | conventional dendritic cell                           | dendritic cell type 2       | [CL:0001056](http://purl.obolibrary.org/obo/CL_0001056) | dendritic cell, human                     | dendritic cell                               |  22.75     |
|  2 | [23](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=23:23) | [CL:0000840](http://purl.obolibrary.org/obo/CL_0000840) | immature conventional dendritic cell                  | transitional Dendritic Cell | [CL:0001056](http://purl.obolibrary.org/obo/CL_0001056) | dendritic cell, human                     | dendritic cell                               |  11.2415   |
|  3 | [39](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=39:39) | [CL:0000839](http://purl.obolibrary.org/obo/CL_0000839) | myeloid lineage restricted progenitor cell            | Myeloid progenitor          | [CL:0000576](http://purl.obolibrary.org/obo/CL_0000576) | monocyte                                  | monocyte                                     |   6.39729  |
|  4 | [33](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=33:33) | [CL:0000037](http://purl.obolibrary.org/obo/CL_0000037) | hematopoietic stem cell                               | hemopoietic stem cell       | [CL:0000837](http://purl.obolibrary.org/obo/CL_0000837) | hematopoietic multipotent progenitor cell | hemopoietic stem cell/multipotent progenitor |   0.549838 |
| 10 | [17](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=17:17) | [CL:0000826](http://purl.obolibrary.org/obo/CL_0000826) | pro-B cell                                            | pro B progenitor            | [CL:0000945](http://purl.obolibrary.org/obo/CL_0000945) | lymphocyte of B lineage                   | B lineage                                    | nan        |
| 15 | [21](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=21:21) | [CL:0001056](http://purl.obolibrary.org/obo/CL_0001056) | dendritic cell, human                                 | dendritic cell type 3       | [CL:0001056](http://purl.obolibrary.org/obo/CL_0001056) | dendritic cell, human                     | dendritic cell                               | nan        |
| 19 | [24](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=24:24) | [CL:0000764](http://purl.obolibrary.org/obo/CL_0000764) | erythroid lineage cell                                | early erythroid             | [CL:0000764](http://purl.obolibrary.org/obo/CL_0000764) | erythroid lineage cell                    | erythroid                                    | nan        |
| 21 | [25](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=25:25) | [CL:0000764](http://purl.obolibrary.org/obo/CL_0000764) | erythroid lineage cell                                | mid erythroid               | [CL:0000764](http://purl.obolibrary.org/obo/CL_0000764) | erythroid lineage cell                    | erythroid                                    | nan        |
| 23 | [26](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=26:26) | [CL:0000764](http://purl.obolibrary.org/obo/CL_0000764) | erythroid lineage cell                                | late erythroid              | [CL:0000764](http://purl.obolibrary.org/obo/CL_0000764) | erythroid lineage cell                    | erythroid                                    | nan        |
| 25 | [27](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=27:27) | [CL:0000556](http://purl.obolibrary.org/obo/CL_0000556) | megakaryocyte                                         | Megakaryocyte               | [CL:0000556](http://purl.obolibrary.org/obo/CL_0000556) | Megakaryocyte                             | Megakaryocyte                                | nan        |
| 27 | [28](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=28:28) | [CL:0000553](http://purl.obolibrary.org/obo/CL_0000553) | megakaryocyte progenitor cell                         | early Megakaryocyte         | [CL:0000556](http://purl.obolibrary.org/obo/CL_0000556) | Megakaryocyte                             | Megakaryocyte                                | nan        |
| 34 | [35](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=35:35) | [CL:0000837](http://purl.obolibrary.org/obo/CL_0000837) | hematopoietic multipotent progenitor cell             | multipotent progenitor cell | [CL:0000837](http://purl.obolibrary.org/obo/CL_0000837) | hematopoietic multipotent progenitor cell | hemopoietic stem cell/multipotent progenitor | nan        |
| 38 | [38](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=38:38) | [CL:0000559](http://purl.obolibrary.org/obo/CL_0000559) | promonocyte                                           | promonocyte                 | [CL:0000576](http://purl.obolibrary.org/obo/CL_0000576) | monocyte                                  | monocyte                                     | nan        |
| 41 | [40](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=40:40) | [CL:0002193](http://purl.obolibrary.org/obo/CL_0002193) | myelocyte                                             | myelocyte                   | [CL:0000775](http://purl.obolibrary.org/obo/CL_0000775) | neutrophil                                | neutrophilic granulocyte                     | nan        |
| 43 | [41](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=41:41) | [CL:0000775](http://purl.obolibrary.org/obo/CL_0000775) | neutrophil                                            | neutrophil                  | [CL:0000775](http://purl.obolibrary.org/obo/CL_0000775) | neutrophil                                | neutrophilic granulocyte                     | nan        |
| 44 | [42](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=42:42) | [CL:0000836](http://purl.obolibrary.org/obo/CL_0000836) | promyelocyte                                          | promyelocyte                | [CL:0000775](http://purl.obolibrary.org/obo/CL_0000775) | neutrophil                                | neutrophilic granulocyte                     | nan        |
| 48 | [45](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=45:45) | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                             | mast cell                   | [CL:0000094](http://purl.obolibrary.org/obo/CL_0000094) | granulocyte                               | granulocyte                                  | nan        |
| 59 | [55](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=55:55) | [CL:0000938](http://purl.obolibrary.org/obo/CL_0000938) | CD16-negative, CD56-bright natural killer cell, human | CD56 bright Natural Killer  | [CL:0000814](http://purl.obolibrary.org/obo/CL_0000814) | mature NK T cell                          | NK lymphocyte                                | nan        |
| 61 | [56](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=56:56) | [CL:0000824](http://purl.obolibrary.org/obo/CL_0000824) | mature natural killer cell                            | mature Natural killer       | [CL:0000814](http://purl.obolibrary.org/obo/CL_0000814) | mature NK T cell                          | NK lymphocyte                                | nan        |




## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | row_number                                                                                                               | s                                                       | slabel                                                                     | user_slabel                                  | o                                                               | olabel      | user_olabel   |   deltaIC |
|----|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------|-----------------------------------------------------------------|-------------|---------------|-----------|
|  5 | [12](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=12:12) | [CL:0000817](http://purl.obolibrary.org/obo/CL_0000817) | precursor B cell                                                           | precursor B cell                             | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
|  6 | [13](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=13:13) | [CL:0000816](http://purl.obolibrary.org/obo/CL_0000816) | immature B cell                                                            | immature B cell                              | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
|  7 | [14](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=14:14) | [CL:0000787](http://purl.obolibrary.org/obo/CL_0000787) | memory B cell                                                              | memory B cell                                | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
|  8 | [15](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=15:15) | [CL:0000788](http://purl.obolibrary.org/obo/CL_0000788) | naive B cell                                                               | naive B cell                                 | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
|  9 | [16](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=16:16) | [CL:0000786](http://purl.obolibrary.org/obo/CL_0000786) | plasma cell                                                                | plasma cell                                  | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 11 | [17](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=17:17) | [CL:0000826](http://purl.obolibrary.org/obo/CL_0000826) | pro-B cell                                                                 | pro B progenitor                             | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 12 | [18](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=18:18) | [CL:0000818](http://purl.obolibrary.org/obo/CL_0000818) | transitional stage B cell                                                  | transitional B cell                          | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 13 | [19](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=19:19) | [CL:0000990](http://purl.obolibrary.org/obo/CL_0000990) | conventional dendritic cell                                                | dendritic cell type 1                        | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 14 | [20](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=20:20) | [CL:0000990](http://purl.obolibrary.org/obo/CL_0000990) | conventional dendritic cell                                                | dendritic cell type 2                        | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 16 | [21](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=21:21) | [CL:0001056](http://purl.obolibrary.org/obo/CL_0001056) | dendritic cell, human                                                      | dendritic cell type 3                        | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 17 | [22](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=22:22) | [CL:0001058](http://purl.obolibrary.org/obo/CL_0001058) | plasmacytoid dendritic cell, human                                         | Plasmacytoid Dendritic Cell                  | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 18 | [23](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=23:23) | [CL:0000840](http://purl.obolibrary.org/obo/CL_0000840) | immature conventional dendritic cell                                       | transitional Dendritic Cell                  | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 20 | [24](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=24:24) | [CL:0000764](http://purl.obolibrary.org/obo/CL_0000764) | erythroid lineage cell                                                     | early erythroid                              | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 22 | [25](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=25:25) | [CL:0000764](http://purl.obolibrary.org/obo/CL_0000764) | erythroid lineage cell                                                     | mid erythroid                                | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 24 | [26](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=26:26) | [CL:0000764](http://purl.obolibrary.org/obo/CL_0000764) | erythroid lineage cell                                                     | late erythroid                               | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 26 | [27](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=27:27) | [CL:0000556](http://purl.obolibrary.org/obo/CL_0000556) | megakaryocyte                                                              | Megakaryocyte                                | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 28 | [28](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=28:28) | [CL:0000553](http://purl.obolibrary.org/obo/CL_0000553) | megakaryocyte progenitor cell                                              | early Megakaryocyte                          | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 29 | [29](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=29:29) | [CL:0000050](http://purl.obolibrary.org/obo/CL_0000050) | megakaryocyte-erythroid progenitor cell                                    | megakaryocyte-erythroid-mast cell progenitor | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 30 | [30](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=30:30) | [CL:0000051](http://purl.obolibrary.org/obo/CL_0000051) | common lymphoid progenitor                                                 | common lymphoid progenitor                   | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 31 | [31](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=31:31) | [CL:0000049](http://purl.obolibrary.org/obo/CL_0000049) | common myeloid progenitor                                                  | common myeloid progenitor                    | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 32 | [33](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=33:33) | [CL:0000037](http://purl.obolibrary.org/obo/CL_0000037) | hematopoietic stem cell                                                    | hemopoietic stem cell                        | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 33 | [34](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=34:34) | [CL:0000936](http://purl.obolibrary.org/obo/CL_0000936) | early lymphoid progenitor                                                  | lympho-myeloid progenitor cell               | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 35 | [35](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=35:35) | [CL:0000837](http://purl.obolibrary.org/obo/CL_0000837) | hematopoietic multipotent progenitor cell                                  | multipotent progenitor cell                  | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 36 | [36](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=36:36) | [CL:0001054](http://purl.obolibrary.org/obo/CL_0001054) | CD14-positive monocyte                                                     | CD14 monocyte                                | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 37 | [37](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=37:37) | [CL:0002396](http://purl.obolibrary.org/obo/CL_0002396) | CD14-low, CD16-positive monocyte                                           | CD16 monocyte                                | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 39 | [38](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=38:38) | [CL:0000559](http://purl.obolibrary.org/obo/CL_0000559) | promonocyte                                                                | promonocyte                                  | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 40 | [39](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=39:39) | [CL:0000839](http://purl.obolibrary.org/obo/CL_0000839) | myeloid lineage restricted progenitor cell                                 | Myeloid progenitor                           | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 42 | [40](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=40:40) | [CL:0002193](http://purl.obolibrary.org/obo/CL_0002193) | myelocyte                                                                  | myelocyte                                    | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 45 | [42](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=42:42) | [CL:0000836](http://purl.obolibrary.org/obo/CL_0000836) | promyelocyte                                                               | promyelocyte                                 | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 46 | [43](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=43:43) | [CL:0000771](http://purl.obolibrary.org/obo/CL_0000771) | eosinophil                                                                 | eosinophil                                   | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 47 | [44](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=44:44) | [CL:0000767](http://purl.obolibrary.org/obo/CL_0000767) | basophil                                                                   | basophil                                     | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 49 | [45](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=45:45) | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                                                  | mast cell                                    | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 50 | [46](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=46:46) | [CL:0000895](http://purl.obolibrary.org/obo/CL_0000895) | naive thymus-derived CD4-positive, alpha-beta T cell                       | CD4 naive                                    | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 51 | [47](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=47:47) | [CL:0000897](http://purl.obolibrary.org/obo/CL_0000897) | CD4-positive, alpha-beta memory T cell                                     | CD4 T cell memory                            | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 52 | [48](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=48:48) | [CL:0000897](http://purl.obolibrary.org/obo/CL_0000897) | CD4-positive, alpha-beta memory T cell                                     | CD4 T cell memory                            | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 53 | [49](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=49:49) | [CL:0001087](http://purl.obolibrary.org/obo/CL_0001087) | effector memory CD4-positive, alpha-beta T cell, terminally differentiated | CD4 T cell effector memory CD45RA            | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 54 | [50](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=50:50) | [CL:0000900](http://purl.obolibrary.org/obo/CL_0000900) | naive thymus-derived CD8-positive, alpha-beta T cell                       | CD8 naive                                    | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 55 | [51](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=51:51) | [CL:0000909](http://purl.obolibrary.org/obo/CL_0000909) | CD8-positive, alpha-beta memory T cell                                     | CD8 T cell memory                            | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 56 | [52](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=52:52) | [CL:0000913](http://purl.obolibrary.org/obo/CL_0000913) | effector memory CD8-positive, alpha-beta T cell                            | CD8 T cell effector memory                   | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 57 | [53](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=53:53) | [CL:0001062](http://purl.obolibrary.org/obo/CL_0001062) | effector memory CD8-positive, alpha-beta T cell, terminally differentiated | CD8 T cell effector memory CD45RA            | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 58 | [54](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=54:54) | [CL:0000625](http://purl.obolibrary.org/obo/CL_0000625) | CD8-positive, alpha-beta T cell                                            | mature CD8 T cell                            | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 60 | [55](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=55:55) | [CL:0000938](http://purl.obolibrary.org/obo/CL_0000938) | CD16-negative, CD56-bright natural killer cell, human                      | CD56 bright Natural Killer                   | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 62 | [56](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=56:56) | [CL:0000824](http://purl.obolibrary.org/obo/CL_0000824) | mature natural killer cell                                                 | mature Natural killer                        | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |
| 63 | [57](https://docs.google.com/spreadsheets/d/1EbZkIPnQDfXRCk4m30Onlt5vCNdaypEkRZd--xvB4uM/edit#gid=771476671&range=57:57) | [CL:0000815](http://purl.obolibrary.org/obo/CL_0000815) | regulatory T cell                                                          | T regulatory                                 | [UBERON:0002371](http://purl.obolibrary.org/obo/UBERON_0002371) | Bone marrow | Bone marrow   |       nan |




# New CL terms
[**Report**](new_cl_terms_Bone-Marrow.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Bone-Marrow.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Bone-Marrow_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Bone-Marrow_AS_has_part_CT_log.tsv)