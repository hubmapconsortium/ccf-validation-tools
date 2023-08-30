
ASCT+B Validation Reports for Knee (2023-08-30)
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
  
1. In row _[13](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=13:13)_, the term _[UBERON:0008772](http://purl.obolibrary.org/obo/UBERON_0008772)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _Proximal Epiphysis of the Tibia_ and the one in the **ontology** is _proximal epiphysis of tibia_. For reference, the given name/label **by SMEs** is _Proximal Epiphysis of the Tibia_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[23](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=23:23)_, the term _[UBERON:0011088](http://purl.obolibrary.org/obo/UBERON_0011088)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _Tibial collageral ligament_ and the one in the **ontology** is _ligament of knee joint_. For reference, the given name/label **by SMEs** is _Tibial collageral ligament_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[12](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=12:12)_, the term _[UBERON:0004406](http://purl.obolibrary.org/obo/UBERON_0004406)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _Distal Epiphysis of the Femur_ and the one in the **ontology** is _distal epiphysis of femur_. For reference, the given name/label **by SMEs** is _Distal Epiphysis of the Femur_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[28](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=28:28)_, the term _[UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _Articular cartilage of a joint_ and the one in the **ontology** is _articular cartilage of joint_. For reference, the given name/label **by SMEs** is _Articular cartilage of a joint_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[27](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=27:27)_, the term _[UBERON:0003680](http://purl.obolibrary.org/obo/UBERON_0003680)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _Posterior cruciate ligament of the knee_ and the one in the **ontology** is _posterior cruciate ligament of knee joint_. For reference, the given name/label **by SMEs** is _Posterior cruciate ligament_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[14](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=14:14)_, the term _[UBERON:0008775](http://purl.obolibrary.org/obo/UBERON_0008775)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _Proximal Epiphysis of the Fibula_ and the one in the **ontology** is _proximal epiphysis of fibula_. For reference, the given name/label **by SMEs** is _Proximal Epiphysis of the Fibula_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[17](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=17:17)_, the term _[UBERON:0007617](http://purl.obolibrary.org/obo/UBERON_0007617)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _Space encapsulated by the synovial membrane_ and the one in the **ontology** is _synovial cavity of joint_. For reference, the given name/label **by SMEs** is _Synovial Cavity_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[26](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=26:26)_, the term _[UBERON:0003671](http://purl.obolibrary.org/obo/UBERON_0003671)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _Anterior cruciate ligament of the knee_ and the one in the **ontology** is _anterior cruciate ligament of knee joint_. For reference, the given name/label **by SMEs** is _Anterior cruciate ligament_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[28](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=28:28)_, no term id was found for the name/label _superficial zone cell of articular cartilage_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=29:29)_, no term id was found for the name/label _transition zone cell of the articular cartilage_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=30:30)_, no term id was found for the name/label _middle zone cell of articular cartilage_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=31:31)_, no term id was found for the name/label _deep zone cell of articular cartilage_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=32:32)_, no term id was found for the name/label _subchondral bone cell of articular cartilage_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[15](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=15:15)_, the term _FMA:321690_ is from another ontology that is not validated in this process.

1. In row _[25](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=25:25)_, the term _FMA:9660_ is from another ontology that is not validated in this process.


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



|    | s              | slabel                              | user_slabel                      | o              | olabel     | user_olabel   | row_number                                                                                                                |       deltaIC |
|----|----------------|-------------------------------------|----------------------------------|----------------|------------|---------------|---------------------------------------------------------------------------------------------------------------------------|---------------|
|  0 | UBERON:0008772 | proximal epiphysis of tibia         | Proximal Epiphysis of the Tibia  | UBERON:0000387 | meniscus   | Meniscus      | [33](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=33:33) | 100           |
|  1 | UBERON:0010996 | articular cartilage of joint        | Articular cartilage of a joint   | UBERON:0001485 | Knee Joint | knee joint    | [28](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=28:28) |   0.0135579   |
|  2 | UBERON:0010996 | articular cartilage of joint        | Articular cartilage of a joint   | UBERON:0001485 | Knee Joint | knee joint    | [29](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=29:29) |   0.0135579   |
|  3 | UBERON:0010996 | articular cartilage of joint        | Articular cartilage of a joint   | UBERON:0001485 | Knee Joint | knee joint    | [30](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=30:30) |   0.0135579   |
|  4 | UBERON:0010996 | articular cartilage of joint        | Articular cartilage of a joint   | UBERON:0001485 | Knee Joint | knee joint    | [31](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=31:31) |   0.0135579   |
|  5 | UBERON:0010996 | articular cartilage of joint        | Articular cartilage of a joint   | UBERON:0001485 | Knee Joint | knee joint    | [32](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=32:32) |   0.0135579   |
|  6 | UBERON:0008775 | proximal epiphysis of fibula        | Proximal Epiphysis of the Fibula | UBERON:0001485 | Knee Joint | knee joint    | [14](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=14:14) |   1.30881e-15 |
|  7 | UBERON:0007617 | synovial cavity of joint            | Synovial Cavity                  | UBERON:0001485 | Knee Joint | knee joint    | [17](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=17:17) |   1.30881e-15 |
|  8 | UBERON:0002018 | synovial membrane of synovial joint | Synovial membrane                | UBERON:0001485 | Knee Joint | knee joint    | [16](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=16:16) |   1.19766e-21 |
|  9 | UBERON:0014848 | tendon of quadriceps femoris        | Patellar Tendon                  | UBERON:0001485 | Knee Joint | knee joint    | [18](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=18:18) |   1.19766e-21 |
| 10 | UBERON:0002446 | patella                             | Patella                          | UBERON:0001485 | Knee Joint | knee joint    | [19](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=19:19) |   1.19766e-21 |
| 11 | UBERON:0003668 | synovial bursa                      | Synovial Bursa                   | UBERON:0001485 | Knee Joint | knee joint    | [22](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=22:22) |   1.19766e-21 |
| 12 | UBERON:0008772 | proximal epiphysis of tibia         | Proximal Epiphysis of the Tibia  | UBERON:0001485 | Knee Joint | knee joint    | [13](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=13:13) |   1.19766e-21 |
| 13 | UBERON:0004406 | distal epiphysis of femur           | Distal Epiphysis of the Femur    | UBERON:0001485 | Knee Joint | knee joint    | [12](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=12:12) |   1.19617e-21 |
| 14 | UBERON:0016400 | infrapatellar fat pad               | Infrapatellar fat pad            | UBERON:0001485 | Knee Joint | knee joint    | [21](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=21:21) | nan           |
| 15 | UBERON:0000387 | meniscus                            | Meniscus                         | UBERON:0001485 | Knee Joint | knee joint    | [33](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=33:33) | nan           |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.








# New CL terms
[**Report**](new_cl_terms_Knee.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Knee.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Knee_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Knee_AS_has_part_CT_log.tsv)