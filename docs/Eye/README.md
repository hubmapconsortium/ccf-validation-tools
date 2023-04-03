
ASCT+B Validation Reports for Eye (2023-04-03)
==============================================

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
  
1. In row _[74](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=74:74)_, the term _[UBERON:0006761](http://purl.obolibrary.org/obo/UBERON_0006761)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _corneoscleral limbus_ and the one in the **ontology** is _corneo-scleral junction_. For reference, the given name/label **by SMEs** is _corneoscleral limbus_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[64](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=64:64)_, the term _[UBERON:0004904](http://purl.obolibrary.org/obo/UBERON_0004904)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _optic nerve_ and the one in the **ontology** is _neuron projection bundle connecting eye with brain_. For reference, the given name/label **by SMEs** is _neuron projection bundle connecting eye with brain_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[72](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=72:72)_, the term _[UBERON:0001783](http://purl.obolibrary.org/obo/UBERON_0001783)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _optic nerve head_ and the one in the **ontology** is _optic disc_. For reference, the given name/label **by SMEs** is _optic disc_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[74](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=74:74)_, the term _[UBERON:0000482](http://purl.obolibrary.org/obo/UBERON_0000482)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _basal epithelium_ and the one in the **ontology** is _basal lamina of epithelium_. For reference, the given name/label **by SMEs** is _basal epithelium_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[68](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=68:68)_, the term _[UBERON:0034713](http://purl.obolibrary.org/obo/UBERON_0034713)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _nerve bundle_ and the one in the **ontology** is _cranial neuron projection bundle_. For reference, the given name/label **by SMEs** is _cranial neuron projection bundle_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[70](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=70:70)_, the term _[UBERON:0006136](http://purl.obolibrary.org/obo/UBERON_0006136)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _unmyelinated nerve bundles_ and the one in the **ontology** is _unmyelinated nerve fiber_. For reference, the given name/label **by SMEs** is _unmyelinated nerve fiber_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[34](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=34:34)_, the term _[UBERON:0004864](http://purl.obolibrary.org/obo/UBERON_0004864)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _vasculature of retina _ and the one in the **ontology** is _vasculature of retina_. For reference, the given name/label **by SMEs** is _vasculature_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[13](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=13:13)_, no term id was found for the name/label _glutamic acid decarboxylase 65 cell_.

1. In row _[14](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=14:14)_, no term id was found for the name/label _A8 bistratified small-field cell_.

1. In row _[16](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=16:16)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[16](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=16:16)_, no term id was found for the name/label _semilunar type 1 cell_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=17:17)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=17:17)_, no term id was found for the name/label _semilunar type 3 cell_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=18:18)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=18:18)_, no term id was found for the name/label _semilunar cell_.

1. In row _[21](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=21:21)_, no term id was found for the name/label _blue cone bipolar cell_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=22:22)_, no term id was found for the name/label _Diffuse bipolar 1 (DB1)_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=23:23)_, no term id was found for the name/label _Diffuse bipolar 2 cell_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=24:24)_, no term id was found for the name/label _Diffuse bipolar 3a cell_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=25:25)_, no term id was found for the name/label _Diffuse bipolar 3b cell_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=26:26)_, no term id was found for the name/label _Diffuse bipolar 4 cell_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=27:27)_, no term id was found for the name/label _Diffuse bipolar 6 cell_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=28:28)_, no term id was found for the name/label _Flat midget bipolar cell_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=29:29)_, no term id was found for the name/label _invaginating bipolar cell_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=46:46)_, no term id was found for the name/label _Inner cortex_.

1. In row _[47](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=47:47)_, no term id was found for the name/label _Outer cortex_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=53:53)_, no term id was found for the name/label _Outer cortex_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=64:64)_, no term id was found for the name/label _glial cell_.

1. In row _[65](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=65:65)_, no term id was found for the name/label _glial cell_.

1. In row _[73](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=73:73)_, no term id was found for the name/label _conjuctival epithelium_.

1. In row _[74](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=74:74)_, no term id was found for the name/label _limbal stem cells_.


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



