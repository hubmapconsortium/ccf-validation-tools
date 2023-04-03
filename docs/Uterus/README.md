
ASCT+B Validation Reports for Uterus (2023-04-03)
=================================================

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
  
1. In row _[54](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=54:54)_, the term _[UBERON:0001295](http://purl.obolibrary.org/obo/UBERON_0001295)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is __ and the one in the **ontology** is _endometrium_. For reference, the given name/label **by SMEs** is _endometrium_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[429](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=429:429)_, the term _[UBERON:0011949](http://purl.obolibrary.org/obo/UBERON_0011949)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is __ and the one in the **ontology** is _endometrium luminal epithelium_. For reference, the given name/label **by SMEs** is _endometrium luminal epithelium_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[13](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=13:13)_, the term _[UBERON:0008889](http://purl.obolibrary.org/obo/UBERON_0008889)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _uterine venous plexsus_ and the one in the **ontology** is _uterine venous plexus_. For reference, the given name/label **by SMEs** is _uterine venous plexsus_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[35](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=35:35)_, the term _[UBERON:0012252](http://purl.obolibrary.org/obo/UBERON_0012252)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is __ and the one in the **ontology** is _endocervical epithelium_. For reference, the given name/label **by SMEs** is _endocervical epithelium_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[428](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=428:428)_, the term _[UBERON:0012276](http://purl.obolibrary.org/obo/UBERON_0012276)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is __ and the one in the **ontology** is _endometrium glandular epithelium_. For reference, the given name/label **by SMEs** is _endometrium glandular epithelium_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[43](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=43:43)_, the term _[UBERON:0006922](http://purl.obolibrary.org/obo/UBERON_0006922)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is __ and the one in the **ontology** is _cervix squamous epithelium_. For reference, the given name/label **by SMEs** is _cervix squamous epithelium_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[22](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=22:22)_, the term _[UBERON:0002493](http://purl.obolibrary.org/obo/UBERON_0002493)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is __ and the one in the **ontology** is _uterine artery_. For reference, the given name/label **by SMEs** is _uterine artery_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[42](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=42:42)_, the term _[UBERON:0012250](http://purl.obolibrary.org/obo/UBERON_0012250)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is __ and the one in the **ontology** is _cervix glandular epithelium_. For reference, the given name/label **by SMEs** is _cervix glandular epithelium_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[21](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=21:21)_, the term _[UBERON:0003885](http://purl.obolibrary.org/obo/UBERON_0003885)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is __ and the one in the **ontology** is _mesometrium_. For reference, the given name/label **by SMEs** is _mesometrium_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[428](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=428:428)_, the term _[UBERON:0002451](http://purl.obolibrary.org/obo/UBERON_0002451)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is __ and the one in the **ontology** is _endometrial gland_. For reference, the given name/label **by SMEs** is _endometrial gland_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[410](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=410:410)_, the term _[UBERON:0002337](http://purl.obolibrary.org/obo/UBERON_0002337)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is __ and the one in the **ontology** is _endometrial stroma_. For reference, the given name/label **by SMEs** is _endometrial stroma_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[14](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=14:14)_, no term id was found for the name/label _superior uterine vein_.

1. In row _[15](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=15:15)_, no term id was found for the name/label _inferior uterine vein_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=18:18)_, no term id was found for the name/label _cervical mucosa_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=19:19)_, no term id was found for the name/label _cervical os_.

1. In row _[20](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=20:20)_, no term id was found for the name/label _cervical squamo-columnar junction_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=23:23)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=23:23)_, no term id was found for the name/label _endothelial cell_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=24:24)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=24:24)_, no term id was found for the name/label _endothelial cell_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=25:25)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=25:25)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=25:25)_, no term id was found for the name/label _endothelial cell_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=26:26)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=26:26)_, no term id was found for the name/label _endothelial cell_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=27:27)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=27:27)_, no term id was found for the name/label _endothelial cell_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=28:28)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=28:28)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=28:28)_, no term id was found for the name/label _endothelial cell_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=29:29)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=29:29)_, no term id was found for the name/label _endothelial cell_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=30:30)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=30:30)_, no term id was found for the name/label _endothelial cell_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=31:31)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=31:31)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=31:31)_, no term id was found for the name/label _endothelial cell_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=32:32)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=32:32)_, no term id was found for the name/label _endothelial cell_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=33:33)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=33:33)_, no term id was found for the name/label _endothelial cell_.

1. In row _[34](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=34:34)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[34](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=34:34)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[34](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=34:34)_, no term id was found for the name/label _endothelial cell_.

1. In row _[35](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=35:35)_, no term id was found for the name/label _endocervical epithelial cell_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=36:36)_, no term id was found for the name/label _internal cervical os_.

1. In row _[37](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=37:37)_, no term id was found for the name/label _endocervical stroma_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=38:38)_, no term id was found for the name/label _columnar cell of endocervix_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=39:39)_, no term id was found for the name/label _external cervical os_.

1. In row _[40](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=40:40)_, no term id was found for the name/label _ectocervical epithelium_.

1. In row _[41](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=41:41)_, no term id was found for the name/label _ectocervical stroma_.

1. In row _[44](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=44:44)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[44](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=44:44)_, no term id was found for the name/label _endothelial cell_.

1. In row _[45](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=45:45)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[45](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=45:45)_, no term id was found for the name/label _endothelial cell_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=46:46)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=46:46)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=46:46)_, no term id was found for the name/label _endothelial cell_.

1. In row _[47](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=47:47)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[47](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=47:47)_, no term id was found for the name/label _endothelial cell_.

1. In row _[48](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=48:48)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[48](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=48:48)_, no term id was found for the name/label _endothelial cell_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=49:49)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=49:49)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=49:49)_, no term id was found for the name/label _endothelial cell_.

1. In row _[50](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=50:50)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[50](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=50:50)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=51:51)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=51:51)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=52:52)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=52:52)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=52:52)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=53:53)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=53:53)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=53:53)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=54:54)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=54:54)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[55](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=55:55)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[55](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=55:55)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[56](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=56:56)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[56](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=56:56)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[57](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=57:57)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[57](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=57:57)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=58:58)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=58:58)_, no term id was found for the name/label _stromal cell_.

1. In row _[59](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=59:59)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[59](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=59:59)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=60:60)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=60:60)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[61](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=61:61)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[61](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=61:61)_, no term id was found for the name/label _macrophage_.

1. In row _[62](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=62:62)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[62](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=62:62)_, no term id was found for the name/label _lymphocyte_.

