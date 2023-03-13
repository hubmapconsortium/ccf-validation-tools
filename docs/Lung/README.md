
ASCT+B Validation Reports for Lung (2023-03-13)
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
  
1. CL:4033005

1. CL:4033007

1. CL:4033008

1. CL:00008775

1. CL:4033003

1. CL:10019018

1. CL:4033009

1. CL:4033010


## Typos or punctuation mistakes


This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.  
  
- No issues found.


## Different labels


This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.

If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.

If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.  
  
1. In row _[12](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=12:12)_, the term _[UBERON:0007196](http://purl.obolibrary.org/obo/UBERON_0007196)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _tracheobronchial tree _ and the one in the ontology is _tracheobronchial tree_. For reference, the given name/label by SMEs is _tracheobronchial tree _. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[152](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=152:152)_, the term _[CL:0002619](http://purl.obolibrary.org/obo/CL_0002619)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _adult endothelial progenitor cells_ and the one in the ontology is _adult endothelial progenitor cell_. For reference, the given name/label by SMEs is _endothelial progenitor cells_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[171](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=171:171)_, the term _[CL:0002394](http://purl.obolibrary.org/obo/CL_0002394)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _CD141-postive myeloid dendritic cell_ and the one in the ontology is _CD141-positive myeloid dendritic cell_. For reference, the given name/label by SMEs is _cDC1 CD141-positive myeloid dendritic cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[57](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=57:57)_, the term _[UBERON:0008886](http://purl.obolibrary.org/obo/UBERON_0008886)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _pulmonary vascular system _ and the one in the ontology is _pulmonary vascular system_. For reference, the given name/label by SMEs is _pulmonary vascular system _. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[57](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=57:57)_, the term _[UBERON:0008886](http://purl.obolibrary.org/obo/UBERON_0008886)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _vascular system_ and the one in the ontology is _pulmonary vascular system_. For reference, the given name/label by SMEs is _vascular system_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[159](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=159:159)_, the term _[CL:0000945](http://purl.obolibrary.org/obo/CL_0000945)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _lymphocyte of B cell lineage_ and the one in the ontology is _lymphocyte of B lineage_. For reference, the given name/label by SMEs is _lymphocyte of B cell lineage_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[135](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=135:135)_, the term _[CL:1000350](http://purl.obolibrary.org/obo/CL_1000350)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _basal cell of epithelium of terminal  bronchiole_ and the one in the ontology is _basal cell of epithelium of terminal bronchiole_. For reference, the given name/label by SMEs is _basal cell of epithelium of terminal  bronchiole_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[152](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=152:152)_, the term _[CL:0000566](http://purl.obolibrary.org/obo/CL_0000566)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _angiobalstic mesenchymal cell_ and the one in the ontology is _angioblastic mesenchymal cell_. For reference, the given name/label by SMEs is _angiobalstic mesenchymal cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[22](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=22:22)_, the term _[CL:0000313](http://purl.obolibrary.org/obo/CL_0000313)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _serous secreting cells_ and the one in the ontology is _serous secreting cell_. For reference, the given name/label by SMEs is _submucosal gland serous cells_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[18](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=18:18)_, no term id was found for the name/label _terminal ciliated ducts of tracheal submucosal gland_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=19:19)_, no term id was found for the name/label _terminal ciliated ducts of tracheal submucosal gland_.

1. In row _[20](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=20:20)_, no term id was found for the name/label _collecting ducts of tracheal submucosal gland_.

1. In row _[21](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=21:21)_, no term id was found for the name/label _mucous tubules of tracheal submucosal gland_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=22:22)_, no term id was found for the name/label _distal acini of tracheal submucosal gland_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=23:23)_, no term id was found for the name/label _myoepithelium tracheal submucosal gland_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=26:26)_, no term id was found for the name/label _perichondrial fibroblasts_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=36:36)_, no term id was found for the name/label _airway deuterosomal cell_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=38:38)_, no term id was found for the name/label _suprabasal cell_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=39:39)_, no term id was found for the name/label _airway deuterosomal cell_.

