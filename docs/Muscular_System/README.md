
ASCT+B Validation Reports for Muscular_System (2024-12-25)
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


These are the reports related to issues in the terms found in the ASCT+B table. We validate only [CL](https://www.ebi.ac.uk/ols4/ontologies/cl), [UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon) and [PCL](https://www.ebi.ac.uk/ols4/ontologies/pcl) terms.
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


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols4/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
1. No term id was found for the name/label _internal abdominal oblique muscle_ in the following 1 row _[16](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=16:16)_.

1. No term id was found for the name/label _pelvic floor muscle_ in the following 9 rows _[20](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=20:20)_, _[21](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=21:21)_, _[22](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=22:22)_, _[23](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=23:23)_, _[24](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=24:24)_, _[25](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=25:25)_, _[26](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=26:26)_, _[27](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=27:27)_, _[28](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=28:28)_.

1. No term id was found for the name/label _puboanalis muscle_ in the following 1 row _[23](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=23:23)_.

1. No term id was found for the name/label _puboperineales muscle_ in the following 1 row _[25](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=25:25)_.

1. No term id was found for the name/label _external anal sphincter muscle_ in the following 4 rows _[33](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=33:33)_, _[34](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=34:34)_, _[35](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=35:35)_, _[36](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=36:36)_.

1. No term id was found for the name/label _sphincter urethrae muscle_ in the following 1 row _[38](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=38:38)_.

1. No term id was found for the name/label _posterior abdominal wall muscle_ in the following 10 rows _[41](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=41:41)_, _[42](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=42:42)_, _[43](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=43:43)_, _[44](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=44:44)_, _[45](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=45:45)_, _[46](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=46:46)_, _[47](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=47:47)_, _[304](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=304:304)_, _[305](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=305:305)_, _[306](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=306:306)_.

1. No term id was found for the name/label _respiratory diaphragm muscle_ in the following 5 rows _[43](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=43:43)_, _[44](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=44:44)_, _[45](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=45:45)_, _[46](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=46:46)_, _[47](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=47:47)_.

1. No term id was found for the name/label _costal part of respiratory diaphragm muscle_ in the following 1 row _[44](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=44:44)_.

1. No term id was found for the name/label _left crus of lumbar part of respiratory diaphragm muscle_ in the following 1 row _[45](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=45:45)_.

1. No term id was found for the name/label _right crus of lumbar part of respiratory diaphragm muscle_ in the following 1 row _[46](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=46:46)_.

1. No term id was found for the name/label _sternal part of respiratory diaphragm muscle_ in the following 1 row _[47](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=47:47)_.

1. No term id was found for the name/label _spermatic cord muscle_ in the following 2 rows _[48](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=48:48)_, _[49](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=49:49)_.

1. No term id was found for the name/label _palmar interosseous muscle_ in the following 1 row _[76](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=76:76)_.

1. No term id was found for the name/label _flexor digiti minimi brevis muscle_ in the following 2 rows _[78](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=78:78)_, _[330](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=330:330)_.

1. No term id was found for the name/label _opponens digiti minimi muscle_ in the following 1 row _[79](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=79:79)_.

1. No term id was found for the name/label _hypothenar hand muscle_ in the following 2 rows _[81](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=81:81)_, _[82](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=82:82)_.

1. No term id was found for the name/label _iliocostalis cervicalis muscle_ in the following 1 row _[124](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=124:124)_.

1. No term id was found for the name/label _intermediate back muscle_ in the following 3 rows _[133](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=133:133)_, _[134](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=134:134)_, _[135](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=135:135)_.

1. No term id was found for the name/label _segmental back muscle_ in the following 12 rows _[136](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=136:136)_, _[137](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=137:137)_, _[138](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=138:138)_, _[139](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=139:139)_, _[140](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=140:140)_, _[141](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=141:141)_, _[142](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=142:142)_, _[143](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=143:143)_, _[144](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=144:144)_, _[145](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=145:145)_, _[146](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=146:146)_, _[147](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=147:147)_.

1. No term id was found for the name/label _anterior cervical intertransversarii muscle_ in the following 1 row _[137](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=137:137)_.

1. No term id was found for the name/label _interspinales cervicalis muscle_ in the following 1 row _[138](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=138:138)_.

1. No term id was found for the name/label _intertransversarii laterales lumborum muscle_ in the following 3 rows _[141](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=141:141)_, _[142](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=142:142)_, _[143](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=143:143)_.

1. No term id was found for the name/label _dorsal part of intertransversarii laterales lumborum muscle_ in the following 1 row _[142](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=142:142)_.

1. No term id was found for the name/label _ventral part of intertransversarii laterales lumborum muscle_ in the following 1 row _[143](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=143:143)_.

1. No term id was found for the name/label _lateral posterior cervical intertransversarii muscle_ in the following 1 row _[144](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=144:144)_.

1. No term id was found for the name/label _medial lumbar intertransversarii muscle_ in the following 1 row _[145](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=145:145)_.

1. No term id was found for the name/label _medial posterior cervical intertransversarii muscle_ in the following 1 row _[146](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=146:146)_.

1. No term id was found for the name/label _thoracic intertransversarii muscle_ in the following 1 row _[147](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=147:147)_.

1. No term id was found for the name/label _spinotransversales muscle_ in the following 3 rows _[148](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=148:148)_, _[149](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=149:149)_, _[150](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=150:150)_.

1. No term id was found for the name/label _splenius capitus muscle_ in the following 1 row _[149](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=149:149)_.

1. No term id was found for the name/label _superficial back muscle_ in the following 9 rows _[151](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=151:151)_, _[152](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=152:152)_, _[153](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=153:153)_, _[154](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=154:154)_, _[155](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=155:155)_, _[156](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=156:156)_, _[157](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=157:157)_, _[158](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=158:158)_, _[159](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=159:159)_.

1. No term id was found for the name/label _multifidus cervicis muscle_ in the following 1 row _[161](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=161:161)_.

1. No term id was found for the name/label _multifidus lumborum muscle_ in the following 1 row _[162](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=162:162)_.

1. No term id was found for the name/label _multifidus thoracis muscle_ in the following 1 row _[163](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=163:163)_.

1. No term id was found for the name/label _clavicular head of pectoralis major muscle_ in the following 1 row _[173](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=173:173)_.

1. No term id was found for the name/label _sternocostal head of pectoralis major muscle_ in the following 1 row _[174](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=174:174)_.

1. No term id was found for the name/label _thoracic wall muscle_ in the following 9 rows _[179](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=179:179)_, _[180](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=180:180)_, _[181](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=181:181)_, _[182](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=182:182)_, _[183](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=183:183)_, _[184](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=184:184)_, _[185](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=185:185)_, _[186](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=186:186)_, _[187](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=187:187)_.

1. No term id was found for the name/label _levator costarum muscle_ in the following 3 rows _[183](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=183:183)_, _[184](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=184:184)_, _[185](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=185:185)_.

1. No term id was found for the name/label _levatores costarum breves of levator costarum muscle_ in the following 1 row _[184](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=184:184)_.

1. No term id was found for the name/label _levatores costarum longi of levator costarum muscle_ in the following 1 row _[185](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=185:185)_.

1. No term id was found for the name/label _external ear muscle_ in the following 5 rows _[189](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=189:189)_, _[190](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=190:190)_, _[191](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=191:191)_, _[192](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=192:192)_, _[193](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=193:193)_.

1. No term id was found for the name/label _ceratoglossus of hyoglossus muscle_ in the following 1 row _[206](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=206:206)_.

1. No term id was found for the name/label _chondroglossus of hyoglossus muscle_ in the following 1 row _[207](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=207:207)_.

1. No term id was found for the name/label _intrinsic eye muscle_ in the following 4 rows _[209](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=209:209)_, _[210](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=210:210)_, _[211](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=211:211)_, _[212](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=212:212)_.

1. No term id was found for the name/label _inferior longitudinal lingual muscle_ in the following 1 row _[214](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=214:214)_.

1. No term id was found for the name/label _superior longitudinal lingual muscle_ in the following 1 row _[215](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=215:215)_.

1. No term id was found for the name/label _transverse muscle_ in the following 1 row _[216](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=216:216)_.

1. No term id was found for the name/label _vertical muscle_ in the following 1 row _[217](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=217:217)_.

1. No term id was found for the name/label _inferior head of lateral pterygoid muscle_ in the following 1 row _[220](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=220:220)_.

1. No term id was found for the name/label _superior head of lateral pterygoid muscle_ in the following 1 row _[221](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=221:221)_.

1. No term id was found for the name/label _middle ear muscle_ in the following 3 rows _[227](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=227:227)_, _[228](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=228:228)_, _[229](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=229:229)_.

1. No term id was found for the name/label _muscle of facial expression_ in the following 31 rows _[230](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=230:230)_, _[231](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=231:231)_, _[232](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=232:232)_, _[233](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=233:233)_, _[234](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=234:234)_, _[235](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=235:235)_, _[236](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=236:236)_, _[237](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=237:237)_, _[238](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=238:238)_, _[239](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=239:239)_, _[240](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=240:240)_, _[241](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=241:241)_, _[242](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=242:242)_, _[243](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=243:243)_, _[244](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=244:244)_, _[245](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=245:245)_, _[246](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=246:246)_, _[247](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=247:247)_, _[248](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=248:248)_, _[249](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=249:249)_, _[250](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=250:250)_, _[251](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=251:251)_, _[252](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=252:252)_, _[253](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=253:253)_, _[254](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=254:254)_, _[255](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=255:255)_, _[256](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=256:256)_, _[257](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=257:257)_, _[258](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=258:258)_, _[382](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=382:382)_, _[383](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=383:383)_.

1. No term id was found for the name/label _frontal belly of occipitofrontalis muscle_ in the following 1 row _[246](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=246:246)_.

1. No term id was found for the name/label _occipital belly of occipitofrontalis muscle_ in the following 1 row _[247](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=247:247)_.

1. No term id was found for the name/label _musculus uvulae muscle_ in the following 1 row _[261](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=261:261)_.

1. No term id was found for the name/label _tibalis anterior muscle_ in the following 1 row _[269](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=269:269)_.

1. No term id was found for the name/label _articularis genu muscle_ in the following 1 row _[271](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=271:271)_.

1. No term id was found for the name/label _dorsum of foot muscle_ in the following 3 rows _[280](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=280:280)_, _[281](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=281:281)_, _[282](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=282:282)_.

1. No term id was found for the name/label _tensor fascia latae muscle_ in the following 1 row _[292](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=292:292)_.

1. No term id was found for the name/label _lateral compartmet of leg muscle_ in the following 3 rows _[293](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=293:293)_, _[294](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=294:294)_, _[295](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=295:295)_.

1. No term id was found for the name/label _hamstring portion of adductor magnus muscle_ in the following 1 row _[300](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=300:300)_.

1. No term id was found for the name/label _tibalis posterior muscle_ in the following 1 row _[316](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=316:316)_.

1. No term id was found for the name/label _sole of foot muscle_ in the following 13 rows _[323](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=323:323)_, _[324](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=324:324)_, _[325](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=325:325)_, _[326](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=326:326)_, _[327](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=327:327)_, _[328](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=328:328)_, _[329](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=329:329)_, _[330](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=330:330)_, _[331](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=331:331)_, _[332](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=332:332)_, _[333](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=333:333)_, _[334](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=334:334)_, _[335](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=335:335)_.

1. No term id was found for the name/label _plantar interosseous muscle_ in the following 1 row _[334](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=334:334)_.

1. No term id was found for the name/label _anterior vertebral muscle_ in the following 4 rows _[337](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=337:337)_, _[338](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=338:338)_, _[339](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=339:339)_, _[340](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=340:340)_.

1. No term id was found for the name/label _longus capitus muscle_ in the following 1 row _[338](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=338:338)_.

1. No term id was found for the name/label _rectus capitus anterior muscle_ in the following 1 row _[340](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=340:340)_.

1. No term id was found for the name/label _circular pharyngeal muscle_ in the following 12 rows _[341](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=341:341)_, _[342](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=342:342)_, _[343](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=343:343)_, _[344](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=344:344)_, _[345](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=345:345)_, _[346](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=346:346)_, _[347](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=347:347)_, _[348](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=348:348)_, _[349](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=349:349)_, _[350](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=350:350)_, _[351](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=351:351)_, _[352](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=352:352)_.

1. No term id was found for the name/label _thyropharyngeal part of inferior pharyngeal constrictor muscle_ in the following 1 row _[344](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=344:344)_.

1. No term id was found for the name/label _pteryopharyngeal part of superior pharyngeal constrictor muscle_ in the following 1 row _[352](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=352:352)_.

1. No term id was found for the name/label _aryepiglottic part of oblique arytenoid muscle_ in the following 1 row _[366](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=366:366)_.

1. No term id was found for the name/label _thyroepiglottic part of thyroarytenoid muscle_ in the following 1 row _[369](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=369:369)_.

1. No term id was found for the name/label _lateral vertebral muscle_ in the following 4 rows _[372](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=372:372)_, _[373](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=373:373)_, _[374](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=374:374)_, _[375](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=375:375)_.

1. No term id was found for the name/label _longitudinal pharyngeal muscle_ in the following 6 rows _[376](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=376:376)_, _[377](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=377:377)_, _[378](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=378:378)_, _[379](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=379:379)_, _[380](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=380:380)_, _[381](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=381:381)_.

1. No term id was found for the name/label _rectus capitius posterior minor muscle_ in the following 1 row _[392](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=392:392)_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
- No issues found.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Same case for Anatomic Ontology for Human Lung Maturation (LMHA) and Interlex IDs (ILX) from Stimulating Peripheral Activity to Relieve Conditions (SPARC). You can request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols4/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols4/ontologies/pcl).  
  
