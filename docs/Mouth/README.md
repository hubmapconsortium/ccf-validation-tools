
ASCT+B Validation Reports for Mouth (2025-02-26)
================================================

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
  
1. The term _[UBERON:0000165](http://purl.obolibrary.org/obo/UBERON_0000165)_ has a different name/label in the source ontology in the following 66 rows _[12](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=12:12)_, _[13](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=13:13)_, _[14](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=14:14)_, _[15](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=15:15)_, _[16](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=16:16)_, _[17](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=17:17)_, _[18](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=18:18)_, _[19](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=19:19)_, _[20](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=20:20)_, _[21](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=21:21)_, _[22](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=22:22)_, _[23](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=23:23)_, _[24](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=24:24)_, _[25](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=25:25)_, _[26](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=26:26)_, _[27](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=27:27)_, _[28](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=28:28)_, _[29](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=29:29)_, _[30](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=30:30)_, _[31](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=31:31)_, _[32](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=32:32)_, _[33](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=33:33)_, _[34](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=34:34)_, _[35](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=35:35)_, _[36](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=36:36)_, _[37](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=37:37)_, _[38](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=38:38)_, _[39](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=39:39)_, _[40](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=40:40)_, _[41](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=41:41)_, _[42](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=42:42)_, _[43](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=43:43)_, _[44](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=44:44)_, _[45](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=45:45)_, _[46](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=46:46)_, _[47](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=47:47)_, _[48](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=48:48)_, _[49](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=49:49)_, _[50](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=50:50)_, _[51](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=51:51)_, _[52](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=52:52)_, _[53](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=53:53)_, _[54](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=54:54)_, _[55](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=55:55)_, _[56](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=56:56)_, _[57](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=57:57)_, _[58](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=58:58)_, _[59](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=59:59)_, _[60](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=60:60)_, _[61](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=61:61)_, _[62](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=62:62)_, _[63](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=63:63)_, _[64](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=64:64)_, _[65](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=65:65)_, _[66](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=66:66)_, _[67](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=67:67)_, _[68](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=68:68)_, _[69](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=69:69)_, _[70](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=70:70)_, _[71](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=71:71)_, _[72](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=72:72)_, _[73](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=73:73)_, _[74](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=74:74)_, _[75](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=75:75)_, _[76](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=76:76)_, _[77](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=77:77)_. The name/label in the **ASCT+B table** is _oral cavity_ and the one in the **ontology** is _mouth_. For reference, the given name/label **by SMEs** is _oral cavity_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. The term _[UBERON:0003729](http://purl.obolibrary.org/obo/UBERON_0003729)_ has a different name/label in the source ontology in the following 22 rows _[36](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=36:36)_, _[37](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=37:37)_, _[38](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=38:38)_, _[39](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=39:39)_, _[40](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=40:40)_, _[41](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=41:41)_, _[42](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=42:42)_, _[43](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=43:43)_, _[44](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=44:44)_, _[45](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=45:45)_, _[46](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=46:46)_, _[47](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=47:47)_, _[48](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=48:48)_, _[49](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=49:49)_, _[50](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=50:50)_, _[51](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=51:51)_, _[52](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=52:52)_, _[53](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=53:53)_, _[54](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=54:54)_, _[55](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=55:55)_, _[56](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=56:56)_, _[57](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=57:57)_. The name/label in the **ASCT+B table** is _oral cavity mucosa_ and the one in the **ontology** is _mouth mucosa_. For reference, the given name/label **by SMEs** is _oral cavity mucosa_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


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



- No issues found.






## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                              | user_slabel                         | o                                                               | olabel                      | user_olabel                 | row_number                                                                                                                |   deltaIC |
|----|---------------------------------------------------------|-------------------------------------|-------------------------------------|-----------------------------------------------------------------|-----------------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | [CL:0002623](http://purl.obolibrary.org/obo/CL_0002623) | acinar cell of salivary gland       | acinar cell of salivary gland       | [UBERON:0011847](http://purl.obolibrary.org/obo/UBERON_0011847) | acinus of parotid gland     | acinus of parotid gland     | [58](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=58:58) |       nan |
|  1 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland | intercalated cell of salivary gland | [UBERON:0003360](http://purl.obolibrary.org/obo/UBERON_0003360) | epithelium of parotid gland | epithelium of parotid gland | [59](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=59:59) |       nan |
|  2 | [CL:4052049](http://purl.obolibrary.org/obo/CL_4052049) | striated cell of salivary gland     | striated cell of salivary gland     | [UBERON:0003419](http://purl.obolibrary.org/obo/UBERON_0003419) | mesenchyme of parotid       | mesenchyme of parotid       | [60](https://docs.google.com/spreadsheets/d/1F3AWx_miDX1i5zo7FKwmBqEHfhX34coeJqSc-qczUbY/edit#gid=1843863063&range=60:60) |       nan |




# New CL terms
[**Report**](new_cl_terms_Mouth.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Mouth.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Mouth_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Mouth_AS_has_part_CT_log.tsv)