1. In row _[63](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=63:63)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[63](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=63:63)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=64:64)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=64:64)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[65](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=65:65)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[65](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=65:65)_, no term id was found for the name/label _B cell_.

1. In row _[66](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=66:66)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[66](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=66:66)_, no term id was found for the name/label _T cell_.

1. In row _[67](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=67:67)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[67](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=67:67)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[68](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=68:68)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[68](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=68:68)_, no term id was found for the name/label _mast cell_.

1. In row _[69](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=69:69)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[69](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=69:69)_, no term id was found for the name/label _endothelial cell_.

1. In row _[70](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=70:70)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[70](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=70:70)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[71](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=71:71)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[71](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=71:71)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[72](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=72:72)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[72](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=72:72)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[72](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=72:72)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[73](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=73:73)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[73](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=73:73)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[73](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=73:73)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[74](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=74:74)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[74](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=74:74)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[75](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=75:75)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[75](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=75:75)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[76](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=76:76)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[76](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=76:76)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[77](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=77:77)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[77](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=77:77)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[78](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=78:78)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[78](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=78:78)_, no term id was found for the name/label _stromal cell_.

1. In row _[79](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=79:79)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[79](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=79:79)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[80](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=80:80)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[80](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=80:80)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[81](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=81:81)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[81](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=81:81)_, no term id was found for the name/label _macrophage_.

1. In row _[82](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=82:82)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[82](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=82:82)_, no term id was found for the name/label _lymphocyte_.

1. In row _[83](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=83:83)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[83](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=83:83)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[84](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=84:84)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[84](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=84:84)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[85](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=85:85)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[85](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=85:85)_, no term id was found for the name/label _B cell_.

1. In row _[86](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=86:86)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[86](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=86:86)_, no term id was found for the name/label _T cell_.

1. In row _[87](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=87:87)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[87](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=87:87)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[88](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=88:88)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[88](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=88:88)_, no term id was found for the name/label _mast cell_.

1. In row _[89](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=89:89)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[89](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=89:89)_, no term id was found for the name/label _endothelial cell_.

1. In row _[90](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=90:90)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[90](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=90:90)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[90](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=90:90)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[91](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=91:91)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[91](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=91:91)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[91](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=91:91)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[92](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=92:92)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[92](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=92:92)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[92](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=92:92)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[92](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=92:92)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[93](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=93:93)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[93](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=93:93)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[93](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=93:93)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[93](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=93:93)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[94](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=94:94)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[94](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=94:94)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[94](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=94:94)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[95](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=95:95)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[95](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=95:95)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[95](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=95:95)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[96](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=96:96)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[96](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=96:96)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[96](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=96:96)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[97](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=97:97)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[97](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=97:97)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[97](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=97:97)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[98](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=98:98)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[98](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=98:98)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[98](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=98:98)_, no term id was found for the name/label _stromal cell_.

1. In row _[99](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=99:99)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[99](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=99:99)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[99](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=99:99)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[100](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=100:100)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[100](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=100:100)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[100](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=100:100)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[101](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=101:101)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[101](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=101:101)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[101](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=101:101)_, no term id was found for the name/label _macrophage_.

1. In row _[102](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=102:102)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[102](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=102:102)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[102](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=102:102)_, no term id was found for the name/label _lymphocyte_.

1. In row _[103](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=103:103)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[103](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=103:103)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[103](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=103:103)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[104](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=104:104)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[104](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=104:104)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[104](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=104:104)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[105](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=105:105)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[105](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=105:105)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[105](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=105:105)_, no term id was found for the name/label _B cell_.

1. In row _[106](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=106:106)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[106](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=106:106)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[106](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=106:106)_, no term id was found for the name/label _T cell_.

1. In row _[107](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=107:107)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[107](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=107:107)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[107](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=107:107)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[108](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=108:108)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[108](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=108:108)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[108](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=108:108)_, no term id was found for the name/label _mast cell_.

1. In row _[109](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=109:109)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[109](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=109:109)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[109](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=109:109)_, no term id was found for the name/label _endothelial cell_.

1. In row _[110](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=110:110)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[110](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=110:110)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[111](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=111:111)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[111](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=111:111)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[112](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=112:112)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[112](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=112:112)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[112](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=112:112)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[113](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=113:113)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[113](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=113:113)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[113](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=113:113)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[114](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=114:114)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[114](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=114:114)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[115](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=115:115)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[115](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=115:115)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[116](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=116:116)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[116](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=116:116)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[117](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=117:117)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[117](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=117:117)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[118](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=118:118)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[118](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=118:118)_, no term id was found for the name/label _stromal cell_.

1. In row _[119](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=119:119)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[119](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=119:119)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[120](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=120:120)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[120](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=120:120)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[121](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=121:121)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[121](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=121:121)_, no term id was found for the name/label _macrophage_.

1. In row _[122](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=122:122)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[122](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=122:122)_, no term id was found for the name/label _lymphocyte_.

1. In row _[123](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=123:123)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[123](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=123:123)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[124](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=124:124)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[124](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=124:124)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[125](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=125:125)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[125](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=125:125)_, no term id was found for the name/label _B cell_.

1. In row _[126](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=126:126)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[126](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=126:126)_, no term id was found for the name/label _T cell_.

1. In row _[127](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=127:127)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[127](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=127:127)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[128](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=128:128)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[128](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=128:128)_, no term id was found for the name/label _mast cell_.

1. In row _[129](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=129:129)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[129](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=129:129)_, no term id was found for the name/label _endothelial cell_.

1. In row _[130](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=130:130)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[130](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=130:130)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[131](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=131:131)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[131](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=131:131)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[132](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=132:132)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[132](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=132:132)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[132](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=132:132)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[133](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=133:133)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[133](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=133:133)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[133](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=133:133)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[134](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=134:134)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[134](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=134:134)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[135](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=135:135)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[135](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=135:135)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[136](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=136:136)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[136](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=136:136)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[137](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=137:137)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[137](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=137:137)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[138](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=138:138)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[138](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=138:138)_, no term id was found for the name/label _stromal cell_.

1. In row _[139](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=139:139)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[139](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=139:139)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[140](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=140:140)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[140](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=140:140)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[141](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=141:141)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[141](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=141:141)_, no term id was found for the name/label _macrophage_.

1. In row _[142](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=142:142)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[142](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=142:142)_, no term id was found for the name/label _lymphocyte_.

1. In row _[143](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=143:143)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[143](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=143:143)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[144](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=144:144)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[144](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=144:144)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[145](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=145:145)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[145](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=145:145)_, no term id was found for the name/label _B cell_.

1. In row _[146](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=146:146)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[146](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=146:146)_, no term id was found for the name/label _T cell_.

