
ASCT+B Validation Reports for Skin (2023-08-30)
===============================================

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
  
1. In row _[52](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=52:52)_, the term _[CL:0000669](http://purl.obolibrary.org/obo/CL_0000669)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _pericyte cell_ and the one in the **ontology** is _pericyte_. For reference, the given name/label **by SMEs** is _Pericyte_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[24](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=24:24)_, the term _[CL:0000151](http://purl.obolibrary.org/obo/CL_0000151)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _sebum secreting cell_ and the one in the **ontology** is _secretory cell_. For reference, the given name/label **by SMEs** is _Germinative (epithelial) cell, Sebocyte_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[50](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=50:50)_, the term _[CL:0000359](http://purl.obolibrary.org/obo/CL_0000359)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _smooth muscle cell_ and the one in the **ontology** is _vascular associated smooth muscle cell_. For reference, the given name/label **by SMEs** is _Perivascular smooth muscle cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[22](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=22:22)_, no term id was found for the name/label _Keratinocyte (Onychocyte)_.

1. In row _[48](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=48:48)_, no term id was found for the name/label _perineurial cells_.

1. In row _[68](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=68:68)_, no term id was found for the name/label _Perineural cell_.


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



|    | s              | slabel                       | user_slabel            | o              | olabel         | user_olabel   | row_number                                                                                                               |          deltaIC |
|----|----------------|------------------------------|------------------------|----------------|----------------|---------------|--------------------------------------------------------------------------------------------------------------------------|------------------|
|  0 | UBERON:0002027 | stratum corneum of epidermis | Stratum corneum (SC)   | UBERON:0001003 | skin epidermis | Epidermis     | [12](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=12:12) |      2.25501e+14 |
| 19 | UBERON:0007121 | skin nerve field             | nerve                  | UBERON:0002072 | hypodermis     | Subcutaneous  | [66](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=66:66) |      2.96426e+06 |
| 20 | UBERON:0000423 | eccrine sweat gland          | Eccrine (sweat) glands | UBERON:0002067 | dermis         | Dermis        | [25](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=25:25) | 274247           |
| 29 | UBERON:0001821 | sebaceous gland              | Sebaceous glands       | UBERON:0002067 | dermis         | Dermis        | [24](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=24:24) |      1.23282e-22 |
| 38 | UBERON:0008974 | apocrine gland               | Apocrine glands        | UBERON:0002067 | dermis         | Dermis        | [26](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=26:26) |    nan           |
| 48 | UBERON:0035549 | vasculature of integument    | Blood vessels          | UBERON:0002067 | dermis         | Dermis        | [49](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=49:49) |    nan           |
| 50 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [55](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=55:55) |    nan           |
| 51 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [56](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=56:56) |    nan           |
| 52 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [57](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=57:57) |    nan           |
| 53 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [58](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=58:58) |    nan           |
| 54 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [59](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=59:59) |    nan           |
| 56 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [60](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=60:60) |    nan           |
| 57 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [61](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=61:61) |    nan           |
| 58 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [62](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=62:62) |    nan           |
| 59 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [63](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=63:63) |    nan           |
| 60 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [64](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=64:64) |    nan           |
| 61 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [65](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=65:65) |    nan           |
| 62 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [66](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=66:66) |    nan           |
| 63 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [67](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=67:67) |    nan           |
| 64 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [68](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=68:68) |    nan           |
| 65 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [69](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=69:69) |    nan           |
| 66 | UBERON:0035549 | vasculature of integument    | Blood vessels          | UBERON:0002072 | hypodermis     | Subcutaneous  | [69](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=69:69) |    nan           |
| 67 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [70](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=70:70) |    nan           |
| 68 | UBERON:0002072 | hypodermis                   | Subcutaneous           | UBERON:0002097 | skin of body   | skin          | [71](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=71:71) |    nan           |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                 | user_slabel                                  | o              | olabel                          | user_olabel             | row_number                                                                                                               |
|----|------------|----------------------------------------|----------------------------------------------|----------------|---------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------|
|  0 | CL:0000097 | mast cell                              | Mast cell                                    | UBERON:0002067 | dermis                          | Dermis                  | [29](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=29:29) |
|  1 | CL:0000097 | mast cell                              | Mast cell                                    | UBERON:0002072 | hypodermis                      | Subcutaneous            | [59](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=59:59) |
|  2 | CL:0000115 | endothelial cell                       | Endothelial cell                             | UBERON:0035549 | vasculature of integument       | Blood vessels           | [69](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=69:69) |
|  3 | CL:0000115 | endothelial cell                       | Endothelial cell                             | UBERON:0035549 | vasculature of integument       | Blood vessels           | [49](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=49:49) |
|  4 | CL:0000151 | secretory cell                         | Germinative (epithelial) cell, Sebocyte      | UBERON:0001821 | sebaceous gland                 | Sebaceous glands        | [24](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=24:24) |
|  5 | CL:0000235 | macrophage                             | Macrophage                                   | UBERON:0002072 | hypodermis                      | Subcutaneous            | [58](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=58:58) |
|  6 | CL:0000235 | macrophage                             | Macrophage                                   | UBERON:0002067 | dermis                          | Dermis                  | [34](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=34:34) |
|  7 | CL:0000236 | B cell                                 | B cell                                       | UBERON:0002067 | dermis                          | Dermis                  | [42](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=42:42) |
|  8 | CL:0000236 | B cell                                 | B cell                                       | UBERON:0002072 | hypodermis                      | Subcutaneous            | [63](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=63:63) |
|  9 | CL:0000242 | Merkel cell                            | Merkel cell                                  | UBERON:0002026 | stratum spinosum of epidermis   | Stratum spinosum (SS)   | [17](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=17:17) |
| 10 | CL:0000312 | keratinocyte                           | Keratinocyte (Granular)                      | UBERON:0002069 | stratum granulosum of epidermis | Stratum granulosum (SG) | [13](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=13:13) |
| 11 | CL:0000359 | vascular associated smooth muscle cell | Perivascular smooth muscle cell              | UBERON:0002067 | dermis                          | Dermis                  | [50](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=50:50) |
| 12 | CL:0000359 | vascular associated smooth muscle cell | Perivascular smooth muscle cell              | UBERON:0002072 | hypodermis                      | Subcutaneous            | [70](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=70:70) |
| 13 | CL:0000540 | Neuron                                 | Neuron                                       | UBERON:0007121 | skin nerve field                | nerve                   | [66](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=66:66) |
| 14 | CL:0000540 | Neuron                                 | Neuron                                       | UBERON:0007121 | skin nerve field                | nerve                   | [46](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=46:46) |
| 15 | CL:0000545 | T-helper 1 cell                        | T helper                                     | UBERON:0002067 | dermis                          | Dermis                  | [35](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=35:35) |
| 16 | CL:0000545 | T-helper 1 cell                        | T helper                                     | UBERON:0002072 | hypodermis                      | Subcutaneous            | [60](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=60:60) |
| 17 | CL:0000623 | natural killer cell                    | Natural killer cell                          | UBERON:0002067 | dermis                          | Dermis                  | [38](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=38:38) |
| 18 | CL:0000646 | basal cell                             | Keratinocyte (Basal)                         | UBERON:0002025 | stratum basale of epidermis     | Stratum basale (SB)     | [18](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=18:18) |
| 19 | CL:0000669 | pericyte                               | Pericyte                                     | UBERON:0002067 | dermis                          | Dermis                  | [53](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=53:53) |
| 20 | CL:0000669 | pericyte                               | Pericyte                                     | UBERON:0002067 | dermis                          | Dermis                  | [52](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=52:52) |
| 21 | CL:0000771 | eosinophil                             | Eosinophil                                   | UBERON:0002072 | hypodermis                      | Subcutaneous            | [65](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=65:65) |
| 22 | CL:0000771 | eosinophil                             | Eosinophil                                   | UBERON:0002067 | dermis                          | Dermis                  | [45](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=45:45) |
| 23 | CL:0000775 | neutrophil                             | Neutrophil                                   | UBERON:0002072 | hypodermis                      | Subcutaneous            | [64](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=64:64) |
| 24 | CL:0000775 | neutrophil                             | Neutrophil                                   | UBERON:0002067 | dermis                          | Dermis                  | [44](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=44:44) |
| 25 | CL:0000786 | plasma cell                            | Plasma cell                                  | UBERON:0002067 | dermis                          | Dermis                  | [43](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=43:43) |
| 26 | CL:0000815 | regulatory T cell                      | T reg                                        | UBERON:0002072 | hypodermis                      | Subcutaneous            | [62](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=62:62) |
| 27 | CL:0000815 | regulatory T cell                      | T reg                                        | UBERON:0002067 | dermis                          | Dermis                  | [37](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=37:37) |
| 28 | CL:0000910 | cytotoxic T cell                       | T killer                                     | UBERON:0002072 | hypodermis                      | Subcutaneous            | [61](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=61:61) |
| 29 | CL:0000910 | cytotoxic T cell                       | T killer                                     | UBERON:0002067 | dermis                          | Dermis                  | [36](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=36:36) |
| 30 | CL:0001067 | group 1 innate lymphoid cell           | Natural killer cell / Innate lymphoid cell 1 | UBERON:0002067 | dermis                          | Dermis                  | [39](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=39:39) |
| 31 | CL:0001069 | group 2 innate lymphoid cell           | Innate lymphoid cell 2                       | UBERON:0002067 | dermis                          | Dermis                  | [40](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=40:40) |
| 32 | CL:0001071 | group 3 innate lymphoid cell           | Innate lymphoid cell 3                       | UBERON:0002067 | dermis                          | Dermis                  | [41](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=41:41) |
| 33 | CL:0002138 | endothelial cell of lymphatic vessel   | Lymphatic                                    | UBERON:0002067 | dermis                          | Dermis                  | [54](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=54:54) |
| 34 | CL:0002138 | endothelial cell of lymphatic vessel   | Lymphatic                                    | UBERON:0002072 | hypodermis                      | Subcutaneous            | [55](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=55:55) |
| 35 | CL:0002292 | type I cell of carotid body            | Glomus cell                                  | UBERON:0002072 | hypodermis                      | Subcutaneous            | [71](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=71:71) |
| 36 | CL:0002292 | type I cell of carotid body            | Glomus cell                                  | UBERON:0002067 | dermis                          | Dermis                  | [51](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=51:51) |
| 37 | CL:0002337 | keratinocyte stem cell                 | keratinocyte stem cell                       | UBERON:0002073 | hair follicle                   | Hair follicles          | [23](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=23:23) |
| 38 | CL:0002457 | epidermal Langerhans cell              | Langerhans cell                              | UBERON:0002025 | stratum basale of epidermis     | Stratum basale (SB)     | [19](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=19:19) |
| 39 | CL:0002457 | epidermal Langerhans cell              | Langerhans cell                              | UBERON:0002026 | stratum spinosum of epidermis   | Stratum spinosum (SS)   | [16](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=16:16) |
| 40 | CL:0002457 | epidermal Langerhans cell              | Langerhans cell                              | UBERON:0002069 | stratum granulosum of epidermis | Stratum granulosum (SG) | [14](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=14:14) |
| 41 | CL:0002573 | Schwann cell                           | Schwann cell                                 | UBERON:0002067 | dermis                          | Dermis                  | [47](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=47:47) |
| 42 | CL:0002573 | Schwann cell                           | Schwann cell                                 | UBERON:0002072 | hypodermis                      | Subcutaneous            | [67](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=67:67) |
| 43 | CL:0002620 | skin fibroblast                        | Fibroblast                                   | UBERON:0002067 | dermis                          | Dermis                  | [28](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=28:28) |
| 44 | CL:0002620 | skin fibroblast                        | Fibroblast                                   | UBERON:0002072 | hypodermis                      | Subcutaneous            | [57](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=57:57) |
| 45 | CL:1000417 | myoepithelial cell of sweat gland      | myoepithelial cell                           | UBERON:0008974 | apocrine gland                  | Apocrine glands         | [26](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=26:26) |
| 46 | CL:1000417 | myoepithelial cell of sweat gland      | myoepithelial cell                           | UBERON:0000423 | eccrine sweat gland             | Eccrine (sweat) glands  | [25](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=25:25) |
| 47 | CL:1000417 | myoepithelial cell of sweat gland      | myoepithelial cell                           | UBERON:0002067 | dermis                          | Dermis                  | [27](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=27:27) |
| 48 | CL:1000458 | melanocyte of skin                     | Melanocyte                                   | UBERON:0002025 | stratum basale of epidermis     | Stratum basale (SB)     | [21](https://docs.google.com/spreadsheets/d/1q2tYQ_uNh5O_eLOMUZm64ncCUeJc8mrern3zkRX3Ppw/edit#gid=269383687&range=21:21) |




# New CL terms
[**Report**](new_cl_terms_Skin.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Skin.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Skin_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Skin_AS_has_part_CT_log.tsv)