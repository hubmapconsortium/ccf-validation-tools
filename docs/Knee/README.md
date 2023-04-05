
ASCT+B Validation Reports for Knee (2023-04-05)
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
  
1. In row _[38](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=38:38)_, the term _[CL:0000669](http://purl.obolibrary.org/obo/CL_0000669)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _pericyte cell_ and the one in the **ontology** is _pericyte_. For reference, the given name/label **by SMEs** is _pericyte cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[24](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=24:24)_, the term _[UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _Superior Articular Cartilage_ and the one in the **ontology** is _articular cartilage of joint_. For reference, the given name/label **by SMEs** is _Articular cartilage of a joint_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[12](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=12:12)_, no term id was found for the name/label _proximal tibia_.

1. In row _[13](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=13:13)_, no term id was found for the name/label _proximal fibula_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=24:24)_, no term id was found for the name/label _Superficial Zone_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=25:25)_, no term id was found for the name/label _Transitional Zone_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=25:25)_, no term id was found for the name/label _Deep Superficial_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=26:26)_, no term id was found for the name/label _Rounded Chondrocytes_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=27:27)_, no term id was found for the name/label _Deep Zone_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=28:28)_, no term id was found for the name/label _Tidemark_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=28:28)_, no term id was found for the name/label _Prehypertrophic Chondrocytes_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=30:30)_, no term id was found for the name/label _Subchondral Bone_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=30:30)_, no term id was found for the name/label _Residual Hypertrophic Chondrocytes_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=33:33)_, no term id was found for the name/label _Bone lIning Cells_.

1. In row _[35](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=35:35)_, no term id was found for the name/label _Preosteoclasts_.

1. In row _[37](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=37:37)_, no term id was found for the name/label _vascular endothelial cells_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=38:38)_, no term id was found for the name/label _perivascular cells_.

1. In row _[40](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=40:40)_, no term id was found for the name/label _sinusoidal cells_.

1. In row _[41](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=41:41)_, no term id was found for the name/label _autonomic neuronal cells_.

1. In row _[42](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=42:42)_, no term id was found for the name/label _Marrow Adipocytes_.


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



|    | s              | slabel                              | user_slabel                    | o              | olabel                  | user_olabel     | row_number                                                                                                                |   deltaIC |
|----|----------------|-------------------------------------|--------------------------------|----------------|-------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | UBERON:0001437 | epiphysis                           | Epiphyseal Bone                | UBERON:0009980 | condyle of femur        | Distal Femur    | [30](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=30:30) |  32.2881  |
|  1 | UBERON:0002371 | bone marrow                         | Bone Marrow                    | UBERON:0009980 | condyle of femur        | Distal Femur    | [37](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=37:37) |  29.3013  |
|  2 | UBERON:0002371 | bone marrow                         | Marrow elements                | UBERON:0009980 | condyle of femur        | Distal Femur    | [43](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=43:43) |  29.3013  |
|  6 | UBERON:0002483 | trabecular bone tissue              | trabecular bone                | UBERON:0009980 | condyle of femur        | Distal Femur    | [36](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=36:36) |  10.1448  |
|  7 | UBERON:0010996 | articular cartilage of joint        | Articular cartilage of a joint | UBERON:0009984 | medial condyle of femur | Medial Condyles | [24](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=24:24) |   8.60674 |
| 12 | UBERON:0009989 | condyle of tibia                    | condyle of tibia               | UBERON:0004098 | tibial plateaux         | Tibial Plateau  | [12](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=12:12) |   1.47815 |
| 13 | UBERON:0002446 | patella                             | Patella                        | UBERON:0001485 | knee joint              | knee joint      | [14](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=14:14) |   0.18661 |
| 14 | UBERON:0014848 | tendon of quadriceps femoris        | Patellar Tendon                | UBERON:0001485 | knee joint              | knee joint      | [15](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=15:15) | nan       |
| 15 | UBERON:0000387 | meniscus                            | Meniscus                       | UBERON:0001485 | knee joint              | knee joint      | [17](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=17:17) | nan       |
| 16 | UBERON:0002018 | synovial membrane of synovial joint | Synovial membrane              | UBERON:0001485 | knee joint              | knee joint      | [21](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=21:21) | nan       |
| 17 | UBERON:0003668 | synovial bursa                      | Synovial Bursa                 | UBERON:0001485 | knee joint              | knee joint      | [22](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=22:22) | nan       |
| 18 | UBERON:0016400 | infrapatellar fat pad               | Infrapatellar fat pad          | UBERON:0001485 | knee joint              | knee joint      | [23](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=23:23) | nan       |
| 19 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [24](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=24:24) | nan       |
| 20 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [25](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=25:25) | nan       |
| 22 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [26](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=26:26) | nan       |
| 24 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [27](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=27:27) | nan       |
| 26 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [28](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=28:28) | nan       |
| 28 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [29](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=29:29) | nan       |
| 29 | UBERON:4000088 | mineralized cartilage tissue        | Mineralized Cartilage          | UBERON:0009980 | condyle of femur        | Distal Femur    | [29](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=29:29) | nan       |
| 32 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [30](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=30:30) | nan       |
| 33 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [31](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=31:31) | nan       |
| 35 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [32](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=32:32) | nan       |
| 37 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [33](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=33:33) | nan       |
| 38 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [34](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=34:34) | nan       |
| 40 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [35](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=35:35) | nan       |
| 42 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [36](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=36:36) | nan       |
| 43 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [37](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=37:37) | nan       |
| 44 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [38](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=38:38) | nan       |
| 45 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [39](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=39:39) | nan       |
| 47 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [40](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=40:40) | nan       |
| 49 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [41](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=41:41) | nan       |
| 50 | UBERON:0006136 | unmyelinated nerve fiber            | unmyelinated nerve fiber       | UBERON:0009980 | condyle of femur        | Distal Femur    | [41](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=41:41) | nan       |
| 51 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [42](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=42:42) | nan       |
| 52 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [43](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=43:43) | nan       |
| 53 | UBERON:0009980 | condyle of femur                    | Distal Femur                   | UBERON:0001485 | knee joint              | knee joint      | [44](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=44:44) | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