1. In row _[147](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=147:147)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[147](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=147:147)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[148](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=148:148)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[148](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=148:148)_, no term id was found for the name/label _mast cell_.

1. In row _[149](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=149:149)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[149](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=149:149)_, no term id was found for the name/label _endothelial cell_.

1. In row _[150](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=150:150)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[150](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=150:150)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[150](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=150:150)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[151](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=151:151)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[151](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=151:151)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[151](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=151:151)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[152](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=152:152)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[152](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=152:152)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[152](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=152:152)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[152](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=152:152)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[153](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=153:153)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[153](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=153:153)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[153](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=153:153)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[153](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=153:153)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[154](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=154:154)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[154](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=154:154)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[154](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=154:154)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[155](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=155:155)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[155](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=155:155)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[155](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=155:155)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[156](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=156:156)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[156](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=156:156)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[156](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=156:156)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[157](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=157:157)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[157](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=157:157)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[157](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=157:157)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[158](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=158:158)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[158](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=158:158)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[158](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=158:158)_, no term id was found for the name/label _stromal cell_.

1. In row _[159](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=159:159)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[159](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=159:159)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[159](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=159:159)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[160](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=160:160)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[160](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=160:160)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[160](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=160:160)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[161](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=161:161)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[161](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=161:161)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[161](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=161:161)_, no term id was found for the name/label _macrophage_.

1. In row _[162](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=162:162)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[162](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=162:162)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[162](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=162:162)_, no term id was found for the name/label _lymphocyte_.

1. In row _[163](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=163:163)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[163](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=163:163)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[163](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=163:163)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[164](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=164:164)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[164](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=164:164)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[164](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=164:164)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[165](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=165:165)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[165](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=165:165)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[165](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=165:165)_, no term id was found for the name/label _B cell_.

1. In row _[166](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=166:166)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[166](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=166:166)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[166](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=166:166)_, no term id was found for the name/label _T cell_.

1. In row _[167](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=167:167)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[167](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=167:167)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[167](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=167:167)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[168](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=168:168)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[168](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=168:168)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[168](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=168:168)_, no term id was found for the name/label _mast cell_.

1. In row _[169](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=169:169)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[169](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=169:169)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[169](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=169:169)_, no term id was found for the name/label _endothelial cell_.

1. In row _[170](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=170:170)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[170](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=170:170)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[171](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=171:171)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[171](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=171:171)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[172](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=172:172)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[172](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=172:172)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[172](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=172:172)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[173](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=173:173)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[173](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=173:173)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[173](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=173:173)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[174](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=174:174)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[174](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=174:174)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[175](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=175:175)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[175](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=175:175)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[176](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=176:176)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[176](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=176:176)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[177](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=177:177)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[177](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=177:177)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[178](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=178:178)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[178](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=178:178)_, no term id was found for the name/label _stromal cell_.

1. In row _[179](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=179:179)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[179](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=179:179)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[180](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=180:180)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[180](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=180:180)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[181](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=181:181)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[181](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=181:181)_, no term id was found for the name/label _macrophage_.

1. In row _[182](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=182:182)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[182](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=182:182)_, no term id was found for the name/label _lymphocyte_.

1. In row _[183](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=183:183)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[183](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=183:183)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[184](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=184:184)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[184](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=184:184)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[185](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=185:185)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[185](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=185:185)_, no term id was found for the name/label _B cell_.

1. In row _[186](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=186:186)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[186](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=186:186)_, no term id was found for the name/label _T cell_.

1. In row _[187](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=187:187)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[187](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=187:187)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[188](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=188:188)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[188](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=188:188)_, no term id was found for the name/label _mast cell_.

1. In row _[189](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=189:189)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[189](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=189:189)_, no term id was found for the name/label _endothelial cell_.

1. In row _[190](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=190:190)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[190](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=190:190)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[191](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=191:191)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[191](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=191:191)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[192](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=192:192)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[192](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=192:192)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[192](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=192:192)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[193](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=193:193)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[193](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=193:193)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[193](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=193:193)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[194](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=194:194)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[194](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=194:194)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[195](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=195:195)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[195](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=195:195)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[196](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=196:196)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[196](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=196:196)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[197](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=197:197)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[197](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=197:197)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[198](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=198:198)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[198](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=198:198)_, no term id was found for the name/label _stromal cell_.

1. In row _[199](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=199:199)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[199](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=199:199)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[200](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=200:200)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[200](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=200:200)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[201](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=201:201)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[201](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=201:201)_, no term id was found for the name/label _macrophage_.

1. In row _[202](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=202:202)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[202](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=202:202)_, no term id was found for the name/label _lymphocyte_.

1. In row _[203](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=203:203)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[203](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=203:203)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[204](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=204:204)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[204](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=204:204)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[205](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=205:205)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[205](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=205:205)_, no term id was found for the name/label _B cell_.

1. In row _[206](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=206:206)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[206](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=206:206)_, no term id was found for the name/label _T cell_.

1. In row _[207](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=207:207)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[207](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=207:207)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[208](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=208:208)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[208](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=208:208)_, no term id was found for the name/label _mast cell_.

1. In row _[209](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=209:209)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[209](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=209:209)_, no term id was found for the name/label _endothelial cell_.

1. In row _[210](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=210:210)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[210](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=210:210)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[210](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=210:210)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[211](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=211:211)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[211](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=211:211)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[211](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=211:211)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[212](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=212:212)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[212](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=212:212)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[212](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=212:212)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[212](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=212:212)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[213](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=213:213)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[213](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=213:213)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[213](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=213:213)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[213](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=213:213)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[214](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=214:214)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[214](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=214:214)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[214](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=214:214)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[215](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=215:215)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[215](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=215:215)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[215](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=215:215)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[216](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=216:216)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[216](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=216:216)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[216](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=216:216)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[217](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=217:217)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[217](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=217:217)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[217](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=217:217)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[218](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=218:218)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[218](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=218:218)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[218](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=218:218)_, no term id was found for the name/label _stromal cell_.

1. In row _[219](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=219:219)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[219](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=219:219)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[219](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=219:219)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[220](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=220:220)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[220](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=220:220)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[220](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=220:220)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[221](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=221:221)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[221](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=221:221)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[221](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=221:221)_, no term id was found for the name/label _macrophage_.

1. In row _[222](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=222:222)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[222](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=222:222)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[222](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=222:222)_, no term id was found for the name/label _lymphocyte_.

1. In row _[223](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=223:223)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[223](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=223:223)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[223](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=223:223)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[224](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=224:224)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[224](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=224:224)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[224](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=224:224)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[225](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=225:225)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[225](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=225:225)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[225](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=225:225)_, no term id was found for the name/label _B cell_.

