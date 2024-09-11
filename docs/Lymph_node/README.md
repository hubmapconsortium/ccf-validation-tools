
ASCT+B Validation Reports for Lymph_node (2024-09-11)
=====================================================

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
  
1. The term _[CL:0000669](http://purl.obolibrary.org/obo/CL_0000669)_ has a different name/label in the source ontology in the following 1 row _[92](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=92:92)_. The name/label in the **ASCT+B table** is _pericyte cell_ and the one in the **ontology** is _pericyte_. For reference, the given name/label **by SMEs** is _Pericyte_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


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



|    | s                                                               | slabel                                | user_slabel               | o                                                               | olabel                          | user_olabel               | row_number                                                                                                                |   deltaIC |
|----|-----------------------------------------------------------------|---------------------------------------|---------------------------|-----------------------------------------------------------------|---------------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  7 | [UBERON:0001473](http://purl.obolibrary.org/obo/UBERON_0001473) | lymphatic vessel                      | Lymphatic Vessels         | [UBERON:0010396](http://purl.obolibrary.org/obo/UBERON_0010396) | afferent lymphatic vessel       | Afferent lymphatic vessel | [18](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=18:18) |  29.6005  |
|  8 | [UBERON:0001473](http://purl.obolibrary.org/obo/UBERON_0001473) | lymphatic vessel                      | Lymphatic Vessels         | [UBERON:0010396](http://purl.obolibrary.org/obo/UBERON_0010396) | afferent lymphatic vessel       | Afferent lymphatic vessel | [19](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=19:19) |  29.6005  |
| 14 | [UBERON:0034729](http://purl.obolibrary.org/obo/UBERON_0034729) | sympathetic nerve                     | Sympathetic nerve         | [UBERON:0035495](http://purl.obolibrary.org/obo/UBERON_0035495) | hilum of lymph node             | Hilum                     | [96](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=96:96) |  24.9394  |
| 37 | [UBERON:0010397](http://purl.obolibrary.org/obo/UBERON_0010397) | efferent lymphatic vessel             | Efferent Lymphatics       | [UBERON:0035495](http://purl.obolibrary.org/obo/UBERON_0035495) | hilum of lymph node             | Hilum                     | [94](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=94:94) |  11.8085  |
| 38 | [UBERON:0010397](http://purl.obolibrary.org/obo/UBERON_0010397) | efferent lymphatic vessel             | Efferent Lymphatics       | [UBERON:0035495](http://purl.obolibrary.org/obo/UBERON_0035495) | hilum of lymph node             | Hilum                     | [95](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=95:95) |  11.8085  |
| 45 | [UBERON:8410034](http://purl.obolibrary.org/obo/UBERON_8410034) | lymph node artery                     | Lymphatic Artery          | [UBERON:0035495](http://purl.obolibrary.org/obo/UBERON_0035495) | hilum of lymph node             | Hilum                     | [97](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=97:97) |   4.56814 |
| 49 | [UBERON:8410042](http://purl.obolibrary.org/obo/UBERON_8410042) | arteriole of lymph node               | Arteriole                 | [UBERON:0002194](http://purl.obolibrary.org/obo/UBERON_0002194) | capsule of lymph node           | Capsule                   | [13](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=13:13) | nan       |
| 50 | [UBERON:8410041](http://purl.obolibrary.org/obo/UBERON_8410041) | venule of lymph node                  | Venule                    | [UBERON:0002194](http://purl.obolibrary.org/obo/UBERON_0002194) | capsule of lymph node           | Capsule                   | [14](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=14:14) | nan       |
| 51 | [UBERON:0002195](http://purl.obolibrary.org/obo/UBERON_0002195) | trabecula of lymph node               | Trabeculae                | [UBERON:0002194](http://purl.obolibrary.org/obo/UBERON_0002194) | capsule of lymph node           | Capsule                   | [15](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=15:15) | nan       |
| 52 | [UBERON:0002195](http://purl.obolibrary.org/obo/UBERON_0002195) | trabecula of lymph node               | Trabeculae                | [UBERON:0002194](http://purl.obolibrary.org/obo/UBERON_0002194) | capsule of lymph node           | Capsule                   | [16](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=16:16) | nan       |
| 53 | [UBERON:8410042](http://purl.obolibrary.org/obo/UBERON_8410042) | arteriole of lymph node               | Arteriole                 | [UBERON:0002195](http://purl.obolibrary.org/obo/UBERON_0002195) | trabecula of lymph node         | Trabeculae                | [16](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=16:16) | nan       |
| 54 | [UBERON:0002195](http://purl.obolibrary.org/obo/UBERON_0002195) | trabecula of lymph node               | Trabeculae                | [UBERON:0002194](http://purl.obolibrary.org/obo/UBERON_0002194) | capsule of lymph node           | Capsule                   | [17](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=17:17) | nan       |
| 55 | [UBERON:8410041](http://purl.obolibrary.org/obo/UBERON_8410041) | venule of lymph node                  | Venule                    | [UBERON:0002195](http://purl.obolibrary.org/obo/UBERON_0002195) | trabecula of lymph node         | Trabeculae                | [17](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=17:17) | nan       |
| 56 | [UBERON:0010396](http://purl.obolibrary.org/obo/UBERON_0010396) | afferent lymphatic vessel             | Afferent lymphatic vessel | [UBERON:0005463](http://purl.obolibrary.org/obo/UBERON_0005463) | subcapsular sinus of lymph node | Subcapsular Sinus         | [18](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=18:18) | nan       |
| 57 | [UBERON:0010396](http://purl.obolibrary.org/obo/UBERON_0010396) | afferent lymphatic vessel             | Afferent lymphatic vessel | [UBERON:0005463](http://purl.obolibrary.org/obo/UBERON_0005463) | subcapsular sinus of lymph node | Subcapsular Sinus         | [19](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=19:19) | nan       |
| 59 | [UBERON:8410071](http://purl.obolibrary.org/obo/UBERON_8410071) | subcapsular sinus ceiling             | Subcapsular sinus ceiling | [UBERON:0005463](http://purl.obolibrary.org/obo/UBERON_0005463) | subcapsular sinus of lymph node | Subcapsular Sinus         | [22](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=22:22) | nan       |
| 60 | [UBERON:8410072](http://purl.obolibrary.org/obo/UBERON_8410072) | subcapsular sinus floor               | Subcapsular sinus floor   | [UBERON:0005463](http://purl.obolibrary.org/obo/UBERON_0005463) | subcapsular sinus of lymph node | Subcapsular Sinus         | [23](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=23:23) | nan       |
| 61 | [UBERON:8410032](http://purl.obolibrary.org/obo/UBERON_8410032) | trabecular sinus of lymph node        | Trabecular sinus          | [UBERON:0005463](http://purl.obolibrary.org/obo/UBERON_0005463) | subcapsular sinus of lymph node | Subcapsular Sinus         | [24](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=24:24) | nan       |
| 63 | [UBERON:8410041](http://purl.obolibrary.org/obo/UBERON_8410041) | venule of lymph node                  | Venule                    | [UBERON:0002006](http://purl.obolibrary.org/obo/UBERON_0002006) | cortex of lymph node            | Cortex                    | [25](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=25:25) | nan       |
| 64 | [UBERON:8410042](http://purl.obolibrary.org/obo/UBERON_8410042) | arteriole of lymph node               | Arteriole                 | [UBERON:0002006](http://purl.obolibrary.org/obo/UBERON_0002006) | cortex of lymph node            | Cortex                    | [26](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=26:26) | nan       |
| 71 | [UBERON:8410042](http://purl.obolibrary.org/obo/UBERON_8410042) | arteriole of lymph node               | Arteriole                 | [UBERON:8410066](http://purl.obolibrary.org/obo/UBERON_8410066) | lymph node paracortex           | Paracortex                | [58](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=58:58) | nan       |
| 72 | [UBERON:0006842](http://purl.obolibrary.org/obo/UBERON_0006842) | lymphatic capillary                   | capillaries of lymph node | [UBERON:8410066](http://purl.obolibrary.org/obo/UBERON_8410066) | lymph node paracortex           | Paracortex                | [59](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=59:59) | nan       |
| 73 | [UBERON:8410038](http://purl.obolibrary.org/obo/UBERON_8410038) | high endothelial venule of lymph node | High Endothelial Venule   | [UBERON:8410066](http://purl.obolibrary.org/obo/UBERON_8410066) | lymph node paracortex           | Paracortex                | [60](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=60:60) | nan       |
| 84 | [UBERON:8410034](http://purl.obolibrary.org/obo/UBERON_8410034) | lymph node artery                     | Lymphatic Artery          | [UBERON:0002007](http://purl.obolibrary.org/obo/UBERON_0002007) | medulla of lymph node           | Medulla                   | [90](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=90:90) | nan       |
| 85 | [UBERON:8410033](http://purl.obolibrary.org/obo/UBERON_8410033) | lymph node vein                       | Hilar Vein                | [UBERON:0002007](http://purl.obolibrary.org/obo/UBERON_0002007) | medulla of lymph node           | Medulla                   | [91](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=91:91) | nan       |
| 86 | [UBERON:8410036](http://purl.obolibrary.org/obo/UBERON_8410036) | medullary venule of lymph node        | Venule                    | [UBERON:8410033](http://purl.obolibrary.org/obo/UBERON_8410033) | lymph node vein                 | Hilar Vein                | [91](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=91:91) | nan       |
| 88 | [UBERON:0005463](http://purl.obolibrary.org/obo/UBERON_0005463) | subcapsular sinus of lymph node       | Subcapsular Sinus         | [UBERON:0002007](http://purl.obolibrary.org/obo/UBERON_0002007) | medulla of lymph node           | Medulla                   | [93](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=93:93) | nan       |
| 92 | [UBERON:8410033](http://purl.obolibrary.org/obo/UBERON_8410033) | lymph node vein                       | Hilar Vein                | [UBERON:0035495](http://purl.obolibrary.org/obo/UBERON_0035495) | hilum of lymph node             | Hilum                     | [98](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=98:98) | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                                               | user_slabel                                   | o                                                               | olabel                                 | user_olabel               | row_number                                                                                                                |   deltaIC |
|----|---------------------------------------------------------|------------------------------------------------------|-----------------------------------------------|-----------------------------------------------------------------|----------------------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | [CL:0000236](http://purl.obolibrary.org/obo/CL_0000236) | B cell                                               | B Cell                                        | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [78](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=78:78) |  44.3446  |
|  1 | [CL:0000071](http://purl.obolibrary.org/obo/CL_0000071) | blood vessel endothelial cell                        | Blood Vessel Endothelial Cell                 | [UBERON:0006842](http://purl.obolibrary.org/obo/UBERON_0006842) | lymphatic capillary                    | capillaries of lymph node | [59](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=59:59) |  35.8679  |
|  2 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                                       | Dendritic Cell                                | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [52](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=52:52) |  35.3641  |
|  3 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                                       | Dendritic Cell                                | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [63](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=63:63) |  35.3641  |
|  4 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                                           | Macrophage                                    | [UBERON:8410074](http://purl.obolibrary.org/obo/UBERON_8410074) | lymph node paracortical sinus          | Paracortical Sinus        | [57](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=57:57) |  35.3022  |
|  5 | [CL:0000623](http://purl.obolibrary.org/obo/CL_0000623) | natural killer cell                                  | Natural Killer Cell                           | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [50](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=50:50) |  30.8573  |
|  6 | [CL:0000623](http://purl.obolibrary.org/obo/CL_0000623) | natural killer cell                                  | Natural Killer Cell                           | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [74](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=74:74) |  30.8573  |
|  9 | [CL:0000798](http://purl.obolibrary.org/obo/CL_0000798) | gamma-delta T cell                                   | Gamma/Delta T cells                           | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [69](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=69:69) |  29.5076  |
| 10 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                            | Mast Cell                                     | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [75](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=75:75) |  28.5414  |
| 11 | [CL:0000786](http://purl.obolibrary.org/obo/CL_0000786) | plasma cell                                          | Plasma Cell                                   | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [76](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=76:76) |  26.2891  |
| 12 | [CL:0000815](http://purl.obolibrary.org/obo/CL_0000815) | regulatory T cell                                    | T Regulatory Cell                             | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [46](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=46:46) |  26.1659  |
| 13 | [CL:0000815](http://purl.obolibrary.org/obo/CL_0000815) | regulatory T cell                                    | T Regulatory Cell                             | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [70](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=70:70) |  26.1659  |
| 15 | [CL:0000909](http://purl.obolibrary.org/obo/CL_0000909) | CD8-positive, alpha-beta memory T cell               | Memory CD8+ T cell                            | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [73](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=73:73) |  23.6169  |
| 16 | [CL:0000909](http://purl.obolibrary.org/obo/CL_0000909) | CD8-positive, alpha-beta memory T cell               | Memory CD8+ T cell                            | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [49](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=49:49) |  23.6169  |
| 17 | [CL:0000897](http://purl.obolibrary.org/obo/CL_0000897) | CD4-positive, alpha-beta memory T cell               | Memory CD4+ T cell                            | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [42](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=42:42) |  23.2402  |
| 18 | [CL:0002138](http://purl.obolibrary.org/obo/CL_0002138) | endothelial cell of lymphatic vessel                 | Lymphatic Endothelial Cell                    | [UBERON:8410074](http://purl.obolibrary.org/obo/UBERON_8410074) | lymph node paracortical sinus          | Paracortical Sinus        | [55](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=55:55) |  23.2402  |
| 19 | [CL:0000897](http://purl.obolibrary.org/obo/CL_0000897) | CD4-positive, alpha-beta memory T cell               | Memory CD4+ T cell                            | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [65](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=65:65) |  23.2402  |
| 20 | [CL:0000980](http://purl.obolibrary.org/obo/CL_0000980) | plasmablast                                          | Plasmablast                                   | [UBERON:8410052](http://purl.obolibrary.org/obo/UBERON_8410052) | lymph node germinal center light zone  | Light Zone                | [36](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=36:36) |  21.3443  |
| 21 | [CL:0000895](http://purl.obolibrary.org/obo/CL_0000895) | naive thymus-derived CD4-positive, alpha-beta T cell | Naive CD4+ T cell                             | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [41](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=41:41) |  20.0647  |
| 22 | [CL:0000895](http://purl.obolibrary.org/obo/CL_0000895) | naive thymus-derived CD4-positive, alpha-beta T cell | Naive CD4+ T cell                             | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [64](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=64:64) |  20.0647  |
| 23 | [CL:0000545](http://purl.obolibrary.org/obo/CL_0000545) | T-helper 1 cell                                      | Th1 cell                                      | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [66](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=66:66) |  19.4051  |
| 24 | [CL:0000545](http://purl.obolibrary.org/obo/CL_0000545) | T-helper 1 cell                                      | Th1 cell                                      | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [43](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=43:43) |  19.4051  |
| 25 | [CL:0000900](http://purl.obolibrary.org/obo/CL_0000900) | naive thymus-derived CD8-positive, alpha-beta T cell | Naive CD8+ T cell                             | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [72](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=72:72) |  19.0488  |
| 26 | [CL:0000900](http://purl.obolibrary.org/obo/CL_0000900) | naive thymus-derived CD8-positive, alpha-beta T cell | Naive CD8+ T cell                             | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [48](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=48:48) |  19.0488  |
| 27 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                                             | Pericyte                                      | [UBERON:8410041](http://purl.obolibrary.org/obo/UBERON_8410041) | venule of lymph node                   | Venule                    | [17](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=17:17) |  18.8254  |
| 28 | [CL:0000546](http://purl.obolibrary.org/obo/CL_0000546) | T-helper 2 cell                                      | Th2 cell                                      | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [67](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=67:67) |  18.2726  |
| 29 | [CL:0000546](http://purl.obolibrary.org/obo/CL_0000546) | T-helper 2 cell                                      | Th2 cell                                      | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [44](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=44:44) |  18.2726  |
| 30 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                                           | Macrophage                                    | [UBERON:0010395](http://purl.obolibrary.org/obo/UBERON_0010395) | lymph node primary follicle            | Primary Follicle          | [30](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=30:30) |  17.9097  |
| 31 | [CL:0000899](http://purl.obolibrary.org/obo/CL_0000899) | T-helper 17 cell                                     | Th17 cell                                     | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [45](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=45:45) |  17.3925  |
| 32 | [CL:0000899](http://purl.obolibrary.org/obo/CL_0000899) | T-helper 17 cell                                     | Th17 cell                                     | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [68](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=68:68) |  17.3925  |
| 33 | [CL:0000787](http://purl.obolibrary.org/obo/CL_0000787) | memory B cell                                        | Memory B Cell                                 | [UBERON:0010420](http://purl.obolibrary.org/obo/UBERON_0010420) | lymph node germinal center mantle zone | Mantle Zone               | [40](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=40:40) |  17.0297  |
| 34 | [CL:0000910](http://purl.obolibrary.org/obo/CL_0000910) | cytotoxic T cell                                     | T Cytotoxic Cell                              | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [71](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=71:71) |  15.8032  |
| 35 | [CL:0000910](http://purl.obolibrary.org/obo/CL_0000910) | cytotoxic T cell                                     | T Cytotoxic Cell                              | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [47](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=47:47) |  15.8032  |
| 36 | [CL:0000442](http://purl.obolibrary.org/obo/CL_0000442) | follicular dendritic cell                            | Follicular Dendritic Cell                     | [UBERON:8410052](http://purl.obolibrary.org/obo/UBERON_8410052) | lymph node germinal center light zone  | Light Zone                | [31](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=31:31) |  13.7044  |
| 39 | [CL:0002038](http://purl.obolibrary.org/obo/CL_0002038) | T follicular helper cell                             | T Follicular Helper Cell                      | [UBERON:8410052](http://purl.obolibrary.org/obo/UBERON_8410052) | lymph node germinal center light zone  | Light Zone                | [33](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=33:33) |  11.8085  |
| 40 | [CL:0000788](http://purl.obolibrary.org/obo/CL_0000788) | naive B cell                                         | Naive B Cell                                  | [UBERON:0010420](http://purl.obolibrary.org/obo/UBERON_0010420) | lymph node germinal center mantle zone | Mantle Zone               | [39](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=39:39) |  10.2688  |
| 41 | [CL:0000787](http://purl.obolibrary.org/obo/CL_0000787) | memory B cell                                        | Memory B Cell                                 | [UBERON:0010395](http://purl.obolibrary.org/obo/UBERON_0010395) | lymph node primary follicle            | Primary Follicle          | [29](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=29:29) |   8.77341 |
| 42 | [CL:0000084](http://purl.obolibrary.org/obo/CL_0000084) | T Cell                                               | T Cell                                        | [UBERON:0009745](http://purl.obolibrary.org/obo/UBERON_0009745) | lymph node medullary cord              | Medullary Cord            | [81](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=81:81) |   8.26409 |
| 43 | [CL:0000084](http://purl.obolibrary.org/obo/CL_0000084) | T Cell                                               | T Cell                                        | [UBERON:0009745](http://purl.obolibrary.org/obo/UBERON_0009745) | lymph node medullary cord              | Medullary Cord            | [82](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=82:82) |   8.26409 |
| 44 | [CL:0000236](http://purl.obolibrary.org/obo/CL_0000236) | B cell                                               | B Cell                                        | [UBERON:0009745](http://purl.obolibrary.org/obo/UBERON_0009745) | lymph node medullary cord              | Medullary Cord            | [85](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=85:85) |   8.22479 |
| 46 | [CL:0000186](http://purl.obolibrary.org/obo/CL_0000186) | myofibroblast cell                                   | Myofibroblast                                 | [UBERON:0002195](http://purl.obolibrary.org/obo/UBERON_0002195) | trabecula of lymph node                | Trabeculae                | [15](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=15:15) |   3.9947  |
| 47 | [CL:0000442](http://purl.obolibrary.org/obo/CL_0000442) | follicular dendritic cell                            | Follicular Dendritic Cell                     | [UBERON:0010395](http://purl.obolibrary.org/obo/UBERON_0010395) | lymph node primary follicle            | Primary Follicle          | [27](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=27:27) |   0.88003 |
| 48 | [CL:0000186](http://purl.obolibrary.org/obo/CL_0000186) | myofibroblast cell                                   | Myofibroblast                                 | [UBERON:0002194](http://purl.obolibrary.org/obo/UBERON_0002194) | capsule of lymph node                  | Capsule                   | [12](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=12:12) | nan       |
| 58 | [CL:0000887](http://purl.obolibrary.org/obo/CL_0000887) | lymph node subcapsular sinus macrophage              | Macrophage                                    | [UBERON:0005463](http://purl.obolibrary.org/obo/UBERON_0005463) | subcapsular sinus of lymph node        | Subcapsular Sinus         | [20](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=20:20) | nan       |
| 62 | [CL:0009109](http://purl.obolibrary.org/obo/CL_0009109) | lymphatic endothelial cell of trabecula              | Lymphatic Endothelial Cell-Trabeculae         | [UBERON:8410032](http://purl.obolibrary.org/obo/UBERON_8410032) | trabecular sinus of lymph node         | Trabecular sinus          | [24](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=24:24) | nan       |
| 65 | [CL:0009113](http://purl.obolibrary.org/obo/CL_0009113) | T follicular regulatory cell                         | T Follicular Regulatory Cell                  | [UBERON:8410052](http://purl.obolibrary.org/obo/UBERON_8410052) | lymph node germinal center light zone  | Light Zone                | [34](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=34:34) | nan       |
| 66 | [CL:0000888](http://purl.obolibrary.org/obo/CL_0000888) | lymph node tingible body macrophage                  | Tingible Body Macrophage                      | [UBERON:8410052](http://purl.obolibrary.org/obo/UBERON_8410052) | lymph node germinal center light zone  | Light Zone                | [35](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=35:35) | nan       |
| 67 | [CL:0009105](http://purl.obolibrary.org/obo/CL_0009105) | T cell zone reticular cell                           | T Cell Zone Reticular Cell                    | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [51](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=51:51) | nan       |
| 68 | [CL:0009113](http://purl.obolibrary.org/obo/CL_0009113) | T follicular regulatory cell                         | T Follicular Regulatory Cell                  | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [53](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=53:53) | nan       |
| 69 | [CL:0002399](http://purl.obolibrary.org/obo/CL_0002399) | CD1c-positive myeloid dendritic cell                 | Conventional Dendritic Cell cDC2              | [UBERON:8410067](http://purl.obolibrary.org/obo/UBERON_8410067) | lymph node interfollicular cortex      | Interfollicular Cortex    | [54](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=54:54) | nan       |
| 70 | [CL:0009105](http://purl.obolibrary.org/obo/CL_0009105) | T cell zone reticular cell                           | T Cell Zone Reticular Cell                    | [UBERON:8410074](http://purl.obolibrary.org/obo/UBERON_8410074) | lymph node paracortical sinus          | Paracortical Sinus        | [56](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=56:56) | nan       |
| 74 | [CL:0001058](http://purl.obolibrary.org/obo/CL_0001058) | plasmacytoid dendritic cell, human                   | Plasmacytoid Dendritic Cell                   | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [61](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=61:61) | nan       |
| 75 | [CL:0002394](http://purl.obolibrary.org/obo/CL_0002394) | CD141-positive myeloid dendritic cell                | Conventional Dendritic Cell cDC1              | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [62](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=62:62) | nan       |
| 76 | [CL:0009114](http://purl.obolibrary.org/obo/CL_0009114) | monocytoid B Cell                                    | Monocytoid B Cell                             | [UBERON:8410075](http://purl.obolibrary.org/obo/UBERON_8410075) | lymph node paracortical cord           | Paracortical Cord         | [77](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=77:77) | nan       |
| 77 | [CL:0009106](http://purl.obolibrary.org/obo/CL_0009106) | medullary reticular cell                             | Medullary Reticular Cell                      | [UBERON:0009745](http://purl.obolibrary.org/obo/UBERON_0009745) | lymph node medullary cord              | Medullary Cord            | [80](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=80:80) | nan       |
| 78 | [CL:0002138](http://purl.obolibrary.org/obo/CL_0002138) | endothelial cell of lymphatic vessel                 | Lymphatic Endothelial Cell                    | [UBERON:0009744](http://purl.obolibrary.org/obo/UBERON_0009744) | lymph node medullary sinus             | Medullary Sinus           | [83](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=83:83) | nan       |
| 79 | [CL:0000786](http://purl.obolibrary.org/obo/CL_0000786) | plasma cell                                          | Plasma Cell                                   | [UBERON:0009745](http://purl.obolibrary.org/obo/UBERON_0009745) | lymph node medullary cord              | Medullary Cord            | [84](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=84:84) | nan       |
| 80 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                                            | Mast Cell                                     | [UBERON:0009745](http://purl.obolibrary.org/obo/UBERON_0009745) | lymph node medullary cord              | Medullary Cord            | [86](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=86:86) | nan       |
| 81 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                                           | Macrophage                                    | [UBERON:0009745](http://purl.obolibrary.org/obo/UBERON_0009745) | lymph node medullary cord              | Medullary Cord            | [87](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=87:87) | nan       |
| 82 | [CL:0000980](http://purl.obolibrary.org/obo/CL_0000980) | plasmablast                                          | Plasmablast                                   | [UBERON:0009745](http://purl.obolibrary.org/obo/UBERON_0009745) | lymph node medullary cord              | Medullary Cord            | [88](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=88:88) | nan       |
| 83 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                                       | Dendritic Cell                                | [UBERON:0009745](http://purl.obolibrary.org/obo/UBERON_0009745) | lymph node medullary cord              | Medullary Cord            | [89](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=89:89) | nan       |
| 87 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                                             | Pericyte                                      | [UBERON:0002007](http://purl.obolibrary.org/obo/UBERON_0002007) | medulla of lymph node                  | Medulla                   | [92](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=92:92) | nan       |
| 89 | [CL:0009110](http://purl.obolibrary.org/obo/CL_0009110) | lymphatic endothelial cell of medulla ceiling        | Lymphatic Endothelial Cell of Medulla Ceiling | [UBERON:0005463](http://purl.obolibrary.org/obo/UBERON_0005463) | subcapsular sinus of lymph node        | Subcapsular Sinus         | [93](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=93:93) | nan       |
| 90 | [CL:0019017](http://purl.obolibrary.org/obo/CL_0019017) | lymphatic vessel smooth muscle cell                  | Smooth Muscle Cell                            | [UBERON:0010397](http://purl.obolibrary.org/obo/UBERON_0010397) | efferent lymphatic vessel              | Efferent Lymphatics       | [95](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=95:95) | nan       |
| 91 | [CL:0011103](http://purl.obolibrary.org/obo/CL_0011103) | sympathetic neuron                                   | Sympathetic Neuron                            | [UBERON:0034729](http://purl.obolibrary.org/obo/UBERON_0034729) | sympathetic nerve                      | Sympathetic nerve         | [96](https://docs.google.com/spreadsheets/d/130Q491MKJWv8eZdEgx8x0ysmVrr1-5MHi_gyUNjTAdc/edit#gid=1223566381&range=96:96) | nan       |




# New CL terms
[**Report**](new_cl_terms_Lymph_node.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Lymph_node.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Lymph_node_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Lymph_node_AS_has_part_CT_log.tsv)