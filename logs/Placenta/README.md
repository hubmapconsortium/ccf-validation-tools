
ASCT+B Validation Reports for Placenta (2023-01-25)
===================================================

Table of contents
=================

* [Invalid terms](#invalid-terms)
	* [Terms not found](#terms-not-found)
	* [Typos or punctuation mistakes](#typos-or-punctuation-mistakes)
	* [Different labels](#different-labels)
	* [Blank ontology ID](#blank-ontology-id)
	* [Terms from another ontology](#terms-from-another-ontology)
* [Relationship reports](#relationship-reports)
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


This report provides a list of terms not found neither in UBERON nor in CL. Please remove these terms from the ASCT+B table.  
  
- No issues found.


## Typos or punctuation mistakes


This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.  
  
- No issues found.


## Different labels


This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.

If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.

If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.  
  
1. In row _[34](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=34:34)_, the term _[CL:2000091](http://purl.obolibrary.org/obo/CL_2000091)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _endometrial microvascular endothelial cells_ and the one in the ontology is _endometrial microvascular endothelial cell_. For reference, the given name/label by SMEs is _endometrial microvascular endothelial cell (EMEC)_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[25](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=25:25)_, the term _[CL:0000523](http://purl.obolibrary.org/obo/CL_0000523)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _cytotrophoblast_ and the one in the ontology is _mononuclear cytotrophoblast cell_. For reference, the given name/label by SMEs is _cytotrophoblast (CTB)_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[13](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=13:13)_, the term _[CL:0000669](http://purl.obolibrary.org/obo/CL_0000669)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _pericyte cell_ and the one in the ontology is _pericyte_. For reference, the given name/label by SMEs is _pericytes_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[53](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=53:53)_, the term _[CL:2000062](http://purl.obolibrary.org/obo/CL_2000062)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _placental villous capillary endothelial cell_ and the one in the ontology is _placental villus capillary endothelial cell_. For reference, the given name/label by SMEs is _placental microvascular endothelial cells_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[40](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=40:40)_, the term _[CL:0000525](http://purl.obolibrary.org/obo/CL_0000525)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _syncytiotrophoblast_ and the one in the ontology is _syncytiotrophoblast cell_. For reference, the given name/label by SMEs is _syncytiotrophoblast (STB)_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[20](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=20:20)_, the term _[UBERON:0003254](http://purl.obolibrary.org/obo/UBERON_0003254)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _amnion epithelium_ and the one in the ontology is _amniotic ectoderm_. For reference, the given name/label by SMEs is _amniotic ectoderm_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[19](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=19:19)_, no term id was found for the name/label _placental disc_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=19:19)_, no term id was found for the name/label _placental disc_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=19:19)_, no term id was found for the name/label _basal plate_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=19:19)_, no term id was found for the name/label _placental disc_.

1. In row _[21](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=21:21)_, no term id was found for the name/label _amnion mesenchymal stromal cell (AMSC)_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=22:22)_, no term id was found for the name/label _placental disc_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=22:22)_, no term id was found for the name/label _placental disc_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=23:23)_, no term id was found for the name/label _placental disc_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=23:23)_, no term id was found for the name/label _placental disc_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=23:23)_, no term id was found for the name/label _amnion mesenchymal stromal cell (AMSC)_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=24:24)_, no term id was found for the name/label _fetal membranes_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=24:24)_, no term id was found for the name/label _fetal membranes_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=24:24)_, no term id was found for the name/label _chorionic mesenchymal stromal cell (CMSC)_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=25:25)_, no term id was found for the name/label _fetal membranes_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=25:25)_, no term id was found for the name/label _fetal membranes_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=26:26)_, no term id was found for the name/label _fetal membranes_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=26:26)_, no term id was found for the name/label _fetal membranes_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=27:27)_, no term id was found for the name/label _fetal membranes_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=27:27)_, no term id was found for the name/label _fetal membranes_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=27:27)_, no term id was found for the name/label _endometrial epithelial cell_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=28:28)_, no term id was found for the name/label _fetal membranes_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=28:28)_, no term id was found for the name/label _fetal membranes_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=29:29)_, no term id was found for the name/label _fetal membranes_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=29:29)_, no term id was found for the name/label _fetal membranes_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=29:29)_, no term id was found for the name/label _uterine NK cell_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=30:30)_, no term id was found for the name/label _fetal membranes_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=30:30)_, no term id was found for the name/label _fetal membranes_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=30:30)_, no term id was found for the name/label _uterine macrophage_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=31:31)_, no term id was found for the name/label _fetal membranes_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=31:31)_, no term id was found for the name/label _fetal membranes_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=32:32)_, no term id was found for the name/label _fetal membranes_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=32:32)_, no term id was found for the name/label _fetal membranes_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=33:33)_, no term id was found for the name/label _fetal membranes_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=33:33)_, no term id was found for the name/label _fetal membranes_.