1. In row _[226](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=226:226)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[226](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=226:226)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[226](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=226:226)_, no term id was found for the name/label _T cell_.

1. In row _[227](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=227:227)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[227](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=227:227)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[227](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=227:227)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[228](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=228:228)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[228](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=228:228)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[228](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=228:228)_, no term id was found for the name/label _mast cell_.

1. In row _[229](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=229:229)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[229](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=229:229)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[229](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=229:229)_, no term id was found for the name/label _endothelial cell_.

1. In row _[230](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=230:230)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[230](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=230:230)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[231](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=231:231)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[231](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=231:231)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[232](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=232:232)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[232](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=232:232)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[232](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=232:232)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[233](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=233:233)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[233](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=233:233)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[233](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=233:233)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[234](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=234:234)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[234](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=234:234)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[235](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=235:235)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[235](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=235:235)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[236](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=236:236)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[236](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=236:236)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[237](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=237:237)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[237](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=237:237)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[238](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=238:238)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[238](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=238:238)_, no term id was found for the name/label _stromal cell_.

1. In row _[239](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=239:239)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[239](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=239:239)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[240](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=240:240)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[240](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=240:240)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[241](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=241:241)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[241](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=241:241)_, no term id was found for the name/label _macrophage_.

1. In row _[242](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=242:242)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[242](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=242:242)_, no term id was found for the name/label _lymphocyte_.

1. In row _[243](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=243:243)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[243](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=243:243)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[244](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=244:244)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[244](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=244:244)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[245](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=245:245)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[245](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=245:245)_, no term id was found for the name/label _B cell_.

1. In row _[246](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=246:246)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[246](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=246:246)_, no term id was found for the name/label _T cell_.

1. In row _[247](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=247:247)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[247](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=247:247)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[248](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=248:248)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[248](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=248:248)_, no term id was found for the name/label _mast cell_.

1. In row _[249](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=249:249)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[249](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=249:249)_, no term id was found for the name/label _endothelial cell_.

1. In row _[250](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=250:250)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[250](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=250:250)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[251](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=251:251)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[251](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=251:251)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[252](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=252:252)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[252](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=252:252)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[252](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=252:252)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[253](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=253:253)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[253](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=253:253)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[253](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=253:253)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[254](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=254:254)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[254](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=254:254)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[255](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=255:255)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[255](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=255:255)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[256](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=256:256)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[256](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=256:256)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[257](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=257:257)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[257](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=257:257)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[258](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=258:258)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[258](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=258:258)_, no term id was found for the name/label _stromal cell_.

1. In row _[259](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=259:259)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[259](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=259:259)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[260](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=260:260)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[260](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=260:260)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[261](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=261:261)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[261](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=261:261)_, no term id was found for the name/label _macrophage_.

1. In row _[262](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=262:262)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[262](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=262:262)_, no term id was found for the name/label _lymphocyte_.

1. In row _[263](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=263:263)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[263](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=263:263)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[264](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=264:264)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[264](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=264:264)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[265](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=265:265)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[265](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=265:265)_, no term id was found for the name/label _B cell_.

1. In row _[266](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=266:266)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[266](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=266:266)_, no term id was found for the name/label _T cell_.

1. In row _[267](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=267:267)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[267](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=267:267)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[268](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=268:268)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[268](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=268:268)_, no term id was found for the name/label _mast cell_.

1. In row _[269](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=269:269)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[269](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=269:269)_, no term id was found for the name/label _endothelial cell_.

1. In row _[270](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=270:270)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[270](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=270:270)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[270](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=270:270)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[271](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=271:271)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[271](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=271:271)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[271](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=271:271)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[272](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=272:272)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[272](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=272:272)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[272](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=272:272)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[272](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=272:272)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[273](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=273:273)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[273](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=273:273)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[273](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=273:273)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[273](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=273:273)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[274](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=274:274)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[274](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=274:274)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[274](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=274:274)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[275](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=275:275)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[275](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=275:275)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[275](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=275:275)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[276](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=276:276)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[276](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=276:276)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[276](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=276:276)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[277](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=277:277)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[277](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=277:277)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[277](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=277:277)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[278](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=278:278)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[278](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=278:278)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[278](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=278:278)_, no term id was found for the name/label _stromal cell_.

1. In row _[279](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=279:279)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[279](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=279:279)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[279](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=279:279)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[280](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=280:280)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[280](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=280:280)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[280](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=280:280)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[281](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=281:281)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[281](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=281:281)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[281](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=281:281)_, no term id was found for the name/label _macrophage_.

1. In row _[282](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=282:282)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[282](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=282:282)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[282](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=282:282)_, no term id was found for the name/label _lymphocyte_.

1. In row _[283](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=283:283)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[283](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=283:283)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[283](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=283:283)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[284](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=284:284)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[284](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=284:284)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[284](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=284:284)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[285](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=285:285)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[285](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=285:285)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[285](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=285:285)_, no term id was found for the name/label _B cell_.

1. In row _[286](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=286:286)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[286](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=286:286)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[286](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=286:286)_, no term id was found for the name/label _T cell_.

1. In row _[287](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=287:287)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[287](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=287:287)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[287](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=287:287)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[288](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=288:288)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[288](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=288:288)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[288](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=288:288)_, no term id was found for the name/label _mast cell_.

1. In row _[289](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=289:289)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[289](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=289:289)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[289](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=289:289)_, no term id was found for the name/label _endothelial cell_.

1. In row _[290](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=290:290)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[290](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=290:290)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[291](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=291:291)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[291](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=291:291)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[292](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=292:292)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[292](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=292:292)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[292](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=292:292)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[293](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=293:293)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[293](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=293:293)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[293](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=293:293)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[294](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=294:294)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[294](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=294:294)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[295](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=295:295)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[295](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=295:295)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[296](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=296:296)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[296](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=296:296)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[297](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=297:297)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[297](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=297:297)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[298](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=298:298)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[298](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=298:298)_, no term id was found for the name/label _stromal cell_.

1. In row _[299](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=299:299)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[299](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=299:299)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[300](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=300:300)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[300](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=300:300)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[301](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=301:301)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[301](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=301:301)_, no term id was found for the name/label _macrophage_.

1. In row _[302](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=302:302)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[302](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=302:302)_, no term id was found for the name/label _lymphocyte_.

1. In row _[303](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=303:303)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[303](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=303:303)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[304](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=304:304)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[304](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=304:304)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[305](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=305:305)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[305](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=305:305)_, no term id was found for the name/label _B cell_.

