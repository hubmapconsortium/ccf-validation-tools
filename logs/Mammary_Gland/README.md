
ASCT+B Validation Reports for Mammary_Gland (2023-09-01)
========================================================

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
  
1. In row _[12](https://docs.google.com/spreadsheets/d/1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/edit#gid=928286522&range=12:12)_, no term id was found for the name/label _Basal cell_.

1. In row _[13](https://docs.google.com/spreadsheets/d/1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/edit#gid=928286522&range=13:13)_, no term id was found for the name/label _estrogen receptor negative luminal progenitor cell_.

1. In row _[14](https://docs.google.com/spreadsheets/d/1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/edit#gid=928286522&range=14:14)_, no term id was found for the name/label _mature luminal cell_.

1. In row _[15](https://docs.google.com/spreadsheets/d/1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/edit#gid=928286522&range=15:15)_, no term id was found for the name/label _Endothelial cell 1_.

1. In row _[16](https://docs.google.com/spreadsheets/d/1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/edit#gid=928286522&range=16:16)_, no term id was found for the name/label _Endothelial cell 2_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/edit#gid=928286522&range=17:17)_, no term id was found for the name/label _Adipocyte 1_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/edit#gid=928286522&range=18:18)_, no term id was found for the name/label _Adipocyte 2_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/edit#gid=928286522&range=19:19)_, no term id was found for the name/label _Fibroblast_.

1. In row _[20](https://docs.google.com/spreadsheets/d/1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/edit#gid=928286522&range=20:20)_, no term id was found for the name/label _T-cell_.

1. In row _[21](https://docs.google.com/spreadsheets/d/1Ac7C4dX7eYSMyR75AA2uVY9ZgNGOZZgbqgR8wmp-wdk/edit#gid=928286522&range=21:21)_, no term id was found for the name/label _Macrophage_.


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



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



- No issues found.






# New CL terms
[**Report**](new_cl_terms_Mammary_Gland.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Mammary_Gland.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Mammary_Gland_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Mammary_Gland_AS_has_part_CT_log.tsv)