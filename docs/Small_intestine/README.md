
ASCT+B Validation Reports for Small_intestine (2023-09-22)
==========================================================

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
  
1. In row _[52](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=52:52)_, no term id was found for the name/label _serosa_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=53:53)_, no term id was found for the name/label _serosa_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=54:54)_, no term id was found for the name/label _serosa_.

1. In row _[62](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=62:62)_, no term id was found for the name/label _BCHE (butyrylcholinesterase) cell_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=64:64)_, no term id was found for the name/label _lymphatic_.

1. In row _[67](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=67:67)_, no term id was found for the name/label _nerve_.

1. In row _[71](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=71:71)_, no term id was found for the name/label _CD4+ T_.

1. In row _[72](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=72:72)_, no term id was found for the name/label _regulatory CD4+ T_.

1. In row _[73](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=73:73)_, no term id was found for the name/label _CD8+ T_.

1. In row _[82](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=82:82)_, no term id was found for the name/label _nerves_.

1. In row _[83](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=83:83)_, no term id was found for the name/label _endoethlial_.

1. In row _[84](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=84:84)_, no term id was found for the name/label _lymphatic_.

1. In row _[85](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=85:85)_, no term id was found for the name/label _nerve_.

1. In row _[86](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=86:86)_, no term id was found for the name/label _muscle_.

1. In row _[97](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=97:97)_, no term id was found for the name/label _mucosa_.

1. In row _[98](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=98:98)_, no term id was found for the name/label _mucosa_.

1. In row _[99](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=99:99)_, no term id was found for the name/label _mucosa_.

1. In row _[100](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=100:100)_, no term id was found for the name/label _mucosa_.

1. In row _[101](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=101:101)_, no term id was found for the name/label _mucosa_.

1. In row _[102](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=102:102)_, no term id was found for the name/label _mucosa_.

1. In row _[103](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=103:103)_, no term id was found for the name/label _mucosa_.

1. In row _[104](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=104:104)_, no term id was found for the name/label _mucosa_.

1. In row _[105](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=105:105)_, no term id was found for the name/label _mucosa_.

1. In row _[106](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=106:106)_, no term id was found for the name/label _mucosa_.

1. In row _[107](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=107:107)_, no term id was found for the name/label _mucosa_.

1. In row _[108](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=108:108)_, no term id was found for the name/label _mucosa_.

1. In row _[109](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=109:109)_, no term id was found for the name/label _mucosa_.

1. In row _[110](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=110:110)_, no term id was found for the name/label _mucosa_.

1. In row _[111](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=111:111)_, no term id was found for the name/label _mucosa_.

1. In row _[112](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=112:112)_, no term id was found for the name/label _mucosa_.

1. In row _[113](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=113:113)_, no term id was found for the name/label _mucosa_.

1. In row _[114](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=114:114)_, no term id was found for the name/label _mucosa_.

1. In row _[115](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=115:115)_, no term id was found for the name/label _mucosa_.

1. In row _[116](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=116:116)_, no term id was found for the name/label _mucosa_.

1. In row _[117](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=117:117)_, no term id was found for the name/label _mucosa_.

1. In row _[118](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=118:118)_, no term id was found for the name/label _mucosa_.

1. In row _[119](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=119:119)_, no term id was found for the name/label _mucosa_.

1. In row _[120](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=120:120)_, no term id was found for the name/label _mucosa_.

1. In row _[121](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=121:121)_, no term id was found for the name/label _mucosa_.

1. In row _[122](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=122:122)_, no term id was found for the name/label _mucosa_.

1. In row _[123](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=123:123)_, no term id was found for the name/label _mucosa_.

1. In row _[124](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=124:124)_, no term id was found for the name/label _submucosa_.

1. In row _[125](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=125:125)_, no term id was found for the name/label _submucosa_.

1. In row _[126](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=126:126)_, no term id was found for the name/label _submucosa_.

1. In row _[127](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=127:127)_, no term id was found for the name/label _submucosa_.

1. In row _[128](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=128:128)_, no term id was found for the name/label _submucosa_.

1. In row _[129](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=129:129)_, no term id was found for the name/label _muscularis propria_.

1. In row _[130](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=130:130)_, no term id was found for the name/label _muscularis propria_.

1. In row _[131](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=131:131)_, no term id was found for the name/label _muscularis propria_.

1. In row _[132](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=132:132)_, no term id was found for the name/label _muscularis propria_.

1. In row _[133](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=133:133)_, no term id was found for the name/label _muscularis propria_.

1. In row _[134](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=134:134)_, no term id was found for the name/label _muscularis propria_.

1. In row _[135](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=135:135)_, no term id was found for the name/label _muscularis propria_.

1. In row _[136](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=136:136)_, no term id was found for the name/label _serosa_.

1. In row _[137](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=137:137)_, no term id was found for the name/label _serosa_.

1. In row _[138](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=138:138)_, no term id was found for the name/label _serosa_.

1. In row _[139](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=139:139)_, no term id was found for the name/label _mucosa_.

1. In row _[140](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=140:140)_, no term id was found for the name/label _mucosa_.

1. In row _[141](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=141:141)_, no term id was found for the name/label _mucosa_.

1. In row _[142](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=142:142)_, no term id was found for the name/label _mucosa_.

1. In row _[143](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=143:143)_, no term id was found for the name/label _mucosa_.

1. In row _[144](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=144:144)_, no term id was found for the name/label _mucosa_.

1. In row _[145](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=145:145)_, no term id was found for the name/label _mucosa_.

1. In row _[146](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=146:146)_, no term id was found for the name/label _mucosa_.

