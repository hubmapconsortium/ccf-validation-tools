
ASCT+B Validation Reports
=========================

Table of contents
=================

* [Invalid terms](#invalid-terms)
	* [Typos or punctuation mistakes](#typos-or-punctuation-mistakes)
	* [Blank ontology ID](#blank-ontology-id)
	* [Different labels](#different-labels)
	* [Foundational models of anatomy ontology](#foundational-models-of-anatomy-ontology)
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


These are the reports related to issues in the terms found in the ASCT+B table. We validate only 
[CL](https://www.ebi.ac.uk/ols/ontologies/cl) and [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) terms.
## Typos or punctuation mistakes


This report provides a general quality check of the terms used in the ASCT+B table. Typos, font case (upper case), 
punctuation mistakes in IDs: two colons, spaces, underscore instead of a colon.
## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However,
 in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index)
## Different labels


This report provides a list of terms having different names found in the ontology and related to the one found in the 
ASCT+B table. Make sure to add the term's name in the column AS/N/LABEL or CT/N/LABEL. 
## Foundational models of anatomy ontology


This report provides a list of foundational models of anatomy ontology IDs provided when an adequate term is not found 
in Uberon. You can also request cross-database requests the same way a new term requests.##--[invalid_terms]--##
# Relationship reports

## Relationship AS-AS report
##--[as-as_report]--##
## Relationship CT-CT report
##--[ct-ct_report]--##
## Relationship CT-AS report
[**Report**](../logs/Kidney/Kidney_AS__CT_strict_log.tsv)
# New CL terms
##--[new_cl]--##
# New UBERON terms
##--[new_uberon]--##
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](../logs/Kidney/class_Kidney_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](../logs/Kidney/Kidney_AS_has_part_CT_log.tsv)