1. The term _FMA:77253_ in the following 1 row _[26](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=26:26)_ is from another ontology that is not validated in this process.

1. The term _FMA:30438_ in the following 1 row _[31](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=31:31)_ is from another ontology that is not validated in this process.

1. The term _FMA:19732_ in the following 1 row _[32](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=32:32)_ is from another ontology that is not validated in this process.

1. The term _FMA:27292_ in the following 1 row _[34](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=34:34)_ is from another ontology that is not validated in this process.

1. The term _FMA:27286_ in the following 1 row _[35](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=35:35)_ is from another ontology that is not validated in this process.

1. The term _FMA:27287_ in the following 1 row _[36](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=36:36)_ is from another ontology that is not validated in this process.

1. The term _FMA:30439_ in the following 1 row _[39](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=39:39)_ is from another ontology that is not validated in this process.

1. The term _FMA:19731_ in the following 1 row _[40](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=40:40)_ is from another ontology that is not validated in this process.

1. The term _FMA:15569_ in the following 1 row _[42](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=42:42)_ is from another ontology that is not validated in this process.

1. The term _FMA:37711_ in the following 7 rows _[51](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=51:51)_, _[52](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=52:52)_, _[53](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=53:53)_, _[54](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=54:54)_, _[55](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=55:55)_, _[56](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=56:56)_, _[57](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=57:57)_ is from another ontology that is not validated in this process.