|    | s          | slabel                   | user_slabel              | o          | olabel                   | user_olabel               | row_number                                                                                                                |   deltaIC |
|----|------------|--------------------------|--------------------------|------------|--------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  8 | CL:1001607 | articular chondrocyte    | articular chondrocyte    | CL:0000744 | columnar chondrocyte     | Columnar Chondrocytes     | [27](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=27:27) |   7.27745 |
| 30 | CL:0000743 | hypertrophic chondrocyte | hypertrophic chondrocyte | CL:0000743 | hypertrophic chondrocyte | Hypertrophic Chondrocytes | [29](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=29:29) | nan       |
| 34 | CL:0000137 | osteocyte                | osteocyte                | CL:0000137 | osteocyte                | Osteocytes                | [31](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=31:31) | nan       |
| 36 | CL:0000062 | osteoblast               | osteoblast               | CL:0000062 | osteoblast               | Osteoblasts               | [32](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=32:32) | nan       |
| 46 | CL:0007010 | preosteoblast            | preosteoblast            | CL:0007010 | preosteoblast            | Preosteoblast             | [39](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=39:39) | nan       |




## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                         | user_slabel                    | o              | olabel                       | user_olabel           | row_number                                                                                                                |
|----|------------|--------------------------------|--------------------------------|----------------|------------------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------|
|  0 | CL:0000062 | osteoblast                     | osteoblast                     | UBERON:0009980 | condyle of femur             | Distal Femur          | [32](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=32:32) |
|  1 | CL:0000136 | fat cell                       | fat cell                       | UBERON:0009980 | condyle of femur             | Distal Femur          | [42](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=42:42) |
|  2 | CL:0000137 | osteocyte                      | osteocyte                      | UBERON:0009980 | condyle of femur             | Distal Femur          | [31](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=31:31) |
|  3 | CL:0000669 | pericyte                       | pericyte cell                  | UBERON:0009980 | condyle of femur             | Distal Femur          | [38](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=38:38) |
|  4 | CL:0000743 | hypertrophic chondrocyte       | hypertrophic chondrocyte       | UBERON:0009980 | condyle of femur             | Distal Femur          | [28](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=28:28) |
|  5 | CL:0000743 | hypertrophic chondrocyte       | hypertrophic chondrocyte       | UBERON:4000088 | mineralized cartilage tissue | Mineralized Cartilage | [29](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=29:29) |
|  6 | CL:0000778 | mononuclear osteoclast         | mononuclear osteoclast         | UBERON:0009980 | condyle of femur             | Distal Femur          | [35](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=35:35) |
|  7 | CL:0000779 | multinuclear osteoclast        | multinuclear osteoclast        | UBERON:0009980 | condyle of femur             | Distal Femur          | [34](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=34:34) |
|  8 | CL:0002262 | endothelial cell of sinusoid   | endothelial cell of sinusoid   | UBERON:0009980 | condyle of femur             | Distal Femur          | [40](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=40:40) |
|  9 | CL:0007010 | preosteoblast                  | preosteoblast                  | UBERON:0009980 | condyle of femur             | Distal Femur          | [39](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=39:39) |
| 10 | CL:1001607 | articular chondrocyte          | articular chondrocyte          | UBERON:0009980 | condyle of femur             | Distal Femur          | [25](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=25:25) |
| 11 | CL:1001607 | articular chondrocyte          | articular chondrocyte          | UBERON:0009980 | condyle of femur             | Distal Femur          | [26](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=26:26) |
| 12 | CL:1001607 | articular chondrocyte          | articular chondrocyte          | UBERON:0009980 | condyle of femur             | Distal Femur          | [27](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=27:27) |
| 13 | CL:2000008 | microvascular endothelial cell | microvascular endothelial cell | UBERON:0007195 | stroma of bone marrow        | Bone Marrow Stroma    | [37](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=37:37) |




# New CL terms
[**Report**](new_cl_terms_Knee.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Knee.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Knee_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Knee_AS_has_part_CT_log.tsv)