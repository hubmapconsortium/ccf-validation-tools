
ASCT+B Validation Reports for Knee (2024-07-31)
===============================================

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
  
1. No term id was found for the name/label _Regulatory Chondrocyte 1_ in the following 2 rows _[12](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=12:12)_, _[22](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=22:22)_.

1. No term id was found for the name/label _Regulatory Chondrocyte 2_ in the following 2 rows _[13](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=13:13)_, _[23](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=23:23)_.

1. No term id was found for the name/label _Effector Chondrocyte_ in the following 2 rows _[14](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=14:14)_, _[24](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=24:24)_.

1. No term id was found for the name/label _Prefibrocartilage Chondrocyte_ in the following 2 rows _[15](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=15:15)_, _[25](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=25:25)_.

1. No term id was found for the name/label _Fibrocartilage Chondrocyte 1_ in the following 2 rows _[16](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=16:16)_, _[26](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=26:26)_.

1. No term id was found for the name/label _Fibrocartilage Chondrocyte 2_ in the following 2 rows _[17](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=17:17)_, _[27](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=27:27)_.

1. No term id was found for the name/label _Homeostatic Chodrocyte_ in the following 2 rows _[18](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=18:18)_, _[28](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=28:28)_.

1. No term id was found for the name/label _Reparative Chondrocyte_ in the following 2 rows _[19](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=19:19)_, _[29](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=29:29)_.

1. No term id was found for the name/label _Prehypertrophic Chondrocyte_ in the following 2 rows _[20](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=20:20)_, _[30](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=30:30)_.


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