1. The term _FMA:37701_ in the following 1 row _[52](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=52:52)_ is from another ontology that is not validated in this process.

1. The term _FMA:37670_ in the following 3 rows _[53](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=53:53)_, _[54](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=54:54)_, _[55](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=55:55)_ is from another ontology that is not validated in this process.

1. The term _FMA:37683_ in the following 1 row _[54](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=54:54)_ is from another ontology that is not validated in this process.

1. The term _FMA:37682_ in the following 1 row _[55](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=55:55)_ is from another ontology that is not validated in this process.

1. The term _FMA:38456_ in the following 15 rows _[58](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=58:58)_, _[59](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=59:59)_, _[60](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=60:60)_, _[61](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=61:61)_, _[62](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=62:62)_, _[63](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=63:63)_, _[64](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=64:64)_, _[65](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=65:65)_, _[66](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=66:66)_, _[67](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=67:67)_, _[68](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=68:68)_, _[69](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=69:69)_, _[70](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=70:70)_, _[71](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=71:71)_, _[72](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=72:72)_ is from another ontology that is not validated in this process.

1. The term _FMA:38615_ in the following 1 row _[61](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=61:61)_ is from another ontology that is not validated in this process.

1. The term _FMA:38616_ in the following 1 row _[62](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=62:62)_ is from another ontology that is not validated in this process.

1. The term _FMA:38636_ in the following 1 row _[65](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=65:65)_ is from another ontology that is not validated in this process.

1. The term _FMA:38637_ in the following 1 row _[66](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=66:66)_ is from another ontology that is not validated in this process.

1. The term _FMA:38453_ in the following 1 row _[69](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=69:69)_ is from another ontology that is not validated in this process.

1. The term _FMA:38450_ in the following 3 rows _[70](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=70:70)_, _[71](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=71:71)_, _[72](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=72:72)_ is from another ontology that is not validated in this process.

1. The term _FMA:38558_ in the following 1 row _[71](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=71:71)_ is from another ontology that is not validated in this process.

1. The term _FMA:38559_ in the following 1 row _[72](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=72:72)_ is from another ontology that is not validated in this process.

1. The term _FMA:37418_ in the following 1 row _[74](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=74:74)_ is from another ontology that is not validated in this process.

1. The term _FMA:37385_ in the following 1 row _[75](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=75:75)_ is from another ontology that is not validated in this process.

1. The term _FMA:321806_ in the following 4 rows _[77](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=77:77)_, _[78](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=78:78)_, _[79](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=79:79)_, _[80](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=80:80)_ is from another ontology that is not validated in this process.

1. The term _FMA:37382_ in the following 2 rows _[82](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=82:82)_, _[324](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=324:324)_ is from another ontology that is not validated in this process.

1. The term _FMA:37712_ in the following 6 rows _[83](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=83:83)_, _[84](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=84:84)_, _[85](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=85:85)_, _[86](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=86:86)_, _[87](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=87:87)_, _[88](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=88:88)_ is from another ontology that is not validated in this process.

1. The term _FMA:37694_ in the following 1 row _[86](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=86:86)_ is from another ontology that is not validated in this process.

1. The term _FMA:37692_ in the following 1 row _[87](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=87:87)_ is from another ontology that is not validated in this process.

1. The term _FMA:37693_ in the following 1 row _[88](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=88:88)_ is from another ontology that is not validated in this process.

1. The term _FMA:38488_ in the following 14 rows _[89](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=89:89)_, _[90](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=90:90)_, _[91](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=91:91)_, _[92](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=92:92)_, _[93](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=93:93)_, _[94](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=94:94)_, _[95](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=95:95)_, _[96](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=96:96)_, _[97](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=97:97)_, _[98](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=98:98)_, _[99](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=99:99)_, _[100](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=100:100)_, _[101](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=101:101)_, _[102](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=102:102)_ is from another ontology that is not validated in this process.

1. The term _FMA:38515_ in the following 1 row _[90](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=90:90)_ is from another ontology that is not validated in this process.

1. The term _FMA:77260_ in the following 1 row _[95](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=95:95)_ is from another ontology that is not validated in this process.

1. The term _FMA:77261_ in the following 1 row _[96](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=96:96)_ is from another ontology that is not validated in this process.

1. The term _FMA:38500_ in the following 1 row _[98](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=98:98)_ is from another ontology that is not validated in this process.

1. The term _FMA:38524_ in the following 1 row _[99](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=99:99)_ is from another ontology that is not validated in this process.

1. The term _FMA:34678_ in the following 1 row _[105](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=105:105)_ is from another ontology that is not validated in this process.

1. The term _FMA:34677_ in the following 1 row _[106](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=106:106)_ is from another ontology that is not validated in this process.

1. The term _FMA:34679_ in the following 1 row _[107](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=107:107)_ is from another ontology that is not validated in this process.

1. The term _FMA:321805_ in the following 9 rows _[113](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=113:113)_, _[114](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=114:114)_, _[115](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=115:115)_, _[116](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=116:116)_, _[117](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=117:117)_, _[118](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=118:118)_, _[119](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=119:119)_, _[120](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=120:120)_, _[121](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=121:121)_ is from another ontology that is not validated in this process.

1. The term _FMA:46119_ in the following 1 row _[116](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=116:116)_ is from another ontology that is not validated in this process.

1. The term _FMA:46120_ in the following 1 row _[117](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=117:117)_ is from another ontology that is not validated in this process.

1. The term _FMA:46107_ in the following 1 row _[119](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=119:119)_ is from another ontology that is not validated in this process.

1. The term _FMA:46104_ in the following 1 row _[120](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=120:120)_ is from another ontology that is not validated in this process.

1. The term _FMA:37379_ in the following 1 row _[121](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=121:121)_ is from another ontology that is not validated in this process.

1. The term _FMA:71302_ in the following 10 rows _[123](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=123:123)_, _[124](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=124:124)_, _[125](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=125:125)_, _[126](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=126:126)_, _[127](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=127:127)_, _[128](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=128:128)_, _[129](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=129:129)_, _[130](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=130:130)_, _[131](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=131:131)_, _[132](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=132:132)_ is from another ontology that is not validated in this process.

1. The term _FMA:22702_ in the following 1 row _[125](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=125:125)_ is from another ontology that is not validated in this process.

1. The term _FMA:22714_ in the following 1 row _[127](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=127:127)_ is from another ontology that is not validated in this process.

1. The term _FMA:13402_ in the following 1 row _[134](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=134:134)_ is from another ontology that is not validated in this process.

1. The term _FMA:13401_ in the following 1 row _[135](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=135:135)_ is from another ontology that is not validated in this process.

1. The term _FMA:71307_ in the following 1 row _[139](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=139:139)_ is from another ontology that is not validated in this process.

1. The term _FMA:71308_ in the following 1 row _[140](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=140:140)_ is from another ontology that is not validated in this process.

1. The term _FMA:22681_ in the following 1 row _[150](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=150:150)_ is from another ontology that is not validated in this process.

