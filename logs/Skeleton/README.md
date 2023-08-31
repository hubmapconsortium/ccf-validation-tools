
ASCT+B Validation Reports for Skeleton (2023-08-31)
===================================================

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
  
- No issues found.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[15](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=15:15)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[16](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=16:16)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=17:17)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=17:17)_, no term id was found for the name/label _anatomical neck of humerus_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=18:18)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=19:19)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=19:19)_, no term id was found for the name/label _coronoid fossa of humerus_.

1. In row _[20](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=20:20)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[20](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=20:20)_, no term id was found for the name/label _deltoid tuberosity of humerus_.

1. In row _[21](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=21:21)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[21](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=21:21)_, no term id was found for the name/label _greater tubercle of humerus_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=22:22)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=22:22)_, no term id was found for the name/label _head of humerus_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=23:23)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=23:23)_, no term id was found for the name/label _intertubercular sulcus of humerus_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=24:24)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=24:24)_, no term id was found for the name/label _lateral epicondyle of humerus_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=25:25)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=25:25)_, no term id was found for the name/label _lateral supracondylar ridge of humerus_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=26:26)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=27:27)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=27:27)_, no term id was found for the name/label _medial epicondyle of humerus_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=28:28)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=28:28)_, no term id was found for the name/label _medial supracondylar ridge of humerus_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=29:29)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=29:29)_, no term id was found for the name/label _olecranon fossa of humerus_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=30:30)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=30:30)_, no term id was found for the name/label _radial fossa of humerus_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=31:31)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=31:31)_, no term id was found for the name/label _radial groove of humerus_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=32:32)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=32:32)_, no term id was found for the name/label _shaft of humerus_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=33:33)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=33:33)_, no term id was found for the name/label _surgical neck of humerus_.

1. In row _[34](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=34:34)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[35](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=35:35)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=36:36)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=36:36)_, no term id was found for the name/label _head of radius of radius_.

1. In row _[37](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=37:37)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[37](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=37:37)_, no term id was found for the name/label _interosseous border of radius_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=38:38)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=38:38)_, no term id was found for the name/label _neck of radius of radius_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=39:39)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=39:39)_, no term id was found for the name/label _radial tuberosity of radius_.

1. In row _[40](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=40:40)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[40](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=40:40)_, no term id was found for the name/label _shaft of radius of radius_.

1. In row _[41](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=41:41)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[41](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=41:41)_, no term id was found for the name/label _styloid process of radius_.

1. In row _[42](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=42:42)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[42](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=42:42)_, no term id was found for the name/label _ulnar notch of radius_.

1. In row _[43](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=43:43)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[44](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=44:44)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[45](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=45:45)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[45](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=45:45)_, no term id was found for the name/label _head of ulna of ulna_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=46:46)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=46:46)_, no term id was found for the name/label _interosseous border of ulna_.

1. In row _[47](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=47:47)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[47](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=47:47)_, no term id was found for the name/label _olecranon of ulna_.

1. In row _[48](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=48:48)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[48](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=48:48)_, no term id was found for the name/label _radial notch of ulna_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=49:49)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=49:49)_, no term id was found for the name/label _shaft of ulna of ulna_.

1. In row _[50](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=50:50)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=51:51)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=51:51)_, no term id was found for the name/label _supinator crest of ulna_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=52:52)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=52:52)_, no term id was found for the name/label _supinator fossa of ulna_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=53:53)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=53:53)_, no term id was found for the name/label _trochlear notch of ulna_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=54:54)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=54:54)_, no term id was found for the name/label _ulnar tuberosity of ulna_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=60:60)_, no term id was found for the name/label _hook of hamate_.

1. In row _[62](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=62:62)_, no term id was found for the name/label _base of first distal phalanx of hand_.

1. In row _[63](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=63:63)_, no term id was found for the name/label _head of first distal phalanx of hand_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=64:64)_, no term id was found for the name/label _shaft of first distal phalanx of hand_.

1. In row _[65](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=65:65)_, no term id was found for the name/label _tuberosity of first distal phalanx of hand_.

1. In row _[67](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=67:67)_, no term id was found for the name/label _base of second distal phalanx of hand_.

1. In row _[68](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=68:68)_, no term id was found for the name/label _head of second distal phalanx of hand_.

1. In row _[69](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=69:69)_, no term id was found for the name/label _shaft of second distal phalanx of hand_.

1. In row _[70](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=70:70)_, no term id was found for the name/label _tuberosity of second distal phalanx of hand_.

1. In row _[72](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=72:72)_, no term id was found for the name/label _base of third distal phalanx of hand_.

1. In row _[73](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=73:73)_, no term id was found for the name/label _head of third distal phalanx of hand_.

1. In row _[74](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=74:74)_, no term id was found for the name/label _shaft of third distal phalanx of hand_.

1. In row _[75](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=75:75)_, no term id was found for the name/label _tuberosity of third distal phalanx of hand_.

1. In row _[77](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=77:77)_, no term id was found for the name/label _base of fourth distal phalanx of hand_.

1. In row _[78](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=78:78)_, no term id was found for the name/label _head of fourth distal phalanx of hand_.

1. In row _[79](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=79:79)_, no term id was found for the name/label _shaft of fourth distal phalanx of hand_.

1. In row _[80](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=80:80)_, no term id was found for the name/label _tuberosity of fourth distal phalanx of hand_.

1. In row _[82](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=82:82)_, no term id was found for the name/label _base of fifth distal phalanx of hand_.

1. In row _[83](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=83:83)_, no term id was found for the name/label _head of fifth distal phalanx of hand_.

1. In row _[84](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=84:84)_, no term id was found for the name/label _shaft of fifth distal phalanx of hand_.

1. In row _[85](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=85:85)_, no term id was found for the name/label _tuberosity of fifth distal phalanx of hand_.

1. In row _[88](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=88:88)_, no term id was found for the name/label _base of first metacarpal bone_.

1. In row _[89](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=89:89)_, no term id was found for the name/label _head of first metacarpal bone_.

1. In row _[90](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=90:90)_, no term id was found for the name/label _shaft of first metacarpal bone_.

1. In row _[92](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=92:92)_, no term id was found for the name/label _base of second metacarpal bone_.

1. In row _[93](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=93:93)_, no term id was found for the name/label _head of second metacarpal bone_.

1. In row _[94](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=94:94)_, no term id was found for the name/label _shaft of second metacarpal bone_.

1. In row _[96](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=96:96)_, no term id was found for the name/label _base of third metacarpal bone_.

1. In row _[97](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=97:97)_, no term id was found for the name/label _head of third metacarpal bone_.

1. In row _[98](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=98:98)_, no term id was found for the name/label _shaft of third metacarpal bone_.

1. In row _[100](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=100:100)_, no term id was found for the name/label _base of fourth metacarpal bone_.

1. In row _[101](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=101:101)_, no term id was found for the name/label _head of fourth metacarpal bone_.

1. In row _[102](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=102:102)_, no term id was found for the name/label _shaft of fourth metacarpal bone_.

1. In row _[104](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=104:104)_, no term id was found for the name/label _base of fifth metacarpal bone_.

1. In row _[105](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=105:105)_, no term id was found for the name/label _head of fifth metacarpal bone_.

1. In row _[106](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=106:106)_, no term id was found for the name/label _shaft of fifth metacarpal bone_.

1. In row _[108](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=108:108)_, no term id was found for the name/label _base of second middle phalanx of hand_.

1. In row _[109](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=109:109)_, no term id was found for the name/label _head of second middle phalanx of hand_.

1. In row _[110](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=110:110)_, no term id was found for the name/label _shaft of second middle phalanx of hand_.

1. In row _[112](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=112:112)_, no term id was found for the name/label _base of third middle phalanx of hand_.

1. In row _[113](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=113:113)_, no term id was found for the name/label _head of third middle phalanx of han_.

1. In row _[114](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=114:114)_, no term id was found for the name/label _shaft of third middle phalanx of hand_.

1. In row _[116](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=116:116)_, no term id was found for the name/label _base of fourth middle phalanx of hand_.

1. In row _[117](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=117:117)_, no term id was found for the name/label _head of fourth middle phalanx of hand_.

1. In row _[118](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=118:118)_, no term id was found for the name/label _shaft of fourth middle phalanx of hand_.

1. In row _[120](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=120:120)_, no term id was found for the name/label _base of fifth middle phalanx of hand_.

1. In row _[121](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=121:121)_, no term id was found for the name/label _head of fifth middle phalanx of hand_.

1. In row _[122](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=122:122)_, no term id was found for the name/label _shaft of fifth middle phalanx of hand_.

1. In row _[125](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=125:125)_, no term id was found for the name/label _base of first proximal phalanx of hand_.

1. In row _[126](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=126:126)_, no term id was found for the name/label _head of first proximal phalanx of hand_.

1. In row _[127](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=127:127)_, no term id was found for the name/label _shaft of first proximal phalanx of hand_.

1. In row _[129](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=129:129)_, no term id was found for the name/label _base of second proximal phalanx of hand_.

1. In row _[130](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=130:130)_, no term id was found for the name/label _head of second proximal phalanx of hand_.

1. In row _[131](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=131:131)_, no term id was found for the name/label _shaft of second proximal phalanx of hand_.

1. In row _[133](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=133:133)_, no term id was found for the name/label _base of third proximal phalanx of hand_.

1. In row _[134](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=134:134)_, no term id was found for the name/label _head of third proximal phalanx of hand_.

1. In row _[135](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=135:135)_, no term id was found for the name/label _shaft of third proximal phalanx of hand_.

1. In row _[137](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=137:137)_, no term id was found for the name/label _base of fourth proximal phalanx of hand_.

1. In row _[138](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=138:138)_, no term id was found for the name/label _head of fourth proximal phalanx of hand_.

1. In row _[139](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=139:139)_, no term id was found for the name/label _shaft of fourth proximal phalanx of hand_.

1. In row _[141](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=141:141)_, no term id was found for the name/label _base of fifth proximal phalanx of hand_.

1. In row _[142](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=142:142)_, no term id was found for the name/label _head of fifth proximal phalanx of hand_.

1. In row _[143](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=143:143)_, no term id was found for the name/label _shaft of fifth proximal phalanx of hand_.

1. In row _[145](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=145:145)_, no term id was found for the name/label _scaphoid tubercle of scaphoid_.

1. In row _[149](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=149:149)_, no term id was found for the name/label _acromial end of clavicle_.

1. In row _[150](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=150:150)_, no term id was found for the name/label _acromial facet of clavicle_.

1. In row _[151](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=151:151)_, no term id was found for the name/label _conoid tubercle of clavicle_.

1. In row _[152](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=152:152)_, no term id was found for the name/label _shaft of clavicle_.

1. In row _[154](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=154:154)_, no term id was found for the name/label _sternal facet of clavicle_.

1. In row _[155](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=155:155)_, no term id was found for the name/label _subclavian groove of clavicle_.

1. In row _[156](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=156:156)_, no term id was found for the name/label _trapezoid line of clavicle_.

1. In row _[158](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=158:158)_, no term id was found for the name/label _acromial process of scapula_.

1. In row _[159](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=159:159)_, no term id was found for the name/label _clavicular facet of scapula_.

1. In row _[161](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=161:161)_, no term id was found for the name/label _glenoid fossa of scapula_.

1. In row _[163](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=163:163)_, no term id was found for the name/label _infraglenoid tubercle of scapula_.

1. In row _[164](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=164:164)_, no term id was found for the name/label _infraspinous fossa of scapula_.

1. In row _[167](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=167:167)_, no term id was found for the name/label _scapular neck of scapula_.

1. In row _[168](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=168:168)_, no term id was found for the name/label _scapular notch of scapula_.

1. In row _[169](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=169:169)_, no term id was found for the name/label _scapular spine of scapula_.

1. In row _[170](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=170:170)_, no term id was found for the name/label _subscapular fossa of scapula_.

1. In row _[172](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=172:172)_, no term id was found for the name/label _superior border of scapula_.

1. In row _[173](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=173:173)_, no term id was found for the name/label _supraglenoid tubercle of scapula_.

1. In row _[174](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=174:174)_, no term id was found for the name/label _supraspinous fossa of scapula_.

1. In row _[178](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=178:178)_, no term id was found for the name/label _anterior talar articular surface of calcaneus_.

1. In row _[179](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=179:179)_, no term id was found for the name/label _articular surface for cuboid bone of calcaneus_.

1. In row _[180](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=180:180)_, no term id was found for the name/label _body of calcaneus_.

1. In row _[181](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=181:181)_, no term id was found for the name/label _calcaneal sulcus of calcaneus_.

1. In row _[182](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=182:182)_, no term id was found for the name/label _calcaneal tuberosity of calcaneus_.

1. In row _[183](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=183:183)_, no term id was found for the name/label _fibular trochlea of calcaneus_.

1. In row _[184](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=184:184)_, no term id was found for the name/label _groove for tendon of flexor hallucis longus muscle of calcaneus_.

1. In row _[185](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=185:185)_, no term id was found for the name/label _lateral process of tuberosity of calcaneus_.

1. In row _[186](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=186:186)_, no term id was found for the name/label _medial process of tuberosity of calcaneus_.

1. In row _[187](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=187:187)_, no term id was found for the name/label _middle talar articular surface of calcaneus_.

1. In row _[188](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=188:188)_, no term id was found for the name/label _posterior talar articular surface of calcaneus_.

1. In row _[189](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=189:189)_, no term id was found for the name/label _sustentaculum tali of calcaneus_.

1. In row _[191](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=191:191)_, no term id was found for the name/label _groove for fibularis longus tendon of cuboid_.

1. In row _[192](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=192:192)_, no term id was found for the name/label _tuberosity of cuboid_.

1. In row _[194](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=194:194)_, no term id was found for the name/label _base of first distal phalanx of foot_.

1. In row _[195](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=195:195)_, no term id was found for the name/label _head of first distal phalanx of foot_.

1. In row _[196](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=196:196)_, no term id was found for the name/label _shaft of first distal phalanx of foot_.

1. In row _[198](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=198:198)_, no term id was found for the name/label _base of second distal phalanx of foot_.

1. In row _[199](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=199:199)_, no term id was found for the name/label _head of second distal phalanx of foot_.

1. In row _[200](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=200:200)_, no term id was found for the name/label _shaft of second distal phalanx of foot_.

1. In row _[202](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=202:202)_, no term id was found for the name/label _base of third distal phalanx of foot_.

1. In row _[203](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=203:203)_, no term id was found for the name/label _head of third distal phalanx of foot_.

1. In row _[204](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=204:204)_, no term id was found for the name/label _shaft of third distal phalanx of foot_.

1. In row _[206](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=206:206)_, no term id was found for the name/label _base of fourth distal phalanx of foot_.

1. In row _[207](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=207:207)_, no term id was found for the name/label _head of fourth distal phalanx of foot_.

1. In row _[208](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=208:208)_, no term id was found for the name/label _shaft of fourth distal phalanx of foot_.

1. In row _[210](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=210:210)_, no term id was found for the name/label _base of fifth distal phalanx of foot_.

1. In row _[211](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=211:211)_, no term id was found for the name/label _head of fifth distal phalanx of foot_.

1. In row _[212](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=212:212)_, no term id was found for the name/label _shaft of fifth distal phalanx of foot_.

1. In row _[217](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=217:217)_, no term id was found for the name/label _base of first metatarsal bone_.

1. In row _[218](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=218:218)_, no term id was found for the name/label _head of first metatarsal bone_.

1. In row _[219](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=219:219)_, no term id was found for the name/label _shaft of first metatarsal bone_.

1. In row _[221](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=221:221)_, no term id was found for the name/label _base of second metatarsal bone_.

1. In row _[222](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=222:222)_, no term id was found for the name/label _head of second metatarsal bone_.

1. In row _[223](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=223:223)_, no term id was found for the name/label _shaft of second metatarsal bone_.

1. In row _[225](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=225:225)_, no term id was found for the name/label _base of third metatarsal bone_.

1. In row _[226](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=226:226)_, no term id was found for the name/label _head of third metatarsal bone_.

1. In row _[227](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=227:227)_, no term id was found for the name/label _shaft of third metatarsal bone_.

1. In row _[229](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=229:229)_, no term id was found for the name/label _base of fourth metatarsal bone_.

1. In row _[230](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=230:230)_, no term id was found for the name/label _head of fourth metatarsal bone_.

1. In row _[231](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=231:231)_, no term id was found for the name/label _shaft of fourth metatarsal bone_.

1. In row _[233](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=233:233)_, no term id was found for the name/label _base of fifth metatarsal bone_.

1. In row _[234](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=234:234)_, no term id was found for the name/label _head of fifth metatarsal bone_.

1. In row _[235](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=235:235)_, no term id was found for the name/label _shaft of fifth metatarsal bone_.

1. In row _[236](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=236:236)_, no term id was found for the name/label _tuberosity of fifth metatarsal bone_.

1. In row _[238](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=238:238)_, no term id was found for the name/label _base of second middle phalanx of foot_.

1. In row _[239](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=239:239)_, no term id was found for the name/label _head of second middle phalanx of foot_.

1. In row _[240](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=240:240)_, no term id was found for the name/label _shaft of second middle phalanx of foot_.

1. In row _[242](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=242:242)_, no term id was found for the name/label _base of third middle phalanx of foot_.

1. In row _[243](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=243:243)_, no term id was found for the name/label _head of third middle phalanx of foot_.

1. In row _[244](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=244:244)_, no term id was found for the name/label _shaft of third middle phalanx of foot_.

1. In row _[246](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=246:246)_, no term id was found for the name/label _base of fourth middle phalanx of foot_.

1. In row _[247](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=247:247)_, no term id was found for the name/label _head of fourth middle phalanx of foot_.

1. In row _[248](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=248:248)_, no term id was found for the name/label _shaft of fourth middle phalanx of foot_.

1. In row _[250](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=250:250)_, no term id was found for the name/label _base of fifth middle phalanx of foot_.

1. In row _[251](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=251:251)_, no term id was found for the name/label _head of fifth middle phalanx of foot_.

1. In row _[252](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=252:252)_, no term id was found for the name/label _shaft of fifth middle phalanx of foot_.

1. In row _[254](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=254:254)_, no term id was found for the name/label _tuberosity of navicular_.

1. In row _[256](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=256:256)_, no term id was found for the name/label _base of first proximal phalanx of foot_.

1. In row _[257](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=257:257)_, no term id was found for the name/label _head of first proximal phalanx of foot_.

1. In row _[258](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=258:258)_, no term id was found for the name/label _shaft of first proximal phalanx of foot_.

1. In row _[260](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=260:260)_, no term id was found for the name/label _base of second proximal phalanx of foot_.

1. In row _[261](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=261:261)_, no term id was found for the name/label _head of second proximal phalanx of foot_.

1. In row _[262](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=262:262)_, no term id was found for the name/label _shaft of second proximal phalanx of foot_.

1. In row _[264](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=264:264)_, no term id was found for the name/label _base of third proximal phalanx of foot_.

1. In row _[265](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=265:265)_, no term id was found for the name/label _head of third proximal phalanx of foot_.

1. In row _[266](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=266:266)_, no term id was found for the name/label _shaft of third proximal phalanx of foot_.

1. In row _[268](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=268:268)_, no term id was found for the name/label _base of fourth proximal phalanx of foot_.

1. In row _[269](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=269:269)_, no term id was found for the name/label _head of fourth proximal phalanx of foot_.

1. In row _[270](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=270:270)_, no term id was found for the name/label _shaft of fourth proximal phalanx of foot_.

1. In row _[272](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=272:272)_, no term id was found for the name/label _base of fifth proximal phalanx of foot_.

1. In row _[273](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=273:273)_, no term id was found for the name/label _head of fifth proximal phalanx of foot_.

1. In row _[274](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=274:274)_, no term id was found for the name/label _shaft of fifth proximal phalanx of foot_.

1. In row _[276](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=276:276)_, no term id was found for the name/label _head of talus_.

1. In row _[277](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=277:277)_, no term id was found for the name/label _lateral process of talus_.

1. In row _[279](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=279:279)_, no term id was found for the name/label _posterior process of talus_.

1. In row _[280](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=280:280)_, no term id was found for the name/label _trochlea of talus_.

1. In row _[281](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=281:281)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[282](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=282:282)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[283](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=283:283)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[283](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=283:283)_, no term id was found for the name/label _adductor tubercle of femur_.

1. In row _[284](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=284:284)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[284](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=284:284)_, no term id was found for the name/label _gluteal tuberosity of femur_.

1. In row _[285](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=285:285)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[285](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=285:285)_, no term id was found for the name/label _greater trochanter of femur_.

1. In row _[286](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=286:286)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[287](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=287:287)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[287](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=287:287)_, no term id was found for the name/label _intercondylar fossa of femur_.

1. In row _[288](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=288:288)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[288](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=288:288)_, no term id was found for the name/label _intercondylar notch of femur_.

1. In row _[289](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=289:289)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[289](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=289:289)_, no term id was found for the name/label _intertrochanteric crest of femur_.

1. In row _[290](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=290:290)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[291](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=291:291)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[292](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=292:292)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[292](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=292:292)_, no term id was found for the name/label _lateral lip of linea aspera of femur_.

1. In row _[293](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=293:293)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[293](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=293:293)_, no term id was found for the name/label _lesser trochanter of femur_.

1. In row _[294](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=294:294)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[294](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=294:294)_, no term id was found for the name/label _linea aspera of femur_.

1. In row _[295](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=295:295)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[296](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=296:296)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[297](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=297:297)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[297](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=297:297)_, no term id was found for the name/label _medial lip of linea aspera of femur_.

1. In row _[298](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=298:298)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[299](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=299:299)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[299](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=299:299)_, no term id was found for the name/label _pectinal line of femur_.

1. In row _[300](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=300:300)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[300](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=300:300)_, no term id was found for the name/label _popliteal surface of femur_.

1. In row _[301](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=301:301)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[301](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=301:301)_, no term id was found for the name/label _quadrate tubercle of femur_.

1. In row _[302](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=302:302)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[302](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=302:302)_, no term id was found for the name/label _shaft of femur_.

1. In row _[303](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=303:303)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[303](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=303:303)_, no term id was found for the name/label _trochanteric fossa of femur_.

1. In row _[304](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=304:304)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[305](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=305:305)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[305](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=305:305)_, no term id was found for the name/label _head of fibula_.

1. In row _[306](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=306:306)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[307](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=307:307)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[308](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=308:308)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[308](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=308:308)_, no term id was found for the name/label _shaft of fibula_.

1. In row _[309](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=309:309)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[310](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=310:310)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[311](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=311:311)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[311](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=311:311)_, no term id was found for the name/label _anterolateral tubercle of tibia_.

1. In row _[312](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=312:312)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[312](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=312:312)_, no term id was found for the name/label _fibular facet of tibia_.

1. In row _[313](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=313:313)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[313](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=313:313)_, no term id was found for the name/label _fibular notch of tibia_.

1. In row _[314](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=314:314)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[314](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=314:314)_, no term id was found for the name/label _intercondylar eminence of tibia_.

1. In row _[315](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=315:315)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[315](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=315:315)_, no term id was found for the name/label _interosseus border of tibia_.

1. In row _[316](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=316:316)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[317](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=317:317)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[318](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=318:318)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[318](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=318:318)_, no term id was found for the name/label _medial malleolus of tibia_.

1. In row _[319](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=319:319)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[319](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=319:319)_, no term id was found for the name/label _shaft of tibia_.

1. In row _[320](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=320:320)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[320](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=320:320)_, no term id was found for the name/label _soleal line of tibia_.

1. In row _[321](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=321:321)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[321](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=321:321)_, no term id was found for the name/label _tibial plateau of tibia_.

1. In row _[322](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=322:322)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[322](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=322:322)_, no term id was found for the name/label _tibial tuberosity of tibia_.

1. In row _[325](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=325:325)_, no term id was found for the name/label _acetabular fossa of os coxa_.

1. In row _[326](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=326:326)_, no term id was found for the name/label _acetabular notch of os coxa_.

1. In row _[327](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=327:327)_, no term id was found for the name/label _acetabulum of os coxa_.

1. In row _[328](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=328:328)_, no term id was found for the name/label _anterior gluteal line of ilium of os coxa_.

1. In row _[329](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=329:329)_, no term id was found for the name/label _anterior inferior iliac spine of ilium of os coxa_.

1. In row _[330](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=330:330)_, no term id was found for the name/label _anterior superior iliac spine of ilium of os coxa_.

1. In row _[331](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=331:331)_, no term id was found for the name/label _arcuate line of ilium of os coxa_.

1. In row _[332](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=332:332)_, no term id was found for the name/label _auricular surface of ilium of os coxa_.

1. In row _[333](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=333:333)_, no term id was found for the name/label _gluteal surface of ilium of os coxa_.

1. In row _[334](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=334:334)_, no term id was found for the name/label _greater sciatic notch of ilium of os coxa_.

1. In row _[335](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=335:335)_, no term id was found for the name/label _iliac crest of ilium of os coxa_.

1. In row _[336](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=336:336)_, no term id was found for the name/label _iliac fossa of ilium of os coxa_.

1. In row _[337](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=337:337)_, no term id was found for the name/label _iliac tubercle of ilium of os coxa_.

1. In row _[338](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=338:338)_, no term id was found for the name/label _iliac tuberosity of ilium of os coxa_.

1. In row _[339](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=339:339)_, no term id was found for the name/label _iliopubic ramus of os coxa_.

1. In row _[340](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=340:340)_, no term id was found for the name/label _inferior pubic ramus of pubis of os coxa_.

1. In row _[341](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=341:341)_, no term id was found for the name/label _ischial body of ischium of os coxa_.

1. In row _[342](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=342:342)_, no term id was found for the name/label _ischial ramus of ischium of os coxa_.

1. In row _[343](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=343:343)_, no term id was found for the name/label _ischial spine of ischium of os coxa_.

1. In row _[344](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=344:344)_, no term id was found for the name/label _ischial tuberosity of ischium of os coxa_.

1. In row _[345](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=345:345)_, no term id was found for the name/label _ischiopubic ramus of os coxa_.

1. In row _[346](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=346:346)_, no term id was found for the name/label _lesser sciatic notch of ischium of os coxa_.

1. In row _[347](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=347:347)_, no term id was found for the name/label _lunate surface of os coxa_.

1. In row _[348](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=348:348)_, no term id was found for the name/label _obturator foramen of os coxa_.

1. In row _[349](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=349:349)_, no term id was found for the name/label _obturator groove of pubis of os coxa_.

1. In row _[350](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=350:350)_, no term id was found for the name/label _pecten pubis of pubis of os coxa_.

1. In row _[351](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=351:351)_, no term id was found for the name/label _posterior gluteal line of ilium of os coxa_.

1. In row _[352](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=352:352)_, no term id was found for the name/label _posterior inferior iliac spine of ilium of os coxa_.

1. In row _[353](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=353:353)_, no term id was found for the name/label _posterior superior iliac spine of ilium of os coxa_.

1. In row _[354](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=354:354)_, no term id was found for the name/label _pubic body of pubis of os coxa_.

1. In row _[355](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=355:355)_, no term id was found for the name/label _pubic crest of pubis of os coxa_.

1. In row _[356](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=356:356)_, no term id was found for the name/label _pubic symphysis of pubis of os coxa_.

1. In row _[357](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=357:357)_, no term id was found for the name/label _pubic tubercle of pubis of os coxa_.

1. In row _[358](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=358:358)_, no term id was found for the name/label _superior pubic ramus of pubis of os coxa_.

1. In row _[361](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=361:361)_, no term id was found for the name/label _hyoid region bone_.

1. In row _[362](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=362:362)_, no term id was found for the name/label _hyoid region bone_.

1. In row _[363](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=363:363)_, no term id was found for the name/label _hyoid region bone_.

1. In row _[363](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=363:363)_, no term id was found for the name/label _body of hyoid bone_.

1. In row _[364](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=364:364)_, no term id was found for the name/label _hyoid region bone_.

1. In row _[364](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=364:364)_, no term id was found for the name/label _greater cornu of hyoid bone_.

1. In row _[365](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=365:365)_, no term id was found for the name/label _hyoid region bone_.

1. In row _[365](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=365:365)_, no term id was found for the name/label _lesser cornu of hyoid bone_.

1. In row _[368](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=368:368)_, no term id was found for the name/label _anterior ethmoidal foramen of ethmoid bone_.

1. In row _[369](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=369:369)_, no term id was found for the name/label _cribiform plate of ethmoid bone_.

1. In row _[370](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=370:370)_, no term id was found for the name/label _crista galla of ethmoid bone_.

1. In row _[371](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=371:371)_, no term id was found for the name/label _ethmoidal air cells of ethmoid bone_.

1. In row _[372](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=372:372)_, no term id was found for the name/label _ethmoidal bulla of ethmoid bone_.

1. In row _[373](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=373:373)_, no term id was found for the name/label _middle nasal concha of ethmoid bone_.

1. In row _[374](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=374:374)_, no term id was found for the name/label _olfactory foramina of ethmoid bone_.

1. In row _[375](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=375:375)_, no term id was found for the name/label _perpendicular plate of ethmoid bone_.

1. In row _[376](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=376:376)_, no term id was found for the name/label _posterior ethmoidal foramen of ethmoid bone_.

1. In row _[377](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=377:377)_, no term id was found for the name/label _superior nasal concha of ethmoid bone_.

