
ASCT+B Validation Reports for Spleen (2023-06-05)
=================================================

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
  
1. In row _[36](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=36:36)_, the term _[CL:0000037](http://purl.obolibrary.org/obo/CL_0000037)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _hematopoetic stem cell_ and the one in the **ontology** is _hematopoietic stem cell_. For reference, the given name/label **by SMEs** is _Hematopoetic Stem Cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[55](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=55:55)_, the term _[CL:0002399](http://purl.obolibrary.org/obo/CL_0002399)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _myeloid dendritic cell cDC2_ and the one in the **ontology** is _CD1c-positive myeloid dendritic cell_. For reference, the given name/label **by SMEs** is _cDC2 myeloid dendritic cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[54](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=54:54)_, the term _[CL:0002394](http://purl.obolibrary.org/obo/CL_0002394)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _myeloid dendritic cell cDC1_ and the one in the **ontology** is _CD141-positive myeloid dendritic cell_. For reference, the given name/label **by SMEs** is _cDC1 myeloid dendritic cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[30](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=30:30)_, the term _[UBERON:0009967](http://purl.obolibrary.org/obo/UBERON_0009967)_ has different name/label in the source ontology. The name/label in the **ASCT+B table** is _splenic sinusoid_ and the one in the **ontology** is _spleen venous sinus_. For reference, the given name/label **by SMEs** is _Splenic Sinusoid_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[13](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=13:13)_, no term id was found for the name/label _Catecholaminergic Neuron_.

1. In row _[14](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=14:14)_, no term id was found for the name/label _Catecholaminergic Neuron_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=19:19)_, no term id was found for the name/label _Adventitial Stromal Cell_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=22:22)_, no term id was found for the name/label _Arterial Capillary_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=23:23)_, no term id was found for the name/label _Sheathed Capillary_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=24:24)_, no term id was found for the name/label _Sheathed Capillary_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=25:25)_, no term id was found for the name/label _Sheathed Capillary_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=25:25)_, no term id was found for the name/label _Splenic Stromal Sheath Cell_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=26:26)_, no term id was found for the name/label _Sheathed Capillary_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=27:27)_, no term id was found for the name/label _Sheathed Capillary_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=28:28)_, no term id was found for the name/label _Sheathed Capillary_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=29:29)_, no term id was found for the name/label _Sheathed Capillary_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=30:30)_, no term id was found for the name/label _Ring Fiber_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=30:30)_, no term id was found for the name/label _Reticular Cell of splenic sinusoid_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=31:31)_, no term id was found for the name/label _Splenic Littoral Cell_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=32:32)_, no term id was found for the name/label _Splenic Red Pulp Stroma_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=32:32)_, no term id was found for the name/label _Splenic Red Pulp Stromal Cell_.

1. In row _[34](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=34:34)_, no term id was found for the name/label _Splenic venules_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=39:39)_, no term id was found for the name/label _B cell_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=49:49)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[50](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=50:50)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=51:51)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=52:52)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=52:52)_, no term id was found for the name/label _Splenic perifollicular zone macrophage_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=53:53)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=53:53)_, no term id was found for the name/label _Sheathed Capillary_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=54:54)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[55](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=55:55)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[56](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=56:56)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[57](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=57:57)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=58:58)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=58:58)_, no term id was found for the name/label _DEC205+ DC_.

1. In row _[59](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=59:59)_, no term id was found for the name/label _Central arteries_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=60:60)_, no term id was found for the name/label _White Pulp Lymphatic Vessels_.

1. In row _[65](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=65:65)_, no term id was found for the name/label _DEC205+ DC_.

1. In row _[72](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=72:72)_, no term id was found for the name/label _Mantle Zone B Cell_.

1. In row _[76](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=76:76)_, no term id was found for the name/label _Splenic Pericyte_.

1. In row _[80](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=80:80)_, no term id was found for the name/label _Splenic Pericyte_.