1. The term _FMA:13379_ in the following 1 row _[154](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=154:154)_ is from another ontology that is not validated in this process.

1. The term _FMA:13380_ in the following 1 row _[155](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=155:155)_ is from another ontology that is not validated in this process.

1. The term _FMA:32555_ in the following 1 row _[157](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=157:157)_ is from another ontology that is not validated in this process.

1. The term _FMA:32557_ in the following 1 row _[158](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=158:158)_ is from another ontology that is not validated in this process.

1. The term _FMA:32556_ in the following 1 row _[159](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=159:159)_ is from another ontology that is not validated in this process.

1. The term _FMA:23082_ in the following 1 row _[164](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=164:164)_ is from another ontology that is not validated in this process.

1. The term _FMA:23083_ in the following 1 row _[165](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=165:165)_ is from another ontology that is not validated in this process.

1. The term _FMA:22830_ in the following 1 row _[166](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=166:166)_ is from another ontology that is not validated in this process.

1. The term _FMA:22829_ in the following 1 row _[167](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=167:167)_ is from another ontology that is not validated in this process.

1. The term _FMA:22828_ in the following 1 row _[168](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=168:168)_ is from another ontology that is not validated in this process.

1. The term _FMA:34699_ in the following 1 row _[172](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=172:172)_ is from another ontology that is not validated in this process.

1. The term _FMA:13410_ in the following 1 row _[178](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=178:178)_ is from another ontology that is not validated in this process.

1. The term _FMA:9760_ in the following 1 row _[187](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=187:187)_ is from another ontology that is not validated in this process.

1. The term _FMA:46856_ in the following 1 row _[190](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=190:190)_ is from another ontology that is not validated in this process.

1. The term _FMA:48962_ in the following 1 row _[191](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=191:191)_ is from another ontology that is not validated in this process.

1. The term _FMA:46855_ in the following 1 row _[192](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=192:192)_ is from another ontology that is not validated in this process.

1. The term _FMA:46753_ in the following 1 row _[193](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=193:193)_ is from another ontology that is not validated in this process.

1. The term _FMA:49041_ in the following 1 row _[198](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=198:198)_ is from another ontology that is not validated in this process.

1. The term _FMA:46692_ in the following 1 row _[208](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=208:208)_ is from another ontology that is not validated in this process.

1. The term _FMA:49157_ in the following 1 row _[212](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=212:212)_ is from another ontology that is not validated in this process.

1. The term _FMA:46794_ in the following 1 row _[232](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=232:232)_ is from another ontology that is not validated in this process.

1. The term _FMA:46816_ in the following 1 row _[234](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=234:234)_ is from another ontology that is not validated in this process.

1. The term _FMA:46777_ in the following 1 row _[235](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=235:235)_ is from another ontology that is not validated in this process.

1. The term _FMA:46798_ in the following 1 row _[236](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=236:236)_ is from another ontology that is not validated in this process.

1. The term _FMA:46802_ in the following 1 row _[238](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=238:238)_ is from another ontology that is not validated in this process.

1. The term _FMA:46805_ in the following 1 row _[239](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=239:239)_ is from another ontology that is not validated in this process.

1. The term _FMA:322110_ in the following 1 row _[241](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=241:241)_ is from another ontology that is not validated in this process.

1. The term _FMA:46773_ in the following 1 row _[243](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=243:243)_ is from another ontology that is not validated in this process.

1. The term _FMA:46772_ in the following 1 row _[244](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=244:244)_ is from another ontology that is not validated in this process.

1. The term _FMA:46781_ in the following 1 row _[249](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=249:249)_ is from another ontology that is not validated in this process.

1. The term _FMA:46784_ in the following 1 row _[250](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=250:250)_ is from another ontology that is not validated in this process.

1. The term _FMA:323230_ in the following 1 row _[252](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=252:252)_ is from another ontology that is not validated in this process.

1. The term _FMA:276073_ in the following 1 row _[253](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=253:253)_ is from another ontology that is not validated in this process.

1. The term _FMA:46769_ in the following 1 row _[254](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=254:254)_ is from another ontology that is not validated in this process.

1. The term _FMA:46727_ in the following 1 row _[260](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=260:260)_ is from another ontology that is not validated in this process.

1. The term _FMA:22472_ in the following 5 rows _[265](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=265:265)_, _[266](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=266:266)_, _[267](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=267:267)_, _[268](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=268:268)_, _[269](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=269:269)_ is from another ontology that is not validated in this process.

1. The term _FMA:22533_ in the following 1 row _[267](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=267:267)_ is from another ontology that is not validated in this process.

1. The term _FMA:22538_ in the following 1 row _[268](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=268:268)_ is from another ontology that is not validated in this process.

1. The term _FMA:22424_ in the following 10 rows _[270](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=270:270)_, _[271](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=271:271)_, _[272](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=272:272)_, _[273](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=273:273)_, _[274](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=274:274)_, _[275](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=275:275)_, _[276](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=276:276)_, _[277](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=277:277)_, _[278](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=278:278)_, _[279](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=279:279)_ is from another ontology that is not validated in this process.

1. The term _FMA:22430_ in the following 3 rows _[273](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=273:273)_, _[274](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=274:274)_, _[275](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=275:275)_ is from another ontology that is not validated in this process.

1. The term _FMA:22436_ in the following 1 row _[274](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=274:274)_ is from another ontology that is not validated in this process.

1. The term _FMA:22435_ in the following 1 row _[275](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=275:275)_ is from another ontology that is not validated in this process.

1. The term _FMA:22433_ in the following 1 row _[277](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=277:277)_ is from another ontology that is not validated in this process.

1. The term _FMA:51141_ in the following 1 row _[282](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=282:282)_ is from another ontology that is not validated in this process.

1. The term _FMA:22315_ in the following 1 row _[285](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=285:285)_ is from another ontology that is not validated in this process.

1. The term _FMA:22298_ in the following 1 row _[288](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=288:288)_ is from another ontology that is not validated in this process.

1. The term _FMA:22321_ in the following 1 row _[290](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=290:290)_ is from another ontology that is not validated in this process.

1. The term _FMA:22540_ in the following 1 row _[294](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=294:294)_ is from another ontology that is not validated in this process.

1. The term _FMA:22539_ in the following 1 row _[295](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=295:295)_ is from another ontology that is not validated in this process.

1. The term _FMA:22439_ in the following 8 rows _[296](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=296:296)_, _[297](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=297:297)_, _[298](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=298:298)_, _[299](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=299:299)_, _[300](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=300:300)_, _[301](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=301:301)_, _[302](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=302:302)_, _[303](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=303:303)_ is from another ontology that is not validated in this process.

1. The term _FMA:22299_ in the following 1 row _[302](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=302:302)_ is from another ontology that is not validated in this process.

1. The term _FMA:22474_ in the following 10 rows _[307](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=307:307)_, _[308](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=308:308)_, _[309](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=309:309)_, _[310](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=310:310)_, _[311](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=311:311)_, _[312](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=312:312)_, _[313](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=313:313)_, _[314](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=314:314)_, _[315](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=315:315)_, _[316](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=316:316)_ is from another ontology that is not validated in this process.

1. The term _FMA:51071_ in the following 1 row _[308](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=308:308)_ is from another ontology that is not validated in this process.

1. The term _FMA:22543_ in the following 1 row _[313](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=313:313)_ is from another ontology that is not validated in this process.