1. In row _[379](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=379:379)_, no term id was found for the name/label _frontal crest of frontal bone_.

1. In row _[380](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=380:380)_, no term id was found for the name/label _frontal sinus of frontal bone_.

1. In row _[381](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=381:381)_, no term id was found for the name/label _glabella of frontal bone_.

1. In row _[382](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=382:382)_, no term id was found for the name/label _groove for superior sagittal sinus of frontal bone_.

1. In row _[383](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=383:383)_, no term id was found for the name/label _lacrimal fossa of frontal bone_.

1. In row _[384](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=384:384)_, no term id was found for the name/label _orbital surface of frontal bone_.

1. In row _[385](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=385:385)_, no term id was found for the name/label _supercilary arch of frontal bone_.

1. In row _[386](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=386:386)_, no term id was found for the name/label _supraorbital margin of frontal bone_.

1. In row _[387](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=387:387)_, no term id was found for the name/label _supraorbital notch or foramen of frontal bone_.

1. In row _[390](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=390:390)_, no term id was found for the name/label _external occipital protuberance of squamous part of occipital bone_.

1. In row _[391](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=391:391)_, no term id was found for the name/label _foramen magnum of basilar part of occipital bone_.

1. In row _[392](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=392:392)_, no term id was found for the name/label _groove for transverse sinus of squamous part of occipital bone_.

1. In row _[393](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=393:393)_, no term id was found for the name/label _hypoglossal canal of basilar part of occipital bone_.

1. In row _[394](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=394:394)_, no term id was found for the name/label _inferior nuchal line of squamous part of occipital bone_.

1. In row _[395](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=395:395)_, no term id was found for the name/label _internal occipital protuberance of squamous part of occipital bone_.

1. In row _[396](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=396:396)_, no term id was found for the name/label _jugular foramen of basilar part of occipital bone_.

1. In row _[397](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=397:397)_, no term id was found for the name/label _occipital condyle of basilar part of occipital bone_.

1. In row _[398](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=398:398)_, no term id was found for the name/label _superior nuchal line of squamous part of occipital bone_.

1. In row _[400](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=400:400)_, no term id was found for the name/label _granula foveaolae of parietal bone_.

1. In row _[401](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=401:401)_, no term id was found for the name/label _groove for middle meningeal a. of parietal bone_.

1. In row _[402](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=402:402)_, no term id was found for the name/label _groove for superior sagittal sinus of parietal bone_.

1. In row _[403](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=403:403)_, no term id was found for the name/label _inferior temporal line of parietal bone_.

1. In row _[404](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=404:404)_, no term id was found for the name/label _superior temporal line of parietal bone_.

1. In row _[405](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=405:405)_, no term id was found for the name/label _temporal fossa of parietal bone_.

1. In row _[407](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=407:407)_, no term id was found for the name/label _anterior clinoid process of sphenoid bone_.

1. In row _[408](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=408:408)_, no term id was found for the name/label _body of sphenoid bone_.

1. In row _[409](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=409:409)_, no term id was found for the name/label _dorsum sellae of sphenoid bone_.

1. In row _[410](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=410:410)_, no term id was found for the name/label _foramen lacerum of sphenoid bone_.

1. In row _[411](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=411:411)_, no term id was found for the name/label _foramen ovale of sphenoid bone_.

1. In row _[412](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=412:412)_, no term id was found for the name/label _foramen rotundum of sphenoid bone_.

1. In row _[414](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=414:414)_, no term id was found for the name/label _greater wings of sphenoid bone_.

1. In row _[415](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=415:415)_, no term id was found for the name/label _hypophyseal fossa of sphenoid bone_.

1. In row _[416](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=416:416)_, no term id was found for the name/label _lateral pterygoid plate of sphenoid bone_.

1. In row _[417](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=417:417)_, no term id was found for the name/label _lesser wings of sphenoid bone_.

1. In row _[418](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=418:418)_, no term id was found for the name/label _medial pterygoid plate of sphenoid bone_.

1. In row _[419](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=419:419)_, no term id was found for the name/label _optic canal of sphenoid bone_.

1. In row _[420](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=420:420)_, no term id was found for the name/label _posterior clinoid process of sphenoid bone_.

1. In row _[421](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=421:421)_, no term id was found for the name/label _pterygoid canal of sphenoid bone_.

1. In row _[422](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=422:422)_, no term id was found for the name/label _pterygoid fossa of sphenoid bone_.

1. In row _[423](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=423:423)_, no term id was found for the name/label _pterygoid hamulus of sphenoid bone_.

1. In row _[424](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=424:424)_, no term id was found for the name/label _pterygoid process of sphenoid bone_.

1. In row _[425](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=425:425)_, no term id was found for the name/label _sella turcica of sphenoid bone_.

1. In row _[426](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=426:426)_, no term id was found for the name/label _sphenoid sinus of sphenoid bone_.

1. In row _[427](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=427:427)_, no term id was found for the name/label _superior orbital fissure of sphenoid bone_.

1. In row _[429](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=429:429)_, no term id was found for the name/label _articular tubercle of squamous part of temporal bone_.

1. In row _[430](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=430:430)_, no term id was found for the name/label _carotid canal of petrous part of temporal bone_.

1. In row _[431](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=431:431)_, no term id was found for the name/label _external auditory meatus of squamous part of temporal bone_.

1. In row _[432](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=432:432)_, no term id was found for the name/label _groove for posterior deep temporal artery of squamous part of temporal bone_.

1. In row _[433](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=433:433)_, no term id was found for the name/label _groove for sigmoid sinus of mastoid part of temporal bone_.

1. In row _[434](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=434:434)_, no term id was found for the name/label _hiatus and groove of petrous part of temporal bone for greater petrosal nerve_.

1. In row _[435](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=435:435)_, no term id was found for the name/label _hiatus and groove of petrous part of temporal bone for lesser petrosal nerve_.

1. In row _[436](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=436:436)_, no term id was found for the name/label _internal auditory meatus of petrous part of temporal bone_.

1. In row _[437](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=437:437)_, no term id was found for the name/label _jugular foramen of petrous part of temporal bone_.

1. In row _[438](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=438:438)_, no term id was found for the name/label _mandibular fossa of squamous part of temporal bone_.

1. In row _[439](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=439:439)_, no term id was found for the name/label _mastoid foramen of mastoid part of temporal bone_.

1. In row _[440](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=440:440)_, no term id was found for the name/label _mastoid notch of mastoid part of temporal bone_.

1. In row _[441](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=441:441)_, no term id was found for the name/label _mastoid process of mastoid part of temporal bone_.

1. In row _[442](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=442:442)_, no term id was found for the name/label _petrotympanic fissure of squamous part of temporal bone_.

1. In row _[443](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=443:443)_, no term id was found for the name/label _postglenoid tubercle of squamous part of temporal bone_.

1. In row _[444](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=444:444)_, no term id was found for the name/label _styloid process of petrous part of temporal bone_.

1. In row _[445](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=445:445)_, no term id was found for the name/label _stylomastoid foramen of petrous part of temporal bone_.

1. In row _[446](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=446:446)_, no term id was found for the name/label _supramastoid crest of squamous part of temporal bone_.

1. In row _[447](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=447:447)_, no term id was found for the name/label _trigeminal impression of petrous part of temporal bone_.

1. In row _[448](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=448:448)_, no term id was found for the name/label _tympanic caniliculus of petrous part of temporal bone_.

1. In row _[449](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=449:449)_, no term id was found for the name/label _zygomatic process of squamous part of temporal bone_.

1. In row _[457](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=457:457)_, no term id was found for the name/label _fossa for lacrimal sac of lacrimal bone_.

1. In row _[459](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=459:459)_, no term id was found for the name/label _alveolar border of mandible_.

1. In row _[461](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=461:461)_, no term id was found for the name/label _coronoid process of mandible_.

1. In row _[462](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=462:462)_, no term id was found for the name/label _digastric fossa of mandible_.

1. In row _[463](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=463:463)_, no term id was found for the name/label _inferior mental spine of mandible_.

1. In row _[464](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=464:464)_, no term id was found for the name/label _lingula of mandible_.

1. In row _[465](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=465:465)_, no term id was found for the name/label _mandibular angle of mandible_.

1. In row _[466](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=466:466)_, no term id was found for the name/label _mandibular canal of mandible_.

1. In row _[467](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=467:467)_, no term id was found for the name/label _mandibular condyle of mandible_.

1. In row _[468](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=468:468)_, no term id was found for the name/label _mandibular foramen of mandible_.

1. In row _[469](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=469:469)_, no term id was found for the name/label _mandibular neck of mandible_.

1. In row _[470](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=470:470)_, no term id was found for the name/label _mandibular notch of mandible_.

1. In row _[471](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=471:471)_, no term id was found for the name/label _mental foramen of mandible_.

1. In row _[472](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=472:472)_, no term id was found for the name/label _mental protuberance of mandible_.

1. In row _[473](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=473:473)_, no term id was found for the name/label _mylohyoid groove of mandible_.

1. In row _[474](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=474:474)_, no term id was found for the name/label _mylohyoid line of mandible_.

1. In row _[475](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=475:475)_, no term id was found for the name/label _pterygoid fovea of mandible_.

1. In row _[476](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=476:476)_, no term id was found for the name/label _ramus of mandible_.

1. In row _[477](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=477:477)_, no term id was found for the name/label _sublingual fossa of mandible_.

1. In row _[478](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=478:478)_, no term id was found for the name/label _submandibular fossa of mandible_.

1. In row _[479](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=479:479)_, no term id was found for the name/label _superior mental spine of mandible_.

1. In row _[481](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=481:481)_, no term id was found for the name/label _alveolar canals of maxilla_.

1. In row _[485](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=485:485)_, no term id was found for the name/label _greater palatine canal of maxilla_.

1. In row _[486](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=486:486)_, no term id was found for the name/label _incisive foramen of maxilla_.

1. In row _[487](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=487:487)_, no term id was found for the name/label _infraorbital canal of maxilla_.

1. In row _[488](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=488:488)_, no term id was found for the name/label _infraorbital foramen of maxilla_.

1. In row _[489](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=489:489)_, no term id was found for the name/label _infraorbital groove of maxilla_.

1. In row _[490](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=490:490)_, no term id was found for the name/label _intermaxillary suture of maxilla_.

1. In row _[491](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=491:491)_, no term id was found for the name/label _maxillary sinus of maxilla_.

1. In row _[492](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=492:492)_, no term id was found for the name/label _nasal surface of maxilla_.

1. In row _[493](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=493:493)_, no term id was found for the name/label _nasolacrimal canal of maxilla_.

1. In row _[498](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=498:498)_, no term id was found for the name/label _greater palatine foramen of palatine bone_.

1. In row _[499](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=499:499)_, no term id was found for the name/label _horizontal plate of palatine bone_.

1. In row _[500](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=500:500)_, no term id was found for the name/label _lesser palatine foramen of palatine bone_.

1. In row _[501](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=501:501)_, no term id was found for the name/label _perpendicular plate of palatine bone_.

1. In row _[503](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=503:503)_, no term id was found for the name/label _ala of vomer_.

1. In row _[504](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=504:504)_, no term id was found for the name/label _groove for nasopalatine nerve of vomer_.

1. In row _[507](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=507:507)_, no term id was found for the name/label _maxillary process of zygomatic bone_.

1. In row _[509](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=509:509)_, no term id was found for the name/label _zygomaticofacial foramen of zygomatic bone_.

1. In row _[511](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=511:511)_, no term id was found for the name/label _costal region bone_.

1. In row _[512](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=512:512)_, no term id was found for the name/label _costal region bone_.

1. In row _[513](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=513:513)_, no term id was found for the name/label _costal region bone_.

1. In row _[513](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=513:513)_, no term id was found for the name/label _angle of first rib_.

1. In row _[514](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=514:514)_, no term id was found for the name/label _costal region bone_.

1. In row _[514](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=514:514)_, no term id was found for the name/label _articular facet of tubercle of first rib_.

1. In row _[515](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=515:515)_, no term id was found for the name/label _costal region bone_.

1. In row _[515](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=515:515)_, no term id was found for the name/label _body of first rib_.

1. In row _[516](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=516:516)_, no term id was found for the name/label _costal region bone_.

1. In row _[516](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=516:516)_, no term id was found for the name/label _costal groove of first rib_.

1. In row _[517](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=517:517)_, no term id was found for the name/label _costal region bone_.

1. In row _[517](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=517:517)_, no term id was found for the name/label _facet of first rib_.

1. In row _[518](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=518:518)_, no term id was found for the name/label _costal region bone_.

1. In row _[518](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=518:518)_, no term id was found for the name/label _groove for subclavian artery of first rib_.

1. In row _[519](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=519:519)_, no term id was found for the name/label _costal region bone_.

1. In row _[519](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=519:519)_, no term id was found for the name/label _groove for subclavian vein of first rib_.

1. In row _[520](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=520:520)_, no term id was found for the name/label _costal region bone_.

1. In row _[520](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=520:520)_, no term id was found for the name/label _head of first rib_.

1. In row _[521](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=521:521)_, no term id was found for the name/label _costal region bone_.

1. In row _[521](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=521:521)_, no term id was found for the name/label _neck of first rib_.

1. In row _[522](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=522:522)_, no term id was found for the name/label _costal region bone_.

1. In row _[522](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=522:522)_, no term id was found for the name/label _non-articular facet of tubercle of first rib_.

1. In row _[523](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=523:523)_, no term id was found for the name/label _costal region bone_.

1. In row _[523](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=523:523)_, no term id was found for the name/label _scalene tubercle of first rib_.

1. In row _[524](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=524:524)_, no term id was found for the name/label _costal region bone_.

1. In row _[524](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=524:524)_, no term id was found for the name/label _sternal end of first rib_.

1. In row _[525](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=525:525)_, no term id was found for the name/label _costal region bone_.

1. In row _[525](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=525:525)_, no term id was found for the name/label _tubercle of first rib_.

1. In row _[526](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=526:526)_, no term id was found for the name/label _costal region bone_.

1. In row _[527](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=527:527)_, no term id was found for the name/label _costal region bone_.

1. In row _[527](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=527:527)_, no term id was found for the name/label _angle of tenth rib_.

1. In row _[528](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=528:528)_, no term id was found for the name/label _costal region bone_.

1. In row _[528](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=528:528)_, no term id was found for the name/label _articular facet of tubercle of tenth rib_.

1. In row _[529](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=529:529)_, no term id was found for the name/label _costal region bone_.

1. In row _[529](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=529:529)_, no term id was found for the name/label _body of tenth rib_.

1. In row _[530](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=530:530)_, no term id was found for the name/label _costal region bone_.

1. In row _[530](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=530:530)_, no term id was found for the name/label _costal groove of tenth rib_.

1. In row _[531](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=531:531)_, no term id was found for the name/label _costal region bone_.

1. In row _[531](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=531:531)_, no term id was found for the name/label _facet of tenth rib_.

1. In row _[532](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=532:532)_, no term id was found for the name/label _costal region bone_.

1. In row _[532](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=532:532)_, no term id was found for the name/label _head of tenth rib_.

1. In row _[533](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=533:533)_, no term id was found for the name/label _costal region bone_.

1. In row _[533](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=533:533)_, no term id was found for the name/label _neck of tenth rib_.

1. In row _[534](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=534:534)_, no term id was found for the name/label _costal region bone_.

1. In row _[534](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=534:534)_, no term id was found for the name/label _non-articular facet of tubercle of tenth rib_.

1. In row _[535](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=535:535)_, no term id was found for the name/label _costal region bone_.

1. In row _[535](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=535:535)_, no term id was found for the name/label _sternal end of tenth rib_.

1. In row _[536](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=536:536)_, no term id was found for the name/label _costal region bone_.

1. In row _[536](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=536:536)_, no term id was found for the name/label _tubercle of tenth rib_.

1. In row _[537](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=537:537)_, no term id was found for the name/label _costal region bone_.

1. In row _[538](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=538:538)_, no term id was found for the name/label _costal region bone_.

1. In row _[538](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=538:538)_, no term id was found for the name/label _body of eleventh rib_.

1. In row _[539](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=539:539)_, no term id was found for the name/label _costal region bone_.

1. In row _[539](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=539:539)_, no term id was found for the name/label _costal groove of eleventh rib_.

1. In row _[540](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=540:540)_, no term id was found for the name/label _costal region bone_.

1. In row _[540](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=540:540)_, no term id was found for the name/label _facet of eleventh rib_.

1. In row _[541](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=541:541)_, no term id was found for the name/label _costal region bone_.

1. In row _[541](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=541:541)_, no term id was found for the name/label _head of eleventh rib_.

1. In row _[542](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=542:542)_, no term id was found for the name/label _costal region bone_.

1. In row _[542](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=542:542)_, no term id was found for the name/label _sternal end of eleventh rib_.

1. In row _[543](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=543:543)_, no term id was found for the name/label _costal region bone_.

1. In row _[544](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=544:544)_, no term id was found for the name/label _costal region bone_.

1. In row _[544](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=544:544)_, no term id was found for the name/label _body of twelfth rib_.

1. In row _[545](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=545:545)_, no term id was found for the name/label _costal region bone_.

1. In row _[545](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=545:545)_, no term id was found for the name/label _costal groove of twelfth rib_.

1. In row _[546](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=546:546)_, no term id was found for the name/label _costal region bone_.

1. In row _[546](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=546:546)_, no term id was found for the name/label _facet of twelfth rib_.

1. In row _[547](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=547:547)_, no term id was found for the name/label _costal region bone_.

1. In row _[547](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=547:547)_, no term id was found for the name/label _head of twelfth rib_.

1. In row _[548](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=548:548)_, no term id was found for the name/label _costal region bone_.

1. In row _[548](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=548:548)_, no term id was found for the name/label _sternal end of twelfth rib_.

1. In row _[549](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=549:549)_, no term id was found for the name/label _costal region bone_.

1. In row _[550](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=550:550)_, no term id was found for the name/label _costal region bone_.

1. In row _[550](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=550:550)_, no term id was found for the name/label _angle of second rib_.

1. In row _[551](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=551:551)_, no term id was found for the name/label _costal region bone_.

1. In row _[551](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=551:551)_, no term id was found for the name/label _articular facet of tubercle of second rib_.

1. In row _[552](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=552:552)_, no term id was found for the name/label _costal region bone_.

1. In row _[552](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=552:552)_, no term id was found for the name/label _body of second rib_.

1. In row _[553](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=553:553)_, no term id was found for the name/label _costal region bone_.

1. In row _[553](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=553:553)_, no term id was found for the name/label _costal groove of second rib_.

1. In row _[554](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=554:554)_, no term id was found for the name/label _costal region bone_.

1. In row _[554](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=554:554)_, no term id was found for the name/label _head of second rib_.

1. In row _[555](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=555:555)_, no term id was found for the name/label _costal region bone_.

1. In row _[555](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=555:555)_, no term id was found for the name/label _inferior articular facet of second rib_.

1. In row _[556](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=556:556)_, no term id was found for the name/label _costal region bone_.

1. In row _[556](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=556:556)_, no term id was found for the name/label _neck of second rib_.

1. In row _[557](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=557:557)_, no term id was found for the name/label _costal region bone_.

1. In row _[557](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=557:557)_, no term id was found for the name/label _non-articular facet of tubercle of second rib_.

1. In row _[558](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=558:558)_, no term id was found for the name/label _costal region bone_.

1. In row _[558](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=558:558)_, no term id was found for the name/label _sternal end of second rib_.

1. In row _[559](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=559:559)_, no term id was found for the name/label _costal region bone_.

1. In row _[559](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=559:559)_, no term id was found for the name/label _superior articular facet of second rib_.

1. In row _[560](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=560:560)_, no term id was found for the name/label _costal region bone_.

1. In row _[560](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=560:560)_, no term id was found for the name/label _tubercle of second rib_.

1. In row _[561](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=561:561)_, no term id was found for the name/label _costal region bone_.

1. In row _[562](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=562:562)_, no term id was found for the name/label _costal region bone_.

1. In row _[562](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=562:562)_, no term id was found for the name/label _angle of third rib_.

1. In row _[563](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=563:563)_, no term id was found for the name/label _costal region bone_.

1. In row _[563](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=563:563)_, no term id was found for the name/label _articular facet of tubercle of third rib_.

1. In row _[564](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=564:564)_, no term id was found for the name/label _costal region bone_.

1. In row _[564](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=564:564)_, no term id was found for the name/label _body of third rib_.

1. In row _[565](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=565:565)_, no term id was found for the name/label _costal region bone_.

1. In row _[565](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=565:565)_, no term id was found for the name/label _costal groove of third rib_.

1. In row _[566](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=566:566)_, no term id was found for the name/label _costal region bone_.

1. In row _[566](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=566:566)_, no term id was found for the name/label _crest of head of third rib_.

1. In row _[567](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=567:567)_, no term id was found for the name/label _costal region bone_.

1. In row _[567](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=567:567)_, no term id was found for the name/label _head of third rib_.

1. In row _[568](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=568:568)_, no term id was found for the name/label _costal region bone_.

1. In row _[568](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=568:568)_, no term id was found for the name/label _inferior articular facet of third rib_.

1. In row _[569](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=569:569)_, no term id was found for the name/label _costal region bone_.

1. In row _[569](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=569:569)_, no term id was found for the name/label _neck of third rib_.

1. In row _[570](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=570:570)_, no term id was found for the name/label _costal region bone_.

1. In row _[570](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=570:570)_, no term id was found for the name/label _non-articular facet of tubercle of third rib_.

1. In row _[571](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=571:571)_, no term id was found for the name/label _costal region bone_.

1. In row _[571](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=571:571)_, no term id was found for the name/label _sternal end of third rib_.

1. In row _[572](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=572:572)_, no term id was found for the name/label _costal region bone_.

1. In row _[572](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=572:572)_, no term id was found for the name/label _superior articular facet of third rib_.

1. In row _[573](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=573:573)_, no term id was found for the name/label _costal region bone_.

1. In row _[573](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=573:573)_, no term id was found for the name/label _tubercle of third rib_.

1. In row _[574](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=574:574)_, no term id was found for the name/label _costal region bone_.

1. In row _[575](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=575:575)_, no term id was found for the name/label _costal region bone_.

1. In row _[575](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=575:575)_, no term id was found for the name/label _angle of fourth rib_.

1. In row _[576](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=576:576)_, no term id was found for the name/label _costal region bone_.

1. In row _[576](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=576:576)_, no term id was found for the name/label _articular facet of tubercle of fourth rib_.

1. In row _[577](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=577:577)_, no term id was found for the name/label _costal region bone_.

1. In row _[577](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=577:577)_, no term id was found for the name/label _body of fourth rib_.

1. In row _[578](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=578:578)_, no term id was found for the name/label _costal region bone_.

1. In row _[578](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=578:578)_, no term id was found for the name/label _costal groove of fourth rib_.

1. In row _[579](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=579:579)_, no term id was found for the name/label _costal region bone_.

1. In row _[579](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=579:579)_, no term id was found for the name/label _crest of head of fourth rib_.

1. In row _[580](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=580:580)_, no term id was found for the name/label _costal region bone_.

1. In row _[580](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=580:580)_, no term id was found for the name/label _head of fourth rib_.

1. In row _[581](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=581:581)_, no term id was found for the name/label _costal region bone_.

1. In row _[581](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=581:581)_, no term id was found for the name/label _inferior articular facet of fourth rib_.

1. In row _[582](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=582:582)_, no term id was found for the name/label _costal region bone_.

1. In row _[582](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=582:582)_, no term id was found for the name/label _neck of fourth rib_.

1. In row _[583](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=583:583)_, no term id was found for the name/label _costal region bone_.

1. In row _[583](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=583:583)_, no term id was found for the name/label _non-articular facet of tubercle of fourth rib_.

1. In row _[584](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=584:584)_, no term id was found for the name/label _costal region bone_.

1. In row _[584](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=584:584)_, no term id was found for the name/label _sternal end of fourth rib_.

1. In row _[585](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=585:585)_, no term id was found for the name/label _costal region bone_.

1. In row _[585](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=585:585)_, no term id was found for the name/label _superior articular facet of fourth rib_.

1. In row _[586](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=586:586)_, no term id was found for the name/label _costal region bone_.

1. In row _[586](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=586:586)_, no term id was found for the name/label _tubercle of fourth rib_.

1. In row _[587](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=587:587)_, no term id was found for the name/label _costal region bone_.

1. In row _[588](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=588:588)_, no term id was found for the name/label _costal region bone_.

1. In row _[588](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=588:588)_, no term id was found for the name/label _angle of fifth rib_.

1. In row _[589](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=589:589)_, no term id was found for the name/label _costal region bone_.

1. In row _[589](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=589:589)_, no term id was found for the name/label _articular facet of tubercle of fifth rib_.

1. In row _[590](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=590:590)_, no term id was found for the name/label _costal region bone_.

1. In row _[590](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=590:590)_, no term id was found for the name/label _body of fifth rib_.

1. In row _[591](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=591:591)_, no term id was found for the name/label _costal region bone_.

1. In row _[591](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=591:591)_, no term id was found for the name/label _costal groove of fifth rib_.

1. In row _[592](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=592:592)_, no term id was found for the name/label _costal region bone_.

1. In row _[592](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=592:592)_, no term id was found for the name/label _crest of head of fifth rib_.

1. In row _[593](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=593:593)_, no term id was found for the name/label _costal region bone_.

1. In row _[593](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=593:593)_, no term id was found for the name/label _head of fifth rib_.

1. In row _[594](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=594:594)_, no term id was found for the name/label _costal region bone_.

1. In row _[594](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=594:594)_, no term id was found for the name/label _inferior articular facet of fifth rib_.

1. In row _[595](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=595:595)_, no term id was found for the name/label _costal region bone_.

1. In row _[595](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=595:595)_, no term id was found for the name/label _neck of fifth rib_.

1. In row _[596](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=596:596)_, no term id was found for the name/label _costal region bone_.

1. In row _[596](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=596:596)_, no term id was found for the name/label _non-articular facet of tubercle of fifth rib_.

1. In row _[597](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=597:597)_, no term id was found for the name/label _costal region bone_.

1. In row _[597](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=597:597)_, no term id was found for the name/label _sternal end of fifth rib_.

1. In row _[598](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=598:598)_, no term id was found for the name/label _costal region bone_.

1. In row _[598](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=598:598)_, no term id was found for the name/label _superior articular facet of fifth rib_.

1. In row _[599](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=599:599)_, no term id was found for the name/label _costal region bone_.

1. In row _[599](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=599:599)_, no term id was found for the name/label _tubercle of fifth rib_.

1. In row _[600](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=600:600)_, no term id was found for the name/label _costal region bone_.

1. In row _[601](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=601:601)_, no term id was found for the name/label _costal region bone_.

1. In row _[601](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=601:601)_, no term id was found for the name/label _angle of sixth rib_.

1. In row _[602](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=602:602)_, no term id was found for the name/label _costal region bone_.

1. In row _[602](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=602:602)_, no term id was found for the name/label _articular facet of tubercle of sixth rib_.

1. In row _[603](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=603:603)_, no term id was found for the name/label _costal region bone_.

1. In row _[603](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=603:603)_, no term id was found for the name/label _body of sixth rib_.

1. In row _[604](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=604:604)_, no term id was found for the name/label _costal region bone_.

1. In row _[604](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=604:604)_, no term id was found for the name/label _costal groove of sixth rib_.

1. In row _[605](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=605:605)_, no term id was found for the name/label _costal region bone_.

1. In row _[605](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=605:605)_, no term id was found for the name/label _crest of head of sixth rib_.

1. In row _[606](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=606:606)_, no term id was found for the name/label _costal region bone_.

1. In row _[606](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=606:606)_, no term id was found for the name/label _head of sixth rib_.

1. In row _[607](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=607:607)_, no term id was found for the name/label _costal region bone_.

1. In row _[607](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=607:607)_, no term id was found for the name/label _inferior articular facet of sixth rib_.

1. In row _[608](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=608:608)_, no term id was found for the name/label _costal region bone_.

1. In row _[608](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=608:608)_, no term id was found for the name/label _neck of sixth rib_.

1. In row _[609](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=609:609)_, no term id was found for the name/label _costal region bone_.

1. In row _[609](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=609:609)_, no term id was found for the name/label _non-articular facet of tubercle of sixth rib_.

1. In row _[610](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=610:610)_, no term id was found for the name/label _costal region bone_.

1. In row _[610](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=610:610)_, no term id was found for the name/label _sternal end of sixth rib_.

1. In row _[611](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=611:611)_, no term id was found for the name/label _costal region bone_.

1. In row _[611](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=611:611)_, no term id was found for the name/label _superior articular facet of sixth rib_.

1. In row _[612](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=612:612)_, no term id was found for the name/label _costal region bone_.

1. In row _[612](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=612:612)_, no term id was found for the name/label _tubercle of sixth rib_.

1. In row _[613](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=613:613)_, no term id was found for the name/label _costal region bone_.

1. In row _[614](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=614:614)_, no term id was found for the name/label _costal region bone_.

1. In row _[614](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=614:614)_, no term id was found for the name/label _angle of seventh rib_.

1. In row _[615](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=615:615)_, no term id was found for the name/label _costal region bone_.

1. In row _[615](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=615:615)_, no term id was found for the name/label _articular facet of tubercle of seventh rib_.

1. In row _[616](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=616:616)_, no term id was found for the name/label _costal region bone_.