1. In row _[92](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=92:92)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[93](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=93:93)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[94](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=94:94)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[95](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=95:95)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[96](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=96:96)_, no term id was found for the name/label _Inner PALS_.

1. In row _[97](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=97:97)_, no term id was found for the name/label _Inner PALS_.

1. In row _[97](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=97:97)_, no term id was found for the name/label _Adventitial Stromal Cell_.

1. In row _[98](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=98:98)_, no term id was found for the name/label _Inner PALS_.

1. In row _[98](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=98:98)_, no term id was found for the name/label _Catecholaminergic Neuron_.

1. In row _[99](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=99:99)_, no term id was found for the name/label _Inner PALS_.

1. In row _[100](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=100:100)_, no term id was found for the name/label _Inner PALS_.

1. In row _[101](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=101:101)_, no term id was found for the name/label _Inner PALS_.

1. In row _[102](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=102:102)_, no term id was found for the name/label _Inner PALS_.

1. In row _[103](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=103:103)_, no term id was found for the name/label _Inner PALS_.

1. In row _[104](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=104:104)_, no term id was found for the name/label _Inner PALS_.

1. In row _[105](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=105:105)_, no term id was found for the name/label _Inner PALS_.

1. In row _[106](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=106:106)_, no term id was found for the name/label _Inner PALS_.

1. In row _[106](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=106:106)_, no term id was found for the name/label _Interdigitating Dendritic Cells_.

1. In row _[107](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=107:107)_, no term id was found for the name/label _Inner PALS_.

1. In row _[108](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=108:108)_, no term id was found for the name/label _Inner PALS_.

1. In row _[108](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=108:108)_, no term id was found for the name/label _Catecholaminergic Neuron_.

1. In row _[109](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=109:109)_, no term id was found for the name/label _Inner PALS_.

1. In row _[110](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=110:110)_, no term id was found for the name/label _Inner PALS_.

1. In row _[110](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=110:110)_, no term id was found for the name/label _Splenic Smooth Muscle Cell_.

1. In row _[111](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=111:111)_, no term id was found for the name/label _Outer PALS_.

1. In row _[112](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=112:112)_, no term id was found for the name/label _Outer PALS_.

1. In row _[113](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=113:113)_, no term id was found for the name/label _Outer PALS_.

1. In row _[114](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=114:114)_, no term id was found for the name/label _Outer PALS_.

1. In row _[115](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=115:115)_, no term id was found for the name/label _Outer PALS_.

1. In row _[116](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=116:116)_, no term id was found for the name/label _Outer PALS_.

1. In row _[117](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=117:117)_, no term id was found for the name/label _Outer PALS_.

1. In row _[118](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=118:118)_, no term id was found for the name/label _Outer PALS_.

1. In row _[119](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=119:119)_, no term id was found for the name/label _Cytotoxic Memory T Cell_.

1. In row _[127](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=127:127)_, no term id was found for the name/label _DEC205+ DC_.

1. In row _[134](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=134:134)_, no term id was found for the name/label _Catecholaminergic Neuron_.

1. In row _[136](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=136:136)_, no term id was found for the name/label _Connective tissue_.

1. In row _[137](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=137:137)_, no term id was found for the name/label _Subcapsule_.

1. In row _[137](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=137:137)_, no term id was found for the name/label _Subcapsular Dendritic Cell_.

1. In row _[141](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=141:141)_, no term id was found for the name/label _Catecholaminergic Neuron_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
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