1. The term _FMA:22427_ in the following 6 rows _[317](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=317:317)_, _[318](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=318:318)_, _[319](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=319:319)_, _[320](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=320:320)_, _[321](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=321:321)_, _[322](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=322:322)_ is from another ontology that is not validated in this process.

1. The term _FMA:45887_ in the following 1 row _[319](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=319:319)_ is from another ontology that is not validated in this process.

1. The term _FMA:45890_ in the following 1 row _[320](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=320:320)_ is from another ontology that is not validated in this process.

1. The term _FMA:46014_ in the following 1 row _[327](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=327:327)_ is from another ontology that is not validated in this process.

1. The term _FMA:46015_ in the following 1 row _[328](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=328:328)_ is from another ontology that is not validated in this process.

1. The term _FMA:37457_ in the following 1 row _[329](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=329:329)_ is from another ontology that is not validated in this process.

1. The term _FMA:37453_ in the following 1 row _[333](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=333:333)_ is from another ontology that is not validated in this process.

1. The term _FMA:37452_ in the following 1 row _[335](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=335:335)_ is from another ontology that is not validated in this process.

1. The term _FMA:46623_ in the following 3 rows _[342](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=342:342)_, _[343](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=343:343)_, _[344](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=344:344)_ is from another ontology that is not validated in this process.

1. The term _FMA:46622_ in the following 3 rows _[345](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=345:345)_, _[346](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=346:346)_, _[347](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=347:347)_ is from another ontology that is not validated in this process.

1. The term _FMA:46654_ in the following 1 row _[346](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=346:346)_ is from another ontology that is not validated in this process.

1. The term _FMA:46651_ in the following 1 row _[347](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=347:347)_ is from another ontology that is not validated in this process.

1. The term _FMA:46621_ in the following 5 rows _[348](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=348:348)_, _[349](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=349:349)_, _[350](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=350:350)_, _[351](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=351:351)_, _[352](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=352:352)_ is from another ontology that is not validated in this process.

1. The term _FMA:46641_ in the following 1 row _[349](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=349:349)_ is from another ontology that is not validated in this process.

1. The term _FMA:46647_ in the following 1 row _[350](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=350:350)_ is from another ontology that is not validated in this process.

1. The term _FMA:46644_ in the following 1 row _[351](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=351:351)_ is from another ontology that is not validated in this process.

1. The term _FMA:46341_ in the following 1 row _[355](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=355:355)_ is from another ontology that is not validated in this process.

1. The term _FMA:46340_ in the following 1 row _[356](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=356:356)_ is from another ontology that is not validated in this process.

1. The term _FMA:46610_ in the following 1 row _[362](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=362:362)_ is from another ontology that is not validated in this process.

1. The term _FMA:46609_ in the following 1 row _[363](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=363:363)_ is from another ontology that is not validated in this process.

1. The term _FMA:46583_ in the following 2 rows _[365](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=365:365)_, _[366](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=366:366)_ is from another ontology that is not validated in this process.

1. The term _FMA:46588_ in the following 2 rows _[368](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=368:368)_, _[369](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=369:369)_ is from another ontology that is not validated in this process.

1. The term _FMA:46582_ in the following 1 row _[370](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=370:370)_ is from another ontology that is not validated in this process.

1. The term _FMA:13385_ in the following 1 row _[373](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=373:373)_ is from another ontology that is not validated in this process.

1. The term _FMA:13387_ in the following 1 row _[375](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=375:375)_ is from another ontology that is not validated in this process.

1. The term _FMA:46683_ in the following 1 row _[378](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=378:378)_ is from another ontology that is not validated in this process.

1. The term _FMA:46684_ in the following 1 row _[379](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=379:379)_ is from another ontology that is not validated in this process.

1. The term _FMA:45776_ in the following 1 row _[386](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=386:386)_ is from another ontology that is not validated in this process.

1. The term _FMA:13460_ in the following 1 row _[387](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=387:387)_ is from another ontology that is not validated in this process.

1. The term _FMA:71439_ in the following 5 rows _[388](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=388:388)_, _[389](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=389:389)_, _[390](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=390:390)_, _[391](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=391:391)_, _[392](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=392:392)_ is from another ontology that is not validated in this process.

1. The term _FMA:32528_ in the following 1 row _[389](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=389:389)_ is from another ontology that is not validated in this process.

1. The term _FMA:32527_ in the following 1 row _[390](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=390:390)_ is from another ontology that is not validated in this process.

1. The term _FMA:46291_ in the following 3 rows _[394](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=394:394)_, _[395](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=395:395)_, _[396](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=396:396)_ is from another ontology that is not validated in this process.


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