1. In row _[616](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=616:616)_, no term id was found for the name/label _body of seventh rib_.

1. In row _[617](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=617:617)_, no term id was found for the name/label _costal region bone_.

1. In row _[617](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=617:617)_, no term id was found for the name/label _costal groove of seventh rib_.

1. In row _[618](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=618:618)_, no term id was found for the name/label _costal region bone_.

1. In row _[618](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=618:618)_, no term id was found for the name/label _crest of head of seventh rib_.

1. In row _[619](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=619:619)_, no term id was found for the name/label _costal region bone_.

1. In row _[619](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=619:619)_, no term id was found for the name/label _head of seventh rib_.

1. In row _[620](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=620:620)_, no term id was found for the name/label _costal region bone_.

1. In row _[620](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=620:620)_, no term id was found for the name/label _inferior articular facet of seventh rib_.

1. In row _[621](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=621:621)_, no term id was found for the name/label _costal region bone_.

1. In row _[621](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=621:621)_, no term id was found for the name/label _neck of seventh rib_.

1. In row _[622](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=622:622)_, no term id was found for the name/label _costal region bone_.

1. In row _[622](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=622:622)_, no term id was found for the name/label _non-articular facet of tubercle of seventh rib_.

1. In row _[623](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=623:623)_, no term id was found for the name/label _costal region bone_.

1. In row _[623](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=623:623)_, no term id was found for the name/label _sternal end of seventh rib_.

1. In row _[624](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=624:624)_, no term id was found for the name/label _costal region bone_.

1. In row _[624](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=624:624)_, no term id was found for the name/label _superior articular facet of seventh rib_.

1. In row _[625](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=625:625)_, no term id was found for the name/label _costal region bone_.

1. In row _[625](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=625:625)_, no term id was found for the name/label _tubercle of seventh rib_.

1. In row _[626](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=626:626)_, no term id was found for the name/label _costal region bone_.

1. In row _[627](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=627:627)_, no term id was found for the name/label _costal region bone_.

1. In row _[627](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=627:627)_, no term id was found for the name/label _angle of eighth rib_.

1. In row _[628](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=628:628)_, no term id was found for the name/label _costal region bone_.

1. In row _[628](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=628:628)_, no term id was found for the name/label _articular facet of tubercle of eighth rib_.

1. In row _[629](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=629:629)_, no term id was found for the name/label _costal region bone_.

1. In row _[629](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=629:629)_, no term id was found for the name/label _body of eighth rib_.

1. In row _[630](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=630:630)_, no term id was found for the name/label _costal region bone_.

1. In row _[630](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=630:630)_, no term id was found for the name/label _costal groove of eighth rib_.

1. In row _[631](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=631:631)_, no term id was found for the name/label _costal region bone_.

1. In row _[631](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=631:631)_, no term id was found for the name/label _crest of head of eighth rib_.

1. In row _[632](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=632:632)_, no term id was found for the name/label _costal region bone_.

1. In row _[632](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=632:632)_, no term id was found for the name/label _head of eighth rib_.

1. In row _[633](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=633:633)_, no term id was found for the name/label _costal region bone_.

1. In row _[633](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=633:633)_, no term id was found for the name/label _inferior articular facet of eighth rib_.

1. In row _[634](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=634:634)_, no term id was found for the name/label _costal region bone_.

1. In row _[634](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=634:634)_, no term id was found for the name/label _neck of eighth rib_.

1. In row _[635](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=635:635)_, no term id was found for the name/label _costal region bone_.

1. In row _[635](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=635:635)_, no term id was found for the name/label _non-articular facet of tubercle of eighth rib_.

1. In row _[636](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=636:636)_, no term id was found for the name/label _costal region bone_.

1. In row _[636](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=636:636)_, no term id was found for the name/label _sternal end of eighth rib_.

1. In row _[637](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=637:637)_, no term id was found for the name/label _costal region bone_.

1. In row _[637](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=637:637)_, no term id was found for the name/label _superior articular facet of eighth rib_.

1. In row _[638](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=638:638)_, no term id was found for the name/label _costal region bone_.

1. In row _[638](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=638:638)_, no term id was found for the name/label _tubercle of eighth rib_.

1. In row _[639](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=639:639)_, no term id was found for the name/label _costal region bone_.

1. In row _[640](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=640:640)_, no term id was found for the name/label _costal region bone_.

1. In row _[640](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=640:640)_, no term id was found for the name/label _angle of ninth rib_.

1. In row _[641](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=641:641)_, no term id was found for the name/label _costal region bone_.

1. In row _[641](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=641:641)_, no term id was found for the name/label _articular facet of tubercle of ninth rib_.

1. In row _[642](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=642:642)_, no term id was found for the name/label _costal region bone_.

1. In row _[642](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=642:642)_, no term id was found for the name/label _body of ninth rib_.

1. In row _[643](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=643:643)_, no term id was found for the name/label _costal region bone_.

1. In row _[643](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=643:643)_, no term id was found for the name/label _costal groove of ninth rib_.

1. In row _[644](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=644:644)_, no term id was found for the name/label _costal region bone_.

1. In row _[644](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=644:644)_, no term id was found for the name/label _crest of head of ninth rib_.

1. In row _[645](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=645:645)_, no term id was found for the name/label _costal region bone_.

1. In row _[645](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=645:645)_, no term id was found for the name/label _head of ninth rib_.

1. In row _[646](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=646:646)_, no term id was found for the name/label _costal region bone_.

1. In row _[646](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=646:646)_, no term id was found for the name/label _inferior articular facet of ninth rib_.

1. In row _[647](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=647:647)_, no term id was found for the name/label _costal region bone_.

1. In row _[647](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=647:647)_, no term id was found for the name/label _neck of ninth rib_.

1. In row _[648](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=648:648)_, no term id was found for the name/label _costal region bone_.

1. In row _[648](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=648:648)_, no term id was found for the name/label _non-articular facet of tubercle of ninth rib_.

1. In row _[649](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=649:649)_, no term id was found for the name/label _costal region bone_.

1. In row _[649](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=649:649)_, no term id was found for the name/label _sternal end of ninth rib_.

1. In row _[650](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=650:650)_, no term id was found for the name/label _costal region bone_.

1. In row _[650](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=650:650)_, no term id was found for the name/label _superior articular facet of ninth rib_.

1. In row _[651](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=651:651)_, no term id was found for the name/label _costal region bone_.

1. In row _[651](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=651:651)_, no term id was found for the name/label _tubercle of ninth rib_.

1. In row _[652](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=652:652)_, no term id was found for the name/label _sternal region bone_.

1. In row _[653](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=653:653)_, no term id was found for the name/label _sternal region bone_.

1. In row _[654](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=654:654)_, no term id was found for the name/label _sternal region bone_.

1. In row _[654](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=654:654)_, no term id was found for the name/label _clavicular notch of sternum_.

1. In row _[655](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=655:655)_, no term id was found for the name/label _sternal region bone_.

1. In row _[655](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=655:655)_, no term id was found for the name/label _costal notches of sternum_.

1. In row _[656](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=656:656)_, no term id was found for the name/label _sternal region bone_.

1. In row _[656](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=656:656)_, no term id was found for the name/label _jugular notch of sternum_.

1. In row _[657](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=657:657)_, no term id was found for the name/label _sternal region bone_.

1. In row _[658](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=658:658)_, no term id was found for the name/label _sternal region bone_.

1. In row _[658](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=658:658)_, no term id was found for the name/label _sternal angle of sternum_.

1. In row _[659](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=659:659)_, no term id was found for the name/label _sternal region bone_.

1. In row _[659](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=659:659)_, no term id was found for the name/label _sternal body of sternum_.

1. In row _[660](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=660:660)_, no term id was found for the name/label _sternal region bone_.

1. In row _[660](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=660:660)_, no term id was found for the name/label _transverse ridges of sternum_.

1. In row _[661](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=661:661)_, no term id was found for the name/label _sternal region bone_.

1. In row _[661](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=661:661)_, no term id was found for the name/label _xiphoid process of sternum_.

1. In row _[665](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=665:665)_, no term id was found for the name/label _coccygeal cornu of coccyx_.

1. In row _[666](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=666:666)_, no term id was found for the name/label _transverse process of coccyx_.

1. In row _[669](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=669:669)_, no term id was found for the name/label _anterior arch of first cervical vertebra_.

1. In row _[670](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=670:670)_, no term id was found for the name/label _anterior tubercle of first cervical vertebra_.

1. In row _[671](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=671:671)_, no term id was found for the name/label _groove for vertebral artery of first cervical vertebra_.

1. In row _[672](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=672:672)_, no term id was found for the name/label _inferior articular facet of first cervical vertebra_.

1. In row _[673](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=673:673)_, no term id was found for the name/label _inferior articular process of first cervical vertebra_.

1. In row _[674](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=674:674)_, no term id was found for the name/label _inferior vertebral notch of first cervical vertebra_.

1. In row _[675](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=675:675)_, no term id was found for the name/label _lamina of first cervical vertebra_.

1. In row _[676](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=676:676)_, no term id was found for the name/label _pedicle of first cervical vertebra_.

1. In row _[677](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=677:677)_, no term id was found for the name/label _posterior arch of first cervical vertebra_.

1. In row _[678](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=678:678)_, no term id was found for the name/label _posterior tubercle of first cervical vertebra_.

1. In row _[679](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=679:679)_, no term id was found for the name/label _spinous process of first cervical vertebra_.

1. In row _[680](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=680:680)_, no term id was found for the name/label _superior articular facet of first cervical vertebra_.

1. In row _[681](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=681:681)_, no term id was found for the name/label _superior articular process of first cervical vertebra_.

1. In row _[682](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=682:682)_, no term id was found for the name/label _superior vertebral notch of first cervical vertebra_.

1. In row _[683](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=683:683)_, no term id was found for the name/label _transverse foramen of first cervical vertebra_.

1. In row _[684](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=684:684)_, no term id was found for the name/label _transverse process of first cervical vertebra_.

1. In row _[685](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=685:685)_, no term id was found for the name/label _vertebral body of first cervical vertebra_.

1. In row _[686](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=686:686)_, no term id was found for the name/label _vertebral foramen of first cervical vertebra_.

1. In row _[688](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=688:688)_, no term id was found for the name/label _body of second cervical vertebra_.

1. In row _[689](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=689:689)_, no term id was found for the name/label _inferior articular facet of second cervical vertebra_.

1. In row _[690](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=690:690)_, no term id was found for the name/label _inferior articular process of second cervical vertebra_.

1. In row _[691](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=691:691)_, no term id was found for the name/label _inferior vertebral notch of second cervical vertebra_.

1. In row _[692](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=692:692)_, no term id was found for the name/label _lamina of second cervical vertebra_.

1. In row _[694](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=694:694)_, no term id was found for the name/label _pedicle of second cervical vertebra_.

1. In row _[695](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=695:695)_, no term id was found for the name/label _spinous process of second cervical vertebra_.

1. In row _[696](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=696:696)_, no term id was found for the name/label _superior articular facet of second cervical vertebra_.

1. In row _[697](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=697:697)_, no term id was found for the name/label _superior articular process of second cervical vertebra_.

1. In row _[698](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=698:698)_, no term id was found for the name/label _superior vertebral notch of second cervical vertebra_.

1. In row _[699](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=699:699)_, no term id was found for the name/label _transverse foramen of second cervical vertebra_.

1. In row _[700](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=700:700)_, no term id was found for the name/label _transverse process of second cervical vertebra_.

1. In row _[701](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=701:701)_, no term id was found for the name/label _vertebral arch of second cervical vertebra_.

1. In row _[702](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=702:702)_, no term id was found for the name/label _vertebral body of second cervical vertebra_.

1. In row _[703](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=703:703)_, no term id was found for the name/label _vertebral foramen of second cervical vertebra_.

1. In row _[705](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=705:705)_, no term id was found for the name/label _inferior articular facet of third cervical vertebra_.

1. In row _[706](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=706:706)_, no term id was found for the name/label _inferior articular process of third cervical vertebra_.

1. In row _[707](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=707:707)_, no term id was found for the name/label _inferior vertebral notch of third cervical vertebra_.

1. In row _[708](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=708:708)_, no term id was found for the name/label _lamina of third cervical vertebra_.

1. In row _[709](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=709:709)_, no term id was found for the name/label _pedicle of third cervical vertebra_.

1. In row _[710](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=710:710)_, no term id was found for the name/label _spinous process of third cervical vertebra_.

1. In row _[711](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=711:711)_, no term id was found for the name/label _superior articular facet of third cervical vertebra_.

1. In row _[712](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=712:712)_, no term id was found for the name/label _superior articular process of third cervical vertebra_.

1. In row _[713](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=713:713)_, no term id was found for the name/label _superior vertebral notch of third cervical vertebra_.

1. In row _[714](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=714:714)_, no term id was found for the name/label _transverse foramen of third cervical vertebra_.

1. In row _[715](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=715:715)_, no term id was found for the name/label _transverse process of third cervical vertebra_.

1. In row _[716](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=716:716)_, no term id was found for the name/label _vertebral arch of third cervical vertebra_.

1. In row _[717](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=717:717)_, no term id was found for the name/label _vertebral body of third cervical vertebra_.

1. In row _[718](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=718:718)_, no term id was found for the name/label _vertebral foramen of third cervical vertebra_.

1. In row _[720](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=720:720)_, no term id was found for the name/label _inferior articular facet of fourth cervical vertebra_.

1. In row _[721](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=721:721)_, no term id was found for the name/label _inferior articular process of fourth cervical vertebra_.

1. In row _[722](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=722:722)_, no term id was found for the name/label _inferior vertebral notch of fourth cervical vertebra_.

1. In row _[723](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=723:723)_, no term id was found for the name/label _lamina of fourth cervical vertebra_.

1. In row _[724](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=724:724)_, no term id was found for the name/label _pedicle of fourth cervical vertebra_.

1. In row _[725](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=725:725)_, no term id was found for the name/label _spinous process of fourth cervical vertebra_.

1. In row _[726](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=726:726)_, no term id was found for the name/label _superior articular facet of fourth cervical vertebra_.

1. In row _[727](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=727:727)_, no term id was found for the name/label _superior articular process of fourth cervical vertebra_.

1. In row _[728](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=728:728)_, no term id was found for the name/label _superior vertebral notch of fourth cervical vertebra_.

1. In row _[729](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=729:729)_, no term id was found for the name/label _transverse foramen of fourth cervical vertebra_.

1. In row _[730](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=730:730)_, no term id was found for the name/label _transverse process of fourth cervical vertebra_.

1. In row _[731](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=731:731)_, no term id was found for the name/label _vertebral arch of fourth cervical vertebra_.

1. In row _[732](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=732:732)_, no term id was found for the name/label _vertebral body of fourth cervical vertebra_.

1. In row _[733](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=733:733)_, no term id was found for the name/label _vertebral foramen of fourth cervical vertebra_.

1. In row _[735](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=735:735)_, no term id was found for the name/label _inferior articular facet of fifth cervical vertebra_.

1. In row _[736](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=736:736)_, no term id was found for the name/label _inferior articular process of fifth cervical vertebra_.

1. In row _[737](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=737:737)_, no term id was found for the name/label _inferior vertebral notch of fifth cervical vertebra_.

1. In row _[738](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=738:738)_, no term id was found for the name/label _lamina of fifth cervical vertebra_.

1. In row _[739](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=739:739)_, no term id was found for the name/label _pedicle of fifth cervical vertebra_.

1. In row _[740](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=740:740)_, no term id was found for the name/label _spinous process of fifth cervical vertebra_.

1. In row _[741](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=741:741)_, no term id was found for the name/label _superior articular facet of fifth cervical vertebra_.

1. In row _[742](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=742:742)_, no term id was found for the name/label _superior articular process of fifth cervical vertebra_.

1. In row _[743](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=743:743)_, no term id was found for the name/label _superior vertebral notch of fifth cervical vertebra_.

1. In row _[744](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=744:744)_, no term id was found for the name/label _transverse foramen of fifth cervical vertebra_.

1. In row _[745](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=745:745)_, no term id was found for the name/label _transverse process of fifth cervical vertebra_.

1. In row _[746](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=746:746)_, no term id was found for the name/label _vertebral arch of fifth cervical vertebra_.

1. In row _[747](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=747:747)_, no term id was found for the name/label _vertebral body of fifth cervical vertebra_.

1. In row _[748](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=748:748)_, no term id was found for the name/label _vertebral foramen of fifth cervical vertebra_.

1. In row _[750](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=750:750)_, no term id was found for the name/label _inferior articular facet of sixth cervical vertebra_.

1. In row _[751](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=751:751)_, no term id was found for the name/label _inferior articular process of sixth cervical vertebra_.

1. In row _[752](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=752:752)_, no term id was found for the name/label _inferior vertebral notch of sixth cervical vertebra_.

1. In row _[753](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=753:753)_, no term id was found for the name/label _lamina of sixth cervical vertebra_.

1. In row _[754](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=754:754)_, no term id was found for the name/label _pedicle of sixth cervical vertebra_.

1. In row _[755](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=755:755)_, no term id was found for the name/label _spinous process of sixth cervical vertebra_.

1. In row _[756](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=756:756)_, no term id was found for the name/label _superior articular facet of sixth cervical vertebra_.

1. In row _[757](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=757:757)_, no term id was found for the name/label _superior articular process of sixth cervical vertebra_.

1. In row _[758](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=758:758)_, no term id was found for the name/label _superior vertebral notch of sixth cervical vertebra_.

1. In row _[759](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=759:759)_, no term id was found for the name/label _transverse foramen of sixth cervical vertebra_.

1. In row _[760](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=760:760)_, no term id was found for the name/label _transverse process of sixth cervical vertebra_.

1. In row _[761](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=761:761)_, no term id was found for the name/label _vertebral arch of sixth cervical vertebra_.

1. In row _[762](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=762:762)_, no term id was found for the name/label _vertebral body of sixth cervical vertebra_.

1. In row _[763](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=763:763)_, no term id was found for the name/label _vertebral foramen of sixth cervical vertebra_.

1. In row _[765](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=765:765)_, no term id was found for the name/label _inferior articular facet of seventh cervical vertebra_.

1. In row _[766](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=766:766)_, no term id was found for the name/label _inferior articular process of seventh cervical vertebra_.

1. In row _[767](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=767:767)_, no term id was found for the name/label _inferior vertebral notch of seventh cervical vertebra_.

1. In row _[768](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=768:768)_, no term id was found for the name/label _lamina of seventh cervical vertebra_.

1. In row _[769](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=769:769)_, no term id was found for the name/label _pedicle of seventh cervical vertebra_.

1. In row _[770](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=770:770)_, no term id was found for the name/label _spinous process of seventh cervical vertebra_.

1. In row _[771](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=771:771)_, no term id was found for the name/label _superior articular facet of seventh cervical vertebra_.

1. In row _[772](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=772:772)_, no term id was found for the name/label _superior articular process of seventh cervical vertebra_.

1. In row _[773](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=773:773)_, no term id was found for the name/label _superior vertebral notch of seventh cervical vertebra_.

1. In row _[774](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=774:774)_, no term id was found for the name/label _transverse foramen of seventh cervical vertebra_.

1. In row _[775](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=775:775)_, no term id was found for the name/label _transverse process of seventh cervical vertebra_.

1. In row _[776](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=776:776)_, no term id was found for the name/label _vertebra prominens of seventh cervical vertebra_.

1. In row _[777](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=777:777)_, no term id was found for the name/label _vertebral arch of seventh cervical vertebra_.

1. In row _[778](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=778:778)_, no term id was found for the name/label _vertebral body of seventh cervical vertebra_.

1. In row _[779](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=779:779)_, no term id was found for the name/label _vertebral foramen of seventh cervical vertebra_.

1. In row _[782](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=782:782)_, no term id was found for the name/label _accessory process of first lumbar vertebra_.

1. In row _[783](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=783:783)_, no term id was found for the name/label _inferior articular facet of first lumbar vertebra_.

1. In row _[784](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=784:784)_, no term id was found for the name/label _inferior articular process of first lumbar vertebra_.

1. In row _[785](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=785:785)_, no term id was found for the name/label _inferior vertebral notch of first lumbar vertebra_.

1. In row _[786](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=786:786)_, no term id was found for the name/label _lamina of first lumbar vertebra_.

1. In row _[787](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=787:787)_, no term id was found for the name/label _mammillary process of first lumbar vertebra_.

1. In row _[788](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=788:788)_, no term id was found for the name/label _pedicle of first lumbar vertebra_.

1. In row _[789](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=789:789)_, no term id was found for the name/label _spinous process of first lumbar vertebra_.

1. In row _[790](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=790:790)_, no term id was found for the name/label _superior articular facet of first lumbar vertebra_.

1. In row _[791](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=791:791)_, no term id was found for the name/label _superior articular process of first lumbar vertebra_.

1. In row _[792](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=792:792)_, no term id was found for the name/label _superior vertebral notch of first lumbar vertebra_.

1. In row _[793](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=793:793)_, no term id was found for the name/label _transverse process of first lumbar vertebra_.

1. In row _[794](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=794:794)_, no term id was found for the name/label _vertebral arch of first lumbar vertebra_.

1. In row _[795](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=795:795)_, no term id was found for the name/label _vertebral body of first lumbar vertebra_.

1. In row _[796](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=796:796)_, no term id was found for the name/label _vertebral foramen of first lumbar vertebra_.

1. In row _[798](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=798:798)_, no term id was found for the name/label _accessory process of second lumbar vertebra_.

1. In row _[799](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=799:799)_, no term id was found for the name/label _inferior articular facet of second lumbar vertebra_.

1. In row _[800](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=800:800)_, no term id was found for the name/label _inferior articular process of second lumbar vertebra_.

1. In row _[801](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=801:801)_, no term id was found for the name/label _inferior vertebral notch of second lumbar vertebra_.

1. In row _[802](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=802:802)_, no term id was found for the name/label _lamina of second lumbar vertebra_.

1. In row _[803](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=803:803)_, no term id was found for the name/label _mammillary process of second lumbar vertebra_.

1. In row _[804](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=804:804)_, no term id was found for the name/label _pedicle of second lumbar vertebra_.

1. In row _[805](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=805:805)_, no term id was found for the name/label _spinous process of second lumbar vertebra_.

1. In row _[806](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=806:806)_, no term id was found for the name/label _superior articular facet of second lumbar vertebra_.

1. In row _[807](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=807:807)_, no term id was found for the name/label _superior articular process of second lumbar vertebra_.

1. In row _[808](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=808:808)_, no term id was found for the name/label _superior vertebral notch of second lumbar vertebra_.

1. In row _[809](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=809:809)_, no term id was found for the name/label _transverse process of second lumbar vertebra_.

1. In row _[810](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=810:810)_, no term id was found for the name/label _vertebral arch of second lumbar vertebra_.

1. In row _[811](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=811:811)_, no term id was found for the name/label _vertebral body of second lumbar vertebra_.

1. In row _[812](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=812:812)_, no term id was found for the name/label _vertebral foramen of second lumbar vertebra_.

1. In row _[814](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=814:814)_, no term id was found for the name/label _accessory process of third lumbar vertebra_.

1. In row _[815](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=815:815)_, no term id was found for the name/label _inferior articular facet of third lumbar vertebra_.

1. In row _[816](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=816:816)_, no term id was found for the name/label _inferior articular process of third lumbar vertebra_.

1. In row _[817](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=817:817)_, no term id was found for the name/label _inferior vertebral notch of third lumbar vertebra_.

1. In row _[818](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=818:818)_, no term id was found for the name/label _lamina of third lumbar vertebra_.

1. In row _[819](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=819:819)_, no term id was found for the name/label _mammillary process of third lumbar vertebra_.

1. In row _[820](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=820:820)_, no term id was found for the name/label _pedicle of third lumbar vertebra_.

1. In row _[821](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=821:821)_, no term id was found for the name/label _spinous process of third lumbar vertebra_.

1. In row _[822](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=822:822)_, no term id was found for the name/label _superior articular facet of third lumbar vertebra_.

1. In row _[823](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=823:823)_, no term id was found for the name/label _superior articular process of third lumbar vertebra_.

1. In row _[824](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=824:824)_, no term id was found for the name/label _superior vertebral notch of third lumbar vertebra_.

1. In row _[825](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=825:825)_, no term id was found for the name/label _transverse process of third lumbar vertebra_.

1. In row _[826](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=826:826)_, no term id was found for the name/label _vertebral arch of third lumbar vertebra_.

1. In row _[827](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=827:827)_, no term id was found for the name/label _vertebral body of third lumbar vertebra_.

1. In row _[828](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=828:828)_, no term id was found for the name/label _vertebral foramen of third lumbar vertebra_.

1. In row _[830](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=830:830)_, no term id was found for the name/label _accessory process of fourth lumbar vertebra_.

1. In row _[831](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=831:831)_, no term id was found for the name/label _inferior articular facet of fourth lumbar vertebra_.

1. In row _[832](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=832:832)_, no term id was found for the name/label _inferior articular process of fourth lumbar vertebra_.

1. In row _[833](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=833:833)_, no term id was found for the name/label _inferior vertebral notch of fourth lumbar vertebra_.

1. In row _[834](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=834:834)_, no term id was found for the name/label _lamina of fourth lumbar vertebra_.

1. In row _[835](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=835:835)_, no term id was found for the name/label _mammillary process of fourth lumbar vertebra_.

1. In row _[836](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=836:836)_, no term id was found for the name/label _pedicle of fourth lumbar vertebra_.

1. In row _[837](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=837:837)_, no term id was found for the name/label _spinous process of fourth lumbar vertebra_.

1. In row _[838](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=838:838)_, no term id was found for the name/label _superior articular facet of fourth lumbar vertebra_.

1. In row _[839](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=839:839)_, no term id was found for the name/label _superior articular process of fourth lumbar vertebra_.

1. In row _[840](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=840:840)_, no term id was found for the name/label _superior vertebral notch of fourth lumbar vertebra_.

1. In row _[841](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=841:841)_, no term id was found for the name/label _transverse process of fourth lumbar vertebra_.

1. In row _[842](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=842:842)_, no term id was found for the name/label _vertebral arch of fourth lumbar vertebra_.

1. In row _[843](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=843:843)_, no term id was found for the name/label _vertebral body of fourth lumbar vertebra_.

1. In row _[844](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=844:844)_, no term id was found for the name/label _vertebral foramen of fourth lumbar vertebra_.

1. In row _[846](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=846:846)_, no term id was found for the name/label _accessory process of fifth lumbar vertebra_.

1. In row _[847](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=847:847)_, no term id was found for the name/label _inferior articular facet of fifth lumbar vertebra_.

1. In row _[848](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=848:848)_, no term id was found for the name/label _inferior articular process of fifth lumbar vertebra_.

1. In row _[849](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=849:849)_, no term id was found for the name/label _inferior vertebral notch of fifth lumbar vertebra_.

1. In row _[850](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=850:850)_, no term id was found for the name/label _lamina of fifth lumbar vertebra_.

1. In row _[851](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=851:851)_, no term id was found for the name/label _mammillary process of fifth lumbar vertebra_.

1. In row _[852](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=852:852)_, no term id was found for the name/label _pedicle of fifth lumbar vertebra_.

1. In row _[853](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=853:853)_, no term id was found for the name/label _spinous process of fifth lumbar vertebra_.

1. In row _[854](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=854:854)_, no term id was found for the name/label _superior articular facet of fifth lumbar vertebra_.

1. In row _[855](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=855:855)_, no term id was found for the name/label _superior articular process of fifth lumbar vertebra_.

1. In row _[856](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=856:856)_, no term id was found for the name/label _superior vertebral notch of fifth lumbar vertebra_.

1. In row _[857](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=857:857)_, no term id was found for the name/label _transverse process of fifth lumbar vertebra_.

1. In row _[858](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=858:858)_, no term id was found for the name/label _vertebral arch of fifth lumbar vertebra_.

1. In row _[859](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=859:859)_, no term id was found for the name/label _vertebral body of fifth lumbar vertebra_.

1. In row _[860](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=860:860)_, no term id was found for the name/label _vertebral foramen of fifth lumbar vertebra_.

1. In row _[863](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=863:863)_, no term id was found for the name/label _alae of sacrum_.

1. In row _[864](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=864:864)_, no term id was found for the name/label _anterior sacral foramina of sacrum_.

1. In row _[865](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=865:865)_, no term id was found for the name/label _auricular surface of sacrum_.

1. In row _[866](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=866:866)_, no term id was found for the name/label _intermediate sacral crest of sacrum_.

1. In row _[867](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=867:867)_, no term id was found for the name/label _lateral sacral crest of sacrum_.

1. In row _[868](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=868:868)_, no term id was found for the name/label _linea terminalis of sacrum_.

1. In row _[869](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=869:869)_, no term id was found for the name/label _median sacral crest of sacrum_.

1. In row _[870](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=870:870)_, no term id was found for the name/label _posterior sacral foramina of sacrum_.

1. In row _[871](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=871:871)_, no term id was found for the name/label _sacral apex of sacrum_.

1. In row _[872](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=872:872)_, no term id was found for the name/label _sacral canal of sacrum_.

1. In row _[873](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=873:873)_, no term id was found for the name/label _sacral cornu of sacrum_.

1. In row _[874](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=874:874)_, no term id was found for the name/label _sacral hiatus of sacrum_.

