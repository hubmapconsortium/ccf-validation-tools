---
comments: true
---

ASCT+B Validation Reports for Skin (2022-11-30)
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
  
- No issues found.


## Typos or punctuation mistakes


This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.  
  
- No issues found.


## Different labels


This report provides a list of terms having different names/labels found in the ontology and related to the one found in the ASCT+B table. Make sure to add the term's name/label in the column AS/N/LABEL or CT/N/LABEL. If the SME wants to give another name/label, please use the column AS/N or CT/N. N is the number in the column.

If the term's name/label and the name/label given by SME are too different, please make sure the term ID and its name/label are matching in OLS.

If the name/label in the ontology contains *obsolete*, please look into OLS, clicking on the term ID, for its replacement.  
  
1. In row _50_, the term _[CL:0000359](http://purl.obolibrary.org/obo/CL_0000359)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _smooth muscle cell_ and the one in the ontology is _vascular associated smooth muscle cell_. For reference, the given name/label by SMEs is _Perivascular smooth muscle cell_. Please correct it in the ASCT+B table.

1. In row _52_, the term _[CL:0000669](http://purl.obolibrary.org/obo/CL_0000669)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _pericyte cell_ and the one in the ontology is _pericyte_. For reference, the given name/label by SMEs is _Pericyte_. Please correct it in the ASCT+B table.

1. In row _24_, the term _[CL:0000151](http://purl.obolibrary.org/obo/CL_0000151)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _sebum secreting cell_ and the one in the ontology is _secretory cell_. For reference, the given name/label by SMEs is _Germinative (epithelial) cell, Sebocyte_. Please correct it in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _22_, no term id was found for the name/label _Keratinocyte (Onychocyte)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _48_, no term id was found for the name/label _perineurial cells_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _68_, no term id was found for the name/label _Perineural cell_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request.  
  
- No issues found.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Skin_log.tsv)
## Relationship CT-CT report
[**Report**](class_Skin_log.tsv)
## Relationship CT-AS report
[**Report**](Skin_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Skin.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Skin.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Skin_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Skin_AS_has_part_CT_log.tsv)