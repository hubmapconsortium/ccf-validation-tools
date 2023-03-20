
ASCT+B Validation Reports for Bone-Marrow (2023-03-20)
======================================================

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
  
1. In row _[33](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=33:33)_, the term _[CL:0000037](http://purl.obolibrary.org/obo/CL_0000037)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _hemopoietic stem cell_ and the one in the ontology is _hematopoietic stem cell_. For reference, the given name/label by SMEs is _hemopoietic stem cell (HSC)_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[55](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=55:55)_, the term _[CL:0000938](http://purl.obolibrary.org/obo/CL_0000938)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _CD16-negative, CD56-bright natural killer cell_ and the one in the ontology is _CD16-negative, CD56-bright natural killer cell, human_. For reference, the given name/label by SMEs is _CD56 bright Natural Killer_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[34](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=34:34)_, no term id was found for the name/label _lympho-myeloid progenitor cell (LMPP)_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=39:39)_, no term id was found for the name/label _Myeloid progenitor (MOP)_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=52:52)_, no term id was found for the name/label _CD8 T cell effector memory_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1z60ZA9r8Y435skSIjRwMX_EgBK0FN9up4CFfBQ0s944/edit#gid=771476671&range=54:54)_, no term id was found for the name/label _mature CD8 T cell_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
- No issues found.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Bone-Marrow_log.tsv)
## Relationship CT-CT report
[**Report**](class_Bone-Marrow_log.tsv)
## Relationship CT-AS report
[**Report**](Bone-Marrow_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Bone-Marrow.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Bone-Marrow.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Bone-Marrow_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Bone-Marrow_AS_has_part_CT_log.tsv)