1. In row _[50](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=50:50)_, no term id was found for the name/label _ciliated ducts of bronchial submucosal gland_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=51:51)_, no term id was found for the name/label _ciliated ducts of bronchial submucosal gland_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=64:64)_, no term id was found for the name/label _airway deuterosomal cell_.

1. In row _[66](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=66:66)_, no term id was found for the name/label _suprabasal cell_.

1. In row _[67](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=67:67)_, no term id was found for the name/label _airway deuterosomal cell_.

1. In row _[79](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=79:79)_, no term id was found for the name/label _ciliated ducts of bronchial submucosal gland_.

1. In row _[80](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=80:80)_, no term id was found for the name/label _ciliated ducts of bronchial submucosal gland_.

1. In row _[88](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=88:88)_, no term id was found for the name/label _airway deuterosomal cell _.

1. In row _[90](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=90:90)_, no term id was found for the name/label _suprabasal cell_.

1. In row _[91](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=91:91)_, no term id was found for the name/label _airway deuterosomal cell_.

1. In row _[105](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=105:105)_, no term id was found for the name/label _airway deuterosomal cell _.

1. In row _[107](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=107:107)_, no term id was found for the name/label _suprabasal cell_.

1. In row _[108](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=108:108)_, no term id was found for the name/label _airway deuterosomal cell_.

1. In row _[122](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=122:122)_, no term id was found for the name/label _ciliated ducts of bronchial submucosal gland_.

1. In row _[123](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=123:123)_, no term id was found for the name/label _ciliated ducts of bronchial submucosal gland_.

1. In row _[130](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=130:130)_, no term id was found for the name/label _bronchiolar smooth muscle cell_.

1. In row _[134](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=134:134)_, no term id was found for the name/label _bronchiolar smooth muscle cell_.

1. In row _[137](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=137:137)_, no term id was found for the name/label _bronchiolar smooth muscle cell_.

1. In row _[145](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=145:145)_, no term id was found for the name/label _secondary crest myofibroblasts_.

1. In row _[151](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=151:151)_, no term id was found for the name/label _Pulmonary Vein endotheliim_.

1. In row _[152](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=152:152)_, no term id was found for the name/label _Pulmonary Vein endotheliim_.

1. In row _[162](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=162:162)_, no term id was found for the name/label _pulmonary alveolus_.

1. In row _[163](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=163:163)_, no term id was found for the name/label _pulmonary alveolus_.

1. In row _[163](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=163:163)_, no term id was found for the name/label _alveolar macrophage proliferating_.

1. In row _[164](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=164:164)_, no term id was found for the name/label _pulmonary alveolus_.

1. In row _[164](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=164:164)_, no term id was found for the name/label _alveolar macrophage CCL3+_.

1. In row _[165](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=165:165)_, no term id was found for the name/label _pulmonary alveolus_.

1. In row _[165](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=165:165)_, no term id was found for the name/label _alveolar macrophage MT-positive_.

1. In row _[168](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=168:168)_, no term id was found for the name/label _lung megakaryocyte_.

1. In row _[174](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=174:174)_, no term id was found for the name/label _migratory dendritic cell_.

1. In row _[179](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=179:179)_, no term id was found for the name/label _CD4+ T cell resident memory_.

