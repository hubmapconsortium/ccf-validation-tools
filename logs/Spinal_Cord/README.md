
ASCT+B Validation Reports for Spinal_Cord (2023-09-13)
======================================================

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
  
1. In row _[132](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=132:132)_, the term _[UBERON:0006461](http://purl.obolibrary.org/obo/UBERON_0006461)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _second sacral spinal cord segment_ and the one in the **ontology** is _S2 segment of sacral spinal cord_. For reference, the given name/label **by SMEs** is _S2 sacral spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[122](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=122:122)_, the term _[UBERON:0006466](http://purl.obolibrary.org/obo/UBERON_0006466)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _tenth thoracic spinal cord segment_ and the one in the **ontology** is _T10 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T10 thoracic spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[111](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=111:111)_, the term _[UBERON:0006451](http://purl.obolibrary.org/obo/UBERON_0006451)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _fourth lumbar spinal cord segment_ and the one in the **ontology** is _L4 segment of lumbar spinal cord_. For reference, the given name/label **by SMEs** is _L4 lumbar spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[113](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=113:113)_, the term _[UBERON:0006457](http://purl.obolibrary.org/obo/UBERON_0006457)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _first thoracic spinal cord segment_ and the one in the **ontology** is _T1 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T1 segment of thoracic spinal cord_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[110](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=110:110)_, the term _[UBERON:0006449](http://purl.obolibrary.org/obo/UBERON_0006449)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _third lumbar spinal cord segment_ and the one in the **ontology** is _L3 segment of lumbar spinal cord_. For reference, the given name/label **by SMEs** is _L3 lumbar spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[121](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=121:121)_, the term _[UBERON:0006465](http://purl.obolibrary.org/obo/UBERON_0006465)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _ninth thoracic spinal cord segment_ and the one in the **ontology** is _T9 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T9 segment of thoracic spinal cord_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[117](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=117:117)_, the term _[UBERON:0006453](http://purl.obolibrary.org/obo/UBERON_0006453)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _fifth thoracic spinal cord segment_ and the one in the **ontology** is _T5 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T5 segment of thoracic spinal cord_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[120](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=120:120)_, the term _[UBERON:0006456](http://purl.obolibrary.org/obo/UBERON_0006456)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _eighth thoracic spinal cord segment_ and the one in the **ontology** is _T8 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T8 segment of thoracic spinal cord_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[133](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=133:133)_, the term _[UBERON:0006462](http://purl.obolibrary.org/obo/UBERON_0006462)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _third sacral spinal cord segment_ and the one in the **ontology** is _S3 segment of sacral spinal cord_. For reference, the given name/label **by SMEs** is _S3 sacral spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[131](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=131:131)_, the term _[UBERON:0006460](http://purl.obolibrary.org/obo/UBERON_0006460)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _first sacral spinal cord segment_ and the one in the **ontology** is _S1 segment of sacral spinal cord_. For reference, the given name/label **by SMEs** is _S1 sacral spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[112](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=112:112)_, the term _[UBERON:0006447](http://purl.obolibrary.org/obo/UBERON_0006447)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _fifth lumbar spinal cord segment_ and the one in the **ontology** is _L5 segment of lumbar spinal cord_. For reference, the given name/label **by SMEs** is _L5 lumbar spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[116](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=116:116)_, the term _[UBERON:0006452](http://purl.obolibrary.org/obo/UBERON_0006452)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _fourth thoracic spinal cord segment_ and the one in the **ontology** is _T4 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T4 segment of thoracic spinal cord_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[123](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=123:123)_, the term _[UBERON:0006467](http://purl.obolibrary.org/obo/UBERON_0006467)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _eleventh thoracic spinal cord segment_ and the one in the **ontology** is _T11 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T11 thoracic spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[119](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=119:119)_, the term _[UBERON:0006455](http://purl.obolibrary.org/obo/UBERON_0006455)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _seventh thoracic spinal cord segment_ and the one in the **ontology** is _T7 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T7 segment of thoracic spinal cord_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[115](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=115:115)_, the term _[UBERON:0006459](http://purl.obolibrary.org/obo/UBERON_0006459)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _third thoracic spinal cord segment_ and the one in the **ontology** is _T3 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T3 segment of thoracic spinal cord_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[108](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=108:108)_, the term _[UBERON:0006448](http://purl.obolibrary.org/obo/UBERON_0006448)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _first lumbar spinal cord segment_ and the one in the **ontology** is _L1 segment of lumbar spinal cord_. For reference, the given name/label **by SMEs** is _L1 lumbar spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[118](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=118:118)_, the term _[UBERON:0006454](http://purl.obolibrary.org/obo/UBERON_0006454)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _sixth thoracic spinal cord segment_ and the one in the **ontology** is _T6 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T6 segment of thoracic spinal cord_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[109](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=109:109)_, the term _[UBERON:0006450](http://purl.obolibrary.org/obo/UBERON_0006450)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _second lumbar spinal cord segment_ and the one in the **ontology** is _L2 segment of lumbar spinal cord_. For reference, the given name/label **by SMEs** is _L2 lumbar spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[135](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=135:135)_, the term _[UBERON:0006464](http://purl.obolibrary.org/obo/UBERON_0006464)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _fifth sacral spinal cord segment_ and the one in the **ontology** is _S5 segment of sacral spinal cord_. For reference, the given name/label **by SMEs** is _S5 sacral spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[114](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=114:114)_, the term _[UBERON:0006458](http://purl.obolibrary.org/obo/UBERON_0006458)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _second thoracic spinal cord segment_ and the one in the **ontology** is _T2 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T2 segment of thoracic spinal cord_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[124](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=124:124)_, the term _[UBERON:0006468](http://purl.obolibrary.org/obo/UBERON_0006468)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _twelfth thoracic spinal cord segment_ and the one in the **ontology** is _T12 segment of thoracic spinal cord_. For reference, the given name/label **by SMEs** is _T12 thoracic spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[134](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=134:134)_, the term _[UBERON:0006463](http://purl.obolibrary.org/obo/UBERON_0006463)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _fourth sacral spinal cord segment_ and the one in the **ontology** is _S4 segment of sacral spinal cord_. For reference, the given name/label **by SMEs** is _S4 sacral spinal cord segment_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


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



|    | s              | slabel                                         | user_slabel                                    | o              | olabel                           | user_olabel                      | row_number                                                                                                                  |   deltaIC |
|----|----------------|------------------------------------------------|------------------------------------------------|----------------|----------------------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------|
| 18 | UBERON:0014620 | cervical spinal cord dorsal horn               | cervical spinal cord dorsal horn               | UBERON:0014613 | cervical spinal cord gray matter | cervical spinal cord gray matter | [141](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=141:141) |    21.852 |
| 19 | UBERON:0014620 | cervical spinal cord dorsal horn               | cervical spinal cord dorsal horn               | UBERON:0014613 | cervical spinal cord gray matter | cervical spinal cord gray matter | [142](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=142:142) |    21.852 |
| 20 | UBERON:0014609 | thoracic spinal cord dorsal horn               | thoracic spinal cord dorsal horn               | UBERON:0014636 | thoracic spinal cord gray matter | thoracic spinal cord gray matter | [145](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=145:145) |    21.852 |
| 21 | UBERON:0014543 | lumbar division of spinal cord central canal   | lumbar division of spinal cord central canal   | UBERON:0002792 | lumbar spinal cord               | lumbar spinal cord               | [20](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=20:20)    |    21.852 |
| 22 | UBERON:0014609 | thoracic spinal cord dorsal horn               | thoracic spinal cord dorsal horn               | UBERON:0014636 | thoracic spinal cord gray matter | thoracic spinal cord gray matter | [146](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=146:146) |    21.852 |
| 23 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [79](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=79:79)    |    21.852 |
| 24 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [71](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=71:71)    |    21.852 |
| 25 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [62](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=62:62)    |    21.852 |
| 26 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [144](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=144:144) |    21.852 |
| 27 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [143](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=143:143) |    21.852 |
| 28 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [63](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=63:63)    |    21.852 |
| 29 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [64](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=64:64)    |    21.852 |
| 30 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [65](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=65:65)    |    21.852 |
| 31 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [66](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=66:66)    |    21.852 |
| 32 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [67](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=67:67)    |    21.852 |
| 33 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [68](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=68:68)    |    21.852 |
| 34 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [69](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=69:69)    |    21.852 |
| 35 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [70](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=70:70)    |    21.852 |
| 36 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [72](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=72:72)    |    21.852 |
| 37 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [80](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=80:80)    |    21.852 |
| 38 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [73](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=73:73)    |    21.852 |
| 39 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [74](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=74:74)    |    21.852 |
| 40 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [75](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=75:75)    |    21.852 |
| 41 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [76](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=76:76)    |    21.852 |
| 42 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [77](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=77:77)    |    21.852 |
| 43 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [86](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=86:86)    |    21.852 |
| 44 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [85](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=85:85)    |    21.852 |
| 45 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [84](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=84:84)    |    21.852 |
| 46 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [83](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=83:83)    |    21.852 |
| 47 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [82](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=82:82)    |    21.852 |
| 48 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [78](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=78:78)    |    21.852 |
| 49 | UBERON:0014638 | lumbar spinal cord dorsal horn                 | lumbar spinal cord dorsal horn                 | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [81](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=81:81)    |    21.852 |
| 51 | UBERON:0014541 | thoracic division of spinal cord central canal | thoracic division of spinal cord central canal | UBERON:0003038 | thoracic spinal cord             | thoracic spinal cord             | [35](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=35:35)    |   nan     |
| 52 | UBERON:0014547 | sacral division of spinal cord central canal   | sacral division of spinal cord central canal   | UBERON:0005843 | sacral spinal cord               | sacral spinal cord               | [36](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=36:36)    |   nan     |
| 53 | UBERON:0014619 | cervical spinal cord lateral horn              | cervical spinal cord lateral horn              | UBERON:0014613 | cervical spinal cord gray matter | cervical spinal cord gray matter | [48](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=48:48)    |   nan     |
| 54 | UBERON:0014621 | cervical spinal cord ventral horn              | cervical spinal cord ventral horn              | UBERON:0014613 | cervical spinal cord gray matter | cervical spinal cord gray matter | [49](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=49:49)    |   nan     |
| 55 | UBERON:0007836 | cervical spinal cord ventral commissure        | cervical spinal cord ventral commissure        | UBERON:0014613 | cervical spinal cord gray matter | cervical spinal cord gray matter | [50](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=50:50)    |   nan     |
| 56 | UBERON:0007834 | lumbar spinal cord ventral commissure          | lumbar spinal cord ventral commissure          | UBERON:0029636 | lumbar spinal cord gray matter   | lumbar spinal cord gray matter   | [61](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=61:61)    |   nan     |
| 61 | UBERON:0014607 | thoracic spinal cord lateral horn              | thoracic spinal cord lateral horn              | UBERON:0014636 | thoracic spinal cord gray matter | thoracic spinal cord gray matter | [127](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=127:127) |   nan     |
| 62 | UBERON:0014610 | thoracic spinal cord ventral horn              | thoracic spinal cord ventral horn              | UBERON:0014636 | thoracic spinal cord gray matter | thoracic spinal cord gray matter | [128](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=128:128) |   nan     |
| 63 | UBERON:0007837 | thoracic spinal cord ventral commissure        | thoracic spinal cord ventral commissure        | UBERON:0014636 | thoracic spinal cord gray matter | thoracic spinal cord gray matter | [129](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=129:129) |   nan     |
| 64 | UBERON:0007835 | sacral spinal cord ventral commissure          | sacral spinal cord ventral commissure          | UBERON:0029503 | sacral spinal cord gray matter   | sacral spinal cord gray matter   | [136](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=136:136) |   nan     |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                         | user_slabel                    | o              | olabel                                       | user_olabel                                  | row_number                                                                                                                  |       deltaIC |
|----|------------|--------------------------------|--------------------------------|----------------|----------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------|
|  0 | CL:0000540 | neuron                         | Medial Excitatory Neuron 1     | UBERON:0031906 | lumbar spinal cord lateral horn              | lumbar spinal cord lateral horn              | [99](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=99:99)    |   1.83794e+14 |
|  1 | CL:0000540 | neuron                         | Medial Excitatory Neuron 2     | UBERON:0031906 | lumbar spinal cord lateral horn              | lumbar spinal cord lateral horn              | [100](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=100:100) |   1.83794e+14 |
|  2 | CL:0000540 | neuron                         | Medial Excitatory Neuron 3     | UBERON:0031906 | lumbar spinal cord lateral horn              | lumbar spinal cord lateral horn              | [101](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=101:101) |   1.83794e+14 |
|  3 | CL:0000540 | neuron                         | Medial Excitatory Neuron 4     | UBERON:0031906 | lumbar spinal cord lateral horn              | lumbar spinal cord lateral horn              | [102](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=102:102) |   1.83794e+14 |
|  4 | CL:0000540 | neuron                         | Medial Inhibitory Neuron 1     | UBERON:0031906 | lumbar spinal cord lateral horn              | lumbar spinal cord lateral horn              | [103](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=103:103) |   1.83794e+14 |
|  5 | CL:0002453 | Oligodendrocyte Precursor Cell | Oligodendrocyte Precursor Cell | UBERON:0026386 | lumbar spinal cord white matter              | lumbar spinal cord white matter              | [22](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=22:22)    |   1.62188e+10 |
|  6 | CL:0000127 | Astrocyte                      | Astrocyte                      | UBERON:0031906 | lumbar spinal cord lateral horn              | lumbar spinal cord lateral horn              | [105](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=105:105) | 100           |
|  7 | CL:0000128 | Oligodendrocyte                | Oligodendrocyte                | UBERON:0031906 | lumbar spinal cord lateral horn              | lumbar spinal cord lateral horn              | [104](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=104:104) | 100           |
|  8 | CL:0000127 | Astrocyte                      | Astrocyte                      | UBERON:0030276 | lumbar spinal cord ventral horn              | lumbar spinal cord ventral horn              | [96](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=96:96)    | 100           |
|  9 | CL:0000129 | microglial cell                | Microglia                      | UBERON:0030276 | lumbar spinal cord ventral horn              | lumbar spinal cord ventral horn              | [97](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=97:97)    | 100           |
| 10 | CL:0000115 | Endothelial Cell               | Endothelial Cell               | UBERON:0030276 | lumbar spinal cord ventral horn              | lumbar spinal cord ventral horn              | [98](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=98:98)    | 100           |
| 11 | CL:0000128 | Oligodendrocyte                | Oligodendrocyte                | UBERON:0030276 | lumbar spinal cord ventral horn              | lumbar spinal cord ventral horn              | [95](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=95:95)    | 100           |
| 12 | CL:0000128 | Oligodendrocyte                | Oligodendrocyte                | UBERON:0026386 | lumbar spinal cord white matter              | lumbar spinal cord white matter              | [21](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=21:21)    | 100           |
| 13 | CL:0000129 | microglial cell                | Microglia                      | UBERON:0031906 | lumbar spinal cord lateral horn              | lumbar spinal cord lateral horn              | [106](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=106:106) | 100           |
| 14 | CL:0000115 | Endothelial Cell               | Endothelial Cell               | UBERON:0031906 | lumbar spinal cord lateral horn              | lumbar spinal cord lateral horn              | [107](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=107:107) | 100           |
| 15 | CL:0000115 | Endothelial Cell               | Endothelial Cell               | UBERON:0026386 | lumbar spinal cord white matter              | lumbar spinal cord white matter              | [25](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=25:25)    | 100           |
| 16 | CL:0000129 | microglial cell                | Microglia                      | UBERON:0026386 | lumbar spinal cord white matter              | lumbar spinal cord white matter              | [24](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=24:24)    | 100           |
| 17 | CL:0000127 | Astrocyte                      | Astrocyte                      | UBERON:0026386 | lumbar spinal cord white matter              | lumbar spinal cord white matter              | [23](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=23:23)    | 100           |
| 50 | CL:0000065 | Ependymal Cell                 | Ependymal Cell                 | UBERON:0014543 | lumbar division of spinal cord central canal | lumbar division of spinal cord central canal | [20](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=20:20)    | nan           |
| 57 | CL:0000128 | Oligodendrocyte                | Oligodendrocyte                | UBERON:0014638 | lumbar spinal cord dorsal horn               | lumbar spinal cord dorsal horn               | [83](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=83:83)    | nan           |
| 58 | CL:0000127 | Astrocyte                      | Astrocyte                      | UBERON:0014638 | lumbar spinal cord dorsal horn               | lumbar spinal cord dorsal horn               | [84](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=84:84)    | nan           |
| 59 | CL:0000129 | microglial cell                | Microglia                      | UBERON:0014638 | lumbar spinal cord dorsal horn               | lumbar spinal cord dorsal horn               | [85](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=85:85)    | nan           |
| 60 | CL:0000115 | Endothelial Cell               | Endothelial Cell               | UBERON:0014638 | lumbar spinal cord dorsal horn               | lumbar spinal cord dorsal horn               | [86](https://docs.google.com/spreadsheets/d/10stOnKN9uucxrI665_tfu-PWC33E-0HCP1QMdFgYJ0s/edit#gid=243784891&range=86:86)    | nan           |




# New CL terms
[**Report**](new_cl_terms_Spinal_Cord.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Spinal_Cord.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Spinal_Cord_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Spinal_Cord_AS_has_part_CT_log.tsv)