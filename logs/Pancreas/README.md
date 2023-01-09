
ASCT+B Validation Reports for Pancreas (2023-01-09)
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
  
1. In row _45_, the term _[UBERON:0002384](http://purl.obolibrary.org/obo/UBERON_0002384)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _connective tissue
_ and the one in the ontology is _connective tissue_. For reference, the given name/label by SMEs is _Interlobular connective tissue_. Please correct it in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _16_, no term id was found for the name/label _Low columnar epithelial cell_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _17_, no term id was found for the name/label _Low columnar epithelial cell_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _18_, no term id was found for the name/label _Nonmucinous cuboidal epithelial cell_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _19_, no term id was found for the name/label _Flat epithelial cells_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _24_, no term id was found for the name/label _Tall columnar epithelial cell_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _38_, no term id was found for the name/label _M1-like macrophage_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _39_, no term id was found for the name/label _M2-like macrophage_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _41_, no term id was found for the name/label _Activated stellate cell_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _42_, no term id was found for the name/label _Quiescent stellate cell_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request.  
  
1. In row _47_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _47_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _48_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _48_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _49_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _49_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _50_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _50_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _51_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _51_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _52_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _52_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _53_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _53_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _54_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _54_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _55_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _55_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _56_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _56_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _57_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _57_, the term _FMA:14517_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Pancreas_log.tsv)
## Relationship CT-CT report
[**Report**](class_Pancreas_log.tsv)
## Relationship CT-AS report
[**Report**](Pancreas_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Pancreas.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Pancreas.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Pancreas_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Pancreas_AS_has_part_CT_log.tsv)