|     | row_number                                                                                                          | s                                                               | slabel                     | user_slabel               | o                                                               | olabel            | user_olabel    |   deltaIC |
|-----|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|----------------------------|---------------------------|-----------------------------------------------------------------|-------------------|----------------|-----------|
|  33 | [170](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=170:170) | [UBERON:0001495](http://purl.obolibrary.org/obo/UBERON_0001495) | pectoral muscle            | pectoral muscle           | [UBERON:0002426](http://purl.obolibrary.org/obo/UBERON_0002426) | chest muscle      | chest muscle   |  18.6649  |
|  34 | [171](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=171:171) | [UBERON:0001495](http://purl.obolibrary.org/obo/UBERON_0001495) | pectoral muscle            | pectoral muscle           | [UBERON:0002426](http://purl.obolibrary.org/obo/UBERON_0002426) | chest muscle      | chest muscle   |  18.6649  |
|  35 | [172](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=172:172) | [UBERON:0001495](http://purl.obolibrary.org/obo/UBERON_0001495) | pectoral muscle            | pectoral muscle           | [UBERON:0002426](http://purl.obolibrary.org/obo/UBERON_0002426) | chest muscle      | chest muscle   |  18.6649  |
|  36 | [173](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=173:173) | [UBERON:0001495](http://purl.obolibrary.org/obo/UBERON_0001495) | pectoral muscle            | pectoral muscle           | [UBERON:0002426](http://purl.obolibrary.org/obo/UBERON_0002426) | chest muscle      | chest muscle   |  18.6649  |
|  37 | [175](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=175:175) | [UBERON:0001495](http://purl.obolibrary.org/obo/UBERON_0001495) | pectoral muscle            | pectoral muscle           | [UBERON:0002426](http://purl.obolibrary.org/obo/UBERON_0002426) | chest muscle      | chest muscle   |  18.6649  |
|  38 | [174](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=174:174) | [UBERON:0001495](http://purl.obolibrary.org/obo/UBERON_0001495) | pectoral muscle            | pectoral muscle           | [UBERON:0002426](http://purl.obolibrary.org/obo/UBERON_0002426) | chest muscle      | chest muscle   |  18.6649  |
|  39 | [177](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=177:177) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0002426](http://purl.obolibrary.org/obo/UBERON_0002426) | chest muscle      | chest muscle   |  15.6965  |
|  40 | [176](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=176:176) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0002426](http://purl.obolibrary.org/obo/UBERON_0002426) | chest muscle      | chest muscle   |  15.6965  |
|  41 | [178](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=178:178) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0002426](http://purl.obolibrary.org/obo/UBERON_0002426) | chest muscle      | chest muscle   |  15.6965  |
|  42 | [108](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=108:108) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     |   1.86152 |
|  43 | [109](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=109:109) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     |   1.86152 |
|  44 | [106](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=106:106) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     |   1.86152 |
|  45 | [105](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=105:105) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     |   1.86152 |
|  46 | [104](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=104:104) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     |   1.86152 |
|  47 | [103](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=103:103) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     |   1.86152 |
|  48 | [110](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=110:110) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     |   1.86152 |
|  49 | [111](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=111:111) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     |   1.86152 |
|  50 | [112](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=112:112) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     |   1.86152 |
|  51 | [107](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=107:107) | [UBERON:0001482](http://purl.obolibrary.org/obo/UBERON_0001482) | muscle of shoulder         | shoulder muscle           | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     |   1.86152 |
|  52 | [29](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=29:29)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  53 | [30](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=30:30)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  54 | [31](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=31:31)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  55 | [32](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=32:32)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  56 | [33](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=33:33)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  57 | [34](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=34:34)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  58 | [35](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=35:35)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  59 | [36](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=36:36)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  60 | [37](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=37:37)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  61 | [38](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=38:38)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  62 | [39](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=39:39)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  63 | [40](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=40:40)    | [UBERON:0002379](http://purl.obolibrary.org/obo/UBERON_0002379) | perineal muscle            | perineal muscle           | [UBERON:0002378](http://purl.obolibrary.org/obo/UBERON_0002378) | muscle of abdomen | abdomen muscle | nan       |
|  64 | [73](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=73:73)    | [UBERON:0001500](http://purl.obolibrary.org/obo/UBERON_0001500) | muscle of manus            | hand muscle               | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     | nan       |
|  65 | [74](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=74:74)    | [UBERON:0001500](http://purl.obolibrary.org/obo/UBERON_0001500) | muscle of manus            | hand muscle               | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     | nan       |
|  66 | [75](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=75:75)    | [UBERON:0001500](http://purl.obolibrary.org/obo/UBERON_0001500) | muscle of manus            | hand muscle               | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     | nan       |
|  67 | [76](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=76:76)    | [UBERON:0001500](http://purl.obolibrary.org/obo/UBERON_0001500) | muscle of manus            | hand muscle               | [UBERON:0001499](http://purl.obolibrary.org/obo/UBERON_0001499) | muscle of arm     | arm muscle     | nan       |
|  68 | [160](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=160:160) | [UBERON:0010990](http://purl.obolibrary.org/obo/UBERON_0010990) | transversospinales muscle  | transversospinales muscle | [UBERON:0002324](http://purl.obolibrary.org/obo/UBERON_0002324) | muscle of back    | back muscle    | nan       |
|  69 | [161](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=161:161) | [UBERON:0010990](http://purl.obolibrary.org/obo/UBERON_0010990) | transversospinales muscle  | transversospinales muscle | [UBERON:0002324](http://purl.obolibrary.org/obo/UBERON_0002324) | muscle of back    | back muscle    | nan       |
|  70 | [162](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=162:162) | [UBERON:0010990](http://purl.obolibrary.org/obo/UBERON_0010990) | transversospinales muscle  | transversospinales muscle | [UBERON:0002324](http://purl.obolibrary.org/obo/UBERON_0002324) | muscle of back    | back muscle    | nan       |
|  71 | [163](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=163:163) | [UBERON:0010990](http://purl.obolibrary.org/obo/UBERON_0010990) | transversospinales muscle  | transversospinales muscle | [UBERON:0002324](http://purl.obolibrary.org/obo/UBERON_0002324) | muscle of back    | back muscle    | nan       |
|  72 | [164](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=164:164) | [UBERON:0010990](http://purl.obolibrary.org/obo/UBERON_0010990) | transversospinales muscle  | transversospinales muscle | [UBERON:0002324](http://purl.obolibrary.org/obo/UBERON_0002324) | muscle of back    | back muscle    | nan       |
|  73 | [165](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=165:165) | [UBERON:0010990](http://purl.obolibrary.org/obo/UBERON_0010990) | transversospinales muscle  | transversospinales muscle | [UBERON:0002324](http://purl.obolibrary.org/obo/UBERON_0002324) | muscle of back    | back muscle    | nan       |
|  74 | [166](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=166:166) | [UBERON:0010990](http://purl.obolibrary.org/obo/UBERON_0010990) | transversospinales muscle  | transversospinales muscle | [UBERON:0002324](http://purl.obolibrary.org/obo/UBERON_0002324) | muscle of back    | back muscle    | nan       |
|  75 | [167](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=167:167) | [UBERON:0010990](http://purl.obolibrary.org/obo/UBERON_0010990) | transversospinales muscle  | transversospinales muscle | [UBERON:0002324](http://purl.obolibrary.org/obo/UBERON_0002324) | muscle of back    | back muscle    | nan       |
|  76 | [168](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=168:168) | [UBERON:0010990](http://purl.obolibrary.org/obo/UBERON_0010990) | transversospinales muscle  | transversospinales muscle | [UBERON:0002324](http://purl.obolibrary.org/obo/UBERON_0002324) | muscle of back    | back muscle    | nan       |
|  77 | [194](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=194:194) | [UBERON:0001601](http://purl.obolibrary.org/obo/UBERON_0001601) | extra-ocular muscle        | extra-ocular muscle       | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  78 | [195](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=195:195) | [UBERON:0001601](http://purl.obolibrary.org/obo/UBERON_0001601) | extra-ocular muscle        | extra-ocular muscle       | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  79 | [196](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=196:196) | [UBERON:0001601](http://purl.obolibrary.org/obo/UBERON_0001601) | extra-ocular muscle        | extra-ocular muscle       | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  80 | [197](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=197:197) | [UBERON:0001601](http://purl.obolibrary.org/obo/UBERON_0001601) | extra-ocular muscle        | extra-ocular muscle       | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  81 | [198](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=198:198) | [UBERON:0001601](http://purl.obolibrary.org/obo/UBERON_0001601) | extra-ocular muscle        | extra-ocular muscle       | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  82 | [199](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=199:199) | [UBERON:0001601](http://purl.obolibrary.org/obo/UBERON_0001601) | extra-ocular muscle        | extra-ocular muscle       | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  83 | [200](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=200:200) | [UBERON:0001601](http://purl.obolibrary.org/obo/UBERON_0001601) | extra-ocular muscle        | extra-ocular muscle       | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  84 | [201](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=201:201) | [UBERON:0001601](http://purl.obolibrary.org/obo/UBERON_0001601) | extra-ocular muscle        | extra-ocular muscle       | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  85 | [202](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=202:202) | [UBERON:0001601](http://purl.obolibrary.org/obo/UBERON_0001601) | extra-ocular muscle        | extra-ocular muscle       | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  86 | [203](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=203:203) | [UBERON:0001575](http://purl.obolibrary.org/obo/UBERON_0001575) | extrinsic muscle of tongue | extrinsic tongue muscle   | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  87 | [204](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=204:204) | [UBERON:0001575](http://purl.obolibrary.org/obo/UBERON_0001575) | extrinsic muscle of tongue | extrinsic tongue muscle   | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  88 | [205](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=205:205) | [UBERON:0001575](http://purl.obolibrary.org/obo/UBERON_0001575) | extrinsic muscle of tongue | extrinsic tongue muscle   | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  89 | [206](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=206:206) | [UBERON:0001575](http://purl.obolibrary.org/obo/UBERON_0001575) | extrinsic muscle of tongue | extrinsic tongue muscle   | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  90 | [207](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=207:207) | [UBERON:0001575](http://purl.obolibrary.org/obo/UBERON_0001575) | extrinsic muscle of tongue | extrinsic tongue muscle   | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  91 | [208](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=208:208) | [UBERON:0001575](http://purl.obolibrary.org/obo/UBERON_0001575) | extrinsic muscle of tongue | extrinsic tongue muscle   | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  92 | [213](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=213:213) | [UBERON:0001576](http://purl.obolibrary.org/obo/UBERON_0001576) | intrinsic muscle of tongue | intrinsic tongue muscle   | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  93 | [214](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=214:214) | [UBERON:0001576](http://purl.obolibrary.org/obo/UBERON_0001576) | intrinsic muscle of tongue | intrinsic tongue muscle   | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  94 | [215](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=215:215) | [UBERON:0001576](http://purl.obolibrary.org/obo/UBERON_0001576) | intrinsic muscle of tongue | intrinsic tongue muscle   | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  95 | [216](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=216:216) | [UBERON:0001576](http://purl.obolibrary.org/obo/UBERON_0001576) | intrinsic muscle of tongue | intrinsic tongue muscle   | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  96 | [217](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=217:217) | [UBERON:0001576](http://purl.obolibrary.org/obo/UBERON_0001576) | intrinsic muscle of tongue | intrinsic tongue muscle   | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  97 | [259](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=259:259) | [UBERON:0003682](http://purl.obolibrary.org/obo/UBERON_0003682) | palatal muscle             | palatal muscle            | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  98 | [260](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=260:260) | [UBERON:0003682](http://purl.obolibrary.org/obo/UBERON_0003682) | palatal muscle             | palatal muscle            | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
|  99 | [261](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=261:261) | [UBERON:0003682](http://purl.obolibrary.org/obo/UBERON_0003682) | palatal muscle             | palatal muscle            | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
| 100 | [262](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=262:262) | [UBERON:0003682](http://purl.obolibrary.org/obo/UBERON_0003682) | palatal muscle             | palatal muscle            | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
| 101 | [263](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=263:263) | [UBERON:0003682](http://purl.obolibrary.org/obo/UBERON_0003682) | palatal muscle             | palatal muscle            | [UBERON:0002376](http://purl.obolibrary.org/obo/UBERON_0002376) | cranial muscle    | cranial muscle | nan       |
| 102 | [283](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=283:283) | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle             | gluteal muscle            | [UBERON:0001383](http://purl.obolibrary.org/obo/UBERON_0001383) | muscle of leg     | leg muscle     | nan       |
| 103 | [284](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=284:284) | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle             | gluteal muscle            | [UBERON:0001383](http://purl.obolibrary.org/obo/UBERON_0001383) | muscle of leg     | leg muscle     | nan       |
| 104 | [285](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=285:285) | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle             | gluteal muscle            | [UBERON:0001383](http://purl.obolibrary.org/obo/UBERON_0001383) | muscle of leg     | leg muscle     | nan       |
| 105 | [286](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=286:286) | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle             | gluteal muscle            | [UBERON:0001383](http://purl.obolibrary.org/obo/UBERON_0001383) | muscle of leg     | leg muscle     | nan       |
| 106 | [287](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=287:287) | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle             | gluteal muscle            | [UBERON:0001383](http://purl.obolibrary.org/obo/UBERON_0001383) | muscle of leg     | leg muscle     | nan       |
| 107 | [287](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=287:287) | [UBERON:0019202](http://purl.obolibrary.org/obo/UBERON_0019202) | inferior gemellus muscle   | inferior gemellus muscle  | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle    | gluteal muscle | nan       |
| 108 | [288](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=288:288) | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle             | gluteal muscle            | [UBERON:0001383](http://purl.obolibrary.org/obo/UBERON_0001383) | muscle of leg     | leg muscle     | nan       |
| 109 | [289](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=289:289) | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle             | gluteal muscle            | [UBERON:0001383](http://purl.obolibrary.org/obo/UBERON_0001383) | muscle of leg     | leg muscle     | nan       |
| 110 | [290](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=290:290) | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle             | gluteal muscle            | [UBERON:0001383](http://purl.obolibrary.org/obo/UBERON_0001383) | muscle of leg     | leg muscle     | nan       |
| 111 | [291](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=291:291) | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle             | gluteal muscle            | [UBERON:0001383](http://purl.obolibrary.org/obo/UBERON_0001383) | muscle of leg     | leg muscle     | nan       |
| 112 | [291](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=291:291) | [UBERON:0019203](http://purl.obolibrary.org/obo/UBERON_0019203) | superior gemellus muscle   | superior gemellus muscle  | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle    | gluteal muscle | nan       |
| 113 | [292](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=292:292) | [UBERON:0002000](http://purl.obolibrary.org/obo/UBERON_0002000) | gluteal muscle             | gluteal muscle            | [UBERON:0001383](http://purl.obolibrary.org/obo/UBERON_0001383) | muscle of leg     | leg muscle     | nan       |
| 114 | [353](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=353:353) | [UBERON:0008523](http://purl.obolibrary.org/obo/UBERON_0008523) | infrahyoid muscle          | infrahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 115 | [354](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=354:354) | [UBERON:0008523](http://purl.obolibrary.org/obo/UBERON_0008523) | infrahyoid muscle          | infrahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 116 | [355](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=355:355) | [UBERON:0008523](http://purl.obolibrary.org/obo/UBERON_0008523) | infrahyoid muscle          | infrahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 117 | [356](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=356:356) | [UBERON:0008523](http://purl.obolibrary.org/obo/UBERON_0008523) | infrahyoid muscle          | infrahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 118 | [357](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=357:357) | [UBERON:0008523](http://purl.obolibrary.org/obo/UBERON_0008523) | infrahyoid muscle          | infrahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 119 | [358](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=358:358) | [UBERON:0008523](http://purl.obolibrary.org/obo/UBERON_0008523) | infrahyoid muscle          | infrahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 120 | [359](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=359:359) | [UBERON:0008523](http://purl.obolibrary.org/obo/UBERON_0008523) | infrahyoid muscle          | infrahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 121 | [384](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=384:384) | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck             | neck muscle               | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 122 | [385](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=385:385) | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck             | neck muscle               | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 123 | [386](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=386:386) | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck             | neck muscle               | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 124 | [387](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=387:387) | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck             | neck muscle               | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 125 | [393](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=393:393) | [UBERON:0008571](http://purl.obolibrary.org/obo/UBERON_0008571) | suprahyoid muscle          | suprahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 126 | [394](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=394:394) | [UBERON:0008571](http://purl.obolibrary.org/obo/UBERON_0008571) | suprahyoid muscle          | suprahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 127 | [395](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=395:395) | [UBERON:0008571](http://purl.obolibrary.org/obo/UBERON_0008571) | suprahyoid muscle          | suprahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 128 | [396](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=396:396) | [UBERON:0008571](http://purl.obolibrary.org/obo/UBERON_0008571) | suprahyoid muscle          | suprahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 129 | [397](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=397:397) | [UBERON:0008571](http://purl.obolibrary.org/obo/UBERON_0008571) | suprahyoid muscle          | suprahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 130 | [398](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=398:398) | [UBERON:0008571](http://purl.obolibrary.org/obo/UBERON_0008571) | suprahyoid muscle          | suprahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |
| 131 | [399](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=399:399) | [UBERON:0008571](http://purl.obolibrary.org/obo/UBERON_0008571) | suprahyoid muscle          | suprahyoid muscle         | [UBERON:0002377](http://purl.obolibrary.org/obo/UBERON_0002377) | muscle of neck    | neck muscle    | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | row_number                                                                                                          | s                                                       | slabel                  | user_slabel          | o                                                               | olabel                              | user_olabel                                                    |   deltaIC |
|----|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|-------------------------|----------------------|-----------------------------------------------------------------|-------------------------------------|----------------------------------------------------------------|-----------|
|  0 | [223](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=223:223) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0010995](http://purl.obolibrary.org/obo/UBERON_0010995) | deep part of masseter muscle        | deep part of masseter muscle                                   |   44.3197 |
|  1 | [355](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=355:355) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001108](http://purl.obolibrary.org/obo/UBERON_0001108) | omohyoid muscle                     | omohyoid muscle                                                |   44.3197 |
|  2 | [202](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=202:202) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0010379](http://purl.obolibrary.org/obo/UBERON_0010379) | superior tarsal muscle              | superior tarsal muscle                                         |   44.3197 |
|  3 | [276](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=276:276) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001373](http://purl.obolibrary.org/obo/UBERON_0001373) | sartorius muscle                    | sartorius muscle                                               |   44.3197 |
|  4 | [311](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=311:311) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0011908](http://purl.obolibrary.org/obo/UBERON_0011908) | gastrocnemius lateralis             | lateral head of gastrocnemius muscle                           |   44.3197 |
|  5 | [312](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=312:312) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0011907](http://purl.obolibrary.org/obo/UBERON_0011907) | gastrocnemius medialis              | medial head of gastrocnemius muscle                            |   44.3197 |
|  6 | [343](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=343:343) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0010928](http://purl.obolibrary.org/obo/UBERON_0010928) | cricopharyngeus muscle              | cricopharyngeal part of inferior pharyngeal constrictor muscle |   44.3197 |
|  7 | [180](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=180:180) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0005441](http://purl.obolibrary.org/obo/UBERON_0005441) | external intercostal muscle         | external intercostal muscle                                    |   44.3197 |
|  8 | [354](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=354:354) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001108](http://purl.obolibrary.org/obo/UBERON_0001108) | omohyoid muscle                     | omohyoid muscle                                                |   44.3197 |
|  9 | [356](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=356:356) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001108](http://purl.obolibrary.org/obo/UBERON_0001108) | omohyoid muscle                     | omohyoid muscle                                                |   44.3197 |
| 10 | [357](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=357:357) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001107](http://purl.obolibrary.org/obo/UBERON_0001107) | sternohyoid muscle                  | sternohyoid muscle                                             |   44.3197 |
| 11 | [358](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=358:358) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001109](http://purl.obolibrary.org/obo/UBERON_0001109) | sternothyroid muscle                | sternothyroid muscle                                           |   44.3197 |
| 12 | [359](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=359:359) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001110](http://purl.obolibrary.org/obo/UBERON_0001110) | thyrohyoid muscle                   | thyrohyoid muscle                                              |   44.3197 |
| 13 | [380](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=380:380) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0010937](http://purl.obolibrary.org/obo/UBERON_0010937) | salpingopharyngeus muscle           | salpingopharyngeus muscle                                      |   44.3197 |
| 14 | [181](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=181:181) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0008617](http://purl.obolibrary.org/obo/UBERON_0008617) | innermost intercostal muscle        | innermost intercostal muscle                                   |   44.3197 |
| 15 | [224](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=224:224) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0011140](http://purl.obolibrary.org/obo/UBERON_0011140) | superficial part of masseter muscle | superficial part of masseter muscle                            |   39.7533 |
| 16 | [381](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=381:381) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0008804](http://purl.obolibrary.org/obo/UBERON_0008804) | stylopharyngeus muscle              | stylopharyngeus muscle                                         |   39.7533 |
| 17 | [182](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=182:182) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0002403](http://purl.obolibrary.org/obo/UBERON_0002403) | internal intercostal muscle         | internal intercostal muscle                                    |   39.7533 |
| 18 | [399](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=399:399) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0008712](http://purl.obolibrary.org/obo/UBERON_0008712) | stylohyoid muscle                   | stylohyoid muscle                                              |   39.7533 |
| 19 | [49](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=49:49)    | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0008488](http://purl.obolibrary.org/obo/UBERON_0008488) | cremaster muscle                    | cremaster muscle                                               |   37.0821 |
| 20 | [397](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=397:397) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001565](http://purl.obolibrary.org/obo/UBERON_0001565) | geniohyoid muscle                   | geniohyoid muscle                                              |   37.0821 |
| 21 | [211](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=211:211) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001608](http://purl.obolibrary.org/obo/UBERON_0001608) | dilatator pupillae                  | dilator pupillae muscle                                        |   37.0821 |
| 22 | [398](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=398:398) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001564](http://purl.obolibrary.org/obo/UBERON_0001564) | mylohyoid muscle                    | mylohyoid muscle                                               |   32.5157 |
| 23 | [248](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=248:248) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001578](http://purl.obolibrary.org/obo/UBERON_0001578) | orbicularis oculi muscle            | orbicularis oculi muscle                                       |   31.5002 |
| 24 | [249](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=249:249) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001578](http://purl.obolibrary.org/obo/UBERON_0001578) | orbicularis oculi muscle            | orbicularis oculi muscle                                       |   31.5002 |
| 25 | [250](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=250:250) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001578](http://purl.obolibrary.org/obo/UBERON_0001578) | orbicularis oculi muscle            | orbicularis oculi muscle                                       |   31.5002 |
| 26 | [210](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=210:210) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0001605](http://purl.obolibrary.org/obo/UBERON_0001605) | ciliary muscle                      | ciliary muscle                                                 |   30.6205 |
| 27 | [353](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=353:353) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0008523](http://purl.obolibrary.org/obo/UBERON_0008523) | infrahyoid muscle                   | infrahyoid muscle                                              |   30.6205 |
| 28 | [245](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=245:245) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0010946](http://purl.obolibrary.org/obo/UBERON_0010946) | occipitofrontalis muscle            | occipitofrontalis muscle                                       |   28.5226 |
| 29 | [246](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=246:246) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0010946](http://purl.obolibrary.org/obo/UBERON_0010946) | occipitofrontalis muscle            | occipitofrontalis muscle                                       |   28.5226 |
| 30 | [247](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=247:247) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0010946](http://purl.obolibrary.org/obo/UBERON_0010946) | occipitofrontalis muscle            | occipitofrontalis muscle                                       |   28.5226 |
| 31 | [394](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=394:394) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0008571](http://purl.obolibrary.org/obo/UBERON_0008571) | suprahyoid muscle                   | suprahyoid muscle                                              |   22.8556 |
| 32 | [393](https://docs.google.com/spreadsheets/d/1o1rFeNs4UQoynU4qL4Bx8Pr6bn2c96__mCCeNtB0_fw/edit#gid=0&range=393:393) | [CL:0000188](http://purl.obolibrary.org/obo/CL_0000188) | cell of skeletal muscle | skeletal muscle cell | [UBERON:0008571](http://purl.obolibrary.org/obo/UBERON_0008571) | suprahyoid muscle                   | suprahyoid muscle                                              |   22.8556 |




# New CL terms
[**Report**](new_cl_terms_Muscular_System.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Muscular_System.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Muscular_System_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Muscular_System_AS_has_part_CT_log.tsv)