
ASCT+B Validation Reports for Kidney (2023-01-09)
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
  
1. In row _42_, the term _[UBERON:0005097](http://purl.obolibrary.org/obo/UBERON_0005097)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _connecting tubule_ and the one in the ontology is _renal connecting tubule_. For reference, the given name/label by SMEs is _Connecting Tubule_. Please correct it in the ASCT+B table.

1. In row _33_, the term _[CL:4030014](http://purl.obolibrary.org/obo/CL_4030014)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Descending Thin Limb Cell Type 3_ and the one in the ontology is _kidney loop of Henle long descending thin limb inner medulla epithelial cell_. For reference, the given name/label by SMEs is _Descending Thin Limb Cell Type 3_. Please correct it in the ASCT+B table.

1. In row _59_, the term _[CL:0000115](http://purl.obolibrary.org/obo/CL_0000115)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _endothlial cell_ and the one in the ontology is _endothelial cell_. For reference, the given name/label by SMEs is _Endothelial Cell_. Please correct it in the ASCT+B table.

1. In row _17_, the term _[UBERON:0001289](http://purl.obolibrary.org/obo/UBERON_0001289)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _descending thin limb of loop of Henle_ and the one in the ontology is _descending limb of loop of Henle_. For reference, the given name/label by SMEs is _Loop of Henle (Thin Limb)_. Please correct it in the ASCT+B table.

1. In row _20_, the term _[UBERON:0001284](http://purl.obolibrary.org/obo/UBERON_0001284)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _renal column (column of Bertin)_ and the one in the ontology is _renal column_. For reference, the given name/label by SMEs is _renal column_. Please correct it in the ASCT+B table.

1. In row _31_, the term _[CL:4030012](http://purl.obolibrary.org/obo/CL_4030012)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _descending thin limb cell type 1_ and the one in the ontology is _kidney loop of Henle short descending thin limb epithelial cell_. For reference, the given name/label by SMEs is _Descending Thin Limb Cell Type 1_. Please correct it in the ASCT+B table.

1. In row _46_, the term _[CL:4030021](http://purl.obolibrary.org/obo/CL_4030021)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _connecting tubule intercalated cell type B_ and the one in the ontology is _kidney connecting tubule beta-intercalated cell_. For reference, the given name/label by SMEs is _Intercalated Cell Type B_. Please correct it in the ASCT+B table.

1. In row _70_, the term _[CL:4030022](http://purl.obolibrary.org/obo/CL_4030022)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _medullary fibroblast_ and the one in the ontology is _renal medullary fibroblast_. For reference, the given name/label by SMEs is _Medullary Fibroblast_. Please correct it in the ASCT+B table.

1. In row _54_, the term _[CL:4030015](http://purl.obolibrary.org/obo/CL_4030015)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _collecting duct intercalated cell type A_ and the one in the ontology is _kidney collecting duct alpha-intercalated cell_. For reference, the given name/label by SMEs is _Collecting Duct Intercalated Cell Type A_. Please correct it in the ASCT+B table.

1. In row _34_, the term _[UBERON:0004193](http://purl.obolibrary.org/obo/UBERON_0004193)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _ascending thin limb of loop of Henle_ and the one in the ontology is _loop of Henle ascending limb thin segment_. For reference, the given name/label by SMEs is _Loop of Henle (Thin Limb)_. Please correct it in the ASCT+B table.

1. In row _44_, the term _[CL:4030019](http://purl.obolibrary.org/obo/CL_4030019)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _connecting tubule intercalated cell_ and the one in the ontology is _kidney connecting tubule intercalated cell_. For reference, the given name/label by SMEs is _Connecting Tubule Intercalated Cell_. Please correct it in the ASCT+B table.

1. In row _41_, the term _[CL:4030017](http://purl.obolibrary.org/obo/CL_4030017)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _distal convoluted tubule cell type 2_ and the one in the ontology is _epithelial cell of late distal convoluted tubule_. For reference, the given name/label by SMEs is _Distal Convoluted Tubule Cell Type 2_. Please correct it in the ASCT+B table.

1. In row _45_, the term _[CL:4030020](http://purl.obolibrary.org/obo/CL_4030020)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _connecting tubule intercalated cell type A_ and the one in the ontology is _kidney connecting tubule alpha-intercalated cell_. For reference, the given name/label by SMEs is _Connecting Tubule Intercalated Cell Type A_. Please correct it in the ASCT+B table.

1. In row _13_, the term _[CL:0000653](http://purl.obolibrary.org/obo/CL_0000653)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _glomerular visceral epithelial cell_ and the one in the ontology is _podocyte_. For reference, the given name/label by SMEs is _Podocyte_. Please correct it in the ASCT+B table.

1. In row _40_, the term _[CL:4030016](http://purl.obolibrary.org/obo/CL_4030016)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _distal convoluted tubule cell type 1_ and the one in the ontology is _epithelial cell of early distal convoluted tubule_. For reference, the given name/label by SMEs is _Distal Convoluted Tubule Cell Type 1_. Please correct it in the ASCT+B table.

1. In row _13_, the term _[UBERON:0006852](http://purl.obolibrary.org/obo/UBERON_0006852)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _glomerular visceral epithelium_ and the one in the ontology is _obsolete glomerular visceral epithelium_. For reference, the given name/label by SMEs is _visceral epithelial layer_. Please correct it in the ASCT+B table.

1. In row _43_, the term _[CL:4030018](http://purl.obolibrary.org/obo/CL_4030018)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _connecting tubule principal cell_ and the one in the ontology is _kidney connecting tubule principal cell_. For reference, the given name/label by SMEs is _Connecting Tubule Principal Cell_. Please correct it in the ASCT+B table.

1. In row _24_, the term _[UBERON:0004190](http://purl.obolibrary.org/obo/UBERON_0004190)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _glomerulus vasculature_ and the one in the ontology is _renal glomerulus vasculature_. For reference, the given name/label by SMEs is _Glomerulus Vasculature_. Please correct it in the ASCT+B table.

1. In row _32_, the term _[CL:4030013](http://purl.obolibrary.org/obo/CL_4030013)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Descending Thin Limb Cell Type 2_ and the one in the ontology is _kidney loop of Henle long descending thin limb outer medulla epithelial cell_. For reference, the given name/label by SMEs is _Descending Thin Limb Cell Type 2_. Please correct it in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _12_, no term id was found for the name/label _capsule mesenchymal stromal cell_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _17_, no term id was found for the name/label _descending thin limb of loop of Henle 2_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _17_, no term id was found for the name/label _Descending Thin Limb Cell Type 2_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _31_, no term id was found for the name/label _descending thin limb of loop of Henle 1_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _32_, no term id was found for the name/label _descending thin limb of loop of Henle 2_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _33_, no term id was found for the name/label _descending thin limb of loop of Henle 3_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _52_, no term id was found for the name/label _Transitional principal-intercalated cell_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _60_, no term id was found for the name/label _Endothelium/Juxtaglomerular apparatus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _60_, no term id was found for the name/label _Endothelium/Juxtaglomerular apparatus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _61_, no term id was found for the name/label _Endothelium/Juxtaglomerular apparatus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _61_, no term id was found for the name/label _Endothelium/Juxtaglomerular apparatus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _63_, no term id was found for the name/label _Endothelium (non glomerular)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _63_, no term id was found for the name/label _Endothelium (non glomerular)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _64_, no term id was found for the name/label _Endothelium (non glomerular)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _64_, no term id was found for the name/label _Endothelium (non glomerular)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _65_, no term id was found for the name/label _Endothelium (non glomerular)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _65_, no term id was found for the name/label _Endothelium (non glomerular)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _67_, no term id was found for the name/label _Vascular Smooth Muscle Cell_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _72_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _73_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _74_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _75_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _76_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _77_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _78_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _79_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _80_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _80_, no term id was found for the name/label _Monocyte Derived Cell_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _81_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _82_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _83_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _84_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _85_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _86_, no term id was found for the name/label _Immune_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _87_, no term id was found for the name/label _Papillary Tip Epithelium_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request.  
  
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