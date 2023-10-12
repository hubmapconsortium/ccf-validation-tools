
ASCT+B Validation Reports for Thymus (2023-10-11)
=================================================

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
  
1. The term _CL:0009082_ has a different name/label in the source ontology in the following 1 row _[31](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=31:31)_. The name/label in the **ASCT+B table** is _committed double negative thymocyte_ and the one in the **ontology** is _committed double negative thymocyte (Homo sapiens)_. For reference, the given name/label **by SMEs** is _double negative thymocyte 3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
- No issues found.


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



|     | s              | slabel                            | user_slabel                       | o              | olabel                           | user_olabel                         | row_number                                                                                                               |   deltaIC |
|-----|----------------|-----------------------------------|-----------------------------------|----------------|----------------------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
|   0 | UBERON:0002384 | connective tissue                 | connective tissue                 | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [12](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=12:12) |       inf |
|   2 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [14](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=14:14) |       inf |
|   3 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [15](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=15:15) |       inf |
|   4 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [16](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=16:16) |       inf |
|   5 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [18](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=18:18) |       inf |
|   6 | UBERON:0001013 | adipose tissue                    | adipose tissue                    | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [19](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=19:19) |       inf |
|   8 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [22](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=22:22) |       inf |
|   9 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [24](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=24:24) |       inf |
|  12 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [34](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=34:34) |       inf |
|  13 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [36](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=36:36) |       inf |
|  15 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [16](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=16:16) |       nan |
|  16 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [17](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=17:17) |       nan |
|  17 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [17](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=17:17) |       nan |
|  18 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [18](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=18:18) |       nan |
|  20 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [19](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=19:19) |       nan |
|  21 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [20](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=20:20) |       nan |
|  22 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [21](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=21:21) |       nan |
|  23 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [22](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=22:22) |       nan |
|  24 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [23](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=23:23) |       nan |
|  25 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [23](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=23:23) |       nan |
|  26 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [24](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=24:24) |       nan |
|  28 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [25](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=25:25) |       nan |
|  29 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [26](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=26:26) |       nan |
|  31 | UBERON:0004791 | thymus trabecula                  | thymus trabecula                  | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [27](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=27:27) |       nan |
|  32 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [28](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=28:28) |       nan |
|  33 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [29](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=29:29) |       nan |
|  35 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [30](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=30:30) |       nan |
|  37 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [31](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=31:31) |       nan |
|  39 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [32](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=32:32) |       nan |
|  41 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [33](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=33:33) |       nan |
|  43 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [34](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=34:34) |       nan |
|  44 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [35](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=35:35) |       nan |
|  45 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [35](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=35:35) |       nan |
|  46 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [36](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=36:36) |       nan |
|  48 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [37](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=37:37) |       nan |
|  50 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [38](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=38:38) |       nan |
|  52 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [39](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=39:39) |       nan |
|  54 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [40](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=40:40) |       nan |
|  55 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [40](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=40:40) |       nan |
|  56 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [41](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=41:41) |       nan |
|  57 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [41](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=41:41) |       nan |
|  58 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [42](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=42:42) |       nan |
|  59 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [42](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=42:42) |       nan |
|  61 | UBERON:0002123 | cortex of thymus                  | cortex of thymus                  | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [43](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=43:43) |       nan |
|  62 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [43](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=43:43) |       nan |
|  72 | UBERON:8410062 | parasympathetic cholinergic nerve | parasympathetic cholinergic nerve | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [53](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=53:53) |       nan |
|  73 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [54](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=54:54) |       nan |
|  74 | UBERON:0001591 | thymic vein                       | thymic vein                       | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [55](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=55:55) |       nan |
|  79 | UBERON:8410062 | parasympathetic cholinergic nerve | parasympathetic cholinergic nerve | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [60](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=60:60) |       nan |
|  80 | UBERON:0018243 | thymic artery                     | thymic artery                     | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [61](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=61:61) |       nan |
|  81 | UBERON:0001591 | thymic vein                       | thymic vein                       | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [62](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=62:62) |       nan |
|  83 | UBERON:0010397 | efferent lymphatic vessel         | efferent lymphatic                | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [64](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=64:64) |       nan |
|  85 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [66](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=66:66) |       nan |
|  87 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [67](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=67:67) |       nan |
|  89 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [68](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=68:68) |       nan |
|  91 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [69](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=69:69) |       nan |
|  93 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [70](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=70:70) |       nan |
|  95 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [71](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=71:71) |       nan |
|  96 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [72](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=72:72) |       nan |
|  97 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [73](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=73:73) |       nan |
|  99 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [74](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=74:74) |       nan |
| 101 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [75](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=75:75) |       nan |
| 103 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [76](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=76:76) |       nan |
| 105 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [77](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=77:77) |       nan |
| 107 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [78](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=78:78) |       nan |
| 109 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [79](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=79:79) |       nan |
| 111 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [80](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=80:80) |       nan |
| 113 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [81](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=81:81) |       nan |
| 115 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [82](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=82:82) |       nan |
| 116 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [83](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=83:83) |       nan |
| 118 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [84](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=84:84) |       nan |
| 120 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [85](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=85:85) |       nan |
| 122 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [86](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=86:86) |       nan |
| 124 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [87](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=87:87) |       nan |
| 125 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [87](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=87:87) |       nan |
| 126 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [88](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=88:88) |       nan |
| 127 | UBERON:0001591 | thymic vein                       | thymic vein                       | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [88](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=88:88) |       nan |
| 128 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [89](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=89:89) |       nan |
| 129 | UBERON:0001021 | nerve                             | nerve                             | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [89](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=89:89) |       nan |
| 131 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [90](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=90:90) |       nan |
| 132 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [90](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=90:90) |       nan |
| 133 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [91](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=91:91) |       nan |
| 134 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [91](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=91:91) |       nan |
| 135 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [92](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=92:92) |       nan |
| 136 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [92](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=92:92) |       nan |
| 137 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [93](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=93:93) |       nan |
| 138 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [93](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=93:93) |       nan |
| 140 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [94](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=94:94) |       nan |
| 141 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [94](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=94:94) |       nan |
| 142 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [95](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=95:95) |       nan |
| 143 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [95](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=95:95) |       nan |
| 144 | UBERON:0002124 | medulla of thymus                 | medulla of thymus                 | UBERON:0002125 | thymus lobule                    | thymus lobule                       | [96](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=96:96) |       nan |
| 145 | UBERON:0003846 | thymus epithelium                 | thymus epithelium                 | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [96](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=96:96) |       nan |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|     | s          | slabel                                               | user_slabel                             | o              | olabel                           | user_olabel                         | row_number                                                                                                               |   deltaIC |
|-----|------------|------------------------------------------------------|-----------------------------------------|----------------|----------------------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
|   1 | CL:0000866 | thymic macrophage                                    | macrophage                              | UBERON:0002122 | capsule of thymus                | capsule of thymus                   | [13](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=13:13) |       inf |
|   7 | CL:0000866 | thymic macrophage                                    | macrophage                              | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [20](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=20:20) |       inf |
|  10 | CL:0000764 | erythroid lineage cell                               | erythroid                               | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [25](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=25:25) |       inf |
|  11 | CL:0000771 | eosinophil                                           | eosinophil                              | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [27](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=27:27) |       inf |
|  14 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [15](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=15:15) |       nan |
|  19 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [18](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=18:18) |       nan |
|  27 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [24](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=24:24) |       nan |
|  30 | CL:0000097 | mast cell                                            | mast cell                               | UBERON:0004791 | thymus trabecula                 | thymus trabecula                    | [26](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=26:26) |       nan |
|  34 | CL:0002425 | early T lineage precursor                            | early thymic progenitor                 | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [29](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=29:29) |       nan |
|  36 | CL:0009081 | specified double negative thymocyte (Homo sapiens)   | double negative thymocyte 2             | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [30](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=30:30) |       nan |
|  38 | CL:0009082 | committed double negative thymocyte (Homo sapiens)   | double negative thymocyte 3             | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [31](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=31:31) |       nan |
|  40 | CL:0009083 | rearranging double negative thymocyte (Homo sapiens) | double negative thymocyte 4             | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [32](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=32:32) |       nan |
|  42 | CL:0000883 | thymic cortical macrophage                           | macrophage                              | UBERON:0006936 | thymus subcapsular epithelium    | thymus subcapsular epithelium       | [33](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=33:33) |       nan |
|  47 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [36](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=36:36) |       nan |
|  49 | CL:0000809 | double-positive, alpha-beta thymocyte                | double positive thymocyte               | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [37](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=37:37) |       nan |
|  51 | CL:0000942 | thymic plasmacytoid dendritic cell                   | plasmacytoid dendritic cell             | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [38](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=38:38) |       nan |
|  53 | CL:0000764 | erythroid lineage cell                               | erythroid                               | UBERON:0002123 | cortex of thymus                 | cortex of thymus                    | [39](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=39:39) |       nan |
|  60 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [42](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=42:42) |       nan |
|  63 | CL:0000970 | unswitched memory B cell                             | memory B cell                           | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [44](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=44:44) |       nan |
|  64 | CL:0000972 | class switched memory B cell                         | memory B cell                           | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [45](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=45:45) |       nan |
|  65 | CL:0000980 | plasmablast                                          | plasmablast                             | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [46](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=46:46) |       nan |
|  66 | CL:0000786 | plasma cell                                          | plasma cell                             | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [47](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=47:47) |       nan |
|  67 | CL:0000771 | eosinophil                                           | eosinophil                              | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [48](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=48:48) |       nan |
|  68 | CL:0000576 | monocyte                                             | monocyte                                | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [49](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=49:49) |       nan |
|  69 | CL:0002436 | mature CD4 single-positive thymocyte                 | CD4+ T single positive thymocyte        | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [50](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=50:50) |       nan |
|  70 | CL:0002437 | mature CD8 single-positive thymocyte                 | CD8+ T single positive thymocyte        | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [51](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=51:51) |       nan |
|  71 | CL:0001070 | beige adipocyte                                      | beige adipocyte                         | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [52](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=52:52) |       nan |
|  75 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [56](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=56:56) |       nan |
|  76 | CL:0000866 | thymic macrophage                                    | macrophage                              | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [57](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=57:57) |       nan |
|  77 | CL:0002059 | CD8alpha-positive thymic conventional dendritic cell | conventional dendritic cell 1           | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [58](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=58:58) |       nan |
|  78 | CL:0002460 | CD8alpha-negative thymic conventional dendritic cell | conventional dendritic cell 2           | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [59](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=59:59) |       nan |
|  82 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0003988 | thymus corticomedullary boundary | corticomedullary boundary of thymus | [63](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=63:63) |       nan |
|  84 | CL:0002138 | endothelial cell of lymphatic vessel                 | lymphatic endothelial cell              | UBERON:0010397 | efferent lymphatic vessel        | efferent lymphatic                  | [64](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=64:64) |       nan |
|  86 | CL:0002436 | mature CD4 single-positive thymocyte                 | CD4+ T single positive thymocyte        | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [66](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=66:66) |       nan |
|  88 | CL:0000934 | CD4-positive, alpha-beta cytotoxic T cell            | cytotoxic CD4 T cell                    | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [67](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=67:67) |       nan |
|  90 | CL:0000897 | CD4-positive, alpha-beta memory T cell               | CD4+ T memory T cell                    | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [68](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=68:68) |       nan |
|  92 | CL:0002437 | mature CD8 single-positive thymocyte                 | CD8+ T single positive thymocyte        | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [69](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=69:69) |       nan |
|  94 | CL:0000909 | CD8-positive, alpha-beta memory T cell               | CD8+ T memory                           | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [70](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=70:70) |       nan |
|  98 | CL:0002038 | T follicular helper cell                             | T follicular helper cell                | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [73](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=73:73) |       nan |
| 100 | CL:0002677 | naive regulatory T cell                              | regulatory T cells                      | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [74](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=74:74) |       nan |
| 102 | CL:0000798 | gamma-delta T cell                                   | gamma-delta T cell                      | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [75](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=75:75) |       nan |
| 104 | CL:0000899 | T-helper 17 cell                                     | Th17 cell                               | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [76](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=76:76) |       nan |
| 106 | CL:0000940 | mucosal invariant T cell                             | mucosal associated invariant T cell     | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [77](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=77:77) |       nan |
| 108 | CL:0000914 | immature NK T cell                                   | immature NKT cell                       | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [78](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=78:78) |       nan |
| 110 | CL:0002059 | CD8alpha-positive thymic conventional dendritic cell | conventional dendritic cell 1           | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [79](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=79:79) |       nan |
| 112 | CL:0002460 | CD8alpha-negative thymic conventional dendritic cell | conventional dendritic cell 2           | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [80](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=80:80) |       nan |
| 114 | CL:0000942 | thymic plasmacytoid dendritic cell                   | plasmacytoid dendritic cell             | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [81](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=81:81) |       nan |
| 117 | CL:0000788 | naive B cell                                         | naive B cell                            | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [83](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=83:83) |       nan |
| 119 | CL:0001078 | group 3 innate lymphoid cell, human                  | group 3 innate lymphoid cell            | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [84](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=84:84) |       nan |
| 121 | CL:0000623 | natural killer cell                                  | natural killer cell                     | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [85](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=85:85) |       nan |
| 123 | CL:0000771 | eosinophil                                           | eosinophil                              | UBERON:0002124 | medulla of thymus                | medulla of thymus                   | [86](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=86:86) |       nan |
| 130 | CL:3000002 | sympathetic noradrenergic neuron                     | sympathetic noradrenergic nerve         | UBERON:0001021 | nerve                            | nerve                               | [89](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=89:89) |       nan |
| 139 | CL:0009073 | medullary thymic epithelial cell type 3              | medullary thymic epithelial cell type 3 | UBERON:0003987 | Hassall's corpuscle              | Hassall's corpuscle                 | [93](https://docs.google.com/spreadsheets/d/1tbHMjOi7wPXnq3TFp74N2kPKtiJ_pFSgz5u5CZOGGrc/edit#gid=863370556&range=93:93) |       nan |




# New CL terms
[**Report**](new_cl_terms_Thymus.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Thymus.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Thymus_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Thymus_AS_has_part_CT_log.tsv)