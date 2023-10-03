
ASCT+B Validation Reports for Prostate (2023-10-03)
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


These are the reports related to issues in the terms found in the ASCT+B table. We validate only [CL](https://www.ebi.ac.uk/ols/ontologies/cl), [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) and [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) terms.
## Terms not found


This report provides a list of terms not found neither in UBERON nor in CL. Please remove these terms from the ASCT+B table - disconsider this message if a term was recently added to the ontology.  
  
1. UBERON:0000766

1. UBERON:000570

1. UBERON:0000752


## Typos or punctuation mistakes


This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.  
  
- No issues found.


## Different labels


This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.

If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.

If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.  
  
1. In row _[19](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=19:19)_, the term _[UBERON:0001102](http://purl.obolibrary.org/obo/UBERON_0001102)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _blood vessel_ and the one in the **ontology** is _cartilage of main bronchus_. For reference, the given name/label **by SMEs** is _blood vessel_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[23](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=23:23)_, the term _[UBERON:0001431](http://purl.obolibrary.org/obo/UBERON_0001431)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _vascular smooth muscle_ and the one in the **ontology** is _distal carpal bone 2_. For reference, the given name/label **by SMEs** is _vascular smooth muscle_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[26](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=26:26)_, the term _[CL:4032000](http://purl.obolibrary.org/obo/CL_4032000)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _club cell of prostatic urethral epithelium_ and the one in the **ontology** is _club-like cell of the urethral epithelium_. For reference, the given name/label **by SMEs** is _club epithelia_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[22](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=22:22)_, the term _[UBERON:0004167](http://purl.obolibrary.org/obo/UBERON_0004167)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _lymphatic endothelial cell_ and the one in the **ontology** is _orbitofrontal cortex_. For reference, the given name/label **by SMEs** is _lymphatic endothelial cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[24](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=24:24)_, the term _[UBERON:0002441](http://purl.obolibrary.org/obo/UBERON_0002441)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _pericyte_ and the one in the **ontology** is _cervicothoracic ganglion_. For reference, the given name/label **by SMEs** is _pericyte_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[19](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=19:19)_, the term _[UBERON:0001085](http://purl.obolibrary.org/obo/UBERON_0001085)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _vascular system_ and the one in the **ontology** is _skin of trunk_. For reference, the given name/label **by SMEs** is _vascular system_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[19](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=19:19)_, the term _[UBERON:0001489](http://purl.obolibrary.org/obo/UBERON_0001489)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _whole body_ and the one in the **ontology** is _manus joint_. For reference, the given name/label **by SMEs** is _whole body_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[15](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=15:15)_, no term id was found for the name/label _ionocyte epithelia_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=19:19)_, no term id was found for the name/label _endothelial cell of artery_.

1. In row _[20](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=20:20)_, no term id was found for the name/label _capillary endothelial cell_.

1. In row _[21](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=21:21)_, no term id was found for the name/label _vein endothelial cell_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=22:22)_, no term id was found for the name/label _lymph node lymphatic vessel endothelial cell_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
- No issue found.


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



|    | s              | slabel                       | user_slabel                  | o              | olabel                     | user_olabel     | row_number                                                                                                                |   deltaIC |
|----|----------------|------------------------------|------------------------------|----------------|----------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | UBERON:0001335 | prostatic urethra            | prostatic urethra            | UBERON:0002367 | prostate gland             | prostate gland  | [25](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=25:25) | 10199.5   |
|  1 | UBERON:0001335 | prostatic urethra            | prostatic urethra            | UBERON:0002367 | prostate gland             | prostate gland  | [26](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=26:26) | 10199.5   |
|  2 | UBERON:0001335 | prostatic urethra            | prostatic urethra            | UBERON:0002367 | prostate gland             | prostate gland  | [27](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=27:27) | 10199.5   |
|  3 | UBERON:0002441 | cervicothoracic ganglion     | pericyte                     | UBERON:0001102 | cartilage of main bronchus | blood vessel    | [24](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=24:24) |   134.845 |
|  4 | UBERON:0001431 | distal carpal bone 2         | vascular smooth muscle       | UBERON:0001102 | cartilage of main bronchus | blood vessel    | [23](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=23:23) |   100     |
|  7 | UBERON:0004243 | prostate gland smooth muscle | prostate gland smooth muscle | UBERON:0004184 | prostate gland stroma      | prostate stroma | [16](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=16:16) |   nan     |
| 10 | UBERON:0001085 | skin of trunk                | vascular system              | UBERON:0001489 | manus joint                | whole body      | [19](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=19:19) |   nan     |
| 11 | UBERON:0001102 | cartilage of main bronchus   | blood vessel                 | UBERON:0001085 | skin of trunk              | vascular system | [19](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=19:19) |   nan     |
| 12 | UBERON:0001085 | skin of trunk                | vascular system              | UBERON:0001489 | manus joint                | whole body      | [20](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=20:20) |   nan     |
| 13 | UBERON:0001102 | cartilage of main bronchus   | blood vessel                 | UBERON:0001085 | skin of trunk              | vascular system | [20](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=20:20) |   nan     |
| 14 | UBERON:0001085 | skin of trunk                | vascular system              | UBERON:0001489 | manus joint                | whole body      | [21](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=21:21) |   nan     |
| 15 | UBERON:0001102 | cartilage of main bronchus   | blood vessel                 | UBERON:0001085 | skin of trunk              | vascular system | [21](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=21:21) |   nan     |
| 16 | UBERON:0001085 | skin of trunk                | vascular system              | UBERON:0001489 | manus joint                | whole body      | [23](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=23:23) |   nan     |
| 17 | UBERON:0001102 | cartilage of main bronchus   | blood vessel                 | UBERON:0001085 | skin of trunk              | vascular system | [23](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=23:23) |   nan     |
| 19 | UBERON:0001085 | skin of trunk                | vascular system              | UBERON:0001489 | manus joint                | whole body      | [24](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=24:24) |   nan     |
| 20 | UBERON:0001102 | cartilage of main bronchus   | blood vessel                 | UBERON:0001085 | skin of trunk              | vascular system | [24](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=24:24) |   nan     |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                                           | user_slabel                            | o              | olabel                   | user_olabel                | row_number                                                                                                                |       deltaIC |
|----|------------|------------------------------------------------------------------|----------------------------------------|----------------|--------------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------|
|  5 | CL:0002138 | endothelial cell of lymphatic vessel                             | endothelial cell of lymphatic vessel   | UBERON:0004167 | orbitofrontal cortex     | lymphatic endothelial cell | [22](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=22:22) |   1.10703e-43 |
|  6 | CL:0005006 | ionocyte                                                         | ionocyte epithelia                     | UBERON:0000428 | prostate epithelium      | prostate epithelium        | [15](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=15:15) | nan           |
|  8 | CL:1000301 | fibroblast of subepithelial connective tissue of prostatic gland | periprostatic fibroblast               | UBERON:0004184 | prostate gland stroma    | prostate stroma            | [17](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=17:17) | nan           |
|  9 | CL:1000299 | fibroblast of connective tissue of prostate                      | interstitial fibroblast                | UBERON:0004184 | prostate gland stroma    | prostate stroma            | [18](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=18:18) | nan           |
| 18 | CL:0000359 | vascular associated smooth muscle cell                           | vascular associated smooth muscle cell | UBERON:0001431 | distal carpal bone 2     | vascular smooth muscle     | [23](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=23:23) | nan           |
| 21 | CL:0000669 | pericyte                                                         | perictye                               | UBERON:0002441 | cervicothoracic ganglion | pericyte                   | [24](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=24:24) | nan           |
| 22 | CL:1000486 | basal cell of urothelium                                         | basal cell of urothelium               | UBERON:0001335 | prostatic urethra        | prostatic urethra          | [25](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=25:25) | nan           |
| 23 | CL:4032000 | club-like cell of the urethral epithelium                        | club epithelia                         | UBERON:0001335 | prostatic urethra        | prostatic urethra          | [26](https://docs.google.com/spreadsheets/d/1hlSptGNXzyM7vxsH930YMf6gZkHVgHUE-Qc_4uFAmoU/edit#gid=1239199370&range=26:26) | nan           |




# New CL terms
[**Report**](new_cl_terms_Prostate.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Prostate.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Prostate_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Prostate_AS_has_part_CT_log.tsv)