1. In row _[147](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=147:147)_, no term id was found for the name/label _mucosa_.

1. In row _[148](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=148:148)_, no term id was found for the name/label _mucosa_.

1. In row _[149](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=149:149)_, no term id was found for the name/label _mucosa_.

1. In row _[150](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=150:150)_, no term id was found for the name/label _mucosa_.

1. In row _[151](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=151:151)_, no term id was found for the name/label _mucosa_.

1. In row _[152](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=152:152)_, no term id was found for the name/label _mucosa_.

1. In row _[153](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=153:153)_, no term id was found for the name/label _mucosa_.

1. In row _[154](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=154:154)_, no term id was found for the name/label _mucosa_.

1. In row _[155](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=155:155)_, no term id was found for the name/label _mucosa_.

1. In row _[156](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=156:156)_, no term id was found for the name/label _mucosa_.

1. In row _[157](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=157:157)_, no term id was found for the name/label _mucosa_.

1. In row _[158](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=158:158)_, no term id was found for the name/label _mucosa_.

1. In row _[159](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=159:159)_, no term id was found for the name/label _mucosa_.

1. In row _[160](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=160:160)_, no term id was found for the name/label _mucosa_.

1. In row _[161](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=161:161)_, no term id was found for the name/label _mucosa_.

1. In row _[162](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=162:162)_, no term id was found for the name/label _mucosa_.

1. In row _[163](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=163:163)_, no term id was found for the name/label _mucosa_.

1. In row _[164](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=164:164)_, no term id was found for the name/label _mucosa_.

1. In row _[165](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=165:165)_, no term id was found for the name/label _mucosa_.

1. In row _[166](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=166:166)_, no term id was found for the name/label _submucosa_.

1. In row _[167](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=167:167)_, no term id was found for the name/label _submucosa_.

1. In row _[168](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=168:168)_, no term id was found for the name/label _submucosa_.

1. In row _[169](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=169:169)_, no term id was found for the name/label _submucosa_.

1. In row _[170](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=170:170)_, no term id was found for the name/label _submucosa_.

1. In row _[171](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=171:171)_, no term id was found for the name/label _muscularis propria_.

1. In row _[172](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=172:172)_, no term id was found for the name/label _muscularis propria_.

1. In row _[173](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=173:173)_, no term id was found for the name/label _muscularis propria_.

1. In row _[174](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=174:174)_, no term id was found for the name/label _muscularis propria_.

1. In row _[175](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=175:175)_, no term id was found for the name/label _muscularis propria_.

1. In row _[176](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=176:176)_, no term id was found for the name/label _muscularis propria_.

1. In row _[177](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=177:177)_, no term id was found for the name/label _muscularis propria_.

1. In row _[178](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=178:178)_, no term id was found for the name/label _serosa_.

1. In row _[179](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=179:179)_, no term id was found for the name/label _serosa_.

1. In row _[180](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=180:180)_, no term id was found for the name/label _serosa_.

1. In row _[181](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=181:181)_, no term id was found for the name/label _mucosa_.

1. In row _[182](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=182:182)_, no term id was found for the name/label _mucosa_.

1. In row _[183](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=183:183)_, no term id was found for the name/label _mucosa_.

1. In row _[184](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=184:184)_, no term id was found for the name/label _mucosa_.

1. In row _[185](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=185:185)_, no term id was found for the name/label _mucosa_.

1. In row _[186](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=186:186)_, no term id was found for the name/label _mucosa_.

1. In row _[187](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=187:187)_, no term id was found for the name/label _mucosa_.

1. In row _[188](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=188:188)_, no term id was found for the name/label _mucosa_.

1. In row _[189](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=189:189)_, no term id was found for the name/label _mucosa_.

1. In row _[190](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=190:190)_, no term id was found for the name/label _mucosa_.

1. In row _[191](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=191:191)_, no term id was found for the name/label _mucosa_.

1. In row _[192](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=192:192)_, no term id was found for the name/label _mucosa_.

1. In row _[193](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=193:193)_, no term id was found for the name/label _mucosa_.

1. In row _[194](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=194:194)_, no term id was found for the name/label _mucosa_.

1. In row _[195](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=195:195)_, no term id was found for the name/label _mucosa_.

1. In row _[196](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=196:196)_, no term id was found for the name/label _mucosa_.

1. In row _[197](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=197:197)_, no term id was found for the name/label _mucosa_.

1. In row _[198](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=198:198)_, no term id was found for the name/label _mucosa_.

1. In row _[199](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=199:199)_, no term id was found for the name/label _mucosa_.

1. In row _[200](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=200:200)_, no term id was found for the name/label _mucosa_.

1. In row _[201](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=201:201)_, no term id was found for the name/label _mucosa_.

1. In row _[202](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=202:202)_, no term id was found for the name/label _mucosa_.

1. In row _[203](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=203:203)_, no term id was found for the name/label _mucosa_.

1. In row _[204](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=204:204)_, no term id was found for the name/label _mucosa_.

1. In row _[205](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=205:205)_, no term id was found for the name/label _mucosa_.

1. In row _[206](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=206:206)_, no term id was found for the name/label _mucosa_.

1. In row _[207](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=207:207)_, no term id was found for the name/label _mucosa_.

1. In row _[208](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=208:208)_, no term id was found for the name/label _submucosa_.

1. In row _[209](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=209:209)_, no term id was found for the name/label _submucosa_.

1. In row _[210](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=210:210)_, no term id was found for the name/label _submucosa_.

1. In row _[211](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=211:211)_, no term id was found for the name/label _submucosa_.

