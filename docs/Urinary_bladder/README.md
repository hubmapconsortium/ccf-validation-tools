
ASCT+B Validation Reports for Urinary_bladder (2024-04-10)
==========================================================

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
  
1. The term _[CL:0000186](http://purl.obolibrary.org/obo/CL_0000186)_ has a different name/label in the source ontology in the following 1 row _[16](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=16:16)_. The name/label in the **ASCT+B table** is _myofibroblast_ and the one in the **ontology** is _myofibroblast cell_. For reference, the given name/label **by SMEs** is _myofibroblast_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols4/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
1. No term id was found for the name/label _basal cell of bladder urothelium_ in the following 1 row _[12](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=12:12)_.

1. No term id was found for the name/label _intermediate cell of bladder urothelium_ in the following 1 row _[13](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=13:13)_.

1. No term id was found for the name/label _superficial cell of bladder urothelium_ in the following 1 row _[14](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=14:14)_.

1. No term id was found for the name/label _detrusor smooth muscle cell of bladder_ in the following 1 row _[15](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=15:15)_.

1. No term id was found for the name/label _myofibroblast cell of bladder_ in the following 1 row _[16](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=16:16)_.

1. No term id was found for the name/label _fibroblast of urinary bladder_ in the following 2 rows _[17](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=17:17)_, _[18](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=18:18)_.

1. No term id was found for the name/label _PI16+ fibroblast cell of bladder_ in the following 1 row _[17](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=17:17)_.

1. No term id was found for the name/label _DPT+ fibroblast cell of bladder_ in the following 1 row _[18](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=18:18)_.

1. No term id was found for the name/label _lipofibroblast cell of bladder_ in the following 2 rows _[19](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=19:19)_, _[39](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=39:39)_.

1. No term id was found for the name/label _endothelial cell of bladder_ in the following 1 row _[20](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=20:20)_.

1. No term id was found for the name/label _vascular smooth muscle cell of urinary bladder_ in the following 2 rows _[21](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=21:21)_, _[40](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=40:40)_.

1. No term id was found for the name/label _pericyte cell of urinary bladder_ in the following 2 rows _[22](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=22:22)_, _[41](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=41:41)_.

1. No term id was found for the name/label _superficial epithelial cell of urinary bladder_ in the following 1 row _[29](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=29:29)_.

1. No term id was found for the name/label _basal epithelia_ in the following 1 row _[30](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=30:30)_.

1. No term id was found for the name/label _intermediate epithelia_ in the following 1 row _[31](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=31:31)_.

1. No term id was found for the name/label _urinary bladder stroma_ in the following 14 rows _[32](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=32:32)_, _[33](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=33:33)_, _[34](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=34:34)_, _[35](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=35:35)_, _[36](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=36:36)_, _[37](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=37:37)_, _[38](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=38:38)_, _[39](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=39:39)_, _[40](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=40:40)_, _[41](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=41:41)_, _[42](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=42:42)_, _[43](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=43:43)_, _[44](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=44:44)_, _[45](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=45:45)_.

1. No term id was found for the name/label _fibroblast cell of urinary bladder_ in the following 2 rows _[33](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=33:33)_, _[35](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=35:35)_.

1. No term id was found for the name/label _CXCL14 fibroblast_ in the following 1 row _[33](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=33:33)_.

1. No term id was found for the name/label _urinary bladder interstitial fibroblast_ in the following 2 rows _[34](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=34:34)_, _[37](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=37:37)_.

1. No term id was found for the name/label _minor interstitial fibroblast_ in the following 1 row _[34](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=34:34)_.

1. No term id was found for the name/label _periurothelial fibroblast_ in the following 1 row _[35](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=35:35)_.

1. No term id was found for the name/label _myofibroblast cell of urinary bladder_ in the following 1 row _[36](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=36:36)_.

1. No term id was found for the name/label _major interstitial fibroblast_ in the following 1 row _[37](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=37:37)_.

1. No term id was found for the name/label _neruofibroblast of urinary bladder_ in the following 1 row _[38](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=38:38)_.

1. No term id was found for the name/label _vascular arterial endothelial cell of urinary bladder_ in the following 1 row _[42](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=42:42)_.

1. No term id was found for the name/label _vascular capillary endothelial cell of urinary bladder_ in the following 1 row _[43](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=43:43)_.

1. No term id was found for the name/label _vascular venous endothelial cell of urinary bladder_ in the following 1 row _[44](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=44:44)_.

1. No term id was found for the name/label _lymphatic endothelial cell of urinary bladder_ in the following 1 row _[45](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=45:45)_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
1. The term _PI16+ fibroblast cell of bladder_ without ontology ID has no parent that is from the CL ontology in the following 1 row _[17](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=17:17)_.

1. The term _DPT+ fibroblast cell of bladder_ without ontology ID has no parent that is from the CL ontology in the following 1 row _[18](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=18:18)_.

1. The term _CXCL14 fibroblast_ without ontology ID has no parent that is from the CL ontology in the following 1 row _[33](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=33:33)_.

1. The term _minor interstitial fibroblast_ without ontology ID has no parent that is from the CL ontology in the following 1 row _[34](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=34:34)_.

1. The term _periurothelial fibroblast_ without ontology ID has no parent that is from the CL ontology in the following 1 row _[35](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=35:35)_.

1. The term _major interstitial fibroblast_ without ontology ID has no parent that is from the CL ontology in the following 1 row _[37](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=37:37)_.


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



|    | s                                                               | slabel                            | user_slabel                       | o                                                               | olabel                       | user_olabel                  | row_number                                                                                                                |   deltaIC |
|----|-----------------------------------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------------------------------------|------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  3 | [UBERON:0004237](http://purl.obolibrary.org/obo/UBERON_0004237) | blood vessel smooth muscle        | vascular smooth muscle            | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature  | urinary bladder vasculature  | [40](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=40:40) |   21.6621 |
| 20 | [UBERON:0001261](http://purl.obolibrary.org/obo/UBERON_0001261) | lamina propria of urinary bladder | lamina propria of urinary bladder | [UBERON:0004943](http://purl.obolibrary.org/obo/UBERON_0004943) | submucosa of urinary bladder | submucosa of urinary bladder | [16](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=16:16) |  nan      |
| 22 | [UBERON:0001261](http://purl.obolibrary.org/obo/UBERON_0001261) | lamina propria of urinary bladder | lamina propria of urinary bladder | [UBERON:0004943](http://purl.obolibrary.org/obo/UBERON_0004943) | submucosa of urinary bladder | submucosa of urinary bladder | [17](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=17:17) |  nan      |
| 23 | [UBERON:0001261](http://purl.obolibrary.org/obo/UBERON_0001261) | lamina propria of urinary bladder | lamina propria of urinary bladder | [UBERON:0004943](http://purl.obolibrary.org/obo/UBERON_0004943) | submucosa of urinary bladder | submucosa of urinary bladder | [18](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=18:18) |  nan      |
| 24 | [UBERON:0001261](http://purl.obolibrary.org/obo/UBERON_0001261) | lamina propria of urinary bladder | lamina propria of urinary bladder | [UBERON:0004943](http://purl.obolibrary.org/obo/UBERON_0004943) | submucosa of urinary bladder | submucosa of urinary bladder | [19](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=19:19) |  nan      |
| 25 | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature       | urinary bladder vasculature       | [UBERON:0001256](http://purl.obolibrary.org/obo/UBERON_0001256) | wall of urinary bladder      | wall of urinary bladder      | [20](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=20:20) |  nan      |
| 27 | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature       | urinary bladder vasculature       | [UBERON:0001256](http://purl.obolibrary.org/obo/UBERON_0001256) | wall of urinary bladder      | wall of urinary bladder      | [21](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=21:21) |  nan      |
| 29 | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature       | urinary bladder vasculature       | [UBERON:0001256](http://purl.obolibrary.org/obo/UBERON_0001256) | wall of urinary bladder      | wall of urinary bladder      | [22](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=22:22) |  nan      |
| 30 | [UBERON:0011945](http://purl.obolibrary.org/obo/UBERON_0011945) | luminal layer of epithelium       | luminal layer of epithelium       | [UBERON:0004645](http://purl.obolibrary.org/obo/UBERON_0004645) | urinary bladder urothelium   | urinary bladder urothelium   | [29](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=29:29) |  nan      |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



|    | s                                                       | slabel                          | user_slabel                     | o                                                       | olabel                        | user_olabel                   | row_number                                                                                                                |   deltaIC |
|----|---------------------------------------------------------|---------------------------------|---------------------------------|---------------------------------------------------------|-------------------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                        | pericyte                        | [CL:0002597](http://purl.obolibrary.org/obo/CL_0002597) | smooth muscle cell of bladder | smooth muscle cell of bladder | [22](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=22:22) |   29.4636 |
| 13 | [CL:1000486](http://purl.obolibrary.org/obo/CL_1000486) | basal cell of urothelium        | basal cell of urothelium        | [CL:1001428](http://purl.obolibrary.org/obo/CL_1001428) | bladder urothelial cell       | bladder urothelial cell       | [12](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=12:12) |  nan      |
| 15 | [CL:4030055](http://purl.obolibrary.org/obo/CL_4030055) | intermediate cell of urothelium | intermediate cell of urothelium | [CL:1001428](http://purl.obolibrary.org/obo/CL_1001428) | bladder urothelial cell       | bladder urothelial cell       | [13](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=13:13) |  nan      |
| 17 | [CL:4030056](http://purl.obolibrary.org/obo/CL_4030056) | umbrella cell of urothelium     | umbrella cell of urothelium     | [CL:1001428](http://purl.obolibrary.org/obo/CL_1001428) | bladder urothelial cell       | bladder urothelial cell       | [14](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=14:14) |  nan      |
| 21 | [CL:0000186](http://purl.obolibrary.org/obo/CL_0000186) | myofibroblast cell              | myofibroblast                   | [CL:1001319](http://purl.obolibrary.org/obo/CL_1001319) | bladder cell                  | bladder cell                  | [16](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=16:16) |  nan      |




## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                                 | user_slabel                            | o                                                               | olabel                                 | user_olabel                            | row_number                                                                                                                |   deltaIC |
|----|---------------------------------------------------------|----------------------------------------|----------------------------------------|-----------------------------------------------------------------|----------------------------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  1 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                               | pericyte                               | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature            | urinary bladder vasculature            | [22](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=22:22) |  22.2155  |
|  2 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                               | pericyte                               | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature            | urinary bladder vasculature            | [41](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=41:41) |  22.2155  |
|  4 | [CL:0002138](http://purl.obolibrary.org/obo/CL_0002138) | endothelial cell of lymphatic vessel   | endothelial cell of lymphatic vessel   | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature            | urinary bladder vasculature            | [45](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=45:45) |  14.9675  |
|  5 | [CL:1001319](http://purl.obolibrary.org/obo/CL_1001319) | bladder cell                           | bladder cell                           | [UBERON:0001261](http://purl.obolibrary.org/obo/UBERON_0001261) | lamina propria of urinary bladder      | lamina propria of urinary bladder      | [19](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=19:19) |  12.5161  |
|  6 | [CL:0002543](http://purl.obolibrary.org/obo/CL_0002543) | vein endothelial cell                  | vein endothelial cell                  | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature            | urinary bladder vasculature            | [44](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=44:44) |  11.4439  |
|  7 | [CL:0000186](http://purl.obolibrary.org/obo/CL_0000186) | myofibroblast cell                     | myofibroblast                          | [UBERON:0001261](http://purl.obolibrary.org/obo/UBERON_0001261) | lamina propria of urinary bladder      | lamina propria of urinary bladder      | [16](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=16:16) |   8.57194 |
|  8 | [CL:1000413](http://purl.obolibrary.org/obo/CL_1000413) | endothelial cell of artery             | endothelial cell of artery             | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature            | urinary bladder vasculature            | [42](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=42:42) |   8.57194 |
|  9 | [CL:0002144](http://purl.obolibrary.org/obo/CL_0002144) | capillary endothelial cell             | capillary endothelial cell             | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature            | urinary bladder vasculature            | [43](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=43:43) |   8.57194 |
| 10 | [CL:0000646](http://purl.obolibrary.org/obo/CL_0000646) | basal cell                             | basal cell                             | [UBERON:0004645](http://purl.obolibrary.org/obo/UBERON_0004645) | urinary bladder urothelium             | urinary bladder urothelium             | [30](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=30:30) |   5.82151 |
| 11 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057) | fibroblast                             | fibroblast                             | [UBERON:0001255](http://purl.obolibrary.org/obo/UBERON_0001255) | urinary bladder                        | urinary bladder                        | [38](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=38:38) |   5.02817 |
| 12 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057) | fibroblast                             | fibroblast                             | [UBERON:0001255](http://purl.obolibrary.org/obo/UBERON_0001255) | urinary bladder                        | urinary bladder                        | [39](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=39:39) |   5.02817 |
| 14 | [CL:1000486](http://purl.obolibrary.org/obo/CL_1000486) | basal cell of urothelium               | basal cell of urothelium               | [UBERON:0004645](http://purl.obolibrary.org/obo/UBERON_0004645) | urinary bladder urothelium             | urinary bladder urothelium             | [12](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=12:12) | nan       |
| 16 | [CL:4030055](http://purl.obolibrary.org/obo/CL_4030055) | intermediate cell of urothelium        | intermediate cell of urothelium        | [UBERON:0004645](http://purl.obolibrary.org/obo/UBERON_0004645) | urinary bladder urothelium             | urinary bladder urothelium             | [13](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=13:13) | nan       |
| 18 | [CL:4030056](http://purl.obolibrary.org/obo/CL_4030056) | umbrella cell of urothelium            | umbrella cell of urothelium            | [UBERON:0004645](http://purl.obolibrary.org/obo/UBERON_0004645) | urinary bladder urothelium             | urinary bladder urothelium             | [14](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=14:14) | nan       |
| 19 | [CL:0002597](http://purl.obolibrary.org/obo/CL_0002597) | smooth muscle cell of bladder          | smooth muscle                          | [UBERON:0000381](http://purl.obolibrary.org/obo/UBERON_0000381) | urinary bladder detrusor smooth muscle | urinary bladder detrusor smooth muscle | [15](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=15:15) | nan       |
| 26 | [CL:2000040](http://purl.obolibrary.org/obo/CL_2000040) | bladder microvascular endothelial cell | bladder microvascular endothelial cell | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature            | urinary bladder vasculature            | [20](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=20:20) | nan       |
| 28 | [CL:0002597](http://purl.obolibrary.org/obo/CL_0002597) | smooth muscle cell of bladder          | smooth muscle cell of bladder          | [UBERON:0012239](http://purl.obolibrary.org/obo/UBERON_0012239) | urinary bladder vasculature            | urinary bladder vasculature            | [21](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=21:21) | nan       |
| 31 | [CL:4030055](http://purl.obolibrary.org/obo/CL_4030055) | intermediate cell of urothelium        | intermediate cell of urothelium        | [UBERON:0004645](http://purl.obolibrary.org/obo/UBERON_0004645) | urinary bladder urothelium             | urinary bladder urothelium             | [31](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=31:31) | nan       |
| 32 | [CL:0002597](http://purl.obolibrary.org/obo/CL_0002597) | smooth muscle cell of bladder          | smooth muscle cell of bladder          | [UBERON:0012378](http://purl.obolibrary.org/obo/UBERON_0012378) | muscle layer of urinary bladder        | muscle layer of urinary bladder        | [32](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=32:32) | nan       |
| 33 | [CL:0000186](http://purl.obolibrary.org/obo/CL_0000186) | myofibroblast cell                     | myofibroblast                          | [UBERON:0001255](http://purl.obolibrary.org/obo/UBERON_0001255) | urinary bladder                        | urinary bladder                        | [36](https://docs.google.com/spreadsheets/d/1iCZpti7fYupWhQjDz_tE01ii2WH23hIno9kYggMjDZo/edit#gid=1057183099&range=36:36) | nan       |




# New CL terms
[**Report**](new_cl_terms_Urinary_bladder.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Urinary_bladder.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Urinary_bladder_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Urinary_bladder_AS_has_part_CT_log.tsv)