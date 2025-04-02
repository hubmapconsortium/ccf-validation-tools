
ASCT+B Validation Reports for Prostate (2025-04-02)
===================================================

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
  
1. It might have a typo in the term _NEED_ in the following 1 row _[26](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=26:26)_. The term id should have this pattern: UBERON:NNNNNNN or CL:NNNNNNN or PCL:NNNNNNN. The ontology name in upper case. N is a number, and it should have exactly 7 numbers after the colon. Please change it in the ASCT+B table.


## Different labels


This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.

If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.

If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.  
  
1. The term _[CL:0005006](http://purl.obolibrary.org/obo/CL_0005006)_ has a different name/label in the source ontology in the following 1 row _[15](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=15:15)_. The name/label in the **ASCT+B table** is _ionocyte _ and the one in the **ontology** is _ionocyte_. For reference, the given name/label **by SMEs** is _ionocyte_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols4/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
1. No term id was found for the name/label _ionocyte epithelia_ in the following 1 row _[15](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=15:15)_.

1. No term id was found for the name/label _glia_ in the following 1 row _[25](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=25:25)_.

1. No term id was found for the name/label _stroma_ in the following 1 row _[26](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=26:26)_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
1. The term _endoneurial fibroblast_ without ontology ID has no parent that is from the CL ontology in the following 1 row _[26](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=26:26)_.


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



|    | s                                                               | slabel                                             | user_slabel               | o                                                               | olabel                    | user_olabel               | row_number                                                                                                                |   deltaIC |
|----|-----------------------------------------------------------------|----------------------------------------------------|---------------------------|-----------------------------------------------------------------|---------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | [UBERON:0000010](http://purl.obolibrary.org/obo/UBERON_0000010) | peripheral nervous system                          | peripheral nervous system | [UBERON:0002367](http://purl.obolibrary.org/obo/UBERON_0002367) | prostate gland            | prostate gland            | [25](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=25:25) |   20.2635 |
|  1 | [UBERON:0000010](http://purl.obolibrary.org/obo/UBERON_0000010) | peripheral nervous system                          | peripheral nervous system | [UBERON:0002367](http://purl.obolibrary.org/obo/UBERON_0002367) | prostate gland            | prostate gland            | [26](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=26:26) |   20.2635 |
|  2 | [UBERON:0007798](http://purl.obolibrary.org/obo/UBERON_0007798) | vascular system                                    | vascular system           | [UBERON:0002367](http://purl.obolibrary.org/obo/UBERON_0002367) | prostate gland            | prostate gland            | [23](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=23:23) |   20.2533 |
|  3 | [UBERON:0007798](http://purl.obolibrary.org/obo/UBERON_0007798) | vascular system                                    | vascular system           | [UBERON:0002367](http://purl.obolibrary.org/obo/UBERON_0002367) | prostate gland            | prostate gland            | [24](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=24:24) |   20.2533 |
|  4 | [UBERON:0004537](http://purl.obolibrary.org/obo/UBERON_0004537) | blood vasculature                                  | vascular system           | [UBERON:0002367](http://purl.obolibrary.org/obo/UBERON_0002367) | prostate gland            | prostate gland            | [19](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=19:19) |   17.7939 |
|  5 | [UBERON:0004537](http://purl.obolibrary.org/obo/UBERON_0004537) | blood vasculature                                  | vascular system           | [UBERON:0002367](http://purl.obolibrary.org/obo/UBERON_0002367) | prostate gland            | prostate gland            | [20](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=20:20) |   17.7939 |
|  6 | [UBERON:0004537](http://purl.obolibrary.org/obo/UBERON_0004537) | blood vasculature                                  | vascular system           | [UBERON:0002367](http://purl.obolibrary.org/obo/UBERON_0002367) | prostate gland            | prostate gland            | [21](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=21:21) |   17.7939 |
|  9 | [UBERON:0004243](http://purl.obolibrary.org/obo/UBERON_0004243) | prostate gland smooth muscle                       | Prostate Glandular Acinus | [UBERON:0004184](http://purl.obolibrary.org/obo/UBERON_0004184) | prostate gland stroma     | prostate stroma           | [16](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=16:16) |  nan      |
| 10 | [UBERON:0015131](http://purl.obolibrary.org/obo/UBERON_0015131) | subepithelial connective tissue of prostatic gland | Prostate Glandular Acinus | [UBERON:0004184](http://purl.obolibrary.org/obo/UBERON_0004184) | prostate gland stroma     | prostate stroma           | [17](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=17:17) |  nan      |
| 12 | [UBERON:0015131](http://purl.obolibrary.org/obo/UBERON_0015131) | subepithelial connective tissue of prostatic gland | Prostate Glandular Acinus | [UBERON:0004184](http://purl.obolibrary.org/obo/UBERON_0004184) | prostate gland stroma     | prostate stroma           | [18](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=18:18) |  nan      |
| 14 | [UBERON:0004536](http://purl.obolibrary.org/obo/UBERON_0004536) | lymph vasculature                                  | lymph vasculature         | [UBERON:0002367](http://purl.obolibrary.org/obo/UBERON_0002367) | prostate gland            | prostate gland            | [22](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=22:22) |  nan      |
| 16 | [UBERON:0000010](http://purl.obolibrary.org/obo/UBERON_0000010) | peripheral nervous system                          | peripheral nervous system | [UBERON:0000010](http://purl.obolibrary.org/obo/UBERON_0000010) | peripheral nervous system | peripheral nervous system | [25](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=25:25) |  nan      |
| 17 | [UBERON:0000010](http://purl.obolibrary.org/obo/UBERON_0000010) | peripheral nervous system                          | peripheral nervous system | [UBERON:0000010](http://purl.obolibrary.org/obo/UBERON_0000010) | peripheral nervous system | peripheral nervous system | [26](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=26:26) |  nan      |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                                                           | user_slabel              | o                                                               | olabel                                             | user_olabel               | row_number                                                                                                                |   deltaIC |
|----|---------------------------------------------------------|------------------------------------------------------------------|--------------------------|-----------------------------------------------------------------|----------------------------------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  7 | [CL:0005006](http://purl.obolibrary.org/obo/CL_0005006) | ionocyte                                                         | ionocyte                 | [UBERON:0004179](http://purl.obolibrary.org/obo/UBERON_0004179) | Prostate Glandular Acinus                          | Prostate Glandular Acinus | [15](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=15:15) |   1.01446 |
|  8 | [CL:0017002](http://purl.obolibrary.org/obo/CL_0017002) | prostate neuroendocrine cell                                     | neuroendocrine epithelia | [UBERON:0004179](http://purl.obolibrary.org/obo/UBERON_0004179) | Prostate Glandular Acinus                          | Prostate Glandular Acinus | [14](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=14:14) | nan       |
| 11 | [CL:1000301](http://purl.obolibrary.org/obo/CL_1000301) | fibroblast of subepithelial connective tissue of prostatic gland | periprostatic fibroblast | [UBERON:0015131](http://purl.obolibrary.org/obo/UBERON_0015131) | subepithelial connective tissue of prostatic gland | Prostate Glandular Acinus | [17](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=17:17) | nan       |
| 13 | [CL:1000299](http://purl.obolibrary.org/obo/CL_1000299) | fibroblast of connective tissue of prostate                      | interstitial fibroblast  | [UBERON:0015131](http://purl.obolibrary.org/obo/UBERON_0015131) | subepithelial connective tissue of prostatic gland | Prostate Glandular Acinus | [18](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=18:18) | nan       |
| 15 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                                                         | perictye                 | [UBERON:0001981](http://purl.obolibrary.org/obo/UBERON_0001981) | blood vessel                                       | blood vessel              | [24](https://docs.google.com/spreadsheets/d/1jR_UpAkyn-cXNQXjpTBOWv1CTw1Z_5yi_UDoUMIHavw/edit#gid=1239199370&range=24:24) | nan       |




# New CL terms
[**Report**](new_cl_terms_Prostate.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Prostate.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Prostate_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Prostate_AS_has_part_CT_log.tsv)