
ASCT+B Validation Reports for Palatine_Tonsil (2023-04-24)
==========================================================

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
  
1. In row _[28](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=28:28)_, the term _[UBERON:0001612](http://purl.obolibrary.org/obo/UBERON_0001612)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _tonsillar branch of the facial artery_ and the one in the **ontology** is _facial artery_. For reference, the given name/label **by SMEs** is _facial artery_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[18](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=18:18)_, the term _[CL:0000625](http://purl.obolibrary.org/obo/CL_0000625)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _CD8-positive alpha-beta T cells_ and the one in the **ontology** is _CD8-positive, alpha-beta T cell_. For reference, the given name/label **by SMEs** is _CD8 T cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[17](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=17:17)_, the term _[CL:0000624](http://purl.obolibrary.org/obo/CL_0000624)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _CD4-positive alpha-beta T cells_ and the one in the **ontology** is _CD4-positive, alpha-beta T cell_. For reference, the given name/label **by SMEs** is _CD4 T cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[30](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=30:30)_, the term _[UBERON:0001070](http://purl.obolibrary.org/obo/UBERON_0001070)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _lesser palatine artery_ and the one in the **ontology** is _external carotid artery_. For reference, the given name/label **by SMEs** is _lesser palatine artery_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[26](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=26:26)_, the term _[UBERON:0001610](http://purl.obolibrary.org/obo/UBERON_0001610)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _dorsal lingual artery_ and the one in the **ontology** is _lingual artery_. For reference, the given name/label **by SMEs** is _lingual artery_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[25](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=25:25)_, no term id was found for the name/label _plasma cell CD21_.

1. In row _[31](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=31:31)_, no term id was found for the name/label _peritonsillar plexus of veins_.

1. In row _[32](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=32:32)_, no term id was found for the name/label _tonsil T cell zone_.

1. In row _[33](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=33:33)_, no term id was found for the name/label _tonsil T cell zone_.

1. In row _[34](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=34:34)_, no term id was found for the name/label _tonsil T cell zone_.

1. In row _[35](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=35:35)_, no term id was found for the name/label _tonsil T cell zone_.

1. In row _[36](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=36:36)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[36](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=36:36)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[36](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=36:36)_, no term id was found for the name/label _Cycling B_.

1. In row _[37](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=37:37)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[37](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=37:37)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[38](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=38:38)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[38](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=38:38)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[39](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=39:39)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[39](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=39:39)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[40](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=40:40)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[40](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=40:40)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[41](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=41:41)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[41](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=41:41)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[42](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=42:42)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[42](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=42:42)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[42](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=42:42)_, no term id was found for the name/label _Cycling B_.

1. In row _[43](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=43:43)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[43](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=43:43)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[44](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=44:44)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[44](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=44:44)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[45](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=45:45)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[45](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=45:45)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[46](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=46:46)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[46](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=46:46)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[47](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=47:47)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[47](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=47:47)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[48](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=48:48)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[48](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=48:48)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[49](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=49:49)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[49](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=49:49)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[49](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=49:49)_, no term id was found for the name/label _germinal center B cell_.

1. In row _[50](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=50:50)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[50](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=50:50)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[50](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=50:50)_, no term id was found for the name/label _germinal center B cell CD21_.

1. In row _[51](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=51:51)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[51](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=51:51)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[51](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=51:51)_, no term id was found for the name/label _tonsil germinal center mantle zone_.

1. In row _[52](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=52:52)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[52](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=52:52)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[52](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=52:52)_, no term id was found for the name/label _tonsil germinal center mantle zone_.

1. In row _[53](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=53:53)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[53](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=53:53)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[53](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=53:53)_, no term id was found for the name/label _tonsil germinal center mantle zone_.

1. In row _[54](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=54:54)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[54](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=54:54)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[54](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=54:54)_, no term id was found for the name/label _Centroblast_.

1. In row _[55](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=55:55)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[55](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=55:55)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[55](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=55:55)_, no term id was found for the name/label _Cycling B_.

1. In row _[56](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=56:56)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[56](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=56:56)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[57](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=57:57)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[57](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=57:57)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[58](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=58:58)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[58](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=58:58)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[59](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=59:59)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[59](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=59:59)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[60](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=60:60)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[60](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=60:60)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[61](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=61:61)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[61](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=61:61)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[62](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=62:62)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[62](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=62:62)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[62](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=62:62)_, no term id was found for the name/label _germinal center B cell_.

1. In row _[63](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=63:63)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[63](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=63:63)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[63](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=63:63)_, no term id was found for the name/label _germinal center B cell CD21_.

1. In row _[64](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=64:64)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[64](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=64:64)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[64](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=64:64)_, no term id was found for the name/label _tonsil germinal center light zone_.

1. In row _[65](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=65:65)_, no term id was found for the name/label _tonsil follicle_.

1. In row _[65](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=65:65)_, no term id was found for the name/label _tonsil secondary follicle_.

1. In row _[65](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=65:65)_, no term id was found for the name/label _tonsil germinal center dark zone_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[16](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=16:16)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[17](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=17:17)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[18](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=18:18)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[19](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=19:19)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[20](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=20:20)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[21](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=21:21)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[22](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=22:22)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[23](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=23:23)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[24](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=24:24)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[25](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=25:25)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[27](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=27:27)_, the term _FMA:49555_ is from another ontology that is not validated in this process.

1. In row _[29](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=29:29)_, the term _FMA:49497_ is from another ontology that is not validated in this process.

1. In row _[32](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=32:32)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[33](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=33:33)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[34](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=34:34)_, the term _FMA:55221_ is from another ontology that is not validated in this process.

1. In row _[35](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=35:35)_, the term _FMA:55221_ is from another ontology that is not validated in this process.


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



|    | s              | slabel       | user_slabel   | o              | olabel   | user_olabel   | row_number                                                                                                       |   deltaIC |
|----|----------------|--------------|---------------|----------------|----------|---------------|------------------------------------------------------------------------------------------------------------------|-----------|
|  4 | UBERON:0001981 | blood vessel | blood vessel  | UBERON:0002372 | tonsil   | tonsil        | [28](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=28:28) |   26.7669 |
|  5 | UBERON:0001981 | blood vessel | blood vessel  | UBERON:0002372 | tonsil   | tonsil        | [30](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=30:30) |   26.7669 |
|  6 | UBERON:0001981 | blood vessel | blood vessel  | UBERON:0002372 | tonsil   | tonsil        | [29](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=29:29) |   26.7669 |
|  7 | UBERON:0001981 | blood vessel | blood vessel  | UBERON:0002372 | tonsil   | tonsil        | [31](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=31:31) |   26.7669 |
|  8 | UBERON:0001981 | blood vessel | blood vessel  | UBERON:0002372 | tonsil   | tonsil        | [27](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=27:27) |   26.7669 |
|  9 | UBERON:0001981 | blood vessel | blood vessel  | UBERON:0002372 | tonsil   | tonsil        | [26](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=26:26) |   26.7669 |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                          | user_slabel                   | o              | olabel                  | user_olabel            | row_number                                                                                                       |
|----|------------|---------------------------------|-------------------------------|----------------|-------------------------|------------------------|------------------------------------------------------------------------------------------------------------------|
|  0 | CL:0000057 | Fibroblast                      | fibroblast                    | UBERON:0002372 | tonsil                  | tonsil                 | [19](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=19:19) |
|  1 | CL:0000071 | blood vessel endothelial cell   | blood vessel endothelial cell | UBERON:0001070 | external carotid artery | lesser palatine artery | [30](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=30:30) |
|  2 | CL:0000071 | blood vessel endothelial cell   | blood vessel endothelial cell | UBERON:0001612 | facial artery           | facial artery          | [28](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=28:28) |
|  3 | CL:0000071 | blood vessel endothelial cell   | blood vessel endothelial cell | UBERON:0001610 | lingual artery          | lingual artery         | [26](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=26:26) |
|  4 | CL:0000084 | T Cell                          | T Cell                        | UBERON:0010754 | germinal center         | germinal center        | [47](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=47:47) |
|  5 | CL:0000084 | T Cell                          | T Cell                        | UBERON:0013688 | tonsil germinal center  | tonsil germinal center | [60](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=60:60) |
|  6 | CL:0000084 | T cell                          | T cell                        | UBERON:0002372 | tonsil                  | tonsil                 | [16](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=16:16) |
|  7 | CL:0000235 | Macrophage                      | macrophage                    | UBERON:0002372 | tonsil                  | tonsil                 | [23](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=23:23) |
|  8 | CL:0000235 | Macrophage                      | macrophage                    | UBERON:0010754 | germinal center         | germinal center        | [48](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=48:48) |
|  9 | CL:0000235 | Macrophage                      | macrophage                    | UBERON:0013688 | tonsil germinal center  | tonsil germinal center | [61](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=61:61) |
| 10 | CL:0000236 | B cell                          | B cell                        | UBERON:0010754 | germinal center         | germinal center        | [45](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=45:45) |
| 11 | CL:0000236 | B cell                          | B cell                        | UBERON:0013688 | tonsil germinal center  | tonsil germinal center | [58](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=58:58) |
| 12 | CL:0000236 | B cell                          | B cell                        | UBERON:0002372 | tonsil                  | tonsil                 | [21](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=21:21) |
| 13 | CL:0000432 | Reticular cell                  | reticular cells               | UBERON:0002372 | tonsil                  | tonsil                 | [20](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=20:20) |
| 14 | CL:0000451 | Dendritic Cell                  | dendritic cell                | UBERON:0002372 | tonsil                  | tonsil                 | [22](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=22:22) |
| 15 | CL:0000624 | CD4-positive, alpha-beta T cell | CD4 T cell                    | UBERON:0010754 | germinal center         | germinal center        | [43](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=43:43) |
| 16 | CL:0000624 | CD4-positive, alpha-beta T cell | CD4 T cell                    | UBERON:0002372 | tonsil                  | tonsil                 | [17](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=17:17) |
| 17 | CL:0000624 | CD4-positive, alpha-beta T cell | CD4 T cell                    | UBERON:0013688 | tonsil germinal center  | tonsil germinal center | [56](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=56:56) |
| 18 | CL:0000625 | CD8-positive, alpha-beta T cell | CD8 T cell                    | UBERON:0002372 | tonsil                  | tonsil                 | [18](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=18:18) |
| 19 | CL:0000786 | Plasma Cell                     | plasma cell                   | UBERON:0002372 | tonsil                  | tonsil                 | [24](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=24:24) |
| 20 | CL:0000786 | Plasma Cell                     | plasma cell                   | UBERON:0013688 | tonsil germinal center  | tonsil germinal center | [59](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=59:59) |
| 21 | CL:0000786 | Plasma Cell                     | plasma cell                   | UBERON:0010754 | germinal center         | germinal center        | [46](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=46:46) |
| 22 | CL:0000815 | regulatory T cell               | regulatory T cell             | UBERON:0010754 | germinal center         | germinal center        | [44](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=44:44) |
| 23 | CL:0000815 | regulatory T cell               | regulatory T cell             | UBERON:0013688 | tonsil germinal center  | tonsil germinal center | [57](https://docs.google.com/spreadsheets/d/14VTmaZyxa68uEl9sDKE7N8VBGL8893WlrxnTPBhcjBM/edit#gid=0&range=57:57) |




# New CL terms
[**Report**](new_cl_terms_Palatine_Tonsil.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Palatine_Tonsil.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Palatine_Tonsil_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Palatine_Tonsil_AS_has_part_CT_log.tsv)