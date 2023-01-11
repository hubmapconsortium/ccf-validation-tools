---
comments: true
---

ASCT+B Validation Reports for Eye (2023-01-11)
==============================================

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
  
1. In row _[34](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=34:34)_, the term _[UBERON:0004864](http://purl.obolibrary.org/obo/UBERON_0004864)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _retinal vasculature_ and the one in the ontology is _vasculature of retina_. For reference, the given name/label by SMEs is _vasculature_. Please correct it in the ASCT+B table.

1. In row _[52](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=52:52)_, the term _[UBERON:0001782](http://purl.obolibrary.org/obo/UBERON_0001782)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _retinal pigmented epithelium_ and the one in the ontology is _pigmented layer of retina_. For reference, the given name/label by SMEs is _retinal pigmented epithelium_. Please correct it in the ASCT+B table.

1. In row _[50](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=50:50)_, the term _[CL:0000669](http://purl.obolibrary.org/obo/CL_0000669)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _pericyte cell_ and the one in the ontology is _pericyte_. For reference, the given name/label by SMEs is _Pericyte_. Please correct it in the ASCT+B table.

1. In row _[38](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=38:38)_, the term _[UBERON:0000965](http://purl.obolibrary.org/obo/UBERON_0000965)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _lens_ and the one in the ontology is _lens of camera-type eye_. For reference, the given name/label by SMEs is _lens_. Please correct it in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[13](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=13:13)_, no term id was found for the name/label _glutamic acid decarboxylase 65 cell_.

1. In row _[14](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=14:14)_, no term id was found for the name/label _A8 bistratified small-field cell_.

1. In row _[15](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=15:15)_, no term id was found for the name/label _medium-field cell_.

1. In row _[15](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=15:15)_, no term id was found for the name/label _medium-field cell_.

1. In row _[15](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=15:15)_, no term id was found for the name/label _wide field cell_.

1. In row _[15](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=15:15)_, no term id was found for the name/label _medium-field cell_.

1. In row _[16](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=16:16)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[16](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=16:16)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[16](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=16:16)_, no term id was found for the name/label _semilunar type 1 cell_.

1. In row _[16](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=16:16)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=17:17)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=17:17)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=17:17)_, no term id was found for the name/label _semilunar type 3 cell_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=17:17)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=18:18)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=18:18)_, no term id was found for the name/label _polyaxonal amacrine cell_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=18:18)_, no term id was found for the name/label _A2 cell_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=18:18)_, no term id was found for the name/label _A2 cell_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=18:18)_, no term id was found for the name/label _semilunar cell_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=18:18)_, no term id was found for the name/label _A2 cell_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=19:19)_, no term id was found for the name/label _starburst amacrine cell_.

1. In row _[21](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=21:21)_, no term id was found for the name/label _blue cone bipolar cell_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=22:22)_, no term id was found for the name/label _Diffuse bipolar 1 (DB1)_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=23:23)_, no term id was found for the name/label _Diffuse bipolar 2 cell_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=24:24)_, no term id was found for the name/label _Diffuse bipolar 3a cell_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=25:25)_, no term id was found for the name/label _Diffuse bipolar 3b cell_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=26:26)_, no term id was found for the name/label _Diffuse bipolar 4 cell_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=27:27)_, no term id was found for the name/label _Diffuse bipolar 6 cell_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=28:28)_, no term id was found for the name/label _Flat midget bipolar cell_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=29:29)_, no term id was found for the name/label _invaginating bipolar cell_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=46:46)_, no term id was found for the name/label _Inner cortex_.

1. In row _[47](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=47:47)_, no term id was found for the name/label _Outer cortex_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=53:53)_, no term id was found for the name/label _Outer cortex_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=53:53)_, no term id was found for the name/label _Outer cortex_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[14](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=14:14)_, the term _FMA:62362_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _[14](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=14:14)_, the term _FMA:62362_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _[14](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=14:14)_, the term _FMA:62362_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _[35](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=35:35)_, the term _FMA:62360_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.

1. In row _[36](https://docs.google.com/spreadsheets/d/1qx6ljQipIYEjm9HoDweulJoRq4saKXGv16S5en8O4Rs/edit#gid=695483621&range=36:36)_, the term _FMA:67916_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon. Please search for synonyms in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl) to replace these terms.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Eye_log.tsv)
## Relationship CT-CT report
[**Report**](class_Eye_log.tsv)
## Relationship CT-AS report
[**Report**](Eye_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Eye.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Eye.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Eye_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Eye_AS_has_part_CT_log.tsv)