1. In row _[212](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=212:212)_, no term id was found for the name/label _submucosa_.

1. In row _[220](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=220:220)_, no term id was found for the name/label _serosa_.

1. In row _[221](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=221:221)_, no term id was found for the name/label _serosa_.

1. In row _[222](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=222:222)_, no term id was found for the name/label _serosa_.

1. In row _[230](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=230:230)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[231](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=231:231)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[231](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=231:231)_, no term id was found for the name/label _lymphatics_.

1. In row _[232](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=232:232)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[233](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=233:233)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[234](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=234:234)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[234](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=234:234)_, no term id was found for the name/label _nerves_.

1. In row _[235](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=235:235)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[236](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=236:236)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[237](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=237:237)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[238](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=238:238)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[238](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=238:238)_, no term id was found for the name/label _CD4+ T_.

1. In row _[239](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=239:239)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[239](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=239:239)_, no term id was found for the name/label _regulatory CD4+ T_.

1. In row _[240](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=240:240)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[240](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=240:240)_, no term id was found for the name/label _CD8+ T_.

1. In row _[241](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=241:241)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[242](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=242:242)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[243](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=243:243)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[244](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=244:244)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[245](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=245:245)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[246](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=246:246)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[247](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=247:247)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[248](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=248:248)_, no term id was found for the name/label _muscle_.

1. In row _[249](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=249:249)_, no term id was found for the name/label _nerves_.

1. In row _[251](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=251:251)_, no term id was found for the name/label _lymphatic_.

1. In row _[252](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=252:252)_, no term id was found for the name/label _nerves_.

1. In row _[253](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=253:253)_, no term id was found for the name/label _muscle_.

1. In row _[254](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=254:254)_, no term id was found for the name/label _muscle_.

1. In row _[258](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=258:258)_, no term id was found for the name/label _nerves_.

1. In row _[259](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=259:259)_, no term id was found for the name/label _myenteric plexus of Auerbach_.

1. In row _[259](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=259:259)_, no term id was found for the name/label _nerves_.

1. In row _[260](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=260:260)_, no term id was found for the name/label _myenteric plexus of Auerbach_.

1. In row _[260](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=260:260)_, no term id was found for the name/label _muscle_.

1. In row _[262](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=262:262)_, no term id was found for the name/label _connective tissue_.

1. In row _[263](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=263:263)_, no term id was found for the name/label _connective tissue_.

1. In row _[271](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=271:271)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[272](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=272:272)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[273](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=273:273)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[274](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=274:274)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[275](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=275:275)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[276](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=276:276)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[277](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=277:277)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[278](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=278:278)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[279](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=279:279)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[280](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=280:280)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[281](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=281:281)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[282](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=282:282)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[283](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=283:283)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[284](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=284:284)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[285](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=285:285)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[286](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=286:286)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[287](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=287:287)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[288](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=288:288)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[289](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=289:289)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[290](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=290:290)_, no term id was found for the name/label _muscularis mucosa_.

1. In row _[291](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=291:291)_, no term id was found for the name/label _submucosa_.

1. In row _[292](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=292:292)_, no term id was found for the name/label _submucosa_.

1. In row _[293](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=293:293)_, no term id was found for the name/label _submucosa_.

1. In row _[294](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=294:294)_, no term id was found for the name/label _submucosal plexus of Meissner_.

1. In row _[295](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=295:295)_, no term id was found for the name/label _submucosal plexus of Meissner_.

1. In row _[296](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=296:296)_, no term id was found for the name/label _muscularis externa_.

1. In row _[296](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=296:296)_, no term id was found for the name/label _circular/longitudinal muscle_.

1. In row _[297](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=297:297)_, no term id was found for the name/label _muscularis externa_.

1. In row _[297](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=297:297)_, no term id was found for the name/label _circular/longitudinal muscle_.

1. In row _[298](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=298:298)_, no term id was found for the name/label _muscularis externa_.

1. In row _[298](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=298:298)_, no term id was found for the name/label _circular/longitudinal muscle_.

1. In row _[299](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=299:299)_, no term id was found for the name/label _muscularis externa_.

1. In row _[299](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=299:299)_, no term id was found for the name/label _circular/longitudinal muscle_.

1. In row _[300](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=300:300)_, no term id was found for the name/label _muscularis externa_.

1. In row _[300](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=300:300)_, no term id was found for the name/label _circular/longitudinal muscle_.

1. In row _[301](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=301:301)_, no term id was found for the name/label _muscularis externa_.

1. In row _[301](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=301:301)_, no term id was found for the name/label _myenteric plexus of Auerbach_.

1. In row _[302](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=302:302)_, no term id was found for the name/label _muscularis externa_.

1. In row _[302](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=302:302)_, no term id was found for the name/label _myenteric plexus of Auerbach_.

1. In row _[303](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=303:303)_, no term id was found for the name/label _serosa_.

1. In row _[303](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=303:303)_, no term id was found for the name/label _connective tissue_.

1. In row _[304](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=304:304)_, no term id was found for the name/label _serosa_.

1. In row _[304](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=304:304)_, no term id was found for the name/label _connective tissue_.

1. In row _[305](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=305:305)_, no term id was found for the name/label _serosa_.

1. In row _[306](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=306:306)_, no term id was found for the name/label _mucosa_.

1. In row _[306](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=306:306)_, no term id was found for the name/label _Epithelium_.

1. In row _[306](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=306:306)_, no term id was found for the name/label _epithelial stem cells_.

1. In row _[307](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=307:307)_, no term id was found for the name/label _mucosa_.

1. In row _[307](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=307:307)_, no term id was found for the name/label _Epithelium_.