|     | s              | slabel                   | user_slabel        | o              | olabel                   | user_olabel              | row_number                                                                                                                 |   deltaIC |
|-----|----------------|--------------------------|--------------------|----------------|--------------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------|
|   7 | UBERON:0001473 | lymphatic vessel         | Lymphatic Vessels  | UBERON:0001248 | hilum of spleen          | Hilum                    | [135](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=135:135) |  34.1545  |
|  10 | UBERON:0001473 | lymphatic vessel         | Lymphatic Vessels  | UBERON:0004641 | spleen capsule           | Capsule                  | [138](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=138:138) |  31.4687  |
|  19 | UBERON:0001473 | lymphatic vessel         | Lymphatic Vessels  | UBERON:0001265 | trabecula of spleen      | Trabeculae               | [142](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=142:142) |  22.2859  |
|  47 | UBERON:0001194 | splenic artery           | Splenic Artery     | UBERON:0001248 | hilum of spleen          | Hilum                    | [132](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=132:132) |  10.6609  |
|  49 | UBERON:0001265 | trabecula of spleen      | Trabeculae         | UBERON:0004641 | spleen capsule           | Capsule                  | [140](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=140:140) |   9.18281 |
|  50 | UBERON:0001265 | trabecula of spleen      | Trabeculae         | UBERON:0004641 | spleen capsule           | Capsule                  | [141](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=141:141) |   9.18281 |
|  51 | UBERON:0001265 | trabecula of spleen      | Trabeculae         | UBERON:0004641 | spleen capsule           | Capsule                  | [142](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=142:142) |   9.18281 |
|  52 | UBERON:0001265 | trabecula of spleen      | Trabeculae         | UBERON:0004641 | spleen capsule           | Capsule                  | [139](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=139:139) |   9.18281 |
|  54 | UBERON:0001265 | trabecula of spleen      | Trabeculae         | UBERON:0004641 | spleen capsule           | Capsule                  | [143](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=143:143) |   9.18281 |
|  59 | UBERON:0003713 | splenic vein             | Splenic Vein       | UBERON:0001248 | hilum of spleen          | Hilum                    | [133](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=133:133) |   8.2983  |
|  64 | UBERON:0012373 | Sympathetic nerve plexus | Sympathetic nerves | UBERON:0001248 | hilum of spleen          | Hilum                    | [134](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=134:134) |   4.5914  |
|  73 | UBERON:0001194 | Splenic Artery           | Splenic Artery     | UBERON:1000023 | spleen pulp              | Splenic Pulp             | [12](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=12:12)    | nan       |
|  75 | UBERON:0001194 | Splenic Artery           | Splenic Artery     | UBERON:1000023 | spleen pulp              | Splenic Pulp             | [13](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=13:13)    | nan       |
|  76 | UBERON:0012373 | Sympathetic nerve plexus | Sympathetic nerves | UBERON:0001194 | Splenic Artery           | Splenic Artery           | [13](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=13:13)    | nan       |
|  77 | UBERON:0012373 | Sympathetic nerve plexus | Sympathetic nerves | UBERON:0010401 | Spleen central arteriole | Spleen central arteriole | [14](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=14:14)    | nan       |
|  78 | UBERON:0003713 | splenic vein             | Splenic Vein       | UBERON:0001250 | red pulp of spleen       | Red Pulp                 | [33](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=33:33)    | nan       |
| 113 | UBERON:0012373 | Sympathetic nerve plexus | Sympathetic nerves | UBERON:0001265 | trabecula of spleen      | Trabeculae               | [141](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=141:141) | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|     | s          | slabel                                               | user_slabel                            | o              | olabel                        | user_olabel                           | row_number                                                                                                                 |
|-----|------------|------------------------------------------------------|----------------------------------------|----------------|-------------------------------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
|   0 | CL:0000037 | hematopoietic stem cell                              | Hematopoetic Stem Cell                 | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [36](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=36:36)    |
|   1 | CL:0000186 | myofibroblast cell                                   | Myofibroblast                          | UBERON:0001265 | trabecula of spleen           | Trabeculae                            | [143](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=143:143) |
|   2 | CL:0000186 | myofibroblast cell                                   | Myofibroblast                          | UBERON:0004641 | spleen capsule                | Capsule                               | [136](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=136:136) |
|   3 | CL:0000186 | myofibroblast cell                                   | Myofibroblasts                         | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [122](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=122:122) |
|   4 | CL:0000192 | smooth muscle cell                                   | Splenic Smooth Muscle Cell             | UBERON:0013132 | Penicillar Arteriole          | Penicillar Arteriole                  | [21](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=21:21)    |
|   5 | CL:0000232 | erythrocyte                                          | Erythrocytes                           | UBERON:0005353 | spleen perifollicular zone    | Perifollicular Zone                   | [49](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=49:49)    |
|   6 | CL:0000232 | erythrocyte                                          | Erythrocytes                           | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [38](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=38:38)    |
|   7 | CL:0000233 | platelet                                             | Platelet                               | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [45](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=45:45)    |
|   8 | CL:0000442 | follicular dendritic cell                            | Follicular Dendritic Cell (FDC)        | UBERON:0005196 | spleen germinal center        | Germinal Center                       | [66](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=66:66)    |
|   9 | CL:0000442 | follicular dendritic cell                            | Follicular Dendritic Cell (FDC)        | UBERON:0010421 | spleen B cell corona          | Mantle Zone                           | [74](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=74:74)    |
|  10 | CL:0000442 | follicular dendritic cell                            | Follicular Dendritic Cell (FDC)        | UBERON:0010421 | spleen B cell corona          | Mantle Zone                           | [79](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=79:79)    |
|  11 | CL:0000442 | follicular dendritic cell                            | Follicular Dendritic Cell (FDC)        | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [86](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=86:86)    |
|  12 | CL:0000442 | follicular dendritic cell                            | Follicular Dendritic Cell (FDC)        | UBERON:0004041 | spleen primary B follicle     | Primary Follicle                      | [61](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=61:61)    |
|  13 | CL:0000492 | CD4-positive helper T cell                           | CD4+ T cell                            | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [90](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=90:90)    |
|  14 | CL:0000492 | CD4-positive helper T cell                           | CD4+ T Cell                            | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [100](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=100:100) |
|  15 | CL:0000492 | CD4-positive helper T cell                           | CD4+ T Cell                            | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [112](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=112:112) |
|  16 | CL:0000499 | stromal cell                                         | Splenic Stromal Cell (non-FRC/non-FDC) | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [88](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=88:88)    |
|  17 | CL:0000499 | stromal cell                                         | Stromal Cell                           | UBERON:0005353 | spleen perifollicular zone    | Perifollicular Zone                   | [53](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=53:53)    |
|  18 | CL:0000499 | stromal cell                                         | Splenic Stromal Cell (non-FRC/non-FDC) | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [124](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=124:124) |
|  19 | CL:0000499 | stromal cell                                         | Splenic Stromal Cell (non-FRC/non-FDC) | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [47](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=47:47)    |
|  20 | CL:0000499 | stromal cell                                         | Splenic Stromal Cell (non-FRC/non-FDC) | UBERON:0013132 | Penicillar Arteriole          | Penicillar Arteriole                  | [20](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=20:20)    |
|  21 | CL:0000623 | natural killer cell                                  | NK Cell                                | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [130](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=130:130) |
|  22 | CL:0000623 | natural killer cell                                  | NK Cell                                | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [46](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=46:46)    |
|  23 | CL:0000625 | CD8-positive, alpha-beta T cell                      | CD8+ T Cell                            | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [40](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=40:40)    |
|  24 | CL:0000669 | pericyte                                             | Splenic Pericyte                       | UBERON:0001250 | red pulp of spleen            | Red Pulp                              | [24](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=24:24)    |
|  25 | CL:0000775 | neutrophil                                           | Neutrophil                             | UBERON:0005353 | spleen perifollicular zone    | Perifollicular Zone                   | [51](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=51:51)    |
|  26 | CL:0000775 | neutrophil                                           | Neutrophil                             | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [93](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=93:93)    |
|  27 | CL:0000786 | plasma cell                                          | Plasma Cell                            | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [42](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=42:42)    |
|  28 | CL:0000786 | plasma cell                                          | Plasma Cell                            | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [91](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=91:91)    |
|  29 | CL:0000787 | memory B cell                                        | Memory-Like B Cell                     | UBERON:0013132 | Penicillar Arteriole          | Penicillar Arteriole                  | [17](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=17:17)    |
|  30 | CL:0000787 | memory B cell                                        | Memory B Cell                          | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [83](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=83:83)    |
|  31 | CL:0000787 | memory B cell                                        | Memory B Cell                          | UBERON:0004041 | spleen primary B follicle     | Primary Follicle                      | [63](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=63:63)    |
|  32 | CL:0000787 | memory B cell                                        | Memory-Like B Cell                     | UBERON:0001250 | red pulp of spleen            | Red Pulp                              | [28](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=28:28)    |
|  33 | CL:0000787 | memory B cell                                        | Memory B Cell                          | UBERON:0010421 | spleen B cell corona          | Mantle Zone                           | [78](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=78:78)    |
|  34 | CL:0000788 | naive B cell                                         | Naive B Cell                           | UBERON:0004041 | spleen primary B follicle     | Primary Follicle                      | [62](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=62:62)    |
|  35 | CL:0000788 | naive B cell                                         | Naive B Cell                           | UBERON:0010421 | spleen B cell corona          | Mantle Zone                           | [77](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=77:77)    |
|  36 | CL:0000788 | naive B Cell                                         | Naive B Cell                           | UBERON:0001250 | red pulp of spleen            | Red Pulp                              | [27](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=27:27)    |
|  37 | CL:0000788 | naive B Cell                                         | Naive B Cell                           | UBERON:0013132 | Penicillar Arteriole          | Penicillar Arteriole                  | [16](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=16:16)    |
|  38 | CL:0000794 | CD8-positive, alpha-beta cytotoxic T cell            | Cytotoxic T Cells                      | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [103](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=103:103) |
|  39 | CL:0000794 | CD8-positive, alpha-beta cytotoxic T cell            | Cytotoxic T Cells                      | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [115](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=115:115) |
|  40 | CL:0000798 | gamma-delta T cell                                   | Gamma/Delta T cells                    | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [131](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=131:131) |
|  41 | CL:0000815 | regulatory T cell                                    | T Regulatory Cell                      | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [104](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=104:104) |
|  42 | CL:0000815 | regulatory T cell                                    | T Regulatory Cell                      | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [116](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=116:116) |
|  43 | CL:0000818 | transitional stage B cell                            | Transitional Immature B Cells          | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [118](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=118:118) |
|  44 | CL:0000818 | transitional stage B cell                            | Transitional Immature B Cells          | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [85](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=85:85)    |
|  45 | CL:0000818 | transitional stage B cell                            | Transitional Immature B Cells          | UBERON:0010421 | spleen B cell corona          | Mantle Zone                           | [73](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=73:73)    |
|  46 | CL:0000844 | germinal center B cell                               | Germinal Center B Cell                 | UBERON:0005196 | spleen germinal center        | Germinal Center                       | [67](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=67:67)    |
|  47 | CL:0000874 | splenic red pulp macrophage                          | Red Pulp Macrophage                    | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [35](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=35:35)    |
|  48 | CL:0000876 | splenic white pulp macrophage                        | Macrophages                            | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [107](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=107:107) |
|  49 | CL:0000876 | splenic white pulp macrophage                        | Macrophage                             | UBERON:0004041 | spleen primary B follicle     | Primary Follicle                      | [64](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=64:64)    |
|  50 | CL:0000877 | splenic tingible body macrophage                     | Tingible Body Macrophage               | UBERON:0005196 | spleen germinal center        | Germinal Center                       | [70](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=70:70)    |
|  51 | CL:0000895 | naive thymus-derived CD4-positive, alpha-beta T cell | Naive CD4+ T Cell                      | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [99](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=99:99)    |
|  52 | CL:0000895 | naive thymus-derived CD4-positive, alpha-beta T cell | Naive CD4+ T Cell                      | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [111](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=111:111) |
|  53 | CL:0000897 | CD4-positive, alpha-beta memory T cell               | CD4+ Memory T Cell                     | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [121](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=121:121) |
|  54 | CL:0000900 | naive thymus-derived CD8-positive, alpha-beta T cell | Naive CD8+ T Cell                      | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [113](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=113:113) |
|  55 | CL:0000900 | naive thymus-derived CD8-positive, alpha-beta T cell | Naive CD8+ T Cell                      | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [101](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=101:101) |
|  56 | CL:0000909 | CD8-positive, alpha-beta memory T cell               | Non-Cytotoxic CD8+ Memory T Cell       | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [120](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=120:120) |
|  57 | CL:0000909 | CD8-positive, alpha-beta memory T cell               | Memory CD8+ T Cell                     | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [41](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=41:41)    |
|  58 | CL:0000972 | class switched memory B cell                         | Switched B Cell                        | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [82](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=82:82)    |
|  59 | CL:0000972 | class switched memory B cell                         | Switched B Cell                        | UBERON:0013132 | Penicillar Arteriole          | Penicillar Arteriole                  | [18](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=18:18)    |
|  60 | CL:0000972 | class switched memory B cell                         | Switched B Cell                        | UBERON:0001250 | red pulp of spleen            | Red Pulp                              | [29](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=29:29)    |
|  61 | CL:0000980 | plasmablast                                          | Plasmablast                            | UBERON:0005196 | spleen germinal center        | Germinal Center                       | [71](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=71:71)    |
|  62 | CL:0000980 | plasmablast                                          | Plasmablast                            | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [129](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=129:129) |
|  63 | CL:0000980 | plasmablast                                          | Plasmablast                            | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [43](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=43:43)    |
|  64 | CL:0001050 | effector CD8-positive, alpha-beta T cell             | CD8+ T Cell                            | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [102](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=102:102) |
|  65 | CL:0001050 | effector CD8-positive, alpha-beta T cell             | CD8+ T Cell                            | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [114](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=114:114) |
|  66 | CL:0001055 | CD14-positive, CD16-low monocyte                     | Monocytes                              | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [37](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=37:37)    |
|  67 | CL:0001055 | CD14-positive, CD16-low monocyte                     | Monocytes                              | UBERON:0005353 | spleen perifollicular zone    | Perifollicular Zone                   | [50](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=50:50)    |
|  68 | CL:0001056 | dendritic cell, human                                | Dendritic Cell                         | UBERON:0001266 | splenic cord                  | Splenic Cord                          | [44](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=44:44)    |
|  69 | CL:0001058 | plasmacytoid dendritic cell, human                   | Plasmacytoid Dendritic Cell            | UBERON:0005353 | spleen perifollicular zone    | Perifollicular Zone                   | [57](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=57:57)    |
|  70 | CL:0001058 | plasmacytoid dendritic cell, human                   | Plasmacytoid Dendritic Cell            | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [123](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=123:123) |
|  71 | CL:0001058 | plasmacytoid dendritic cell, human                   | Plasmacytoid Dendritic Cell            | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [89](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=89:89)    |
|  72 | CL:0001078 | group 3 innate lymphoid cell, human                  | Innate Lymphoid Cell (Type 3)          | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [92](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=92:92)    |
|  73 | CL:0002038 | T follicular helper cell                             | T Follicular Helper Cell               | UBERON:0005196 | spleen germinal center        | Germinal Center                       | [68](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=68:68)    |
|  74 | CL:0002138 | endothelial cell of lymphatic vessel                 | Lymphatic Endothelium Cell             | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [109](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=109:109) |
|  75 | CL:0002138 | endothelial cell of lymphatic vessel                 | Lymphatic Endothelium Cell             | UBERON:0001959 | white pulp of spleen          | White Pulp                            | [60](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=60:60)    |
|  76 | CL:0002394 | CD141-positive myeloid dendritic cell                | cDC1 myeloid dendritic cell            | UBERON:0005353 | spleen perifollicular zone    | Perifollicular Zone                   | [54](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=54:54)    |
|  77 | CL:0002394 | CD141-positive myeloid dendritic cell                | cDC1 myeloid dendritic cell            | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [125](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=125:125) |
|  78 | CL:0002399 | CD1c-positive myeloid dendritic cell                 | cDC2 myeloid dendritic cell            | UBERON:0005353 | spleen perifollicular zone    | Perifollicular Zone                   | [55](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=55:55)    |
|  79 | CL:0002399 | CD1c-positive myeloid dendritic cell                 | cDC2 myeloid dendritic cell            | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [126](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=126:126) |
|  80 | CL:0002543 | vein endothelial cell                                | Blood Endothelial Cells                | UBERON:0003713 | splenic vein                  | Splenic Vein                          | [133](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=133:133) |
|  81 | CL:0009113 | T follicular regulatory cell                         | T Follicular Regulatory Cell           | UBERON:0005196 | spleen germinal center        | Germinal Center                       | [69](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=69:69)    |
|  82 | CL:0011031 | monocyte-derived dendritic cell                      | Monocyte-Derived DC                    | UBERON:0005353 | spleen perifollicular zone    | Perifollicular Zone                   | [56](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=56:56)    |
|  83 | CL:0011031 | monocyte-derived dendritic cell                      | Monocyte-Derived DC                    | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [128](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=128:128) |
|  84 | CL:1000413 | endothelial cell of artery                           | Blood Endothelial Cells                | UBERON:0001194 | splenic artery                | Splenic Artery                        | [132](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=132:132) |
|  85 | CL:1000489 | reticular cell of splenic cord                       | Fibroblastic Reticular Cell (FRC)      | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [95](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=95:95)    |
|  86 | CL:1000489 | reticular cell of splenic cord                       | Fibroblastic Reticular Cell (FRC)      | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [117](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=117:117) |
|  87 | CL:1000489 | reticular cell of splenic cord                       | Fibroblastic Reticular Cell (FRC)      | UBERON:0001960 | periarterial lymphatic sheath | Periarteriolar Lymphoid Sheath (PALS) | [105](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=105:105) |
|  88 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0010399 | Spleen Trabecular Artery      | Spleen Trabecular Artery              | [139](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=139:139) |
|  89 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0013132 | Penicillar Arteriole          | Penicillar Arteriole                  | [15](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=15:15)    |
|  90 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0001959 | white pulp of spleen          | White Pulp                            | [59](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=59:59)    |
|  91 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0001250 | red pulp of spleen            | Red Pulp                              | [22](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=22:22)    |
|  92 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0010400 | Spleen Trabecular Vein        | Spleen Trabecular Vein                | [140](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=140:140) |
|  93 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0010421 | spleen B cell corona          | Mantle Zone                           | [81](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=81:81)    |
|  94 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0001250 | red pulp of spleen            | Red Pulp                              | [34](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=34:34)    |
|  95 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0003713 | splenic vein                  | Splenic Vein                          | [33](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=33:33)    |
|  96 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0001251 | Marginal Zone of Spleen       | Superficial Zone                      | [94](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=94:94)    |
|  97 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0010401 | spleen central arteriole      | Periarteriolar Lymphoid Sheath (PALS) | [96](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=96:96)    |
|  98 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0001250 | red pulp of spleen            | Red Pulp                              | [23](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=23:23)    |
|  99 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0010421 | spleen B cell corona          | Mantle Zone                           | [75](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=75:75)    |
| 100 | CL:2000053 | splenic endothelial cell                             | Splenic endothelial cell               | UBERON:0001194 | Splenic Artery                | Splenic Artery                        | [12](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=12:12)    |




# New CL terms
[**Report**](new_cl_terms_Spleen.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Spleen.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Spleen_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Spleen_AS_has_part_CT_log.tsv)