1. In row _[306](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=306:306)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[306](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=306:306)_, no term id was found for the name/label _T cell_.

1. In row _[307](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=307:307)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[307](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=307:307)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[308](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=308:308)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[308](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=308:308)_, no term id was found for the name/label _mast cell_.

1. In row _[309](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=309:309)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[309](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=309:309)_, no term id was found for the name/label _endothelial cell_.

1. In row _[310](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=310:310)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[310](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=310:310)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[311](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=311:311)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[311](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=311:311)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[312](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=312:312)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[312](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=312:312)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[312](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=312:312)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[313](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=313:313)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[313](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=313:313)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[313](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=313:313)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[314](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=314:314)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[314](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=314:314)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[315](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=315:315)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[315](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=315:315)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[316](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=316:316)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[316](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=316:316)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[317](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=317:317)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[317](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=317:317)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[318](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=318:318)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[318](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=318:318)_, no term id was found for the name/label _stromal cell_.

1. In row _[319](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=319:319)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[319](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=319:319)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[320](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=320:320)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[320](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=320:320)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[321](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=321:321)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[321](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=321:321)_, no term id was found for the name/label _macrophage_.

1. In row _[322](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=322:322)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[322](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=322:322)_, no term id was found for the name/label _lymphocyte_.

1. In row _[323](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=323:323)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[323](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=323:323)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[324](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=324:324)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[324](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=324:324)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[325](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=325:325)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[325](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=325:325)_, no term id was found for the name/label _B cell_.

1. In row _[326](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=326:326)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[326](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=326:326)_, no term id was found for the name/label _T cell_.

1. In row _[327](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=327:327)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[327](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=327:327)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[328](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=328:328)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[328](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=328:328)_, no term id was found for the name/label _mast cell_.

1. In row _[329](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=329:329)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[329](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=329:329)_, no term id was found for the name/label _endothelial cell_.

1. In row _[330](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=330:330)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[330](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=330:330)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[330](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=330:330)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[331](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=331:331)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[331](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=331:331)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[331](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=331:331)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[332](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=332:332)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[332](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=332:332)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[332](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=332:332)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[332](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=332:332)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[333](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=333:333)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[333](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=333:333)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[333](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=333:333)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[333](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=333:333)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[334](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=334:334)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[334](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=334:334)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[334](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=334:334)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[335](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=335:335)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[335](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=335:335)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[335](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=335:335)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[336](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=336:336)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[336](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=336:336)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[336](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=336:336)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[337](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=337:337)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[337](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=337:337)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[337](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=337:337)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[338](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=338:338)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[338](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=338:338)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[338](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=338:338)_, no term id was found for the name/label _stromal cell_.

1. In row _[339](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=339:339)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[339](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=339:339)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[339](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=339:339)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[340](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=340:340)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[340](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=340:340)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[340](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=340:340)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[341](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=341:341)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[341](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=341:341)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[341](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=341:341)_, no term id was found for the name/label _macrophage_.

1. In row _[342](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=342:342)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[342](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=342:342)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[342](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=342:342)_, no term id was found for the name/label _lymphocyte_.

1. In row _[343](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=343:343)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[343](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=343:343)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[343](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=343:343)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[344](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=344:344)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[344](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=344:344)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[344](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=344:344)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[345](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=345:345)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[345](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=345:345)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[345](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=345:345)_, no term id was found for the name/label _B cell_.

1. In row _[346](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=346:346)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[346](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=346:346)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[346](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=346:346)_, no term id was found for the name/label _T cell_.

1. In row _[347](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=347:347)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[347](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=347:347)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[347](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=347:347)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[348](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=348:348)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[348](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=348:348)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[348](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=348:348)_, no term id was found for the name/label _mast cell_.

1. In row _[349](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=349:349)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[349](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=349:349)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[349](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=349:349)_, no term id was found for the name/label _endothelial cell_.

1. In row _[350](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=350:350)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[350](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=350:350)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[351](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=351:351)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[351](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=351:351)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[352](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=352:352)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[352](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=352:352)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[352](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=352:352)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[353](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=353:353)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[353](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=353:353)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[353](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=353:353)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[354](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=354:354)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[354](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=354:354)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[355](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=355:355)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[355](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=355:355)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[356](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=356:356)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[356](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=356:356)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[357](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=357:357)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[357](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=357:357)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[358](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=358:358)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[358](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=358:358)_, no term id was found for the name/label _stromal cell_.

1. In row _[359](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=359:359)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[359](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=359:359)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[360](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=360:360)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[360](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=360:360)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[361](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=361:361)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[361](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=361:361)_, no term id was found for the name/label _macrophage_.

1. In row _[362](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=362:362)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[362](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=362:362)_, no term id was found for the name/label _lymphocyte_.

1. In row _[363](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=363:363)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[363](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=363:363)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[364](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=364:364)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[364](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=364:364)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[365](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=365:365)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[365](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=365:365)_, no term id was found for the name/label _B cell_.

1. In row _[366](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=366:366)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[366](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=366:366)_, no term id was found for the name/label _T cell_.

1. In row _[367](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=367:367)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[367](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=367:367)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[368](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=368:368)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[368](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=368:368)_, no term id was found for the name/label _mast cell_.

1. In row _[369](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=369:369)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[369](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=369:369)_, no term id was found for the name/label _endothelial cell_.

1. In row _[370](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=370:370)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[370](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=370:370)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[371](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=371:371)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[371](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=371:371)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[372](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=372:372)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[372](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=372:372)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[372](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=372:372)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[373](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=373:373)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[373](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=373:373)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[373](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=373:373)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[374](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=374:374)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[374](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=374:374)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[375](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=375:375)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[375](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=375:375)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[376](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=376:376)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[376](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=376:376)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[377](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=377:377)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[377](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=377:377)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[378](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=378:378)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[378](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=378:378)_, no term id was found for the name/label _stromal cell_.

1. In row _[379](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=379:379)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[379](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=379:379)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[380](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=380:380)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[380](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=380:380)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[381](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=381:381)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[381](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=381:381)_, no term id was found for the name/label _macrophage_.

1. In row _[382](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=382:382)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[382](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=382:382)_, no term id was found for the name/label _lymphocyte_.

1. In row _[383](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=383:383)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[383](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=383:383)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[384](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=384:384)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[384](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=384:384)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[385](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=385:385)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[385](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=385:385)_, no term id was found for the name/label _B cell_.

1. In row _[386](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=386:386)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[386](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=386:386)_, no term id was found for the name/label _T cell_.