1. In row _[308](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=308:308)_, no term id was found for the name/label _mucosa_.

1. In row _[308](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=308:308)_, no term id was found for the name/label _Epithelium_.

1. In row _[309](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=309:309)_, no term id was found for the name/label _mucosa_.

1. In row _[309](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=309:309)_, no term id was found for the name/label _Epithelium_.

1. In row _[310](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=310:310)_, no term id was found for the name/label _mucosa_.

1. In row _[310](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=310:310)_, no term id was found for the name/label _Epithelium_.

1. In row _[311](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=311:311)_, no term id was found for the name/label _mucosa_.

1. In row _[311](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=311:311)_, no term id was found for the name/label _Epithelium_.

1. In row _[312](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=312:312)_, no term id was found for the name/label _mucosa_.

1. In row _[312](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=312:312)_, no term id was found for the name/label _Epithelium_.

1. In row _[313](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=313:313)_, no term id was found for the name/label _mucosa_.

1. In row _[313](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=313:313)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[314](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=314:314)_, no term id was found for the name/label _mucosa_.

1. In row _[314](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=314:314)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[314](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=314:314)_, no term id was found for the name/label _lymphatics_.

1. In row _[315](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=315:315)_, no term id was found for the name/label _mucosa_.

1. In row _[315](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=315:315)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[316](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=316:316)_, no term id was found for the name/label _mucosa_.

1. In row _[316](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=316:316)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[317](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=317:317)_, no term id was found for the name/label _mucosa_.

1. In row _[317](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=317:317)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[317](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=317:317)_, no term id was found for the name/label _nerves_.

1. In row _[318](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=318:318)_, no term id was found for the name/label _mucosa_.

1. In row _[318](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=318:318)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[319](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=319:319)_, no term id was found for the name/label _mucosa_.

1. In row _[319](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=319:319)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[320](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=320:320)_, no term id was found for the name/label _mucosa_.

1. In row _[320](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=320:320)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[321](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=321:321)_, no term id was found for the name/label _mucosa_.

1. In row _[321](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=321:321)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[321](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=321:321)_, no term id was found for the name/label _CD4+ T_.

1. In row _[322](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=322:322)_, no term id was found for the name/label _mucosa_.

1. In row _[322](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=322:322)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[322](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=322:322)_, no term id was found for the name/label _regulatory CD4+ T_.

1. In row _[323](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=323:323)_, no term id was found for the name/label _mucosa_.

1. In row _[323](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=323:323)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[323](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=323:323)_, no term id was found for the name/label _CD8+ T_.

1. In row _[324](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=324:324)_, no term id was found for the name/label _mucosa_.

1. In row _[324](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=324:324)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[325](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=325:325)_, no term id was found for the name/label _mucosa_.

1. In row _[325](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=325:325)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[326](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=326:326)_, no term id was found for the name/label _mucosa_.

1. In row _[326](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=326:326)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[327](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=327:327)_, no term id was found for the name/label _mucosa_.

1. In row _[327](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=327:327)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[328](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=328:328)_, no term id was found for the name/label _mucosa_.

1. In row _[328](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=328:328)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[329](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=329:329)_, no term id was found for the name/label _mucosa_.

1. In row _[329](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=329:329)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[330](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=330:330)_, no term id was found for the name/label _mucosa_.

1. In row _[330](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=330:330)_, no term id was found for the name/label _Lamina propria/Gut associated lymphoid tissue (GALT)_.

1. In row _[331](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=331:331)_, no term id was found for the name/label _mucosa_.

1. In row _[331](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=331:331)_, no term id was found for the name/label _muscularis mucosa_.

1. In row _[331](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=331:331)_, no term id was found for the name/label _muscle_.

1. In row _[332](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=332:332)_, no term id was found for the name/label _submucosa_.

1. In row _[332](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=332:332)_, no term id was found for the name/label _nerves_.

1. In row _[333](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=333:333)_, no term id was found for the name/label _submucosa_.

1. In row _[334](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=334:334)_, no term id was found for the name/label _submucosa_.

1. In row _[334](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=334:334)_, no term id was found for the name/label _lymphatic_.

1. In row _[335](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=335:335)_, no term id was found for the name/label _submucosa_.

1. In row _[335](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=335:335)_, no term id was found for the name/label _submucosal plexus of Meissner_.

1. In row _[335](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=335:335)_, no term id was found for the name/label _nerves_.

1. In row _[336](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=336:336)_, no term id was found for the name/label _submucosa_.

1. In row _[336](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=336:336)_, no term id was found for the name/label _submucosal plexus of Meissner_.

1. In row _[336](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=336:336)_, no term id was found for the name/label _muscle_.

1. In row _[337](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=337:337)_, no term id was found for the name/label _muscularis externa_.

1. In row _[337](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=337:337)_, no term id was found for the name/label _circular/longitudinal muscle_.

1. In row _[337](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=337:337)_, no term id was found for the name/label _muscle_.

1. In row _[338](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=338:338)_, no term id was found for the name/label _muscularis externa_.

1. In row _[338](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=338:338)_, no term id was found for the name/label _circular/longitudinal muscle_.

1. In row _[339](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=339:339)_, no term id was found for the name/label _muscularis externa_.

1. In row _[339](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=339:339)_, no term id was found for the name/label _circular/longitudinal muscle_.

1. In row _[340](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=340:340)_, no term id was found for the name/label _muscularis externa_.

1. In row _[340](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=340:340)_, no term id was found for the name/label _circular/longitudinal muscle_.

1. In row _[341](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=341:341)_, no term id was found for the name/label _muscularis externa_.

