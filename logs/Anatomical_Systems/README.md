
ASCT+B Validation Reports for Anatomical_Systems (2023-09-01)
=============================================================

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
  
1. In row _[12](https://docs.google.com/spreadsheets/d/1oB3m_IOMEcDsdQoDicXd9KXXz7oytIPIPiu9lq88quU/edit#gid=2028977062&range=12:12)_, the term _[UBERON:0000467](http://purl.obolibrary.org/obo/UBERON_0000467)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _circulatory system_ and the one in the **ontology** is _anatomical system_. For reference, the given name/label **by SMEs** is _circulatory system_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[18](https://docs.google.com/spreadsheets/d/1oB3m_IOMEcDsdQoDicXd9KXXz7oytIPIPiu9lq88quU/edit#gid=2028977062&range=18:18)_, no term id was found for the name/label _liver_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1oB3m_IOMEcDsdQoDicXd9KXXz7oytIPIPiu9lq88quU/edit#gid=2028977062&range=36:36)_, no term id was found for the name/label _upper respiratory system_.

1. In row _[37](https://docs.google.com/spreadsheets/d/1oB3m_IOMEcDsdQoDicXd9KXXz7oytIPIPiu9lq88quU/edit#gid=2028977062&range=37:37)_, no term id was found for the name/label _lower respiratory system_.


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



|    | s              | slabel        | user_slabel   | o              | olabel            | user_olabel       | row_number                                                                                                                |   deltaIC |
|----|----------------|---------------|---------------|----------------|-------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | UBERON:0002405 | immune system | immune system | UBERON:0000467 | anatomical system | anatomical system | [24](https://docs.google.com/spreadsheets/d/1oB3m_IOMEcDsdQoDicXd9KXXz7oytIPIPiu9lq88quU/edit#gid=2028977062&range=24:24) |       nan |
|  1 | UBERON:0002405 | immune system | immune system | UBERON:0000467 | anatomical system | anatomical system | [25](https://docs.google.com/spreadsheets/d/1oB3m_IOMEcDsdQoDicXd9KXXz7oytIPIPiu9lq88quU/edit#gid=2028977062&range=25:25) |       nan |
|  2 | UBERON:0002405 | immune system | immune system | UBERON:0000467 | anatomical system | anatomical system | [26](https://docs.google.com/spreadsheets/d/1oB3m_IOMEcDsdQoDicXd9KXXz7oytIPIPiu9lq88quU/edit#gid=2028977062&range=26:26) |       nan |
|  3 | UBERON:0002405 | immune system | immune system | UBERON:0000467 | anatomical system | anatomical system | [27](https://docs.google.com/spreadsheets/d/1oB3m_IOMEcDsdQoDicXd9KXXz7oytIPIPiu9lq88quU/edit#gid=2028977062&range=27:27) |       nan |
|  4 | UBERON:0002405 | immune system | immune system | UBERON:0000467 | anatomical system | anatomical system | [28](https://docs.google.com/spreadsheets/d/1oB3m_IOMEcDsdQoDicXd9KXXz7oytIPIPiu9lq88quU/edit#gid=2028977062&range=28:28) |       nan |
|  5 | UBERON:0002405 | immune system | immune system | UBERON:0000467 | anatomical system | anatomical system | [29](https://docs.google.com/spreadsheets/d/1oB3m_IOMEcDsdQoDicXd9KXXz7oytIPIPiu9lq88quU/edit#gid=2028977062&range=29:29) |       nan |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



- No issues found.






# New CL terms
[**Report**](new_cl_terms_Anatomical_Systems.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Anatomical_Systems.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Anatomical_Systems_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Anatomical_Systems_AS_has_part_CT_log.tsv)