|    | s              | slabel                                             | user_slabel                                        | o              | olabel                                             | user_olabel                                        | row_number                                                                                                               |   deltaIC |
|----|----------------|----------------------------------------------------|----------------------------------------------------|----------------|----------------------------------------------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | UBERON:0034713 | cranial neuron projection bundle                   | cranial neuron projection bundle                   | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | [68](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=68:68) |  35.4441  |
|  1 | UBERON:0003902 | retinal neural layer                               | retinal neural layer                               | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | [67](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=67:67) |  27.2041  |
|  3 | UBERON:0001773 | sclera                                             | sclera                                             | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | [66](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=66:66) |  18.5701  |
| 10 | UBERON:0000482 | basal lamina of epithelium                         | basal epithelium                                   | UBERON:0006761 | corneo-scleral junction                            | corneoscleral limbus                               | [74](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=74:74) |   2.22887 |
| 27 | UBERON:0002203 | vasculature of eye                                 | vasculature of eye                                 | UBERON:0000966 | retina                                             | retina                                             | [32](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=32:32) | nan       |
| 41 | UBERON:0006762 | suspensory ligament of lens                        | ciliary zonules                                    | UBERON:0000965 | lens                                               | lens                                               | [59](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=59:59) | nan       |
| 42 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye                                                | eye                                                | [64](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=64:64) | nan       |
| 43 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye                                                | eye                                                | [65](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=65:65) | nan       |
| 44 | UBERON:0035966 | scleral lamina cribrosa                            | scleral lamina cribrosa                            | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | [65](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=65:65) | nan       |
| 45 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye                                                | eye                                                | [66](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=66:66) | nan       |
| 46 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye                                                | eye                                                | [67](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=67:67) | nan       |
| 47 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye                                                | eye                                                | [68](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=68:68) | nan       |
| 48 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye                                                | eye                                                | [70](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=70:70) | nan       |
| 49 | UBERON:0006136 | unmyelinated nerve fiber                           | unmyelinated nerve fiber                           | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | [70](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=70:70) | nan       |
| 50 | UBERON:0002276 | lamina of spiral limbus                            | lamina of spiral limbus                            | UBERON:0000970 | eye                                                | eye                                                | [74](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=74:74) | nan       |
| 51 | UBERON:0006761 | corneo-scleral junction                            | corneoscleral limbus                               | UBERON:0002276 | lamina of spiral limbus                            | lamina of spiral limbus                            | [74](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=74:74) | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



|    | s          | slabel                           | user_slabel           | o          | olabel                             | user_olabel       | row_number                                                                                                               |   deltaIC |
|----|------------|----------------------------------|-----------------------|------------|------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
|  2 | CL:0011005 | GABAergic interneuron            | GABAergic interneuron | CL:0000561 | Amacrine Cell                      | Amacrine cell     | [13](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=13:13) |   18.674  |
|  4 | CL:0000751 | rod bipolar cell                 | rod bipolar cell      | CL:0000749 | ON-bipolar cell                    | ON Bipolar cell   | [31](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=31:31) |   13.7747 |
| 12 | CL:0004253 | wide field retinal amacrine cell | wide field cell       | CL:0004252 | medium field retinal amacrine cell | medium-field cell | [15](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=15:15) |  nan      |
| 33 | CL:0000129 | microglial cell                  | microglial cell       | CL:0000540 | neuron                             | Neuron            | [48](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=48:48) |  nan      |
| 35 | CL:0000636 | Mueller cell                     | Muller glia           | CL:0000540 | neuron                             | Neuron            | [49](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=49:49) |  nan      |




## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                | user_slabel               | o              | olabel                        | user_olabel                 | row_number                                                                                                               |
|----|------------|---------------------------------------|---------------------------|----------------|-------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------|
|  0 | CL:0000066 | epithelial cell                       | epithelial cell           | UBERON:0002506 | iris epithelium               | iris epithelium             | [61](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=61:61) |
|  1 | CL:0000129 | microglial cell                       | microglial cell           | UBERON:0000966 | retina                        | retina                      | [48](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=48:48) |
|  2 | CL:0000132 | corneal endothelial cell              | corneal endothelial cell  | UBERON:0001985 | corneal endothelium           | corneal endothelium         | [55](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=55:55) |
|  3 | CL:0000561 | Amacrine Cell                         | Amacrine Cell             | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [12](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=12:12) |
|  4 | CL:0000573 | retinal cone cell                     | retinal cone cell         | UBERON:0001789 | outer nuclear layer of retina | outer nuclear layer         | [33](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=33:33) |
|  5 | CL:0000604 | retinal rod cell                      | retinal rod cell          | UBERON:0001789 | outer nuclear layer of retina | outer nuclear layer         | [51](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=51:51) |
|  6 | CL:0000636 | Mueller cell                          | Muller glia               | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [49](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=49:49) |
|  7 | CL:0000669 | pericyte                              | Pericyte                  | UBERON:0004864 | vasculature of retina         | vasculature                 | [50](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=50:50) |
|  8 | CL:0000740 | retinal ganglion cell                 | Ganglion cell             | UBERON:0001792 | ganglionic layer of retina    | retinal ganglion cell layer | [37](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=37:37) |
|  9 | CL:0000740 | retinal ganglion cell                 | Ganglion cell             | UBERON:0001792 | ganglionic layer of retina    | retinal ganglion cell layer | [69](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=69:69) |
| 10 | CL:0000745 | retina horizontal cell                | Horizontal Cell           | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [39](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=39:39) |
| 11 | CL:0000748 | retinal bipolar neuron                | Bipolar Cell              | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [20](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=20:20) |
| 12 | CL:0000749 | ON-bipolar cell                       | ON Bipolar cell           | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [26](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=26:26) |
| 13 | CL:0000749 | ON-bipolar cell                       | ON Bipolar cell           | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [27](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=27:27) |
| 14 | CL:0000749 | ON-bipolar cell                       | ON Bipolar cell           | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [29](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=29:29) |
| 15 | CL:0000749 | ON-bipolar cell                       | ON Bipolar cell           | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [30](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=30:30) |
| 16 | CL:0000749 | ON-bipolar cell                       | ON Bipolar cell           | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [21](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=21:21) |
| 17 | CL:0000750 | OFF-bipolar cell                      | OFF Bipolar cell          | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [23](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=23:23) |
| 18 | CL:0000750 | OFF-bipolar cell                      | OFF Bipolar cell          | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [24](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=24:24) |
| 19 | CL:0000750 | OFF-bipolar cell                      | OFF Bipolar cell          | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [22](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=22:22) |
| 20 | CL:0000750 | OFF-bipolar cell                      | OFF Bipolar cell          | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [28](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=28:28) |
| 21 | CL:0000750 | OFF-bipolar cell                      | OFF Bipolar cell          | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [25](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=25:25) |
| 22 | CL:0000751 | rod bipolar cell                      | rod bipolar cell          | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [31](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=31:31) |
| 23 | CL:0002225 | secondary lens fiber                  | mature fiber cell         | UBERON:0000390 | lens nucleus                  | Fetal nucleus               | [44](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=44:44) |
| 24 | CL:0002228 | primary lens fiber                    | primary lens fiber        | UBERON:0002444 | lens fiber                    | lens Fibers                 | [38](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=38:38) |
| 25 | CL:0002363 | keratocyte                            | keratocyte                | UBERON:0003952 | anterior stroma of cornea     | anterior stroma of cornea   | [56](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=56:56) |
| 26 | CL:0002585 | retinal blood vessel endothelial cell | Endothelial Cell          | UBERON:0004864 | vasculature of retina         | vasculature                 | [34](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=34:34) |
| 27 | CL:0004219 | A2 amacrine cell                      | A2 cell                   | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [18](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=18:18) |
| 28 | CL:0004232 | starburst amacrine cell               | starburst amacrine cell   | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [19](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=19:19) |
| 29 | CL:0004253 | wide field retinal amacrine cell      | wide field cell           | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [15](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=15:15) |
| 30 | CL:0011004 | lens fiber cell                       | lens fiber cell           | UBERON:0000390 | lens nucleus                  | Adult nucleus               | [45](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=45:45) |
| 31 | CL:0011004 | lens fiber cell                       | lens fiber cell           | UBERON:0000389 | lens cortex                   | cortex                      | [46](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=46:46) |
| 32 | CL:0011004 | lens fiber cell                       | lens fiber cell           | UBERON:0002444 | lens Fiber                    | lens Fiber                  | [53](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=53:53) |
| 33 | CL:0011004 | lens fiber cell                       | lens fiber cell           | UBERON:0002444 | lens fiber                    | lens Fibers                 | [41](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=41:41) |
| 34 | CL:0011004 | lens fiber cell                       | lens fiber cell           | UBERON:0000389 | lens cortex                   | cortex                      | [47](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=47:47) |
| 35 | CL:0011005 | GABAergic interneuron                 | GABAergic interneuron     | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [13](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=13:13) |
| 36 | CL:0017004 | telocyte                              | telocyte                  | UBERON:0003952 | anterior stroma of cornea     | anterior stroma of cornea   | [57](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=57:57) |
| 37 | CL:4023188 | Midget ganglion cell of retina        | Midget cell               | UBERON:0001792 | ganglionic layer of retina    | retinal ganglion cell layer | [35](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=35:35) |
| 38 | CL:4023189 | Parasol ganglion cell of retina       | Parasol cell              | UBERON:0001792 | ganglionic layer of retina    | retinal ganglion cell layer | [36](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=36:36) |
| 39 | CL:4030028 | glycinergic amacrine cell             | Glycinergic Amacrine Cell | UBERON:0001791 | inner nuclear layer of retina | inner nuclear layer         | [14](https://docs.google.com/spreadsheets/d/1tZ3YZ_PJ5viU2h8Bx3l02uhcMZ41AW4sbmJrKfRtfgg/edit#gid=695483621&range=14:14) |




# New CL terms
[**Report**](new_cl_terms_Eye.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Eye.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Eye_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Eye_AS_has_part_CT_log.tsv)