1. In row _[341](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=341:341)_, no term id was found for the name/label _circular/longitudinal muscle_.

1. In row _[341](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=341:341)_, no term id was found for the name/label _nerves_.

1. In row _[342](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=342:342)_, no term id was found for the name/label _muscularis externa_.

1. In row _[342](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=342:342)_, no term id was found for the name/label _myenteric plexus of Auerbach_.

1. In row _[342](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=342:342)_, no term id was found for the name/label _nerves_.

1. In row _[343](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=343:343)_, no term id was found for the name/label _muscularis externa_.

1. In row _[343](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=343:343)_, no term id was found for the name/label _myenteric plexus of Auerbach_.

1. In row _[343](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=343:343)_, no term id was found for the name/label _muscle_.

1. In row _[344](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=344:344)_, no term id was found for the name/label _serosa_.

1. In row _[345](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=345:345)_, no term id was found for the name/label _serosa_.

1. In row _[346](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=346:346)_, no term id was found for the name/label _serosa_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
1. In row _[62](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=62:62)_, the term _BCHE (butyrylcholinesterase) cell_ without ontology ID has no parent that is from the CL ontology.

1. In row _[64](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=64:64)_, the term _lymphatic_ without ontology ID has no parent that is from the CL ontology.

1. In row _[67](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=67:67)_, the term _nerve_ without ontology ID has no parent that is from the CL ontology.

1. In row _[71](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=71:71)_, the term _CD4+ T_ without ontology ID has no parent that is from the CL ontology.

1. In row _[72](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=72:72)_, the term _regulatory CD4+ T_ without ontology ID has no parent that is from the CL ontology.

1. In row _[73](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=73:73)_, the term _CD8+ T_ without ontology ID has no parent that is from the CL ontology.

1. In row _[85](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=85:85)_, the term _nerve_ without ontology ID has no parent that is from the CL ontology.

1. In row _[86](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=86:86)_, the term _muscle_ without ontology ID has no parent that is from the CL ontology.

1. In row _[231](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=231:231)_, the term _lymphatics_ without ontology ID has no parent that is from the CL ontology.

1. In row _[234](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=234:234)_, the term _nerves_ without ontology ID has no parent that is from the CL ontology.

1. In row _[238](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=238:238)_, the term _CD4+ T_ without ontology ID has no parent that is from the CL ontology.

1. In row _[239](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=239:239)_, the term _regulatory CD4+ T_ without ontology ID has no parent that is from the CL ontology.

1. In row _[240](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=240:240)_, the term _CD8+ T_ without ontology ID has no parent that is from the CL ontology.

1. In row _[248](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=248:248)_, the term _muscle_ without ontology ID has no parent that is from the CL ontology.

1. In row _[249](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=249:249)_, the term _nerves_ without ontology ID has no parent that is from the CL ontology.

1. In row _[251](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=251:251)_, the term _lymphatic_ without ontology ID has no parent that is from the CL ontology.

1. In row _[252](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=252:252)_, the term _nerves_ without ontology ID has no parent that is from the CL ontology.

1. In row _[253](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=253:253)_, the term _muscle_ without ontology ID has no parent that is from the CL ontology.

1. In row _[254](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=254:254)_, the term _muscle_ without ontology ID has no parent that is from the CL ontology.

1. In row _[258](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=258:258)_, the term _nerves_ without ontology ID has no parent that is from the CL ontology.

1. In row _[259](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=259:259)_, the term _nerves_ without ontology ID has no parent that is from the CL ontology.

1. In row _[260](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=260:260)_, the term _muscle_ without ontology ID has no parent that is from the CL ontology.

1. In row _[306](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=306:306)_, the term _epithelial stem cells_ without ontology ID has no parent that is from the CL ontology.

1. In row _[314](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=314:314)_, the term _lymphatics_ without ontology ID has no parent that is from the CL ontology.

1. In row _[317](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=317:317)_, the term _nerves_ without ontology ID has no parent that is from the CL ontology.

1. In row _[321](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=321:321)_, the term _CD4+ T_ without ontology ID has no parent that is from the CL ontology.

1. In row _[322](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=322:322)_, the term _regulatory CD4+ T_ without ontology ID has no parent that is from the CL ontology.

1. In row _[323](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=323:323)_, the term _CD8+ T_ without ontology ID has no parent that is from the CL ontology.

1. In row _[331](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=331:331)_, the term _muscle_ without ontology ID has no parent that is from the CL ontology.

1. In row _[332](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=332:332)_, the term _nerves_ without ontology ID has no parent that is from the CL ontology.

1. In row _[334](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=334:334)_, the term _lymphatic_ without ontology ID has no parent that is from the CL ontology.

1. In row _[335](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=335:335)_, the term _nerves_ without ontology ID has no parent that is from the CL ontology.

1. In row _[336](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=336:336)_, the term _muscle_ without ontology ID has no parent that is from the CL ontology.

1. In row _[337](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=337:337)_, the term _muscle_ without ontology ID has no parent that is from the CL ontology.

1. In row _[341](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=341:341)_, the term _nerves_ without ontology ID has no parent that is from the CL ontology.

1. In row _[342](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=342:342)_, the term _nerves_ without ontology ID has no parent that is from the CL ontology.