1. In row _[387](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=387:387)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[387](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=387:387)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[388](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=388:388)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[388](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=388:388)_, no term id was found for the name/label _mast cell_.

1. In row _[389](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=389:389)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[389](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=389:389)_, no term id was found for the name/label _endothelial cell_.

1. In row _[390](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=390:390)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[390](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=390:390)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[390](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=390:390)_, no term id was found for the name/label _connective tissue of the uterine serosa_.

1. In row _[391](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=391:391)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[391](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=391:391)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[391](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=391:391)_, no term id was found for the name/label _mesothelium of the uterine serosa_.

1. In row _[392](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=392:392)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[392](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=392:392)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[392](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=392:392)_, no term id was found for the name/label _inner uterine myometrium_.

1. In row _[392](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=392:392)_, no term id was found for the name/label _uterine smooth muscle type I cell_.

1. In row _[393](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=393:393)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[393](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=393:393)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[393](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=393:393)_, no term id was found for the name/label _outer uterine myometrium_.

1. In row _[393](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=393:393)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[394](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=394:394)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[394](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=394:394)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[394](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=394:394)_, no term id was found for the name/label _SOX9+ epithelial cell_.

1. In row _[395](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=395:395)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[395](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=395:395)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[395](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=395:395)_, no term id was found for the name/label _ciliated epithelial cell_.

1. In row _[396](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=396:396)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[396](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=396:396)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[396](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=396:396)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[397](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=397:397)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[397](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=397:397)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[397](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=397:397)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[398](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=398:398)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[398](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=398:398)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[398](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=398:398)_, no term id was found for the name/label _stromal cell_.

1. In row _[399](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=399:399)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[399](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=399:399)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[399](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=399:399)_, no term id was found for the name/label _uterine smooth muscle type II cell_.

1. In row _[400](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=400:400)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[400](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=400:400)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[400](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=400:400)_, no term id was found for the name/label _perivascular support cell_.

1. In row _[401](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=401:401)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[401](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=401:401)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[401](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=401:401)_, no term id was found for the name/label _macrophage_.

1. In row _[402](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=402:402)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[402](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=402:402)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[402](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=402:402)_, no term id was found for the name/label _lymphocyte_.

1. In row _[403](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=403:403)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[403](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=403:403)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[403](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=403:403)_, no term id was found for the name/label _uterine natural killer cell_.

1. In row _[404](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=404:404)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[404](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=404:404)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[404](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=404:404)_, no term id was found for the name/label _uterine dendritic cells_.

1. In row _[405](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=405:405)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[405](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=405:405)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[405](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=405:405)_, no term id was found for the name/label _B cell_.

1. In row _[406](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=406:406)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[406](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=406:406)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[406](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=406:406)_, no term id was found for the name/label _T cell_.

1. In row _[407](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=407:407)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[407](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=407:407)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[407](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=407:407)_, no term id was found for the name/label _innate lymphoid cell_.

1. In row _[408](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=408:408)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[408](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=408:408)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[408](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=408:408)_, no term id was found for the name/label _mast cell_.

1. In row _[409](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=409:409)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[409](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=409:409)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[409](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=409:409)_, no term id was found for the name/label _endothelial cell_.

1. In row _[410](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=410:410)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[410](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=410:410)_, no term id was found for the name/label _stromal cell_.

1. In row _[411](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=411:411)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[411](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=411:411)_, no term id was found for the name/label _stromal cell_.

1. In row _[412](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=412:412)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[412](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=412:412)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[412](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=412:412)_, no term id was found for the name/label _stromal cell_.

1. In row _[413](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=413:413)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[413](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=413:413)_, no term id was found for the name/label _stromal cell_.

1. In row _[414](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=414:414)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[414](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=414:414)_, no term id was found for the name/label _stromal cell_.

1. In row _[415](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=415:415)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[415](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=415:415)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[415](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=415:415)_, no term id was found for the name/label _stromal cell_.

1. In row _[416](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=416:416)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[416](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=416:416)_, no term id was found for the name/label _stromal cell_.

1. In row _[417](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=417:417)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[417](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=417:417)_, no term id was found for the name/label _stromal cell_.

1. In row _[418](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=418:418)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[418](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=418:418)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[418](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=418:418)_, no term id was found for the name/label _stromal cell_.

1. In row _[419](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=419:419)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[419](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=419:419)_, no term id was found for the name/label _stromal cell_.

1. In row _[420](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=420:420)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[420](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=420:420)_, no term id was found for the name/label _stromal cell_.

1. In row _[421](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=421:421)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[421](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=421:421)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[421](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=421:421)_, no term id was found for the name/label _stromal cell_.

1. In row _[422](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=422:422)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[422](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=422:422)_, no term id was found for the name/label _stromal cell_.

1. In row _[423](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=423:423)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[423](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=423:423)_, no term id was found for the name/label _stromal cell_.

1. In row _[424](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=424:424)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[424](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=424:424)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[424](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=424:424)_, no term id was found for the name/label _stromal cell_.

1. In row _[425](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=425:425)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[425](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=425:425)_, no term id was found for the name/label _stromal cell_.

1. In row _[426](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=426:426)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[426](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=426:426)_, no term id was found for the name/label _stromal cell_.

1. In row _[427](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=427:427)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[427](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=427:427)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[427](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=427:427)_, no term id was found for the name/label _stromal cell_.

1. In row _[428](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=428:428)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[428](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=428:428)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[429](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=429:429)_, no term id was found for the name/label _central anterior body of uterus_.

1. In row _[429](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=429:429)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[430](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=430:430)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[430](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=430:430)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[431](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=431:431)_, no term id was found for the name/label _central anterior fundus of uterus_.

1. In row _[431](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=431:431)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[432](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=432:432)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[432](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=432:432)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[432](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=432:432)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[433](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=433:433)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[433](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=433:433)_, no term id was found for the name/label _central anterior lower uterine segment_.

1. In row _[433](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=433:433)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[434](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=434:434)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[434](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=434:434)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[435](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=435:435)_, no term id was found for the name/label _central posterior body of uterus_.

1. In row _[435](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=435:435)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[436](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=436:436)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[436](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=436:436)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[437](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=437:437)_, no term id was found for the name/label _central posterior fundus of uterus_.

1. In row _[437](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=437:437)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[438](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=438:438)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[438](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=438:438)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[438](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=438:438)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[439](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=439:439)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[439](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=439:439)_, no term id was found for the name/label _central posterior lower uterine segment_.

1. In row _[439](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=439:439)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[440](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=440:440)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[440](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=440:440)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[441](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=441:441)_, no term id was found for the name/label _left anterior body of uterus_.

