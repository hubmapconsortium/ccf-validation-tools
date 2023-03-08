
ASCT+B Validation Reports for Spleen (2023-03-08)
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
  
1. In row _[54](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=54:54)_, the term _[CL:0002394](http://purl.obolibrary.org/obo/CL_0002394)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _myeloid dendritic cell cDC1_ and the one in the ontology is _CD141-positive myeloid dendritic cell_. For reference, the given name/label by SMEs is _cDC1 myeloid dendritic cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[36](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=36:36)_, the term _[CL:0000037](http://purl.obolibrary.org/obo/CL_0000037)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _hematopoetic stem cell_ and the one in the ontology is _hematopoietic stem cell_. For reference, the given name/label by SMEs is _Hematopoetic Stem Cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[30](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=30:30)_, the term _[UBERON:0009967](http://purl.obolibrary.org/obo/UBERON_0009967)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _splenic sinusoid_ and the one in the ontology is _spleen venous sinus_. For reference, the given name/label by SMEs is _Splenic Sinusoid_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[55](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=55:55)_, the term _[CL:0002399](http://purl.obolibrary.org/obo/CL_0002399)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _myeloid dendritic cell cDC2_ and the one in the ontology is _CD1c-positive myeloid dendritic cell_. For reference, the given name/label by SMEs is _cDC2 myeloid dendritic cell_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


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

1. In row _[49](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=49:49)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[50](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=50:50)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[50](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=50:50)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=51:51)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=51:51)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=52:52)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=52:52)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=52:52)_, no term id was found for the name/label _Splenic perifollicular zone macrophage_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=53:53)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=53:53)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=53:53)_, no term id was found for the name/label _Sheathed Capillary_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=54:54)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=54:54)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[55](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=55:55)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[55](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=55:55)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[56](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=56:56)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[56](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=56:56)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[57](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=57:57)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[57](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=57:57)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=58:58)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=58:58)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[58](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=58:58)_, no term id was found for the name/label _DEC205+ DC_.

1. In row _[59](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=59:59)_, no term id was found for the name/label _Central arteries_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=60:60)_, no term id was found for the name/label _White Pulp Lymphatic Vessels_.

1. In row _[65](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=65:65)_, no term id was found for the name/label _DEC205+ DC_.

1. In row _[72](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=72:72)_, no term id was found for the name/label _Mantle Zone B Cell_.

1. In row _[76](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=76:76)_, no term id was found for the name/label _Splenic Pericyte_.

1. In row _[80](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=80:80)_, no term id was found for the name/label _Splenic Pericyte_.

1. In row _[92](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=92:92)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[92](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=92:92)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[93](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=93:93)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[93](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=93:93)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[94](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=94:94)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[94](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=94:94)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

1. In row _[95](https://docs.google.com/spreadsheets/d/1KugrRJwk_IlvOpCpDffvk9YKFbSFd4PtJgAzxgrAmtM/edit#gid=69626346&range=95:95)_, no term id was found for the name/label _Red Pulp-White Pulp Border_.

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

## Relationship AS-AS report
[**Report**](class_Spleen_log.tsv)
## Relationship CT-CT report
[**Report**](class_Spleen_log.tsv)
## Relationship CT-AS report
[**Report**](Spleen_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Spleen.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Spleen.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Spleen_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Spleen_AS_has_part_CT_log.tsv)