1. In row _[343](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=343:343)_, the term _muscle_ without ontology ID has no parent that is from the CL ontology.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[13](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=13:13)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[14](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=14:14)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[15](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=15:15)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[16](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=16:16)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[17](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=17:17)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[18](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=18:18)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[19](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=19:19)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[20](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=20:20)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[21](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=21:21)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[22](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=22:22)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[23](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=23:23)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[24](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=24:24)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[25](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=25:25)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[26](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=26:26)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[27](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=27:27)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[28](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=28:28)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[29](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=29:29)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[30](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=30:30)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[31](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=31:31)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[32](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=32:32)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[33](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=33:33)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[34](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=34:34)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[35](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=35:35)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[36](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=36:36)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[37](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=37:37)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[38](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=38:38)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[39](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=39:39)_, the term _FMA:17101_ is from another ontology that is not validated in this process.

1. In row _[40](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=40:40)_, the term _FMA:17107_ is from another ontology that is not validated in this process.

1. In row _[41](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=41:41)_, the term _FMA:17107_ is from another ontology that is not validated in this process.

1. In row _[42](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=42:42)_, the term _FMA:17107_ is from another ontology that is not validated in this process.

1. In row _[43](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=43:43)_, the term _FMA:17107_ is from another ontology that is not validated in this process.

1. In row _[44](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=44:44)_, the term _FMA:17107_ is from another ontology that is not validated in this process.

1. In row _[45](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=45:45)_, the term _FMA:17113_ is from another ontology that is not validated in this process.

1. In row _[46](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=46:46)_, the term _FMA:17113_ is from another ontology that is not validated in this process.

1. In row _[47](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=47:47)_, the term _FMA:17113_ is from another ontology that is not validated in this process.

1. In row _[48](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=48:48)_, the term _FMA:17113_ is from another ontology that is not validated in this process.

1. In row _[49](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=49:49)_, the term _FMA:17113_ is from another ontology that is not validated in this process.

1. In row _[50](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=50:50)_, the term _FMA:17113_ is from another ontology that is not validated in this process.

1. In row _[51](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=51:51)_, the term _FMA:17113_ is from another ontology that is not validated in this process.

1. In row _[55](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=55:55)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[56](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=56:56)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[57](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=57:57)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[58](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=58:58)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[59](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=59:59)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[60](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=60:60)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[61](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=61:61)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[62](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=62:62)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[63](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=63:63)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[64](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=64:64)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[65](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=65:65)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[66](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=66:66)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[67](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=67:67)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[68](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=68:68)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[69](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=69:69)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[70](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=70:70)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[71](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=71:71)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[72](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=72:72)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[73](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=73:73)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[74](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=74:74)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[75](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=75:75)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[76](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=76:76)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[77](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=77:77)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[78](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=78:78)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[79](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=79:79)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[80](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=80:80)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[81](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=81:81)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[82](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=82:82)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[83](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=83:83)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[84](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=84:84)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[85](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=85:85)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[86](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=86:86)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[87](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=87:87)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[88](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=88:88)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[89](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=89:89)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[90](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=90:90)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[91](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=91:91)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[92](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=92:92)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[93](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=93:93)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[94](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=94:94)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[95](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=95:95)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[96](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=96:96)_, the term _FMA:14926_ is from another ontology that is not validated in this process.

1. In row _[97](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=97:97)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[98](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=98:98)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[99](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=99:99)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[100](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=100:100)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[101](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=101:101)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[102](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=102:102)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[103](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=103:103)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[104](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=104:104)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[105](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=105:105)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[106](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=106:106)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[107](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=107:107)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[108](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=108:108)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[109](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=109:109)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[110](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=110:110)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[111](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=111:111)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[112](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=112:112)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[113](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=113:113)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[114](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=114:114)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[115](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=115:115)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[116](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=116:116)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[117](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=117:117)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[118](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=118:118)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[119](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=119:119)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[120](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=120:120)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[121](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=121:121)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[122](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=122:122)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[123](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=123:123)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[124](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=124:124)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[125](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=125:125)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[126](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=126:126)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[127](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=127:127)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[128](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=128:128)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[129](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=129:129)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[130](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=130:130)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[131](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=131:131)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[132](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=132:132)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[133](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=133:133)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[134](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=134:134)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[135](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=135:135)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[136](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=136:136)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[137](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=137:137)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[138](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=138:138)_, the term _FMA:14928_ is from another ontology that is not validated in this process.

1. In row _[139](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=139:139)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[140](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=140:140)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[141](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=141:141)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[142](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=142:142)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[143](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=143:143)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[144](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=144:144)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[145](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=145:145)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[146](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=146:146)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[147](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=147:147)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[148](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=148:148)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[149](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=149:149)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[150](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=150:150)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[151](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=151:151)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[152](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=152:152)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[153](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=153:153)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[154](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=154:154)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[155](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=155:155)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[156](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=156:156)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[157](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=157:157)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[158](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=158:158)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[159](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=159:159)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[160](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=160:160)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[161](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=161:161)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[162](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=162:162)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[163](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=163:163)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[164](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=164:164)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[165](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=165:165)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[166](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=166:166)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[167](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=167:167)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[168](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=168:168)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[169](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=169:169)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[170](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=170:170)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[171](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=171:171)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[172](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=172:172)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[173](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=173:173)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[174](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=174:174)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[175](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=175:175)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[176](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=176:176)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[177](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=177:177)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[178](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=178:178)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[179](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=179:179)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[180](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=180:180)_, the term _FMA:14929_ is from another ontology that is not validated in this process.

