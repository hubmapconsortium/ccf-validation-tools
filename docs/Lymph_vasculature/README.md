---
comments: true
---

ASCT+B Validation Reports for Lymph_vasculature (2022-11-30)
============================================================

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
  
- No issues found.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _43_, no term id was found for the name/label _medial lymphatic pathway of upper arm_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _46_, no term id was found for the name/label _lateral lymphatic pathway of upper arm_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _47_, no term id was found for the name/label _subclavicular lymph node_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _48_, no term id was found for the name/label _subclavicular lymph node_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _48_, no term id was found for the name/label _subclavicular lymph node_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _48_, no term id was found for the name/label _lateral lymphatic pathway of upper arm #2_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _48_, no term id was found for the name/label _subclavicular lymph node_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request.  
  
1. In row _12_, the term _FMA:5832_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _13_, the term _FMA:5832_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _13_, the term _FMA:5832_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _13_, the term _FMA:5831_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _13_, the term _FMA:5832_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _14_, the term _FMA:5832_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _14_, the term _FMA:5832_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _14_, the term _FMA:12251_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _14_, the term _FMA:5832_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _15_, the term _FMA:5832_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _15_, the term _FMA:5832_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _15_, the term _FMA:5830_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _15_, the term _FMA:5832_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _17_, the term _FMA:9585_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _19_, the term _FMA:5841_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _20_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _21_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _21_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _21_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _21_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _22_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _22_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _22_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _22_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _22_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _22_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _23_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _23_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _23_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _23_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _23_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _23_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _24_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _24_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _24_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _24_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _24_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _24_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _25_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _25_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _25_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _25_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _25_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _25_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _25_, the term _FMA:71813_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _25_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _26_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _26_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _26_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _26_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _26_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _26_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _26_, the term _FMA:71813_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _26_, the term _FMA:71813_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _26_, the term _FMA:71841_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _26_, the term _FMA:71813_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _27_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _27_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _27_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _27_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _27_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _27_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _28_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _28_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _28_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _28_, the term _FMA:5842_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _28_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _28_, the term _FMA:323951_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _29_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _29_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _30_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _30_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _31_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _31_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _32_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _32_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _33_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _33_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _34_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _34_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _35_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _35_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _35_, the term _FMA:233577_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _35_, the term _FMA:12765_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _36_, the term _FMA:5840_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _37_, the term _FMA:12250_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _38_, the term _FMA:5834_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _39_, the term _FMA:5032_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _40_, the term _FMA:5033_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _41_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _42_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _42_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _42_, the term _FMA:71749_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _42_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _43_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _43_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _43_, the term _FMA:71749_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _43_, the term _FMA:71749_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _43_, the term _FMA:71749_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _44_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _44_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _44_, the term _FMA:234912_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _44_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _45_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _45_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _45_, the term _FMA:234912_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _45_, the term _FMA:234912_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _46_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _46_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _46_, the term _FMA:234912_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _46_, the term _FMA:234912_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _47_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _47_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _47_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _48_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _48_, the term _FMA:12252_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Lymph_vasculature_log.tsv)
## Relationship CT-CT report
[**Report**](class_Lymph_vasculature_log.tsv)
## Relationship CT-AS report
[**Report**](Lymph_vasculature_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Lymph_vasculature.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Lymph_vasculature.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Lymph_vasculature_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Lymph_vasculature_AS_has_part_CT_log.tsv)