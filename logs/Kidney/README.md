
ASCT+B Validation Reports for Kidney (2023-01-24)
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
  
1. In row _[42](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=42:42)_, the term _[UBERON:0005097](http://purl.obolibrary.org/obo/UBERON_0005097)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _connecting tubule_ and the one in the ontology is _renal connecting tubule_. For reference, the given name/label by SMEs is _Connecting Tubule_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[13](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=13:13)_, the term _[UBERON:0006852](http://purl.obolibrary.org/obo/UBERON_0006852)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _glomerular visceral epithelium_ and the one in the ontology is _obsolete glomerular visceral epithelium_. For reference, the given name/label by SMEs is _visceral epithelial layer_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[46](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=46:46)_, the term _[CL:4030021](http://purl.obolibrary.org/obo/CL_4030021)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _connecting tubule intercalated cell type B_ and the one in the ontology is _kidney connecting tubule beta-intercalated cell_. For reference, the given name/label by SMEs is _Intercalated Cell Type B_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[40](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=40:40)_, the term _[CL:4030016](http://purl.obolibrary.org/obo/CL_4030016)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _distal convoluted tubule cell type 1_ and the one in the ontology is _epithelial cell of early distal convoluted tubule_. For reference, the given name/label by SMEs is _Distal Convoluted Tubule Cell Type 1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[31](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=31:31)_, the term _[CL:4030012](http://purl.obolibrary.org/obo/CL_4030012)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _descending thin limb cell type 1_ and the one in the ontology is _kidney loop of Henle short descending thin limb epithelial cell_. For reference, the given name/label by SMEs is _Descending Thin Limb Cell Type 1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[17](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=17:17)_, the term _[UBERON:0001289](http://purl.obolibrary.org/obo/UBERON_0001289)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _descending thin limb of loop of Henle_ and the one in the ontology is _descending limb of loop of Henle_. For reference, the given name/label by SMEs is _Loop of Henle (Thin Limb)_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[43](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=43:43)_, the term _[CL:4030018](http://purl.obolibrary.org/obo/CL_4030018)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _connecting tubule principal cell_ and the one in the ontology is _kidney connecting tubule principal cell_. For reference, the given name/label by SMEs is _Connecting Tubule Principal Cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[34](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=34:34)_, the term _[UBERON:0004193](http://purl.obolibrary.org/obo/UBERON_0004193)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _ascending thin limb of loop of Henle_ and the one in the ontology is _loop of Henle ascending limb thin segment_. For reference, the given name/label by SMEs is _Loop of Henle (Thin Limb)_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[33](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=33:33)_, the term _[CL:4030014](http://purl.obolibrary.org/obo/CL_4030014)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Descending Thin Limb Cell Type 3_ and the one in the ontology is _kidney loop of Henle long descending thin limb inner medulla epithelial cell_. For reference, the given name/label by SMEs is _Descending Thin Limb Cell Type 3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[20](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=20:20)_, the term _[UBERON:0001284](http://purl.obolibrary.org/obo/UBERON_0001284)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _renal column (column of Bertin)_ and the one in the ontology is _renal column_. For reference, the given name/label by SMEs is _renal column_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[70](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=70:70)_, the term _[CL:4030022](http://purl.obolibrary.org/obo/CL_4030022)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _medullary fibroblast_ and the one in the ontology is _renal medullary fibroblast_. For reference, the given name/label by SMEs is _Medullary Fibroblast_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[45](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=45:45)_, the term _[CL:4030020](http://purl.obolibrary.org/obo/CL_4030020)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _connecting tubule intercalated cell type A_ and the one in the ontology is _kidney connecting tubule alpha-intercalated cell_. For reference, the given name/label by SMEs is _Connecting Tubule Intercalated Cell Type A_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[44](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=44:44)_, the term _[CL:4030019](http://purl.obolibrary.org/obo/CL_4030019)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _connecting tubule intercalated cell_ and the one in the ontology is _kidney connecting tubule intercalated cell_. For reference, the given name/label by SMEs is _Connecting Tubule Intercalated Cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[59](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=59:59)_, the term _[CL:0000115](http://purl.obolibrary.org/obo/CL_0000115)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _endothlial cell_ and the one in the ontology is _endothelial cell_. For reference, the given name/label by SMEs is _Endothelial Cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[13](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=13:13)_, the term _[CL:0000653](http://purl.obolibrary.org/obo/CL_0000653)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _glomerular visceral epithelial cell_ and the one in the ontology is _podocyte_. For reference, the given name/label by SMEs is _Podocyte_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[41](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=41:41)_, the term _[CL:4030017](http://purl.obolibrary.org/obo/CL_4030017)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _distal convoluted tubule cell type 2_ and the one in the ontology is _epithelial cell of late distal convoluted tubule_. For reference, the given name/label by SMEs is _Distal Convoluted Tubule Cell Type 2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[24](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=24:24)_, the term _[UBERON:0004190](http://purl.obolibrary.org/obo/UBERON_0004190)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _glomerulus vasculature_ and the one in the ontology is _renal glomerulus vasculature_. For reference, the given name/label by SMEs is _Glomerulus Vasculature_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[54](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=54:54)_, the term _[CL:4030015](http://purl.obolibrary.org/obo/CL_4030015)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _collecting duct intercalated cell type A_ and the one in the ontology is _kidney collecting duct alpha-intercalated cell_. For reference, the given name/label by SMEs is _Collecting Duct Intercalated Cell Type A_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[32](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=32:32)_, the term _[CL:4030013](http://purl.obolibrary.org/obo/CL_4030013)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Descending Thin Limb Cell Type 2_ and the one in the ontology is _kidney loop of Henle long descending thin limb outer medulla epithelial cell_. For reference, the given name/label by SMEs is _Descending Thin Limb Cell Type 2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[12](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=12:12)_, no term id was found for the name/label _capsule mesenchymal stromal cell_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=17:17)_, no term id was found for the name/label _descending thin limb of loop of Henle 2_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=17:17)_, no term id was found for the name/label _Descending Thin Limb Cell Type 2_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=31:31)_, no term id was found for the name/label _descending thin limb of loop of Henle 1_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=32:32)_, no term id was found for the name/label _descending thin limb of loop of Henle 2_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=33:33)_, no term id was found for the name/label _descending thin limb of loop of Henle 3_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=52:52)_, no term id was found for the name/label _Transitional principal-intercalated cell_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=60:60)_, no term id was found for the name/label _Endothelium/Juxtaglomerular apparatus_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=60:60)_, no term id was found for the name/label _Endothelium/Juxtaglomerular apparatus_.

1. In row _[61](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=61:61)_, no term id was found for the name/label _Endothelium/Juxtaglomerular apparatus_.

1. In row _[61](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=61:61)_, no term id was found for the name/label _Endothelium/Juxtaglomerular apparatus_.

1. In row _[63](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=63:63)_, no term id was found for the name/label _Endothelium (non glomerular)_.

1. In row _[63](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=63:63)_, no term id was found for the name/label _Endothelium (non glomerular)_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=64:64)_, no term id was found for the name/label _Endothelium (non glomerular)_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=64:64)_, no term id was found for the name/label _Endothelium (non glomerular)_.