1. In row _[181](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=181:181)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[182](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=182:182)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[183](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=183:183)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[184](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=184:184)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[185](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=185:185)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[186](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=186:186)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[187](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=187:187)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[188](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=188:188)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[189](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=189:189)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[190](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=190:190)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[191](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=191:191)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[192](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=192:192)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[193](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=193:193)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[194](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=194:194)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[195](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=195:195)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[196](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=196:196)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[197](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=197:197)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[198](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=198:198)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[199](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=199:199)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[200](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=200:200)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[201](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=201:201)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[202](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=202:202)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[203](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=203:203)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[204](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=204:204)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[205](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=205:205)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[206](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=206:206)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[207](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=207:207)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[208](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=208:208)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[209](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=209:209)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[210](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=210:210)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[211](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=211:211)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[212](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=212:212)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[213](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=213:213)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[213](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=213:213)_, the term _FMA:17116_ is from another ontology that is not validated in this process.

1. In row _[214](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=214:214)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[214](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=214:214)_, the term _FMA:17116_ is from another ontology that is not validated in this process.

1. In row _[215](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=215:215)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[215](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=215:215)_, the term _FMA:17116_ is from another ontology that is not validated in this process.

1. In row _[216](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=216:216)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[216](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=216:216)_, the term _FMA:17116_ is from another ontology that is not validated in this process.

1. In row _[217](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=217:217)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[217](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=217:217)_, the term _FMA:17116_ is from another ontology that is not validated in this process.

1. In row _[218](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=218:218)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[218](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=218:218)_, the term _FMA:17116_ is from another ontology that is not validated in this process.

1. In row _[219](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=219:219)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[219](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=219:219)_, the term _FMA:17116_ is from another ontology that is not validated in this process.

1. In row _[220](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=220:220)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[221](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=221:221)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[222](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=222:222)_, the term _FMA:14930_ is from another ontology that is not validated in this process.

1. In row _[306](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=306:306)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[307](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=307:307)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[308](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=308:308)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[309](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=309:309)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[310](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=310:310)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[311](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=311:311)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[312](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=312:312)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[313](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=313:313)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[314](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=314:314)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[315](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=315:315)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[316](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=316:316)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[317](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=317:317)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[318](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=318:318)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[319](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=319:319)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[320](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=320:320)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[321](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=321:321)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[322](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=322:322)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[323](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=323:323)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[324](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=324:324)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[325](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=325:325)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[326](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=326:326)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[327](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=327:327)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[328](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=328:328)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[329](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=329:329)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[330](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=330:330)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[331](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=331:331)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[332](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=332:332)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[333](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=333:333)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[334](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=334:334)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[335](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=335:335)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[336](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=336:336)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[337](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=337:337)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[338](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=338:338)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[339](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=339:339)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[340](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=340:340)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[341](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=341:341)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[342](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=342:342)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[343](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=343:343)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[344](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=344:344)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[345](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=345:345)_, the term _FMA:14966_ is from another ontology that is not validated in this process.

1. In row _[346](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=346:346)_, the term _FMA:14966_ is from another ontology that is not validated in this process.


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