1. In row _[181](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=181:181)_, no term id was found for the name/label _CD8+ T cell resident memory_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[18](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=18:18)_, the term _LMHA:00142_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[19](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=19:19)_, the term _LMHA:00087_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[20](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=20:20)_, the term _LMHA:00693_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[21](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=21:21)_, the term _LMHA:00238_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[50](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=50:50)_, the term _LMHA:00142_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[51](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=51:51)_, the term _LMHA:00087_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[52](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=52:52)_, the term _LMHA:00693_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[53](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=53:53)_, the term _LMHA:00238_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[79](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=79:79)_, the term _LMHA:00142_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[80](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=80:80)_, the term _LMHA:00087_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[81](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=81:81)_, the term _LMHA:00693_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[82](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=82:82)_, the term _LMHA:00238_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[103](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=103:103)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[103](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=103:103)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[104](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=104:104)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[104](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=104:104)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[105](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=105:105)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[105](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=105:105)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[106](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=106:106)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[106](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=106:106)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[107](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=107:107)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[107](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=107:107)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[108](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=108:108)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[108](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=108:108)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[109](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=109:109)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[109](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=109:109)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[110](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=110:110)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[110](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=110:110)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[111](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=111:111)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[111](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=111:111)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[112](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=112:112)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[112](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=112:112)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[113](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=113:113)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[113](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=113:113)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[114](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=114:114)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[114](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=114:114)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[115](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=115:115)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[115](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=115:115)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[116](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=116:116)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[117](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=117:117)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[118](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=118:118)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[119](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=119:119)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[122](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=122:122)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[122](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=122:122)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[122](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=122:122)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[122](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=122:122)_, the term _LMHA:00142_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[123](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=123:123)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[123](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=123:123)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[123](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=123:123)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[123](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=123:123)_, the term _LMHA:00087_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[124](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=124:124)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[124](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=124:124)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[124](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=124:124)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[124](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=124:124)_, the term _LMHA:00693_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[125](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=125:125)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[125](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=125:125)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[125](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=125:125)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[125](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=125:125)_, the term _LMHA:00238_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[126](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=126:126)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[126](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=126:126)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[126](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=126:126)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[127](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=127:127)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[127](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=127:127)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[127](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=127:127)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[128](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=128:128)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[128](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=128:128)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[128](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=128:128)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[129](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=129:129)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[129](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=129:129)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[129](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=129:129)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[130](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=130:130)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[130](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=130:130)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[130](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=130:130)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[131](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=131:131)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[131](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=131:131)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[131](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=131:131)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[132](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=132:132)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[132](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=132:132)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[132](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=132:132)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[133](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=133:133)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[133](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=133:133)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[133](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=133:133)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[134](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=134:134)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[134](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=134:134)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[134](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=134:134)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[135](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=135:135)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[135](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=135:135)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[135](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=135:135)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[136](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=136:136)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[136](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=136:136)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[136](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=136:136)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[137](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=137:137)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[137](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=137:137)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[137](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=137:137)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[138](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=138:138)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[138](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=138:138)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[138](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=138:138)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[139](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=139:139)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[139](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=139:139)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[139](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=139:139)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[140](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=140:140)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[140](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=140:140)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[140](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=140:140)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[141](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=141:141)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[141](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=141:141)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[141](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=141:141)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[142](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=142:142)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[142](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=142:142)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[142](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=142:142)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[143](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=143:143)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[143](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=143:143)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[143](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=143:143)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[144](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=144:144)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[144](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=144:144)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[144](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=144:144)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[145](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=145:145)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[145](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=145:145)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[145](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=145:145)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[146](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=146:146)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[146](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=146:146)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[146](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=146:146)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[147](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=147:147)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[147](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=147:147)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[147](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=147:147)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[148](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=148:148)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[148](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=148:148)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[148](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=148:148)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[149](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=149:149)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[149](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=149:149)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[149](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=149:149)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[150](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=150:150)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[150](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=150:150)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[150](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=150:150)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[151](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=151:151)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[151](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=151:151)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[151](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=151:151)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[151](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=151:151)_, the term _FMA:84472_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[151](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=151:151)_, the term _FMA:76965_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[152](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=152:152)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[152](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=152:152)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[152](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=152:152)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[152](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=152:152)_, the term _FMA:84472_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[152](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=152:152)_, the term _FMA:76965_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[153](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=153:153)_, the term _FMA:7312_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[153](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=153:153)_, the term _FMA:7408_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[153](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=153:153)_, the term _FMA:323213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[153](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=153:153)_, the term _FMA:84472_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[161](https://docs.google.com/spreadsheets/d/1oo9v-77W1wPD6uLLEF0MxBHv_BCcJziiPFEfWZCW_QY/edit#gid=1523836586&range=161:161)_, the term _LMHA:00213_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Lung_log.tsv)
## Relationship CT-CT report
[**Report**](class_Lung_log.tsv)
## Relationship CT-AS report
[**Report**](Lung_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Lung.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Lung.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Lung_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Lung_AS_has_part_CT_log.tsv)