1. In row _[65](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=65:65)_, no term id was found for the name/label _Endothelium (non glomerular)_.

1. In row _[65](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=65:65)_, no term id was found for the name/label _Endothelium (non glomerular)_.

1. In row _[67](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=67:67)_, no term id was found for the name/label _Vascular Smooth Muscle Cell_.

1. In row _[72](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=72:72)_, no term id was found for the name/label _Immune_.

1. In row _[73](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=73:73)_, no term id was found for the name/label _Immune_.

1. In row _[74](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=74:74)_, no term id was found for the name/label _Immune_.

1. In row _[75](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=75:75)_, no term id was found for the name/label _Immune_.

1. In row _[76](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=76:76)_, no term id was found for the name/label _Immune_.

1. In row _[77](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=77:77)_, no term id was found for the name/label _Immune_.

1. In row _[78](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=78:78)_, no term id was found for the name/label _Immune_.

1. In row _[79](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=79:79)_, no term id was found for the name/label _Immune_.

1. In row _[80](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=80:80)_, no term id was found for the name/label _Immune_.

1. In row _[80](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=80:80)_, no term id was found for the name/label _Monocyte Derived Cell_.

1. In row _[81](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=81:81)_, no term id was found for the name/label _Immune_.

1. In row _[82](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=82:82)_, no term id was found for the name/label _Immune_.

1. In row _[83](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=83:83)_, no term id was found for the name/label _Immune_.

1. In row _[84](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=84:84)_, no term id was found for the name/label _Immune_.

1. In row _[85](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=85:85)_, no term id was found for the name/label _Immune_.

1. In row _[86](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=86:86)_, no term id was found for the name/label _Immune_.

1. In row _[87](https://docs.google.com/spreadsheets/d/1NMfu1bEGNFcTYTFT-jCao_lSbFD8n0ti630iIpRj-hw/edit#gid=949267305&range=87:87)_, no term id was found for the name/label _Papillary Tip Epithelium_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
- No issues found.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Kidney_log.tsv)
## Relationship CT-CT report
[**Report**](class_Kidney_log.tsv)
## Relationship CT-AS report
[**Report**](Kidney_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Kidney.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Kidney.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Kidney_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Kidney_AS_has_part_CT_log.tsv)