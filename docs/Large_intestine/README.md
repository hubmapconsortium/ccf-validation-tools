
ASCT+B Validation Reports for Large_intestine (2023-03-20)
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
  
1. In row _[15](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=15:15)_, the term _[CL:0009009](http://purl.obolibrary.org/obo/CL_0009009)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _paneth cell of epithelium of large intestine_ and the one in the ontology is _paneth cell of colon_. For reference, the given name/label by SMEs is _Paneth_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[89](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=89:89)_, the term _[CL:1000279](http://purl.obolibrary.org/obo/CL_1000279)_ has different name/label in the source ontology. The name/label in the ASCT+B table is __ and the one in the ontology is _smooth muscle cell of large intestine_. For reference, the given name/label by SMEs is _muscle_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[1196](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1196:1196)_, the term _[UBERON:0015716](http://purl.obolibrary.org/obo/UBERON_0015716)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _epithelium_ and the one in the ontology is _anal canal epithelium_. For reference, the given name/label by SMEs is _epithelium_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[19](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=19:19)_, the term _[CL:0009011](http://purl.obolibrary.org/obo/CL_0009011)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _transit amplifying cell of large intestine_ and the one in the ontology is _transit amplifying cell of colon_. For reference, the given name/label by SMEs is _transient amplifying cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[31](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=31:31)_, the term _[CL:0000669](http://purl.obolibrary.org/obo/CL_0000669)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _pericyte cell_ and the one in the ontology is _pericyte_. For reference, the given name/label by SMEs is _pericyte_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[330](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=330:330)_, the term _[UBERON:0012498](http://purl.obolibrary.org/obo/UBERON_0012498)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _serosa_ and the one in the ontology is _serosa of appendix_. For reference, the given name/label by SMEs is _serosa_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[119](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=119:119)_, the term _[UBERON:0001153](http://purl.obolibrary.org/obo/UBERON_0001153)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _cecum_ and the one in the ontology is _caecum_. For reference, the given name/label by SMEs is _cecum_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[1213](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1213:1213)_, the term _[CL:0000240](http://purl.obolibrary.org/obo/CL_0000240)_ has different name/label in the source ontology. The name/label in the ASCT+B table is __ and the one in the ontology is _stratified squamous epithelial cell_. For reference, the given name/label by SMEs is _squamous_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[436](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=436:436)_, the term _[UBERON:0012419](http://purl.obolibrary.org/obo/UBERON_0012419)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _tenia coli_ and the one in the ontology is _taenia coli_. For reference, the given name/label by SMEs is _tenia coli_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[436](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=436:436)_, the term _[CL:0000192](http://purl.obolibrary.org/obo/CL_0000192)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _smooth muscle_ and the one in the ontology is _smooth muscle cell_. For reference, the given name/label by SMEs is _smooth muscle_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[1196](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1196:1196)_, the term _[CL:0000244](http://purl.obolibrary.org/obo/CL_0000244)_ has different name/label in the source ontology. The name/label in the ASCT+B table is __ and the one in the ontology is _transitional epithelial cell_. For reference, the given name/label by SMEs is _transitional_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[1211](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1211:1211)_, the term _[CL:0000146](http://purl.obolibrary.org/obo/CL_0000146)_ has different name/label in the source ontology. The name/label in the ASCT+B table is __ and the one in the ontology is _simple columnar epithelial cell_. For reference, the given name/label by SMEs is _columnar_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[1323](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1323:1323)_, the term _[UBERON:0000423](http://purl.obolibrary.org/obo/UBERON_0000423)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _eccrine (sweat) gland_ and the one in the ontology is _eccrine sweat gland_. For reference, the given name/label by SMEs is _eccrine (sweat) gland_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[1211](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1211:1211)_, the term _[UBERON:0004760](http://purl.obolibrary.org/obo/UBERON_0004760)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _anal gland_ and the one in the ontology is _gland of anal canal_. For reference, the given name/label by SMEs is _anal gland_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[27](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=27:27)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=28:28)_, no term id was found for the name/label _pericryptal fibroblastic sheath_.

1. In row _[35](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=35:35)_, no term id was found for the name/label _ganglion_.

1. In row _[83](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=83:83)_, no term id was found for the name/label _ganglion_.

1. In row _[85](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=85:85)_, no term id was found for the name/label _ganglion_.

1. In row _[87](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=87:87)_, no term id was found for the name/label _ganglion_.

1. In row _[97](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=97:97)_, no term id was found for the name/label _ganglion_.

1. In row _[134](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=134:134)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[135](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=135:135)_, no term id was found for the name/label _pericryptal fibroblastic sheath_.

1. In row _[142](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=142:142)_, no term id was found for the name/label _ganglion_.

1. In row _[189](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=189:189)_, no term id was found for the name/label _ganglion_.

1. In row _[191](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=191:191)_, no term id was found for the name/label _ganglion_.

1. In row _[193](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=193:193)_, no term id was found for the name/label _ganglion_.

1. In row _[203](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=203:203)_, no term id was found for the name/label _ganglion_.

1. In row _[240](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=240:240)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[241](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=241:241)_, no term id was found for the name/label _pericryptal fibroblastic sheath_.

1. In row _[248](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=248:248)_, no term id was found for the name/label _ganglion_.

1. In row _[295](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=295:295)_, no term id was found for the name/label _ganglion_.

1. In row _[297](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=297:297)_, no term id was found for the name/label _ganglion_.

1. In row _[299](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=299:299)_, no term id was found for the name/label _ganglion_.

1. In row _[309](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=309:309)_, no term id was found for the name/label _ganglion_.

1. In row _[346](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=346:346)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[347](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=347:347)_, no term id was found for the name/label _pericryptal fibroblastic sheath_.

1. In row _[354](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=354:354)_, no term id was found for the name/label _ganglion_.

1. In row _[401](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=401:401)_, no term id was found for the name/label _ganglion_.

1. In row _[403](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=403:403)_, no term id was found for the name/label _ganglion_.

1. In row _[405](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=405:405)_, no term id was found for the name/label _ganglion_.

1. In row _[415](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=415:415)_, no term id was found for the name/label _ganglion_.

1. In row _[455](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=455:455)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[456](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=456:456)_, no term id was found for the name/label _pericryptal fibroblastic sheath_.

1. In row _[463](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=463:463)_, no term id was found for the name/label _ganglion_.

1. In row _[510](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=510:510)_, no term id was found for the name/label _ganglion_.

1. In row _[512](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=512:512)_, no term id was found for the name/label _ganglion_.

1. In row _[514](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=514:514)_, no term id was found for the name/label _ganglion_.

1. In row _[524](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=524:524)_, no term id was found for the name/label _ganglion_.

1. In row _[564](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=564:564)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[565](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=565:565)_, no term id was found for the name/label _pericryptal fibroblastic sheath_.

1. In row _[572](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=572:572)_, no term id was found for the name/label _ganglion_.

1. In row _[619](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=619:619)_, no term id was found for the name/label _ganglion_.

1. In row _[621](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=621:621)_, no term id was found for the name/label _ganglion_.

1. In row _[623](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=623:623)_, no term id was found for the name/label _ganglion_.

1. In row _[633](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=633:633)_, no term id was found for the name/label _ganglion_.

1. In row _[673](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=673:673)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[674](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=674:674)_, no term id was found for the name/label _pericryptal fibroblastic sheath_.

1. In row _[681](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=681:681)_, no term id was found for the name/label _ganglion_.

1. In row _[728](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=728:728)_, no term id was found for the name/label _ganglion_.

1. In row _[730](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=730:730)_, no term id was found for the name/label _ganglion_.

1. In row _[732](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=732:732)_, no term id was found for the name/label _ganglion_.

1. In row _[742](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=742:742)_, no term id was found for the name/label _ganglion_.

1. In row _[782](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=782:782)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[783](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=783:783)_, no term id was found for the name/label _pericryptal fibroblastic sheath_.

1. In row _[790](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=790:790)_, no term id was found for the name/label _ganglion_.

1. In row _[837](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=837:837)_, no term id was found for the name/label _ganglion_.

1. In row _[839](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=839:839)_, no term id was found for the name/label _ganglion_.

1. In row _[841](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=841:841)_, no term id was found for the name/label _ganglion_.

1. In row _[851](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=851:851)_, no term id was found for the name/label _ganglion_.

1. In row _[891](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=891:891)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[892](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=892:892)_, no term id was found for the name/label _pericryptal fibroblastic sheath_.

1. In row _[899](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=899:899)_, no term id was found for the name/label _ganglion_.

1. In row _[946](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=946:946)_, no term id was found for the name/label _ganglion_.

1. In row _[948](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=948:948)_, no term id was found for the name/label _ganglion_.

1. In row _[950](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=950:950)_, no term id was found for the name/label _ganglion_.

1. In row _[960](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=960:960)_, no term id was found for the name/label _ganglion_.

1. In row _[1000](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1000:1000)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[1001](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1001:1001)_, no term id was found for the name/label _pericryptal fibroblastic sheath_.

1. In row _[1008](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1008:1008)_, no term id was found for the name/label _ganglion_.

1. In row _[1055](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1055:1055)_, no term id was found for the name/label _ganglion_.

1. In row _[1057](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1057:1057)_, no term id was found for the name/label _ganglion_.

1. In row _[1059](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1059:1059)_, no term id was found for the name/label _ganglion_.

1. In row _[1069](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1069:1069)_, no term id was found for the name/label _ganglion_.

1. In row _[1106](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1106:1106)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[1107](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1107:1107)_, no term id was found for the name/label _pericryptal fibroblastic sheath_.

1. In row _[1114](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1114:1114)_, no term id was found for the name/label _ganglion_.

1. In row _[1161](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1161:1161)_, no term id was found for the name/label _ganglion_.

1. In row _[1163](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1163:1163)_, no term id was found for the name/label _ganglion_.

1. In row _[1165](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1165:1165)_, no term id was found for the name/label _ganglion_.

1. In row _[1175](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1175:1175)_, no term id was found for the name/label _ganglion_.

1. In row _[1203](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1203:1203)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[1210](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1210:1210)_, no term id was found for the name/label _ganglion_.

1. In row _[1222](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1222:1222)_, no term id was found for the name/label _ganglion_.

1. In row _[1224](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1224:1224)_, no term id was found for the name/label _ganglion_.

1. In row _[1226](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1226:1226)_, no term id was found for the name/label _ganglion_.

1. In row _[1236](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1236:1236)_, no term id was found for the name/label _ganglion_.

1. In row _[1266](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1266:1266)_, no term id was found for the name/label _subepithelial membrane_.

1. In row _[1273](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1273:1273)_, no term id was found for the name/label _ganglion_.

1. In row _[1282](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1282:1282)_, no term id was found for the name/label _ganglion_.

1. In row _[1284](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1284:1284)_, no term id was found for the name/label _ganglion_.

1. In row _[1286](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1286:1286)_, no term id was found for the name/label _ganglion_.

1. In row _[1296](https://docs.google.com/spreadsheets/d/1zzyJg9zL_mbSfcqXWNbQgf9KMsxZViVgugm79H9fUp8/edit#gid=2043181688&range=1296:1296)_, no term id was found for the name/label _ganglion_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
- No issues found.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Large_intestine_log.tsv)
## Relationship CT-CT report
[**Report**](class_Large_intestine_log.tsv)
## Relationship CT-AS report
[**Report**](Large_intestine_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Large_intestine.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Large_intestine.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Large_intestine_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Large_intestine_AS_has_part_CT_log.tsv)