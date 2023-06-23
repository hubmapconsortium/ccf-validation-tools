
ASCT+B Validation Reports for Thymus (2023-06-19)
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
  
1. In row _[30](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=30:30)_, the term _[CL:0009081](http://purl.obolibrary.org/obo/CL_0009081)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _specified double negative thymocyte_ and the one in the **ontology** is _specified double negative thymocyte (Homo sapiens)_. For reference, the given name/label **by SMEs** is _double negative thymocyte 2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[31](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=31:31)_, the term _[CL:0009082](http://purl.obolibrary.org/obo/CL_0009082)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _committed double negative thymocyte_ and the one in the **ontology** is _committed double negative thymocyte (Homo sapiens)_. For reference, the given name/label **by SMEs** is _double negative thymocyte 3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[78](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=78:78)_, the term _[CL:0000914](http://purl.obolibrary.org/obo/CL_0000914)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _immature NKT cell_ and the one in the **ontology** is _immature NK T cell_. For reference, the given name/label **by SMEs** is _immature NKT cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[32](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=32:32)_, the term _[CL:0009083](http://purl.obolibrary.org/obo/CL_0009083)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _rearranging double negative thymocyte_ and the one in the **ontology** is _rearranging double negative thymocyte (Homo sapiens)_. For reference, the given name/label **by SMEs** is _double negative thymocyte 4_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
- No issues found.


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



|     | s              | slabel                            | user_slabel                       | o              | olabel                           | user_olabel                         | row_number                                                                                                               |    deltaIC |
|-----|----------------|-----------------------------------|-----------------------------------|----------------|----------------------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------|------------|
|   0 | UBERON:0002384 | connective tissue                 | connective tissue                 | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [21](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=21:21) |  50.9862   |
|   1 | UBERON:0002384 | connective tissue                 | connective tissue                 | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [12](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=12:12) |  46.3948   |
|   2 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [16](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=16:16) |  43.8863   |
|   3 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [18](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=18:18) |  43.8863   |
|   4 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [36](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=36:36) |  43.8863   |
|   5 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [22](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=22:22) |  43.8863   |
|   6 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [24](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=24:24) |  43.8863   |
|   7 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [34](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=34:34) |  43.8863   |
|   8 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [14](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=14:14) |  39.295    |
|   9 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [15](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=15:15) |  39.295    |
|  10 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [42](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=42:42) |  32.9023   |
|  11 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [40](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=40:40) |  32.9023   |
|  13 | UBERON:0001013 | adipose tissue                    | adipose tissue                    | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [19](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=19:19) |  31.0449   |
|  14 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [87](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=87:87) |  30.3225   |
|  15 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [89](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=89:89) |  30.3225   |
|  33 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [78](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=78:78) |   1.69529  |
|  34 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [77](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=77:77) |   1.69529  |
|  35 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [80](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=80:80) |   1.69529  |
|  36 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [81](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=81:81) |   1.69529  |
|  37 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [82](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=82:82) |   1.69529  |
|  38 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [83](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=83:83) |   1.69529  |
|  39 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [84](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=84:84) |   1.69529  |
|  40 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [85](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=85:85) |   1.69529  |
|  41 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [86](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=86:86) |   1.69529  |
|  42 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [87](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=87:87) |   1.69529  |
|  43 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [88](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=88:88) |   1.69529  |
|  44 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [89](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=89:89) |   1.69529  |
|  45 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [90](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=90:90) |   1.69529  |
|  46 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [91](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=91:91) |   1.69529  |
|  47 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [92](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=92:92) |   1.69529  |
|  48 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [93](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=93:93) |   1.69529  |
|  49 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [94](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=94:94) |   1.69529  |
|  50 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [95](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=95:95) |   1.69529  |
|  51 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [79](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=79:79) |   1.69529  |
|  52 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [96](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=96:96) |   1.69529  |
|  53 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [76](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=76:76) |   1.69529  |
|  54 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [68](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=68:68) |   1.69529  |
|  55 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [75](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=75:75) |   1.69529  |
|  56 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [74](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=74:74) |   1.69529  |
|  57 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [73](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=73:73) |   1.69529  |
|  58 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [72](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=72:72) |   1.69529  |
|  59 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [71](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=71:71) |   1.69529  |
|  60 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [70](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=70:70) |   1.69529  |
|  61 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [69](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=69:69) |   1.69529  |
|  62 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [66](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=66:66) |   1.69529  |
|  63 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [67](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=67:67) |   1.69529  |
|  64 | UBERON:0010397 | efferent lymphatic vessel         | efferent lymphatic                | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [64](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=64:64) |   1.20769  |
|  65 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [43](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=43:43) |   1.15491  |
|  68 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [29](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=29:29) |   0.270403 |
|  69 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [28](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=28:28) |   0.270403 |
|  70 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [32](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=32:32) |   0.270403 |
|  71 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [30](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=30:30) |   0.270403 |
|  72 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [36](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=36:36) |   0.270403 |
|  73 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [35](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=35:35) |   0.270403 |
|  74 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [34](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=34:34) |   0.270403 |
|  75 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [31](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=31:31) |   0.270403 |
|  76 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [33](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=33:33) |   0.270403 |
|  79 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [16](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=16:16) | nan        |
|  80 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [17](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=17:17) | nan        |
|  81 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [17](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=17:17) | nan        |
|  82 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [18](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=18:18) | nan        |
|  84 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [19](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=19:19) | nan        |
|  85 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [20](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=20:20) | nan        |
|  87 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [21](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=21:21) | nan        |
|  88 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [22](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=22:22) | nan        |
|  89 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [23](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=23:23) | nan        |
|  90 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [23](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=23:23) | nan        |
|  91 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [24](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=24:24) | nan        |
|  93 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [25](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=25:25) | nan        |
|  94 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [26](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=26:26) | nan        |
|  95 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [27](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=27:27) | nan        |
| 100 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [35](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=35:35) | nan        |
| 102 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [37](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=37:37) | nan        |
| 103 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [38](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=38:38) | nan        |
| 105 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [39](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=39:39) | nan        |
| 106 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [40](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=40:40) | nan        |
| 107 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [41](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=41:41) | nan        |
| 108 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [41](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=41:41) | nan        |
| 109 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [42](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=42:42) | nan        |
| 111 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [43](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=43:43) | nan        |
| 113 | UBERON:8410062 | parasympathetic cholinergic nerve | parasympathetic cholinergic nerve | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [53](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=53:53) | nan        |
| 114 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [54](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=54:54) | nan        |
| 115 | UBERON:0001591 | thymic vein                       | thymic vein                       | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [55](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=55:55) | nan        |
| 120 | UBERON:8410062 | parasympathetic cholinergic nerve | parasympathetic cholinergic nerve | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [60](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=60:60) | nan        |
| 121 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [61](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=61:61) | nan        |
| 122 | UBERON:0001591 | thymic vein                       | thymic vein                       | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [62](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=62:62) | nan        |
| 137 | UBERON:0001591 | thymic vein                       | thymic vein                       | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [88](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=88:88) | nan        |
| 139 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [90](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=90:90) | nan        |
| 140 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [91](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=91:91) | nan        |
| 141 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [92](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=92:92) | nan        |
| 142 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [93](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=93:93) | nan        |
| 144 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [94](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=94:94) | nan        |
| 145 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [95](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=95:95) | nan        |
| 146 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [96](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=96:96) | nan        |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                               | user_slabel                             | o              | olabel                           | user_olabel                         | row_number                                                                                                               |
|----|------------|------------------------------------------------------|-----------------------------------------|----------------|----------------------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
|  0 | CL:0000071 | blood vessel endothelial cell                        | blood endothelial cell                  | UBERON:0018243 | thymic artery                    | thymic artery                       | [41](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=41:41) |
|  1 | CL:0000071 | blood vessel endothelial cell                        | blood endothelial cell                  | UBERON:0018243 | thymic artery                    | thymic artery                       | [35](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=35:35) |
|  2 | CL:0000071 | blood vessel endothelial cell                        | blood endothelial cell                  | UBERON:0001591 | thymic vein                      | thymic vein                         | [62](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=62:62) |
|  3 | CL:0000071 | blood vessel endothelial cell                        | blood endothelial cell                  | UBERON:0018243 | thymic artery                    | thymic artery                       | [54](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=54:54) |
|  4 | CL:0000071 | blood vessel endothelial cell                        | blood endothelial cell                  | UBERON:0018243 | thymic artery                    | thymic artery                       | [23](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=23:23) |
|  5 | CL:0000071 | blood vessel endothelial cell                        | blood endothelial cell                  | UBERON:0018243 | thymic artery                    | thymic artery                       | [61](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=61:61) |
|  6 | CL:0000071 | blood vessel endothelial cell                        | blood endothelial cell                  | UBERON:0018243 | thymic artery                    | thymic artery                       | [17](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=17:17) |
|  7 | CL:0000071 | blood vessel endothelial cell                        | blood endothelial cell                  | UBERON:0001591 | thymic vein                      | thymic vein                         | [88](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=88:88) |
|  8 | CL:0000071 | blood vessel endothelial cell                        | blood endothelial cell                  | UBERON:0001591 | thymic vein                      | thymic vein                         | [55](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=55:55) |
|  9 | CL:0000097 | mast cell                                            | mast cell                               | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [26](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=26:26) |
| 10 | CL:0000576 | monocyte                                             | monocyte                                | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [49](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=49:49) |
| 11 | CL:0000623 | natural killer cell                                  | natural killer cell                     | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [85](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=85:85) |
| 12 | CL:0000764 | erythroid lineage cell                               | erythroid                               | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [25](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=25:25) |
| 13 | CL:0000764 | erythroid lineage cell                               | erythroid                               | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [39](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=39:39) |
| 14 | CL:0000771 | eosinophil                                           | eosinophil                              | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [27](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=27:27) |
| 15 | CL:0000771 | eosinophil                                           | eosinophil                              | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [86](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=86:86) |
| 16 | CL:0000771 | eosinophil                                           | eosinophil                              | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [48](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=48:48) |
| 17 | CL:0000786 | plasma cell                                          | plasma cell                             | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [47](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=47:47) |
| 18 | CL:0000788 | naive B cell                                         | naive B cell                            | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [83](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=83:83) |
| 19 | CL:0000798 | gamma-delta T cell                                   | gamma-delta T cell                      | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [75](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=75:75) |
| 20 | CL:0000809 | double-positive, alpha-beta thymocyte                | double positive thymocyte               | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [37](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=37:37) |
| 21 | CL:0000866 | thymic macrophage                                    | macrophage                              | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [13](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=13:13) |
| 22 | CL:0000866 | thymic macrophage                                    | macrophage                              | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [20](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=20:20) |
| 23 | CL:0000866 | thymic macrophage                                    | macrophage                              | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [57](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=57:57) |
| 24 | CL:0000883 | thymic cortical macrophage                           | macrophage                              | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [33](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=33:33) |
| 25 | CL:0000897 | CD4-positive, alpha-beta memory T cell               | CD4+ T memory T cell                    | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [68](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=68:68) |
| 26 | CL:0000899 | T-helper 17 cell                                     | Th17 cell                               | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [76](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=76:76) |
| 27 | CL:0000909 | CD8-positive, alpha-beta memory T cell               | CD8+ T memory                           | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [70](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=70:70) |
| 28 | CL:0000914 | immature NK T cell                                   | immature NKT cell                       | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [78](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=78:78) |
| 29 | CL:0000934 | CD4-positive, alpha-beta cytotoxic T cell            | cytotoxic CD4 T cell                    | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [67](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=67:67) |
| 30 | CL:0000940 | mucosal invariant T cell                             | mucosal associated invariant T cell     | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [77](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=77:77) |
| 31 | CL:0000942 | thymic plasmacytoid dendritic cell                   | plasmacytoid dendritic cell             | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [81](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=81:81) |
| 32 | CL:0000942 | thymic plasmacytoid dendritic cell                   | plasmacytoid dendritic cell             | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [38](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=38:38) |
| 33 | CL:0000970 | unswitched memory B cell                             | memory B cell                           | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [44](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=44:44) |
| 34 | CL:0000972 | class switched memory B cell                         | memory B cell                           | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [45](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=45:45) |
| 35 | CL:0000980 | plasmablast                                          | plasmablast                             | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [46](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=46:46) |
| 36 | CL:0001070 | beige adipocyte                                      | beige adipocyte                         | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [52](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=52:52) |
| 37 | CL:0001078 | group 3 innate lymphoid cell, human                  | group 3 innate lymphoid cell            | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [84](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=84:84) |
| 38 | CL:0002038 | T follicular helper cell                             | T follicular helper cell                | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [73](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=73:73) |
| 39 | CL:0002059 | CD8alpha-positive thymic conventional dendritic cell | conventional dendritic cell 1           | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [58](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=58:58) |
| 40 | CL:0002059 | CD8alpha-positive thymic conventional dendritic cell | conventional dendritic cell 1           | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [79](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=79:79) |
| 41 | CL:0002138 | endothelial cell of lymphatic vessel                 | lymphatic endothelial cell              | UBERON:0010397 | efferent lymphatic vessel        | efferent lymphatic                  | [64](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=64:64) |
| 42 | CL:0002364 | cortical thymic epithelial cell                      | cortical thymic epithelial cell         | UBERON:0003846 | thymus epithelium                | thymus epithelium                   | [43](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=43:43) |
| 43 | CL:0002425 | early T lineage precursor                            | early thymic progenitor                 | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [29](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=29:29) |
| 44 | CL:0002436 | mature CD4 single-positive thymocyte                 | CD4+ T single positive thymocyte        | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [66](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=66:66) |
| 45 | CL:0002436 | mature CD4 single-positive thymocyte                 | CD4+ T single positive thymocyte        | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [50](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=50:50) |
| 46 | CL:0002437 | mature CD8 single-positive thymocyte                 | CD8+ T single positive thymocyte        | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [51](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=51:51) |
| 47 | CL:0002437 | mature CD8 single-positive thymocyte                 | CD8+ T single positive thymocyte        | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [69](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=69:69) |
| 48 | CL:0002460 | CD8alpha-negative thymic conventional dendritic cell | conventional dendritic cell 2           | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [59](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=59:59) |
| 49 | CL:0002460 | CD8alpha-negative thymic conventional dendritic cell | conventional dendritic cell 2           | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [80](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=80:80) |
| 50 | CL:0002677 | naive regulatory T cell                              | regulatory T cells                      | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [74](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=74:74) |
| 51 | CL:0009073 | medullary thymic epithelial cell type 3              | medullary thymic epithelial cell type 3 | UBERON:0003987 | Hassall's corpuscle              | Hassall's corpuscle                 | [93](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=93:93) |
| 52 | CL:0009081 | specified double negative thymocyte (Homo sapiens)   | double negative thymocyte 2             | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [30](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=30:30) |
| 53 | CL:0009082 | committed double negative thymocyte (Homo sapiens)   | double negative thymocyte 3             | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [31](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=31:31) |
| 54 | CL:0009083 | rearranging double negative thymocyte (Homo sapiens) | double negative thymocyte 4             | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [32](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=32:32) |
| 55 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [36](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=36:36) |
| 56 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [63](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=63:63) |
| 57 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [89](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=89:89) |
| 58 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [56](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=56:56) |
| 59 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [24](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=24:24) |
| 60 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [18](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=18:18) |
| 61 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [15](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=15:15) |
| 62 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [42](https://docs.google.com/spreadsheets/d/13VmRAofv85ZapJgmtHAVO67ICY4nK1FOugkTKV8_eoM/edit#gid=863370556&range=42:42) |




# New CL terms
[**Report**](new_cl_terms_Thymus.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Thymus.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Thymus_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Thymus_AS_has_part_CT_log.tsv)