
ASCT+B Validation Reports for Placenta (2023-10-06)
===================================================

Table of contents
=================

* [Invalid terms](#invalid-terms)
	* [Terms not found](#terms-not-found)
	* [Typos or punctuation mistakes](#typos-or-punctuation-mistakes)
	* [Different labels](#different-labels)
	* [Blank ontology ID](#blank-ontology-id)
	* [Blank ontology ID missing parent](#blank-ontology-id-missing-parent)
	* [Terms from another ontology](#terms-from-another-ontology)
* [Relationship reports](#relationship-reports)
	* [How to read a table entry](#how-to-read-a-table-entry)
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


This report provides a list of terms not found neither in UBERON nor in CL. Please remove these terms from the ASCT+B table - disconsider this message if a term was recently added to the ontology.  
  
1. UBERON:8600021

1. UBERON:8600019

1. UBERON:8600020


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

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
1. No term id was found for the name/label _placental disc_ in the following 73 rows _[19](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=19:19)_, _[22](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=22:22)_, _[23](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=23:23)_, _[39](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=39:39)_, _[40](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=40:40)_, _[41](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=41:41)_, _[42](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=42:42)_, _[43](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=43:43)_, _[44](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=44:44)_, _[45](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=45:45)_, _[46](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=46:46)_, _[47](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=47:47)_, _[48](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=48:48)_, _[49](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=49:49)_, _[50](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=50:50)_, _[51](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=51:51)_, _[52](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=52:52)_, _[53](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=53:53)_, _[54](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=54:54)_, _[55](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=55:55)_, _[56](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=56:56)_, _[57](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=57:57)_, _[58](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=58:58)_, _[59](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=59:59)_, _[60](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=60:60)_, _[61](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=61:61)_, _[62](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=62:62)_, _[63](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=63:63)_, _[64](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=64:64)_, _[65](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=65:65)_, _[66](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=66:66)_, _[67](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=67:67)_, _[68](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=68:68)_, _[69](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=69:69)_, _[70](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=70:70)_, _[71](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=71:71)_, _[72](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=72:72)_, _[73](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=73:73)_, _[74](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=74:74)_, _[75](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=75:75)_, _[76](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=76:76)_, _[77](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=77:77)_, _[78](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=78:78)_, _[79](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=79:79)_, _[80](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=80:80)_, _[81](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=81:81)_, _[82](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=82:82)_, _[83](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=83:83)_, _[84](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=84:84)_, _[85](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=85:85)_, _[86](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=86:86)_, _[87](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=87:87)_, _[88](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=88:88)_, _[89](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=89:89)_, _[90](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=90:90)_, _[91](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=91:91)_, _[92](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=92:92)_, _[93](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=93:93)_, _[94](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=94:94)_, _[95](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=95:95)_, _[96](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=96:96)_, _[97](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=97:97)_, _[98](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=98:98)_, _[99](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=99:99)_, _[100](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=100:100)_, _[101](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=101:101)_, _[102](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=102:102)_, _[103](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=103:103)_, _[104](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=104:104)_, _[105](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=105:105)_, _[106](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=106:106)_, _[107](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=107:107)_, _[108](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=108:108)_.

1. No term id was found for the name/label _interstitial extravillous trophoblast_ in the following 1 row _[19](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=19:19)_.

1. No term id was found for the name/label _chorionic mesoderm (from chorion)_ in the following 1 row _[24](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=24:24)_.

1. No term id was found for the name/label _chorionic ectoderm (from chorion)_ in the following 2 rows _[25](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=25:25)_, _[26](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=26:26)_.

1. No term id was found for the name/label _uterine macrophage_ in the following 3 rows _[30](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=30:30)_, _[62](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=62:62)_, _[102](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=102:102)_.

1. No term id was found for the name/label _endovascular extravillous trophoblast_ in the following 3 rows _[35](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=35:35)_, _[67](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=67:67)_, _[107](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=107:107)_.

1. No term id was found for the name/label _endometrial lymphatic vessel_ in the following 3 rows _[36](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=36:36)_, _[68](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=68:68)_, _[108](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=108:108)_.

1. No term id was found for the name/label _chorionic mesoderm (from chorionic plate)_ in the following 4 rows _[39](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=39:39)_, _[49](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=49:49)_, _[50](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=50:50)_, _[51](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=51:51)_.

1. No term id was found for the name/label _chorionic ectoderm (from chorionic plate)_ in the following 18 rows _[40](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=40:40)_, _[41](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=41:41)_, _[42](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=42:42)_, _[52](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=52:52)_, _[53](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=53:53)_, _[54](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=54:54)_, _[69](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=69:69)_, _[70](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=70:70)_, _[71](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=71:71)_, _[77](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=77:77)_, _[78](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=78:78)_, _[79](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=79:79)_, _[85](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=85:85)_, _[86](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=86:86)_, _[87](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=87:87)_, _[92](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=92:92)_, _[93](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=93:93)_, _[94](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=94:94)_.

1. No term id was found for the name/label _trophoblast island_ in the following 5 rows _[43](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=43:43)_, _[44](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=44:44)_, _[45](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=45:45)_, _[46](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=46:46)_, _[47](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=47:47)_.

1. No term id was found for the name/label _anchoring villus_ in the following 7 rows _[52](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=52:52)_, _[53](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=53:53)_, _[54](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=54:54)_, _[55](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=55:55)_, _[56](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=56:56)_, _[57](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=57:57)_, _[58](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=58:58)_.

1. No term id was found for the name/label _villous mesenchyme_ in the following 10 rows _[55](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=55:55)_, _[56](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=56:56)_, _[72](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=72:72)_, _[73](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=73:73)_, _[80](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=80:80)_, _[81](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=81:81)_, _[88](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=88:88)_, _[89](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=89:89)_, _[95](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=95:95)_, _[96](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=96:96)_.

1. No term id was found for the name/label _villous capillary_ in the following 6 rows _[57](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=57:57)_, _[58](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=58:58)_, _[90](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=90:90)_, _[91](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=91:91)_, _[97](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=97:97)_, _[98](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=98:98)_.

1. No term id was found for the name/label _floating villus_ in the following 30 rows _[69](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=69:69)_, _[70](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=70:70)_, _[71](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=71:71)_, _[72](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=72:72)_, _[73](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=73:73)_, _[74](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=74:74)_, _[75](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=75:75)_, _[76](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=76:76)_, _[77](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=77:77)_, _[78](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=78:78)_, _[79](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=79:79)_, _[80](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=80:80)_, _[81](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=81:81)_, _[82](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=82:82)_, _[83](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=83:83)_, _[84](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=84:84)_, _[85](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=85:85)_, _[86](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=86:86)_, _[87](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=87:87)_, _[88](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=88:88)_, _[89](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=89:89)_, _[90](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=90:90)_, _[91](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=91:91)_, _[92](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=92:92)_, _[93](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=93:93)_, _[94](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=94:94)_, _[95](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=95:95)_, _[96](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=96:96)_, _[97](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=97:97)_, _[98](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=98:98)_.

1. No term id was found for the name/label _stem villus_ in the following 8 rows _[69](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=69:69)_, _[70](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=70:70)_, _[71](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=71:71)_, _[72](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=72:72)_, _[73](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=73:73)_, _[74](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=74:74)_, _[75](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=75:75)_, _[76](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=76:76)_.

1. No term id was found for the name/label _stem villous vessel_ in the following 3 rows _[74](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=74:74)_, _[75](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=75:75)_, _[76](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=76:76)_.

1. No term id was found for the name/label _immature intermediate villus_ in the following 8 rows _[77](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=77:77)_, _[78](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=78:78)_, _[79](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=79:79)_, _[80](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=80:80)_, _[81](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=81:81)_, _[82](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=82:82)_, _[83](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=83:83)_, _[84](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=84:84)_.

1. No term id was found for the name/label _mature intermediate villus_ in the following 7 rows _[85](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=85:85)_, _[86](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=86:86)_, _[87](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=87:87)_, _[88](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=88:88)_, _[89](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=89:89)_, _[90](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=90:90)_, _[91](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=91:91)_.

1. No term id was found for the name/label _terminal villus_ in the following 7 rows _[92](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=92:92)_, _[93](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=93:93)_, _[94](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=94:94)_, _[95](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=95:95)_, _[96](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=96:96)_, _[97](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=97:97)_, _[98](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=98:98)_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
- No issues found.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Same case for Anatomic Ontology for Human Lung Maturation (LMHA) and Interlex IDs (ILX) from Stimulating Peripheral Activity to Relieve Conditions (SPARC). You can request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
- No issues found.


# Relationship reports


These reports are other representations of the ASCT+B table. We split each row into pairs with adjacent terms, resulting in a table with two primary columns, object (o), left side and subject (s), right side. The experts' labels for the subject and object are in the columns user_slabel and user_olabel. The other columns are the subject label (s_label) and object label (o_label), the label from the source ontologies.

The report means it could not find a partonomy relationship in the source ontologies, but it doesn't mean this relationship is entirely invalid. In some cases, the pair is in the *inverse order*. In other cases, the relationship is *missing* in the source ontologies. Finally, how it was modelled in the ASCT+B table is not aligned with the ontologies sources and needs a more general discussion.
## How to read a table entry


**In the ASCT+B table**




|AS/2|AS/2/LABEL|AS/2/ID|AS/3|AS/3/LABEL|AS/3/ID|
| :---: | :---: | :---: | :---: | :---: | :---: |
|lens|lens|UBERON:0000965|ciliary zonules|suspensory ligament of lens|UBERON:0006762|






**In the Relationship Report**




|s|slabel|user_slabel|o|olabel|user_olabel|
| :---: | :---: | :---: | :---: | :---: | :---: |
|UBERON:0006762|suspensory ligament of lens|ciliary zonules|UBERON:0000965|lens|lens|





## Relationship AS-AS report


This table contains terms for anatomical structures that are related to each other according to the ASCT+B table but are not related to each other in source ontologies via one of the relation types we consider valid for ASCT+B tables. Valid relationships are: *part_of*, e.g. corneal endothelium part_of cornea; *subClassOf*, e.g. left kidney subClassOf (is_a) kidney; and *overlaps* (has some part in), e.g. ureter overlaps kidney; *connected_to*, e.g. TBA. *part_of* and *subClassOf* relationships should be specific to general, e.g. left kidney (specific) to kidney (general); corneal endothelium (specific) to cornea (general). The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



|    | s              | slabel            | user_slabel       | o              | olabel          | user_olabel     | row_number                                                                                                               |       deltaIC |
|----|----------------|-------------------|-------------------|----------------|-----------------|-----------------|--------------------------------------------------------------------------------------------------------------------------|---------------|
|  0 | UBERON:0000305 | amnion            | amnion            | UBERON:0002331 | umbilical cord  | umbilical cord  | [20](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=20:20) |   2.67779e+08 |
|  1 | UBERON:0000305 | amnion            | amnion            | UBERON:0002331 | umbilical cord  | umbilical cord  | [21](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=21:21) |   2.67779e+08 |
|  2 | UBERON:0000305 | amnion            | amnion            | UBERON:0005630 | fetal membrane  | fetal membranes | [37](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=37:37) |   2.67779e+08 |
|  3 | UBERON:0000305 | amnion            | amnion            | UBERON:0005630 | fetal membrane  | fetal membranes | [38](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=38:38) |   2.67779e+08 |
| 12 | UBERON:0002331 | umbilical cord    | umbilical cord    | UBERON:0001987 | placenta        | placenta        | [12](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=12:12) | nan           |
| 13 | UBERON:0002331 | umbilical cord    | umbilical cord    | UBERON:0001987 | placenta        | placenta        | [13](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=13:13) | nan           |
| 14 | UBERON:0002331 | umbilical cord    | umbilical cord    | UBERON:0001987 | placenta        | placenta        | [14](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=14:14) | nan           |
| 15 | UBERON:0002331 | umbilical cord    | umbilical cord    | UBERON:0001987 | placenta        | placenta        | [15](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=15:15) | nan           |
| 16 | UBERON:0002331 | umbilical cord    | umbilical cord    | UBERON:0001987 | placenta        | placenta        | [16](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=16:16) | nan           |
| 17 | UBERON:0002331 | umbilical cord    | umbilical cord    | UBERON:0001987 | placenta        | placenta        | [17](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=17:17) | nan           |
| 18 | UBERON:0002331 | umbilical cord    | umbilical cord    | UBERON:0001987 | placenta        | placenta        | [18](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=18:18) | nan           |
| 19 | UBERON:0002331 | umbilical cord    | umbilical cord    | UBERON:0001987 | placenta        | placenta        | [20](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=20:20) | nan           |
| 21 | UBERON:0002331 | umbilical cord    | umbilical cord    | UBERON:0001987 | placenta        | placenta        | [21](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=21:21) | nan           |
| 23 | UBERON:0003254 | amniotic ectoderm | amniotic ectoderm | UBERON:0004027 | chorionic plate | chorionic plate | [22](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=22:22) | nan           |
| 25 | UBERON:0003262 | amniotic mesoderm | amniotic mesoderm | UBERON:0004027 | chorionic plate | chorionic plate | [23](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=23:23) | nan           |
| 27 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [24](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=24:24) | nan           |
| 28 | UBERON:0003124 | chorion membrane  | chorion           | UBERON:0005630 | fetal membrane  | fetal membranes | [24](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=24:24) | nan           |
| 29 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [25](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=25:25) | nan           |
| 30 | UBERON:0003124 | chorion membrane  | chorion           | UBERON:0005630 | fetal membrane  | fetal membranes | [25](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=25:25) | nan           |
| 32 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [26](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=26:26) | nan           |
| 33 | UBERON:0003124 | chorion membrane  | chorion           | UBERON:0005630 | fetal membrane  | fetal membranes | [26](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=26:26) | nan           |
| 35 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [27](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=27:27) | nan           |
| 36 | UBERON:0001295 | endometrium       | endometrium       | UBERON:0005630 | fetal membrane  | fetal membranes | [27](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=27:27) | nan           |
| 37 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [28](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=28:28) | nan           |
| 38 | UBERON:0001295 | endometrium       | endometrium       | UBERON:0005630 | fetal membrane  | fetal membranes | [28](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=28:28) | nan           |
| 39 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [29](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=29:29) | nan           |
| 40 | UBERON:0001295 | endometrium       | endometrium       | UBERON:0005630 | fetal membrane  | fetal membranes | [29](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=29:29) | nan           |
| 42 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [30](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=30:30) | nan           |
| 43 | UBERON:0001295 | endometrium       | endometrium       | UBERON:0005630 | fetal membrane  | fetal membranes | [30](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=30:30) | nan           |
| 45 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [31](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=31:31) | nan           |
| 46 | UBERON:0001295 | endometrium       | endometrium       | UBERON:0005630 | fetal membrane  | fetal membranes | [31](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=31:31) | nan           |
| 48 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [32](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=32:32) | nan           |
| 49 | UBERON:0001295 | endometrium       | endometrium       | UBERON:0005630 | fetal membrane  | fetal membranes | [32](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=32:32) | nan           |
| 51 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [33](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=33:33) | nan           |
| 52 | UBERON:0001295 | endometrium       | endometrium       | UBERON:0005630 | fetal membrane  | fetal membranes | [33](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=33:33) | nan           |
| 54 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [34](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=34:34) | nan           |
| 55 | UBERON:0001295 | endometrium       | endometrium       | UBERON:0005630 | fetal membrane  | fetal membranes | [34](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=34:34) | nan           |
| 56 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [35](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=35:35) | nan           |
| 57 | UBERON:0001295 | endometrium       | endometrium       | UBERON:0005630 | fetal membrane  | fetal membranes | [35](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=35:35) | nan           |
| 58 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [36](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=36:36) | nan           |
| 59 | UBERON:0001295 | endometrium       | endometrium       | UBERON:0005630 | fetal membrane  | fetal membranes | [36](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=36:36) | nan           |
| 60 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [37](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=37:37) | nan           |
| 62 | UBERON:0005630 | fetal membrane    | fetal membranes   | UBERON:0001987 | placenta        | placenta        | [38](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=38:38) | nan           |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                      | user_slabel                     | o              | olabel                   | user_olabel              | row_number                                                                                                                  |       deltaIC |
|----|------------|---------------------------------------------|---------------------------------|----------------|--------------------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------|
|  4 | CL:0008036 | extravillous trophoblast                    | extravillous trophoblast        | UBERON:0015172 | endometrial blood vessel | endometrial blood vessel | [35](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=35:35)    |   2.59986e-14 |
|  5 | CL:0008036 | extravillous trophoblast                    | extravillous trophoblast        | UBERON:0015172 | endometrial blood vessel | endometrial blood vessel | [67](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=67:67)    |   2.59986e-14 |
|  6 | CL:0008036 | extravillous trophoblast                    | extravillous trophoblast        | UBERON:0015172 | endometrial blood vessel | endometrial blood vessel | [107](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=107:107) |   2.59986e-14 |
|  7 | CL:0000669 | pericyte                                    | pericyte                        | UBERON:0001310 | umbilical artery         | umbilical arteries       | [16](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=16:16)    |   1.57509e-14 |
|  8 | CL:0000669 | pericyte                                    | pericyte                        | UBERON:0002066 | umbilical vein           | umbilical vein           | [13](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=13:13)    |   5.04377e-17 |
|  9 | CL:0002138 | endothelial cell of lymphatic vessel        | lymphatic endothelial cell      | UBERON:0001295 | endometrium              | endometrium              | [36](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=36:36)    |   5.04459e-37 |
| 10 | CL:0002138 | endothelial cell of lymphatic vessel        | lymphatic endothelial cell      | UBERON:0001295 | endometrium              | endometrium              | [68](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=68:68)    |   5.04459e-37 |
| 11 | CL:0002138 | endothelial cell of lymphatic vessel        | lymphatic endothelial cell      | UBERON:0001295 | endometrium              | endometrium              | [108](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=108:108) |   5.04459e-37 |
| 20 | CL:0002536 | epithelial cell of amnion                   | amnion epithelial cell          | UBERON:0003254 | amniotic ectoderm        | amniotic ectoderm        | [20](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=20:20)    | nan           |
| 22 | CL:2000061 | placental amniotic mesenchymal stromal cell | amnion mesenchymal stromal cell | UBERON:0003262 | amniotic mesoderm        | amniotic mesoderm        | [21](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=21:21)    | nan           |
| 24 | CL:0002536 | epithelial cell of amnion                   | amnion epithelial cell          | UBERON:0003254 | amniotic ectoderm        | amniotic ectoderm        | [22](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=22:22)    | nan           |
| 26 | CL:2000061 | placental amniotic mesenchymal stromal cell | amnion mesenchymal stromal cell | UBERON:0003262 | amniotic mesoderm        | amniotic mesoderm        | [23](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=23:23)    | nan           |
| 31 | CL:0000523 | mononuclear cytotrophoblast cell            | cytotrophoblast                 | UBERON:0003124 | chorion membrane         | chorion                  | [25](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=25:25)    | nan           |
| 34 | CL:0008036 | extravillous trophoblast                    | extravillous trophoblast        | UBERON:0003124 | chorion membrane         | chorion                  | [26](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=26:26)    | nan           |
| 41 | CL:0002343 | decidual natural killer cell, human         | uterine NK cell                 | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [29](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=29:29)    | nan           |
| 44 | CL:0000864 | tissue-resident macrophage                  | tissue-resident macrophage      | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [30](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=30:30)    | nan           |
| 47 | CL:0000815 | regulatory T cell                           | regulatory T cell               | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [31](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=31:31)    | nan           |
| 50 | CL:0000910 | cytotoxic T cell                            | cytotoxic T cell                | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [32](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=32:32)    | nan           |
| 53 | CL:0000236 | B cell                                      | B cell                          | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [33](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=33:33)    | nan           |
| 61 | CL:0002536 | epithelial cell of amnion                   | amnion epithelial cell          | UBERON:0003254 | amniotic ectoderm        | amniotic ectoderm        | [37](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=37:37)    | nan           |
| 63 | CL:2000061 | placental amniotic mesenchymal stromal cell | amnion mesenchymal stromal cell | UBERON:0003262 | amniotic mesoderm        | amniotic mesoderm        | [38](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=38:38)    | nan           |
| 64 | CL:0002558 | fibroblast of villous mesenchyme            | placental stromal cell          | UBERON:0004027 | chorionic plate          | chorionic plate          | [39](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=39:39)    | nan           |
| 65 | CL:0000523 | mononuclear cytotrophoblast cell            | cytotrophoblast                 | UBERON:0004027 | chorionic plate          | chorionic plate          | [40](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=40:40)    | nan           |
| 66 | CL:0000525 | syncytiotrophoblast cell                    | syncytiotrophoblast             | UBERON:0004027 | chorionic plate          | chorionic plate          | [41](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=41:41)    | nan           |
| 67 | CL:0008036 | extravillous trophoblast                    | extravillous trophoblast        | UBERON:0004027 | chorionic plate          | chorionic plate          | [42](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=42:42)    | nan           |
| 68 | CL:0008036 | extravillous trophoblast                    | extravillous trophoblast        | UBERON:0004027 | chorionic plate          | chorionic plate          | [43](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=43:43)    | nan           |
| 69 | CL:0000523 | mononuclear cytotrophoblast cell            | cytotrophoblast                 | UBERON:0004027 | chorionic plate          | chorionic plate          | [44](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=44:44)    | nan           |
| 70 | CL:0000525 | syncytiotrophoblast cell                    | syncytiotrophoblast             | UBERON:0004027 | chorionic plate          | chorionic plate          | [45](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=45:45)    | nan           |
| 71 | CL:0000071 | blood vessel endothelial cell               | vascular endothelial cell       | UBERON:0004027 | chorionic plate          | chorionic plate          | [46](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=46:46)    | nan           |
| 72 | CL:0002558 | fibroblast of villous mesenchyme            | placental stromal cell          | UBERON:0004027 | chorionic plate          | chorionic plate          | [47](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=47:47)    | nan           |
| 73 | CL:0002343 | decidual natural killer cell, human         | uterine NK cell                 | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [61](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=61:61)    | nan           |
| 74 | CL:0000864 | tissue-resident macrophage                  | tissue-resident macrophage      | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [62](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=62:62)    | nan           |
| 75 | CL:0000815 | regulatory T cell                           | regulatory T cell               | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [63](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=63:63)    | nan           |
| 76 | CL:0000910 | cytotoxic T cell                            | cytotoxic T cell                | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [64](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=64:64)    | nan           |
| 77 | CL:0000236 | B cell                                      | B cell                          | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [65](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=65:65)    | nan           |
| 78 | CL:0000669 | pericyte                                    | pericyte                        | UBERON:0022358 | placenta blood vessel    | placental blood vessel   | [83](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=83:83)    | nan           |
| 79 | CL:0000359 | vascular associated smooth muscle cell      | vascular smooth muscle cell     | UBERON:0022358 | placenta blood vessel    | placental blood vessel   | [84](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=84:84)    | nan           |
| 80 | CL:0002343 | decidual natural killer cell, human         | uterine NK cell                 | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [101](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=101:101) | nan           |
| 81 | CL:0000864 | tissue-resident macrophage                  | tissue-resident macrophage      | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [102](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=102:102) | nan           |
| 82 | CL:0000815 | regulatory T cell                           | regulatory T cell               | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [103](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=103:103) | nan           |
| 83 | CL:0000910 | cytotoxic T cell                            | cytotoxic T cell                | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [104](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=104:104) | nan           |
| 84 | CL:0000236 | B cell                                      | B cell                          | UBERON:0002337 | endometrial stroma       | endometrial stroma       | [105](https://docs.google.com/spreadsheets/d/1JeeIxpcyD8eWAgdNuKtf1OMlTzEw_6AKrS5OVDkC7t4/edit#gid=231591207&range=105:105) | nan           |




# New CL terms
[**Report**](new_cl_terms_Placenta.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Placenta.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Placenta_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Placenta_AS_has_part_CT_log.tsv)