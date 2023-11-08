
ASCT+B Validation Reports for Liver (2023-11-08)
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


These are the reports related to issues in the terms found in the ASCT+B table. We validate only [CL](https://www.ebi.ac.uk/ols/ontologies/cl), [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) and [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) terms.
## Terms not found


This report provides a list of terms not found neither in UBERON nor in CL. Please remove these terms from the ASCT+B table - disconsider this message if a term was recently added to the ontology.  
  

## Typos or punctuation mistakes


This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.  
  
- No issues found.


## Different labels


This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.

If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.

If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.  
  
1. The term _CL:0000909_ has a different name/label in the source ontology in the following 1 row _[36](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=36:36)_. The name/label in the **ASCT+B table** is _CD8-positive, alpha-beta memory T cell _ and the one in the **ontology** is _CD8-positive, alpha-beta memory T cell_. For reference, the given name/label **by SMEs** is _CD8-positive, alpha-beta memory T cell _. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
1. No term id was found for the name/label _Liver immune resident component_ in the following 13 rows _[32](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=32:32)_, _[33](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=33:33)_, _[34](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=34:34)_, _[35](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=35:35)_, _[36](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=36:36)_, _[37](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=37:37)_, _[38](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=38:38)_, _[39](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=39:39)_, _[40](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=40:40)_, _[41](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=41:41)_, _[42](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=42:42)_, _[43](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=43:43)_, _[44](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=44:44)_.

1. No term id was found for the name/label _CD8 TRm (residence memory)_ in the following 1 row _[36](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=36:36)_.

1. No term id was found for the name/label _Eomes low Liver NK cell_ in the following 1 row _[41](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=41:41)_.

1. No term id was found for the name/label _TBet low Liver NK cell_ in the following 1 row _[42](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=42:42)_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
- No issues found.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Same case for Anatomic Ontology for Human Lung Maturation (LMHA) and Interlex IDs (ILX) from Stimulating Peripheral Activity to Relieve Conditions (SPARC). You can request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
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



|    | s              | slabel              | user_slabel        | o              | olabel       | user_olabel        | row_number                                                                                                                |   deltaIC |
|----|----------------|---------------------|--------------------|----------------|--------------|--------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  2 | UBERON:0001021 | nerve               | nerve              | UBERON:0001279 | portal triad | portal triad/tract | [24](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=24:24) |   36.0333 |
|  3 | UBERON:0005169 | interstitial tissue | interstitial       | UBERON:0001279 | portal triad | portal triad/tract | [27](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=27:27) |   14.1911 |
|  4 | UBERON:0001473 | lymphatic vessel    | lymphatic vessel   | UBERON:0004647 | liver lobule | hepatic Lobule     | [30](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=30:30) |   11.5469 |
| 15 | UBERON:0005452 | hepatic cord        | hepatic plate      | UBERON:0004647 | liver lobule | hepatic Lobule     | [16](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=16:16) |  nan      |
| 16 | UBERON:0005452 | hepatic cord        | hepatic plate      | UBERON:0004647 | liver lobule | hepatic Lobule     | [17](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=17:17) |  nan      |
| 18 | UBERON:0005452 | hepatic cord        | hepatic plate      | UBERON:0004647 | liver lobule | hepatic Lobule     | [18](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=18:18) |  nan      |
| 20 | UBERON:0005452 | hepatic cord        | hepatic plate      | UBERON:0004647 | liver lobule | hepatic Lobule     | [19](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=19:19) |  nan      |
| 22 | UBERON:0001279 | portal triad        | portal triad/tract | UBERON:0004647 | liver lobule | hepatic Lobule     | [21](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=21:21) |  nan      |
| 23 | UBERON:0004058 | biliary ductule     | bile duct/ule      | UBERON:0001279 | portal triad | portal triad/tract | [21](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=21:21) |  nan      |
| 25 | UBERON:0001279 | portal triad        | portal triad/tract | UBERON:0004647 | liver lobule | hepatic Lobule     | [22](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=22:22) |  nan      |
| 26 | UBERON:0004058 | biliary ductule     | bile duct/ule      | UBERON:0001279 | portal triad | portal triad/tract | [22](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=22:22) |  nan      |
| 27 | UBERON:0001279 | portal triad        | portal triad/tract | UBERON:0004647 | liver lobule | hepatic Lobule     | [23](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=23:23) |  nan      |
| 29 | UBERON:0001279 | portal triad        | portal triad/tract | UBERON:0004647 | liver lobule | hepatic Lobule     | [24](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=24:24) |  nan      |
| 31 | UBERON:0001279 | portal triad        | portal triad/tract | UBERON:0004647 | liver lobule | hepatic Lobule     | [25](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=25:25) |  nan      |
| 32 | UBERON:0001279 | portal triad        | portal triad/tract | UBERON:0004647 | liver lobule | hepatic Lobule     | [26](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=26:26) |  nan      |
| 33 | UBERON:0001279 | portal triad        | portal triad/tract | UBERON:0004647 | liver lobule | hepatic Lobule     | [27](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=27:27) |  nan      |
| 37 | UBERON:0016478 | liver stroma        | stroma             | UBERON:0004647 | liver lobule | hepatic Lobule     | [31](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=31:31) |  nan      |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                                  | user_slabel                                                        | o              | olabel                     | user_olabel      | row_number                                                                                                                |    deltaIC |
|----|------------|---------------------------------------------------------|--------------------------------------------------------------------|----------------|----------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------|------------|
|  0 | CL:0000738 | leukocyte                                               | leukocyte                                                          | UBERON:0006729 | liver perisinusoidal space | Disse's space    | [15](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=15:15) |  40.3009   |
|  1 | CL:0000075 | columnar/cuboidal epithelial cell                       | columnar cell (larger cholangiocytes are more columnar) has ciliae | UBERON:0004058 | biliary ductule            | bile duct/ule    | [22](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=22:22) |  36.1832   |
|  5 | CL:0019018 | blood vessel smooth muscle cell                         | smooth muscle cell                                                 | UBERON:0001193 | hepatic artery             | hepatic artery   | [26](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=26:26) |   8.89174  |
|  6 | CL:0000624 | CD4-positive, alpha-beta T cell                         | CD4+T cell                                                         | UBERON:0004647 | liver lobule               | hepatic Lobule   | [37](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=37:37) |   6.94153  |
|  7 | CL:0000990 | conventional dendritic cell                             | Conventional DC 1                                                  | UBERON:0004647 | liver lobule               | hepatic Lobule   | [33](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=33:33) |   4.74487  |
|  8 | CL:0002543 | vein endothelial cell                                   | endothelial cell                                                   | UBERON:0006841 | central vein of liver      | central vein     | [20](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=20:20) |   3.80729  |
|  9 | CL:0000623 | natural killer cell                                     | natural killer cell                                                | UBERON:0004647 | liver lobule               | hepatic Lobule   | [41](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=41:41) |   3.54883  |
| 10 | CL:0000623 | natural killer cell                                     | natural killer cell                                                | UBERON:0004647 | liver lobule               | hepatic Lobule   | [42](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=42:42) |   3.54883  |
| 11 | CL:0000623 | Natural killer Cell                                     | NK                                                                 | UBERON:0004647 | liver lobule               | hepatic Lobule   | [43](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=43:43) |   3.54883  |
| 12 | CL:1000413 | endothelial cell of artery                              | endothelial cell                                                   | UBERON:0001193 | hepatic artery             | hepatic artery   | [25](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=25:25) |   3.38023  |
| 13 | CL:0000798 | gamma-delta T cell                                      | gamma delta T cell                                                 | UBERON:0004647 | liver lobule               | hepatic Lobule   | [38](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=38:38) |   2.24173  |
| 14 | CL:0000632 | hepatic stellate cell                                   | quiescent hepatic stellate cell                                    | UBERON:0006729 | liver perisinusoidal space | Disse's space    | [14](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=14:14) |   0.883602 |
| 17 | CL:0019026 | periportal region hepatocyte                            | periportal hepatocyte                                              | UBERON:0005452 | hepatic cord               | hepatic plate    | [17](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=17:17) | nan        |
| 19 | CL:0019029 | centrilobular region hepatocyte                         | pericentral hepatocyte                                             | UBERON:0005452 | hepatic cord               | hepatic plate    | [18](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=18:18) | nan        |
| 21 | CL:0019028 | midzonal region hepatocyte                              | mid zone hepatocyte                                                | UBERON:0005452 | hepatic cord               | hepatic plate    | [19](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=19:19) | nan        |
| 24 | CL:0000241 | stratified cuboidal epithelial cell                     | cuboidal cell (Small cholangiocytes are cuboidal)                  | UBERON:0004058 | biliary ductule            | bile duct/ule    | [21](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=21:21) | nan        |
| 28 | CL:0002543 | vein endothelial cell                                   | endothelial cell                                                   | UBERON:0002017 | portal vein                | portal vein      | [23](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=23:23) | nan        |
| 30 | CL:0000526 | afferent neuron                                         | neuron cell                                                        | UBERON:0001021 | nerve                      | nerve            | [24](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=24:24) | nan        |
| 34 | CL:0009100 | hepatic portal fibroblast                               | portal fibroblast                                                  | UBERON:0005169 | interstitial tissue        | interstitial     | [27](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=27:27) | nan        |
| 35 | CL:0002196 | Hepatic oval stem cell                                  | hepatic oval cell                                                  | UBERON:0001282 | intralobular bile duct     | Canals of Hering | [28](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=28:28) | nan        |
| 36 | CL:0002196 | Hepatic oval stem cell                                  | hepatic progenitor cell                                            | UBERON:0001282 | intralobular bile duct     | Canals of Hering | [29](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=29:29) | nan        |
| 38 | CL:0001056 | dendritic cell, human                                   | conventional Dendritic cell                                        | UBERON:0004647 | liver lobule               | hepatic Lobule   | [32](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=32:32) | nan        |
| 39 | CL:0002399 | CD1c-positive myeloid dendritic cell                    | Conventional DC 2                                                  | UBERON:0004647 | liver lobule               | hepatic Lobule   | [34](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=34:34) | nan        |
| 40 | CL:0000784 | plasmacytoid dendritic cell                             | plasmacytoid Dendritic cell                                        | UBERON:0004647 | liver lobule               | hepatic Lobule   | [35](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=35:35) | nan        |
| 41 | CL:0000909 | CD8-positive, alpha-beta memory T cell                  | CD8-positive, alpha-beta memory T cell                             | UBERON:0004647 | liver lobule               | hepatic Lobule   | [36](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=36:36) | nan        |
| 42 | CL:0001203 | CD8-positive, alpha-beta memory T cell, CD45RO-positive | CD8+ Liver-Resident Memory T cell                                  | UBERON:0004647 | liver lobule               | hepatic Lobule   | [39](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=39:39) | nan        |
| 43 | CL:0000921 | Type I NK T cell                                        | iNKT                                                               | UBERON:0004647 | liver lobule               | hepatic Lobule   | [40](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=40:40) | nan        |




# New CL terms
[**Report**](new_cl_terms_Liver.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Liver.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Liver_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Liver_AS_has_part_CT_log.tsv)