1. In row _[441](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=441:441)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[442](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=442:442)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[442](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=442:442)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[443](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=443:443)_, no term id was found for the name/label _left anterior fundus of uterus_.

1. In row _[443](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=443:443)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[444](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=444:444)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[444](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=444:444)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[444](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=444:444)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[445](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=445:445)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[445](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=445:445)_, no term id was found for the name/label _left anterior lower uterine segment_.

1. In row _[445](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=445:445)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[446](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=446:446)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[446](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=446:446)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[447](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=447:447)_, no term id was found for the name/label _left posterior body of uterus_.

1. In row _[447](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=447:447)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[448](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=448:448)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[448](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=448:448)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[449](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=449:449)_, no term id was found for the name/label _left posterior fundus of uterus_.

1. In row _[449](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=449:449)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[450](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=450:450)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[450](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=450:450)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[450](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=450:450)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[451](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=451:451)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[451](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=451:451)_, no term id was found for the name/label _left posterior lower uterine segment_.

1. In row _[451](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=451:451)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[452](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=452:452)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[452](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=452:452)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[453](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=453:453)_, no term id was found for the name/label _right anterior body of uterus_.

1. In row _[453](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=453:453)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[454](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=454:454)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[454](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=454:454)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[455](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=455:455)_, no term id was found for the name/label _right anterior fundus of uterus_.

1. In row _[455](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=455:455)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[456](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=456:456)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[456](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=456:456)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[456](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=456:456)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[457](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=457:457)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[457](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=457:457)_, no term id was found for the name/label _right anterior lower uterine segment_.

1. In row _[457](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=457:457)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[458](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=458:458)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[458](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=458:458)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[459](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=459:459)_, no term id was found for the name/label _right posterior body of uterus_.

1. In row _[459](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=459:459)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[460](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=460:460)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[460](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=460:460)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[461](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=461:461)_, no term id was found for the name/label _right posterior fundus of uterus_.

1. In row _[461](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=461:461)_, no term id was found for the name/label _luminal epithelial cell_.

1. In row _[462](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=462:462)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[462](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=462:462)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[462](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=462:462)_, no term id was found for the name/label _glandular epithelial cell_.

1. In row _[463](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=463:463)_, no term id was found for the name/label _lower uterine segment_.

1. In row _[463](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=463:463)_, no term id was found for the name/label _right posterior lower uterine segment_.

1. In row _[463](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=463:463)_, no term id was found for the name/label _luminal epithelial cell_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[12](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=12:12)_, the term _FMA:70195_ is from another ontology that is not validated in this process.

1. In row _[24](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=24:24)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[27](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=27:27)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[30](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=30:30)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[33](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=33:33)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[45](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=45:45)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[48](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=48:48)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[70](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=70:70)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[71](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=71:71)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[72](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=72:72)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[73](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=73:73)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[74](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=74:74)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[75](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=75:75)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[76](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=76:76)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[77](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=77:77)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[78](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=78:78)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[79](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=79:79)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[80](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=80:80)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[81](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=81:81)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[82](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=82:82)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[83](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=83:83)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[84](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=84:84)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[85](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=85:85)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[86](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=86:86)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[87](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=87:87)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[88](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=88:88)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[89](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=89:89)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[130](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=130:130)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[131](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=131:131)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[132](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=132:132)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[133](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=133:133)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[134](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=134:134)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[135](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=135:135)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[136](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=136:136)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[137](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=137:137)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[138](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=138:138)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[139](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=139:139)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[140](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=140:140)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[141](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=141:141)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[142](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=142:142)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[143](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=143:143)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[144](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=144:144)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[145](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=145:145)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[146](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=146:146)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[147](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=147:147)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[148](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=148:148)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[149](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=149:149)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[190](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=190:190)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[191](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=191:191)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[192](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=192:192)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[193](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=193:193)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[194](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=194:194)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[195](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=195:195)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[196](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=196:196)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[197](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=197:197)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[198](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=198:198)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[199](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=199:199)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[200](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=200:200)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[201](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=201:201)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[202](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=202:202)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[203](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=203:203)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[204](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=204:204)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[205](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=205:205)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[206](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=206:206)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[207](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=207:207)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[208](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=208:208)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[209](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=209:209)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[250](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=250:250)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[251](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=251:251)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[252](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=252:252)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[253](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=253:253)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[254](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=254:254)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[255](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=255:255)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[256](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=256:256)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[257](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=257:257)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[258](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=258:258)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[259](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=259:259)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[260](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=260:260)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[261](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=261:261)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[262](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=262:262)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[263](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=263:263)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[264](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=264:264)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[265](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=265:265)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[266](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=266:266)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[267](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=267:267)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[268](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=268:268)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[269](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=269:269)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[310](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=310:310)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[311](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=311:311)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[312](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=312:312)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[313](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=313:313)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[314](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=314:314)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[315](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=315:315)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[316](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=316:316)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[317](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=317:317)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[318](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=318:318)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[319](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=319:319)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[320](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=320:320)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[321](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=321:321)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[322](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=322:322)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[323](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=323:323)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[324](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=324:324)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[325](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=325:325)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[326](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=326:326)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[327](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=327:327)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[328](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=328:328)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[329](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=329:329)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[370](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=370:370)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[371](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=371:371)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[372](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=372:372)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[373](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=373:373)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[374](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=374:374)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[375](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=375:375)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[376](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=376:376)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[377](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=377:377)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[378](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=378:378)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[379](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=379:379)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[380](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=380:380)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[381](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=381:381)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[382](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=382:382)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[383](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=383:383)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[384](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=384:384)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[385](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=385:385)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[386](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=386:386)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[387](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=387:387)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[388](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=388:388)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[389](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=389:389)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[411](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=411:411)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[414](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=414:414)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[417](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=417:417)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[420](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=420:420)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[423](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=423:423)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[426](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=426:426)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[430](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=430:430)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[431](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=431:431)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[436](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=436:436)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[437](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=437:437)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[442](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=442:442)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[443](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=443:443)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[448](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=448:448)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[449](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=449:449)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[454](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=454:454)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[455](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=455:455)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[460](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=460:460)_, the term _FMA:17561_ is from another ontology that is not validated in this process.

1. In row _[461](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=461:461)_, the term _FMA:17561_ is from another ontology that is not validated in this process.


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



