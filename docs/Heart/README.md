
ASCT+B Validation Reports for Heart (2023-01-25)
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
  
1. In row _[21](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=21:21)_, the term _[CL:0002138](http://purl.obolibrary.org/obo/CL_0002138)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _lymphatic endothelial cell_ and the one in the ontology is _endothelial cell of lymphatic vessel_. For reference, the given name/label by SMEs is _lymphatic endothelial cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[196](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=196:196)_, the term _[UBERON:0000946](http://purl.obolibrary.org/obo/UBERON_0000946)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Cardial valve_ and the one in the ontology is _cardiac valve_. For reference, the given name/label by SMEs is _Cardial valve_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[142](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=142:142)_, the term _[UBERON:0002353](http://purl.obolibrary.org/obo/UBERON_0002353)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _atrioventricular bundle_ and the one in the ontology is _bundle of His_. For reference, the given name/label by SMEs is _bundle of His_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[133](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=133:133)_, the term _[UBERON:0006958](http://purl.obolibrary.org/obo/UBERON_0006958)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _great cardiac vein_ and the one in the ontology is _great vein of heart_. For reference, the given name/label by SMEs is _great cardiac vein_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[29](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=29:29)_, no term id was found for the name/label _vasculature_.

1. In row _[130](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=130:130)_, no term id was found for the name/label _septal perforating arteries_.

1. In row _[131](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=131:131)_, no term id was found for the name/label _septal perforating arteries_.

1. In row _[132](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=132:132)_, no term id was found for the name/label _septal perforating arteries_.

1. In row _[196](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=196:196)_, no term id was found for the name/label _valve interstitial cell_.

1. In row _[198](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=198:198)_, no term id was found for the name/label _valve interstitial cell_.

1. In row _[200](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=200:200)_, no term id was found for the name/label _valve interstitial cell_.

1. In row _[202](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=202:202)_, no term id was found for the name/label _valve interstitial cell_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
1. In row _[13](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=13:13)_, the term _FMA:3823_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[14](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=14:14)_, the term _FMA:3823_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[15](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=15:15)_, the term _FMA:3823_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[30](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=30:30)_, the term _FMA:76767_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[31](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=31:31)_, the term _FMA:76767_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[32](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=32:32)_, the term _FMA:76767_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[33](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=33:33)_, the term _FMA:83531_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[34](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=34:34)_, the term _FMA:83531_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[35](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=35:35)_, the term _FMA:83531_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[36](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=36:36)_, the term _FMA:83531_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[40](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=40:40)_, the term _FMA:3851_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[41](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=41:41)_, the term _FMA:3851_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[42](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=42:42)_, the term _FMA:3851_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[54](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=54:54)_, the term _FMA:83532_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[55](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=55:55)_, the term _FMA:83532_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[56](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=56:56)_, the term _FMA:83532_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[57](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=57:57)_, the term _FMA:83532_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[58](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=58:58)_, the term _FMA:83532_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[59](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=59:59)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[60](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=60:60)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[61](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=61:61)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[62](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=62:62)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[63](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=63:63)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[64](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=64:64)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[71](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=71:71)_, the term _FMA:49913_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[72](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=72:72)_, the term _FMA:49913_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[73](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=73:73)_, the term _FMA:49913_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[74](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=74:74)_, the term _FMA:49916_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[75](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=75:75)_, the term _FMA:49916_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[76](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=76:76)_, the term _FMA:49916_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[77](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=77:77)_, the term _FMA:49911_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[78](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=78:78)_, the term _FMA:49911_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[79](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=79:79)_, the term _FMA:49911_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[80](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=80:80)_, the term _FMA:49914_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[81](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=81:81)_, the term _FMA:49914_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[82](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=82:82)_, the term _FMA:49914_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[83](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=83:83)_, the term _FMA:4715_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[84](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=84:84)_, the term _FMA:4715_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[85](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=85:85)_, the term _FMA:4715_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[86](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=86:86)_, the term _FMA:83532_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[87](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=87:87)_, the term _FMA:83532_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[88](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=88:88)_, the term _FMA:83532_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[89](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=89:89)_, the term _FMA:83532_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[109](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=109:109)_, the term _FMA:3860_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[110](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=110:110)_, the term _FMA:3860_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[111](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=111:111)_, the term _FMA:3860_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[112](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=112:112)_, the term _FMA:3902_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[113](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=113:113)_, the term _FMA:3902_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[114](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=114:114)_, the term _FMA:3902_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[115](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=115:115)_, the term _FMA:3835_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[116](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=116:116)_, the term _FMA:3835_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[117](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=117:117)_, the term _FMA:3835_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[118](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=118:118)_, the term _FMA:4708_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[119](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=119:119)_, the term _FMA:4708_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[120](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=120:120)_, the term _FMA:4708_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[121](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=121:121)_, the term _FMA:4712_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[122](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=122:122)_, the term _FMA:4712_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[123](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=123:123)_, the term _FMA:4712_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[124](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=124:124)_, the term _FMA:3862_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[125](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=125:125)_, the term _FMA:3862_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[126](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=126:126)_, the term _FMA:3862_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[127](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=127:127)_, the term _FMA:3840_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[128](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=128:128)_, the term _FMA:3840_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[129](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=129:129)_, the term _FMA:3840_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[143](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=143:143)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[144](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=144:144)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[145](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=145:145)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[146](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=146:146)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[147](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=147:147)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[148](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=148:148)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[149](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=149:149)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[150](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=150:150)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[151](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=151:151)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[152](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=152:152)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[153](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=153:153)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[154](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=154:154)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[155](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=155:155)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[156](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=156:156)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[167](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=167:167)_, the term _FMA:15736_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[168](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=168:168)_, the term _FMA:15736_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[169](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=169:169)_, the term _FMA:15736_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[170](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=170:170)_, the term _FMA:3818_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[171](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=171:171)_, the term _FMA:3818_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[172](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=172:172)_, the term _FMA:3818_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[173](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=173:173)_, the term _FMA:76767_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[174](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=174:174)_, the term _FMA:76767_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[175](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=175:175)_, the term _FMA:76767_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[182](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=182:182)_, the term _FMA:9535_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[183](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=183:183)_, the term _FMA:9535_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[184](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=184:184)_, the term _FMA:9535_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[185](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=185:185)_, the term _FMA:9535_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[186](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=186:186)_, the term _FMA:7272_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[187](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=187:187)_, the term _FMA:7272_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[188](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=188:188)_, the term _FMA:7272_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[189](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=189:189)_, the term _FMA:7272_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[190](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=190:190)_, the term _FMA:7272_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[191](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=191:191)_, the term _FMA:7272_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[192](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=192:192)_, the term _FMA:7272_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[193](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=193:193)_, the term _FMA:7272_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[194](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=194:194)_, the term _FMA:7272_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[195](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=195:195)_, the term _FMA:7272_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[211](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=211:211)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[212](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=212:212)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[213](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=213:213)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.

1. In row _[214](https://docs.google.com/spreadsheets/d/1eSzDzv_wOpMGTrSShmy_S7IXs8_H_Kp3QZg-gfKyUWk/edit#gid=1759721736&range=214:214)_, the term _FMA:83539_ is from another ontology that is not validated in this process. The term id should have this pattern: FMA:NNNNN or LMHA:NNNNN. The ontology name in upper case. N is a number and it should have exact 5 number after the colon.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Heart_log.tsv)
## Relationship CT-CT report
[**Report**](class_Heart_log.tsv)
## Relationship CT-AS report
[**Report**](Heart_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Heart.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Heart.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Heart_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Heart_AS_has_part_CT_log.tsv)