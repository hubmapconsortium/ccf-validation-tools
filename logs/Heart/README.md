
ASCT+B Validation Reports for Heart (2023-05-22)
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
  
1. In row _[142](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=142:142)_, the term _[UBERON:0002353](http://purl.obolibrary.org/obo/UBERON_0002353)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _atrioventricular bundle_ and the one in the **ontology** is _bundle of His_. For reference, the given name/label **by SMEs** is _bundle of His_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[133](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=133:133)_, the term _[UBERON:0006958](http://purl.obolibrary.org/obo/UBERON_0006958)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _great cardiac vein_ and the one in the **ontology** is _great vein of heart_. For reference, the given name/label **by SMEs** is _great cardiac vein_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[21](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=21:21)_, the term _[CL:0002138](http://purl.obolibrary.org/obo/CL_0002138)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _lymphatic endothelial cell_ and the one in the **ontology** is _endothelial cell of lymphatic vessel_. For reference, the given name/label **by SMEs** is _lymphatic endothelial cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[196](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=196:196)_, the term _[UBERON:0000946](http://purl.obolibrary.org/obo/UBERON_0000946)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _Cardial valve_ and the one in the **ontology** is _cardiac valve_. For reference, the given name/label **by SMEs** is _Cardial valve_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[29](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=29:29)_, no term id was found for the name/label _vasculature_.

1. In row _[130](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=130:130)_, no term id was found for the name/label _septal perforating arteries_.

1. In row _[131](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=131:131)_, no term id was found for the name/label _septal perforating arteries_.

1. In row _[132](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=132:132)_, no term id was found for the name/label _septal perforating arteries_.

1. In row _[196](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=196:196)_, no term id was found for the name/label _valve interstitial cell_.

1. In row _[198](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=198:198)_, no term id was found for the name/label _valve interstitial cell_.

1. In row _[200](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=200:200)_, no term id was found for the name/label _valve interstitial cell_.

1. In row _[202](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=202:202)_, no term id was found for the name/label _valve interstitial cell_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[13](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=13:13)_, the term _FMA:3823_ is from another ontology that is not validated in this process.

1. In row _[14](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=14:14)_, the term _FMA:3823_ is from another ontology that is not validated in this process.

1. In row _[15](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=15:15)_, the term _FMA:3823_ is from another ontology that is not validated in this process.

1. In row _[30](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=30:30)_, the term _FMA:76767_ is from another ontology that is not validated in this process.

1. In row _[31](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=31:31)_, the term _FMA:76767_ is from another ontology that is not validated in this process.

1. In row _[32](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=32:32)_, the term _FMA:76767_ is from another ontology that is not validated in this process.

1. In row _[33](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=33:33)_, the term _FMA:83531_ is from another ontology that is not validated in this process.

1. In row _[34](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=34:34)_, the term _FMA:83531_ is from another ontology that is not validated in this process.

1. In row _[35](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=35:35)_, the term _FMA:83531_ is from another ontology that is not validated in this process.

1. In row _[36](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=36:36)_, the term _FMA:83531_ is from another ontology that is not validated in this process.

1. In row _[40](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=40:40)_, the term _FMA:3851_ is from another ontology that is not validated in this process.

1. In row _[41](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=41:41)_, the term _FMA:3851_ is from another ontology that is not validated in this process.

1. In row _[42](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=42:42)_, the term _FMA:3851_ is from another ontology that is not validated in this process.

1. In row _[54](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=54:54)_, the term _FMA:83532_ is from another ontology that is not validated in this process.

1. In row _[55](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=55:55)_, the term _FMA:83532_ is from another ontology that is not validated in this process.

1. In row _[56](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=56:56)_, the term _FMA:83532_ is from another ontology that is not validated in this process.

1. In row _[57](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=57:57)_, the term _FMA:83532_ is from another ontology that is not validated in this process.

1. In row _[58](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=58:58)_, the term _FMA:83532_ is from another ontology that is not validated in this process.

1. In row _[59](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=59:59)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[60](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=60:60)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[61](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=61:61)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[62](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=62:62)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[63](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=63:63)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[64](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=64:64)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[71](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=71:71)_, the term _FMA:49913_ is from another ontology that is not validated in this process.

1. In row _[72](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=72:72)_, the term _FMA:49913_ is from another ontology that is not validated in this process.

1. In row _[73](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=73:73)_, the term _FMA:49913_ is from another ontology that is not validated in this process.

1. In row _[74](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=74:74)_, the term _FMA:49916_ is from another ontology that is not validated in this process.

1. In row _[75](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=75:75)_, the term _FMA:49916_ is from another ontology that is not validated in this process.

1. In row _[76](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=76:76)_, the term _FMA:49916_ is from another ontology that is not validated in this process.

1. In row _[77](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=77:77)_, the term _FMA:49911_ is from another ontology that is not validated in this process.

1. In row _[78](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=78:78)_, the term _FMA:49911_ is from another ontology that is not validated in this process.

1. In row _[79](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=79:79)_, the term _FMA:49911_ is from another ontology that is not validated in this process.

1. In row _[80](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=80:80)_, the term _FMA:49914_ is from another ontology that is not validated in this process.

1. In row _[81](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=81:81)_, the term _FMA:49914_ is from another ontology that is not validated in this process.

1. In row _[82](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=82:82)_, the term _FMA:49914_ is from another ontology that is not validated in this process.

1. In row _[83](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=83:83)_, the term _FMA:4715_ is from another ontology that is not validated in this process.

1. In row _[84](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=84:84)_, the term _FMA:4715_ is from another ontology that is not validated in this process.

1. In row _[85](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=85:85)_, the term _FMA:4715_ is from another ontology that is not validated in this process.

1. In row _[86](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=86:86)_, the term _FMA:83532_ is from another ontology that is not validated in this process.

1. In row _[87](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=87:87)_, the term _FMA:83532_ is from another ontology that is not validated in this process.

1. In row _[88](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=88:88)_, the term _FMA:83532_ is from another ontology that is not validated in this process.

1. In row _[89](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=89:89)_, the term _FMA:83532_ is from another ontology that is not validated in this process.

1. In row _[109](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=109:109)_, the term _FMA:3860_ is from another ontology that is not validated in this process.

1. In row _[110](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=110:110)_, the term _FMA:3860_ is from another ontology that is not validated in this process.

1. In row _[111](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=111:111)_, the term _FMA:3860_ is from another ontology that is not validated in this process.

1. In row _[112](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=112:112)_, the term _FMA:3902_ is from another ontology that is not validated in this process.

1. In row _[113](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=113:113)_, the term _FMA:3902_ is from another ontology that is not validated in this process.

1. In row _[114](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=114:114)_, the term _FMA:3902_ is from another ontology that is not validated in this process.

1. In row _[115](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=115:115)_, the term _FMA:3835_ is from another ontology that is not validated in this process.

1. In row _[116](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=116:116)_, the term _FMA:3835_ is from another ontology that is not validated in this process.

1. In row _[117](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=117:117)_, the term _FMA:3835_ is from another ontology that is not validated in this process.

1. In row _[118](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=118:118)_, the term _FMA:4708_ is from another ontology that is not validated in this process.

1. In row _[119](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=119:119)_, the term _FMA:4708_ is from another ontology that is not validated in this process.

1. In row _[120](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=120:120)_, the term _FMA:4708_ is from another ontology that is not validated in this process.

1. In row _[121](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=121:121)_, the term _FMA:4712_ is from another ontology that is not validated in this process.

1. In row _[122](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=122:122)_, the term _FMA:4712_ is from another ontology that is not validated in this process.

1. In row _[123](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=123:123)_, the term _FMA:4712_ is from another ontology that is not validated in this process.

1. In row _[124](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=124:124)_, the term _FMA:3862_ is from another ontology that is not validated in this process.

1. In row _[125](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=125:125)_, the term _FMA:3862_ is from another ontology that is not validated in this process.

1. In row _[126](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=126:126)_, the term _FMA:3862_ is from another ontology that is not validated in this process.

1. In row _[127](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=127:127)_, the term _FMA:3840_ is from another ontology that is not validated in this process.

1. In row _[128](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=128:128)_, the term _FMA:3840_ is from another ontology that is not validated in this process.

1. In row _[129](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=129:129)_, the term _FMA:3840_ is from another ontology that is not validated in this process.

1. In row _[143](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=143:143)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[144](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=144:144)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[145](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=145:145)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[146](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=146:146)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[147](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=147:147)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[148](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=148:148)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[149](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=149:149)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[150](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=150:150)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[151](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=151:151)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[152](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=152:152)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[153](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=153:153)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[154](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=154:154)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[155](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=155:155)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[156](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=156:156)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[167](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=167:167)_, the term _FMA:15736_ is from another ontology that is not validated in this process.

1. In row _[168](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=168:168)_, the term _FMA:15736_ is from another ontology that is not validated in this process.

1. In row _[169](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=169:169)_, the term _FMA:15736_ is from another ontology that is not validated in this process.

1. In row _[170](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=170:170)_, the term _FMA:3818_ is from another ontology that is not validated in this process.

1. In row _[171](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=171:171)_, the term _FMA:3818_ is from another ontology that is not validated in this process.

1. In row _[172](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=172:172)_, the term _FMA:3818_ is from another ontology that is not validated in this process.

1. In row _[173](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=173:173)_, the term _FMA:76767_ is from another ontology that is not validated in this process.

1. In row _[174](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=174:174)_, the term _FMA:76767_ is from another ontology that is not validated in this process.

1. In row _[175](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=175:175)_, the term _FMA:76767_ is from another ontology that is not validated in this process.

1. In row _[182](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=182:182)_, the term _FMA:9535_ is from another ontology that is not validated in this process.

1. In row _[183](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=183:183)_, the term _FMA:9535_ is from another ontology that is not validated in this process.

1. In row _[184](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=184:184)_, the term _FMA:9535_ is from another ontology that is not validated in this process.

1. In row _[185](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=185:185)_, the term _FMA:9535_ is from another ontology that is not validated in this process.

1. In row _[186](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=186:186)_, the term _FMA:7272_ is from another ontology that is not validated in this process.

1. In row _[187](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=187:187)_, the term _FMA:7272_ is from another ontology that is not validated in this process.

1. In row _[188](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=188:188)_, the term _FMA:7272_ is from another ontology that is not validated in this process.

1. In row _[189](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=189:189)_, the term _FMA:7272_ is from another ontology that is not validated in this process.

1. In row _[190](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=190:190)_, the term _FMA:7272_ is from another ontology that is not validated in this process.

1. In row _[191](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=191:191)_, the term _FMA:7272_ is from another ontology that is not validated in this process.

1. In row _[192](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=192:192)_, the term _FMA:7272_ is from another ontology that is not validated in this process.

1. In row _[193](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=193:193)_, the term _FMA:7272_ is from another ontology that is not validated in this process.

1. In row _[194](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=194:194)_, the term _FMA:7272_ is from another ontology that is not validated in this process.

1. In row _[195](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=195:195)_, the term _FMA:7272_ is from another ontology that is not validated in this process.

1. In row _[211](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=211:211)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[212](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=212:212)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[213](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=213:213)_, the term _FMA:83539_ is from another ontology that is not validated in this process.

1. In row _[214](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=214:214)_, the term _FMA:83539_ is from another ontology that is not validated in this process.


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



|     | s              | slabel                                           | user_slabel            | o              | olabel                  | user_olabel               | row_number                                                                                                                   |   deltaIC |
|-----|----------------|--------------------------------------------------|------------------------|----------------|-------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------|-----------|
|  12 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002079 | left cardiac atrium     | left atrium               | [66](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=66:66)    |  24.5502  |
|  13 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002079 | left cardiac atrium     | left atrium               | [65](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=65:65)    |  24.5502  |
|  14 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002079 | left cardiac atrium     | left atrium               | [67](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=67:67)    |  24.5502  |
|  15 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002080 | heart right ventricle   | right ventricle           | [176](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=176:176) |  24.3671  |
|  16 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002080 | heart right ventricle   | right ventricle           | [177](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=177:177) |  24.3671  |
|  17 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002080 | heart right ventricle   | right ventricle           | [178](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=178:178) |  24.3671  |
|  26 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002078 | right cardiac atrium    | right atrium              | [28](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=28:28)    |  21.6813  |
|  27 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002078 | right cardiac atrium    | right atrium              | [27](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=27:27)    |  21.6813  |
|  28 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002078 | right cardiac atrium    | right atrium              | [26](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=26:26)    |  21.6813  |
|  29 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002084 | heart left ventricle    | left ventricle            | [96](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=96:96)    |  21.5226  |
|  30 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002084 | heart left ventricle    | left ventricle            | [95](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=95:95)    |  21.5226  |
|  31 | UBERON:0002049 | vasculature                                      | vasculature            | UBERON:0002084 | heart left ventricle    | left ventricle            | [94](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=94:94)    |  21.5226  |
|  64 | UBERON:0001982 | capillary                                        | vasculature            | UBERON:0002094 | interventricular septum | septum                    | [139](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=139:139) |  13.3601  |
|  65 | UBERON:0001982 | capillary                                        | vasculature            | UBERON:0002094 | interventricular septum | septum                    | [140](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=140:140) |  13.3601  |
|  80 | UBERON:0001982 | capillary                                        | vasculature            | UBERON:0002079 | left cardiac atrium     | left atrium               | [68](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=68:68)    |  10.1596  |
|  81 | UBERON:0001982 | capillary                                        | vasculature            | UBERON:0002079 | left cardiac atrium     | left atrium               | [69](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=69:69)    |  10.1596  |
|  82 | UBERON:0001982 | capillary                                        | vasculature            | UBERON:0002080 | heart right ventricle   | right ventricle           | [180](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=180:180) |   9.97639 |
|  83 | UBERON:0001982 | capillary                                        | vasculature            | UBERON:0002080 | heart right ventricle   | right ventricle           | [179](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=179:179) |   9.97639 |
|  96 | UBERON:0001982 | capillary                                        | vasculature            | UBERON:0002084 | heart left ventricle    | left ventricle            | [98](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=98:98)    |   7.13192 |
|  97 | UBERON:0001982 | capillary                                        | vasculature            | UBERON:0002084 | heart left ventricle    | left ventricle            | [97](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=97:97)    |   7.13192 |
| 121 | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium             | UBERON:0002078 | right cardiac atrium    | right atrium              | [20](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=20:20)    | nan       |
| 122 | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium             | UBERON:0002078 | right cardiac atrium    | right atrium              | [21](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=21:21)    | nan       |
| 123 | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium             | UBERON:0002078 | right cardiac atrium    | right atrium              | [22](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=22:22)    | nan       |
| 124 | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium             | UBERON:0002078 | right cardiac atrium    | right atrium              | [23](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=23:23)    | nan       |
| 125 | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium             | UBERON:0002078 | right cardiac atrium    | right atrium              | [24](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=24:24)    | nan       |
| 126 | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium             | UBERON:0002078 | right cardiac atrium    | right atrium              | [25](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=25:25)    | nan       |
| 134 | UBERON:0035422 | circumflex branch of left coronary artery        | left circumflex artery | UBERON:0011820 | atrioventricular region | atrioventricular junction | [37](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=37:37)    | nan       |
| 135 | UBERON:0035422 | circumflex branch of left coronary artery        | left circumflex artery | UBERON:0011820 | atrioventricular region | atrioventricular junction | [38](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=38:38)    | nan       |
| 137 | UBERON:0035422 | circumflex branch of left coronary artery        | left circumflex artery | UBERON:0011820 | atrioventricular region | atrioventricular junction | [39](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=39:39)    | nan       |
| 140 | UBERON:0005438 | coronary sinus                                   | coronary sinus         | UBERON:0011820 | atrioventricular region | atrioventricular junction | [43](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=43:43)    | nan       |
| 142 | UBERON:0005438 | coronary sinus                                   | coronary sinus         | UBERON:0011820 | atrioventricular region | atrioventricular junction | [44](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=44:44)    | nan       |
| 143 | UBERON:0005438 | coronary sinus                                   | coronary sinus         | UBERON:0011820 | atrioventricular region | atrioventricular junction | [45](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=45:45)    | nan       |
| 144 | UBERON:0002352 | atrioventricular node                            | atrioventricular node  | UBERON:0011820 | atrioventricular region | atrioventricular junction | [46](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=46:46)    | nan       |
| 146 | UBERON:0002352 | atrioventricular node                            | atrioventricular node  | UBERON:0011820 | atrioventricular region | atrioventricular junction | [47](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=47:47)    | nan       |
| 147 | UBERON:0001625 | right coronary artery                            | right coronary artery  | UBERON:0011820 | atrioventricular region | atrioventricular junction | [48](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=48:48)    | nan       |
| 148 | UBERON:0001625 | right coronary artery                            | right coronary artery  | UBERON:0011820 | atrioventricular region | atrioventricular junction | [49](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=49:49)    | nan       |
| 150 | UBERON:0001625 | right coronary artery                            | right coronary artery  | UBERON:0011820 | atrioventricular region | atrioventricular junction | [50](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=50:50)    | nan       |
| 151 | UBERON:0035374 | small cardiac vein                               | small cardiac vein     | UBERON:0011820 | atrioventricular region | atrioventricular junction | [51](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=51:51)    | nan       |
| 152 | UBERON:0035374 | small cardiac vein                               | small cardiac vein     | UBERON:0011820 | atrioventricular region | atrioventricular junction | [52](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=52:52)    | nan       |
| 154 | UBERON:0035374 | small cardiac vein                               | small cardiac vein     | UBERON:0011820 | atrioventricular region | atrioventricular junction | [53](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=53:53)    | nan       |
| 164 | UBERON:0001979 | venule                                           | vasculature            | UBERON:0002079 | left cardiac atrium     | left atrium               | [70](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=70:70)    | nan       |
| 180 | UBERON:0001979 | venule                                           | vasculature            | UBERON:0002084 | heart left ventricle    | left ventricle            | [99](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=99:99)    | nan       |
| 192 | UBERON:0006958 | great vein of heart                              | great cardiac vein     | UBERON:0002094 | interventricular septum | septum                    | [133](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=133:133) | nan       |
| 193 | UBERON:0006958 | great vein of heart                              | great cardiac vein     | UBERON:0002094 | interventricular septum | septum                    | [134](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=134:134) | nan       |
| 194 | UBERON:0006958 | great vein of heart                              | great cardiac vein     | UBERON:0002094 | interventricular septum | septum                    | [135](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=135:135) | nan       |
| 195 | UBERON:0009687 | middle cardiac vein                              | middle cardiac vein    | UBERON:0002094 | interventricular septum | septum                    | [136](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=136:136) | nan       |
| 196 | UBERON:0009687 | middle cardiac vein                              | middle cardiac vein    | UBERON:0002094 | interventricular septum | septum                    | [137](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=137:137) | nan       |
| 197 | UBERON:0009687 | middle cardiac vein                              | middle cardiac vein    | UBERON:0002094 | interventricular septum | septum                    | [138](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=138:138) | nan       |
| 199 | UBERON:0001979 | venule                                           | vasculature            | UBERON:0002094 | interventricular septum | septum                    | [141](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=141:141) | nan       |
| 200 | UBERON:0002353 | bundle of His                                    | bundle of His          | UBERON:0002094 | interventricular septum | septum                    | [142](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=142:142) | nan       |
| 213 | UBERON:0001979 | venule                                           | vasculature            | UBERON:0002080 | heart right ventricle   | right ventricle           | [181](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=181:181) | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|     | s          | slabel                                    | user_slabel                                | o              | olabel                                           | user_olabel               | row_number                                                                                                                   |
|-----|------------|-------------------------------------------|--------------------------------------------|----------------|--------------------------------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------|
|   0 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002080 | heart right ventricle                            | right ventricle           | [172](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=172:172) |
|   1 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0035374 | small cardiac vein                               | small cardiac vein        | [53](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=53:53)    |
|   2 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002080 | heart right ventricle                            | right ventricle           | [192](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=192:192) |
|   3 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0001625 | right coronary artery                            | right coronary artery     | [50](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=50:50)    |
|   4 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002080 | heart right ventricle                            | right ventricle           | [188](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=188:188) |
|   5 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0005438 | coronary sinus                                   | coronary sinus            | [45](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=45:45)    |
|   6 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002084 | heart left ventricle                             | left ventricle            | [111](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=111:111) |
|   7 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0011820 | atrioventricular region                          | atrioventricular junction | [42](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=42:42)    |
|   8 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002084 | heart left ventricle                             | left ventricle            | [114](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=114:114) |
|   9 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002348 | epicardium                                       | Epicardium                | [208](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=208:208) |
|  10 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0035422 | circumflex branch of left coronary artery        | left circumflex artery    | [39](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=39:39)    |
|  11 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002084 | heart left ventricle                             | left ventricle            | [117](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=117:117) |
|  12 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002084 | heart left ventricle                             | left ventricle            | [123](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=123:123) |
|  13 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002078 | right cardiac atrium                             | right atrium              | [32](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=32:32)    |
|  14 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002094 | interventricular septum                          | septum                    | [126](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=126:126) |
|  15 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002084 | heart left ventricle                             | left ventricle            | [120](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=120:120) |
|  16 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002094 | interventricular septum                          | septum                    | [129](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=129:129) |
|  17 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002080 | heart right ventricle                            | right ventricle           | [169](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=169:169) |
|  18 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002094 | interventricular septum                          | septum                    | [132](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=132:132) |
|  19 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002078 | right cardiac atrium                             | right atrium              | [15](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=15:15)    |
|  20 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0006958 | great vein of heart                              | great cardiac vein        | [135](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=135:135) |
|  21 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0009687 | middle cardiac vein                              | middle cardiac vein       | [138](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=138:138) |
|  22 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002049 | vasculature                                      | vasculature               | [178](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=178:178) |
|  23 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002094 | interventricular septum                          | septum                    | [145](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=145:145) |
|  24 | CL:0000057 | fibroblast                                | fibroblast                                 | UBERON:0002080 | heart right ventricle                            | right ventricle           | [175](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=175:175) |
|  25 | CL:0000071 | blood vessel endothelial cell             | endothelial cell                           | UBERON:0002079 | left cardiac atrium                              | left atrium               | [77](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=77:77)    |
|  26 | CL:0000071 | blood vessel endothelial cell             | endothelial cell                           | UBERON:0002079 | left cardiac atrium                              | left atrium               | [80](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=80:80)    |
|  27 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0002080 | heart right ventricle                            | right ventricle           | [168](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=168:168) |
|  28 | CL:0000071 | blood vessel endothelial cell             | endothelial cell                           | UBERON:0002079 | left cardiac atrium                              | left atrium               | [83](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=83:83)    |
|  29 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0002080 | heart right ventricle                            | right ventricle           | [171](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=171:171) |
|  30 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0002080 | heart right ventricle                            | right ventricle           | [174](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=174:174) |
|  31 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0002084 | heart left ventricle                             | left ventricle            | [110](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=110:110) |
|  32 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0002084 | heart left ventricle                             | left ventricle            | [113](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=113:113) |
|  33 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0009687 | middle cardiac vein                              | middle cardiac vein       | [137](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=137:137) |
|  34 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0002084 | heart left ventricle                             | left ventricle            | [116](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=116:116) |
|  35 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0006958 | great vein of heart                              | great cardiac vein        | [134](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=134:134) |
|  36 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0002084 | heart left ventricle                             | left ventricle            | [119](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=119:119) |
|  37 | CL:0000071 | blood vessel endothelial cell             | endothelial cell                           | UBERON:0002079 | left cardiac atrium                              | left atrium               | [74](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=74:74)    |
|  38 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0002084 | heart left ventricle                             | left ventricle            | [122](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=122:122) |
|  39 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0002094 | interventricular septum                          | septum                    | [131](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=131:131) |
|  40 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0002094 | interventricular septum                          | septum                    | [125](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=125:125) |
|  41 | CL:0000071 | blood vessel endothelial cell             | smooth muscle cell                         | UBERON:0002094 | interventricular septum                          | septum                    | [128](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=128:128) |
|  42 | CL:0000071 | blood vessel endothelial cell             | endothelial cell                           | UBERON:0002079 | left cardiac atrium                              | left atrium               | [71](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=71:71)    |
|  43 | CL:0000071 | blood vessel endothelial cell             | endothelial cell                           | UBERON:0002080 | heart right ventricle                            | right ventricle           | [190](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=190:190) |
|  44 | CL:0000071 | blood vessel endothelial cell             | endothelial cell                           | UBERON:0002348 | epicardium                                       | Epicardium                | [209](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=209:209) |
|  45 | CL:0000071 | blood vessel endothelial cell             | endothelial cell                           | UBERON:0002137 | Aortic valve                                     | Aortic valve              | [203](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=203:203) |
|  46 | CL:0000077 | mesothelial cell                          | mesothelial cell                           | UBERON:0002348 | epicardium                                       | Epicardium                | [204](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=204:204) |
|  47 | CL:0000097 | mast cell                                 | mast cell                                  | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [103](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=103:103) |
|  48 | CL:0000097 | mast cell                                 | mast cell                                  | UBERON:0002094 | interventricular septum                          | septum                    | [151](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=151:151) |
|  49 | CL:0000097 | mast cell                                 | mast cell                                  | UBERON:0006567 | right ventricle myocardium                       | myocardium                | [157](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=157:157) |
|  50 | CL:0000097 | mast cell                                 | mast cell                                  | UBERON:0002348 | epicardium                                       | Epicardium                | [211](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=211:211) |
|  51 | CL:0000097 | mast cell                                 | mast cell                                  | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium                | [20](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=20:20)    |
|  52 | CL:0000097 | mast cell                                 | mast cell                                  | UBERON:0002079 | left cardiac atrium                              | left atrium               | [59](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=59:59)    |
|  53 | CL:0000136 | fat cell                                  | adipocyte                                  | UBERON:0002094 | interventricular septum                          | septum                    | [150](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=150:150) |
|  54 | CL:0000136 | fat cell                                  | adipocyte                                  | UBERON:0002078 | right cardiac atrium                             | right atrium              | [36](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=36:36)    |
|  55 | CL:0000136 | fat cell                                  | adipocyte                                  | UBERON:0002080 | heart right ventricle                            | right ventricle           | [185](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=185:185) |
|  56 | CL:0000136 | fat cell                                  | adipocyte                                  | UBERON:0002079 | left cardiac atrium                              | left atrium               | [89](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=89:89)    |
|  57 | CL:0000136 | fat cell                                  | adipocyte                                  | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [102](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=102:102) |
|  58 | CL:0000136 | fat cell                                  | adipocyte                                  | UBERON:0002352 | atrioventricular node                            | atrioventricular node     | [47](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=47:47)    |
|  59 | CL:0000235 | macrophage                                | macrophage                                 | UBERON:0002080 | heart right ventricle                            | right ventricle           | [189](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=189:189) |
|  60 | CL:0000235 | macrophage                                | macrophage                                 | UBERON:0003379 | cardiac muscle of right atrium                   | myocardium                | [18](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=18:18)    |
|  61 | CL:0000235 | macrophage                                | macrophage                                 | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [93](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=93:93)    |
|  62 | CL:0000235 | macrophage                                | macrophage                                 | UBERON:0002348 | epicardium                                       | Epicardium                | [210](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=210:210) |
|  63 | CL:0000235 | macrophage                                | macrophage                                 | UBERON:0006567 | right ventricle myocardium                       | myocardium                | [166](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=166:166) |
|  64 | CL:0000235 | macrophage                                | macrophage                                 | UBERON:0002094 | interventricular septum                          | septum                    | [146](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=146:146) |
|  65 | CL:0000235 | macrophage                                | macrophage                                 | UBERON:0002079 | left cardiac atrium                              | left atrium               | [57](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=57:57)    |
|  66 | CL:0000236 | B cell                                    | B lymphocyte                               | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [105](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=105:105) |
|  67 | CL:0000236 | B cell                                    | B lymphocyte                               | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium                | [22](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=22:22)    |
|  68 | CL:0000236 | B cell                                    | B lymphocyte                               | UBERON:0002094 | interventricular septum                          | septum                    | [153](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=153:153) |
|  69 | CL:0000236 | B cell                                    | B lymphocyte                               | UBERON:0002079 | left cardiac atrium                              | left atrium               | [61](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=61:61)    |
|  70 | CL:0000236 | B cell                                    | B lymphocyte                               | UBERON:0002348 | epicardium                                       | Epicardium                | [213](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=213:213) |
|  71 | CL:0000236 | B cell                                    | B lymphocyte                               | UBERON:0006567 | right ventricle myocardium                       | myocardium                | [159](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=159:159) |
|  72 | CL:0000359 | vascular associated smooth muscle cell    | smooth muscle cell                         | UBERON:0002079 | left cardiac atrium                              | left atrium               | [84](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=84:84)    |
|  73 | CL:0000359 | vascular associated smooth muscle cell    | smooth muscle cell                         | UBERON:0002079 | left cardiac atrium                              | left atrium               | [81](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=81:81)    |
|  74 | CL:0000359 | vascular associated smooth muscle cell    | smooth muscle cell                         | UBERON:0002079 | left cardiac atrium                              | left atrium               | [78](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=78:78)    |
|  75 | CL:0000359 | vascular associated smooth muscle cell    | smooth muscle cell                         | UBERON:0005438 | coronary sinus                                   | coronary sinus            | [44](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=44:44)    |
|  76 | CL:0000359 | vascular associated smooth muscle cell    | smooth muscle cell                         | UBERON:0002079 | left cardiac atrium                              | left atrium               | [75](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=75:75)    |
|  77 | CL:0000359 | vascular associated smooth muscle cell    | smooth muscle cell                         | UBERON:0002348 | epicardium                                       | Epicardium                | [207](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=207:207) |
|  78 | CL:0000359 | vascular associated smooth muscle cell    | smooth muscle cell                         | UBERON:0002079 | left cardiac atrium                              | left atrium               | [72](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=72:72)    |
|  79 | CL:0000359 | vascular associated smooth muscle cell    | smooth muscle cell                         | UBERON:0002080 | heart right ventricle                            | right ventricle           | [191](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=191:191) |
|  80 | CL:0000542 | lymphocyte                                | lymphocyte                                 | UBERON:0002080 | heart right ventricle                            | right ventricle           | [183](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=183:183) |
|  81 | CL:0000542 | lymphocyte                                | lymphocyte                                 | UBERON:0002078 | right cardiac atrium                             | right atrium              | [34](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=34:34)    |
|  82 | CL:0000542 | lymphocyte                                | lymphocyte                                 | UBERON:0002080 | heart right ventricle                            | right ventricle           | [194](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=194:194) |
|  83 | CL:0000542 | lymphocyte                                | lymphocyte                                 | UBERON:0002079 | left cardiac atrium                              | left atrium               | [87](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=87:87)    |
|  84 | CL:0000542 | lymphocyte                                | lymphocyte                                 | UBERON:0002094 | interventricular septum                          | septum                    | [148](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=148:148) |
|  85 | CL:0000669 | pericyte                                  | pericyte                                   | UBERON:0001982 | capillary                                        | vasculature               | [68](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=68:68)    |
|  86 | CL:0000669 | pericyte                                  | pericyte                                   | UBERON:0002078 | right cardiac atrium                             | right atrium              | [29](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=29:29)    |
|  87 | CL:0000669 | pericyte                                  | pericyte                                   | UBERON:0001979 | venule                                           | vasculature               | [70](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=70:70)    |
|  88 | CL:0000669 | pericyte                                  | pericyte                                   | UBERON:0001979 | venule                                           | vasculature               | [141](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=141:141) |
|  89 | CL:0000669 | pericyte                                  | pericyte                                   | UBERON:0001979 | venule                                           | vasculature               | [181](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=181:181) |
|  90 | CL:0000669 | pericyte                                  | pericyte                                   | UBERON:0001979 | venule                                           | vasculature               | [99](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=99:99)    |
|  91 | CL:0000669 | pericyte                                  | pericyte                                   | UBERON:0001982 | capillary                                        | vasculature               | [179](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=179:179) |
|  92 | CL:0000669 | pericyte                                  | pericyte                                   | UBERON:0001982 | capillary                                        | vasculature               | [139](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=139:139) |
|  93 | CL:0000669 | pericyte                                  | pericyte                                   | UBERON:0001982 | capillary                                        | vasculature               | [98](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=98:98)    |
|  94 | CL:0000746 | cardiac muscle cell                       | cardiomyocyte                              | UBERON:0002079 | left cardiac atrium                              | left atrium               | [54](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=54:54)    |
|  95 | CL:0000746 | cardiac muscle cell                       | cardiomyocyte                              | UBERON:0002094 | interventricular septum                          | septum                    | [143](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=143:143) |
|  96 | CL:0000746 | cardiac muscle cell                       | cardiomyocyte                              | UBERON:0002080 | heart right ventricle                            | right ventricle           | [186](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=186:186) |
|  97 | CL:0000746 | cardiac muscle cell                       | cardiomyocyte                              | UBERON:0006567 | right ventricle myocardium                       | myocardium                | [163](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=163:163) |
|  98 | CL:0000746 | cardiac muscle cell                       | cardiomyocyte                              | UBERON:0003379 | cardiac muscle of right atrium                   | myocardium                | [16](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=16:16)    |
|  99 | CL:0000746 | cardiac muscle cell                       | cardiomyocyte                              | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [90](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=90:90)    |
| 100 | CL:0000914 | immature NK T cell                        | NK/T lymphocyte                            | UBERON:0002094 | interventricular septum                          | septum                    | [154](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=154:154) |
| 101 | CL:0000914 | immature NK T cell                        | NK/T lymphocyte                            | UBERON:0006567 | right ventricle myocardium                       | myocardium                | [160](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=160:160) |
| 102 | CL:0000914 | immature NK T cell                        | NK/T lymphocyte                            | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium                | [23](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=23:23)    |
| 103 | CL:0000914 | immature NK T cell                        | NK/T lymphocyte                            | UBERON:0002348 | epicardium                                       | Epicardium                | [214](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=214:214) |
| 104 | CL:0000914 | immature NK T cell                        | NK/T lymphocyte                            | UBERON:0002079 | left cardiac atrium                              | left atrium               | [62](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=62:62)    |
| 105 | CL:0000914 | immature NK T cell                        | NK/T lymphocyte                            | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [106](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=106:106) |
| 106 | CL:0001056 | dendritic cell, human                     | dendritic cell                             | UBERON:0002080 | heart right ventricle                            | right ventricle           | [184](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=184:184) |
| 107 | CL:0001056 | dendritic cell, human                     | dendritic cell                             | UBERON:0002080 | heart right ventricle                            | right ventricle           | [195](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=195:195) |
| 108 | CL:0001056 | dendritic cell, human                     | dendritic cell                             | UBERON:0002078 | right cardiac atrium                             | right atrium              | [35](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=35:35)    |
| 109 | CL:0001056 | dendritic cell, human                     | dendritic cell                             | UBERON:0002094 | interventricular septum                          | septum                    | [149](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=149:149) |
| 110 | CL:0001056 | dendritic cell, human                     | dendritic cell                             | UBERON:0002079 | left cardiac atrium                              | left atrium               | [88](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=88:88)    |
| 111 | CL:0001056 | dendritic cell, human                     | dendritic cell                             | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [101](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=101:101) |
| 112 | CL:0001065 | innate lymphoid cell                      | ILC                                        | UBERON:0006567 | right ventricle myocardium                       | myocardium                | [161](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=161:161) |
| 113 | CL:0001065 | innate lymphoid cell                      | ILC                                        | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [107](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=107:107) |
| 114 | CL:0001065 | innate lymphoid cell                      | ILC                                        | UBERON:0002094 | interventricular septum                          | septum                    | [155](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=155:155) |
| 115 | CL:0001065 | innate lymphoid cell                      | ILC                                        | UBERON:0002079 | left cardiac atrium                              | left atrium               | [63](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=63:63)    |
| 116 | CL:0001065 | Innate lymphoid cell                      | Innate lymphoid cell                       | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium                | [24](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=24:24)    |
| 117 | CL:0002068 | Purkinje myocyte                          | Purkinje fiber cell                        | UBERON:0006567 | right ventricle myocardium                       | myocardium                | [164](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=164:164) |
| 118 | CL:0002068 | Purkinje myocyte                          | Purkinje fiber cell                        | UBERON:0002080 | heart right ventricle                            | right ventricle           | [187](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=187:187) |
| 119 | CL:0002068 | Purkinje myocyte                          | Purkinje fiber cell                        | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [91](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=91:91)    |
| 120 | CL:0002068 | Purkinje myocyte                          | Purkinje fiber cell                        | UBERON:0002094 | interventricular septum                          | septum                    | [144](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=144:144) |
| 121 | CL:0002138 | endothelial cell of lymphatic vessel      | lymphatic endothelial cell                 | UBERON:0002094 | interventricular septum                          | septum                    | [152](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=152:152) |
| 122 | CL:0002138 | endothelial cell of lymphatic vessel      | lymphatic endothelial cell                 | UBERON:0002079 | left cardiac atrium                              | left atrium               | [60](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=60:60)    |
| 123 | CL:0002138 | endothelial cell of lymphatic vessel      | lymphatic endothelial cell                 | UBERON:0006567 | right ventricle myocardium                       | myocardium                | [158](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=158:158) |
| 124 | CL:0002138 | endothelial cell of lymphatic vessel      | lymphatic endothelial cell                 | UBERON:0002348 | epicardium                                       | Epicardium                | [212](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=212:212) |
| 125 | CL:0002138 | endothelial cell of lymphatic vessel      | lymphatic endothelial cell                 | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [104](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=104:104) |
| 126 | CL:0002138 | endothelial cell of lymphatic vessel      | lymphatic endothelial cell                 | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium                | [21](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=21:21)    |
| 127 | CL:0002350 | endocardial cell                          | endocardial                                | UBERON:0002134 | Tricuspid valve                                  | Tricuspid valve           | [197](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=197:197) |
| 128 | CL:0002350 | endocardial cell                          | endocardial                                | UBERON:0002146 | Pulmonary Valve                                  | Pulmonary Valve           | [199](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=199:199) |
| 129 | CL:0002350 | endocardial cell                          | endocardial                                | UBERON:0002135 | Mitral valve                                     | Mitral valve              | [201](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=201:201) |
| 130 | CL:0002350 | endocardial cell                          | endocardial cell                           | UBERON:0003383 | cardiac muscle tissue of interventricular septum | myocardium                | [25](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=25:25)    |
| 131 | CL:0002350 | endocardial cell                          | endocardial                                | UBERON:0002079 | left cardiac atrium                              | left atrium               | [64](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=64:64)    |
| 132 | CL:0002350 | endocardial cell                          | endocardial                                | UBERON:0002094 | interventricular septum                          | septum                    | [156](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=156:156) |
| 133 | CL:0002350 | endocardial cell                          | endocardial                                | UBERON:0006567 | right ventricle myocardium                       | myocardium                | [162](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=162:162) |
| 134 | CL:0002350 | endocardial cell                          | endocardial                                | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [108](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=108:108) |
| 135 | CL:0002573 | Schwann cell                              | Schwann Cell                               | UBERON:0002079 | left cardiac atrium                              | left atrium               | [58](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=58:58)    |
| 136 | CL:0002573 | Schwann cell                              | Schwann Cell                               | UBERON:0003379 | cardiac muscle of right atrium                   | myocardium                | [19](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=19:19)    |
| 137 | CL:0002573 | Schwann cell                              | Schwann Cell                               | UBERON:0002348 | epicardium                                       | Epicardium                | [206](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=206:206) |
| 138 | CL:0002592 | smooth muscle cell of the coronary artery | smooth muscle cell                         | UBERON:0035374 | small cardiac vein                               | small cardiac vein        | [52](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=52:52)    |
| 139 | CL:0002592 | smooth muscle cell of the coronary artery | smooth muscle cell                         | UBERON:0001625 | right coronary artery                            | right coronary artery     | [49](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=49:49)    |
| 140 | CL:0002592 | smooth muscle cell of the coronary artery | smooth muscle cell                         | UBERON:0011820 | atrioventricular region                          | atrioventricular junction | [41](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=41:41)    |
| 141 | CL:0002592 | smooth muscle cell of the coronary artery | smooth muscle cell                         | UBERON:0035422 | circumflex branch of left coronary artery        | left circumflex artery    | [38](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=38:38)    |
| 142 | CL:0002592 | smooth muscle cell of the coronary artery | smooth muscle cell                         | UBERON:0002078 | right cardiac atrium                             | right atrium              | [31](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=31:31)    |
| 143 | CL:0002592 | smooth muscle cell of the coronary artery | smooth muscle cell                         | UBERON:0002078 | right cardiac atrium                             | right atrium              | [14](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=14:14)    |
| 144 | CL:0010008 | cardiac endothelial cell                  | endothelial cell                           | UBERON:0002049 | vasculature                                      | vasculature               | [26](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=26:26)    |
| 145 | CL:0017004 | telocyte                                  | telocyte (interstitial like cell of cajal) | UBERON:0002078 | right cardiac atrium                             | right atrium              | [33](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=33:33)    |
| 146 | CL:0017004 | telocyte                                  | telocyte (interstitial like cell of cajal) | UBERON:0002094 | interventricular septum                          | septum                    | [147](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=147:147) |
| 147 | CL:0017004 | telocyte                                  | telocyte (interstitial like cell of cajal) | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [100](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=100:100) |
| 148 | CL:0017004 | telocyte                                  | telocyte (interstitial like cell of cajal) | UBERON:0002080 | heart right ventricle                            | right ventricle           | [182](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=182:182) |
| 149 | CL:0017004 | telocyte                                  | telocyte (interstitial like cell of cajal) | UBERON:0002080 | heart right ventricle                            | right ventricle           | [193](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=193:193) |
| 150 | CL:0017004 | telocyte                                  | telocyte (interstitial like cell of cajal) | UBERON:0002079 | left cardiac atrium                              | left atrium               | [86](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=86:86)    |
| 151 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002080 | heart right ventricle                            | right ventricle           | [173](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=173:173) |
| 152 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002078 | right cardiac atrium                             | right atrium              | [13](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=13:13)    |
| 153 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002080 | heart right ventricle                            | right ventricle           | [167](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=167:167) |
| 154 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002078 | right cardiac atrium                             | right atrium              | [30](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=30:30)    |
| 155 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0035422 | circumflex branch of left coronary artery        | left circumflex artery    | [37](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=37:37)    |
| 156 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0011820 | atrioventricular region                          | atrioventricular junction | [40](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=40:40)    |
| 157 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0005438 | coronary sinus                                   | coronary sinus            | [43](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=43:43)    |
| 158 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0001625 | right coronary artery                            | right coronary artery     | [48](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=48:48)    |
| 159 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0035374 | small cardiac vein                               | small cardiac vein        | [51](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=51:51)    |
| 160 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002080 | heart right ventricle                            | right ventricle           | [170](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=170:170) |
| 161 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002084 | heart left ventricle                             | left ventricle            | [109](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=109:109) |
| 162 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002084 | heart left ventricle                             | left ventricle            | [115](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=115:115) |
| 163 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002084 | heart left ventricle                             | left ventricle            | [112](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=112:112) |
| 164 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002084 | heart left ventricle                             | left ventricle            | [121](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=121:121) |
| 165 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0009687 | middle cardiac vein                              | middle cardiac vein       | [136](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=136:136) |
| 166 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0006958 | great vein of heart                              | great cardiac vein        | [133](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=133:133) |
| 167 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002094 | interventricular septum                          | septum                    | [124](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=124:124) |
| 168 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002094 | interventricular septum                          | septum                    | [130](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=130:130) |
| 169 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002094 | interventricular septum                          | septum                    | [127](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=127:127) |
| 170 | CL:1000413 | endothelial cell of artery                | endothelial cell                           | UBERON:0002084 | heart left ventricle                             | left ventricle            | [118](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=118:118) |
| 171 | CL:1000477 | cardiac pacemaker cell of sinoatrial node | pacemaker cardiomyocyte                    | UBERON:0002353 | bundle of His                                    | bundle of His             | [142](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=142:142) |
| 172 | CL:1000477 | cardiac pacemaker cell of sinoatrial node | pacemaker cell                             | UBERON:0002352 | atrioventricular node                            | atrioventricular node     | [46](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=46:46)    |
| 173 | CL:1000477 | cardiac pacemaker cell of sinoatrial node | pacemaker cell                             | UBERON:0002079 | left cardiac atrium                              | left atrium               | [55](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=55:55)    |
| 174 | CL:2000066 | cardiac ventricle fibroblast              | fibroblast                                 | UBERON:0006566 | left ventricle myocardium                        | myocardium                | [92](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=92:92)    |
| 175 | CL:2000066 | cardiac ventricle fibroblast              | fibroblast                                 | UBERON:0002049 | vasculature                                      | vasculature               | [96](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=96:96)    |
| 176 | CL:2000066 | cardiac ventricle fibroblast              | fibroblast                                 | UBERON:0006567 | right ventricle myocardium                       | myocardium                | [165](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=165:165) |
| 177 | CL:2000067 | cardiac atrium fibroblast                 | fibroblast                                 | UBERON:0002049 | vasculature                                      | vasculature               | [67](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=67:67)    |
| 178 | CL:2000067 | cardiac atrium fibroblast                 | fibroblast                                 | UBERON:0002079 | left cardiac atrium                              | left atrium               | [73](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=73:73)    |
| 179 | CL:2000067 | cardiac atrium fibroblast                 | fibroblast                                 | UBERON:0002079 | left cardiac atrium                              | left atrium               | [76](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=76:76)    |
| 180 | CL:2000067 | cardiac atrium fibroblast                 | fibroblast                                 | UBERON:0002079 | left cardiac atrium                              | left atrium               | [82](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=82:82)    |
| 181 | CL:2000067 | cardiac atrium fibroblast                 | fibroblast                                 | UBERON:0002079 | left cardiac atrium                              | left atrium               | [85](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=85:85)    |
| 182 | CL:2000067 | cardiac atrium fibroblast                 | fibroblast                                 | UBERON:0002049 | vasculature                                      | vasculature               | [28](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=28:28)    |
| 183 | CL:2000067 | cardiac atrium fibroblast                 | fibroblast                                 | UBERON:0003379 | cardiac muscle of right atrium                   | myocardium                | [17](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=17:17)    |
| 184 | CL:2000067 | cardiac atrium fibroblast                 | fibroblast                                 | UBERON:0002079 | left cardiac atrium                              | left atrium               | [56](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=56:56)    |
| 185 | CL:2000067 | cardiac atrium fibroblast                 | fibroblast                                 | UBERON:0002079 | left cardiac atrium                              | left atrium               | [79](https://docs.google.com/spreadsheets/d/107Mt6KUlHxQIv3nuly6Mv8XdmxBCmgA7xjv1PEcfrqk/edit#gid=1759721736&range=79:79)    |




# New CL terms
[**Report**](new_cl_terms_Heart.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Heart.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Heart_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Heart_AS_has_part_CT_log.tsv)