|    | s              | slabel                           | user_slabel                      | o              | olabel                     | user_olabel              | row_number                                                                                                                  |    deltaIC |
|----|----------------|----------------------------------|----------------------------------|----------------|----------------------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------|
|  0 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [440](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=440:440) |  17.9387   |
|  1 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [435](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=435:435) |  17.9387   |
|  2 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [437](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=437:437) |  17.9387   |
|  3 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [438](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=438:438) |  17.9387   |
|  4 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [439](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=439:439) |  17.9387   |
|  5 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [441](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=441:441) |  17.9387   |
|  6 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [442](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=442:442) |  17.9387   |
|  7 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [443](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=443:443) |  17.9387   |
|  8 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [444](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=444:444) |  17.9387   |
|  9 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [445](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=445:445) |  17.9387   |
| 10 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [446](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=446:446) |  17.9387   |
| 11 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [447](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=447:447) |  17.9387   |
| 12 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [448](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=448:448) |  17.9387   |
| 13 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [449](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=449:449) |  17.9387   |
| 14 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [450](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=450:450) |  17.9387   |
| 15 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [451](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=451:451) |  17.9387   |
| 16 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [452](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=452:452) |  17.9387   |
| 17 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [453](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=453:453) |  17.9387   |
| 18 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [454](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=454:454) |  17.9387   |
| 19 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [455](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=455:455) |  17.9387   |
| 20 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [456](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=456:456) |  17.9387   |
| 21 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [457](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=457:457) |  17.9387   |
| 22 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [458](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=458:458) |  17.9387   |
| 23 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [459](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=459:459) |  17.9387   |
| 24 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [460](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=460:460) |  17.9387   |
| 25 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [461](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=461:461) |  17.9387   |
| 26 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [462](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=462:462) |  17.9387   |
| 27 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [436](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=436:436) |  17.9387   |
| 28 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [463](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=463:463) |  17.9387   |
| 29 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [429](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=429:429) |  17.9387   |
| 30 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [433](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=433:433) |  17.9387   |
| 31 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [432](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=432:432) |  17.9387   |
| 32 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [428](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=428:428) |  17.9387   |
| 33 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [431](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=431:431) |  17.9387   |
| 34 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [434](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=434:434) |  17.9387   |
| 35 | UBERON:0002451 | endometrial gland                | endometrial gland                | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [430](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=430:430) |  17.9387   |
| 36 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [425](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=425:425) |  13.7747   |
| 37 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [423](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=423:423) |  13.7747   |
| 38 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [422](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=422:422) |  13.7747   |
| 39 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [421](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=421:421) |  13.7747   |
| 40 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [420](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=420:420) |  13.7747   |
| 41 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [419](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=419:419) |  13.7747   |
| 42 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [417](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=417:417) |  13.7747   |
| 43 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [418](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=418:418) |  13.7747   |
| 44 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [416](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=416:416) |  13.7747   |
| 45 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [415](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=415:415) |  13.7747   |
| 46 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [414](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=414:414) |  13.7747   |
| 47 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [413](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=413:413) |  13.7747   |
| 48 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [412](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=412:412) |  13.7747   |
| 49 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [424](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=424:424) |  13.7747   |
| 50 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [410](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=410:410) |  13.7747   |
| 51 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [426](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=426:426) |  13.7747   |
| 52 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [427](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=427:427) |  13.7747   |
| 53 | UBERON:0002337 | endometrial stroma               | endometrial stroma               | UBERON:0022355 | basal layer of endometrium | stratum basalis          | [411](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=411:411) |  13.7747   |
| 54 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [448](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=448:448) |   0.427518 |
| 55 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [440](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=440:440) |   0.427518 |
| 56 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [462](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=462:462) |   0.427518 |
| 57 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [436](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=436:436) |   0.427518 |
| 58 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [432](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=432:432) |   0.427518 |
| 59 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [460](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=460:460) |   0.427518 |
| 60 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [438](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=438:438) |   0.427518 |
| 61 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [458](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=458:458) |   0.427518 |
| 62 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [456](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=456:456) |   0.427518 |
| 63 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [430](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=430:430) |   0.427518 |
| 64 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [450](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=450:450) |   0.427518 |
| 65 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [442](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=442:442) |   0.427518 |
| 66 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [444](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=444:444) |   0.427518 |
| 67 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [454](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=454:454) |   0.427518 |
| 68 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [428](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=428:428) |   0.427518 |
| 69 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [446](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=446:446) |   0.427518 |
| 70 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [452](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=452:452) |   0.427518 |
| 71 | UBERON:0012276 | endometrium glandular epithelium | endometrium glandular epithelium | UBERON:0002451 | endometrial gland          | endometrial gland        | [434](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=434:434) |   0.427518 |
| 72 | UBERON:0008889 | uterine venous plexus            | uterine venous plexsus           | UBERON:0000995 | uterus                     | Uterus                   | [13](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=13:13)    | nan        |
| 73 | UBERON:0012332 | broad ligament of uterus         | broad ligament of uterus         | UBERON:0000995 | uterus                     | Uterus                   | [21](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=21:21)    | nan        |
| 74 | UBERON:0012332 | broad ligament of uterus         | broad ligament of uterus         | UBERON:0000995 | uterus                     | Uterus                   | [22](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=22:22)    | nan        |
| 75 | UBERON:0002493 | uterine artery                   | uterine artery                   | UBERON:0012332 | broad ligament of uterus   | broad ligament of uterus | [22](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=22:22)    | nan        |
| 76 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [429](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=429:429) | nan        |
| 77 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [431](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=431:431) | nan        |
| 78 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [433](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=433:433) | nan        |
| 79 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [435](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=435:435) | nan        |
| 80 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [437](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=437:437) | nan        |
| 81 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [439](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=439:439) | nan        |
| 82 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [441](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=441:441) | nan        |
| 83 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [443](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=443:443) | nan        |
| 84 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [445](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=445:445) | nan        |
| 85 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [447](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=447:447) | nan        |
| 86 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [449](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=449:449) | nan        |
| 87 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [451](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=451:451) | nan        |
| 88 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [453](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=453:453) | nan        |
| 89 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [455](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=455:455) | nan        |
| 90 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [457](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=457:457) | nan        |
| 91 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [459](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=459:459) | nan        |
| 92 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [461](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=461:461) | nan        |
| 93 | UBERON:0011949 | endometrium luminal epithelium   | endometrium luminal epithelium   | UBERON:0002451 | endometrial gland          | endometrial gland        | [463](https://docs.google.com/spreadsheets/d/1Ei-scFQ5N-giPMm9_TKt3-hAFPveAyibCCulXDTBbig/edit#gid=603441642&range=463:463) | nan        |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.








# New CL terms
[**Report**](new_cl_terms_Uterus.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Uterus.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Uterus_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Uterus_AS_has_part_CT_log.tsv)