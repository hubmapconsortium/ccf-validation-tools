
ASCT+B Validation Reports for Kidney (2023-05-02)
=================================================

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
  
1. In row _[12](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=12:12)_, no term id was found for the name/label _capsule mesenchymal stromal cell_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=17:17)_, no term id was found for the name/label _descending thin limb of loop of Henle 2_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=31:31)_, no term id was found for the name/label _descending thin limb of loop of Henle 1_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=32:32)_, no term id was found for the name/label _descending thin limb of loop of Henle 2_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=33:33)_, no term id was found for the name/label _descending thin limb of loop of Henle 3_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=52:52)_, no term id was found for the name/label _Transitional principal-intercalated cell_.

1. In row _[81](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=81:81)_, no term id was found for the name/label _Monocyte Derived Cell_.

1. In row _[89](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=89:89)_, no term id was found for the name/label _Papillary Tip Epithelium_.


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



|    | s              | slabel                                | user_slabel                        | o              | olabel                                | user_olabel                        | row_number                                                                                                               |    deltaIC |
|----|----------------|---------------------------------------|------------------------------------|----------------|---------------------------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------|------------|
|  0 | UBERON:0001986 | endothelium                           | Endothelium (non glomerular)       | UBERON:0009091 | vasa recta ascending limb             | Ascending Vasa Recta               | [64](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=64:64) |  38.2152   |
|  1 | UBERON:0001986 | endothelium                           | Endothelium (non glomerular)       | UBERON:0009202 | vasa recta descending limb            | Descending Vasa Recta              | [63](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=63:63) |  38.2152   |
|  2 | UBERON:0004188 | glomerular epithelium                 | Glomerular Epithelium              | UBERON:0002189 | outer cortex of kidney                | outer cortex of kidney             | [13](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=13:13) |  25.1418   |
|  3 | UBERON:0004188 | glomerular epithelium                 | Glomerular Epithelium              | UBERON:0001284 | renal column                          | renal column (column of Bertin)    | [20](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=20:20) |  25.1418   |
|  4 | UBERON:0004188 | glomerular epithelium                 | Glomerular Epithelium              | UBERON:0005271 | juxtamedullary cortex                 | juxtamedullary cortex              | [14](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=14:14) |  25.1418   |
|  5 | UBERON:0001981 | blood vessel                          | Blood Vessel                       | UBERON:0006544 | kidney vasculature                    | Vessels                            | [60](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=60:60) |  19.2529   |
|  6 | UBERON:0001981 | blood vessel                          | Blood Vessel                       | UBERON:0006544 | kidney vasculature                    | Vessels                            | [64](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=64:64) |  19.2529   |
|  7 | UBERON:0001981 | blood vessel                          | Blood Vessel                       | UBERON:0006544 | kidney vasculature                    | Vessels                            | [63](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=63:63) |  19.2529   |
|  8 | UBERON:0001981 | blood vessel                          | Blood Vessel                       | UBERON:0006544 | kidney vasculature                    | Vessels                            | [61](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=61:61) |  19.2529   |
|  9 | UBERON:0004640 | renal efferent arteriole              | Efferent Arteriole                 | UBERON:0034884 | juxtaglomerular arteriole             | Juxtaglomerular Arteriole          | [61](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=61:61) |  16.4603   |
| 10 | UBERON:0004639 | renal afferent arteriole              | Afferent Arteriole                 | UBERON:0034884 | juxtaglomerular arteriole             | Juxtaglomerular Arteriole          | [60](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=60:60) |  15.8839   |
| 13 | UBERON:0001986 | endothelium                           | Endothelium (non glomerular)       | UBERON:0003517 | kidney blood vessel                   | Kidney Blood Vessel                | [59](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=59:59) |  14.4317   |
| 14 | UBERON:0001981 | blood vessel                          | Blood Vessel                       | UBERON:0001229 | Renal Corpuscle                       | Renal Corpuscle                    | [24](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=24:24) |  13.6903   |
| 15 | UBERON:0001289 | descending limb of loop of Henle      | Loop of Henle (Thin Limb)          | UBERON:0004201 | kidney outer medulla inner stripe     | kidney outer medulla inner stripe  | [17](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=17:17) |   7.58549  |
| 17 | UBERON:0001473 | lymphatic vessel                      | Lymphatic Vessel                   | UBERON:0006544 | kidney vasculature                    | Vessels                            | [65](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=65:65) |   4.68763  |
| 18 | UBERON:0004203 | cortical collecting duct              | Collecting Duct (Cortex)           | UBERON:0009883 | medullary ray                         | medullary ray                      | [15](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=15:15) |   4.59149  |
| 22 | UBERON:0002335 | macula densa                          | Macula Densa                       | UBERON:0001291 | thick ascending limb of loop of Henle | Loop of Henle (Thick Limb/ Cortex) | [38](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=38:38) |   1.02111  |
| 23 | UBERON:0001291 | thick ascending limb of loop of Henle | Loop of Henle (Thick Limb/Medulla) | UBERON:0004202 | kidney outer medulla outer stripe     | kidney outer medulla outer stripe  | [16](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=16:16) |   0.576374 |
| 24 | UBERON:0009202 | vasa recta descending limb            | Descending Vasa Recta              | UBERON:0001294 | inner medulla of kidney               | inner medulla of kidney            | [18](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=18:18) | nan        |
| 26 | UBERON:0001284 | renal column                          | renal column (column of Bertin)    | UBERON:0001225 | cortex of kidney                      | renal cortex                       | [20](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=20:20) | nan        |
| 27 | UBERON:0009202 | vasa recta descending limb            | Descending Vasa Recta              | UBERON:0004200 | kidney pyramid                        | renal pyramid                      | [21](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=21:21) | nan        |
| 28 | UBERON:0004190 | renal glomerulus vasculature          | Glomerulus Vasculature             | UBERON:0001981 | blood vessel                          | Blood Vessel                       | [24](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=24:24) | nan        |
| 29 | UBERON:0005215 | kidney interstitium                   | Interstitium                       | UBERON:0001229 | Renal Corpuscle                       | Renal Corpuscle                    | [25](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=25:25) | nan        |
| 33 | UBERON:0001232 | collecting duct of renal tubule       | Collecting Duct                    | UBERON:0001232 | collecting duct of renal tubule       | Tubules                            | [47](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=47:47) | nan        |
| 34 | UBERON:0001232 | collecting duct of renal tubule       | Collecting Duct                    | UBERON:0001232 | collecting duct of renal tubule       | Tubules                            | [48](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=48:48) | nan        |
| 35 | UBERON:0001232 | collecting duct of renal tubule       | Collecting Duct                    | UBERON:0001232 | collecting duct of renal tubule       | Tubules                            | [52](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=52:52) | nan        |
| 36 | UBERON:0001232 | collecting duct of renal tubule       | Collecting Duct                    | UBERON:0001232 | collecting duct of renal tubule       | Tubules                            | [53](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=53:53) | nan        |
| 37 | UBERON:0001232 | collecting duct of renal tubule       | Collecting Duct                    | UBERON:0001232 | collecting duct of renal tubule       | Tubules                            | [54](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=54:54) | nan        |
| 38 | UBERON:0001232 | collecting duct of renal tubule       | Collecting Duct                    | UBERON:0001232 | collecting duct of renal tubule       | Tubules                            | [57](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=57:57) | nan        |
| 39 | UBERON:0002303 | juxtaglomerular apparatus             | Juxtaglomerular Apparatus          | UBERON:0001981 | blood vessel                          | Blood Vessel                       | [60](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=60:60) | nan        |
| 40 | UBERON:0034884 | juxtaglomerular arteriole             | Juxtaglomerular Arteriole          | UBERON:0002303 | juxtaglomerular apparatus             | Juxtaglomerular Apparatus          | [60](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=60:60) | nan        |
| 41 | UBERON:0002303 | juxtaglomerular apparatus             | Juxtaglomerular Apparatus          | UBERON:0001981 | blood vessel                          | Blood Vessel                       | [61](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=61:61) | nan        |
| 42 | UBERON:0034884 | juxtaglomerular arteriole             | Juxtaglomerular Arteriole          | UBERON:0002303 | juxtaglomerular apparatus             | Juxtaglomerular Apparatus          | [61](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=61:61) | nan        |
| 44 | UBERON:0002303 | juxtaglomerular apparatus             | Juxtaglomerular Apparatus          | UBERON:0003517 | kidney blood vessel                   | Kidney Blood Vessel                | [68](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=68:68) | nan        |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                              | user_slabel                                    | o              | olabel                               | user_olabel                          | row_number                                                                                                               |
|----|------------|-----------------------------------------------------|------------------------------------------------|----------------|--------------------------------------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
|  0 | CL:0000084 | T cell                                              | T Cell                                         | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [82](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=82:82) |
|  1 | CL:0000097 | mast cell                                           | Mast cell                                      | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [88](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=88:88) |
|  2 | CL:0000115 | endothelial cell                                    | Endothelial Cell                               | UBERON:0001986 | endothelium                          | Endothelium (non glomerular)         | [59](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=59:59) |
|  3 | CL:0000236 | B cell                                              | B cell                                         | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [85](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=85:85) |
|  4 | CL:0000576 | monocyte                                            | Monocyte                                       | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [80](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=80:80) |
|  5 | CL:0000623 | natural killer cell                                 | Natural Killer Cell                            | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [75](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=75:75) |
|  6 | CL:0000738 | Leukocyte                                           | nan                                            | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [72](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=72:72) |
|  7 | CL:0000775 | neutrophil                                          | Neutrophil                                     | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [87](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=87:87) |
|  8 | CL:0000786 | plasma cell                                         | Plasma cell                                    | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [86](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=86:86) |
|  9 | CL:0000814 | mature NK T cell                                    | Natural Killer T Cell                          | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [76](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=76:76) |
| 10 | CL:0000815 | regulatory T cell                                   | regulatory T cell                              | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [84](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=84:84) |
| 11 | CL:0000875 | non-classical monocyte                              | non Classical Monocyte                         | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [74](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=74:74) |
| 12 | CL:0000910 | cytotoxic T cell                                    | Cytotoxic T Cell                               | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [83](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=83:83) |
| 13 | CL:0000990 | conventional dendritic cell                         | Dendritic Cell (classical)                     | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [78](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=78:78) |
| 14 | CL:0001056 | dendritic cell, human                               | Dendritic Cell (general)                       | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [77](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=77:77) |
| 15 | CL:0001058 | plasmacytoid dendritic cell, human                  | Dendritic Cell (plasmatoid)                    | UBERON:0005215 | kidney interstitium                  | Interstitium                         | [79](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=79:79) |
| 16 | CL:0002138 | endothelial cell of lymphatic vessel                | Lymphatic Endothelial Cell                     | UBERON:0002042 | lymphatic vessel endothelium         | Endothelium (non glomerular)         | [65](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=65:65) |
| 17 | CL:0002201 | renal beta-intercalated cell                        | Intercalated Cell Type B                       | UBERON:0001232 | collecting duct of renal tubule      | Collecting Duct                      | [57](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=57:57) |
| 18 | CL:0019018 | blood vessel smooth muscle cell                     | Vascular Smooth Muscle Cell                    | UBERON:0003517 | kidney blood vessel                  | Kidney Blood Vessel                  | [67](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=67:67) |
| 19 | CL:1000718 | kidney inner medulla collecting duct principal cell | Inner Medullary Collecting Duct Cell           | UBERON:0009095 | tip of renal papilla                 | papillary tip                        | [19](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=19:19) |
| 20 | CL:1001033 | peritubular capillary endothelial cell              | Peritubular Capillary Endothelial Cell         | UBERON:0012441 | endothelium of peritubular capillary | Endothelium (non glomerular)         | [62](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=62:62) |
| 21 | CL:1001318 | renal interstitial pericyte                         | Vascular Smooth Muscle Cell/Pericyte (general) | UBERON:0003517 | kidney blood vessel                  | Kidney Blood Vessel                  | [66](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=66:66) |
| 22 | CL:4030009 | epithelial cell of proximal tubule segment 1        | Proximal Tubule Epithelial Cell Segment 1      | UBERON:0004196 | proximal convoluted tubule segment 1 | proximal convoluted tubule segment 1 | [27](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=27:27) |
| 23 | CL:4030010 | epithelial cell of proximal tubule segment 2        | Proximal Tubule Epithelial Cell Segment 2      | UBERON:0004197 | proximal convoluted tubule segment 2 | proximal convoluted tubule segment 2 | [28](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=28:28) |
| 24 | CL:4030011 | epithelial cell of proximal tubule segment 3        | Proximal Tubule Cell Epithelial Segment 3      | UBERON:0001290 | proximal straight tubule             | proximal straight tubule segment 3   | [29](https://docs.google.com/spreadsheets/d/1aXnWkwArSRmDnhyq0n_ptISWnmRwXvD4X0BPa9WQfmg/edit#gid=949267305&range=29:29) |




# New CL terms
[**Report**](new_cl_terms_Kidney.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Kidney.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Kidney_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Kidney_AS_has_part_CT_log.tsv)