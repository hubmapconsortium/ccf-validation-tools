
ASCT+B Validation Reports for Knee (2023-03-08)
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
  
1. In row _[38](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=38:38)_, the term _[CL:0000669](http://purl.obolibrary.org/obo/CL_0000669)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _pericyte cell_ and the one in the ontology is _pericyte_. For reference, the given name/label by SMEs is _pericyte cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[24](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=24:24)_, the term _[UBERON:0010996](http://purl.obolibrary.org/obo/UBERON_0010996)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Superior Articular Cartilage_ and the one in the ontology is _articular cartilage of joint_. For reference, the given name/label by SMEs is _Articular cartilage of a joint_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[12](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=12:12)_, no term id was found for the name/label _proximal tibia_.

1. In row _[12](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=12:12)_, no term id was found for the name/label _proximal tibia_.

1. In row _[13](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=13:13)_, no term id was found for the name/label _proximal fibula_.

1. In row _[13](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=13:13)_, no term id was found for the name/label _proximal fibula_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=24:24)_, no term id was found for the name/label _Superficial Zone_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=25:25)_, no term id was found for the name/label _Transitional Zone_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=25:25)_, no term id was found for the name/label _Deep Superficial_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=26:26)_, no term id was found for the name/label _Rounded Chondrocytes_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=27:27)_, no term id was found for the name/label _Deep Zone_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=28:28)_, no term id was found for the name/label _Tidemark_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=28:28)_, no term id was found for the name/label _Prehypertrophic Chondrocytes_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=30:30)_, no term id was found for the name/label _Subchondral Bone_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=30:30)_, no term id was found for the name/label _Residual Hypertrophic Chondrocytes_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=33:33)_, no term id was found for the name/label _Bone lIning Cells_.

1. In row _[35](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=35:35)_, no term id was found for the name/label _Preosteoclasts_.

1. In row _[37](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=37:37)_, no term id was found for the name/label _vascular endothelial cells_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=38:38)_, no term id was found for the name/label _perivascular cells_.

1. In row _[40](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=40:40)_, no term id was found for the name/label _sinusoidal cells_.

1. In row _[41](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=41:41)_, no term id was found for the name/label _autonomic neuronal cells_.

1. In row _[42](https://docs.google.com/spreadsheets/d/1v3BfUp55Ty8Bl9ufHursLN9hXmyRcj0MHDbEpPwgFZc/edit#gid=1815525900&range=42:42)_, no term id was found for the name/label _Marrow Adipocytes_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
- No issues found.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Knee_log.tsv)
## Relationship CT-CT report
[**Report**](class_Knee_log.tsv)
## Relationship CT-AS report
[**Report**](Knee_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Knee.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Knee.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Knee_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Knee_AS_has_part_CT_log.tsv)