|    | s                                                               | slabel                       | user_slabel                  | o                                                               | olabel                   | user_olabel     | row_number                                                                                                                |   deltaIC |
|----|-----------------------------------------------------------------|------------------------------|------------------------------|-----------------------------------------------------------------|--------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009984](http://purl.obolibrary.org/obo/UBERON_0009984) | medial condyle of femur  | Medial Condyle  | [12](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=12:12) |   9.14155 |
|  1 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009984](http://purl.obolibrary.org/obo/UBERON_0009984) | medial condyle of femur  | Medial Condyle  | [13](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=13:13) |   9.14155 |
|  2 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009985](http://purl.obolibrary.org/obo/UBERON_0009985) | lateral condyle of femur | Lateral Condyle | [30](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=30:30) |   9.14155 |
|  3 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009985](http://purl.obolibrary.org/obo/UBERON_0009985) | lateral condyle of femur | Lateral Condyle | [29](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=29:29) |   9.14155 |
|  4 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009985](http://purl.obolibrary.org/obo/UBERON_0009985) | lateral condyle of femur | Lateral Condyle | [28](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=28:28) |   9.14155 |
|  5 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009985](http://purl.obolibrary.org/obo/UBERON_0009985) | lateral condyle of femur | Lateral Condyle | [27](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=27:27) |   9.14155 |
|  6 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009985](http://purl.obolibrary.org/obo/UBERON_0009985) | lateral condyle of femur | Lateral Condyle | [26](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=26:26) |   9.14155 |
|  7 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009985](http://purl.obolibrary.org/obo/UBERON_0009985) | lateral condyle of femur | Lateral Condyle | [25](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=25:25) |   9.14155 |
|  8 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009985](http://purl.obolibrary.org/obo/UBERON_0009985) | lateral condyle of femur | Lateral Condyle | [24](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=24:24) |   9.14155 |
|  9 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009985](http://purl.obolibrary.org/obo/UBERON_0009985) | lateral condyle of femur | Lateral Condyle | [23](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=23:23) |   9.14155 |
| 10 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009985](http://purl.obolibrary.org/obo/UBERON_0009985) | lateral condyle of femur | Lateral Condyle | [22](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=22:22) |   9.14155 |
| 11 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009984](http://purl.obolibrary.org/obo/UBERON_0009984) | medial condyle of femur  | Medial Condyle  | [21](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=21:21) |   9.14155 |
| 12 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009984](http://purl.obolibrary.org/obo/UBERON_0009984) | medial condyle of femur  | Medial Condyle  | [20](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=20:20) |   9.14155 |
| 13 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009984](http://purl.obolibrary.org/obo/UBERON_0009984) | medial condyle of femur  | Medial Condyle  | [19](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=19:19) |   9.14155 |
| 14 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009984](http://purl.obolibrary.org/obo/UBERON_0009984) | medial condyle of femur  | Medial Condyle  | [18](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=18:18) |   9.14155 |
| 15 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009984](http://purl.obolibrary.org/obo/UBERON_0009984) | medial condyle of femur  | Medial Condyle  | [17](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=17:17) |   9.14155 |
| 16 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009984](http://purl.obolibrary.org/obo/UBERON_0009984) | medial condyle of femur  | Medial Condyle  | [16](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=16:16) |   9.14155 |
| 17 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009984](http://purl.obolibrary.org/obo/UBERON_0009984) | medial condyle of femur  | Medial Condyle  | [15](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=15:15) |   9.14155 |
| 18 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009984](http://purl.obolibrary.org/obo/UBERON_0009984) | medial condyle of femur  | Medial Condyle  | [14](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=14:14) |   9.14155 |
| 19 | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [UBERON:0009985](http://purl.obolibrary.org/obo/UBERON_0009985) | lateral condyle of femur | Lateral Condyle | [31](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=31:31) |   9.14155 |
| 20 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [12](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=12:12) | nan       |
| 21 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [13](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=13:13) | nan       |
| 22 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [14](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=14:14) | nan       |
| 23 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [15](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=15:15) | nan       |
| 24 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [16](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=16:16) | nan       |
| 25 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [17](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=17:17) | nan       |
| 26 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [18](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=18:18) | nan       |
| 27 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [19](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=19:19) | nan       |
| 28 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [20](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=20:20) | nan       |
| 29 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [21](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=21:21) | nan       |
| 32 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [22](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=22:22) | nan       |
| 33 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [23](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=23:23) | nan       |
| 34 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [24](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=24:24) | nan       |
| 35 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [25](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=25:25) | nan       |
| 36 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [26](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=26:26) | nan       |
| 37 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [27](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=27:27) | nan       |
| 38 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [28](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=28:28) | nan       |
| 39 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [29](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=29:29) | nan       |
| 40 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [30](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=30:30) | nan       |
| 41 | [UBERON:0009980](http://purl.obolibrary.org/obo/UBERON_0009980) | condyle of femur             | Distal Femur                 | [UBERON:0001485](http://purl.obolibrary.org/obo/UBERON_0001485) | Knee Joint               | knee joint      | [31](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=31:31) | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



|    | s                                                       | slabel                   | user_slabel              | o                                                       | olabel                | user_olabel                        | row_number                                                                                                                |   deltaIC |
|----|---------------------------------------------------------|--------------------------|--------------------------|---------------------------------------------------------|-----------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
| 30 | [CL:0000743](http://purl.obolibrary.org/obo/CL_0000743) | hypertrophic chondrocyte | Hypertrophic Chondrocyte | [CL:1001607](http://purl.obolibrary.org/obo/CL_1001607) | articular chondrocyte | articular chondrocyte of the femur | [21](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=21:21) |       nan |
| 42 | [CL:0000743](http://purl.obolibrary.org/obo/CL_0000743) | hypertrophic chondrocyte | Hypertrophic Chondrocyte | [CL:1001607](http://purl.obolibrary.org/obo/CL_1001607) | articular chondrocyte | articular chondrocyte of the femur | [31](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=31:31) |       nan |




## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                   | user_slabel              | o                                                               | olabel                       | user_olabel                  | row_number                                                                                                                |   deltaIC |
|----|---------------------------------------------------------|--------------------------|--------------------------|-----------------------------------------------------------------|------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
| 31 | [CL:0000743](http://purl.obolibrary.org/obo/CL_0000743) | hypertrophic chondrocyte | Hypertrophic Chondrocyte | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [21](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=21:21) |       nan |
| 43 | [CL:0000743](http://purl.obolibrary.org/obo/CL_0000743) | hypertrophic chondrocyte | Hypertrophic Chondrocyte | [UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996) | articular cartilage of joint | Articular Cartilage of femur | [31](https://docs.google.com/spreadsheets/d/15YnWDjFsbuMqStmEjCTA20ZoDzHVEYGh6lqYbeItj6w/edit#gid=1815525900&range=31:31) |       nan |




# New CL terms
[**Report**](new_cl_terms_Knee.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Knee.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Knee_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Knee_AS_has_part_CT_log.tsv)