1. In row _[34](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=34:34)_, no term id was found for the name/label _fetal membranes_.

1. In row _[34](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=34:34)_, no term id was found for the name/label _fetal membranes_.

1. In row _[35](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=35:35)_, no term id was found for the name/label _fetal membranes_.

1. In row _[35](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=35:35)_, no term id was found for the name/label _fetal membranes_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=36:36)_, no term id was found for the name/label _fetal membranes_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=36:36)_, no term id was found for the name/label _fetal membranes_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=36:36)_, no term id was found for the name/label _decidual lymphatic vessel_.

1. In row _[37](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=37:37)_, no term id was found for the name/label _fetal membranes_.

1. In row _[37](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=37:37)_, no term id was found for the name/label _fetal membranes_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=38:38)_, no term id was found for the name/label _fetal membranes_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=38:38)_, no term id was found for the name/label _fetal membranes_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=38:38)_, no term id was found for the name/label _amnion mesenchymal stromal cell (AMSC)_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=39:39)_, no term id was found for the name/label _placental disc_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=39:39)_, no term id was found for the name/label _placental disc_.

1. In row _[40](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=40:40)_, no term id was found for the name/label _placental disc_.

1. In row _[40](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=40:40)_, no term id was found for the name/label _placental disc_.

1. In row _[41](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=41:41)_, no term id was found for the name/label _placental disc_.

1. In row _[41](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=41:41)_, no term id was found for the name/label _placental disc_.

1. In row _[42](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=42:42)_, no term id was found for the name/label _placental disc_.

1. In row _[42](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=42:42)_, no term id was found for the name/label _placental disc_.

1. In row _[42](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=42:42)_, no term id was found for the name/label _chorionic plate vessel_.

1. In row _[43](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=43:43)_, no term id was found for the name/label _placental disc_.

1. In row _[43](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=43:43)_, no term id was found for the name/label _placental disc_.

1. In row _[43](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=43:43)_, no term id was found for the name/label _chorionic plate vessel_.

1. In row _[44](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=44:44)_, no term id was found for the name/label _placental disc_.

1. In row _[44](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=44:44)_, no term id was found for the name/label _placental disc_.

1. In row _[44](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=44:44)_, no term id was found for the name/label _chorionic plate vessel_.

1. In row _[45](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=45:45)_, no term id was found for the name/label _placental disc_.

1. In row _[45](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=45:45)_, no term id was found for the name/label _placental disc_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=46:46)_, no term id was found for the name/label _placental disc_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=46:46)_, no term id was found for the name/label _placental disc_.

1. In row _[47](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=47:47)_, no term id was found for the name/label _placental disc_.

1. In row _[47](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=47:47)_, no term id was found for the name/label _placental disc_.

1. In row _[48](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=48:48)_, no term id was found for the name/label _placental disc_.

1. In row _[48](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=48:48)_, no term id was found for the name/label _placental disc_.

1. In row _[48](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=48:48)_, no term id was found for the name/label _villous mesenchyme_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=49:49)_, no term id was found for the name/label _placental disc_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=49:49)_, no term id was found for the name/label _placental disc_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=49:49)_, no term id was found for the name/label _villous mesenchyme_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=49:49)_, no term id was found for the name/label _placental stromal cell (PSC)_.

1. In row _[50](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=50:50)_, no term id was found for the name/label _placental disc_.

1. In row _[50](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=50:50)_, no term id was found for the name/label _placental disc_.