1. In row _[875](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=875:875)_, no term id was found for the name/label _sacral promontory of sacrum_.

1. In row _[876](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=876:876)_, no term id was found for the name/label _sacral spine of sacrum_.

1. In row _[877](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=877:877)_, no term id was found for the name/label _sacral tuberosity of sacrum_.

1. In row _[878](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=878:878)_, no term id was found for the name/label _superior articular facet of sacrum_.

1. In row _[879](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=879:879)_, no term id was found for the name/label _superior articular process of sacrum_.

1. In row _[880](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=880:880)_, no term id was found for the name/label _transverse ridges of sacrum_.

1. In row _[883](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=883:883)_, no term id was found for the name/label _inferior articular facet of first thoracic vertebra_.

1. In row _[884](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=884:884)_, no term id was found for the name/label _inferior articular process of first thoracic vertebra_.

1. In row _[885](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=885:885)_, no term id was found for the name/label _inferior costal facet of first thoracic vertebra_.

1. In row _[886](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=886:886)_, no term id was found for the name/label _inferior vertebral notch of first thoracic vertebra_.

1. In row _[887](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=887:887)_, no term id was found for the name/label _lamina of first thoracic vertebra_.

1. In row _[888](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=888:888)_, no term id was found for the name/label _pedicle of first thoracic vertebra_.

1. In row _[889](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=889:889)_, no term id was found for the name/label _spinous process of first thoracic vertebra_.

1. In row _[890](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=890:890)_, no term id was found for the name/label _superior articular facet of first thoracic vertebra_.

1. In row _[891](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=891:891)_, no term id was found for the name/label _superior articular process of first thoracic vertebra_.

1. In row _[892](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=892:892)_, no term id was found for the name/label _superior costal facet of first thoracic vertebra_.

1. In row _[893](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=893:893)_, no term id was found for the name/label _superior vertebral notch of first thoracic vertebra_.

1. In row _[894](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=894:894)_, no term id was found for the name/label _transverse costal facet of first thoracic vertebra_.

1. In row _[895](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=895:895)_, no term id was found for the name/label _transverse process of first thoracic vertebra_.

1. In row _[896](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=896:896)_, no term id was found for the name/label _vertebral arch of first thoracic vertebra_.

1. In row _[897](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=897:897)_, no term id was found for the name/label _vertebral body of first thoracic vertebra_.

1. In row _[898](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=898:898)_, no term id was found for the name/label _vertebral foramen of first thoracic vertebra_.

1. In row _[900](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=900:900)_, no term id was found for the name/label _inferior articular facet of tenth thoracic vertebra_.

1. In row _[901](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=901:901)_, no term id was found for the name/label _inferior articular process of tenth thoracic vertebra_.

1. In row _[902](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=902:902)_, no term id was found for the name/label _inferior costal facet of tenth thoracic vertebra_.

1. In row _[903](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=903:903)_, no term id was found for the name/label _inferior vertebral notch of tenth thoracic vertebra_.

1. In row _[904](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=904:904)_, no term id was found for the name/label _lamina of tenth thoracic vertebra_.

1. In row _[905](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=905:905)_, no term id was found for the name/label _pedicle of tenth thoracic vertebra_.

1. In row _[906](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=906:906)_, no term id was found for the name/label _spinous process of tenth thoracic vertebra_.

1. In row _[907](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=907:907)_, no term id was found for the name/label _superior articular facet of tenth thoracic vertebra_.

1. In row _[908](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=908:908)_, no term id was found for the name/label _superior articular process of tenth thoracic vertebra_.

1. In row _[909](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=909:909)_, no term id was found for the name/label _superior costal facet of tenth thoracic vertebra_.

1. In row _[910](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=910:910)_, no term id was found for the name/label _superior vertebral notch of tenth thoracic vertebra_.

1. In row _[911](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=911:911)_, no term id was found for the name/label _transverse costal facet of tenth thoracic vertebra_.

1. In row _[912](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=912:912)_, no term id was found for the name/label _transverse process of tenth thoracic vertebra_.

1. In row _[913](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=913:913)_, no term id was found for the name/label _vertebral arch of tenth thoracic vertebra_.

1. In row _[914](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=914:914)_, no term id was found for the name/label _vertebral body of tenth thoracic vertebra_.

1. In row _[915](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=915:915)_, no term id was found for the name/label _vertebral foramen of tenth thoracic vertebra_.

1. In row _[917](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=917:917)_, no term id was found for the name/label _inferior articular facet of eleventh thoracic vertebra_.

1. In row _[918](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=918:918)_, no term id was found for the name/label _inferior articular process of eleventh thoracic vertebra_.

1. In row _[919](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=919:919)_, no term id was found for the name/label _inferior costal facet of eleventh thoracic vertebra_.

1. In row _[920](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=920:920)_, no term id was found for the name/label _inferior vertebral notch of eleventh thoracic vertebra_.

1. In row _[921](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=921:921)_, no term id was found for the name/label _lamina of eleventh thoracic vertebra_.

1. In row _[922](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=922:922)_, no term id was found for the name/label _pedicle of eleventh thoracic vertebra_.

1. In row _[923](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=923:923)_, no term id was found for the name/label _spinous process of eleventh thoracic vertebra_.

1. In row _[924](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=924:924)_, no term id was found for the name/label _superior articular facet of eleventh thoracic vertebra_.

1. In row _[925](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=925:925)_, no term id was found for the name/label _superior articular process of eleventh thoracic vertebra_.

1. In row _[926](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=926:926)_, no term id was found for the name/label _superior costal facet of eleventh thoracic vertebra_.

1. In row _[927](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=927:927)_, no term id was found for the name/label _superior vertebral notch of eleventh thoracic vertebra_.

1. In row _[928](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=928:928)_, no term id was found for the name/label _transverse costal facet of eleventh thoracic vertebra_.

1. In row _[929](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=929:929)_, no term id was found for the name/label _transverse process of eleventh thoracic vertebra_.

1. In row _[930](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=930:930)_, no term id was found for the name/label _vertebral arch of eleventh thoracic vertebra_.

1. In row _[931](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=931:931)_, no term id was found for the name/label _vertebral body of eleventh thoracic vertebra_.

1. In row _[932](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=932:932)_, no term id was found for the name/label _vertebral foramen of eleventh thoracic vertebra_.

1. In row _[934](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=934:934)_, no term id was found for the name/label _costal facet of twelfth thoracic vertebra_.

1. In row _[935](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=935:935)_, no term id was found for the name/label _inferior articular facet of twelfth thoracic vertebra_.

1. In row _[936](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=936:936)_, no term id was found for the name/label _inferior articular process of twelfth thoracic vertebra_.

1. In row _[937](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=937:937)_, no term id was found for the name/label _inferior vertebral notch of twelfth thoracic vertebra_.

1. In row _[938](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=938:938)_, no term id was found for the name/label _lamina of twelfth thoracic vertebra_.

1. In row _[939](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=939:939)_, no term id was found for the name/label _pedicle of twelfth thoracic vertebra_.

1. In row _[940](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=940:940)_, no term id was found for the name/label _spinous process of twelfth thoracic vertebra_.

1. In row _[941](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=941:941)_, no term id was found for the name/label _superior articular facet of twelfth thoracic vertebra_.

1. In row _[942](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=942:942)_, no term id was found for the name/label _superior articular process of twelfth thoracic vertebra_.

1. In row _[943](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=943:943)_, no term id was found for the name/label _superior vertebral notch of twelfth thoracic vertebra_.

1. In row _[944](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=944:944)_, no term id was found for the name/label _transverse process of twelfth thoracic vertebra_.

1. In row _[945](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=945:945)_, no term id was found for the name/label _vertebral arch of twelfth thoracic vertebra_.

1. In row _[946](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=946:946)_, no term id was found for the name/label _vertebral body of twelfth thoracic vertebra_.

1. In row _[947](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=947:947)_, no term id was found for the name/label _vertebral foramen of twelfth thoracic vertebra_.

1. In row _[949](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=949:949)_, no term id was found for the name/label _inferior articular facet of second thoracic vertebra_.

1. In row _[950](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=950:950)_, no term id was found for the name/label _inferior articular process of second thoracic vertebra_.

1. In row _[951](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=951:951)_, no term id was found for the name/label _inferior costal facet of second thoracic vertebra_.

1. In row _[952](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=952:952)_, no term id was found for the name/label _inferior vertebral notch of second thoracic vertebra_.

1. In row _[953](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=953:953)_, no term id was found for the name/label _lamina of second thoracic vertebra_.

1. In row _[954](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=954:954)_, no term id was found for the name/label _pedicle of second thoracic vertebra_.

1. In row _[955](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=955:955)_, no term id was found for the name/label _spinous process of second thoracic vertebra_.

1. In row _[956](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=956:956)_, no term id was found for the name/label _superior articular facet of second thoracic vertebra_.

1. In row _[957](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=957:957)_, no term id was found for the name/label _superior articular process of second thoracic vertebra_.

1. In row _[958](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=958:958)_, no term id was found for the name/label _superior costal facet of second thoracic vertebra_.

1. In row _[959](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=959:959)_, no term id was found for the name/label _superior vertebral notch of second thoracic vertebra_.

1. In row _[960](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=960:960)_, no term id was found for the name/label _transverse costal facet of second thoracic vertebra_.

1. In row _[961](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=961:961)_, no term id was found for the name/label _transverse process of second thoracic vertebra_.

1. In row _[962](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=962:962)_, no term id was found for the name/label _vertebral arch of second thoracic vertebra_.

1. In row _[963](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=963:963)_, no term id was found for the name/label _vertebral body of second thoracic vertebra_.

1. In row _[964](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=964:964)_, no term id was found for the name/label _vertebral foramen of second thoracic vertebra_.

1. In row _[966](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=966:966)_, no term id was found for the name/label _inferior articular facet of third thoracic vertebra_.

1. In row _[967](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=967:967)_, no term id was found for the name/label _inferior articular process of third thoracic vertebra_.

1. In row _[968](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=968:968)_, no term id was found for the name/label _inferior costal facet of third thoracic vertebra_.

1. In row _[969](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=969:969)_, no term id was found for the name/label _inferior vertebral notch of third thoracic vertebra_.

1. In row _[970](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=970:970)_, no term id was found for the name/label _lamina of third thoracic vertebra_.

1. In row _[971](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=971:971)_, no term id was found for the name/label _pedicle of third thoracic vertebra_.

1. In row _[972](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=972:972)_, no term id was found for the name/label _spinous process of third thoracic vertebra_.

1. In row _[973](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=973:973)_, no term id was found for the name/label _superior articular facet of third thoracic vertebra_.

1. In row _[974](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=974:974)_, no term id was found for the name/label _superior articular process of third thoracic vertebra_.

1. In row _[975](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=975:975)_, no term id was found for the name/label _superior costal facet of third thoracic vertebra_.

1. In row _[976](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=976:976)_, no term id was found for the name/label _superior vertebral notch of third thoracic vertebra_.

1. In row _[977](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=977:977)_, no term id was found for the name/label _transverse costal facet of third thoracic vertebra_.

1. In row _[978](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=978:978)_, no term id was found for the name/label _transverse process of third thoracic vertebra_.

1. In row _[979](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=979:979)_, no term id was found for the name/label _vertebral arch of third thoracic vertebra_.

1. In row _[980](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=980:980)_, no term id was found for the name/label _vertebral body of third thoracic vertebra_.

1. In row _[981](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=981:981)_, no term id was found for the name/label _vertebral foramen of third thoracic vertebra_.

1. In row _[983](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=983:983)_, no term id was found for the name/label _inferior articular facet of fourth thoracic vertebra_.

1. In row _[984](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=984:984)_, no term id was found for the name/label _inferior articular process of fourth thoracic vertebra_.

1. In row _[985](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=985:985)_, no term id was found for the name/label _inferior costal facet of fourth thoracic vertebra_.

1. In row _[986](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=986:986)_, no term id was found for the name/label _inferior vertebral notch of fourth thoracic vertebra_.

1. In row _[987](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=987:987)_, no term id was found for the name/label _lamina of fourth thoracic vertebra_.

1. In row _[988](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=988:988)_, no term id was found for the name/label _pedicle of fourth thoracic vertebra_.

1. In row _[989](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=989:989)_, no term id was found for the name/label _spinous process of fourth thoracic vertebra_.

1. In row _[990](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=990:990)_, no term id was found for the name/label _superior articular facet of fourth thoracic vertebra_.

1. In row _[991](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=991:991)_, no term id was found for the name/label _superior articular process of fourth thoracic vertebra_.

1. In row _[992](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=992:992)_, no term id was found for the name/label _superior costal facet of fourth thoracic vertebra_.

1. In row _[993](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=993:993)_, no term id was found for the name/label _superior vertebral notch of fourth thoracic vertebra_.

1. In row _[994](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=994:994)_, no term id was found for the name/label _transverse costal facet of fourth thoracic vertebra_.

1. In row _[995](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=995:995)_, no term id was found for the name/label _transverse process of fourth thoracic vertebra_.

1. In row _[996](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=996:996)_, no term id was found for the name/label _vertebral arch of fourth thoracic vertebra_.

1. In row _[997](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=997:997)_, no term id was found for the name/label _vertebral body of fourth thoracic vertebra_.

1. In row _[998](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=998:998)_, no term id was found for the name/label _vertebral foramen of fourth thoracic vertebra_.

1. In row _[1000](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1000:1000)_, no term id was found for the name/label _inferior articular facet of fifth thoracic vertebra_.

1. In row _[1001](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1001:1001)_, no term id was found for the name/label _inferior articular process of fifth thoracic vertebra_.

1. In row _[1002](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1002:1002)_, no term id was found for the name/label _inferior costal facet of fifth thoracic vertebra_.

1. In row _[1003](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1003:1003)_, no term id was found for the name/label _inferior vertebral notch of fifth thoracic vertebra_.

1. In row _[1004](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1004:1004)_, no term id was found for the name/label _lamina of fifth thoracic vertebra_.

1. In row _[1005](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1005:1005)_, no term id was found for the name/label _pedicle of fifth thoracic vertebra_.

1. In row _[1006](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1006:1006)_, no term id was found for the name/label _spinous process of fifth thoracic vertebra_.

1. In row _[1007](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1007:1007)_, no term id was found for the name/label _superior articular facet of fifth thoracic vertebra_.

1. In row _[1008](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1008:1008)_, no term id was found for the name/label _superior articular process of fifth thoracic vertebra_.

1. In row _[1009](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1009:1009)_, no term id was found for the name/label _superior costal facet of fifth thoracic vertebra_.

1. In row _[1010](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1010:1010)_, no term id was found for the name/label _superior vertebral notch of fifth thoracic vertebra_.

1. In row _[1011](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1011:1011)_, no term id was found for the name/label _transverse costal facet of fifth thoracic vertebra_.

1. In row _[1012](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1012:1012)_, no term id was found for the name/label _transverse process of fifth thoracic vertebra_.

1. In row _[1013](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1013:1013)_, no term id was found for the name/label _vertebral arch of fifth thoracic vertebra_.

1. In row _[1014](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1014:1014)_, no term id was found for the name/label _vertebral body of fifth thoracic vertebra_.

1. In row _[1015](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1015:1015)_, no term id was found for the name/label _vertebral foramen of fifth thoracic vertebra_.

1. In row _[1017](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1017:1017)_, no term id was found for the name/label _inferior articular facet of sixth thoracic vertebra_.

1. In row _[1018](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1018:1018)_, no term id was found for the name/label _inferior articular process of sixth thoracic vertebra_.

1. In row _[1019](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1019:1019)_, no term id was found for the name/label _inferior costal facet of sixth thoracic vertebra_.

1. In row _[1020](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1020:1020)_, no term id was found for the name/label _inferior vertebral notch of sixth thoracic vertebra_.

1. In row _[1021](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1021:1021)_, no term id was found for the name/label _lamina of sixth thoracic vertebra_.

1. In row _[1022](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1022:1022)_, no term id was found for the name/label _pedicle of sixth thoracic vertebra_.

1. In row _[1023](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1023:1023)_, no term id was found for the name/label _spinous process of sixth thoracic vertebra_.

1. In row _[1024](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1024:1024)_, no term id was found for the name/label _superior articular facet of sixth thoracic vertebra_.

1. In row _[1025](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1025:1025)_, no term id was found for the name/label _superior articular process of sixth thoracic vertebra_.

1. In row _[1026](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1026:1026)_, no term id was found for the name/label _superior costal facet of sixth thoracic vertebra_.

1. In row _[1027](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1027:1027)_, no term id was found for the name/label _superior vertebral notch of sixth thoracic vertebra_.

1. In row _[1028](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1028:1028)_, no term id was found for the name/label _transverse costal facet of sixth thoracic vertebra_.

1. In row _[1029](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1029:1029)_, no term id was found for the name/label _transverse process of sixth thoracic vertebra_.

1. In row _[1030](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1030:1030)_, no term id was found for the name/label _vertebral arch of sixth thoracic vertebra_.

1. In row _[1031](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1031:1031)_, no term id was found for the name/label _vertebral body of sixth thoracic vertebra_.

1. In row _[1032](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1032:1032)_, no term id was found for the name/label _vertebral foramen of sixth thoracic vertebra_.

1. In row _[1034](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1034:1034)_, no term id was found for the name/label _inferior articular facet of seventh thoracic vertebra_.

1. In row _[1035](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1035:1035)_, no term id was found for the name/label _inferior articular process of seventh thoracic vertebra_.

1. In row _[1036](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1036:1036)_, no term id was found for the name/label _inferior costal facet of seventh thoracic vertebra_.

1. In row _[1037](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1037:1037)_, no term id was found for the name/label _inferior vertebral notch of seventh thoracic vertebra_.

1. In row _[1038](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1038:1038)_, no term id was found for the name/label _lamina of seventh thoracic vertebra_.

1. In row _[1039](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1039:1039)_, no term id was found for the name/label _pedicle of seventh thoracic vertebra_.

1. In row _[1040](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1040:1040)_, no term id was found for the name/label _spinous process of seventh thoracic vertebra_.

1. In row _[1041](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1041:1041)_, no term id was found for the name/label _superior articular facet of seventh thoracic vertebra_.

1. In row _[1042](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1042:1042)_, no term id was found for the name/label _superior articular process of seventh thoracic vertebra_.

1. In row _[1043](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1043:1043)_, no term id was found for the name/label _superior costal facet of seventh thoracic vertebra_.

1. In row _[1044](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1044:1044)_, no term id was found for the name/label _superior vertebral notch of seventh thoracic vertebra_.

1. In row _[1045](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1045:1045)_, no term id was found for the name/label _transverse costal facet of seventh thoracic vertebra_.

1. In row _[1046](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1046:1046)_, no term id was found for the name/label _transverse process of seventh thoracic vertebra_.

1. In row _[1047](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1047:1047)_, no term id was found for the name/label _vertebral arch of seventh thoracic vertebra_.

1. In row _[1048](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1048:1048)_, no term id was found for the name/label _vertebral body of seventh thoracic vertebra_.

1. In row _[1049](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1049:1049)_, no term id was found for the name/label _vertebral foramen of seventh thoracic vertebra_.

1. In row _[1051](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1051:1051)_, no term id was found for the name/label _inferior articular facet of eighth thoracic vertebra_.

1. In row _[1052](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1052:1052)_, no term id was found for the name/label _inferior articular process of eighth thoracic vertebra_.

1. In row _[1053](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1053:1053)_, no term id was found for the name/label _inferior costal facet of eighth thoracic vertebra_.

1. In row _[1054](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1054:1054)_, no term id was found for the name/label _inferior vertebral notch of eighth thoracic vertebra_.

1. In row _[1055](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1055:1055)_, no term id was found for the name/label _lamina of eighth thoracic vertebra_.

1. In row _[1056](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1056:1056)_, no term id was found for the name/label _pedicle of eighth thoracic vertebra_.

1. In row _[1057](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1057:1057)_, no term id was found for the name/label _spinous process of eighth thoracic vertebra_.

1. In row _[1058](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1058:1058)_, no term id was found for the name/label _superior articular facet of eighth thoracic vertebra_.

1. In row _[1059](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1059:1059)_, no term id was found for the name/label _superior articular process of eighth thoracic vertebra_.

1. In row _[1060](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1060:1060)_, no term id was found for the name/label _superior costal facet of eighth thoracic vertebra_.

1. In row _[1061](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1061:1061)_, no term id was found for the name/label _superior vertebral notch of eighth thoracic vertebra_.

1. In row _[1062](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1062:1062)_, no term id was found for the name/label _transverse costal facet of eighth thoracic vertebra_.

1. In row _[1063](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1063:1063)_, no term id was found for the name/label _transverse process of eighth thoracic vertebra_.

1. In row _[1064](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1064:1064)_, no term id was found for the name/label _vertebral arch of eighth thoracic vertebra_.

1. In row _[1065](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1065:1065)_, no term id was found for the name/label _vertebral body of eighth thoracic vertebra_.

1. In row _[1066](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1066:1066)_, no term id was found for the name/label _vertebral foramen of eighth thoracic vertebra_.

1. In row _[1068](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1068:1068)_, no term id was found for the name/label _inferior articular facet of ninth thoracic vertebra_.

1. In row _[1069](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1069:1069)_, no term id was found for the name/label _inferior articular process of ninth thoracic vertebra_.

1. In row _[1070](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1070:1070)_, no term id was found for the name/label _inferior costal facet of ninth thoracic vertebra_.

1. In row _[1071](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1071:1071)_, no term id was found for the name/label _inferior vertebral notch of ninth thoracic vertebra_.

1. In row _[1072](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1072:1072)_, no term id was found for the name/label _lamina of ninth thoracic vertebra_.

1. In row _[1073](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1073:1073)_, no term id was found for the name/label _pedicle of ninth thoracic vertebra_.

1. In row _[1074](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1074:1074)_, no term id was found for the name/label _spinous process of ninth thoracic vertebra_.

1. In row _[1075](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1075:1075)_, no term id was found for the name/label _superior articular facet of ninth thoracic vertebra_.

1. In row _[1076](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1076:1076)_, no term id was found for the name/label _superior articular process of ninth thoracic vertebra_.

1. In row _[1077](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1077:1077)_, no term id was found for the name/label _superior costal facet of ninth thoracic vertebra_.

1. In row _[1078](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1078:1078)_, no term id was found for the name/label _superior vertebral notch of ninth thoracic vertebra_.

1. In row _[1079](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1079:1079)_, no term id was found for the name/label _transverse costal facet of ninth thoracic vertebra_.

1. In row _[1080](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1080:1080)_, no term id was found for the name/label _transverse process of ninth thoracic vertebra_.

1. In row _[1081](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1081:1081)_, no term id was found for the name/label _vertebral arch of ninth thoracic vertebra_.

1. In row _[1082](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1082:1082)_, no term id was found for the name/label _vertebral body of ninth thoracic vertebra_.

1. In row _[1083](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1083:1083)_, no term id was found for the name/label _vertebral foramen of ninth thoracic vertebra_.


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



