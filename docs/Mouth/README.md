
ASCT+B Validation Reports for Mouth (2026-02-04)
================================================

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
  
1. The term _[UBERON:0004923](http://purl.obolibrary.org/obo/UBERON_0004923)_ has a different name/label in the source ontology in the following 1 row _[31](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=31:31)_. The name/label in the **ASCT+B table** is _mucosa of the lip_ and the one in the **ontology** is _organ component layer_. For reference, the given name/label **by SMEs** is _mucosa of the lip_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols4/index).

You can find more information on the [New CL terms](#new-cl-terms) or [New UBERON terms](#new-uberon-terms) reports.  
  
1. No term id was found for the name/label _tongue_ in the following 1 row _[11](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=11:11)_.

1. No term id was found for the name/label _gingival attachment_ in the following 18 rows _[12](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=12:12)_, _[13](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=13:13)_, _[14](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=14:14)_, _[15](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=15:15)_, _[16](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=16:16)_, _[17](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=17:17)_, _[18](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=18:18)_, _[19](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=19:19)_, _[20](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=20:20)_, _[21](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=21:21)_, _[22](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=22:22)_, _[23](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=23:23)_, _[24](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=24:24)_, _[25](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=25:25)_, _[26](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=26:26)_, _[27](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=27:27)_, _[28](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=28:28)_, _[29](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=29:29)_.

1. No term id was found for the name/label _junctional epithelium cell_ in the following 1 row _[29](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=29:29)_.

1. No term id was found for the name/label _parotid gland ducto-acinar_ in the following 19 rows _[33](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=33:33)_, _[34](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=34:34)_, _[35](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=35:35)_, _[36](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=36:36)_, _[37](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=37:37)_, _[38](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=38:38)_, _[39](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=39:39)_, _[40](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=40:40)_, _[41](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=41:41)_, _[42](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=42:42)_, _[43](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=43:43)_, _[44](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=44:44)_, _[45](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=45:45)_, _[46](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=46:46)_, _[47](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=47:47)_, _[48](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=48:48)_, _[49](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=49:49)_, _[50](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=50:50)_, _[51](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=51:51)_.

1. No term id was found for the name/label _basal ductal cell_ in the following 2 rows _[34](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=34:34)_, _[68](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=68:68)_.

1. No term id was found for the name/label _helper T_ in the following 3 rows _[37](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=37:37)_, _[55](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=55:55)_, _[72](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=72:72)_.

1. No term id was found for the name/label _ionocyte_ in the following 3 rows _[39](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=39:39)_, _[57](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=57:57)_, _[74](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=74:74)_.

1. No term id was found for the name/label _myoepithelial cell_ in the following 3 rows _[42](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=42:42)_, _[61](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=61:61)_, _[78](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=78:78)_.

1. No term id was found for the name/label _periacinar fibroblast_ in the following 3 rows _[43](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=43:43)_, _[62](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=62:62)_, _[79](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=79:79)_.

1. No term id was found for the name/label _periductal fibroblast_ in the following 3 rows _[45](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=45:45)_, _[64](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=64:64)_, _[81](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=81:81)_.

1. No term id was found for the name/label _serous acinar cell_ in the following 1 row _[46](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=46:46)_.

1. No term id was found for the name/label _tuft cell_ in the following 2 rows _[48](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=48:48)_, _[84](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=84:84)_.

1. No term id was found for the name/label _excretory duct epithelial cell_ in the following 2 rows _[49](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=49:49)_, _[85](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=85:85)_.

1. No term id was found for the name/label _sublingual gland ducto-acinar_ in the following 16 rows _[52](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=52:52)_, _[53](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=53:53)_, _[54](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=54:54)_, _[55](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=55:55)_, _[56](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=56:56)_, _[57](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=57:57)_, _[58](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=58:58)_, _[59](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=59:59)_, _[60](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=60:60)_, _[61](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=61:61)_, _[62](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=62:62)_, _[63](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=63:63)_, _[64](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=64:64)_, _[65](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=65:65)_, _[66](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=66:66)_, _[67](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=67:67)_.

1. No term id was found for the name/label _demilune acinar cell_ in the following 2 rows _[52](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=52:52)_, _[69](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=69:69)_.

1. No term id was found for the name/label _mucous acinar cell_ in the following 2 rows _[60](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=60:60)_, _[77](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=77:77)_.

1. No term id was found for the name/label _seromucosal acinar cell_ in the following 2 rows _[65](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=65:65)_, _[82](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=82:82)_.

1. No term id was found for the name/label _submandibular gland ducto-acinar_ in the following 20 rows _[68](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=68:68)_, _[69](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=69:69)_, _[70](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=70:70)_, _[71](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=71:71)_, _[72](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=72:72)_, _[73](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=73:73)_, _[74](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=74:74)_, _[75](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=75:75)_, _[76](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=76:76)_, _[77](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=77:77)_, _[78](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=78:78)_, _[79](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=79:79)_, _[80](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=80:80)_, _[81](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=81:81)_, _[82](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=82:82)_, _[83](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=83:83)_, _[84](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=84:84)_, _[85](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=85:85)_, _[86](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=86:86)_, _[87](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=87:87)_.

1. No term id was found for the name/label _excretory duct_ in the following 1 row _[85](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=85:85)_.

1. No term id was found for the name/label _intercalated duct_ in the following 1 row _[86](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=86:86)_.

1. No term id was found for the name/label _striated duct_ in the following 1 row _[87](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=87:87)_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
1. The term _junctional epithelium cell_ without ontology ID has no parent that is from the CL ontology in the following 1 row _[29](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=29:29)_.

1. The term _basal ductal cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[34](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=34:34)_, _[68](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=68:68)_.

1. The term _helper T_ without ontology ID has no parent that is from the CL ontology in the following 3 rows _[37](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=37:37)_, _[55](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=55:55)_, _[72](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=72:72)_.

1. The term _ionocyte_ without ontology ID has no parent that is from the CL ontology in the following 3 rows _[39](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=39:39)_, _[57](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=57:57)_, _[74](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=74:74)_.

1. The term _myoepithelial cell_ without ontology ID has no parent that is from the CL ontology in the following 3 rows _[42](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=42:42)_, _[61](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=61:61)_, _[78](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=78:78)_.

1. The term _periacinar fibroblast_ without ontology ID has no parent that is from the CL ontology in the following 3 rows _[43](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=43:43)_, _[62](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=62:62)_, _[79](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=79:79)_.

1. The term _periductal fibroblast_ without ontology ID has no parent that is from the CL ontology in the following 3 rows _[45](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=45:45)_, _[64](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=64:64)_, _[81](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=81:81)_.

1. The term _serous acinar cell_ without ontology ID has no parent that is from the CL ontology in the following 1 row _[46](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=46:46)_.

1. The term _tuft cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[48](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=48:48)_, _[84](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=84:84)_.

1. The term _excretory duct epithelial cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[49](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=49:49)_, _[85](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=85:85)_.

1. The term _demilune acinar cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[52](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=52:52)_, _[69](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=69:69)_.

1. The term _mucous acinar cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[60](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=60:60)_, _[77](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=77:77)_.

1. The term _seromucosal acinar cell_ without ontology ID has no parent that is from the CL ontology in the following 2 rows _[65](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=65:65)_, _[82](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=82:82)_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Same case for Anatomic Ontology for Human Lung Maturation (LMHA) and Interlex IDs (ILX) from Stimulating Peripheral Activity to Relieve Conditions (SPARC). You can request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols4/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols4/ontologies/pcl).  
  
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



|    | s                                                               | slabel                | user_slabel                         | o                                                               | olabel               | user_olabel          | row_number                                                                                                       |   deltaIC |
|----|-----------------------------------------------------------------|-----------------------|-------------------------------------|-----------------------------------------------------------------|----------------------|----------------------|------------------------------------------------------------------------------------------------------------------|-----------|
|  2 | [UBERON:0004923](http://purl.obolibrary.org/obo/UBERON_0004923) | organ component layer | mucosa of the lip                   | [UBERON:0003729](http://purl.obolibrary.org/obo/UBERON_0003729) | mouth mucosa         | mouth mucosa         | [31](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=31:31) |   23.2685 |
| 41 | [UBERON:0013475](http://purl.obolibrary.org/obo/UBERON_0013475) | gustatory gland       | gustatory gland (Von Ebner's gland) | [UBERON:0001830](http://purl.obolibrary.org/obo/UBERON_0001830) | minor salivary gland | minor salivary gland | [92](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=92:92) |  nan      |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|    | s                                                       | slabel                              | user_slabel                       | o                                                               | olabel                          | user_olabel         | row_number                                                                                                       |   deltaIC |
|----|---------------------------------------------------------|-------------------------------------|-----------------------------------|-----------------------------------------------------------------|---------------------------------|---------------------|------------------------------------------------------------------------------------------------------------------|-----------|
|  0 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                    | endothelial cell                  | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland             | submandibular gland | [71](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=71:71) |  24.3174  |
|  1 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                    | endothelial cell                  | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland                | sublingual gland    | [54](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=54:54) |  24.3174  |
|  3 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                    | endothelial cell                  | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland                   | parotid gland       | [36](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=36:36) |  21.103   |
|  4 | [CL:0000115](http://purl.obolibrary.org/obo/CL_0000115) | endothelial cell                    | endothelial cell                  | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [16](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=16:16) |  20.656   |
|  5 | [CL:0000084](http://purl.obolibrary.org/obo/CL_0000084) | T cell                              | T cell                            | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [14](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=14:14) |  17.4089  |
|  6 | [CL:0000236](http://purl.obolibrary.org/obo/CL_0000236) | B cell                              | B cell (non-plasma)               | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [19](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=19:19) |  17.261   |
|  7 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                  | smooth muscle cell                | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland                | sublingual gland    | [66](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=66:66) |  15.0619  |
|  8 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                  | smooth muscle cell                | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland             | submandibular gland | [83](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=83:83) |  15.0619  |
|  9 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                      | dendritic cell                    | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland             | submandibular gland | [70](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=70:70) |  12.5224  |
| 10 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                      | dendritic cell                    | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland                | sublingual gland    | [53](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=53:53) |  12.5224  |
| 11 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                          | macrophage                        | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland                | sublingual gland    | [58](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=58:58) |  12.1754  |
| 12 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                          | macrophage                        | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland             | submandibular gland | [75](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=75:75) |  12.1754  |
| 13 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192) | smooth muscle cell                  | smooth muscle cell                | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland                   | parotid gland       | [47](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=47:47) |  11.8476  |
| 14 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                      | dendritic cell                    | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland                   | parotid gland       | [35](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=35:35) |   9.308   |
| 15 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                          | macrophage                        | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland                   | parotid gland       | [40](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=40:40) |   8.96103 |
| 16 | [CL:0000451](http://purl.obolibrary.org/obo/CL_0000451) | dendritic cell                      | dendritic cell                    | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [22](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=22:22) |   8.86099 |
| 17 | [CL:0000235](http://purl.obolibrary.org/obo/CL_0000235) | macrophage                          | macrophage                        | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [18](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=18:18) |   8.51403 |
| 18 | [CL:0000148](http://purl.obolibrary.org/obo/CL_0000148) | melanocyte                          | melanocyte                        | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [17](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=17:17) |   7.48814 |
| 19 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                            | pericyte                          | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland             | submandibular gland | [80](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=80:80) |   6.36962 |
| 20 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                            | pericyte                          | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland                | sublingual gland    | [63](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=63:63) |   6.36962 |
| 21 | [CL:0000312](http://purl.obolibrary.org/obo/CL_0000312) | keratinocyte                        | keratinocyte                      | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [21](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=21:21) |   5.52234 |
| 22 | [CL:0001065](http://purl.obolibrary.org/obo/CL_0001065) | innate lymphoid cell                | innate lymphoid cell              | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [28](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=28:28) |   5.13737 |
| 23 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                           | mast cell                         | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland                | sublingual gland    | [59](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=59:59) |   5.11041 |
| 24 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                           | mast cell                         | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland             | submandibular gland | [76](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=76:76) |   5.11041 |
| 25 | [CL:0000136](http://purl.obolibrary.org/obo/CL_0000136) | adipocyte                           | adipocyte                         | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland                   | parotid gland       | [33](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=33:33) |   5.06921 |
| 26 | [CL:0000623](http://purl.obolibrary.org/obo/CL_0000623) | natural killer cell                 | NK (natural killer) cells         | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [24](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=24:24) |   4.17895 |
| 27 | [CL:0000775](http://purl.obolibrary.org/obo/CL_0000775) | neutrophil                          | neutrophil                        | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [25](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=25:25) |   3.32339 |
| 28 | [CL:0000669](http://purl.obolibrary.org/obo/CL_0000669) | pericyte                            | pericyte                          | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland                   | parotid gland       | [44](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=44:44) |   3.15526 |
| 29 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                           | mast cell                         | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland                   | parotid gland       | [41](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=41:41) |   1.89606 |
| 30 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097) | mast cell                           | mast cell                         | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [15](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=15:15) |   1.44905 |
| 31 | [CL:0000242](http://purl.obolibrary.org/obo/CL_0000242) | Merkel cell                         | Merkel cell                       | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [20](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=20:20) | nan       |
| 32 | [CL:0000453](http://purl.obolibrary.org/obo/CL_0000453) | Langerhans cell                     | Langerhans cell                   | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [23](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=23:23) | nan       |
| 33 | [CL:0000786](http://purl.obolibrary.org/obo/CL_0000786) | plasma cell                         | plasma cell                       | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [26](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=26:26) | nan       |
| 34 | [CL:0000815](http://purl.obolibrary.org/obo/CL_0000815) | regulatory T cell                   | regulatory T cell (Treg)          | [UBERON:0001828](http://purl.obolibrary.org/obo/UBERON_0001828) | gingiva                         | gingiva             | [27](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=27:27) | nan       |
| 35 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                     | IgA secreting plasma cell         | [UBERON:0001831](http://purl.obolibrary.org/obo/UBERON_0001831) | parotid gland                   | parotid gland       | [38](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=38:38) | nan       |
| 36 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland | intercalated duct epithelial cell | [UBERON:0035046](http://purl.obolibrary.org/obo/UBERON_0035046) | parotid gland intercalated duct | intercalated duct   | [50](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=50:50) | nan       |
| 37 | [CL:4052049](http://purl.obolibrary.org/obo/CL_4052049) | striated cell of salivary gland     | striated duct epithelial cell     | [UBERON:0035047](http://purl.obolibrary.org/obo/UBERON_0035047) | parotid gland striated duct     | striated duct       | [51](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=51:51) | nan       |
| 38 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                     | IgA secreting plasma cell         | [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832) | sublingual gland                | sublingual gland    | [56](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=56:56) | nan       |
| 39 | [CL:4052048](http://purl.obolibrary.org/obo/CL_4052048) | intercalated cell of salivary gland | intercalated duct epithelial cell | [UBERON:0001838](http://purl.obolibrary.org/obo/UBERON_0001838) | sublingual duct                 | intercalated duct   | [67](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=67:67) | nan       |
| 40 | [CL:0000987](http://purl.obolibrary.org/obo/CL_0000987) | IgA plasma cell                     | IgA secreting plasma cell         | [UBERON:0001736](http://purl.obolibrary.org/obo/UBERON_0001736) | submandibular gland             | submandibular gland | [73](https://docs.google.com/spreadsheets/d/1HKK77M1QV2I3uJ6WwKHvVP0tVL7icVTxx25ZZ219Km8/edit#gid=0&range=73:73) | nan       |




# New CL terms
[**Report**](new_cl_terms_Mouth.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Mouth.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Mouth_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Mouth_AS_has_part_CT_log.tsv)