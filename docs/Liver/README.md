
ASCT+B Validation Reports for Liver (2023-02-20)
================================================

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
  
1. In row _[28](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=28:28)_, the term _[CL:0002196](http://purl.obolibrary.org/obo/CL_0002196)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Hepatic oval cell_ and the one in the ontology is _hepatic oval stem cell_. For reference, the given name/label by SMEs is _hepatic oval cell _. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[32](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=32:32)_, the term _[CL:0001056](http://purl.obolibrary.org/obo/CL_0001056)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _human Dendritic cell_ and the one in the ontology is _dendritic cell, human_. For reference, the given name/label by SMEs is _conventional Dendritic cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[24](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=24:24)_, the term _[CL:0000526](http://purl.obolibrary.org/obo/CL_0000526)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _afferent neuron cell_ and the one in the ontology is _afferent neuron_. For reference, the given name/label by SMEs is _neuron cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[37](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=37:37)_, the term _[CL:0000624](http://purl.obolibrary.org/obo/CL_0000624)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _CD4 positive alpha beta_ and the one in the ontology is _CD4-positive, alpha-beta T cell_. For reference, the given name/label by SMEs is _CD4+T cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[39](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=39:39)_, the term _[CL:0001203](http://purl.obolibrary.org/obo/CL_0001203)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _CD8 positiver alpha beta memory T cell CD45RO +_ and the one in the ontology is _CD8-positive, alpha-beta memory T cell, CD45RO-positive_. For reference, the given name/label by SMEs is _CD8+ Liver-Resident Memory T cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[30](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=30:30)_, the term _[CL:0002138](http://purl.obolibrary.org/obo/CL_0002138)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _lymphatic endothelial cell_ and the one in the ontology is _endothelial cell of lymphatic vessel_. For reference, the given name/label by SMEs is _hepatic lymphatic endothelial cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[34](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=34:34)_, the term _[CL:0002399](http://purl.obolibrary.org/obo/CL_0002399)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _CD1c+ myeloid dendritic cell_ and the one in the ontology is _CD1c-positive myeloid dendritic cell_. For reference, the given name/label by SMEs is _Conventional DC 2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[38](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=38:38)_, the term _[CL:0000798](http://purl.obolibrary.org/obo/CL_0000798)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _gamma delta T cell_ and the one in the ontology is _gamma-delta T cell_. For reference, the given name/label by SMEs is _gamma delta T cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[15](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=15:15)_, no term id was found for the name/label _Immune cell_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=24:24)_, no term id was found for the name/label _nerve_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=27:27)_, no term id was found for the name/label _portal fibroblast_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=29:29)_, no term id was found for the name/label _hepatic progenitor cell_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=30:30)_, no term id was found for the name/label _lymphatic vessel_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=32:32)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=33:33)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[34](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=34:34)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[35](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=35:35)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=36:36)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=36:36)_, no term id was found for the name/label _CD8 TRm (residence memory)_.

1. In row _[37](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=37:37)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=38:38)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=39:39)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[40](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=40:40)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[41](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=41:41)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[41](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=41:41)_, no term id was found for the name/label _Eomes low Liver NK cell_.

1. In row _[42](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=42:42)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[42](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=42:42)_, no term id was found for the name/label _TBet low Liver NK cell_.

1. In row _[43](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=43:43)_, no term id was found for the name/label _Liver immune resident component_.

1. In row _[44](https://docs.google.com/spreadsheets/d/1U1UFN1m7fkWj-UgYDNTCfGZUv-opzCjEEYypihDjjSQ/edit#gid=1694828397&range=44:44)_, no term id was found for the name/label _Liver immune resident component_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
- No issues found.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Liver_log.tsv)
## Relationship CT-CT report
[**Report**](class_Liver_log.tsv)
## Relationship CT-AS report
[**Report**](Liver_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Liver.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Liver.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Liver_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Liver_AS_has_part_CT_log.tsv)