|    | s              | slabel                                    | user_slabel                                                                                                    | o              | olabel                | user_olabel   | row_number                                                                                                               |   deltaIC |
|----|----------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------|-----------------------|---------------|--------------------------------------------------------------------------------------------------------------------------|-----------|
| 24 | UBERON:8410000 | duodeno-jejunal junction                  | duodenojejunal flexure                                                                                         | UBERON:0002114 | duodenum              | duodenum      | [12](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=12:12) |       nan |
| 28 | UBERON:8410064 | submucous nerve plexus of small intestine | submucosal plexus of Meissner submucosal plexus (Meissners plexus, plexus of the submucosa, plexus submucosus) | UBERON:0003332 | submucosa of duodenum | submucosa     | [85](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=85:85) |       nan |
| 29 | UBERON:8410064 | submucous nerve plexus of small intestine | submucosal plexus of Meissner                                                                                  | UBERON:0003332 | submucosa of duodenum | submucosa     | [86](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=86:86) |       nan |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s          | slabel                                              | user_slabel                 | o              | olabel                  | user_olabel                                          | row_number                                                                                                                  |          deltaIC |
|----|------------|-----------------------------------------------------|-----------------------------|----------------|-------------------------|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------|
|  0 | CL:0000034 | stem cell                                           | stem cell                   | UBERON:0008346 | duodenal epithelium     | Epithelium                                           | [61](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=61:61)    |      1.04923e+13 |
|  1 | CL:0000584 | enterocyte                                          | enterocyte                  | UBERON:0008346 | duodenal epithelium     | Epithelium                                           | [59](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=59:59)    |      4.17431e+07 |
|  2 | CL:0000584 | enterocyte                                          | enterocytes                 | UBERON:0000400 | jejunal epithelium      | Epithelium                                           | [228](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=228:228) |      4.17431e+07 |
|  3 | CL:0000212 | absorptive cell                                     | absorptive                  | UBERON:0008346 | duodenal epithelium     | Epithelium                                           | [58](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=58:58)    | 274980           |
|  4 | CL:0000212 | absorptive cell                                     | absorptive                  | UBERON:0000400 | jejunal epithelium      | Epithelium                                           | [226](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=226:226) | 274980           |
|  5 | CL:0000036 | epithelial fate stem cell                           | epithelial stem cells       | UBERON:0000400 | jejunal epithelium      | Epithelium                                           | [223](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=223:223) |   2887.63        |
|  6 | CL:0000623 | natural killer cell                                 | natural killer (NK) cell    | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [78](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=78:78)    |    100           |
|  7 | CL:0000236 | B cell                                              | B cell                      | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [69](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=69:69)    |    100           |
|  8 | CL:0000115 | endothelial cell                                    | endothelial                 | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [63](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=63:63)    |    100           |
|  9 | CL:0000771 | eosinophil                                          | eosinophil                  | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [75](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=75:75)    |    100           |
| 10 | CL:0000451 | dendritic cell                                      | dendritic cell (DC)         | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [79](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=79:79)    |    100           |
| 11 | CL:0001065 | innate lymphoid cell                                | innate lyphoid cell (ILC)   | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [80](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=80:80)    |    100           |
| 12 | CL:0000786 | plasma cell                                         | plasma                      | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [70](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=70:70)    |    100           |
| 13 | CL:0000115 | endothelial cell                                    | endoethlial                 | UBERON:0003333 | submucosa of jejunum    | submucosa                                            | [250](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=250:250) |    100           |
| 14 | CL:0000057 | fibroblast                                          | fibroblast                  | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [66](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=66:66)    |    100           |
| 15 | CL:0000186 | myofibroblast cell                                  | myofibroblast               | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [65](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=65:65)    |    100           |
| 16 | CL:0000682 | M cell of gut                                       | M cell                      | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [68](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=68:68)    |    100           |
| 17 | CL:0000775 | neutrophil                                          | neutrophil                  | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [77](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=77:77)    |     86.1242      |
| 18 | CL:0000235 | macrophage                                          | macrophage                  | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [74](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=74:74)    |     66.4327      |
| 19 | CL:0000057 | fibroblast                                          | fibroblasts                 | UBERON:0003336 | serosa of duodenum      | serosa                                               | [95](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=95:95)    |      2.59986e-14 |
| 20 | CL:0000115 | endothelial cell                                    | endothelial cells           | UBERON:0003336 | serosa of duodenum      | serosa                                               | [96](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=96:96)    |      2.59986e-14 |
| 21 | CL:0002088 | interstitial cell of Cajal                          | Interstitial cells of Cajal | UBERON:0012377 | muscle layer of jejunum | muscularis externa                                   | [255](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=255:255) |      2.252e-14   |
| 22 | CL:0000115 | endothelial cell                                    | endothelial                 | UBERON:0012377 | muscle layer of jejunum | muscularis externa                                   | [257](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=257:257) |      1.2522e-41  |
| 23 | CL:0000115 | endothelial cell                                    | endothelial cells           | UBERON:0003337 | serosa of jejunum       | serosa                                               | [263](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=263:263) |      1.2522e-41  |
| 25 | CL:1000344 | paneth cell of epithelium proper of small intestine | Paneth cell                 | UBERON:0008346 | duodenal epithelium     | Epithelium                                           | [55](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=55:55)    |    nan           |
| 26 | CL:0009080 | tuft cell of small intestine                        | tuft cell                   | UBERON:0008346 | duodenal epithelium     | Epithelium                                           | [57](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=57:57)    |    nan           |
| 27 | CL:0000097 | mast cell                                           | mast cell                   | UBERON:0015834 | duodenum lamina propria | Lamina propria/Gut associated lymphoid tissue (GALT) | [76](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=76:76)    |    nan           |
| 30 | CL:1000344 | paneth cell of epithelium proper of small intestine | Paneth                      | UBERON:0000400 | jejunal epithelium      | Epithelium                                           | [224](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=224:224) |    nan           |
| 31 | CL:0009080 | tuft cell of small intestine                        | Tuft cells                  | UBERON:0000400 | jejunal epithelium      | Epithelium                                           | [229](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=229:229) |    nan           |
| 32 | CL:0000115 | endothelial cell                                    | endothelial                 | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [230](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=230:230) |    nan           |
| 33 | CL:0000186 | myofibroblast                                       | myofibroblasts              | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [232](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=232:232) |    nan           |
| 34 | CL:0000057 | fibroblast                                          | fibroblasts                 | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [233](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=233:233) |    nan           |
| 35 | CL:0000682 | M cell of gut                                       | M cell                      | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [235](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=235:235) |    nan           |
| 36 | CL:0000236 | B cell                                              | B cell                      | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [236](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=236:236) |    nan           |
| 37 | CL:0000786 | plasma cell                                         | plasma                      | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [237](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=237:237) |    nan           |
| 38 | CL:0000235 | macrophage                                          | macrophages                 | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [241](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=241:241) |    nan           |
| 39 | CL:0000771 | eosinophil                                          | eosinophils                 | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [242](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=242:242) |    nan           |
| 40 | CL:0000097 | mast cell                                           | mast cells                  | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [243](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=243:243) |    nan           |
| 41 | CL:0000775 | neutrophil                                          | neutrophils                 | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [244](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=244:244) |    nan           |
| 42 | CL:0000623 | natural killer cell                                 | NK cells                    | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [245](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=245:245) |    nan           |
| 43 | CL:0000451 | dendritic cell                                      | DCs                         | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [246](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=246:246) |    nan           |
| 44 | CL:0001065 | innate lymphoid cell                                | ILCs                        | UBERON:0000399 | jejunal mucosa          | mucosa                                               | [247](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=247:247) |    nan           |
| 45 | CL:0000057 | fibroblast                                          | fibroblasts                 | UBERON:0012377 | muscle layer of jejunum | muscularis externa                                   | [256](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=256:256) |    nan           |
| 46 | CL:0000057 | fibroblast                                          | fibroblasts                 | UBERON:0003337 | serosa of jejunum       | serosa                                               | [262](https://docs.google.com/spreadsheets/d/1KMOjJj-bVAqo39KuIOo0SaIVRtW9-5C5Y65NwnXlGqw/edit#gid=247140941&range=262:262) |    nan           |




# New CL terms
[**Report**](new_cl_terms_Small_intestine.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Small_intestine.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Small_intestine_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Small_intestine_AS_has_part_CT_log.tsv)