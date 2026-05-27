
ASCT+B Validation Reports for Skeleton (2026-05-27)
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


These are the reports related to issues in the terms found in the ASCT+B table. We validate only [CL](https://www.ebi.ac.uk/ols4/ontologies/cl), [UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon) and [PCL](https://www.ebi.ac.uk/ols4/ontologies/pcl) terms.
## Terms not found


This report provides a list of terms not found neither in UBERON nor in CL. Please remove these terms from the ASCT+B table - disconsider this message if a term was recently added to the ontology.  
  
1. UBERON:1200117

1. UBERON:1200089

1. UBERON:1200204

1. UBERON:1200266

1. UBERON:1200103

1. UBERON:1200298

1. UBERON:1200065

1. UBERON:1200262

1. UBERON:1200275

1. UBERON:1200234

1. UBERON:1200075

1. UBERON:1200030

1. UBERON:1200233

1. UBERON:1200160

1. UBERON:1200090

1. UBERON:1200285

1. UBERON:1200057

1. UBERON:1200154

1. UBERON:1200068

1. UBERON:1200223

1. UBERON:1200219

1. UBERON:1200153

1. UBERON:1200267

1. UBERON:1200231

1. UBERON:1200101

1. UBERON:1200095

1. UBERON:1200104

1. UBERON:1200066

1. UBERON:1200115


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
  
1. No term id was found for the name/label _free part of arm bone_ in the following 40 rows _[14](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=14:14)_, _[15](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=15:15)_, _[16](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=16:16)_, _[17](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=17:17)_, _[18](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=18:18)_, _[19](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=19:19)_, _[20](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=20:20)_, _[21](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=21:21)_, _[22](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=22:22)_, _[23](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=23:23)_, _[24](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=24:24)_, _[25](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=25:25)_, _[26](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=26:26)_, _[27](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=27:27)_, _[28](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=28:28)_, _[29](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=29:29)_, _[30](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=30:30)_, _[31](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=31:31)_, _[32](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=32:32)_, _[33](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=33:33)_, _[34](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=34:34)_, _[35](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=35:35)_, _[36](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=36:36)_, _[37](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=37:37)_, _[38](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=38:38)_, _[39](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=39:39)_, _[40](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=40:40)_, _[41](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=41:41)_, _[42](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=42:42)_, _[43](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=43:43)_, _[44](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=44:44)_, _[45](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=45:45)_, _[46](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=46:46)_, _[47](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=47:47)_, _[48](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=48:48)_, _[49](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=49:49)_, _[50](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=50:50)_, _[51](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=51:51)_, _[52](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=52:52)_, _[53](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=53:53)_.

1. No term id was found for the name/label _olecranon fossa of humerus_ in the following 1 row _[28](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=28:28)_.

1. No term id was found for the name/label _olecranon of ulna_ in the following 1 row _[46](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=46:46)_.

1. No term id was found for the name/label _trochlear notch of ulna_ in the following 1 row _[52](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=52:52)_.

1. No term id was found for the name/label _glenoid fossa of scapula_ in the following 1 row _[160](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=160:160)_.

1. No term id was found for the name/label _supraglenoid tubercle of scapula_ in the following 1 row _[172](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=172:172)_.

1. No term id was found for the name/label _free part of leg bone_ in the following 42 rows _[280](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=280:280)_, _[281](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=281:281)_, _[282](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=282:282)_, _[283](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=283:283)_, _[284](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=284:284)_, _[285](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=285:285)_, _[286](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=286:286)_, _[287](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=287:287)_, _[288](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=288:288)_, _[289](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=289:289)_, _[290](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=290:290)_, _[291](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=291:291)_, _[292](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=292:292)_, _[293](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=293:293)_, _[294](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=294:294)_, _[295](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=295:295)_, _[296](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=296:296)_, _[297](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=297:297)_, _[298](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=298:298)_, _[299](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=299:299)_, _[300](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=300:300)_, _[301](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=301:301)_, _[302](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=302:302)_, _[303](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=303:303)_, _[304](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=304:304)_, _[305](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=305:305)_, _[306](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=306:306)_, _[307](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=307:307)_, _[308](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=308:308)_, _[309](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=309:309)_, _[310](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=310:310)_, _[311](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=311:311)_, _[312](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=312:312)_, _[313](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=313:313)_, _[314](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=314:314)_, _[315](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=315:315)_, _[316](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=316:316)_, _[317](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=317:317)_, _[318](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=318:318)_, _[319](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=319:319)_, _[320](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=320:320)_, _[321](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=321:321)_.

1. No term id was found for the name/label _acetabulum of os coxa_ in the following 1 row _[326](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=326:326)_.

1. No term id was found for the name/label _iliac crest of ilium of os coxa_ in the following 1 row _[334](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=334:334)_.

1. No term id was found for the name/label _iliac fossa of ilium of os coxa_ in the following 1 row _[335](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=335:335)_.

1. No term id was found for the name/label _ischial ramus of ischium of os coxa_ in the following 1 row _[341](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=341:341)_.

1. No term id was found for the name/label _obturator foramen of os coxa_ in the following 1 row _[347](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=347:347)_.

1. No term id was found for the name/label _pubic symphysis of pubis of os coxa_ in the following 1 row _[355](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=355:355)_.

1. No term id was found for the name/label _cribiform plate of ethmoid bone_ in the following 1 row _[368](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=368:368)_.

1. No term id was found for the name/label _external occipital protuberance of squamous part of occipital bone_ in the following 1 row _[389](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=389:389)_.

1. No term id was found for the name/label _occipital condyle of basilar part of occipital bone_ in the following 1 row _[396](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=396:396)_.

1. No term id was found for the name/label _temporal fossa of parietal bone_ in the following 1 row _[404](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=404:404)_.

1. No term id was found for the name/label _hypophyseal fossa of sphenoid bone_ in the following 1 row _[414](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=414:414)_.

1. No term id was found for the name/label _lateral pterygoid plate of sphenoid bone_ in the following 1 row _[415](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=415:415)_.

1. No term id was found for the name/label _optic canal of sphenoid bone_ in the following 1 row _[418](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=418:418)_.

1. No term id was found for the name/label _pterygoid canal of sphenoid bone_ in the following 1 row _[420](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=420:420)_.

1. No term id was found for the name/label _sella turcica of sphenoid bone_ in the following 1 row _[424](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=424:424)_.

1. No term id was found for the name/label _groove for sigmoid sinus of mastoid part of temporal bone_ in the following 1 row _[432](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=432:432)_.

1. No term id was found for the name/label _styloid process of petrous part of temporal bone_ in the following 1 row _[443](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=443:443)_.

1. No term id was found for the name/label _incisive foramen of maxilla_ in the following 1 row _[485](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=485:485)_.

1. No term id was found for the name/label _infraorbital canal of maxilla_ in the following 1 row _[486](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=486:486)_.

1. No term id was found for the name/label _intermaxillary suture of maxilla_ in the following 1 row _[489](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=489:489)_.

1. No term id was found for the name/label _costal region bone_ in the following 141 rows _[510](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=510:510)_, _[511](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=511:511)_, _[512](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=512:512)_, _[513](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=513:513)_, _[514](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=514:514)_, _[515](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=515:515)_, _[516](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=516:516)_, _[517](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=517:517)_, _[518](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=518:518)_, _[519](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=519:519)_, _[520](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=520:520)_, _[521](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=521:521)_, _[522](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=522:522)_, _[523](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=523:523)_, _[524](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=524:524)_, _[525](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=525:525)_, _[526](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=526:526)_, _[527](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=527:527)_, _[528](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=528:528)_, _[529](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=529:529)_, _[530](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=530:530)_, _[531](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=531:531)_, _[532](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=532:532)_, _[533](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=533:533)_, _[534](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=534:534)_, _[535](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=535:535)_, _[536](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=536:536)_, _[537](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=537:537)_, _[538](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=538:538)_, _[539](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=539:539)_, _[540](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=540:540)_, _[541](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=541:541)_, _[542](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=542:542)_, _[543](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=543:543)_, _[544](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=544:544)_, _[545](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=545:545)_, _[546](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=546:546)_, _[547](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=547:547)_, _[548](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=548:548)_, _[549](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=549:549)_, _[550](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=550:550)_, _[551](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=551:551)_, _[552](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=552:552)_, _[553](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=553:553)_, _[554](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=554:554)_, _[555](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=555:555)_, _[556](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=556:556)_, _[557](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=557:557)_, _[558](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=558:558)_, _[559](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=559:559)_, _[560](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=560:560)_, _[561](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=561:561)_, _[562](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=562:562)_, _[563](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=563:563)_, _[564](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=564:564)_, _[565](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=565:565)_, _[566](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=566:566)_, _[567](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=567:567)_, _[568](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=568:568)_, _[569](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=569:569)_, _[570](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=570:570)_, _[571](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=571:571)_, _[572](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=572:572)_, _[573](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=573:573)_, _[574](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=574:574)_, _[575](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=575:575)_, _[576](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=576:576)_, _[577](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=577:577)_, _[578](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=578:578)_, _[579](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=579:579)_, _[580](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=580:580)_, _[581](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=581:581)_, _[582](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=582:582)_, _[583](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=583:583)_, _[584](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=584:584)_, _[585](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=585:585)_, _[586](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=586:586)_, _[587](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=587:587)_, _[588](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=588:588)_, _[589](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=589:589)_, _[590](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=590:590)_, _[591](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=591:591)_, _[592](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=592:592)_, _[593](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=593:593)_, _[594](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=594:594)_, _[595](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=595:595)_, _[596](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=596:596)_, _[597](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=597:597)_, _[598](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=598:598)_, _[599](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=599:599)_, _[600](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=600:600)_, _[601](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=601:601)_, _[602](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=602:602)_, _[603](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=603:603)_, _[604](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=604:604)_, _[605](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=605:605)_, _[606](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=606:606)_, _[607](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=607:607)_, _[608](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=608:608)_, _[609](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=609:609)_, _[610](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=610:610)_, _[611](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=611:611)_, _[612](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=612:612)_, _[613](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=613:613)_, _[614](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=614:614)_, _[615](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=615:615)_, _[616](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=616:616)_, _[617](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=617:617)_, _[618](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=618:618)_, _[619](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=619:619)_, _[620](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=620:620)_, _[621](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=621:621)_, _[622](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=622:622)_, _[623](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=623:623)_, _[624](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=624:624)_, _[625](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=625:625)_, _[626](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=626:626)_, _[627](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=627:627)_, _[628](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=628:628)_, _[629](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=629:629)_, _[630](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=630:630)_, _[631](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=631:631)_, _[632](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=632:632)_, _[633](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=633:633)_, _[634](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=634:634)_, _[635](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=635:635)_, _[636](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=636:636)_, _[637](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=637:637)_, _[638](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=638:638)_, _[639](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=639:639)_, _[640](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=640:640)_, _[641](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=641:641)_, _[642](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=642:642)_, _[643](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=643:643)_, _[644](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=644:644)_, _[645](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=645:645)_, _[646](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=646:646)_, _[647](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=647:647)_, _[648](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=648:648)_, _[649](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=649:649)_, _[650](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=650:650)_.

1. No term id was found for the name/label _posterior tubercle of first cervical vertebra_ in the following 1 row _[677](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=677:677)_.

1. No term id was found for the name/label _transverse foramen of first cervical vertebra_ in the following 1 row _[682](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=682:682)_.

1. No term id was found for the name/label _vertebral body of first cervical vertebra_ in the following 1 row _[684](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=684:684)_.

1. No term id was found for the name/label _vertebral foramen of first cervical vertebra_ in the following 1 row _[685](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=685:685)_.

1. No term id was found for the name/label _transverse foramen of second cervical vertebra_ in the following 1 row _[698](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=698:698)_.

1. No term id was found for the name/label _vertebral body of second cervical vertebra_ in the following 1 row _[701](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=701:701)_.

1. No term id was found for the name/label _vertebral foramen of second cervical vertebra_ in the following 1 row _[702](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=702:702)_.

1. No term id was found for the name/label _vertebral body of third cervical vertebra_ in the following 1 row _[716](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=716:716)_.

1. No term id was found for the name/label _vertebral body of fourth cervical vertebra_ in the following 1 row _[731](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=731:731)_.

1. No term id was found for the name/label _vertebral body of fifth cervical vertebra_ in the following 1 row _[746](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=746:746)_.

1. No term id was found for the name/label _vertebral body of sixth cervical vertebra_ in the following 1 row _[761](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=761:761)_.

1. No term id was found for the name/label _vertebral body of seventh cervical vertebra_ in the following 1 row _[777](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=777:777)_.

1. No term id was found for the name/label _vertebral body of first lumbar vertebra_ in the following 1 row _[794](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=794:794)_.

1. No term id was found for the name/label _vertebral body of second lumbar vertebra_ in the following 1 row _[810](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=810:810)_.

1. No term id was found for the name/label _vertebral body of third lumbar vertebra_ in the following 1 row _[826](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=826:826)_.

1. No term id was found for the name/label _vertebral body of fourth lumbar vertebra_ in the following 1 row _[842](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=842:842)_.

1. No term id was found for the name/label _vertebral body of fifth lumbar vertebra_ in the following 1 row _[858](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=858:858)_.

1. No term id was found for the name/label _vertebral body of first thoracic vertebra_ in the following 1 row _[896](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=896:896)_.

1. No term id was found for the name/label _vertebral foramen of first thoracic vertebra_ in the following 1 row _[897](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=897:897)_.

1. No term id was found for the name/label _vertebral body of tenth thoracic vertebra_ in the following 1 row _[913](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=913:913)_.

1. No term id was found for the name/label _vertebral body of eleventh thoracic vertebra_ in the following 1 row _[930](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=930:930)_.

1. No term id was found for the name/label _vertebral body of twelfth thoracic vertebra_ in the following 1 row _[945](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=945:945)_.

1. No term id was found for the name/label _vertebral body of second thoracic vertebra_ in the following 1 row _[962](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=962:962)_.

1. No term id was found for the name/label _vertebral body of third thoracic vertebra_ in the following 1 row _[979](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=979:979)_.

1. No term id was found for the name/label _vertebral body of fourth thoracic vertebra_ in the following 1 row _[996](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=996:996)_.

1. No term id was found for the name/label _vertebral body of fifth thoracic vertebra_ in the following 1 row _[1013](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1013:1013)_.

1. No term id was found for the name/label _vertebral body of sixth thoracic vertebra_ in the following 1 row _[1030](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1030:1030)_.

1. No term id was found for the name/label _vertebral body of seventh thoracic vertebra_ in the following 1 row _[1047](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1047:1047)_.

1. No term id was found for the name/label _vertebral body of eighth thoracic vertebra_ in the following 1 row _[1064](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1064:1064)_.

1. No term id was found for the name/label _vertebral body of ninth thoracic vertebra_ in the following 1 row _[1081](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1081:1081)_.


## Blank ontology ID missing parent


This report provides a list of CT terms with blank ontology ID without an upper term from [Cell Ontology](https://www.ebi.ac.uk/ols4/ontologies/cl). Please, create an upper level in the ASCT+B table and add an upper term for them. Please, make sure the term without ontology ID _doesn't exist_ in the ontology.  
  
- No issues found.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Same case for Anatomic Ontology for Human Lung Maturation (LMHA) and Interlex IDs (ILX) from Stimulating Peripheral Activity to Relieve Conditions (SPARC). You can request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols4/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols4/ontologies/pcl).  
  
1. The term _FMA:23356_ in the following 1 row _[16](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=16:16)_ is from another ontology that is not validated in this process.

1. The term _FMA:23418_ in the following 1 row _[19](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=19:19)_ is from another ontology that is not validated in this process.

1. The term _FMA:23390_ in the following 1 row _[20](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=20:20)_ is from another ontology that is not validated in this process.

1. The term _FMA:13304_ in the following 1 row _[21](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=21:21)_ is from another ontology that is not validated in this process.

1. The term _FMA:23396_ in the following 1 row _[22](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=22:22)_ is from another ontology that is not validated in this process.

1. The term _FMA:23442_ in the following 1 row _[23](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=23:23)_ is from another ontology that is not validated in this process.

1. The term _FMA:23436_ in the following 1 row _[24](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=24:24)_ is from another ontology that is not validated in this process.

1. The term _FMA:23441_ in the following 1 row _[26](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=26:26)_ is from another ontology that is not validated in this process.

1. The term _FMA:23435_ in the following 1 row _[27](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=27:27)_ is from another ontology that is not validated in this process.

1. The term _FMA:13305_ in the following 1 row _[31](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=31:31)_ is from another ontology that is not validated in this process.

1. The term _FMA:23359_ in the following 1 row _[32](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=32:32)_ is from another ontology that is not validated in this process.

1. The term _FMA:39682_ in the following 1 row _[36](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=36:36)_ is from another ontology that is not validated in this process.

1. The term _FMA:23524_ in the following 1 row _[40](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=40:40)_ is from another ontology that is not validated in this process.

1. The term _FMA:23530_ in the following 1 row _[41](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=41:41)_ is from another ontology that is not validated in this process.

1. The term _FMA:39685_ in the following 1 row _[45](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=45:45)_ is from another ontology that is not validated in this process.

1. The term _FMA:23618_ in the following 1 row _[47](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=47:47)_ is from another ontology that is not validated in this process.

1. The term _FMA:23626_ in the following 1 row _[50](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=50:50)_ is from another ontology that is not validated in this process.

1. The term _FMA:39978_ in the following 1 row _[59](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=59:59)_ is from another ontology that is not validated in this process.

1. The term _FMA:37609_ in the following 1 row _[62](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=62:62)_ is from another ontology that is not validated in this process.

1. The term _FMA:37505_ in the following 1 row _[66](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=66:66)_ is from another ontology that is not validated in this process.

1. The term _FMA:37563_ in the following 1 row _[68](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=68:68)_ is from another ontology that is not validated in this process.

1. The term _FMA:37517_ in the following 1 row _[71](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=71:71)_ is from another ontology that is not validated in this process.

1. The term _FMA:37633_ in the following 1 row _[72](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=72:72)_ is from another ontology that is not validated in this process.

1. The term _FMA:37575_ in the following 1 row _[73](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=73:73)_ is from another ontology that is not validated in this process.

1. The term _FMA:37529_ in the following 1 row _[76](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=76:76)_ is from another ontology that is not validated in this process.

1. The term _FMA:37645_ in the following 1 row _[77](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=77:77)_ is from another ontology that is not validated in this process.

1. The term _FMA:37587_ in the following 1 row _[78](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=78:78)_ is from another ontology that is not validated in this process.

1. The term _FMA:37541_ in the following 1 row _[81](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=81:81)_ is from another ontology that is not validated in this process.

1. The term _FMA:37657_ in the following 1 row _[82](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=82:82)_ is from another ontology that is not validated in this process.

1. The term _FMA:37599_ in the following 1 row _[83](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=83:83)_ is from another ontology that is not validated in this process.

1. The term _FMA:42788_ in the following 1 row _[87](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=87:87)_ is from another ontology that is not validated in this process.

1. The term _FMA:42803_ in the following 1 row _[88](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=88:88)_ is from another ontology that is not validated in this process.

1. The term _FMA:42869_ in the following 1 row _[89](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=89:89)_ is from another ontology that is not validated in this process.

1. The term _FMA:42791_ in the following 1 row _[91](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=91:91)_ is from another ontology that is not validated in this process.

1. The term _FMA:42806_ in the following 1 row _[92](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=92:92)_ is from another ontology that is not validated in this process.

1. The term _FMA:42872_ in the following 1 row _[93](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=93:93)_ is from another ontology that is not validated in this process.

1. The term _FMA:42794_ in the following 1 row _[95](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=95:95)_ is from another ontology that is not validated in this process.

1. The term _FMA:42809_ in the following 1 row _[96](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=96:96)_ is from another ontology that is not validated in this process.

1. The term _FMA:42875_ in the following 1 row _[97](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=97:97)_ is from another ontology that is not validated in this process.

1. The term _FMA:42797_ in the following 1 row _[99](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=99:99)_ is from another ontology that is not validated in this process.

1. The term _FMA:42812_ in the following 1 row _[100](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=100:100)_ is from another ontology that is not validated in this process.

1. The term _FMA:42878_ in the following 1 row _[101](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=101:101)_ is from another ontology that is not validated in this process.

1. The term _FMA:42800_ in the following 1 row _[103](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=103:103)_ is from another ontology that is not validated in this process.

1. The term _FMA:42815_ in the following 1 row _[104](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=104:104)_ is from another ontology that is not validated in this process.

1. The term _FMA:42881_ in the following 1 row _[105](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=105:105)_ is from another ontology that is not validated in this process.

1. The term _FMA:37502_ in the following 1 row _[107](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=107:107)_ is from another ontology that is not validated in this process.

1. The term _FMA:37560_ in the following 1 row _[109](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=109:109)_ is from another ontology that is not validated in this process.

1. The term _FMA:37514_ in the following 1 row _[111](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=111:111)_ is from another ontology that is not validated in this process.

1. The term _FMA:37572_ in the following 1 row _[113](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=113:113)_ is from another ontology that is not validated in this process.

1. The term _FMA:37526_ in the following 1 row _[115](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=115:115)_ is from another ontology that is not validated in this process.

1. The term _FMA:37642_ in the following 1 row _[116](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=116:116)_ is from another ontology that is not validated in this process.

1. The term _FMA:37584_ in the following 1 row _[117](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=117:117)_ is from another ontology that is not validated in this process.

1. The term _FMA:37538_ in the following 1 row _[119](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=119:119)_ is from another ontology that is not validated in this process.

1. The term _FMA:37654_ in the following 1 row _[120](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=120:120)_ is from another ontology that is not validated in this process.

1. The term _FMA:37596_ in the following 1 row _[121](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=121:121)_ is from another ontology that is not validated in this process.

1. The term _FMA:37606_ in the following 1 row _[125](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=125:125)_ is from another ontology that is not validated in this process.

1. The term _FMA:37499_ in the following 1 row _[128](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=128:128)_ is from another ontology that is not validated in this process.

1. The term _FMA:37615_ in the following 1 row _[129](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=129:129)_ is from another ontology that is not validated in this process.

1. The term _FMA:37557_ in the following 1 row _[130](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=130:130)_ is from another ontology that is not validated in this process.

1. The term _FMA:37511_ in the following 1 row _[132](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=132:132)_ is from another ontology that is not validated in this process.

1. The term _FMA:37627_ in the following 1 row _[133](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=133:133)_ is from another ontology that is not validated in this process.

1. The term _FMA:37569_ in the following 1 row _[134](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=134:134)_ is from another ontology that is not validated in this process.

1. The term _FMA:37523_ in the following 1 row _[136](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=136:136)_ is from another ontology that is not validated in this process.

1. The term _FMA:37639_ in the following 1 row _[137](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=137:137)_ is from another ontology that is not validated in this process.

1. The term _FMA:37581_ in the following 1 row _[138](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=138:138)_ is from another ontology that is not validated in this process.

1. The term _FMA:37535_ in the following 1 row _[140](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=140:140)_ is from another ontology that is not validated in this process.

1. The term _FMA:37651_ in the following 1 row _[141](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=141:141)_ is from another ontology that is not validated in this process.

1. The term _FMA:37593_ in the following 1 row _[142](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=142:142)_ is from another ontology that is not validated in this process.

1. The term _FMA:23300_ in the following 1 row _[148](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=148:148)_ is from another ontology that is not validated in this process.

1. The term _FMA:23340_ in the following 1 row _[149](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=149:149)_ is from another ontology that is not validated in this process.

1. The term _FMA:23322_ in the following 1 row _[150](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=150:150)_ is from another ontology that is not validated in this process.

1. The term _FMA:23294_ in the following 1 row _[151](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=151:151)_ is from another ontology that is not validated in this process.

1. The term _FMA:23334_ in the following 1 row _[153](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=153:153)_ is from another ontology that is not validated in this process.

1. The term _FMA:23343_ in the following 1 row _[154](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=154:154)_ is from another ontology that is not validated in this process.

1. The term _FMA:23325_ in the following 1 row _[155](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=155:155)_ is from another ontology that is not validated in this process.

1. The term _FMA:23303_ in the following 1 row _[158](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=158:158)_ is from another ontology that is not validated in this process.

1. The term _FMA:296241_ in the following 1 row _[171](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=171:171)_ is from another ontology that is not validated in this process.

1. The term _FMA:75330_ in the following 1 row _[177](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=177:177)_ is from another ontology that is not validated in this process.

1. The term _FMA:75331_ in the following 1 row _[186](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=186:186)_ is from another ontology that is not validated in this process.

1. The term _FMA:75332_ in the following 1 row _[187](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=187:187)_ is from another ontology that is not validated in this process.

1. The term _FMA:76642_ in the following 1 row _[191](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=191:191)_ is from another ontology that is not validated in this process.

1. The term _FMA:33036_ in the following 1 row _[194](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=194:194)_ is from another ontology that is not validated in this process.

1. The term _FMA:32994_ in the following 1 row _[195](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=195:195)_ is from another ontology that is not validated in this process.

1. The term _FMA:32961_ in the following 1 row _[197](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=197:197)_ is from another ontology that is not validated in this process.

1. The term _FMA:33003_ in the following 1 row _[199](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=199:199)_ is from another ontology that is not validated in this process.

1. The term _FMA:32970_ in the following 1 row _[201](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=201:201)_ is from another ontology that is not validated in this process.

1. The term _FMA:33054_ in the following 1 row _[202](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=202:202)_ is from another ontology that is not validated in this process.

1. The term _FMA:33012_ in the following 1 row _[203](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=203:203)_ is from another ontology that is not validated in this process.

1. The term _FMA:32979_ in the following 1 row _[205](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=205:205)_ is from another ontology that is not validated in this process.

1. The term _FMA:33091_ in the following 1 row _[206](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=206:206)_ is from another ontology that is not validated in this process.

1. The term _FMA:33021_ in the following 1 row _[207](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=207:207)_ is from another ontology that is not validated in this process.

1. The term _FMA:32988_ in the following 1 row _[209](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=209:209)_ is from another ontology that is not validated in this process.

1. The term _FMA:33106_ in the following 1 row _[210](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=210:210)_ is from another ontology that is not validated in this process.

1. The term _FMA:33030_ in the following 1 row _[211](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=211:211)_ is from another ontology that is not validated in this process.

1. The term _FMA:42963_ in the following 1 row _[216](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=216:216)_ is from another ontology that is not validated in this process.

1. The term _FMA:42983_ in the following 1 row _[217](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=217:217)_ is from another ontology that is not validated in this process.

1. The term _FMA:43007_ in the following 1 row _[218](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=218:218)_ is from another ontology that is not validated in this process.

1. The term _FMA:42964_ in the following 1 row _[220](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=220:220)_ is from another ontology that is not validated in this process.

1. The term _FMA:42986_ in the following 1 row _[221](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=221:221)_ is from another ontology that is not validated in this process.

1. The term _FMA:43008_ in the following 1 row _[222](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=222:222)_ is from another ontology that is not validated in this process.

1. The term _FMA:42965_ in the following 1 row _[224](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=224:224)_ is from another ontology that is not validated in this process.

1. The term _FMA:42998_ in the following 1 row _[225](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=225:225)_ is from another ontology that is not validated in this process.

1. The term _FMA:43009_ in the following 1 row _[226](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=226:226)_ is from another ontology that is not validated in this process.

1. The term _FMA:42966_ in the following 1 row _[228](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=228:228)_ is from another ontology that is not validated in this process.

1. The term _FMA:42999_ in the following 1 row _[229](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=229:229)_ is from another ontology that is not validated in this process.

1. The term _FMA:43010_ in the following 1 row _[230](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=230:230)_ is from another ontology that is not validated in this process.

1. The term _FMA:42967_ in the following 1 row _[232](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=232:232)_ is from another ontology that is not validated in this process.

1. The term _FMA:43000_ in the following 1 row _[233](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=233:233)_ is from another ontology that is not validated in this process.

1. The term _FMA:43011_ in the following 1 row _[234](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=234:234)_ is from another ontology that is not validated in this process.

1. The term _FMA:76644_ in the following 1 row _[235](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=235:235)_ is from another ontology that is not validated in this process.

1. The term _FMA:32958_ in the following 1 row _[237](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=237:237)_ is from another ontology that is not validated in this process.

1. The term _FMA:33000_ in the following 1 row _[239](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=239:239)_ is from another ontology that is not validated in this process.

1. The term _FMA:32967_ in the following 1 row _[241](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=241:241)_ is from another ontology that is not validated in this process.

1. The term _FMA:33051_ in the following 1 row _[242](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=242:242)_ is from another ontology that is not validated in this process.

1. The term _FMA:33009_ in the following 1 row _[243](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=243:243)_ is from another ontology that is not validated in this process.

1. The term _FMA:32976_ in the following 1 row _[245](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=245:245)_ is from another ontology that is not validated in this process.

1. The term _FMA:33088_ in the following 1 row _[246](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=246:246)_ is from another ontology that is not validated in this process.

1. The term _FMA:33018_ in the following 1 row _[247](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=247:247)_ is from another ontology that is not validated in this process.

1. The term _FMA:32985_ in the following 1 row _[249](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=249:249)_ is from another ontology that is not validated in this process.

1. The term _FMA:33103_ in the following 1 row _[250](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=250:250)_ is from another ontology that is not validated in this process.

1. The term _FMA:33027_ in the following 1 row _[251](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=251:251)_ is from another ontology that is not validated in this process.

1. The term _FMA:34782_ in the following 1 row _[253](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=253:253)_ is from another ontology that is not validated in this process.

1. The term _FMA:33033_ in the following 1 row _[256](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=256:256)_ is from another ontology that is not validated in this process.

1. The term _FMA:32991_ in the following 1 row _[257](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=257:257)_ is from another ontology that is not validated in this process.

1. The term _FMA:32955_ in the following 1 row _[259](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=259:259)_ is from another ontology that is not validated in this process.

1. The term _FMA:33039_ in the following 1 row _[260](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=260:260)_ is from another ontology that is not validated in this process.

1. The term _FMA:32997_ in the following 1 row _[261](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=261:261)_ is from another ontology that is not validated in this process.

1. The term _FMA:32964_ in the following 1 row _[263](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=263:263)_ is from another ontology that is not validated in this process.

1. The term _FMA:33048_ in the following 1 row _[264](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=264:264)_ is from another ontology that is not validated in this process.

1. The term _FMA:33006_ in the following 1 row _[265](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=265:265)_ is from another ontology that is not validated in this process.

1. The term _FMA:32973_ in the following 1 row _[267](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=267:267)_ is from another ontology that is not validated in this process.

1. The term _FMA:33085_ in the following 1 row _[268](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=268:268)_ is from another ontology that is not validated in this process.

1. The term _FMA:33015_ in the following 1 row _[269](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=269:269)_ is from another ontology that is not validated in this process.

1. The term _FMA:32982_ in the following 1 row _[271](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=271:271)_ is from another ontology that is not validated in this process.

1. The term _FMA:33100_ in the following 1 row _[272](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=272:272)_ is from another ontology that is not validated in this process.

1. The term _FMA:33024_ in the following 1 row _[273](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=273:273)_ is from another ontology that is not validated in this process.

1. The term _FMA:33635_ in the following 1 row _[275](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=275:275)_ is from another ontology that is not validated in this process.

1. The term _FMA:33651_ in the following 1 row _[276](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=276:276)_ is from another ontology that is not validated in this process.

1. The term _FMA:33650_ in the following 1 row _[278](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=278:278)_ is from another ontology that is not validated in this process.

1. The term _FMA:33638_ in the following 1 row _[279](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=279:279)_ is from another ontology that is not validated in this process.

1. The term _FMA:32870_ in the following 1 row _[282](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=282:282)_ is from another ontology that is not validated in this process.

1. The term _FMA:32852_ in the following 1 row _[284](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=284:284)_ is from another ontology that is not validated in this process.

1. The term _FMA:43748_ in the following 1 row _[286](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=286:286)_ is from another ontology that is not validated in this process.

1. The term _FMA:43706_ in the following 1 row _[288](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=288:288)_ is from another ontology that is not validated in this process.

1. The term _FMA:43718_ in the following 1 row _[291](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=291:291)_ is from another ontology that is not validated in this process.

1. The term _FMA:32853_ in the following 1 row _[292](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=292:292)_ is from another ontology that is not validated in this process.

1. The term _FMA:43715_ in the following 1 row _[293](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=293:293)_ is from another ontology that is not validated in this process.

1. The term _FMA:43719_ in the following 1 row _[296](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=296:296)_ is from another ontology that is not validated in this process.

1. The term _FMA:75328_ in the following 1 row _[299](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=299:299)_ is from another ontology that is not validated in this process.

1. The term _FMA:43709_ in the following 1 row _[300](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=300:300)_ is from another ontology that is not validated in this process.

1. The term _FMA:32847_ in the following 1 row _[301](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=301:301)_ is from another ontology that is not validated in this process.

1. The term _FMA:43703_ in the following 1 row _[302](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=302:302)_ is from another ontology that is not validated in this process.

1. The term _FMA:33729_ in the following 1 row _[304](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=304:304)_ is from another ontology that is not validated in this process.

1. The term _FMA:33738_ in the following 1 row _[307](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=307:307)_ is from another ontology that is not validated in this process.

1. The term _FMA:43761_ in the following 1 row _[313](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=313:313)_ is from another ontology that is not validated in this process.

1. The term _FMA:33125_ in the following 1 row _[318](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=318:318)_ is from another ontology that is not validated in this process.

1. The term _FMA:59495_ in the following 1 row _[362](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=362:362)_ is from another ontology that is not validated in this process.

1. The term _FMA:57131_ in the following 1 row _[383](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=383:383)_ is from another ontology that is not validated in this process.

1. The term _FMA:53097_ in the following 1 row _[385](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=385:385)_ is from another ontology that is not validated in this process.

1. The term _FMA:53132_ in the following 1 row _[402](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=402:402)_ is from another ontology that is not validated in this process.

1. The term _FMA:53130_ in the following 1 row _[403](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=403:403)_ is from another ontology that is not validated in this process.

1. The term _FMA:54682_ in the following 1 row _[423](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=423:423)_ is from another ontology that is not validated in this process.

1. The term _FMA:52833_ in the following 1 row _[460](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=460:460)_ is from another ontology that is not validated in this process.

1. The term _FMA:59470_ in the following 1 row _[463](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=463:463)_ is from another ontology that is not validated in this process.

1. The term _FMA:52828_ in the following 1 row _[475](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=475:475)_ is from another ontology that is not validated in this process.

1. The term _FMA:75360_ in the following 1 row _[480](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=480:480)_ is from another ontology that is not validated in this process.

1. The term _FMA:57703_ in the following 1 row _[491](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=491:491)_ is from another ontology that is not validated in this process.

1. The term _FMA:52901_ in the following 1 row _[498](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=498:498)_ is from another ontology that is not validated in this process.

1. The term _FMA:52899_ in the following 1 row _[500](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=500:500)_ is from another ontology that is not validated in this process.

1. The term _FMA:57674_ in the following 1 row _[502](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=502:502)_ is from another ontology that is not validated in this process.

1. The term _FMA:289670_ in the following 1 row _[506](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=506:506)_ is from another ontology that is not validated in this process.

1. The term _FMA:7608_ in the following 1 row _[512](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=512:512)_ is from another ontology that is not validated in this process.

1. The term _FMA:7606_ in the following 1 row _[513](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=513:513)_ is from another ontology that is not validated in this process.

1. The term _FMA:7602_ in the following 1 row _[514](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=514:514)_ is from another ontology that is not validated in this process.

1. The term _FMA:7600_ in the following 1 row _[519](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=519:519)_ is from another ontology that is not validated in this process.

1. The term _FMA:7601_ in the following 1 row _[520](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=520:520)_ is from another ontology that is not validated in this process.

1. The term _FMA:7605_ in the following 1 row _[524](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=524:524)_ is from another ontology that is not validated in this process.

1. The term _FMA:8430_ in the following 1 row _[526](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=526:526)_ is from another ontology that is not validated in this process.

1. The term _FMA:8428_ in the following 1 row _[527](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=527:527)_ is from another ontology that is not validated in this process.

1. The term _FMA:8426_ in the following 1 row _[528](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=528:528)_ is from another ontology that is not validated in this process.

1. The term _FMA:8433_ in the following 1 row _[529](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=529:529)_ is from another ontology that is not validated in this process.

1. The term _FMA:8419_ in the following 1 row _[531](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=531:531)_ is from another ontology that is not validated in this process.

1. The term _FMA:8424_ in the following 1 row _[532](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=532:532)_ is from another ontology that is not validated in this process.

1. The term _FMA:8427_ in the following 1 row _[535](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=535:535)_ is from another ontology that is not validated in this process.

1. The term _FMA:8501_ in the following 1 row _[537](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=537:537)_ is from another ontology that is not validated in this process.

1. The term _FMA:8506_ in the following 1 row _[538](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=538:538)_ is from another ontology that is not validated in this process.

1. The term _FMA:8500_ in the following 1 row _[540](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=540:540)_ is from another ontology that is not validated in this process.

1. The term _FMA:8517_ in the following 1 row _[543](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=543:543)_ is from another ontology that is not validated in this process.

1. The term _FMA:8516_ in the following 1 row _[546](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=546:546)_ is from another ontology that is not validated in this process.

1. The term _FMA:7630_ in the following 1 row _[549](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=549:549)_ is from another ontology that is not validated in this process.

1. The term _FMA:7627_ in the following 1 row _[550](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=550:550)_ is from another ontology that is not validated in this process.

1. The term _FMA:7623_ in the following 1 row _[551](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=551:551)_ is from another ontology that is not validated in this process.

1. The term _FMA:7636_ in the following 1 row _[552](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=552:552)_ is from another ontology that is not validated in this process.

1. The term _FMA:7621_ in the following 1 row _[553](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=553:553)_ is from another ontology that is not validated in this process.

1. The term _FMA:7628_ in the following 1 row _[554](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=554:554)_ is from another ontology that is not validated in this process.

1. The term _FMA:7622_ in the following 1 row _[555](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=555:555)_ is from another ontology that is not validated in this process.

1. The term _FMA:7624_ in the following 1 row _[558](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=558:558)_ is from another ontology that is not validated in this process.

1. The term _FMA:7626_ in the following 1 row _[559](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=559:559)_ is from another ontology that is not validated in this process.

1. The term _FMA:7711_ in the following 1 row _[561](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=561:561)_ is from another ontology that is not validated in this process.

1. The term _FMA:7709_ in the following 1 row _[562](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=562:562)_ is from another ontology that is not validated in this process.

1. The term _FMA:7700_ in the following 1 row _[563](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=563:563)_ is from another ontology that is not validated in this process.

1. The term _FMA:7714_ in the following 1 row _[564](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=564:564)_ is from another ontology that is not validated in this process.

1. The term _FMA:7640_ in the following 1 row _[565](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=565:565)_ is from another ontology that is not validated in this process.

1. The term _FMA:7639_ in the following 1 row _[566](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=566:566)_ is from another ontology that is not validated in this process.

1. The term _FMA:7706_ in the following 1 row _[567](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=567:567)_ is from another ontology that is not validated in this process.

1. The term _FMA:7699_ in the following 1 row _[568](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=568:568)_ is from another ontology that is not validated in this process.

1. The term _FMA:7705_ in the following 1 row _[571](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=571:571)_ is from another ontology that is not validated in this process.

1. The term _FMA:7708_ in the following 1 row _[572](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=572:572)_ is from another ontology that is not validated in this process.

1. The term _FMA:7761_ in the following 1 row _[574](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=574:574)_ is from another ontology that is not validated in this process.

1. The term _FMA:7759_ in the following 1 row _[575](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=575:575)_ is from another ontology that is not validated in this process.

1. The term _FMA:7757_ in the following 1 row _[576](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=576:576)_ is from another ontology that is not validated in this process.

1. The term _FMA:7764_ in the following 1 row _[577](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=577:577)_ is from another ontology that is not validated in this process.

1. The term _FMA:7751_ in the following 1 row _[578](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=578:578)_ is from another ontology that is not validated in this process.

1. The term _FMA:7750_ in the following 1 row _[579](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=579:579)_ is from another ontology that is not validated in this process.

1. The term _FMA:7754_ in the following 1 row _[580](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=580:580)_ is from another ontology that is not validated in this process.

1. The term _FMA:7755_ in the following 1 row _[581](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=581:581)_ is from another ontology that is not validated in this process.

1. The term _FMA:7753_ in the following 1 row _[584](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=584:584)_ is from another ontology that is not validated in this process.

1. The term _FMA:7758_ in the following 1 row _[585](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=585:585)_ is from another ontology that is not validated in this process.

1. The term _FMA:7788_ in the following 1 row _[587](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=587:587)_ is from another ontology that is not validated in this process.

1. The term _FMA:7786_ in the following 1 row _[588](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=588:588)_ is from another ontology that is not validated in this process.

1. The term _FMA:7784_ in the following 1 row _[589](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=589:589)_ is from another ontology that is not validated in this process.

1. The term _FMA:7791_ in the following 1 row _[590](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=590:590)_ is from another ontology that is not validated in this process.

1. The term _FMA:7778_ in the following 1 row _[591](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=591:591)_ is from another ontology that is not validated in this process.

1. The term _FMA:7777_ in the following 1 row _[592](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=592:592)_ is from another ontology that is not validated in this process.

1. The term _FMA:7781_ in the following 1 row _[593](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=593:593)_ is from another ontology that is not validated in this process.

1. The term _FMA:7782_ in the following 1 row _[594](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=594:594)_ is from another ontology that is not validated in this process.

1. The term _FMA:7780_ in the following 1 row _[597](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=597:597)_ is from another ontology that is not validated in this process.

1. The term _FMA:7785_ in the following 1 row _[598](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=598:598)_ is from another ontology that is not validated in this process.

1. The term _FMA:7815_ in the following 1 row _[600](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=600:600)_ is from another ontology that is not validated in this process.

1. The term _FMA:7813_ in the following 1 row _[601](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=601:601)_ is from another ontology that is not validated in this process.

1. The term _FMA:7811_ in the following 1 row _[602](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=602:602)_ is from another ontology that is not validated in this process.

1. The term _FMA:7818_ in the following 1 row _[603](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=603:603)_ is from another ontology that is not validated in this process.

1. The term _FMA:7805_ in the following 1 row _[604](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=604:604)_ is from another ontology that is not validated in this process.

1. The term _FMA:7804_ in the following 1 row _[605](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=605:605)_ is from another ontology that is not validated in this process.

1. The term _FMA:7808_ in the following 1 row _[606](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=606:606)_ is from another ontology that is not validated in this process.

1. The term _FMA:7809_ in the following 1 row _[607](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=607:607)_ is from another ontology that is not validated in this process.

1. The term _FMA:7807_ in the following 1 row _[610](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=610:610)_ is from another ontology that is not validated in this process.

1. The term _FMA:7812_ in the following 1 row _[611](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=611:611)_ is from another ontology that is not validated in this process.

1. The term _FMA:7842_ in the following 1 row _[613](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=613:613)_ is from another ontology that is not validated in this process.

1. The term _FMA:7840_ in the following 1 row _[614](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=614:614)_ is from another ontology that is not validated in this process.

1. The term _FMA:7838_ in the following 1 row _[615](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=615:615)_ is from another ontology that is not validated in this process.

1. The term _FMA:7845_ in the following 1 row _[616](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=616:616)_ is from another ontology that is not validated in this process.

1. The term _FMA:7832_ in the following 1 row _[617](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=617:617)_ is from another ontology that is not validated in this process.

1. The term _FMA:7831_ in the following 1 row _[618](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=618:618)_ is from another ontology that is not validated in this process.

1. The term _FMA:7835_ in the following 1 row _[619](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=619:619)_ is from another ontology that is not validated in this process.

1. The term _FMA:7836_ in the following 1 row _[620](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=620:620)_ is from another ontology that is not validated in this process.

1. The term _FMA:7834_ in the following 1 row _[623](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=623:623)_ is from another ontology that is not validated in this process.

1. The term _FMA:7839_ in the following 1 row _[624](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=624:624)_ is from another ontology that is not validated in this process.

1. The term _FMA:8132_ in the following 1 row _[626](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=626:626)_ is from another ontology that is not validated in this process.

1. The term _FMA:8130_ in the following 1 row _[627](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=627:627)_ is from another ontology that is not validated in this process.

1. The term _FMA:8128_ in the following 1 row _[628](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=628:628)_ is from another ontology that is not validated in this process.

1. The term _FMA:8135_ in the following 1 row _[629](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=629:629)_ is from another ontology that is not validated in this process.

1. The term _FMA:8122_ in the following 1 row _[630](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=630:630)_ is from another ontology that is not validated in this process.

1. The term _FMA:8121_ in the following 1 row _[631](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=631:631)_ is from another ontology that is not validated in this process.

1. The term _FMA:8125_ in the following 1 row _[632](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=632:632)_ is from another ontology that is not validated in this process.

1. The term _FMA:8126_ in the following 1 row _[633](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=633:633)_ is from another ontology that is not validated in this process.

1. The term _FMA:8124_ in the following 1 row _[636](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=636:636)_ is from another ontology that is not validated in this process.

1. The term _FMA:8129_ in the following 1 row _[637](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=637:637)_ is from another ontology that is not validated in this process.

1. The term _FMA:8349_ in the following 1 row _[639](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=639:639)_ is from another ontology that is not validated in this process.

1. The term _FMA:8347_ in the following 1 row _[640](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=640:640)_ is from another ontology that is not validated in this process.

1. The term _FMA:8345_ in the following 1 row _[641](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=641:641)_ is from another ontology that is not validated in this process.

1. The term _FMA:8352_ in the following 1 row _[642](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=642:642)_ is from another ontology that is not validated in this process.

1. The term _FMA:8339_ in the following 1 row _[643](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=643:643)_ is from another ontology that is not validated in this process.

1. The term _FMA:8338_ in the following 1 row _[644](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=644:644)_ is from another ontology that is not validated in this process.

1. The term _FMA:8342_ in the following 1 row _[645](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=645:645)_ is from another ontology that is not validated in this process.

1. The term _FMA:8343_ in the following 1 row _[646](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=646:646)_ is from another ontology that is not validated in this process.

1. The term _FMA:8341_ in the following 1 row _[649](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=649:649)_ is from another ontology that is not validated in this process.

1. The term _FMA:8346_ in the following 1 row _[650](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=650:650)_ is from another ontology that is not validated in this process.

1. The term _FMA:7541_ in the following 1 row _[653](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=653:653)_ is from another ontology that is not validated in this process.

1. The term _FMA:7542_ in the following 1 row _[655](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=655:655)_ is from another ontology that is not validated in this process.

1. The term _FMA:7488_ in the following 1 row _[660](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=660:660)_ is from another ontology that is not validated in this process.

1. The term _FMA:26527_ in the following 1 row _[690](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=690:690)_ is from another ontology that is not validated in this process.

1. The term _FMA:24283_ in the following 1 row _[705](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=705:705)_ is from another ontology that is not validated in this process.

1. The term _FMA:24768_ in the following 1 row _[706](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=706:706)_ is from another ontology that is not validated in this process.

1. The term _FMA:24242_ in the following 1 row _[707](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=707:707)_ is from another ontology that is not validated in this process.

1. The term _FMA:24239_ in the following 1 row _[708](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=708:708)_ is from another ontology that is not validated in this process.

1. The term _FMA:24245_ in the following 1 row _[709](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=709:709)_ is from another ontology that is not validated in this process.

1. The term _FMA:24280_ in the following 1 row _[711](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=711:711)_ is from another ontology that is not validated in this process.

1. The term _FMA:24766_ in the following 1 row _[712](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=712:712)_ is from another ontology that is not validated in this process.

1. The term _FMA:24300_ in the following 1 row _[713](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=713:713)_ is from another ontology that is not validated in this process.

1. The term _FMA:24246_ in the following 1 row _[714](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=714:714)_ is from another ontology that is not validated in this process.

1. The term _FMA:24295_ in the following 1 row _[717](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=717:717)_ is from another ontology that is not validated in this process.

1. The term _FMA:26348_ in the following 1 row _[720](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=720:720)_ is from another ontology that is not validated in this process.

1. The term _FMA:26528_ in the following 1 row _[721](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=721:721)_ is from another ontology that is not validated in this process.

1. The term _FMA:26316_ in the following 1 row _[722](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=722:722)_ is from another ontology that is not validated in this process.

1. The term _FMA:26310_ in the following 1 row _[723](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=723:723)_ is from another ontology that is not validated in this process.

1. The term _FMA:26354_ in the following 1 row _[724](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=724:724)_ is from another ontology that is not validated in this process.

1. The term _FMA:26342_ in the following 1 row _[726](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=726:726)_ is from another ontology that is not validated in this process.

1. The term _FMA:26515_ in the following 1 row _[727](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=727:727)_ is from another ontology that is not validated in this process.

1. The term _FMA:24303_ in the following 1 row _[728](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=728:728)_ is from another ontology that is not validated in this process.

1. The term _FMA:26322_ in the following 1 row _[729](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=729:729)_ is from another ontology that is not validated in this process.

1. The term _FMA:24296_ in the following 1 row _[732](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=732:732)_ is from another ontology that is not validated in this process.

1. The term _FMA:26401_ in the following 1 row _[735](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=735:735)_ is from another ontology that is not validated in this process.

1. The term _FMA:26529_ in the following 1 row _[736](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=736:736)_ is from another ontology that is not validated in this process.

1. The term _FMA:26366_ in the following 1 row _[737](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=737:737)_ is from another ontology that is not validated in this process.

1. The term _FMA:26360_ in the following 1 row _[738](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=738:738)_ is from another ontology that is not validated in this process.

1. The term _FMA:26407_ in the following 1 row _[739](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=739:739)_ is from another ontology that is not validated in this process.

1. The term _FMA:26394_ in the following 1 row _[741](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=741:741)_ is from another ontology that is not validated in this process.

1. The term _FMA:26518_ in the following 1 row _[742](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=742:742)_ is from another ontology that is not validated in this process.

1. The term _FMA:24306_ in the following 1 row _[743](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=743:743)_ is from another ontology that is not validated in this process.

1. The term _FMA:26372_ in the following 1 row _[744](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=744:744)_ is from another ontology that is not validated in this process.

1. The term _FMA:24297_ in the following 1 row _[747](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=747:747)_ is from another ontology that is not validated in this process.

1. The term _FMA:26451_ in the following 1 row _[750](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=750:750)_ is from another ontology that is not validated in this process.

1. The term _FMA:26530_ in the following 1 row _[751](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=751:751)_ is from another ontology that is not validated in this process.

1. The term _FMA:26419_ in the following 1 row _[752](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=752:752)_ is from another ontology that is not validated in this process.

1. The term _FMA:26413_ in the following 1 row _[753](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=753:753)_ is from another ontology that is not validated in this process.

1. The term _FMA:26457_ in the following 1 row _[754](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=754:754)_ is from another ontology that is not validated in this process.

1. The term _FMA:26445_ in the following 1 row _[756](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=756:756)_ is from another ontology that is not validated in this process.

1. The term _FMA:26519_ in the following 1 row _[757](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=757:757)_ is from another ontology that is not validated in this process.

1. The term _FMA:24309_ in the following 1 row _[758](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=758:758)_ is from another ontology that is not validated in this process.

1. The term _FMA:26425_ in the following 1 row _[759](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=759:759)_ is from another ontology that is not validated in this process.

1. The term _FMA:24298_ in the following 1 row _[762](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=762:762)_ is from another ontology that is not validated in this process.

1. The term _FMA:26501_ in the following 1 row _[765](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=765:765)_ is from another ontology that is not validated in this process.

1. The term _FMA:26531_ in the following 1 row _[766](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=766:766)_ is from another ontology that is not validated in this process.

1. The term _FMA:26469_ in the following 1 row _[767](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=767:767)_ is from another ontology that is not validated in this process.

1. The term _FMA:26463_ in the following 1 row _[768](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=768:768)_ is from another ontology that is not validated in this process.

1. The term _FMA:26507_ in the following 1 row _[769](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=769:769)_ is from another ontology that is not validated in this process.

1. The term _FMA:26495_ in the following 1 row _[771](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=771:771)_ is from another ontology that is not validated in this process.

1. The term _FMA:26520_ in the following 1 row _[772](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=772:772)_ is from another ontology that is not validated in this process.

1. The term _FMA:24312_ in the following 1 row _[773](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=773:773)_ is from another ontology that is not validated in this process.

1. The term _FMA:26475_ in the following 1 row _[774](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=774:774)_ is from another ontology that is not validated in this process.

1. The term _FMA:24299_ in the following 1 row _[778](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=778:778)_ is from another ontology that is not validated in this process.

1. The term _FMA:16309_ in the following 1 row _[781](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=781:781)_ is from another ontology that is not validated in this process.

1. The term _FMA:16349_ in the following 1 row _[782](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=782:782)_ is from another ontology that is not validated in this process.

1. The term _FMA:16137_ in the following 1 row _[783](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=783:783)_ is from another ontology that is not validated in this process.

1. The term _FMA:16289_ in the following 1 row _[784](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=784:784)_ is from another ontology that is not validated in this process.

1. The term _FMA:16164_ in the following 1 row _[785](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=785:785)_ is from another ontology that is not validated in this process.

1. The term _FMA:16094_ in the following 1 row _[787](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=787:787)_ is from another ontology that is not validated in this process.

1. The term _FMA:16196_ in the following 1 row _[788](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=788:788)_ is from another ontology that is not validated in this process.

1. The term _FMA:16128_ in the following 1 row _[790](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=790:790)_ is from another ontology that is not validated in this process.

1. The term _FMA:16272_ in the following 1 row _[791](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=791:791)_ is from another ontology that is not validated in this process.

1. The term _FMA:16179_ in the following 1 row _[792](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=792:792)_ is from another ontology that is not validated in this process.

1. The term _FMA:24827_ in the following 1 row _[795](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=795:795)_ is from another ontology that is not validated in this process.

1. The term _FMA:16310_ in the following 1 row _[797](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=797:797)_ is from another ontology that is not validated in this process.

1. The term _FMA:16350_ in the following 1 row _[798](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=798:798)_ is from another ontology that is not validated in this process.

1. The term _FMA:16138_ in the following 1 row _[799](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=799:799)_ is from another ontology that is not validated in this process.

1. The term _FMA:16290_ in the following 1 row _[800](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=800:800)_ is from another ontology that is not validated in this process.

1. The term _FMA:16165_ in the following 1 row _[801](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=801:801)_ is from another ontology that is not validated in this process.

1. The term _FMA:16095_ in the following 1 row _[803](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=803:803)_ is from another ontology that is not validated in this process.

1. The term _FMA:16197_ in the following 1 row _[804](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=804:804)_ is from another ontology that is not validated in this process.

1. The term _FMA:16129_ in the following 1 row _[806](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=806:806)_ is from another ontology that is not validated in this process.

1. The term _FMA:16273_ in the following 1 row _[807](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=807:807)_ is from another ontology that is not validated in this process.

1. The term _FMA:16180_ in the following 1 row _[808](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=808:808)_ is from another ontology that is not validated in this process.

1. The term _FMA:24828_ in the following 1 row _[811](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=811:811)_ is from another ontology that is not validated in this process.

1. The term _FMA:16311_ in the following 1 row _[813](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=813:813)_ is from another ontology that is not validated in this process.

1. The term _FMA:16351_ in the following 1 row _[814](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=814:814)_ is from another ontology that is not validated in this process.

1. The term _FMA:16139_ in the following 1 row _[815](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=815:815)_ is from another ontology that is not validated in this process.

1. The term _FMA:16291_ in the following 1 row _[816](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=816:816)_ is from another ontology that is not validated in this process.

1. The term _FMA:16166_ in the following 1 row _[817](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=817:817)_ is from another ontology that is not validated in this process.

1. The term _FMA:16096_ in the following 1 row _[819](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=819:819)_ is from another ontology that is not validated in this process.

1. The term _FMA:16198_ in the following 1 row _[820](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=820:820)_ is from another ontology that is not validated in this process.

1. The term _FMA:16130_ in the following 1 row _[822](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=822:822)_ is from another ontology that is not validated in this process.

1. The term _FMA:16274_ in the following 1 row _[823](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=823:823)_ is from another ontology that is not validated in this process.

1. The term _FMA:16181_ in the following 1 row _[824](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=824:824)_ is from another ontology that is not validated in this process.

1. The term _FMA:24829_ in the following 1 row _[827](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=827:827)_ is from another ontology that is not validated in this process.

1. The term _FMA:16312_ in the following 1 row _[829](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=829:829)_ is from another ontology that is not validated in this process.

1. The term _FMA:16352_ in the following 1 row _[830](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=830:830)_ is from another ontology that is not validated in this process.

1. The term _FMA:16140_ in the following 1 row _[831](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=831:831)_ is from another ontology that is not validated in this process.

1. The term _FMA:16292_ in the following 1 row _[832](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=832:832)_ is from another ontology that is not validated in this process.

1. The term _FMA:16167_ in the following 1 row _[833](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=833:833)_ is from another ontology that is not validated in this process.

1. The term _FMA:16097_ in the following 1 row _[835](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=835:835)_ is from another ontology that is not validated in this process.

1. The term _FMA:16199_ in the following 1 row _[836](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=836:836)_ is from another ontology that is not validated in this process.

1. The term _FMA:16131_ in the following 1 row _[838](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=838:838)_ is from another ontology that is not validated in this process.

1. The term _FMA:16275_ in the following 1 row _[839](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=839:839)_ is from another ontology that is not validated in this process.

1. The term _FMA:16182_ in the following 1 row _[840](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=840:840)_ is from another ontology that is not validated in this process.

1. The term _FMA:24830_ in the following 1 row _[843](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=843:843)_ is from another ontology that is not validated in this process.

1. The term _FMA:16313_ in the following 1 row _[845](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=845:845)_ is from another ontology that is not validated in this process.

1. The term _FMA:16353_ in the following 1 row _[846](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=846:846)_ is from another ontology that is not validated in this process.

1. The term _FMA:16141_ in the following 1 row _[847](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=847:847)_ is from another ontology that is not validated in this process.

1. The term _FMA:16293_ in the following 1 row _[848](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=848:848)_ is from another ontology that is not validated in this process.

1. The term _FMA:16168_ in the following 1 row _[849](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=849:849)_ is from another ontology that is not validated in this process.

1. The term _FMA:16098_ in the following 1 row _[851](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=851:851)_ is from another ontology that is not validated in this process.

1. The term _FMA:16200_ in the following 1 row _[852](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=852:852)_ is from another ontology that is not validated in this process.

1. The term _FMA:16132_ in the following 1 row _[854](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=854:854)_ is from another ontology that is not validated in this process.

1. The term _FMA:16276_ in the following 1 row _[855](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=855:855)_ is from another ontology that is not validated in this process.

1. The term _FMA:16183_ in the following 1 row _[856](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=856:856)_ is from another ontology that is not validated in this process.

1. The term _FMA:24831_ in the following 1 row _[859](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=859:859)_ is from another ontology that is not validated in this process.

1. The term _FMA:31730_ in the following 1 row _[864](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=864:864)_ is from another ontology that is not validated in this process.

1. The term _FMA:31733_ in the following 1 row _[877](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=877:877)_ is from another ontology that is not validated in this process.

1. The term _FMA:16215_ in the following 1 row _[878](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=878:878)_ is from another ontology that is not validated in this process.

1. The term _FMA:75796_ in the following 1 row _[879](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=879:879)_ is from another ontology that is not validated in this process.

1. The term _FMA:9183_ in the following 1 row _[883](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=883:883)_ is from another ontology that is not validated in this process.

1. The term _FMA:9172_ in the following 1 row _[884](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=884:884)_ is from another ontology that is not validated in this process.

1. The term _FMA:9177_ in the following 1 row _[885](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=885:885)_ is from another ontology that is not validated in this process.

1. The term _FMA:9178_ in the following 1 row _[886](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=886:886)_ is from another ontology that is not validated in this process.

1. The term _FMA:9175_ in the following 1 row _[887](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=887:887)_ is from another ontology that is not validated in this process.

1. The term _FMA:9179_ in the following 1 row _[888](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=888:888)_ is from another ontology that is not validated in this process.

1. The term _FMA:9182_ in the following 1 row _[890](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=890:890)_ is from another ontology that is not validated in this process.

1. The term _FMA:9171_ in the following 1 row _[891](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=891:891)_ is from another ontology that is not validated in this process.

1. The term _FMA:9176_ in the following 1 row _[892](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=892:892)_ is from another ontology that is not validated in this process.

1. The term _FMA:9180_ in the following 1 row _[894](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=894:894)_ is from another ontology that is not validated in this process.

1. The term _FMA:10056_ in the following 1 row _[900](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=900:900)_ is from another ontology that is not validated in this process.

1. The term _FMA:10048_ in the following 1 row _[902](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=902:902)_ is from another ontology that is not validated in this process.

1. The term _FMA:10049_ in the following 1 row _[903](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=903:903)_ is from another ontology that is not validated in this process.

1. The term _FMA:10046_ in the following 1 row _[904](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=904:904)_ is from another ontology that is not validated in this process.

1. The term _FMA:10050_ in the following 1 row _[905](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=905:905)_ is from another ontology that is not validated in this process.

1. The term _FMA:10054_ in the following 1 row _[907](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=907:907)_ is from another ontology that is not validated in this process.

1. The term _FMA:10042_ in the following 1 row _[908](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=908:908)_ is from another ontology that is not validated in this process.

1. The term _FMA:10047_ in the following 1 row _[909](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=909:909)_ is from another ontology that is not validated in this process.

1. The term _FMA:10051_ in the following 1 row _[911](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=911:911)_ is from another ontology that is not validated in this process.

1. The term _FMA:13490_ in the following 1 row _[914](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=914:914)_ is from another ontology that is not validated in this process.

1. The term _FMA:10078_ in the following 1 row _[917](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=917:917)_ is from another ontology that is not validated in this process.

1. The term _FMA:10070_ in the following 1 row _[919](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=919:919)_ is from another ontology that is not validated in this process.

1. The term _FMA:10071_ in the following 1 row _[920](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=920:920)_ is from another ontology that is not validated in this process.

1. The term _FMA:10068_ in the following 1 row _[921](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=921:921)_ is from another ontology that is not validated in this process.

1. The term _FMA:10072_ in the following 1 row _[922](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=922:922)_ is from another ontology that is not validated in this process.

1. The term _FMA:10076_ in the following 1 row _[924](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=924:924)_ is from another ontology that is not validated in this process.

1. The term _FMA:10069_ in the following 1 row _[926](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=926:926)_ is from another ontology that is not validated in this process.

1. The term _FMA:10073_ in the following 1 row _[928](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=928:928)_ is from another ontology that is not validated in this process.

1. The term _FMA:13491_ in the following 1 row _[931](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=931:931)_ is from another ontology that is not validated in this process.

1. The term _FMA:11994_ in the following 1 row _[933](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=933:933)_ is from another ontology that is not validated in this process.

1. The term _FMA:10099_ in the following 1 row _[935](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=935:935)_ is from another ontology that is not validated in this process.

1. The term _FMA:10092_ in the following 1 row _[936](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=936:936)_ is from another ontology that is not validated in this process.

1. The term _FMA:10093_ in the following 1 row _[937](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=937:937)_ is from another ontology that is not validated in this process.

1. The term _FMA:10090_ in the following 1 row _[938](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=938:938)_ is from another ontology that is not validated in this process.

1. The term _FMA:10094_ in the following 1 row _[939](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=939:939)_ is from another ontology that is not validated in this process.

1. The term _FMA:10097_ in the following 1 row _[941](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=941:941)_ is from another ontology that is not validated in this process.

1. The term _FMA:10091_ in the following 1 row _[942](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=942:942)_ is from another ontology that is not validated in this process.

1. The term _FMA:10095_ in the following 1 row _[943](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=943:943)_ is from another ontology that is not validated in this process.

1. The term _FMA:13492_ in the following 1 row _[946](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=946:946)_ is from another ontology that is not validated in this process.

1. The term _FMA:9207_ in the following 1 row _[949](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=949:949)_ is from another ontology that is not validated in this process.

1. The term _FMA:9193_ in the following 1 row _[950](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=950:950)_ is from another ontology that is not validated in this process.

1. The term _FMA:9199_ in the following 1 row _[951](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=951:951)_ is from another ontology that is not validated in this process.

1. The term _FMA:9200_ in the following 1 row _[952](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=952:952)_ is from another ontology that is not validated in this process.

1. The term _FMA:9197_ in the following 1 row _[953](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=953:953)_ is from another ontology that is not validated in this process.

1. The term _FMA:9201_ in the following 1 row _[954](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=954:954)_ is from another ontology that is not validated in this process.

1. The term _FMA:9205_ in the following 1 row _[956](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=956:956)_ is from another ontology that is not validated in this process.

1. The term _FMA:9192_ in the following 1 row _[957](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=957:957)_ is from another ontology that is not validated in this process.

1. The term _FMA:9198_ in the following 1 row _[958](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=958:958)_ is from another ontology that is not validated in this process.

1. The term _FMA:9202_ in the following 1 row _[960](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=960:960)_ is from another ontology that is not validated in this process.

1. The term _FMA:13482_ in the following 1 row _[963](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=963:963)_ is from another ontology that is not validated in this process.

1. The term _FMA:9229_ in the following 1 row _[966](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=966:966)_ is from another ontology that is not validated in this process.

1. The term _FMA:9215_ in the following 1 row _[967](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=967:967)_ is from another ontology that is not validated in this process.

1. The term _FMA:9221_ in the following 1 row _[968](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=968:968)_ is from another ontology that is not validated in this process.

1. The term _FMA:9222_ in the following 1 row _[969](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=969:969)_ is from another ontology that is not validated in this process.

1. The term _FMA:9219_ in the following 1 row _[970](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=970:970)_ is from another ontology that is not validated in this process.

1. The term _FMA:9223_ in the following 1 row _[971](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=971:971)_ is from another ontology that is not validated in this process.

1. The term _FMA:9227_ in the following 1 row _[973](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=973:973)_ is from another ontology that is not validated in this process.

1. The term _FMA:9214_ in the following 1 row _[974](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=974:974)_ is from another ontology that is not validated in this process.

1. The term _FMA:9220_ in the following 1 row _[975](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=975:975)_ is from another ontology that is not validated in this process.

1. The term _FMA:9224_ in the following 1 row _[977](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=977:977)_ is from another ontology that is not validated in this process.

1. The term _FMA:13483_ in the following 1 row _[980](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=980:980)_ is from another ontology that is not validated in this process.

1. The term _FMA:9268_ in the following 1 row _[983](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=983:983)_ is from another ontology that is not validated in this process.

1. The term _FMA:9254_ in the following 1 row _[984](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=984:984)_ is from another ontology that is not validated in this process.

1. The term _FMA:9260_ in the following 1 row _[985](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=985:985)_ is from another ontology that is not validated in this process.

1. The term _FMA:9261_ in the following 1 row _[986](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=986:986)_ is from another ontology that is not validated in this process.

1. The term _FMA:9258_ in the following 1 row _[987](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=987:987)_ is from another ontology that is not validated in this process.

1. The term _FMA:9262_ in the following 1 row _[988](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=988:988)_ is from another ontology that is not validated in this process.

1. The term _FMA:9266_ in the following 1 row _[990](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=990:990)_ is from another ontology that is not validated in this process.

1. The term _FMA:9253_ in the following 1 row _[991](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=991:991)_ is from another ontology that is not validated in this process.

1. The term _FMA:9259_ in the following 1 row _[992](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=992:992)_ is from another ontology that is not validated in this process.

1. The term _FMA:9263_ in the following 1 row _[994](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=994:994)_ is from another ontology that is not validated in this process.

1. The term _FMA:13484_ in the following 1 row _[997](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=997:997)_ is from another ontology that is not validated in this process.

1. The term _FMA:9942_ in the following 1 row _[1000](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1000:1000)_ is from another ontology that is not validated in this process.

1. The term _FMA:9928_ in the following 1 row _[1001](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1001:1001)_ is from another ontology that is not validated in this process.

1. The term _FMA:9934_ in the following 1 row _[1002](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1002:1002)_ is from another ontology that is not validated in this process.

1. The term _FMA:9935_ in the following 1 row _[1003](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1003:1003)_ is from another ontology that is not validated in this process.

1. The term _FMA:9932_ in the following 1 row _[1004](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1004:1004)_ is from another ontology that is not validated in this process.

1. The term _FMA:9936_ in the following 1 row _[1005](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1005:1005)_ is from another ontology that is not validated in this process.

1. The term _FMA:9940_ in the following 1 row _[1007](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1007:1007)_ is from another ontology that is not validated in this process.

1. The term _FMA:9927_ in the following 1 row _[1008](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1008:1008)_ is from another ontology that is not validated in this process.

1. The term _FMA:9933_ in the following 1 row _[1009](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1009:1009)_ is from another ontology that is not validated in this process.

1. The term _FMA:9937_ in the following 1 row _[1011](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1011:1011)_ is from another ontology that is not validated in this process.

1. The term _FMA:13485_ in the following 1 row _[1014](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1014:1014)_ is from another ontology that is not validated in this process.

1. The term _FMA:9965_ in the following 1 row _[1017](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1017:1017)_ is from another ontology that is not validated in this process.

1. The term _FMA:9951_ in the following 1 row _[1018](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1018:1018)_ is from another ontology that is not validated in this process.

1. The term _FMA:9957_ in the following 1 row _[1019](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1019:1019)_ is from another ontology that is not validated in this process.

1. The term _FMA:9958_ in the following 1 row _[1020](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1020:1020)_ is from another ontology that is not validated in this process.

1. The term _FMA:9955_ in the following 1 row _[1021](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1021:1021)_ is from another ontology that is not validated in this process.

1. The term _FMA:9959_ in the following 1 row _[1022](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1022:1022)_ is from another ontology that is not validated in this process.

1. The term _FMA:9963_ in the following 1 row _[1024](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1024:1024)_ is from another ontology that is not validated in this process.

1. The term _FMA:9950_ in the following 1 row _[1025](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1025:1025)_ is from another ontology that is not validated in this process.

1. The term _FMA:9956_ in the following 1 row _[1026](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1026:1026)_ is from another ontology that is not validated in this process.

1. The term _FMA:9960_ in the following 1 row _[1028](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1028:1028)_ is from another ontology that is not validated in this process.

1. The term _FMA:13486_ in the following 1 row _[1031](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1031:1031)_ is from another ontology that is not validated in this process.

1. The term _FMA:9988_ in the following 1 row _[1034](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1034:1034)_ is from another ontology that is not validated in this process.

1. The term _FMA:9974_ in the following 1 row _[1035](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1035:1035)_ is from another ontology that is not validated in this process.

1. The term _FMA:9980_ in the following 1 row _[1036](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1036:1036)_ is from another ontology that is not validated in this process.

1. The term _FMA:9981_ in the following 1 row _[1037](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1037:1037)_ is from another ontology that is not validated in this process.

1. The term _FMA:9978_ in the following 1 row _[1038](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1038:1038)_ is from another ontology that is not validated in this process.

1. The term _FMA:9982_ in the following 1 row _[1039](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1039:1039)_ is from another ontology that is not validated in this process.

1. The term _FMA:9986_ in the following 1 row _[1041](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1041:1041)_ is from another ontology that is not validated in this process.

1. The term _FMA:9973_ in the following 1 row _[1042](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1042:1042)_ is from another ontology that is not validated in this process.

1. The term _FMA:9979_ in the following 1 row _[1043](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1043:1043)_ is from another ontology that is not validated in this process.

1. The term _FMA:9983_ in the following 1 row _[1045](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1045:1045)_ is from another ontology that is not validated in this process.

1. The term _FMA:13487_ in the following 1 row _[1048](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1048:1048)_ is from another ontology that is not validated in this process.

1. The term _FMA:10011_ in the following 1 row _[1051](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1051:1051)_ is from another ontology that is not validated in this process.

1. The term _FMA:9997_ in the following 1 row _[1052](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1052:1052)_ is from another ontology that is not validated in this process.

1. The term _FMA:10003_ in the following 1 row _[1053](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1053:1053)_ is from another ontology that is not validated in this process.

1. The term _FMA:10004_ in the following 1 row _[1054](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1054:1054)_ is from another ontology that is not validated in this process.

1. The term _FMA:10001_ in the following 1 row _[1055](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1055:1055)_ is from another ontology that is not validated in this process.

1. The term _FMA:10005_ in the following 1 row _[1056](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1056:1056)_ is from another ontology that is not validated in this process.

1. The term _FMA:10009_ in the following 1 row _[1058](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1058:1058)_ is from another ontology that is not validated in this process.

1. The term _FMA:9996_ in the following 1 row _[1059](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1059:1059)_ is from another ontology that is not validated in this process.

1. The term _FMA:10002_ in the following 1 row _[1060](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1060:1060)_ is from another ontology that is not validated in this process.

1. The term _FMA:10006_ in the following 1 row _[1062](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1062:1062)_ is from another ontology that is not validated in this process.

1. The term _FMA:13488_ in the following 1 row _[1065](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1065:1065)_ is from another ontology that is not validated in this process.

1. The term _FMA:10034_ in the following 1 row _[1068](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1068:1068)_ is from another ontology that is not validated in this process.

1. The term _FMA:13610_ in the following 1 row _[1069](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1069:1069)_ is from another ontology that is not validated in this process.

1. The term _FMA:10026_ in the following 1 row _[1070](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1070:1070)_ is from another ontology that is not validated in this process.

1. The term _FMA:10027_ in the following 1 row _[1071](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1071:1071)_ is from another ontology that is not validated in this process.

1. The term _FMA:10024_ in the following 1 row _[1072](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1072:1072)_ is from another ontology that is not validated in this process.

1. The term _FMA:10028_ in the following 1 row _[1073](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1073:1073)_ is from another ontology that is not validated in this process.

1. The term _FMA:10032_ in the following 1 row _[1075](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1075:1075)_ is from another ontology that is not validated in this process.

1. The term _FMA:10019_ in the following 1 row _[1076](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1076:1076)_ is from another ontology that is not validated in this process.

1. The term _FMA:10025_ in the following 1 row _[1077](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1077:1077)_ is from another ontology that is not validated in this process.

1. The term _FMA:10029_ in the following 1 row _[1079](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1079:1079)_ is from another ontology that is not validated in this process.

1. The term _FMA:13489_ in the following 1 row _[1082](https://docs.google.com/spreadsheets/d/1lPVO9TZPdC_c2VNQLOxELyFKcLbqaRq-jJMdOO_ngfY/edit#gid=0&range=1082:1082)_ is from another ontology that is not validated in this process.


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



- No issues found.






## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



- No issues found.






# New CL terms
[**Report**](new_cl_terms_Skeleton.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Skeleton.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Skeleton_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Skeleton_AS_has_part_CT_log.tsv)