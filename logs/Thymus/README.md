
ASCT+B Validation Reports for Thymus (2022-11-30)
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
  
1. In row _30_, the term _[CL:0009081](http://purl.obolibrary.org/obo/CL_0009081)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _specified double negative thymocyte_ and the one in the ontology is _specified double negative thymocyte (Homo sapiens)_. For reference, the given name/label by SMEs is _double negative thymocyte 2_. Please correct it in the ASCT+B table.

1. In row _78_, the term _[CL:0000914](http://purl.obolibrary.org/obo/CL_0000914)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _immature NKT cell_ and the one in the ontology is _immature NK T cell_. For reference, the given name/label by SMEs is _immature NKT cell_. Please correct it in the ASCT+B table.

1. In row _31_, the term _[CL:0009082](http://purl.obolibrary.org/obo/CL_0009082)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _committed double negative thymocyte_ and the one in the ontology is _committed double negative thymocyte (Homo sapiens)_. For reference, the given name/label by SMEs is _double negative thymocyte 3_. Please correct it in the ASCT+B table.

1. In row _32_, the term _[CL:0009083](http://purl.obolibrary.org/obo/CL_0009083)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _rearranging double negative thymocyte_ and the one in the ontology is _rearranging double negative thymocyte (Homo sapiens)_. For reference, the given name/label by SMEs is _double negative thymocyte 4_. Please correct it in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
- No issues found.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request.  
  
- No issues found.


# Relationship reports

## Relationship AS-AS report
[**Report**](../logs/Thymus/class_Thymus_log.tsv)
## Relationship CT-CT report
[**Report**](../logs/Thymus/class_Thymus_log.tsv)
## Relationship CT-AS report
[**Report**](../logs/Thymus/Thymus_AS__CT_strict_log.tsv)
# New CL terms
[**Report**](../logs/Thymus/new_cl_terms_Thymus.tsv)
# New UBERON terms
[**Report**](../logs/Thymus/new_uberon_terms_Thymus.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](../logs/Thymus/class_Thymus_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](../logs/Thymus/Thymus_AS_has_part_CT_log.tsv)