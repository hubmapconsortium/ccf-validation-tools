
ASCT+B Validation Reports for Bone-Marrow (2023-09-20)
======================================================

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
  
- No issues found.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[39](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=39:39)_, no term id was found for the name/label _Myeloid progenitor_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
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



|    | row_number                                                                                                               | s          | slabel                                                | user_slabel                 | o          | olabel                                    | user_olabel                                  |          deltaIC |
|----|--------------------------------------------------------------------------------------------------------------------------|------------|-------------------------------------------------------|-----------------------------|------------|-------------------------------------------|----------------------------------------------|------------------|
|  2 | [56](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=56:56) | CL:0000824 | mature natural killer cell                            | mature Natural killer       | CL:0000814 | mature NK T cell                          | NK lymphocyte                                | 149433           |
|  3 | [55](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=55:55) | CL:0000938 | CD16-negative, CD56-bright natural killer cell, human | CD56 bright Natural Killer  | CL:0000814 | mature NK T cell                          | NK lymphocyte                                | 149333           |
|  4 | [40](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=40:40) | CL:0002193 | myelocyte                                             | myelocyte                   | CL:0000775 | neutrophil                                | neutrophilic granulocyte                     |     13.8758      |
|  5 | [23](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=23:23) | CL:0000840 | immature conventional dendritic cell                  | transitional Dendritic Cell | CL:0001056 | dendritic cell, human                     | dendritic cell                               |      3.36871e-10 |
|  6 | [28](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=28:28) | CL:0000553 | megakaryocyte progenitor cell                         | early Megakaryocyte         | CL:0000556 | Megakaryocyte                             | Megakaryocyte                                |      2.79505e-17 |
|  7 | [17](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=17:17) | CL:0000826 | pro-B cell                                            | pro B progenitor            | CL:0000945 | lymphocyte of B lineage                   | B lineage                                    |      4.92669e-41 |
| 15 | [19](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=19:19) | CL:0000990 | conventional dendritic cell                           | dendritic cell type 1       | CL:0001056 | dendritic cell, human                     | dendritic cell                               |    nan           |
| 17 | [20](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=20:20) | CL:0000990 | conventional dendritic cell                           | dendritic cell type 2       | CL:0001056 | dendritic cell, human                     | dendritic cell                               |    nan           |
| 19 | [21](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=21:21) | CL:0001056 | dendritic cell, human                                 | dendritic cell type 3       | CL:0001056 | dendritic cell, human                     | dendritic cell                               |    nan           |
| 23 | [24](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=24:24) | CL:0000764 | erythroid lineage cell                                | early erythroid             | CL:0000764 | erythroid lineage cell                    | erythroid                                    |    nan           |
| 25 | [25](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=25:25) | CL:0000764 | erythroid lineage cell                                | mid erythroid               | CL:0000764 | erythroid lineage cell                    | erythroid                                    |    nan           |
| 27 | [26](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=26:26) | CL:0000764 | erythroid lineage cell                                | late erythroid              | CL:0000764 | erythroid lineage cell                    | erythroid                                    |    nan           |
| 29 | [27](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=27:27) | CL:0000556 | megakaryocyte                                         | Megakaryocyte               | CL:0000556 | Megakaryocyte                             | Megakaryocyte                                |    nan           |
| 34 | [33](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=33:33) | CL:0000037 | hematopoietic stem cell                               | hemopoietic stem cell       | CL:0000837 | hematopoietic multipotent progenitor cell | hemopoietic stem cell/multipotent progenitor |    nan           |
| 37 | [35](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=35:35) | CL:0000837 | hematopoietic multipotent progenitor cell             | multipotent progenitor cell | CL:0000837 | hematopoietic multipotent progenitor cell | hemopoietic stem cell/multipotent progenitor |    nan           |
| 40 | [38](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=38:38) | CL:0000559 | promonocyte                                           | promonocyte                 | CL:0000576 | monocyte                                  | monocyte                                     |    nan           |
| 44 | [41](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=41:41) | CL:0000775 | neutrophil                                            | neutrophil                  | CL:0000775 | neutrophil                                | neutrophilic granulocyte                     |    nan           |
| 48 | [45](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=45:45) | CL:0000097 | mast cell                                             | mast cell                   | CL:0000094 | granulocyte                               | granulocyte                                  |    nan           |




## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | row_number                                                                                                               | s          | slabel                                                                     | user_slabel                                  | o              | olabel      | user_olabel   |       deltaIC |
|----|--------------------------------------------------------------------------------------------------------------------------|------------|----------------------------------------------------------------------------|----------------------------------------------|----------------|-------------|---------------|---------------|
|  0 | [31](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=31:31) | CL:0000049 | common myeloid progenitor                                                  | common myeloid progenitor                    | UBERON:0002371 | Bone marrow | Bone marrow   |   4.85236e+12 |
|  1 | [35](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=35:35) | CL:0000837 | hematopoietic multipotent progenitor cell                                  | multipotent progenitor cell                  | UBERON:0002371 | Bone marrow | Bone marrow   |   1.50231e+08 |
|  8 | [12](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=12:12) | CL:0000817 | precursor B cell                                                           | precursor B cell                             | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
|  9 | [13](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=13:13) | CL:0000816 | immature B cell                                                            | immature B cell                              | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 10 | [14](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=14:14) | CL:0000787 | memory B cell                                                              | memory B cell                                | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 11 | [15](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=15:15) | CL:0000788 | naive B cell                                                               | naive B cell                                 | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 12 | [16](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=16:16) | CL:0000786 | plasma cell                                                                | plasma cell                                  | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 13 | [17](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=17:17) | CL:0000826 | pro-B cell                                                                 | pro B progenitor                             | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 14 | [18](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=18:18) | CL:0000818 | transitional stage B cell                                                  | transitional B cell                          | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 16 | [19](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=19:19) | CL:0000990 | conventional dendritic cell                                                | dendritic cell type 1                        | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 18 | [20](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=20:20) | CL:0000990 | conventional dendritic cell                                                | dendritic cell type 2                        | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 20 | [21](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=21:21) | CL:0001056 | dendritic cell, human                                                      | dendritic cell type 3                        | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 21 | [22](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=22:22) | CL:0001058 | plasmacytoid dendritic cell, human                                         | Plasmacytoid Dendritic Cell                  | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 22 | [23](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=23:23) | CL:0000840 | immature conventional dendritic cell                                       | transitional Dendritic Cell                  | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 24 | [24](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=24:24) | CL:0000764 | erythroid lineage cell                                                     | early erythroid                              | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 26 | [25](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=25:25) | CL:0000764 | erythroid lineage cell                                                     | mid erythroid                                | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 28 | [26](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=26:26) | CL:0000764 | erythroid lineage cell                                                     | late erythroid                               | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 30 | [27](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=27:27) | CL:0000556 | megakaryocyte                                                              | Megakaryocyte                                | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 31 | [28](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=28:28) | CL:0000553 | megakaryocyte progenitor cell                                              | early Megakaryocyte                          | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 32 | [29](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=29:29) | CL:0000050 | megakaryocyte-erythroid progenitor cell                                    | megakaryocyte-erythroid-mast cell progenitor | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 33 | [30](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=30:30) | CL:0000051 | common lymphoid progenitor                                                 | common lymphoid progenitor                   | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 35 | [33](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=33:33) | CL:0000037 | hematopoietic stem cell                                                    | hemopoietic stem cell                        | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 36 | [34](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=34:34) | CL:0000936 | early lymphoid progenitor                                                  | lympho-myeloid progenitor cell               | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 38 | [36](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=36:36) | CL:0001054 | CD14-positive monocyte                                                     | CD14 monocyte                                | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 39 | [37](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=37:37) | CL:0002396 | CD14-low, CD16-positive monocyte                                           | CD16 monocyte                                | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 41 | [38](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=38:38) | CL:0000559 | promonocyte                                                                | promonocyte                                  | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 42 | [39](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=39:39) | CL:0000576 | monocyte                                                                   | monocyte                                     | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 43 | [40](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=40:40) | CL:0002193 | myelocyte                                                                  | myelocyte                                    | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 45 | [42](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=42:42) | CL:0000836 | promyelocyte                                                               | promyelocyte                                 | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 46 | [43](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=43:43) | CL:0000771 | eosinophil                                                                 | eosinophil                                   | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 47 | [44](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=44:44) | CL:0000767 | basophil                                                                   | basophil                                     | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 49 | [45](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=45:45) | CL:0000097 | mast cell                                                                  | mast cell                                    | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 50 | [46](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=46:46) | CL:0000895 | naive thymus-derived CD4-positive, alpha-beta T cell                       | CD4 naive                                    | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 51 | [47](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=47:47) | CL:0000897 | CD4-positive, alpha-beta memory T cell                                     | CD4 T cell memory                            | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 52 | [48](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=48:48) | CL:0000897 | CD4-positive, alpha-beta memory T cell                                     | CD4 T cell memory                            | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 53 | [49](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=49:49) | CL:0001087 | effector memory CD4-positive, alpha-beta T cell, terminally differentiated | CD4 T cell effector memory CD45RA            | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 54 | [50](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=50:50) | CL:0000900 | naive thymus-derived CD8-positive, alpha-beta T cell                       | CD8 naive                                    | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 55 | [51](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=51:51) | CL:0000909 | CD8-positive, alpha-beta memory T cell                                     | CD8 T cell memory                            | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 56 | [52](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=52:52) | CL:0000913 | effector memory CD8-positive, alpha-beta T cell                            | CD8 T cell effector memory                   | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 57 | [53](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=53:53) | CL:0001062 | effector memory CD8-positive, alpha-beta T cell, terminally differentiated | CD8 T cell effector memory CD45RA            | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 58 | [54](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=54:54) | CL:0000625 | CD8-positive, alpha-beta T cell                                            | mature CD8 T cell                            | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 59 | [55](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=55:55) | CL:0000938 | CD16-negative, CD56-bright natural killer cell, human                      | CD56 bright Natural Killer                   | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 60 | [56](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=56:56) | CL:0000824 | mature natural killer cell                                                 | mature Natural killer                        | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |
| 61 | [57](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=57:57) | CL:0000815 | regulatory T cell                                                          | T regulatory                                 | UBERON:0002371 | Bone marrow | Bone marrow   | nan           |




# New CL terms
[**Report**](new_cl_terms_Bone-Marrow.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Bone-Marrow.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Bone-Marrow_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Bone-Marrow_AS_has_part_CT_log.tsv)