|      | row_number                                                                                                             | s              | slabel                       | user_slabel                  | o              | olabel                               | user_olabel       |       deltaIC |
|------|------------------------------------------------------------------------------------------------------------------------|----------------|------------------------------|------------------------------|----------------|--------------------------------------|-------------------|---------------|
|    3 | [439](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=439:439)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|    4 | [411](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=411:411)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|    5 | [410](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=410:410)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|    6 | [409](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=409:409)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|    7 | [408](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=408:408)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|    8 | [407](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=407:407)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|    9 | [406](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=406:406)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   10 | [405](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=405:405)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   11 | [396](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=396:396)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   12 | [404](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=404:404)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   13 | [403](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=403:403)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   14 | [402](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=402:402)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   15 | [401](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=401:401)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   16 | [400](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=400:400)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   17 | [399](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=399:399)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   18 | [398](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=398:398)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   19 | [412](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=412:412)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   20 | [413](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=413:413)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   21 | [414](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=414:414)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   22 | [424](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=424:424)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   23 | [431](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=431:431)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   24 | [430](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=430:430)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   25 | [429](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=429:429)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   26 | [428](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=428:428)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   27 | [427](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=427:427)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   28 | [426](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=426:426)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   29 | [425](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=425:425)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   30 | [423](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=423:423)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   31 | [415](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=415:415)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   32 | [422](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=422:422)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   33 | [421](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=421:421)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   34 | [420](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=420:420)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   35 | [419](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=419:419)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   36 | [418](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=418:418)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   37 | [417](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=417:417)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   38 | [416](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=416:416)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   39 | [397](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=397:397)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   40 | [394](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=394:394)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   41 | [395](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=395:395)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   42 | [433](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=433:433)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   43 | [375](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=375:375)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   44 | [374](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=374:374)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   45 | [373](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=373:373)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   46 | [372](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=372:372)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   47 | [371](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=371:371)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   48 | [370](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=370:370)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   49 | [369](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=369:369)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   50 | [368](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=368:368)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   51 | [367](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=367:367)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   52 | [366](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=366:366)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   53 | [365](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=365:365)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   54 | [364](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=364:364)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   55 | [363](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=363:363)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   56 | [362](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=362:362)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   57 | [361](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=361:361)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   58 | [376](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=376:376)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   59 | [377](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=377:377)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   60 | [378](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=378:378)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   61 | [387](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=387:387)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   62 | [393](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=393:393)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   63 | [392](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=392:392)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   64 | [391](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=391:391)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   65 | [390](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=390:390)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   66 | [389](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=389:389)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   67 | [388](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=388:388)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   68 | [386](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=386:386)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   69 | [379](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=379:379)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   70 | [385](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=385:385)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   71 | [384](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=384:384)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   72 | [383](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=383:383)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   73 | [382](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=382:382)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   74 | [381](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=381:381)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   75 | [380](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=380:380)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   76 | [432](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=432:432)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   77 | [435](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=435:435)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   78 | [434](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=434:434)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   79 | [481](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=481:481)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   80 | [501](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=501:501)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   81 | [479](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=479:479)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   82 | [502](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=502:502)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   83 | [478](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=478:478)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   84 | [477](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=477:477)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   85 | [503](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=503:503)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   86 | [476](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=476:476)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   87 | [475](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=475:475)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   88 | [504](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=504:504)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   89 | [474](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=474:474)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   90 | [473](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=473:473)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   91 | [505](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=505:505)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   92 | [472](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=472:472)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   93 | [506](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=506:506)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   94 | [471](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=471:471)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   95 | [480](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=480:480)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   96 | [482](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=482:482)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   97 | [498](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=498:498)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   98 | [483](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=483:483)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|   99 | [499](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=499:499)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  100 | [496](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=496:496)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  101 | [500](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=500:500)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  102 | [495](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=495:495)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  103 | [494](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=494:494)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  104 | [493](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=493:493)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  105 | [492](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=492:492)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  106 | [491](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=491:491)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  107 | [490](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=490:490)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  108 | [489](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=489:489)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  109 | [488](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=488:488)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  110 | [487](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=487:487)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  111 | [486](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=486:486)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  112 | [485](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=485:485)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  113 | [484](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=484:484)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  114 | [507](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=507:507)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  115 | [470](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=470:470)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  116 | [508](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=508:508)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  117 | [469](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=469:469)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  118 | [451](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=451:451)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  119 | [450](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=450:450)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  120 | [449](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=449:449)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  121 | [448](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=448:448)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  122 | [447](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=447:447)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  123 | [446](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=446:446)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  124 | [445](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=445:445)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  125 | [444](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=444:444)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  126 | [443](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=443:443)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  127 | [442](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=442:442)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  128 | [441](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=441:441)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  129 | [440](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=440:440)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  130 | [438](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=438:438)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  131 | [437](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=437:437)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  132 | [436](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=436:436)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  133 | [452](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=452:452)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  134 | [453](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=453:453)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  135 | [454](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=454:454)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  136 | [463](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=463:463)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  137 | [468](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=468:468)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  138 | [509](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=509:509)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  139 | [467](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=467:467)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  140 | [466](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=466:466)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  141 | [465](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=465:465)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  142 | [464](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=464:464)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  143 | [462](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=462:462)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  144 | [455](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=455:455)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  145 | [461](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=461:461)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  146 | [460](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=460:460)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  147 | [459](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=459:459)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  148 | [458](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=458:458)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  149 | [457](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=457:457)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  150 | [456](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=456:456)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  151 | [360](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=360:360)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  152 | [497](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=497:497)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    |   1.93449e+13 |
|  153 | [489](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=489:489)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  154 | [491](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=491:491)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  155 | [481](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=481:481)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  156 | [480](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=480:480)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  157 | [484](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=484:484)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  158 | [485](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=485:485)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  159 | [486](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=486:486)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  160 | [487](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=487:487)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  161 | [488](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=488:488)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  162 | [482](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=482:482)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  163 | [490](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=490:490)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  164 | [483](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=483:483)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  165 | [493](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=493:493)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  166 | [495](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=495:495)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  167 | [492](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=492:492)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  168 | [494](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=494:494)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |   2.31986e+12 |
|  169 | [159](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=159:159)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  170 | [156](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=156:156)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  171 | [147](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=147:147)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  172 | [148](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=148:148)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  173 | [169](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=169:169)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  174 | [150](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=150:150)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  175 | [174](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=174:174)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  176 | [153](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=153:153)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  177 | [164](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=164:164)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  178 | [151](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=151:151)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  179 | [172](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=172:172)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  180 | [158](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=158:158)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  181 | [152](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=152:152)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  182 | [155](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=155:155)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  183 | [170](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=170:170)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  184 | [171](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=171:171)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  185 | [157](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=157:157)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  186 | [154](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=154:154)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  187 | [149](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=149:149)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  188 | [160](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=160:160)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  189 | [161](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=161:161)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  190 | [165](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=165:165)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  191 | [163](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=163:163)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  192 | [166](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=166:166)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  193 | [162](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=162:162)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  194 | [167](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=167:167)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  195 | [173](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=173:173)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  196 | [168](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=168:168)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          |   2.20024e+10 |
|  205 | [665](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=665:665)    | UBERON:0001350 | coccyx                       | coccyx                       | UBERON:0001095 | caudal vertebra                      | caudal vertebra   |   2.96436e+06 |
|  206 | [666](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=666:666)    | UBERON:0001350 | coccyx                       | coccyx                       | UBERON:0001095 | caudal vertebra                      | caudal vertebra   |   2.96436e+06 |
|  207 | [664](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=664:664)    | UBERON:0001350 | coccyx                       | coccyx                       | UBERON:0001095 | caudal vertebra                      | caudal vertebra   |   2.96436e+06 |
|  248 | [205](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=205:205)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  249 | [176](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=176:176)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  250 | [200](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=200:200)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  251 | [194](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=194:194)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  252 | [195](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=195:195)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  253 | [196](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=196:196)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  254 | [197](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=197:197)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  255 | [198](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=198:198)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  256 | [199](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=199:199)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  257 | [201](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=201:201)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  258 | [177](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=177:177)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  259 | [202](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=202:202)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  260 | [203](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=203:203)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  261 | [204](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=204:204)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  262 | [209](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=209:209)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  263 | [206](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=206:206)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  264 | [207](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=207:207)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  265 | [193](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=193:193)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  266 | [192](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=192:192)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  267 | [191](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=191:191)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  268 | [190](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=190:190)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  269 | [189](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=189:189)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  270 | [188](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=188:188)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  271 | [187](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=187:187)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  272 | [186](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=186:186)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  273 | [185](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=185:185)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  274 | [184](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=184:184)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  275 | [183](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=183:183)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  276 | [182](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=182:182)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  277 | [181](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=181:181)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  278 | [180](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=180:180)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  279 | [179](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=179:179)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  280 | [208](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=208:208)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  281 | [178](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=178:178)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  282 | [280](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=280:280)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  283 | [266](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=266:266)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  284 | [279](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=279:279)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  285 | [234](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=234:234)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  286 | [228](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=228:228)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  287 | [229](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=229:229)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  288 | [230](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=230:230)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  289 | [231](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=231:231)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  290 | [232](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=232:232)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  291 | [233](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=233:233)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  292 | [235](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=235:235)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  293 | [226](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=226:226)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  294 | [236](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=236:236)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  295 | [237](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=237:237)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  296 | [238](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=238:238)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  297 | [239](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=239:239)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  298 | [278](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=278:278)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  299 | [241](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=241:241)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  300 | [227](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=227:227)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  301 | [225](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=225:225)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  302 | [243](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=243:243)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  303 | [216](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=216:216)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  304 | [210](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=210:210)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  305 | [211](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=211:211)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  306 | [212](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=212:212)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  307 | [213](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=213:213)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  308 | [214](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=214:214)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  309 | [215](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=215:215)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  310 | [217](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=217:217)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  311 | [224](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=224:224)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  312 | [218](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=218:218)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  313 | [219](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=219:219)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  314 | [220](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=220:220)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  315 | [221](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=221:221)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  316 | [222](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=222:222)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  317 | [223](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=223:223)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  318 | [242](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=242:242)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  319 | [240](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=240:240)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  320 | [244](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=244:244)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  321 | [270](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=270:270)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  322 | [263](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=263:263)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  323 | [264](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=264:264)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  324 | [245](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=245:245)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  325 | [267](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=267:267)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  326 | [268](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=268:268)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  327 | [269](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=269:269)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  328 | [271](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=271:271)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  329 | [261](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=261:261)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  330 | [272](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=272:272)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  331 | [273](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=273:273)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  332 | [274](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=274:274)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  333 | [275](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=275:275)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  334 | [276](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=276:276)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  335 | [277](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=277:277)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  336 | [262](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=262:262)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  337 | [265](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=265:265)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  338 | [260](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=260:260)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  339 | [252](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=252:252)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  340 | [246](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=246:246)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  341 | [247](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=247:247)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  342 | [248](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=248:248)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  343 | [259](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=259:259)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  344 | [250](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=250:250)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  345 | [251](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=251:251)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  346 | [249](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=249:249)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  347 | [253](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=253:253)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  348 | [254](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=254:254)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  349 | [255](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=255:255)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  350 | [256](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=256:256)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  351 | [257](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=257:257)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  352 | [258](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=258:258)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  353 | [350](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=350:350)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  354 | [358](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=358:358)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  355 | [357](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=357:357)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  356 | [356](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=356:356)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  357 | [355](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=355:355)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  358 | [354](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=354:354)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  359 | [353](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=353:353)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  360 | [352](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=352:352)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  361 | [351](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=351:351)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  362 | [325](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=325:325)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  363 | [344](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=344:344)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  364 | [334](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=334:334)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  365 | [330](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=330:330)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  366 | [343](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=343:343)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  367 | [331](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=331:331)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  368 | [342](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=342:342)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  369 | [332](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=332:332)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  370 | [333](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=333:333)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  371 | [341](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=341:341)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  372 | [329](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=329:329)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  373 | [335](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=335:335)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  374 | [326](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=326:326)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  375 | [336](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=336:336)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  376 | [340](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=340:340)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  377 | [339](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=339:339)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  378 | [337](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=337:337)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  379 | [345](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=345:345)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  380 | [338](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=338:338)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  381 | [347](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=347:347)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  382 | [328](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=328:328)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  383 | [327](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=327:327)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  384 | [349](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=349:349)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  385 | [324](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=324:324)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  386 | [346](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=346:346)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  387 | [348](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=348:348)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  388 | [323](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=323:323)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | 522.366       |
|  520 | [455](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=455:455)    | UBERON:0005922 | inferior nasal concha        | inferior nasal concha        | UBERON:0008895 | splanchnocranium                     | splanchnocranium  |  21.852       |
|  521 | [699](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=699:699)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  522 | [690](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=690:690)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  523 | [703](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=703:703)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  524 | [701](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=701:701)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  525 | [700](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=700:700)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  526 | [687](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=687:687)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  527 | [688](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=688:688)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  528 | [689](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=689:689)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  529 | [691](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=691:691)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  530 | [698](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=698:698)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  531 | [692](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=692:692)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  532 | [694](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=694:694)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  533 | [695](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=695:695)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  534 | [696](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=696:696)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  535 | [697](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=697:697)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  536 | [693](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=693:693)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  537 | [702](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=702:702)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   3.45825     |
|  538 | [674](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=674:674)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  539 | [681](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=681:681)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  540 | [673](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=673:673)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  541 | [686](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=686:686)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  542 | [685](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=685:685)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  543 | [668](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=668:668)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  544 | [683](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=683:683)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  545 | [669](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=669:669)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  546 | [670](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=670:670)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  547 | [682](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=682:682)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  548 | [684](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=684:684)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  549 | [671](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=671:671)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  550 | [672](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=672:672)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  551 | [679](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=679:679)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  552 | [678](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=678:678)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  553 | [677](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=677:677)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  554 | [676](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=676:676)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  555 | [680](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=680:680)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
|  556 | [675](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=675:675)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra |   0.01951     |
| 1060 | [55](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=55:55)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1061 | [56](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=56:56)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1062 | [57](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=57:57)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1064 | [58](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=58:58)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1066 | [59](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=59:59)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1068 | [60](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=60:60)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1070 | [61](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=61:61)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1071 | [62](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=62:62)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1072 | [63](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=63:63)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1073 | [64](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=64:64)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1074 | [65](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=65:65)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1075 | [66](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=66:66)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1076 | [67](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=67:67)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1077 | [68](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=68:68)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1078 | [69](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=69:69)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1079 | [70](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=70:70)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1080 | [71](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=71:71)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1081 | [72](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=72:72)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1082 | [73](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=73:73)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1083 | [74](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=74:74)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1084 | [75](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=75:75)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1085 | [76](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=76:76)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1087 | [77](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=77:77)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1089 | [78](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=78:78)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1091 | [79](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=79:79)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1093 | [80](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=80:80)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1095 | [81](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=81:81)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1097 | [82](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=82:82)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1099 | [83](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=83:83)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1101 | [84](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=84:84)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1103 | [85](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=85:85)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1105 | [86](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=86:86)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1106 | [87](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=87:87)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1108 | [88](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=88:88)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1110 | [89](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=89:89)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1112 | [90](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=90:90)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1114 | [91](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=91:91)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1115 | [92](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=92:92)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1116 | [93](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=93:93)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1117 | [94](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=94:94)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1118 | [95](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=95:95)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1120 | [96](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=96:96)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1122 | [97](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=97:97)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1124 | [98](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=98:98)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1126 | [99](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=99:99)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1127 | [100](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=100:100)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1128 | [101](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=101:101)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1129 | [102](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=102:102)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1130 | [103](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=103:103)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1132 | [104](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=104:104)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1134 | [105](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=105:105)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1136 | [106](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=106:106)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1138 | [107](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=107:107)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1140 | [108](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=108:108)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1142 | [109](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=109:109)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1144 | [110](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=110:110)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1146 | [111](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=111:111)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1147 | [112](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=112:112)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1148 | [113](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=113:113)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1149 | [114](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=114:114)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1150 | [115](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=115:115)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1151 | [116](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=116:116)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1152 | [117](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=117:117)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1153 | [118](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=118:118)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1154 | [119](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=119:119)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1155 | [120](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=120:120)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1156 | [121](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=121:121)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1157 | [122](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=122:122)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1158 | [123](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=123:123)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1160 | [124](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=124:124)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1162 | [125](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=125:125)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1164 | [126](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=126:126)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1166 | [127](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=127:127)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1168 | [128](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=128:128)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1170 | [129](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=129:129)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1172 | [130](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=130:130)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1174 | [131](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=131:131)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1176 | [132](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=132:132)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1177 | [133](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=133:133)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1178 | [134](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=134:134)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1179 | [135](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=135:135)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1180 | [136](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=136:136)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1181 | [137](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=137:137)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1182 | [138](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=138:138)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1183 | [139](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=139:139)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1184 | [140](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=140:140)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1186 | [141](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=141:141)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1188 | [142](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=142:142)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1190 | [143](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=143:143)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1192 | [144](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=144:144)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1194 | [145](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=145:145)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1196 | [146](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=146:146)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          | nan           |
| 1245 | [366](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=366:366)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1246 | [367](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=367:367)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1247 | [368](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=368:368)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1248 | [369](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=369:369)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1249 | [370](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=370:370)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1250 | [371](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=371:371)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1251 | [372](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=372:372)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1252 | [373](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=373:373)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1253 | [374](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=374:374)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1254 | [375](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=375:375)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1255 | [376](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=376:376)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1256 | [377](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=377:377)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1257 | [378](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=378:378)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1258 | [379](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=379:379)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1259 | [380](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=380:380)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1260 | [381](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=381:381)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1261 | [382](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=382:382)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1262 | [383](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=383:383)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1263 | [384](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=384:384)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1264 | [385](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=385:385)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1265 | [386](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=386:386)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1266 | [387](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=387:387)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1267 | [388](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=388:388)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1269 | [389](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=389:389)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1270 | [390](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=390:390)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1271 | [391](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=391:391)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1272 | [392](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=392:392)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1273 | [393](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=393:393)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1274 | [394](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=394:394)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1275 | [395](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=395:395)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1276 | [396](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=396:396)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1277 | [397](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=397:397)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1278 | [398](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=398:398)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1279 | [399](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=399:399)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1281 | [400](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=400:400)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1283 | [401](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=401:401)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1285 | [402](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=402:402)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1287 | [403](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=403:403)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1289 | [404](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=404:404)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1291 | [405](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=405:405)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1293 | [406](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=406:406)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1294 | [407](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=407:407)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1295 | [408](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=408:408)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1296 | [409](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=409:409)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1297 | [410](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=410:410)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1298 | [411](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=411:411)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1299 | [412](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=412:412)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1300 | [413](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=413:413)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1301 | [414](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=414:414)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1302 | [415](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=415:415)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1303 | [416](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=416:416)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1304 | [417](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=417:417)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1305 | [418](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=418:418)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1306 | [419](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=419:419)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1307 | [420](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=420:420)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1308 | [421](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=421:421)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1309 | [422](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=422:422)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1310 | [423](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=423:423)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1311 | [424](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=424:424)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1312 | [425](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=425:425)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1313 | [426](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=426:426)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1314 | [427](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=427:427)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1315 | [428](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=428:428)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1316 | [428](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=428:428)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1317 | [429](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=429:429)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1318 | [429](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=429:429)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1319 | [430](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=430:430)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1320 | [430](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=430:430)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1321 | [431](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=431:431)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1322 | [431](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=431:431)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1323 | [432](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=432:432)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1324 | [432](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=432:432)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1325 | [433](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=433:433)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1326 | [433](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=433:433)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1327 | [434](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=434:434)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1328 | [434](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=434:434)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1329 | [435](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=435:435)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1330 | [435](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=435:435)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1331 | [436](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=436:436)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1332 | [436](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=436:436)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1333 | [437](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=437:437)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1334 | [437](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=437:437)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1335 | [438](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=438:438)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1336 | [438](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=438:438)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1337 | [439](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=439:439)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1338 | [439](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=439:439)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1339 | [440](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=440:440)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1340 | [440](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=440:440)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1341 | [441](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=441:441)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1342 | [441](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=441:441)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1343 | [442](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=442:442)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1344 | [442](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=442:442)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1345 | [443](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=443:443)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1346 | [443](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=443:443)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1347 | [444](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=444:444)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1348 | [444](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=444:444)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1349 | [445](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=445:445)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1350 | [445](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=445:445)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1351 | [446](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=446:446)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1352 | [446](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=446:446)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1353 | [447](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=447:447)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1354 | [447](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=447:447)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1355 | [448](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=448:448)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1356 | [448](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=448:448)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1357 | [449](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=449:449)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1358 | [449](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=449:449)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan           |
| 1359 | [450](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=450:450)    | UBERON:0010911 | ossicle                      | ossicle                      | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1360 | [451](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=451:451)    | UBERON:0010911 | ossicle                      | ossicle                      | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1361 | [451](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=451:451)    | UBERON:0001688 | incus bone                   | incus bone                   | UBERON:0010911 | ossicle                              | ossicle           | nan           |
| 1362 | [452](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=452:452)    | UBERON:0010911 | ossicle                      | ossicle                      | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1363 | [452](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=452:452)    | UBERON:0001689 | malleus bone                 | malleus bone                 | UBERON:0010911 | ossicle                              | ossicle           | nan           |
| 1364 | [453](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=453:453)    | UBERON:0010911 | ossicle                      | ossicle                      | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1365 | [453](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=453:453)    | UBERON:0001687 | stapes bone                  | stapes bone                  | UBERON:0010911 | ossicle                              | ossicle           | nan           |
| 1366 | [454](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=454:454)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1368 | [455](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=455:455)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1370 | [456](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=456:456)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1371 | [456](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=456:456)    | UBERON:0001680 | lacrimal bone                | lacrimal bone                | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1372 | [457](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=457:457)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1373 | [457](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=457:457)    | UBERON:0001680 | lacrimal bone                | lacrimal bone                | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1374 | [458](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=458:458)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1375 | [458](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=458:458)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1376 | [459](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=459:459)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1377 | [459](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=459:459)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1378 | [460](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=460:460)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1379 | [460](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=460:460)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1380 | [461](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=461:461)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1381 | [461](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=461:461)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1382 | [462](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=462:462)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1383 | [462](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=462:462)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1384 | [463](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=463:463)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1385 | [463](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=463:463)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1386 | [464](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=464:464)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1387 | [464](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=464:464)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1388 | [465](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=465:465)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1389 | [465](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=465:465)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1390 | [466](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=466:466)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1391 | [466](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=466:466)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1392 | [467](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=467:467)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1393 | [467](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=467:467)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1394 | [468](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=468:468)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1395 | [468](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=468:468)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1396 | [469](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=469:469)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1397 | [469](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=469:469)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1398 | [470](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=470:470)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1399 | [470](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=470:470)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1400 | [471](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=471:471)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1401 | [471](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=471:471)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1402 | [472](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=472:472)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1403 | [472](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=472:472)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1404 | [473](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=473:473)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1405 | [473](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=473:473)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1406 | [474](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=474:474)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1407 | [474](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=474:474)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1408 | [475](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=475:475)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1409 | [475](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=475:475)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1410 | [476](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=476:476)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1411 | [476](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=476:476)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1412 | [477](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=477:477)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1413 | [477](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=477:477)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1414 | [478](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=478:478)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1415 | [478](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=478:478)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1416 | [479](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=479:479)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1417 | [479](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=479:479)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1418 | [480](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=480:480)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1420 | [481](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=481:481)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1422 | [482](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=482:482)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1423 | [483](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=483:483)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1425 | [484](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=484:484)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1427 | [485](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=485:485)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1429 | [486](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=486:486)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1431 | [487](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=487:487)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1433 | [488](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=488:488)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1435 | [489](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=489:489)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1437 | [490](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=490:490)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1439 | [491](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=491:491)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1441 | [492](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=492:492)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1443 | [493](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=493:493)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1445 | [494](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=494:494)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1446 | [495](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=495:495)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1447 | [495](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=495:495)    | UBERON:0016477 | zygomatic process of maxilla | zygomatic process of maxilla | UBERON:0002397 | maxilla                              | maxilla           | nan           |
| 1448 | [496](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=496:496)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1449 | [496](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=496:496)    | UBERON:0001681 | nasal bone                   | nasal bone                   | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1450 | [497](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=497:497)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1451 | [498](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=498:498)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1452 | [499](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=499:499)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1453 | [500](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=500:500)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1454 | [501](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=501:501)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1455 | [502](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=502:502)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1456 | [503](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=503:503)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1457 | [504](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=504:504)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1458 | [505](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=505:505)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1459 | [505](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=505:505)    | UBERON:0001683 | jugal bone                   | zygomatic bone               | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1460 | [506](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=506:506)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1461 | [506](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=506:506)    | UBERON:0001683 | jugal bone                   | zygomatic bone               | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1462 | [507](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=507:507)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1463 | [507](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=507:507)    | UBERON:0001683 | jugal bone                   | zygomatic bone               | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1464 | [508](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=508:508)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1465 | [508](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=508:508)    | UBERON:0001683 | jugal bone                   | zygomatic bone               | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1466 | [509](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=509:509)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      | nan           |
| 1467 | [509](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=509:509)    | UBERON:0001683 | jugal bone                   | zygomatic bone               | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan           |
| 1494 | [662](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=662:662)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1495 | [663](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=663:663)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1496 | [664](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=664:664)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1498 | [665](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=665:665)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1500 | [666](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=666:666)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1502 | [667](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=667:667)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1503 | [668](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=668:668)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1505 | [669](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=669:669)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1507 | [670](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=670:670)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1509 | [671](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=671:671)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1511 | [672](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=672:672)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1513 | [673](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=673:673)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1515 | [674](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=674:674)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1517 | [675](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=675:675)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1519 | [676](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=676:676)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1521 | [677](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=677:677)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1523 | [678](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=678:678)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1525 | [679](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=679:679)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1527 | [680](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=680:680)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1529 | [681](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=681:681)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1531 | [682](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=682:682)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1533 | [683](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=683:683)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1535 | [684](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=684:684)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1537 | [685](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=685:685)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1539 | [686](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=686:686)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1541 | [687](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=687:687)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1543 | [688](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=688:688)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1545 | [689](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=689:689)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1547 | [690](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=690:690)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1549 | [691](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=691:691)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1551 | [692](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=692:692)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1553 | [693](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=693:693)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1554 | [694](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=694:694)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1556 | [695](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=695:695)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1558 | [696](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=696:696)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1560 | [697](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=697:697)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1562 | [698](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=698:698)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1564 | [699](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=699:699)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1566 | [700](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=700:700)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1568 | [701](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=701:701)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1570 | [702](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=702:702)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1572 | [703](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=703:703)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1574 | [704](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=704:704)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1576 | [705](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=705:705)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1578 | [706](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=706:706)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1580 | [707](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=707:707)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1582 | [708](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=708:708)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1584 | [709](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=709:709)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1586 | [710](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=710:710)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1588 | [711](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=711:711)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1590 | [712](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=712:712)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1592 | [713](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=713:713)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1594 | [714](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=714:714)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1596 | [715](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=715:715)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1598 | [716](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=716:716)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1600 | [717](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=717:717)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1602 | [718](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=718:718)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1604 | [719](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=719:719)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1605 | [720](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=720:720)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1606 | [721](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=721:721)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1607 | [722](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=722:722)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1608 | [723](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=723:723)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1609 | [724](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=724:724)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1610 | [725](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=725:725)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1611 | [726](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=726:726)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1612 | [727](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=727:727)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1613 | [728](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=728:728)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1614 | [729](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=729:729)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1615 | [730](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=730:730)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1616 | [731](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=731:731)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1617 | [732](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=732:732)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1618 | [733](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=733:733)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1619 | [734](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=734:734)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1621 | [735](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=735:735)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1623 | [736](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=736:736)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1625 | [737](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=737:737)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1627 | [738](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=738:738)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1629 | [739](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=739:739)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1631 | [740](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=740:740)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1633 | [741](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=741:741)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1635 | [742](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=742:742)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1637 | [743](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=743:743)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1639 | [744](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=744:744)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1641 | [745](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=745:745)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1643 | [746](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=746:746)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1645 | [747](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=747:747)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1647 | [748](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=748:748)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1649 | [749](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=749:749)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1650 | [750](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=750:750)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1651 | [751](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=751:751)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1652 | [752](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=752:752)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1653 | [753](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=753:753)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1654 | [754](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=754:754)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1655 | [755](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=755:755)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1656 | [756](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=756:756)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1657 | [757](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=757:757)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1658 | [758](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=758:758)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1659 | [759](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=759:759)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1660 | [760](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=760:760)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1661 | [761](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=761:761)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1662 | [762](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=762:762)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1663 | [763](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=763:763)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1664 | [764](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=764:764)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1665 | [765](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=765:765)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1666 | [766](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=766:766)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1667 | [767](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=767:767)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1668 | [768](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=768:768)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1669 | [769](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=769:769)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1670 | [770](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=770:770)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1671 | [771](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=771:771)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1672 | [772](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=772:772)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1673 | [773](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=773:773)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1674 | [774](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=774:774)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1675 | [775](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=775:775)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1676 | [776](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=776:776)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1677 | [777](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=777:777)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1678 | [778](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=778:778)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1679 | [779](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=779:779)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1680 | [780](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=780:780)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1681 | [781](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=781:781)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1682 | [782](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=782:782)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1683 | [783](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=783:783)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1684 | [784](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=784:784)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1685 | [785](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=785:785)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1686 | [786](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=786:786)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1687 | [787](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=787:787)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1688 | [788](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=788:788)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1689 | [789](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=789:789)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1690 | [790](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=790:790)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1691 | [791](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=791:791)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1692 | [792](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=792:792)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1693 | [793](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=793:793)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1694 | [794](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=794:794)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1695 | [795](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=795:795)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1696 | [796](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=796:796)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1697 | [797](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=797:797)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1699 | [798](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=798:798)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1701 | [799](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=799:799)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1703 | [800](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=800:800)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1705 | [801](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=801:801)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1707 | [802](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=802:802)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1709 | [803](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=803:803)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1711 | [804](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=804:804)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1713 | [805](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=805:805)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1715 | [806](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=806:806)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1717 | [807](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=807:807)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1719 | [808](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=808:808)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1721 | [809](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=809:809)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1723 | [810](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=810:810)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1725 | [811](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=811:811)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1727 | [812](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=812:812)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1729 | [813](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=813:813)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1731 | [814](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=814:814)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1733 | [815](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=815:815)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1735 | [816](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=816:816)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1737 | [817](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=817:817)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1739 | [818](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=818:818)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1741 | [819](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=819:819)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1743 | [820](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=820:820)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1745 | [821](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=821:821)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1747 | [822](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=822:822)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1749 | [823](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=823:823)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1751 | [824](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=824:824)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1753 | [825](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=825:825)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1755 | [826](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=826:826)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1757 | [827](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=827:827)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1759 | [828](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=828:828)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1761 | [829](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=829:829)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1762 | [830](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=830:830)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1763 | [831](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=831:831)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1764 | [832](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=832:832)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1765 | [833](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=833:833)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1766 | [834](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=834:834)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1767 | [835](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=835:835)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1768 | [836](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=836:836)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1769 | [837](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=837:837)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1770 | [838](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=838:838)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1771 | [839](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=839:839)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1772 | [840](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=840:840)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1773 | [841](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=841:841)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1774 | [842](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=842:842)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1775 | [843](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=843:843)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1776 | [844](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=844:844)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1777 | [845](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=845:845)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1779 | [846](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=846:846)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1781 | [847](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=847:847)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1783 | [848](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=848:848)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1785 | [849](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=849:849)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1787 | [850](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=850:850)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1789 | [851](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=851:851)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1791 | [852](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=852:852)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1793 | [853](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=853:853)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1795 | [854](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=854:854)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1797 | [855](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=855:855)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1799 | [856](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=856:856)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1801 | [857](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=857:857)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1803 | [858](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=858:858)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1805 | [859](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=859:859)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1807 | [860](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=860:860)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1809 | [861](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=861:861)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1810 | [862](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=862:862)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1811 | [862](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=862:862)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1812 | [863](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=863:863)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1813 | [863](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=863:863)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1814 | [864](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=864:864)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1815 | [864](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=864:864)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1816 | [865](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=865:865)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1817 | [865](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=865:865)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1818 | [866](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=866:866)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1819 | [866](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=866:866)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1820 | [867](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=867:867)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1821 | [867](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=867:867)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1822 | [868](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=868:868)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1823 | [868](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=868:868)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1824 | [869](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=869:869)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1825 | [869](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=869:869)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1826 | [870](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=870:870)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1827 | [870](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=870:870)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1828 | [871](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=871:871)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1829 | [871](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=871:871)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1830 | [872](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=872:872)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1831 | [872](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=872:872)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1832 | [873](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=873:873)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1833 | [873](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=873:873)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1834 | [874](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=874:874)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1835 | [874](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=874:874)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1836 | [875](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=875:875)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1837 | [875](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=875:875)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1838 | [876](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=876:876)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1839 | [876](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=876:876)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1840 | [877](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=877:877)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1841 | [877](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=877:877)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1842 | [878](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=878:878)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1843 | [878](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=878:878)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1844 | [879](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=879:879)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1845 | [879](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=879:879)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1846 | [880](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=880:880)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1847 | [880](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=880:880)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   | nan           |
| 1848 | [881](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=881:881)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1849 | [882](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=882:882)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1851 | [883](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=883:883)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1853 | [884](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=884:884)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1855 | [885](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=885:885)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1857 | [886](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=886:886)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1859 | [887](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=887:887)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1861 | [888](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=888:888)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1863 | [889](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=889:889)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1865 | [890](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=890:890)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1867 | [891](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=891:891)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1869 | [892](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=892:892)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1871 | [893](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=893:893)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1873 | [894](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=894:894)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1875 | [895](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=895:895)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1877 | [896](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=896:896)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1879 | [897](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=897:897)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1881 | [898](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=898:898)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1883 | [899](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=899:899)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1885 | [900](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=900:900)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1887 | [901](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=901:901)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1889 | [902](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=902:902)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1891 | [903](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=903:903)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1893 | [904](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=904:904)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1895 | [905](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=905:905)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1897 | [906](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=906:906)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1899 | [907](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=907:907)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1901 | [908](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=908:908)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1903 | [909](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=909:909)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1905 | [910](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=910:910)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1907 | [911](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=911:911)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1909 | [912](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=912:912)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1911 | [913](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=913:913)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1913 | [914](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=914:914)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1915 | [915](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=915:915)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1917 | [916](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=916:916)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1918 | [917](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=917:917)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1919 | [918](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=918:918)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1920 | [919](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=919:919)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1921 | [920](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=920:920)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1922 | [921](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=921:921)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1923 | [922](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=922:922)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1924 | [923](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=923:923)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1925 | [924](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=924:924)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1926 | [925](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=925:925)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1927 | [926](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=926:926)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1928 | [927](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=927:927)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1929 | [928](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=928:928)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1930 | [929](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=929:929)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1931 | [930](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=930:930)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1932 | [931](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=931:931)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1933 | [932](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=932:932)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1934 | [933](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=933:933)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1935 | [934](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=934:934)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1936 | [935](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=935:935)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1937 | [936](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=936:936)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1938 | [937](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=937:937)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1939 | [938](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=938:938)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1940 | [939](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=939:939)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1941 | [940](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=940:940)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1942 | [941](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=941:941)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1943 | [942](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=942:942)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1944 | [943](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=943:943)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1945 | [944](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=944:944)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1946 | [945](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=945:945)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1947 | [946](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=946:946)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1948 | [947](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=947:947)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1949 | [948](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=948:948)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1950 | [949](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=949:949)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1951 | [950](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=950:950)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1952 | [951](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=951:951)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1953 | [952](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=952:952)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1954 | [953](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=953:953)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1955 | [954](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=954:954)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1956 | [955](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=955:955)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1957 | [956](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=956:956)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1958 | [957](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=957:957)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1959 | [958](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=958:958)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1960 | [959](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=959:959)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1961 | [960](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=960:960)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1962 | [961](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=961:961)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1963 | [962](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=962:962)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1964 | [963](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=963:963)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1965 | [964](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=964:964)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1966 | [965](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=965:965)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1967 | [966](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=966:966)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1968 | [967](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=967:967)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1969 | [968](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=968:968)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1970 | [969](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=969:969)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1971 | [970](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=970:970)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1972 | [971](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=971:971)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1973 | [972](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=972:972)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1974 | [973](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=973:973)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1975 | [974](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=974:974)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1976 | [975](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=975:975)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1977 | [976](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=976:976)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1978 | [977](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=977:977)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1979 | [978](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=978:978)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1980 | [979](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=979:979)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1981 | [980](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=980:980)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1982 | [981](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=981:981)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1983 | [982](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=982:982)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1984 | [983](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=983:983)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1985 | [984](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=984:984)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1986 | [985](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=985:985)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1987 | [986](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=986:986)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1988 | [987](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=987:987)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1989 | [988](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=988:988)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1990 | [989](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=989:989)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1991 | [990](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=990:990)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1992 | [991](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=991:991)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1993 | [992](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=992:992)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1994 | [993](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=993:993)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1995 | [994](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=994:994)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1996 | [995](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=995:995)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1997 | [996](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=996:996)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1998 | [997](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=997:997)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 1999 | [998](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=998:998)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2000 | [999](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=999:999)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2002 | [1000](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1000:1000) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2004 | [1001](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1001:1001) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2006 | [1002](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1002:1002) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2008 | [1003](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1003:1003) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2010 | [1004](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1004:1004) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2012 | [1005](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1005:1005) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2014 | [1006](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1006:1006) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2016 | [1007](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1007:1007) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2018 | [1008](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1008:1008) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2020 | [1009](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1009:1009) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2022 | [1010](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1010:1010) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2024 | [1011](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1011:1011) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2026 | [1012](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1012:1012) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2028 | [1013](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1013:1013) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2030 | [1014](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1014:1014) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2032 | [1015](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1015:1015) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2034 | [1016](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1016:1016) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2035 | [1017](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1017:1017) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2036 | [1018](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1018:1018) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2037 | [1019](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1019:1019) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2038 | [1020](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1020:1020) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2039 | [1021](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1021:1021) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2040 | [1022](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1022:1022) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2041 | [1023](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1023:1023) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2042 | [1024](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1024:1024) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2043 | [1025](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1025:1025) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2044 | [1026](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1026:1026) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2045 | [1027](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1027:1027) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2046 | [1028](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1028:1028) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2047 | [1029](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1029:1029) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2048 | [1030](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1030:1030) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2049 | [1031](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1031:1031) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2050 | [1032](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1032:1032) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2051 | [1033](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1033:1033) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2053 | [1034](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1034:1034) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2055 | [1035](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1035:1035) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2057 | [1036](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1036:1036) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2059 | [1037](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1037:1037) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2061 | [1038](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1038:1038) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2063 | [1039](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1039:1039) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2065 | [1040](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1040:1040) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2067 | [1041](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1041:1041) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2069 | [1042](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1042:1042) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2071 | [1043](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1043:1043) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2073 | [1044](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1044:1044) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2075 | [1045](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1045:1045) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2077 | [1046](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1046:1046) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2079 | [1047](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1047:1047) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2081 | [1048](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1048:1048) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2083 | [1049](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1049:1049) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2085 | [1050](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1050:1050) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2086 | [1051](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1051:1051) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2087 | [1052](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1052:1052) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2088 | [1053](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1053:1053) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2089 | [1054](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1054:1054) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2090 | [1055](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1055:1055) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2091 | [1056](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1056:1056) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2092 | [1057](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1057:1057) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2093 | [1058](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1058:1058) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2094 | [1059](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1059:1059) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2095 | [1060](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1060:1060) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2096 | [1061](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1061:1061) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2097 | [1062](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1062:1062) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2098 | [1063](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1063:1063) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2099 | [1064](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1064:1064) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2100 | [1065](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1065:1065) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2101 | [1066](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1066:1066) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2102 | [1067](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1067:1067) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2104 | [1068](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1068:1068) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2106 | [1069](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1069:1069) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2108 | [1070](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1070:1070) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2110 | [1071](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1071:1071) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2112 | [1072](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1072:1072) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2114 | [1073](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1073:1073) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2116 | [1074](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1074:1074) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2118 | [1075](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1075:1075) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2120 | [1076](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1076:1076) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2122 | [1077](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1077:1077) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2124 | [1078](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1078:1078) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2126 | [1079](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1079:1079) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2128 | [1080](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1080:1080) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2130 | [1081](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1081:1081) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2132 | [1082](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1082:1082) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |
| 2134 | [1083](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1083:1083) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan           |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|      | row_number                                                                                                             | s          | slabel    | user_slabel   | o              | olabel                                  | user_olabel                                  |          deltaIC |
|------|------------------------------------------------------------------------------------------------------------------------|------------|-----------|---------------|----------------|-----------------------------------------|----------------------------------------------|------------------|
|    0 | [503](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=503:503)    | CL:0001035 | bone cell | bone cell     | UBERON:0002396 | vomer                                   | vomer                                        |      3.55322e+13 |
|    1 | [502](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=502:502)    | CL:0001035 | bone cell | bone cell     | UBERON:0002396 | vomer                                   | vomer                                        |      3.55322e+13 |
|    2 | [504](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=504:504)    | CL:0001035 | bone cell | bone cell     | UBERON:0002396 | vomer                                   | vomer                                        |      3.55322e+13 |
|  197 | [246](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=246:246)    | CL:0001035 | bone cell | bone cell     | UBERON:0004326 | middle phalanx of pedal digit 4         | middle phalanx of digit of foot 4            |      6.2446e+06  |
|  198 | [251](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=251:251)    | CL:0001035 | bone cell | bone cell     | UBERON:0004327 | middle phalanx of pedal digit 5         | middle phalanx of digit of foot 5            |      6.2446e+06  |
|  199 | [250](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=250:250)    | CL:0001035 | bone cell | bone cell     | UBERON:0004327 | middle phalanx of pedal digit 5         | middle phalanx of digit of foot 5            |      6.2446e+06  |
|  200 | [249](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=249:249)    | CL:0001035 | bone cell | bone cell     | UBERON:0004327 | middle phalanx of pedal digit 5         | middle phalanx of digit of foot 5            |      6.2446e+06  |
|  201 | [248](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=248:248)    | CL:0001035 | bone cell | bone cell     | UBERON:0004326 | middle phalanx of pedal digit 4         | middle phalanx of digit of foot 4            |      6.2446e+06  |
|  202 | [247](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=247:247)    | CL:0001035 | bone cell | bone cell     | UBERON:0004326 | middle phalanx of pedal digit 4         | middle phalanx of digit of foot 4            |      6.2446e+06  |
|  203 | [245](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=245:245)    | CL:0001035 | bone cell | bone cell     | UBERON:0004326 | middle phalanx of pedal digit 4         | middle phalanx of digit of foot 4            |      6.2446e+06  |
|  204 | [252](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=252:252)    | CL:0001035 | bone cell | bone cell     | UBERON:0004327 | middle phalanx of pedal digit 5         | middle phalanx of digit of foot 5            |      6.2446e+06  |
|  208 | [663](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=663:663)    | CL:0001035 | bone cell | bone cell     | UBERON:0001095 | caudal vertebra                         | caudal vertebra                              |      2.96436e+06 |
|  209 | [387](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=387:387)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 | 221821           |
|  210 | [154](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=154:154)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                | 221821           |
|  211 | [148](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=148:148)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                | 221821           |
|  212 | [385](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=385:385)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 | 221821           |
|  213 | [156](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=156:156)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                | 221821           |
|  214 | [379](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=379:379)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 | 221821           |
|  215 | [149](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=149:149)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                | 221821           |
|  216 | [384](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=384:384)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 | 221821           |
|  217 | [150](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=150:150)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                | 221821           |
|  218 | [386](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=386:386)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 | 221821           |
|  219 | [382](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=382:382)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 | 221821           |
|  220 | [381](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=381:381)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 | 221821           |
|  221 | [152](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=152:152)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                | 221821           |
|  222 | [380](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=380:380)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 | 221821           |
|  223 | [151](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=151:151)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                | 221821           |
|  224 | [155](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=155:155)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                | 221821           |
|  225 | [378](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=378:378)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 | 221821           |
|  226 | [383](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=383:383)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 | 221821           |
|  227 | [410](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=410:410)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  228 | [422](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=422:422)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  229 | [408](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=408:408)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  230 | [411](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=411:411)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  231 | [423](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=423:423)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  232 | [418](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=418:418)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  233 | [409](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=409:409)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  234 | [412](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=412:412)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  235 | [426](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=426:426)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  236 | [414](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=414:414)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  237 | [407](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=407:407)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  238 | [406](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=406:406)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  239 | [415](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=415:415)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  240 | [421](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=421:421)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  241 | [416](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=416:416)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  242 | [420](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=420:420)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  243 | [425](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=425:425)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  244 | [417](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=417:417)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  245 | [427](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=427:427)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  246 | [419](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=419:419)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  247 | [424](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=424:424)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |    525.751       |
|  389 | [635](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=635:635)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  390 | [619](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=619:619)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  391 | [296](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=296:296)    | CL:0001035 | bone cell | bone cell     | UBERON:0009987 | medial epicondyle of femur              | medial epicondyle of femur                   |    100           |
|  392 | [636](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=636:636)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  393 | [317](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=317:317)    | CL:0001035 | bone cell | bone cell     | UBERON:0009990 | medial condyle of tibia                 | medial condyle of tibia                      |    100           |
|  394 | [592](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=592:592)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  395 | [634](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=634:634)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  396 | [618](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=618:618)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  397 | [617](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=617:617)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  398 | [639](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=639:639)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  399 | [638](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=638:638)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  400 | [620](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=620:620)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  401 | [413](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=413:413)    | CL:0001035 | bone cell | bone cell     | UBERON:0016492 | foramen spinosum of sphenoid bone       | foramen spinosum of sphenoid bone            |    100           |
|  402 | [633](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=633:633)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  403 | [624](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=624:624)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  404 | [625](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=625:625)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  405 | [623](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=623:623)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  406 | [171](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=171:171)    | CL:0001035 | bone cell | bone cell     | UBERON:0007176 | superior angle of scapula               | superior angle of scapula                    |    100           |
|  407 | [626](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=626:626)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  408 | [627](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=627:627)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  409 | [628](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=628:628)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  410 | [640](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=640:640)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  411 | [629](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=629:629)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  412 | [630](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=630:630)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  413 | [622](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=622:622)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  414 | [631](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=631:631)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  415 | [632](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=632:632)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  416 | [307](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=307:307)    | CL:0001035 | bone cell | bone cell     | UBERON:0018673 | neck of fibula                          | neck of fibula                               |    100           |
|  417 | [621](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=621:621)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  418 | [591](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=591:591)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  419 | [644](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=644:644)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  420 | [641](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=641:641)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  421 | [940](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=940:940)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  422 | [935](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=935:935)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  423 | [528](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=528:528)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |    100           |
|  424 | [936](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=936:936)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  425 | [527](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=527:527)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |    100           |
|  426 | [937](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=937:937)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  427 | [526](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=526:526)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |    100           |
|  428 | [938](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=938:938)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  429 | [939](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=939:939)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  430 | [508](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=508:508)    | CL:0001035 | bone cell | bone cell     | UBERON:0004654 | temporal process of zygomatic bone      | temporal process of zygomatic bone           |    100           |
|  431 | [642](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=642:642)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  432 | [941](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=941:941)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  433 | [942](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=942:942)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  434 | [943](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=943:943)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  435 | [944](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=944:944)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  436 | [945](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=945:945)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  437 | [946](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=946:946)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  438 | [947](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=947:947)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  439 | [26](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=26:26)       | CL:0001035 | bone cell | bone cell     | UBERON:0011188 | lesser tubercle of humerus              | lesser tubercle of humerus                   |    100           |
|  440 | [529](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=529:529)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |    100           |
|  441 | [934](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=934:934)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  442 | [530](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=530:530)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |    100           |
|  443 | [933](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=933:933)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |    100           |
|  444 | [643](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=643:643)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  445 | [645](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=645:645)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  446 | [646](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=646:646)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  447 | [647](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=647:647)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  448 | [648](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=648:648)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  449 | [649](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=649:649)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  450 | [650](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=650:650)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  451 | [651](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=651:651)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |    100           |
|  452 | [538](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=538:538)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |    100           |
|  453 | [537](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=537:537)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |    100           |
|  454 | [536](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=536:536)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |    100           |
|  455 | [535](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=535:535)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |    100           |
|  456 | [534](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=534:534)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |    100           |
|  457 | [533](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=533:533)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |    100           |
|  458 | [532](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=532:532)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |    100           |
|  459 | [460](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=460:460)    | CL:0001035 | bone cell | bone cell     | UBERON:0011309 | body of mandible                        | body of mandible                             |    100           |
|  460 | [531](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=531:531)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |    100           |
|  461 | [616](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=616:616)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  462 | [637](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=637:637)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |    100           |
|  463 | [615](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=615:615)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  464 | [572](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=572:572)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  465 | [598](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=598:598)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  466 | [577](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=577:577)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  467 | [576](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=576:576)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  468 | [599](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=599:599)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  469 | [574](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=574:574)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  470 | [573](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=573:573)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  471 | [600](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=600:600)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  472 | [597](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=597:597)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  473 | [571](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=571:571)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  474 | [570](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=570:570)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  475 | [569](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=569:569)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  476 | [568](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=568:568)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  477 | [601](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=601:601)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  478 | [567](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=567:567)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  479 | [578](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=578:578)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  480 | [579](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=579:579)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  481 | [603](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=603:603)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  482 | [586](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=586:586)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  483 | [590](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=590:590)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  484 | [589](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=589:589)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  485 | [593](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=593:593)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  486 | [588](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=588:588)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  487 | [587](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=587:587)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  488 | [594](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=594:594)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  489 | [585](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=585:585)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  490 | [580](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=580:580)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  491 | [595](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=595:595)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  492 | [584](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=584:584)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  493 | [583](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=583:583)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  494 | [582](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=582:582)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  495 | [596](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=596:596)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |    100           |
|  496 | [581](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=581:581)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  497 | [602](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=602:602)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  498 | [575](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=575:575)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |    100           |
|  499 | [604](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=604:604)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  500 | [610](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=610:610)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  501 | [614](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=614:614)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  502 | [539](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=539:539)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |    100           |
|  503 | [613](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=613:613)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |    100           |
|  504 | [540](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=540:540)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |    100           |
|  505 | [605](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=605:605)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  506 | [542](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=542:542)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |    100           |
|  507 | [561](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=561:561)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  508 | [612](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=612:612)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  509 | [562](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=562:562)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  510 | [563](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=563:563)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  511 | [564](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=564:564)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  512 | [565](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=565:565)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  513 | [611](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=611:611)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  514 | [566](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=566:566)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |    100           |
|  515 | [541](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=541:541)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |    100           |
|  516 | [606](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=606:606)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  517 | [607](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=607:607)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  518 | [608](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=608:608)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  519 | [609](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=609:609)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |    100           |
|  557 | [976](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=976:976)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  558 | [969](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=969:969)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  559 | [970](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=970:970)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  560 | [971](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=971:971)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  561 | [972](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=972:972)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  562 | [973](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=973:973)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  563 | [975](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=975:975)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  564 | [979](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=979:979)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  565 | [977](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=977:977)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  566 | [978](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=978:978)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  567 | [980](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=980:980)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  568 | [494](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=494:494)    | CL:0001035 | bone cell | bone cell     | UBERON:0005871 | palatine process of maxilla             | palatine process of maxilla                  |      3.27466e-10 |
|  569 | [981](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=981:981)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  570 | [482](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=482:482)    | CL:0001035 | bone cell | bone cell     | UBERON:0004527 | alveolar process of maxilla             | alveolar process of maxilla                  |      3.27466e-10 |
|  571 | [967](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=967:967)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  572 | [968](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=968:968)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  573 | [974](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=974:974)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  574 | [966](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=966:966)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  575 | [456](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=456:456)    | CL:0001035 | bone cell | bone cell     | UBERON:0001680 | lacrimal bone                           | lacrimal bone                                |      3.27466e-10 |
|  576 | [457](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=457:457)    | CL:0001035 | bone cell | bone cell     | UBERON:0001680 | lacrimal bone                           | lacrimal bone                                |      3.27466e-10 |
|  577 | [965](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=965:965)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |      3.27466e-10 |
|  578 | [1064](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1064:1064) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  579 | [782](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=782:782)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  580 | [750](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=750:750)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  581 | [1055](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1055:1055) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  582 | [759](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=759:759)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  583 | [1056](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1056:1056) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  584 | [758](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=758:758)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  585 | [1057](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1057:1057) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  586 | [796](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=796:796)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  587 | [1058](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1058:1058) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  588 | [795](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=795:795)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  589 | [1059](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1059:1059) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  590 | [794](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=794:794)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  591 | [1054](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1054:1054) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  592 | [783](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=783:783)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  593 | [1061](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1061:1061) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  594 | [793](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=793:793)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  595 | [1062](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1062:1062) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  596 | [1065](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1065:1065) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  597 | [792](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=792:792)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  598 | [1063](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1063:1063) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  599 | [1060](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1060:1060) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  600 | [756](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=756:756)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  601 | [1053](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1053:1053) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  602 | [752](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=752:752)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  603 | [781](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=781:781)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  604 | [785](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=785:785)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  605 | [784](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=784:784)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  606 | [763](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=763:763)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  607 | [762](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=762:762)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  608 | [791](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=791:791)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  609 | [754](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=754:754)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  610 | [788](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=788:788)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  611 | [761](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=761:761)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  612 | [755](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=755:755)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  613 | [753](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=753:753)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  614 | [751](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=751:751)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  615 | [760](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=760:760)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  616 | [749](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=749:749)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  617 | [787](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=787:787)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  618 | [1050](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1050:1050) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  619 | [757](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=757:757)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |      2.07943e-14 |
|  620 | [789](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=789:789)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  621 | [1051](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1051:1051) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  622 | [786](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=786:786)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  623 | [1052](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1052:1052) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  624 | [790](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=790:790)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |      2.07943e-14 |
|  625 | [1066](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1066:1066) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |      2.07943e-14 |
|  626 | [306](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=306:306)    | CL:0001035 | bone cell | bone cell     | UBERON:0012291 | lateral malleolus of fibula             | lateral malleolus of fibula                  |      2.07943e-14 |
|  627 | [693](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=693:693)    | CL:0001035 | bone cell | bone cell     | UBERON:0004096 | odontoid process of cervical vertebra 2 | odontoid process of second cervical vertebra |      1.82157e-14 |
|  628 | [253](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=253:253)    | CL:0001035 | bone cell | bone cell     | UBERON:0001451 | navicular bone of pes                   | navicular bone of foot                       |      1.82157e-14 |
|  629 | [254](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=254:254)    | CL:0001035 | bone cell | bone cell     | UBERON:0001451 | navicular bone of pes                   | navicular bone of foot                       |      1.82157e-14 |
|  630 | [263](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=263:263)    | CL:0001035 | bone cell | bone cell     | UBERON:0004334 | proximal phalanx of pedal digit 3       | proximal phalanx of digit of foot 3          |      1.0307e-16  |
|  631 | [264](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=264:264)    | CL:0001035 | bone cell | bone cell     | UBERON:0004334 | proximal phalanx of pedal digit 3       | proximal phalanx of digit of foot 3          |      1.0307e-16  |
|  632 | [265](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=265:265)    | CL:0001035 | bone cell | bone cell     | UBERON:0004334 | proximal phalanx of pedal digit 3       | proximal phalanx of digit of foot 3          |      1.0307e-16  |
|  633 | [266](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=266:266)    | CL:0001035 | bone cell | bone cell     | UBERON:0004334 | proximal phalanx of pedal digit 3       | proximal phalanx of digit of foot 3          |      1.0307e-16  |
|  634 | [197](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=197:197)    | CL:0001035 | bone cell | bone cell     | UBERON:0004316 | distal phalanx of pedal digit 2         | distal phalanx of digit of foot 2            |      1.02909e-16 |
|  635 | [509](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=509:509)    | CL:0001035 | bone cell | bone cell     | UBERON:0001683 | jugal bone                              | zygomatic bone                               |      1.02909e-16 |
|  636 | [507](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=507:507)    | CL:0001035 | bone cell | bone cell     | UBERON:0001683 | jugal bone                              | zygomatic bone                               |      1.02909e-16 |
|  637 | [505](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=505:505)    | CL:0001035 | bone cell | bone cell     | UBERON:0001683 | jugal bone                              | zygomatic bone                               |      1.02909e-16 |
|  638 | [199](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=199:199)    | CL:0001035 | bone cell | bone cell     | UBERON:0004316 | distal phalanx of pedal digit 2         | distal phalanx of digit of foot 2            |      1.02909e-16 |
|  639 | [200](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=200:200)    | CL:0001035 | bone cell | bone cell     | UBERON:0004316 | distal phalanx of pedal digit 2         | distal phalanx of digit of foot 2            |      1.02909e-16 |
|  640 | [198](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=198:198)    | CL:0001035 | bone cell | bone cell     | UBERON:0004316 | distal phalanx of pedal digit 2         | distal phalanx of digit of foot 2            |      1.02909e-16 |
|  641 | [113](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=113:113)    | CL:0001035 | bone cell | bone cell     | UBERON:0004321 | middle phalanx of manual digit 3        | middle phalanx of digit of hand 3            |      1.02908e-16 |
|  642 | [138](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=138:138)    | CL:0001035 | bone cell | bone cell     | UBERON:0004330 | proximal phalanx of manual digit 4      | proximal phalanx of digit of hand 4          |      1.02908e-16 |
|  643 | [137](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=137:137)    | CL:0001035 | bone cell | bone cell     | UBERON:0004330 | proximal phalanx of manual digit 4      | proximal phalanx of digit of hand 4          |      1.02908e-16 |
|  644 | [136](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=136:136)    | CL:0001035 | bone cell | bone cell     | UBERON:0004330 | proximal phalanx of manual digit 4      | proximal phalanx of digit of hand 4          |      1.02908e-16 |
|  645 | [135](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=135:135)    | CL:0001035 | bone cell | bone cell     | UBERON:0004329 | proximal phalanx of manual digit 3      | proximal phalanx of digit of hand 3          |      1.02908e-16 |
|  646 | [134](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=134:134)    | CL:0001035 | bone cell | bone cell     | UBERON:0004329 | proximal phalanx of manual digit 3      | proximal phalanx of digit of hand 3          |      1.02908e-16 |
|  647 | [132](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=132:132)    | CL:0001035 | bone cell | bone cell     | UBERON:0004329 | proximal phalanx of manual digit 3      | proximal phalanx of digit of hand 3          |      1.02908e-16 |
|  648 | [286](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=286:286)    | CL:0001035 | bone cell | bone cell     | UBERON:0006767 | head of femur                           | head of femur                                |      1.02908e-16 |
|  649 | [112](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=112:112)    | CL:0001035 | bone cell | bone cell     | UBERON:0004321 | middle phalanx of manual digit 3        | middle phalanx of digit of hand 3            |      1.02908e-16 |
|  650 | [118](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=118:118)    | CL:0001035 | bone cell | bone cell     | UBERON:0004322 | middle phalanx of manual digit 4        | middle phalanx of digit of hand 4            |      1.02908e-16 |
|  651 | [117](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=117:117)    | CL:0001035 | bone cell | bone cell     | UBERON:0004322 | middle phalanx of manual digit 4        | middle phalanx of digit of hand 4            |      1.02908e-16 |
|  652 | [116](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=116:116)    | CL:0001035 | bone cell | bone cell     | UBERON:0004322 | middle phalanx of manual digit 4        | middle phalanx of digit of hand 4            |      1.02908e-16 |
|  653 | [115](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=115:115)    | CL:0001035 | bone cell | bone cell     | UBERON:0004322 | middle phalanx of manual digit 4        | middle phalanx of digit of hand 4            |      1.02908e-16 |
|  654 | [114](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=114:114)    | CL:0001035 | bone cell | bone cell     | UBERON:0004321 | middle phalanx of manual digit 3        | middle phalanx of digit of hand 3            |      1.02908e-16 |
|  655 | [111](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=111:111)    | CL:0001035 | bone cell | bone cell     | UBERON:0004321 | middle phalanx of manual digit 3        | middle phalanx of digit of hand 3            |      1.02908e-16 |
|  656 | [139](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=139:139)    | CL:0001035 | bone cell | bone cell     | UBERON:0004330 | proximal phalanx of manual digit 4      | proximal phalanx of digit of hand 4          |      1.02908e-16 |
|  657 | [133](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=133:133)    | CL:0001035 | bone cell | bone cell     | UBERON:0004329 | proximal phalanx of manual digit 3      | proximal phalanx of digit of hand 3          |      1.02908e-16 |
|  658 | [323](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=323:323)    | CL:0001035 | bone cell | bone cell     | UBERON:0007830 | pelvic girdle bone/zone                 | pelvic girdle bone/zone                      |      1.02908e-16 |
|  659 | [451](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=451:451)    | CL:0001035 | bone cell | bone cell     | UBERON:0001688 | incus bone                              | incus bone                                   |      1.02908e-16 |
|  660 | [99](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=99:99)       | CL:0001035 | bone cell | bone cell     | UBERON:0003648 | metacarpal bone of digit 4              | metacarpal bone of digit 4                   |      1.02908e-16 |
|  661 | [100](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=100:100)    | CL:0001035 | bone cell | bone cell     | UBERON:0003648 | metacarpal bone of digit 4              | metacarpal bone of digit 4                   |      1.02908e-16 |
|  662 | [101](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=101:101)    | CL:0001035 | bone cell | bone cell     | UBERON:0003648 | metacarpal bone of digit 4              | metacarpal bone of digit 4                   |      1.02908e-16 |
|  663 | [102](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=102:102)    | CL:0001035 | bone cell | bone cell     | UBERON:0003648 | metacarpal bone of digit 4              | metacarpal bone of digit 4                   |      1.02908e-16 |
|  664 | [62](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=62:62)       | CL:0001035 | bone cell | bone cell     | UBERON:0004337 | distal phalanx of manual digit 1        | distal phalanx of digit of hand 1            |      1.02908e-16 |
|  665 | [65](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=65:65)       | CL:0001035 | bone cell | bone cell     | UBERON:0004337 | distal phalanx of manual digit 1        | distal phalanx of digit of hand 1            |      1.02908e-16 |
|  666 | [64](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=64:64)       | CL:0001035 | bone cell | bone cell     | UBERON:0004337 | distal phalanx of manual digit 1        | distal phalanx of digit of hand 1            |      1.02908e-16 |
|  667 | [63](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=63:63)       | CL:0001035 | bone cell | bone cell     | UBERON:0004337 | distal phalanx of manual digit 1        | distal phalanx of digit of hand 1            |      1.02908e-16 |
|  668 | [61](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=61:61)       | CL:0001035 | bone cell | bone cell     | UBERON:0004337 | distal phalanx of manual digit 1        | distal phalanx of digit of hand 1            |      1.02908e-16 |
|  669 | [55](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=55:55)       | CL:0001035 | bone cell | bone cell     | UBERON:0005897 | manus bone                              | hand bone                                    |      1.02908e-16 |
|  670 | [49](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=49:49)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |      1.02908e-16 |
|  671 | [46](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=46:46)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |      1.02908e-16 |
|  672 | [54](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=54:54)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |      1.02908e-16 |
|  673 | [53](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=53:53)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |      1.02908e-16 |
|  674 | [52](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=52:52)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |      1.02908e-16 |
|  675 | [51](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=51:51)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |      1.02908e-16 |
|  676 | [45](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=45:45)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |      1.02908e-16 |
|  677 | [48](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=48:48)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |      1.02908e-16 |
|  678 | [43](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=43:43)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |      1.02908e-16 |
|  679 | [47](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=47:47)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |      1.02908e-16 |
|  680 | [780](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=780:780)    | CL:0001035 | bone cell | bone cell     | UBERON:0002414 | lumbar vertebra                         | lumbar vertebra                              |      1.02908e-16 |
|  681 | [865](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=865:865)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  682 | [878](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=878:878)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  683 | [187](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=187:187)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  684 | [842](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=842:842)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  685 | [843](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=843:843)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  686 | [872](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=872:872)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  687 | [844](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=844:844)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  688 | [861](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=861:861)    | CL:0001035 | bone cell | bone cell     | UBERON:0001094 | sacral vertebra                         | sacral vertebra                              |      1.02908e-16 |
|  689 | [862](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=862:862)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  690 | [863](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=863:863)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  691 | [864](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=864:864)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  692 | [879](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=879:879)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  693 | [877](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=877:877)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  694 | [186](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=186:186)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  695 | [876](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=876:876)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  696 | [871](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=871:871)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  697 | [870](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=870:870)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  698 | [869](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=869:869)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  699 | [868](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=868:868)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  700 | [873](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=873:873)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  701 | [867](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=867:867)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  702 | [866](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=866:866)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  703 | [875](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=875:875)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  704 | [874](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=874:874)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  705 | [769](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=769:769)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  706 | [838](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=838:838)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  707 | [841](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=841:841)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  708 | [180](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=180:180)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  709 | [765](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=765:765)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  710 | [766](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=766:766)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  711 | [767](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=767:767)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  712 | [153](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=153:153)    | CL:0001035 | bone cell | bone cell     | UBERON:0006805 | sternal end of clavicle                 | sternal end of clavicle                      |      1.02908e-16 |
|  713 | [177](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=177:177)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  714 | [768](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=768:768)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  715 | [178](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=178:178)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  716 | [179](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=179:179)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  717 | [779](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=779:779)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  718 | [840](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=840:840)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  719 | [778](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=778:778)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  720 | [777](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=777:777)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  721 | [776](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=776:776)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  722 | [775](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=775:775)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  723 | [774](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=774:774)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  724 | [773](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=773:773)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  725 | [772](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=772:772)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  726 | [771](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=771:771)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  727 | [764](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=764:764)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  728 | [181](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=181:181)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  729 | [182](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=182:182)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  730 | [881](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=881:881)    | CL:0001035 | bone cell | bone cell     | UBERON:0002347 | thoracic vertebra                       | thoracic vertebra                            |      1.02908e-16 |
|  731 | [839](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=839:839)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  732 | [770](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=770:770)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |      1.02908e-16 |
|  733 | [837](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=837:837)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  734 | [185](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=185:185)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  735 | [184](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=184:184)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  736 | [836](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=836:836)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  737 | [835](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=835:835)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  738 | [834](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=834:834)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  739 | [833](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=833:833)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  740 | [832](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=832:832)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  741 | [831](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=831:831)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  742 | [830](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=830:830)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  743 | [829](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=829:829)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |      1.02908e-16 |
|  744 | [120](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=120:120)    | CL:0001035 | bone cell | bone cell     | UBERON:0004323 | middle phalanx of manual digit 5        | middle phalanx of digit of hand 5            |      1.02908e-16 |
|  745 | [121](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=121:121)    | CL:0001035 | bone cell | bone cell     | UBERON:0004323 | middle phalanx of manual digit 5        | middle phalanx of digit of hand 5            |      1.02908e-16 |
|  746 | [122](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=122:122)    | CL:0001035 | bone cell | bone cell     | UBERON:0004323 | middle phalanx of manual digit 5        | middle phalanx of digit of hand 5            |      1.02908e-16 |
|  747 | [183](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=183:183)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  748 | [880](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=880:880)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |      1.02908e-16 |
|  749 | [497](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=497:497)    | CL:0001035 | bone cell | bone cell     | UBERON:0001682 | palatine bone                           | palatine bone                                |      1.02908e-16 |
|  750 | [916](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=916:916)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  751 | [70](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=70:70)       | CL:0001035 | bone cell | bone cell     | UBERON:0004311 | distal phalanx of manual digit 2        | distal phalanx of digit of hand 2            |      1.02908e-16 |
|  752 | [997](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=997:997)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  753 | [996](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=996:996)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  754 | [995](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=995:995)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  755 | [994](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=994:994)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  756 | [993](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=993:993)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  757 | [992](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=992:992)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  758 | [991](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=991:991)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  759 | [990](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=990:990)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  760 | [989](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=989:989)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  761 | [988](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=988:988)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  762 | [987](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=987:987)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  763 | [986](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=986:986)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  764 | [985](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=985:985)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  765 | [984](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=984:984)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  766 | [983](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=983:983)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  767 | [982](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=982:982)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  768 | [66](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=66:66)       | CL:0001035 | bone cell | bone cell     | UBERON:0004311 | distal phalanx of manual digit 2        | distal phalanx of digit of hand 2            |      1.02908e-16 |
|  769 | [67](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=67:67)       | CL:0001035 | bone cell | bone cell     | UBERON:0004311 | distal phalanx of manual digit 2        | distal phalanx of digit of hand 2            |      1.02908e-16 |
|  770 | [68](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=68:68)       | CL:0001035 | bone cell | bone cell     | UBERON:0004311 | distal phalanx of manual digit 2        | distal phalanx of digit of hand 2            |      1.02908e-16 |
|  771 | [998](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=998:998)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |      1.02908e-16 |
|  772 | [1016](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1016:1016) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  773 | [1017](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1017:1017) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  774 | [1028](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1028:1028) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  775 | [18](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=18:18)       | CL:0001035 | bone cell | bone cell     | UBERON:0010853 | capitulum of humerus                    | capitulum of humerus                         |      1.02908e-16 |
|  776 | [34](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=34:34)       | CL:0001035 | bone cell | bone cell     | UBERON:0000144 | trochlea of humerus                     | trochlea of humerus                          |      1.02908e-16 |
|  777 | [50](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=50:50)       | CL:0001035 | bone cell | bone cell     | UBERON:0011575 | styloid process of ulna                 | styloid process of ulna                      |      1.02908e-16 |
|  778 | [56](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=56:56)       | CL:0001035 | bone cell | bone cell     | UBERON:0001430 | distal carpal bone 1                    | distal carpal bone 1                         |      1.02908e-16 |
|  779 | [1032](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1032:1032) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  780 | [1031](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1031:1031) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  781 | [1030](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1030:1030) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  782 | [1029](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1029:1029) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  783 | [1027](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1027:1027) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  784 | [1018](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1018:1018) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  785 | [1026](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1026:1026) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  786 | [1025](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1025:1025) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  787 | [1024](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1024:1024) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  788 | [1023](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1023:1023) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  789 | [1022](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1022:1022) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  790 | [1021](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1021:1021) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  791 | [1020](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1020:1020) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  792 | [1019](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1019:1019) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |      1.02908e-16 |
|  793 | [69](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=69:69)       | CL:0001035 | bone cell | bone cell     | UBERON:0004311 | distal phalanx of manual digit 2        | distal phalanx of digit of hand 2            |      1.02908e-16 |
|  794 | [71](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=71:71)       | CL:0001035 | bone cell | bone cell     | UBERON:0004312 | distal phalanx of manual digit 3        | distal phalanx of digit of hand 3            |      1.02908e-16 |
|  795 | [917](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=917:917)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  796 | [72](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=72:72)       | CL:0001035 | bone cell | bone cell     | UBERON:0004312 | distal phalanx of manual digit 3        | distal phalanx of digit of hand 3            |      1.02908e-16 |
|  797 | [948](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=948:948)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  798 | [93](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=93:93)       | CL:0001035 | bone cell | bone cell     | UBERON:0003646 | metacarpal bone of digit 2              | metacarpal bone of digit 2                   |      1.02908e-16 |
|  799 | [94](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=94:94)       | CL:0001035 | bone cell | bone cell     | UBERON:0003646 | metacarpal bone of digit 2              | metacarpal bone of digit 2                   |      1.02908e-16 |
|  800 | [119](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=119:119)    | CL:0001035 | bone cell | bone cell     | UBERON:0004323 | middle phalanx of manual digit 5        | middle phalanx of digit of hand 5            |      1.02908e-16 |
|  801 | [932](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=932:932)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  802 | [188](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=188:188)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  803 | [930](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=930:930)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  804 | [929](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=929:929)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  805 | [928](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=928:928)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  806 | [927](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=927:927)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  807 | [926](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=926:926)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  808 | [925](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=925:925)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  809 | [924](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=924:924)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  810 | [923](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=923:923)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  811 | [922](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=922:922)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  812 | [921](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=921:921)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  813 | [920](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=920:920)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  814 | [919](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=919:919)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  815 | [918](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=918:918)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  816 | [949](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=949:949)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  817 | [950](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=950:950)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  818 | [951](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=951:951)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  819 | [962](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=962:962)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  820 | [73](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=73:73)       | CL:0001035 | bone cell | bone cell     | UBERON:0004312 | distal phalanx of manual digit 3        | distal phalanx of digit of hand 3            |      1.02908e-16 |
|  821 | [74](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=74:74)       | CL:0001035 | bone cell | bone cell     | UBERON:0004312 | distal phalanx of manual digit 3        | distal phalanx of digit of hand 3            |      1.02908e-16 |
|  822 | [75](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=75:75)       | CL:0001035 | bone cell | bone cell     | UBERON:0004312 | distal phalanx of manual digit 3        | distal phalanx of digit of hand 3            |      1.02908e-16 |
|  823 | [86](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=86:86)       | CL:0001035 | bone cell | bone cell     | UBERON:0001428 | intermedium                             | lunate                                       |      1.02908e-16 |
|  824 | [91](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=91:91)       | CL:0001035 | bone cell | bone cell     | UBERON:0003646 | metacarpal bone of digit 2              | metacarpal bone of digit 2                   |      1.02908e-16 |
|  825 | [92](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=92:92)       | CL:0001035 | bone cell | bone cell     | UBERON:0003646 | metacarpal bone of digit 2              | metacarpal bone of digit 2                   |      1.02908e-16 |
|  826 | [964](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=964:964)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  827 | [963](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=963:963)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  828 | [961](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=961:961)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  829 | [952](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=952:952)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  830 | [960](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=960:960)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  831 | [959](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=959:959)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  832 | [958](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=958:958)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  833 | [957](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=957:957)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  834 | [956](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=956:956)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  835 | [955](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=955:955)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  836 | [954](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=954:954)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  837 | [953](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=953:953)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |      1.02908e-16 |
|  838 | [931](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=931:931)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |      1.02908e-16 |
|  839 | [731](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=731:731)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  840 | [189](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=189:189)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |      1.02908e-16 |
|  841 | [353](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=353:353)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  842 | [355](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=355:355)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  843 | [356](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=356:356)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  844 | [357](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=357:357)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  845 | [358](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=358:358)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  846 | [359](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=359:359)    | CL:0001035 | bone cell | bone cell     | UBERON:0005944 | axial skeleton plus cranial skeleton    | axial skeleton                               |      1.02908e-16 |
|  847 | [362](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=362:362)    | CL:0001035 | bone cell | bone cell     | UBERON:0001685 | hyoid bone                              | hyoid bone                                   |      1.02908e-16 |
|  848 | [363](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=363:363)    | CL:0001035 | bone cell | bone cell     | UBERON:0001685 | hyoid bone                              | hyoid bone                                   |      1.02908e-16 |
|  849 | [364](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=364:364)    | CL:0001035 | bone cell | bone cell     | UBERON:0001685 | hyoid bone                              | hyoid bone                                   |      1.02908e-16 |
|  850 | [365](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=365:365)    | CL:0001035 | bone cell | bone cell     | UBERON:0001685 | hyoid bone                              | hyoid bone                                   |      1.02908e-16 |
|  851 | [367](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=367:367)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |      1.02908e-16 |
|  852 | [368](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=368:368)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |      1.02908e-16 |
|  853 | [369](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=369:369)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |      1.02908e-16 |
|  854 | [370](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=370:370)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |      1.02908e-16 |
|  855 | [371](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=371:371)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |      1.02908e-16 |
|  856 | [372](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=372:372)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |      1.02908e-16 |
|  857 | [373](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=373:373)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |      1.02908e-16 |
|  858 | [374](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=374:374)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |      1.02908e-16 |
|  859 | [375](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=375:375)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |      1.02908e-16 |
|  860 | [376](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=376:376)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |      1.02908e-16 |
|  861 | [354](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=354:354)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  862 | [352](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=352:352)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  863 | [15](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=15:15)       | CL:0001035 | bone cell | bone cell     | UBERON:0003460 | arm bone                                | arm bone                                     |      1.02908e-16 |
|  864 | [351](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=351:351)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  865 | [332](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=332:332)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  866 | [333](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=333:333)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  867 | [334](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=334:334)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  868 | [205](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=205:205)    | CL:0001035 | bone cell | bone cell     | UBERON:0004318 | distal phalanx of pedal digit 4         | distal phalanx of digit of foot 4            |      1.02908e-16 |
|  869 | [336](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=336:336)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  870 | [337](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=337:337)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  871 | [338](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=338:338)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  872 | [339](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=339:339)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  873 | [340](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=340:340)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  874 | [341](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=341:341)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  875 | [342](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=342:342)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  876 | [343](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=343:343)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  877 | [344](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=344:344)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  878 | [345](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=345:345)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  879 | [346](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=346:346)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  880 | [347](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=347:347)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  881 | [348](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=348:348)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  882 | [349](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=349:349)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  883 | [350](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=350:350)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  884 | [377](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=377:377)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |      1.02908e-16 |
|  885 | [453](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=453:453)    | CL:0001035 | bone cell | bone cell     | UBERON:0001687 | stapes bone                             | stapes bone                                  |      1.02908e-16 |
|  886 | [330](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=330:330)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  887 | [511](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=511:511)    | CL:0001035 | bone cell | bone cell     | UBERON:0014477 | thoracic skeleton                       | thoracic skeleton                            |      1.02908e-16 |
|  888 | [467](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=467:467)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  889 | [468](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=468:468)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  890 | [469](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=469:469)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  891 | [470](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=470:470)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  892 | [506](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=506:506)    | CL:0001035 | bone cell | bone cell     | UBERON:0012110 | frontal process of zygomatic bone       | frontal process of zygomatic bone            |      1.02908e-16 |
|  893 | [471](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=471:471)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  894 | [472](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=472:472)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  895 | [473](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=473:473)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  896 | [474](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=474:474)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  897 | [475](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=475:475)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  898 | [476](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=476:476)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  899 | [477](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=477:477)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  900 | [478](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=478:478)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  901 | [501](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=501:501)    | CL:0001035 | bone cell | bone cell     | UBERON:0001682 | palatine bone                           | palatine bone                                |      1.02908e-16 |
|  902 | [479](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=479:479)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  903 | [500](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=500:500)    | CL:0001035 | bone cell | bone cell     | UBERON:0001682 | palatine bone                           | palatine bone                                |      1.02908e-16 |
|  904 | [495](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=495:495)    | CL:0001035 | bone cell | bone cell     | UBERON:0016477 | zygomatic process of maxilla            | zygomatic process of maxilla                 |      1.02908e-16 |
|  905 | [499](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=499:499)    | CL:0001035 | bone cell | bone cell     | UBERON:0001682 | palatine bone                           | palatine bone                                |      1.02908e-16 |
|  906 | [496](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=496:496)    | CL:0001035 | bone cell | bone cell     | UBERON:0001681 | nasal bone                              | nasal bone                                   |      1.02908e-16 |
|  907 | [510](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=510:510)    | CL:0001035 | bone cell | bone cell     | UBERON:0014477 | thoracic skeleton                       | thoracic skeleton                            |      1.02908e-16 |
|  908 | [512](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=512:512)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  909 | [458](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=458:458)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  910 | [513](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=513:513)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  911 | [459](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=459:459)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  912 | [461](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=461:461)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  913 | [462](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=462:462)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  914 | [463](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=463:463)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  915 | [464](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=464:464)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  916 | [465](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=465:465)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  917 | [466](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=466:466)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |      1.02908e-16 |
|  918 | [525](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=525:525)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  919 | [524](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=524:524)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  920 | [523](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=523:523)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  921 | [522](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=522:522)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  922 | [521](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=521:521)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  923 | [520](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=520:520)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  924 | [519](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=519:519)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  925 | [518](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=518:518)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  926 | [517](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=517:517)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  927 | [516](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=516:516)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  928 | [515](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=515:515)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  929 | [514](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=514:514)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |      1.02908e-16 |
|  930 | [331](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=331:331)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  931 | [335](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=335:335)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  932 | [329](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=329:329)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  933 | [231](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=231:231)    | CL:0001035 | bone cell | bone cell     | UBERON:0003653 | metatarsal bone of digit 4              | metatarsal bone of digit 4                   |      1.02908e-16 |
|  934 | [218](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=218:218)    | CL:0001035 | bone cell | bone cell     | UBERON:0003650 | metatarsal bone of digit 1              | metatarsal bone of digit 1                   |      1.02908e-16 |
|  935 | [219](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=219:219)    | CL:0001035 | bone cell | bone cell     | UBERON:0003650 | metatarsal bone of digit 1              | metatarsal bone of digit 1                   |      1.02908e-16 |
|  936 | [220](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=220:220)    | CL:0001035 | bone cell | bone cell     | UBERON:0003651 | metatarsal bone of digit 2              | metatarsal bone of digit 2                   |      1.02908e-16 |
|  937 | [221](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=221:221)    | CL:0001035 | bone cell | bone cell     | UBERON:0003651 | metatarsal bone of digit 2              | metatarsal bone of digit 2                   |      1.02908e-16 |
|  938 | [222](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=222:222)    | CL:0001035 | bone cell | bone cell     | UBERON:0003651 | metatarsal bone of digit 2              | metatarsal bone of digit 2                   |      1.02908e-16 |
|  939 | [223](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=223:223)    | CL:0001035 | bone cell | bone cell     | UBERON:0003651 | metatarsal bone of digit 2              | metatarsal bone of digit 2                   |      1.02908e-16 |
|  940 | [228](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=228:228)    | CL:0001035 | bone cell | bone cell     | UBERON:0003653 | metatarsal bone of digit 4              | metatarsal bone of digit 4                   |      1.02908e-16 |
|  941 | [229](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=229:229)    | CL:0001035 | bone cell | bone cell     | UBERON:0003653 | metatarsal bone of digit 4              | metatarsal bone of digit 4                   |      1.02908e-16 |
|  942 | [230](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=230:230)    | CL:0001035 | bone cell | bone cell     | UBERON:0003653 | metatarsal bone of digit 4              | metatarsal bone of digit 4                   |      1.02908e-16 |
|  943 | [232](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=232:232)    | CL:0001035 | bone cell | bone cell     | UBERON:0003654 | metatarsal bone of digit 5              | metatarsal bone of digit 5                   |      1.02908e-16 |
|  944 | [216](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=216:216)    | CL:0001035 | bone cell | bone cell     | UBERON:0003650 | metatarsal bone of digit 1              | metatarsal bone of digit 1                   |      1.02908e-16 |
|  945 | [233](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=233:233)    | CL:0001035 | bone cell | bone cell     | UBERON:0003654 | metatarsal bone of digit 5              | metatarsal bone of digit 5                   |      1.02908e-16 |
|  946 | [234](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=234:234)    | CL:0001035 | bone cell | bone cell     | UBERON:0003654 | metatarsal bone of digit 5              | metatarsal bone of digit 5                   |      1.02908e-16 |
|  947 | [235](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=235:235)    | CL:0001035 | bone cell | bone cell     | UBERON:0003654 | metatarsal bone of digit 5              | metatarsal bone of digit 5                   |      1.02908e-16 |
|  948 | [236](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=236:236)    | CL:0001035 | bone cell | bone cell     | UBERON:0003654 | metatarsal bone of digit 5              | metatarsal bone of digit 5                   |      1.02908e-16 |
|  949 | [237](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=237:237)    | CL:0001035 | bone cell | bone cell     | UBERON:0004324 | middle phalanx of pedal digit 2         | middle phalanx of digit of foot 2            |      1.02908e-16 |
|  950 | [238](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=238:238)    | CL:0001035 | bone cell | bone cell     | UBERON:0004324 | middle phalanx of pedal digit 2         | middle phalanx of digit of foot 2            |      1.02908e-16 |
|  951 | [239](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=239:239)    | CL:0001035 | bone cell | bone cell     | UBERON:0004324 | middle phalanx of pedal digit 2         | middle phalanx of digit of foot 2            |      1.02908e-16 |
|  952 | [240](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=240:240)    | CL:0001035 | bone cell | bone cell     | UBERON:0004324 | middle phalanx of pedal digit 2         | middle phalanx of digit of foot 2            |      1.02908e-16 |
|  953 | [241](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=241:241)    | CL:0001035 | bone cell | bone cell     | UBERON:0004325 | middle phalanx of pedal digit 3         | middle phalanx of digit of foot 3            |      1.02908e-16 |
|  954 | [217](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=217:217)    | CL:0001035 | bone cell | bone cell     | UBERON:0003650 | metatarsal bone of digit 1              | metatarsal bone of digit 1                   |      1.02908e-16 |
|  955 | [212](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=212:212)    | CL:0001035 | bone cell | bone cell     | UBERON:0004319 | distal phalanx of pedal digit 5         | distal phalanx of digit of foot 5            |      1.02908e-16 |
|  956 | [328](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=328:328)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
|  957 | [725](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=725:725)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  958 | [206](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=206:206)    | CL:0001035 | bone cell | bone cell     | UBERON:0004318 | distal phalanx of pedal digit 4         | distal phalanx of digit of foot 4            |      1.02908e-16 |
|  959 | [733](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=733:733)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  960 | [732](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=732:732)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  961 | [498](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=498:498)    | CL:0001035 | bone cell | bone cell     | UBERON:0001682 | palatine bone                           | palatine bone                                |      1.02908e-16 |
|  962 | [730](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=730:730)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  963 | [729](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=729:729)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  964 | [728](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=728:728)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  965 | [727](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=727:727)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  966 | [726](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=726:726)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  967 | [724](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=724:724)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  968 | [211](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=211:211)    | CL:0001035 | bone cell | bone cell     | UBERON:0004319 | distal phalanx of pedal digit 5         | distal phalanx of digit of foot 5            |      1.02908e-16 |
|  969 | [723](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=723:723)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  970 | [722](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=722:722)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  971 | [721](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=721:721)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  972 | [720](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=720:720)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  973 | [719](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=719:719)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |      1.02908e-16 |
|  974 | [207](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=207:207)    | CL:0001035 | bone cell | bone cell     | UBERON:0004318 | distal phalanx of pedal digit 4         | distal phalanx of digit of foot 4            |      1.02908e-16 |
|  975 | [208](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=208:208)    | CL:0001035 | bone cell | bone cell     | UBERON:0004318 | distal phalanx of pedal digit 4         | distal phalanx of digit of foot 4            |      1.02908e-16 |
|  976 | [209](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=209:209)    | CL:0001035 | bone cell | bone cell     | UBERON:0004319 | distal phalanx of pedal digit 5         | distal phalanx of digit of foot 5            |      1.02908e-16 |
|  977 | [210](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=210:210)    | CL:0001035 | bone cell | bone cell     | UBERON:0004319 | distal phalanx of pedal digit 5         | distal phalanx of digit of foot 5            |      1.02908e-16 |
|  978 | [242](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=242:242)    | CL:0001035 | bone cell | bone cell     | UBERON:0004325 | middle phalanx of pedal digit 3         | middle phalanx of digit of foot 3            |      1.02908e-16 |
|  979 | [14](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=14:14)       | CL:0001035 | bone cell | bone cell     | UBERON:0003460 | arm bone                                | arm bone                                     |      1.02908e-16 |
|  980 | [274](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=274:274)    | CL:0001035 | bone cell | bone cell     | UBERON:0004336 | proximal phalanx of pedal digit 5       | proximal phalanx of digit of foot 5          |      1.02908e-16 |
|  981 | [279](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=279:279)    | CL:0001035 | bone cell | bone cell     | UBERON:0002395 | talus                                   | talus                                        |      1.02908e-16 |
|  982 | [270](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=270:270)    | CL:0001035 | bone cell | bone cell     | UBERON:0004335 | proximal phalanx of pedal digit 4       | proximal phalanx of digit of foot 4          |      1.02908e-16 |
|  983 | [271](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=271:271)    | CL:0001035 | bone cell | bone cell     | UBERON:0004336 | proximal phalanx of pedal digit 5       | proximal phalanx of digit of foot 5          |      1.02908e-16 |
|  984 | [272](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=272:272)    | CL:0001035 | bone cell | bone cell     | UBERON:0004336 | proximal phalanx of pedal digit 5       | proximal phalanx of digit of foot 5          |      1.02908e-16 |
|  985 | [273](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=273:273)    | CL:0001035 | bone cell | bone cell     | UBERON:0004336 | proximal phalanx of pedal digit 5       | proximal phalanx of digit of foot 5          |      1.02908e-16 |
|  986 | [319](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=319:319)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |      1.02908e-16 |
|  987 | [275](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=275:275)    | CL:0001035 | bone cell | bone cell     | UBERON:0002395 | talus                                   | talus                                        |      1.02908e-16 |
|  988 | [276](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=276:276)    | CL:0001035 | bone cell | bone cell     | UBERON:0002395 | talus                                   | talus                                        |      1.02908e-16 |
|  989 | [277](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=277:277)    | CL:0001035 | bone cell | bone cell     | UBERON:0002395 | talus                                   | talus                                        |      1.02908e-16 |
|  990 | [280](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=280:280)    | CL:0001035 | bone cell | bone cell     | UBERON:0002395 | talus                                   | talus                                        |      1.02908e-16 |
|  991 | [268](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=268:268)    | CL:0001035 | bone cell | bone cell     | UBERON:0004335 | proximal phalanx of pedal digit 4       | proximal phalanx of digit of foot 4          |      1.02908e-16 |
|  992 | [291](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=291:291)    | CL:0001035 | bone cell | bone cell     | UBERON:0009986 | lateral epicondyle of femur             | lateral epicondyle of femur                  |      1.02908e-16 |
|  993 | [309](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=309:309)    | CL:0001035 | bone cell | bone cell     | UBERON:0002446 | patella                                 | patella                                      |      1.02908e-16 |
|  994 | [310](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=310:310)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |      1.02908e-16 |
|  995 | [311](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=311:311)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |      1.02908e-16 |
|  996 | [312](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=312:312)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |      1.02908e-16 |
|  997 | [313](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=313:313)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |      1.02908e-16 |
|  998 | [314](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=314:314)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |      1.02908e-16 |
|  999 | [315](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=315:315)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |      1.02908e-16 |
| 1000 | [318](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=318:318)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |      1.02908e-16 |
| 1001 | [269](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=269:269)    | CL:0001035 | bone cell | bone cell     | UBERON:0004335 | proximal phalanx of pedal digit 4       | proximal phalanx of digit of foot 4          |      1.02908e-16 |
| 1002 | [267](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=267:267)    | CL:0001035 | bone cell | bone cell     | UBERON:0004335 | proximal phalanx of pedal digit 4       | proximal phalanx of digit of foot 4          |      1.02908e-16 |
| 1003 | [320](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=320:320)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |      1.02908e-16 |
| 1004 | [327](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=327:327)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
| 1005 | [326](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=326:326)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
| 1006 | [325](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=325:325)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
| 1007 | [324](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=324:324)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |      1.02908e-16 |
| 1008 | [322](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=322:322)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |      1.02908e-16 |
| 1009 | [321](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=321:321)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |      1.02908e-16 |
| 1010 | [652](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=652:652)    | CL:0001035 | bone cell | bone cell     | UBERON:0014477 | thoracic skeleton                       | thoracic skeleton                            |      1.02908e-16 |
| 1011 | [316](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=316:316)    | CL:0001035 | bone cell | bone cell     | UBERON:0009991 | lateral condyle of tibia                | lateral condyle of tibia                     |      1.02908e-16 |
| 1012 | [243](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=243:243)    | CL:0001035 | bone cell | bone cell     | UBERON:0004325 | middle phalanx of pedal digit 3         | middle phalanx of digit of foot 3            |      1.02908e-16 |
| 1013 | [244](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=244:244)    | CL:0001035 | bone cell | bone cell     | UBERON:0004325 | middle phalanx of pedal digit 3         | middle phalanx of digit of foot 3            |      1.02908e-16 |
| 1014 | [259](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=259:259)    | CL:0001035 | bone cell | bone cell     | UBERON:0004333 | proximal phalanx of pedal digit 2       | proximal phalanx of digit of foot 2          |      1.02908e-16 |
| 1015 | [260](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=260:260)    | CL:0001035 | bone cell | bone cell     | UBERON:0004333 | proximal phalanx of pedal digit 2       | proximal phalanx of digit of foot 2          |      1.02908e-16 |
| 1016 | [261](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=261:261)    | CL:0001035 | bone cell | bone cell     | UBERON:0004333 | proximal phalanx of pedal digit 2       | proximal phalanx of digit of foot 2          |      1.02908e-16 |
| 1017 | [262](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=262:262)    | CL:0001035 | bone cell | bone cell     | UBERON:0004333 | proximal phalanx of pedal digit 2       | proximal phalanx of digit of foot 2          |      1.02908e-16 |
| 1018 | [657](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=657:657)    | CL:0001035 | bone cell | bone cell     | UBERON:0002205 | manubrium of sternum                    | manubrium of sternum                         |      1.02908e-16 |
| 1019 | [667](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=667:667)    | CL:0001035 | bone cell | bone cell     | UBERON:0002413 | cervical vertebra                       | cervical vertebra                            |      1.02908e-16 |
| 1020 | [452](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=452:452)    | CL:0001035 | bone cell | bone cell     | UBERON:0001689 | malleus bone                            | malleus bone                                 |      1.02903e-16 |
| 1021 | [450](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=450:450)    | CL:0001035 | bone cell | bone cell     | UBERON:0010911 | ossicle                                 | ossicle                                      |      1.02864e-16 |
| 1022 | [304](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=304:304)    | CL:0001035 | bone cell | bone cell     | UBERON:0001446 | fibula                                  | fibula                                       |      1.02786e-16 |
| 1023 | [305](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=305:305)    | CL:0001035 | bone cell | bone cell     | UBERON:0001446 | fibula                                  | fibula                                       |      1.02786e-16 |
| 1024 | [308](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=308:308)    | CL:0001035 | bone cell | bone cell     | UBERON:0001446 | fibula                                  | fibula                                       |      1.02786e-16 |
| 1025 | [392](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=392:392)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |      6.38248e-17 |
| 1026 | [393](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=393:393)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |      6.38248e-17 |
| 1027 | [389](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=389:389)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |      6.38248e-17 |
| 1028 | [390](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=390:390)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |      6.38248e-17 |
| 1029 | [398](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=398:398)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |      6.38248e-17 |
| 1030 | [397](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=397:397)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |      6.38248e-17 |
| 1031 | [396](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=396:396)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |      6.38248e-17 |
| 1032 | [391](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=391:391)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |      6.38248e-17 |
| 1033 | [394](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=394:394)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |      6.38248e-17 |
| 1034 | [395](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=395:395)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |      6.38248e-17 |
| 1035 | [16](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=16:16)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1036 | [17](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=17:17)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1037 | [19](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=19:19)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1038 | [20](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=20:20)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1039 | [21](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=21:21)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1040 | [22](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=22:22)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1041 | [23](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=23:23)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1042 | [24](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=24:24)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1043 | [25](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=25:25)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1044 | [27](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=27:27)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1045 | [28](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=28:28)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1046 | [29](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=29:29)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1047 | [30](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=30:30)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1048 | [31](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=31:31)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1049 | [32](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=32:32)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1050 | [33](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=33:33)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |    nan           |
| 1051 | [35](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=35:35)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |    nan           |
| 1052 | [36](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=36:36)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |    nan           |
| 1053 | [37](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=37:37)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |    nan           |
| 1054 | [38](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=38:38)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |    nan           |
| 1055 | [39](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=39:39)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |    nan           |
| 1056 | [40](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=40:40)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |    nan           |
| 1057 | [41](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=41:41)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |    nan           |
| 1058 | [42](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=42:42)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |    nan           |
| 1059 | [44](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=44:44)       | CL:0001035 | bone cell | bone cell     | UBERON:0010994 | coronoid process of ulna                | coronoid process of ulna                     |    nan           |
| 1063 | [57](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=57:57)       | CL:0001035 | bone cell | bone cell     | UBERON:0001431 | distal carpal bone 2                    | distal carpal bone 2                         |    nan           |
| 1065 | [58](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=58:58)       | CL:0001035 | bone cell | bone cell     | UBERON:0001432 | distal carpal bone 3                    | distal carpal bone 3                         |    nan           |
| 1067 | [59](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=59:59)       | CL:0001035 | bone cell | bone cell     | UBERON:0001433 | distal carpal bone 4                    | distal carpal bone 4                         |    nan           |
| 1069 | [60](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=60:60)       | CL:0001035 | bone cell | bone cell     | UBERON:0001433 | distal carpal bone 4                    | distal carpal bone 4                         |    nan           |
| 1086 | [76](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=76:76)       | CL:0001035 | bone cell | bone cell     | UBERON:0004313 | distal phalanx of manual digit 4        | distal phalanx of digit of hand 4            |    nan           |
| 1088 | [77](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=77:77)       | CL:0001035 | bone cell | bone cell     | UBERON:0004313 | distal phalanx of manual digit 4        | distal phalanx of digit of hand 4            |    nan           |
| 1090 | [78](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=78:78)       | CL:0001035 | bone cell | bone cell     | UBERON:0004313 | distal phalanx of manual digit 4        | distal phalanx of digit of hand 4            |    nan           |
| 1092 | [79](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=79:79)       | CL:0001035 | bone cell | bone cell     | UBERON:0004313 | distal phalanx of manual digit 4        | distal phalanx of digit of hand 4            |    nan           |
| 1094 | [80](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=80:80)       | CL:0001035 | bone cell | bone cell     | UBERON:0004313 | distal phalanx of manual digit 4        | distal phalanx of digit of hand 4            |    nan           |
| 1096 | [81](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=81:81)       | CL:0001035 | bone cell | bone cell     | UBERON:0004314 | distal phalanx of manual digit 5        | distal phalanx of digit of hand 5            |    nan           |
| 1098 | [82](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=82:82)       | CL:0001035 | bone cell | bone cell     | UBERON:0004314 | distal phalanx of manual digit 5        | distal phalanx of digit of hand 5            |    nan           |
| 1100 | [83](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=83:83)       | CL:0001035 | bone cell | bone cell     | UBERON:0004314 | distal phalanx of manual digit 5        | distal phalanx of digit of hand 5            |    nan           |
| 1102 | [84](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=84:84)       | CL:0001035 | bone cell | bone cell     | UBERON:0004314 | distal phalanx of manual digit 5        | distal phalanx of digit of hand 5            |    nan           |
| 1104 | [85](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=85:85)       | CL:0001035 | bone cell | bone cell     | UBERON:0004314 | distal phalanx of manual digit 5        | distal phalanx of digit of hand 5            |    nan           |
| 1107 | [87](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=87:87)       | CL:0001035 | bone cell | bone cell     | UBERON:0003645 | metacarpal bone of digit 1              | metacarpal bone of digit 1                   |    nan           |
| 1109 | [88](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=88:88)       | CL:0001035 | bone cell | bone cell     | UBERON:0003645 | metacarpal bone of digit 1              | metacarpal bone of digit 1                   |    nan           |
| 1111 | [89](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=89:89)       | CL:0001035 | bone cell | bone cell     | UBERON:0003645 | metacarpal bone of digit 1              | metacarpal bone of digit 1                   |    nan           |
| 1113 | [90](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=90:90)       | CL:0001035 | bone cell | bone cell     | UBERON:0003645 | metacarpal bone of digit 1              | metacarpal bone of digit 1                   |    nan           |
| 1119 | [95](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=95:95)       | CL:0001035 | bone cell | bone cell     | UBERON:0003647 | metacarpal bone of digit 3              | metacarpal bone of digit 3                   |    nan           |
| 1121 | [96](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=96:96)       | CL:0001035 | bone cell | bone cell     | UBERON:0003647 | metacarpal bone of digit 3              | metacarpal bone of digit 3                   |    nan           |
| 1123 | [97](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=97:97)       | CL:0001035 | bone cell | bone cell     | UBERON:0003647 | metacarpal bone of digit 3              | metacarpal bone of digit 3                   |    nan           |
| 1125 | [98](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=98:98)       | CL:0001035 | bone cell | bone cell     | UBERON:0003647 | metacarpal bone of digit 3              | metacarpal bone of digit 3                   |    nan           |
| 1131 | [103](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=103:103)    | CL:0001035 | bone cell | bone cell     | UBERON:0003649 | metacarpal bone of digit 5              | metacarpal bone of digit 5                   |    nan           |
| 1133 | [104](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=104:104)    | CL:0001035 | bone cell | bone cell     | UBERON:0003649 | metacarpal bone of digit 5              | metacarpal bone of digit 5                   |    nan           |
| 1135 | [105](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=105:105)    | CL:0001035 | bone cell | bone cell     | UBERON:0003649 | metacarpal bone of digit 5              | metacarpal bone of digit 5                   |    nan           |
| 1137 | [106](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=106:106)    | CL:0001035 | bone cell | bone cell     | UBERON:0003649 | metacarpal bone of digit 5              | metacarpal bone of digit 5                   |    nan           |
| 1139 | [107](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=107:107)    | CL:0001035 | bone cell | bone cell     | UBERON:0004320 | middle phalanx of manual digit 2        | middle phalanx of digit of hand 2            |    nan           |
| 1141 | [108](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=108:108)    | CL:0001035 | bone cell | bone cell     | UBERON:0004320 | middle phalanx of manual digit 2        | middle phalanx of digit of hand 2            |    nan           |
| 1143 | [109](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=109:109)    | CL:0001035 | bone cell | bone cell     | UBERON:0004320 | middle phalanx of manual digit 2        | middle phalanx of digit of hand 2            |    nan           |
| 1145 | [110](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=110:110)    | CL:0001035 | bone cell | bone cell     | UBERON:0004320 | middle phalanx of manual digit 2        | middle phalanx of digit of hand 2            |    nan           |
| 1159 | [123](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=123:123)    | CL:0001035 | bone cell | bone cell     | UBERON:0001429 | pisiform                                | pisiform                                     |    nan           |
| 1161 | [124](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=124:124)    | CL:0001035 | bone cell | bone cell     | UBERON:0004338 | proximal phalanx of manual digit 1      | proximal phalanx of digit of hand 1          |    nan           |
| 1163 | [125](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=125:125)    | CL:0001035 | bone cell | bone cell     | UBERON:0004338 | proximal phalanx of manual digit 1      | proximal phalanx of digit of hand 1          |    nan           |
| 1165 | [126](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=126:126)    | CL:0001035 | bone cell | bone cell     | UBERON:0004338 | proximal phalanx of manual digit 1      | proximal phalanx of digit of hand 1          |    nan           |
| 1167 | [127](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=127:127)    | CL:0001035 | bone cell | bone cell     | UBERON:0004338 | proximal phalanx of manual digit 1      | proximal phalanx of digit of hand 1          |    nan           |
| 1169 | [128](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=128:128)    | CL:0001035 | bone cell | bone cell     | UBERON:0004328 | proximal phalanx of manual digit 2      | proximal phalanx of digit of hand 2          |    nan           |
| 1171 | [129](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=129:129)    | CL:0001035 | bone cell | bone cell     | UBERON:0004328 | proximal phalanx of manual digit 2      | proximal phalanx of digit of hand 2          |    nan           |
| 1173 | [130](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=130:130)    | CL:0001035 | bone cell | bone cell     | UBERON:0004328 | proximal phalanx of manual digit 2      | proximal phalanx of digit of hand 2          |    nan           |
| 1175 | [131](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=131:131)    | CL:0001035 | bone cell | bone cell     | UBERON:0004328 | proximal phalanx of manual digit 2      | proximal phalanx of digit of hand 2          |    nan           |
| 1185 | [140](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=140:140)    | CL:0001035 | bone cell | bone cell     | UBERON:0004331 | proximal phalanx of manual digit 5      | proximal phalanx of digit of hand 5          |    nan           |
| 1187 | [141](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=141:141)    | CL:0001035 | bone cell | bone cell     | UBERON:0004331 | proximal phalanx of manual digit 5      | proximal phalanx of digit of hand 5          |    nan           |
| 1189 | [142](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=142:142)    | CL:0001035 | bone cell | bone cell     | UBERON:0004331 | proximal phalanx of manual digit 5      | proximal phalanx of digit of hand 5          |    nan           |
| 1191 | [143](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=143:143)    | CL:0001035 | bone cell | bone cell     | UBERON:0004331 | proximal phalanx of manual digit 5      | proximal phalanx of digit of hand 5          |    nan           |
| 1193 | [144](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=144:144)    | CL:0001035 | bone cell | bone cell     | UBERON:0001427 | radiale                                 | scaphoid                                     |    nan           |
| 1195 | [145](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=145:145)    | CL:0001035 | bone cell | bone cell     | UBERON:0001427 | radiale                                 | scaphoid                                     |    nan           |
| 1197 | [146](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=146:146)    | CL:0001035 | bone cell | bone cell     | UBERON:0002445 | ulnare                                  | ulnare                                       |    nan           |
| 1198 | [147](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=147:147)    | CL:0001035 | bone cell | bone cell     | UBERON:0007829 | pectoral girdle bone                    | pectoral girdle bone                         |    nan           |
| 1199 | [157](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=157:157)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1200 | [158](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=158:158)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1201 | [159](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=159:159)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1202 | [160](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=160:160)    | CL:0001035 | bone cell | bone cell     | UBERON:0006633 | coracoid process of scapula             | coracoid process of scapula                  |    nan           |
| 1203 | [161](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=161:161)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1204 | [162](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=162:162)    | CL:0001035 | bone cell | bone cell     | UBERON:0007175 | inferior angle of scapula               | inferior angle of scapula                    |    nan           |
| 1205 | [163](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=163:163)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1206 | [164](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=164:164)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1207 | [165](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=165:165)    | CL:0001035 | bone cell | bone cell     | UBERON:0007173 | lateral border of scapula               | lateral border of scapula                    |    nan           |
| 1208 | [166](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=166:166)    | CL:0001035 | bone cell | bone cell     | UBERON:0007174 | medial border of scapula                | medial border of scapula                     |    nan           |
| 1209 | [167](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=167:167)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1210 | [168](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=168:168)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1211 | [169](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=169:169)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1212 | [170](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=170:170)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1213 | [172](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=172:172)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1214 | [173](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=173:173)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1215 | [174](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=174:174)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |    nan           |
| 1216 | [176](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=176:176)    | CL:0001035 | bone cell | bone cell     | UBERON:0005899 | pes bone                                | foot bone                                    |    nan           |
| 1217 | [190](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=190:190)    | CL:0001035 | bone cell | bone cell     | UBERON:0001455 | cuboid bone                             | cuboid bone                                  |    nan           |
| 1218 | [191](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=191:191)    | CL:0001035 | bone cell | bone cell     | UBERON:0001455 | cuboid bone                             | cuboid bone                                  |    nan           |
| 1219 | [192](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=192:192)    | CL:0001035 | bone cell | bone cell     | UBERON:0001455 | cuboid bone                             | cuboid bone                                  |    nan           |
| 1220 | [193](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=193:193)    | CL:0001035 | bone cell | bone cell     | UBERON:0004315 | distal phalanx of pedal digit 1         | distal phalanx of digit of foot 1            |    nan           |
| 1221 | [194](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=194:194)    | CL:0001035 | bone cell | bone cell     | UBERON:0004315 | distal phalanx of pedal digit 1         | distal phalanx of digit of foot 1            |    nan           |
| 1222 | [195](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=195:195)    | CL:0001035 | bone cell | bone cell     | UBERON:0004315 | distal phalanx of pedal digit 1         | distal phalanx of digit of foot 1            |    nan           |
| 1223 | [196](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=196:196)    | CL:0001035 | bone cell | bone cell     | UBERON:0004315 | distal phalanx of pedal digit 1         | distal phalanx of digit of foot 1            |    nan           |
| 1224 | [201](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=201:201)    | CL:0001035 | bone cell | bone cell     | UBERON:0004317 | distal phalanx of pedal digit 3         | distal phalanx of digit of foot 3            |    nan           |
| 1225 | [202](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=202:202)    | CL:0001035 | bone cell | bone cell     | UBERON:0004317 | distal phalanx of pedal digit 3         | distal phalanx of digit of foot 3            |    nan           |
| 1226 | [203](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=203:203)    | CL:0001035 | bone cell | bone cell     | UBERON:0004317 | distal phalanx of pedal digit 3         | distal phalanx of digit of foot 3            |    nan           |
| 1227 | [204](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=204:204)    | CL:0001035 | bone cell | bone cell     | UBERON:0004317 | distal phalanx of pedal digit 3         | distal phalanx of digit of foot 3            |    nan           |
| 1228 | [213](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=213:213)    | CL:0001035 | bone cell | bone cell     | UBERON:0001452 | distal tarsal bone 1                    | distal tarsal bone 1                         |    nan           |
| 1229 | [214](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=214:214)    | CL:0001035 | bone cell | bone cell     | UBERON:0001453 | distal tarsal bone 2                    | distal tarsal bone 2                         |    nan           |
| 1230 | [215](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=215:215)    | CL:0001035 | bone cell | bone cell     | UBERON:0001454 | distal tarsal bone 3                    | distal tarsal bone 3                         |    nan           |
| 1231 | [224](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=224:224)    | CL:0001035 | bone cell | bone cell     | UBERON:0003652 | metatarsal bone of digit 3              | metatarsal bone of digit 3                   |    nan           |
| 1232 | [225](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=225:225)    | CL:0001035 | bone cell | bone cell     | UBERON:0003652 | metatarsal bone of digit 3              | metatarsal bone of digit 3                   |    nan           |
| 1233 | [226](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=226:226)    | CL:0001035 | bone cell | bone cell     | UBERON:0003652 | metatarsal bone of digit 3              | metatarsal bone of digit 3                   |    nan           |
| 1234 | [227](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=227:227)    | CL:0001035 | bone cell | bone cell     | UBERON:0003652 | metatarsal bone of digit 3              | metatarsal bone of digit 3                   |    nan           |
| 1235 | [255](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=255:255)    | CL:0001035 | bone cell | bone cell     | UBERON:0004332 | proximal phalanx of pedal digit 1       | proximal phalanx of digit of foot 1          |    nan           |
| 1236 | [256](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=256:256)    | CL:0001035 | bone cell | bone cell     | UBERON:0004332 | proximal phalanx of pedal digit 1       | proximal phalanx of digit of foot 1          |    nan           |
| 1237 | [257](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=257:257)    | CL:0001035 | bone cell | bone cell     | UBERON:0004332 | proximal phalanx of pedal digit 1       | proximal phalanx of digit of foot 1          |    nan           |
| 1238 | [258](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=258:258)    | CL:0001035 | bone cell | bone cell     | UBERON:0004332 | proximal phalanx of pedal digit 1       | proximal phalanx of digit of foot 1          |    nan           |
| 1239 | [278](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=278:278)    | CL:0001035 | bone cell | bone cell     | UBERON:0015180 | neck of talus                           | neck of talus                                |    nan           |
| 1240 | [290](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=290:290)    | CL:0001035 | bone cell | bone cell     | UBERON:0009985 | lateral condyle of femur                | lateral condyle of femur                     |    nan           |
| 1241 | [295](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=295:295)    | CL:0001035 | bone cell | bone cell     | UBERON:0009984 | medial condyle of femur                 | medial condyle of femur                      |    nan           |
| 1242 | [298](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=298:298)    | CL:0001035 | bone cell | bone cell     | UBERON:0007119 | neck of femur                           | neck of femur                                |    nan           |
| 1243 | [360](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=360:360)    | CL:0001035 | bone cell | bone cell     | UBERON:0004766 | cranial bone                            | cranial bone                                 |    nan           |
| 1244 | [361](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=361:361)    | CL:0001035 | bone cell | bone cell     | UBERON:0004766 | cranial bone                            | cranial bone                                 |    nan           |
| 1268 | [388](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=388:388)    | CL:0001035 | bone cell | bone cell     | UBERON:0012109 | zygomatic process of frontal bone       | zygomatic process of frontal bone            |    nan           |
| 1280 | [399](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=399:399)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |    nan           |
| 1282 | [400](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=400:400)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |    nan           |
| 1284 | [401](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=401:401)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |    nan           |
| 1286 | [402](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=402:402)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |    nan           |
| 1288 | [403](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=403:403)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |    nan           |
| 1290 | [404](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=404:404)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |    nan           |
| 1292 | [405](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=405:405)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |    nan           |
| 1367 | [454](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=454:454)    | CL:0001035 | bone cell | bone cell     | UBERON:0008895 | splanchnocranium                        | splanchnocranium                             |    nan           |
| 1369 | [455](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=455:455)    | CL:0001035 | bone cell | bone cell     | UBERON:0005922 | inferior nasal concha                   | inferior nasal concha                        |    nan           |
| 1419 | [480](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=480:480)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |    nan           |
| 1421 | [481](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=481:481)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |    nan           |
| 1424 | [483](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=483:483)    | CL:0001035 | bone cell | bone cell     | UBERON:0035139 | anterior nasal spine of maxilla         | anterior nasal spine of maxilla              |    nan           |
| 1426 | [484](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=484:484)    | CL:0001035 | bone cell | bone cell     | UBERON:0013767 | frontal process of maxilla              | frontal process of maxilla                   |    nan           |
| 1428 | [485](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=485:485)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |    nan           |
| 1430 | [486](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=486:486)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |    nan           |
| 1432 | [487](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=487:487)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |    nan           |
| 1434 | [488](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=488:488)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |    nan           |
| 1436 | [489](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=489:489)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |    nan           |
| 1438 | [490](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=490:490)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |    nan           |
| 1440 | [491](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=491:491)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |    nan           |
| 1442 | [492](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=492:492)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |    nan           |
| 1444 | [493](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=493:493)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |    nan           |
| 1468 | [543](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=543:543)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |    nan           |
| 1469 | [544](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=544:544)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |    nan           |
| 1470 | [545](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=545:545)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |    nan           |
| 1471 | [546](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=546:546)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |    nan           |
| 1472 | [547](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=547:547)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |    nan           |
| 1473 | [548](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=548:548)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |    nan           |
| 1474 | [549](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=549:549)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1475 | [550](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=550:550)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1476 | [551](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=551:551)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1477 | [552](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=552:552)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1478 | [553](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=553:553)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1479 | [554](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=554:554)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1480 | [555](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=555:555)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1481 | [556](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=556:556)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1482 | [557](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=557:557)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1483 | [558](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=558:558)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1484 | [559](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=559:559)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1485 | [560](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=560:560)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |    nan           |
| 1486 | [653](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=653:653)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |    nan           |
| 1487 | [654](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=654:654)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |    nan           |
| 1488 | [655](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=655:655)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |    nan           |
| 1489 | [656](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=656:656)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |    nan           |
| 1490 | [658](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=658:658)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |    nan           |
| 1491 | [659](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=659:659)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |    nan           |
| 1492 | [660](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=660:660)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |    nan           |
| 1493 | [661](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=661:661)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |    nan           |
| 1497 | [664](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=664:664)    | CL:0001035 | bone cell | bone cell     | UBERON:0001350 | coccyx                                  | coccyx                                       |    nan           |
| 1499 | [665](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=665:665)    | CL:0001035 | bone cell | bone cell     | UBERON:0001350 | coccyx                                  | coccyx                                       |    nan           |
| 1501 | [666](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=666:666)    | CL:0001035 | bone cell | bone cell     | UBERON:0001350 | coccyx                                  | coccyx                                       |    nan           |
| 1504 | [668](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=668:668)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1506 | [669](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=669:669)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1508 | [670](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=670:670)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1510 | [671](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=671:671)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1512 | [672](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=672:672)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1514 | [673](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=673:673)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1516 | [674](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=674:674)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1518 | [675](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=675:675)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1520 | [676](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=676:676)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1522 | [677](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=677:677)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1524 | [678](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=678:678)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1526 | [679](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=679:679)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1528 | [680](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=680:680)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1530 | [681](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=681:681)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1532 | [682](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=682:682)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1534 | [683](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=683:683)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1536 | [684](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=684:684)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1538 | [685](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=685:685)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1540 | [686](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=686:686)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |    nan           |
| 1542 | [687](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=687:687)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1544 | [688](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=688:688)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1546 | [689](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=689:689)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1548 | [690](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=690:690)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1550 | [691](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=691:691)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1552 | [692](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=692:692)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1555 | [694](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=694:694)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1557 | [695](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=695:695)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1559 | [696](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=696:696)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1561 | [697](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=697:697)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1563 | [698](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=698:698)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1565 | [699](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=699:699)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1567 | [700](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=700:700)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1569 | [701](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=701:701)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1571 | [702](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=702:702)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1573 | [703](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=703:703)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |    nan           |
| 1575 | [704](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=704:704)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1577 | [705](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=705:705)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1579 | [706](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=706:706)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1581 | [707](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=707:707)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1583 | [708](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=708:708)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1585 | [709](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=709:709)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1587 | [710](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=710:710)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1589 | [711](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=711:711)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1591 | [712](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=712:712)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1593 | [713](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=713:713)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1595 | [714](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=714:714)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1597 | [715](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=715:715)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1599 | [716](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=716:716)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1601 | [717](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=717:717)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1603 | [718](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=718:718)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |    nan           |
| 1620 | [734](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=734:734)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1622 | [735](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=735:735)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1624 | [736](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=736:736)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1626 | [737](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=737:737)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1628 | [738](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=738:738)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1630 | [739](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=739:739)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1632 | [740](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=740:740)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1634 | [741](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=741:741)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1636 | [742](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=742:742)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1638 | [743](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=743:743)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1640 | [744](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=744:744)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1642 | [745](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=745:745)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1644 | [746](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=746:746)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1646 | [747](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=747:747)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1648 | [748](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=748:748)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |    nan           |
| 1698 | [797](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=797:797)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1700 | [798](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=798:798)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1702 | [799](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=799:799)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1704 | [800](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=800:800)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1706 | [801](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=801:801)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1708 | [802](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=802:802)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1710 | [803](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=803:803)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1712 | [804](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=804:804)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1714 | [805](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=805:805)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1716 | [806](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=806:806)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1718 | [807](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=807:807)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1720 | [808](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=808:808)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1722 | [809](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=809:809)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1724 | [810](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=810:810)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1726 | [811](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=811:811)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1728 | [812](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=812:812)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |    nan           |
| 1730 | [813](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=813:813)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1732 | [814](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=814:814)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1734 | [815](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=815:815)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1736 | [816](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=816:816)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1738 | [817](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=817:817)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1740 | [818](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=818:818)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1742 | [819](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=819:819)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1744 | [820](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=820:820)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1746 | [821](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=821:821)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1748 | [822](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=822:822)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1750 | [823](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=823:823)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1752 | [824](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=824:824)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1754 | [825](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=825:825)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1756 | [826](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=826:826)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1758 | [827](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=827:827)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1760 | [828](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=828:828)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |    nan           |
| 1778 | [845](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=845:845)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1780 | [846](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=846:846)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1782 | [847](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=847:847)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1784 | [848](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=848:848)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1786 | [849](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=849:849)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1788 | [850](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=850:850)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1790 | [851](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=851:851)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1792 | [852](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=852:852)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1794 | [853](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=853:853)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1796 | [854](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=854:854)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1798 | [855](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=855:855)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1800 | [856](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=856:856)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1802 | [857](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=857:857)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1804 | [858](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=858:858)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1806 | [859](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=859:859)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1808 | [860](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=860:860)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |    nan           |
| 1850 | [882](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=882:882)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1852 | [883](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=883:883)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1854 | [884](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=884:884)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1856 | [885](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=885:885)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1858 | [886](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=886:886)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1860 | [887](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=887:887)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1862 | [888](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=888:888)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1864 | [889](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=889:889)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1866 | [890](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=890:890)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1868 | [891](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=891:891)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1870 | [892](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=892:892)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1872 | [893](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=893:893)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1874 | [894](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=894:894)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1876 | [895](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=895:895)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1878 | [896](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=896:896)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1880 | [897](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=897:897)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1882 | [898](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=898:898)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |    nan           |
| 1884 | [899](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=899:899)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1886 | [900](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=900:900)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1888 | [901](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=901:901)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1890 | [902](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=902:902)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1892 | [903](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=903:903)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1894 | [904](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=904:904)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1896 | [905](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=905:905)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1898 | [906](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=906:906)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1900 | [907](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=907:907)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1902 | [908](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=908:908)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1904 | [909](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=909:909)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1906 | [910](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=910:910)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1908 | [911](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=911:911)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1910 | [912](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=912:912)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1912 | [913](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=913:913)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1914 | [914](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=914:914)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 1916 | [915](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=915:915)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |    nan           |
| 2001 | [999](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=999:999)    | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2003 | [1000](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1000:1000) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2005 | [1001](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1001:1001) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2007 | [1002](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1002:1002) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2009 | [1003](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1003:1003) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2011 | [1004](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1004:1004) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2013 | [1005](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1005:1005) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2015 | [1006](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1006:1006) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2017 | [1007](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1007:1007) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2019 | [1008](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1008:1008) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2021 | [1009](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1009:1009) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2023 | [1010](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1010:1010) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2025 | [1011](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1011:1011) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2027 | [1012](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1012:1012) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2029 | [1013](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1013:1013) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2031 | [1014](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1014:1014) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2033 | [1015](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1015:1015) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |    nan           |
| 2052 | [1033](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1033:1033) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2054 | [1034](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1034:1034) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2056 | [1035](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1035:1035) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2058 | [1036](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1036:1036) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2060 | [1037](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1037:1037) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2062 | [1038](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1038:1038) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2064 | [1039](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1039:1039) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2066 | [1040](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1040:1040) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2068 | [1041](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1041:1041) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2070 | [1042](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1042:1042) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2072 | [1043](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1043:1043) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2074 | [1044](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1044:1044) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2076 | [1045](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1045:1045) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2078 | [1046](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1046:1046) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2080 | [1047](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1047:1047) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2082 | [1048](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1048:1048) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2084 | [1049](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1049:1049) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |    nan           |
| 2103 | [1067](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1067:1067) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2105 | [1068](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1068:1068) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2107 | [1069](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1069:1069) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2109 | [1070](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1070:1070) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2111 | [1071](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1071:1071) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2113 | [1072](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1072:1072) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2115 | [1073](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1073:1073) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2117 | [1074](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1074:1074) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2119 | [1075](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1075:1075) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2121 | [1076](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1076:1076) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2123 | [1077](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1077:1077) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2125 | [1078](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1078:1078) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2127 | [1079](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1079:1079) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2129 | [1080](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1080:1080) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2131 | [1081](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1081:1081) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2133 | [1082](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1082:1082) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |
| 2135 | [1083](https://docs.google.com/spreadsheets/d/1eJEvULtrtEZWWpZWW2Vu7l7ykgbenm_tv2ZnPlAxs5w/edit#gid=0&range=1083:1083) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |    nan           |




# New CL terms
[**Report**](new_cl_terms_Skeleton.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Skeleton.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Skeleton_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Skeleton_AS_has_part_CT_log.tsv)