1. In row _[50](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=50:50)_, no term id was found for the name/label _stem villous vessel_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=51:51)_, no term id was found for the name/label _placental disc_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=51:51)_, no term id was found for the name/label _placental disc_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=51:51)_, no term id was found for the name/label _stem villous vessel_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=52:52)_, no term id was found for the name/label _placental disc_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=52:52)_, no term id was found for the name/label _placental disc_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=52:52)_, no term id was found for the name/label _stem villous vessel_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=53:53)_, no term id was found for the name/label _placental disc_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=53:53)_, no term id was found for the name/label _placental disc_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=53:53)_, no term id was found for the name/label _villous capillary_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=54:54)_, no term id was found for the name/label _placental disc_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=54:54)_, no term id was found for the name/label _placental disc_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=54:54)_, no term id was found for the name/label _villous capillary_.

1. In row _[55](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=55:55)_, no term id was found for the name/label _placental disc_.

1. In row _[55](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=55:55)_, no term id was found for the name/label _placental disc_.

1. In row _[55](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=55:55)_, no term id was found for the name/label _basal plate_.

1. In row _[55](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=55:55)_, no term id was found for the name/label _basal plate_.

1. In row _[55](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=55:55)_, no term id was found for the name/label _endometrial epithelial cell_.

1. In row _[56](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=56:56)_, no term id was found for the name/label _placental disc_.

1. In row _[56](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=56:56)_, no term id was found for the name/label _placental disc_.

1. In row _[56](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=56:56)_, no term id was found for the name/label _basal plate_.

1. In row _[56](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=56:56)_, no term id was found for the name/label _basal plate_.

1. In row _[57](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=57:57)_, no term id was found for the name/label _placental disc_.

1. In row _[57](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=57:57)_, no term id was found for the name/label _placental disc_.

1. In row _[57](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=57:57)_, no term id was found for the name/label _basal plate_.

1. In row _[57](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=57:57)_, no term id was found for the name/label _basal plate_.

1. In row _[57](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=57:57)_, no term id was found for the name/label _uterine NK cell_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=58:58)_, no term id was found for the name/label _placental disc_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=58:58)_, no term id was found for the name/label _placental disc_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=58:58)_, no term id was found for the name/label _basal plate_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=58:58)_, no term id was found for the name/label _basal plate_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=58:58)_, no term id was found for the name/label _uterine macrophage_.

1. In row _[59](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=59:59)_, no term id was found for the name/label _placental disc_.

1. In row _[59](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=59:59)_, no term id was found for the name/label _placental disc_.

1. In row _[59](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=59:59)_, no term id was found for the name/label _basal plate_.

1. In row _[59](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=59:59)_, no term id was found for the name/label _basal plate_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=60:60)_, no term id was found for the name/label _placental disc_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=60:60)_, no term id was found for the name/label _placental disc_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=60:60)_, no term id was found for the name/label _basal plate_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=60:60)_, no term id was found for the name/label _basal plate_.

1. In row _[61](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=61:61)_, no term id was found for the name/label _placental disc_.

1. In row _[61](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=61:61)_, no term id was found for the name/label _placental disc_.

1. In row _[61](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=61:61)_, no term id was found for the name/label _basal plate_.

1. In row _[61](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=61:61)_, no term id was found for the name/label _basal plate_.

1. In row _[62](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=62:62)_, no term id was found for the name/label _placental disc_.

1. In row _[62](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=62:62)_, no term id was found for the name/label _placental disc_.

1. In row _[62](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=62:62)_, no term id was found for the name/label _basal plate_.

1. In row _[62](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=62:62)_, no term id was found for the name/label _basal plate_.

1. In row _[63](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=63:63)_, no term id was found for the name/label _placental disc_.

1. In row _[63](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=63:63)_, no term id was found for the name/label _placental disc_.

1. In row _[63](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=63:63)_, no term id was found for the name/label _basal plate_.

1. In row _[63](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=63:63)_, no term id was found for the name/label _basal plate_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=64:64)_, no term id was found for the name/label _placental disc_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=64:64)_, no term id was found for the name/label _placental disc_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=64:64)_, no term id was found for the name/label _basal plate_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=64:64)_, no term id was found for the name/label _basal plate_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1TqatRIsZZ5QwvWdz6H4Un-sukbzSd21_x41Gqnn5UEY/edit#gid=231591207&range=64:64)_, no term id was found for the name/label _decidual lymphatic vessel_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
- No issues found.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Placenta_log.tsv)
## Relationship CT-CT report
[**Report**](class_Placenta_log.tsv)
## Relationship CT-AS report
[**Report**](Placenta_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Placenta.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Placenta.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Placenta_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Placenta_AS_has_part_CT_log.tsv)