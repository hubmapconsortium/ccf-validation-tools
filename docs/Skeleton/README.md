
ASCT+B Validation Reports for Skeleton (2023-04-24)
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
  
1. In row _[15](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=15:15)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[16](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=16:16)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=17:17)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[17](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=17:17)_, no term id was found for the name/label _anatomical neck of humerus_.

1. In row _[18](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=18:18)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=19:19)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[19](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=19:19)_, no term id was found for the name/label _coronoid fossa of humerus_.

1. In row _[20](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=20:20)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[20](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=20:20)_, no term id was found for the name/label _deltoid tuberosity of humerus_.

1. In row _[21](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=21:21)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[21](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=21:21)_, no term id was found for the name/label _greater tubercle of humerus_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=22:22)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[22](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=22:22)_, no term id was found for the name/label _head of humerus_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=23:23)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[23](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=23:23)_, no term id was found for the name/label _intertubercular sulcus of humerus_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=24:24)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[24](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=24:24)_, no term id was found for the name/label _lateral epicondyle of humerus_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=25:25)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[25](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=25:25)_, no term id was found for the name/label _lateral supracondylar ridge of humerus_.

1. In row _[26](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=26:26)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=27:27)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[27](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=27:27)_, no term id was found for the name/label _medial epicondyle of humerus_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=28:28)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[28](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=28:28)_, no term id was found for the name/label _medial supracondylar ridge of humerus_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=29:29)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[29](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=29:29)_, no term id was found for the name/label _olecranon fossa of humerus_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=30:30)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[30](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=30:30)_, no term id was found for the name/label _radial fossa of humerus_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=31:31)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[31](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=31:31)_, no term id was found for the name/label _radial groove of humerus_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=32:32)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[32](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=32:32)_, no term id was found for the name/label _shaft of humerus_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=33:33)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[33](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=33:33)_, no term id was found for the name/label _surgical neck of humerus_.

1. In row _[34](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=34:34)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[35](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=35:35)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=36:36)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[36](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=36:36)_, no term id was found for the name/label _head of radius of radius_.

1. In row _[37](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=37:37)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[37](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=37:37)_, no term id was found for the name/label _interosseous border of radius_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=38:38)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[38](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=38:38)_, no term id was found for the name/label _neck of radius of radius_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=39:39)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[39](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=39:39)_, no term id was found for the name/label _radial tuberosity of radius_.

1. In row _[40](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=40:40)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[40](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=40:40)_, no term id was found for the name/label _shaft of radius of radius_.

1. In row _[41](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=41:41)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[41](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=41:41)_, no term id was found for the name/label _styloid process of radius_.

1. In row _[42](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=42:42)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[42](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=42:42)_, no term id was found for the name/label _ulnar notch of radius_.

1. In row _[43](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=43:43)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[44](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=44:44)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[45](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=45:45)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[45](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=45:45)_, no term id was found for the name/label _head of ulna of ulna_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=46:46)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[46](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=46:46)_, no term id was found for the name/label _interosseous border of ulna_.

1. In row _[47](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=47:47)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[47](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=47:47)_, no term id was found for the name/label _olecranon of ulna_.

1. In row _[48](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=48:48)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[48](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=48:48)_, no term id was found for the name/label _radial notch of ulna_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=49:49)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[49](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=49:49)_, no term id was found for the name/label _shaft of ulna of ulna_.

1. In row _[50](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=50:50)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=51:51)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[51](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=51:51)_, no term id was found for the name/label _supinator crest of ulna_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=52:52)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[52](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=52:52)_, no term id was found for the name/label _supinator fossa of ulna_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=53:53)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[53](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=53:53)_, no term id was found for the name/label _trochlear notch of ulna_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=54:54)_, no term id was found for the name/label _free part of arm bone_.

1. In row _[54](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=54:54)_, no term id was found for the name/label _ulnar tuberosity of ulna_.

1. In row _[60](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=60:60)_, no term id was found for the name/label _hook of hamate_.

1. In row _[62](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=62:62)_, no term id was found for the name/label _base of first distal phalanx of hand_.

1. In row _[63](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=63:63)_, no term id was found for the name/label _head of first distal phalanx of hand_.

1. In row _[64](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=64:64)_, no term id was found for the name/label _shaft of first distal phalanx of hand_.

1. In row _[65](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=65:65)_, no term id was found for the name/label _tuberosity of first distal phalanx of hand_.

1. In row _[67](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=67:67)_, no term id was found for the name/label _base of second distal phalanx of hand_.

1. In row _[68](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=68:68)_, no term id was found for the name/label _head of second distal phalanx of hand_.

1. In row _[69](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=69:69)_, no term id was found for the name/label _shaft of second distal phalanx of hand_.

1. In row _[70](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=70:70)_, no term id was found for the name/label _tuberosity of second distal phalanx of hand_.

1. In row _[72](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=72:72)_, no term id was found for the name/label _base of third distal phalanx of hand_.

1. In row _[73](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=73:73)_, no term id was found for the name/label _head of third distal phalanx of hand_.

1. In row _[74](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=74:74)_, no term id was found for the name/label _shaft of third distal phalanx of hand_.

1. In row _[75](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=75:75)_, no term id was found for the name/label _tuberosity of third distal phalanx of hand_.

1. In row _[77](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=77:77)_, no term id was found for the name/label _base of fourth distal phalanx of hand_.

1. In row _[78](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=78:78)_, no term id was found for the name/label _head of fourth distal phalanx of hand_.

1. In row _[79](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=79:79)_, no term id was found for the name/label _shaft of fourth distal phalanx of hand_.

1. In row _[80](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=80:80)_, no term id was found for the name/label _tuberosity of fourth distal phalanx of hand_.

1. In row _[82](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=82:82)_, no term id was found for the name/label _base of fifth distal phalanx of hand_.

1. In row _[83](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=83:83)_, no term id was found for the name/label _head of fifth distal phalanx of hand_.

1. In row _[84](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=84:84)_, no term id was found for the name/label _shaft of fifth distal phalanx of hand_.

1. In row _[85](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=85:85)_, no term id was found for the name/label _tuberosity of fifth distal phalanx of hand_.

1. In row _[88](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=88:88)_, no term id was found for the name/label _base of first metacarpal bone_.

1. In row _[89](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=89:89)_, no term id was found for the name/label _head of first metacarpal bone_.

1. In row _[90](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=90:90)_, no term id was found for the name/label _shaft of first metacarpal bone_.

1. In row _[92](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=92:92)_, no term id was found for the name/label _base of second metacarpal bone_.

1. In row _[93](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=93:93)_, no term id was found for the name/label _head of second metacarpal bone_.

1. In row _[94](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=94:94)_, no term id was found for the name/label _shaft of second metacarpal bone_.

1. In row _[96](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=96:96)_, no term id was found for the name/label _base of third metacarpal bone_.

1. In row _[97](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=97:97)_, no term id was found for the name/label _head of third metacarpal bone_.

1. In row _[98](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=98:98)_, no term id was found for the name/label _shaft of third metacarpal bone_.

1. In row _[100](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=100:100)_, no term id was found for the name/label _base of fourth metacarpal bone_.

1. In row _[101](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=101:101)_, no term id was found for the name/label _head of fourth metacarpal bone_.

1. In row _[102](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=102:102)_, no term id was found for the name/label _shaft of fourth metacarpal bone_.

1. In row _[104](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=104:104)_, no term id was found for the name/label _base of fifth metacarpal bone_.

1. In row _[105](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=105:105)_, no term id was found for the name/label _head of fifth metacarpal bone_.

1. In row _[106](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=106:106)_, no term id was found for the name/label _shaft of fifth metacarpal bone_.

1. In row _[108](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=108:108)_, no term id was found for the name/label _base of second middle phalanx of hand_.

1. In row _[109](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=109:109)_, no term id was found for the name/label _head of second middle phalanx of hand_.

1. In row _[110](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=110:110)_, no term id was found for the name/label _shaft of second middle phalanx of hand_.

1. In row _[112](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=112:112)_, no term id was found for the name/label _base of third middle phalanx of hand_.

1. In row _[113](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=113:113)_, no term id was found for the name/label _head of third middle phalanx of han_.

1. In row _[114](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=114:114)_, no term id was found for the name/label _shaft of third middle phalanx of hand_.

1. In row _[116](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=116:116)_, no term id was found for the name/label _base of fourth middle phalanx of hand_.

1. In row _[117](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=117:117)_, no term id was found for the name/label _head of fourth middle phalanx of hand_.

1. In row _[118](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=118:118)_, no term id was found for the name/label _shaft of fourth middle phalanx of hand_.

1. In row _[120](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=120:120)_, no term id was found for the name/label _base of fifth middle phalanx of hand_.

1. In row _[121](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=121:121)_, no term id was found for the name/label _head of fifth middle phalanx of hand_.

1. In row _[122](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=122:122)_, no term id was found for the name/label _shaft of fifth middle phalanx of hand_.

1. In row _[125](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=125:125)_, no term id was found for the name/label _base of first proximal phalanx of hand_.

1. In row _[126](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=126:126)_, no term id was found for the name/label _head of first proximal phalanx of hand_.

1. In row _[127](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=127:127)_, no term id was found for the name/label _shaft of first proximal phalanx of hand_.

1. In row _[129](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=129:129)_, no term id was found for the name/label _base of second proximal phalanx of hand_.

1. In row _[130](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=130:130)_, no term id was found for the name/label _head of second proximal phalanx of hand_.

1. In row _[131](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=131:131)_, no term id was found for the name/label _shaft of second proximal phalanx of hand_.

1. In row _[133](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=133:133)_, no term id was found for the name/label _base of third proximal phalanx of hand_.

1. In row _[134](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=134:134)_, no term id was found for the name/label _head of third proximal phalanx of hand_.

1. In row _[135](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=135:135)_, no term id was found for the name/label _shaft of third proximal phalanx of hand_.

1. In row _[137](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=137:137)_, no term id was found for the name/label _base of fourth proximal phalanx of hand_.

1. In row _[138](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=138:138)_, no term id was found for the name/label _head of fourth proximal phalanx of hand_.

1. In row _[139](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=139:139)_, no term id was found for the name/label _shaft of fourth proximal phalanx of hand_.

1. In row _[141](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=141:141)_, no term id was found for the name/label _base of fifth proximal phalanx of hand_.

1. In row _[142](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=142:142)_, no term id was found for the name/label _head of fifth proximal phalanx of hand_.

1. In row _[143](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=143:143)_, no term id was found for the name/label _shaft of fifth proximal phalanx of hand_.

1. In row _[145](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=145:145)_, no term id was found for the name/label _scaphoid tubercle of scaphoid_.

1. In row _[149](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=149:149)_, no term id was found for the name/label _acromial end of clavicle_.

1. In row _[150](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=150:150)_, no term id was found for the name/label _acromial facet of clavicle_.

1. In row _[151](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=151:151)_, no term id was found for the name/label _conoid tubercle of clavicle_.

1. In row _[152](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=152:152)_, no term id was found for the name/label _shaft of clavicle_.

1. In row _[154](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=154:154)_, no term id was found for the name/label _sternal facet of clavicle_.

1. In row _[155](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=155:155)_, no term id was found for the name/label _subclavian groove of clavicle_.

1. In row _[156](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=156:156)_, no term id was found for the name/label _trapezoid line of clavicle_.

1. In row _[158](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=158:158)_, no term id was found for the name/label _acromial process of scapula_.

1. In row _[159](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=159:159)_, no term id was found for the name/label _clavicular facet of scapula_.

1. In row _[161](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=161:161)_, no term id was found for the name/label _glenoid fossa of scapula_.

1. In row _[163](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=163:163)_, no term id was found for the name/label _infraglenoid tubercle of scapula_.

1. In row _[164](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=164:164)_, no term id was found for the name/label _infraspinous fossa of scapula_.

1. In row _[167](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=167:167)_, no term id was found for the name/label _scapular neck of scapula_.

1. In row _[168](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=168:168)_, no term id was found for the name/label _scapular notch of scapula_.

1. In row _[169](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=169:169)_, no term id was found for the name/label _scapular spine of scapula_.

1. In row _[170](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=170:170)_, no term id was found for the name/label _subscapular fossa of scapula_.

1. In row _[172](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=172:172)_, no term id was found for the name/label _superior border of scapula_.

1. In row _[173](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=173:173)_, no term id was found for the name/label _supraglenoid tubercle of scapula_.

1. In row _[174](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=174:174)_, no term id was found for the name/label _supraspinous fossa of scapula_.

1. In row _[178](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=178:178)_, no term id was found for the name/label _anterior talar articular surface of calcaneus_.

1. In row _[179](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=179:179)_, no term id was found for the name/label _articular surface for cuboid bone of calcaneus_.

1. In row _[180](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=180:180)_, no term id was found for the name/label _body of calcaneus_.

1. In row _[181](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=181:181)_, no term id was found for the name/label _calcaneal sulcus of calcaneus_.

1. In row _[182](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=182:182)_, no term id was found for the name/label _calcaneal tuberosity of calcaneus_.

1. In row _[183](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=183:183)_, no term id was found for the name/label _fibular trochlea of calcaneus_.

1. In row _[184](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=184:184)_, no term id was found for the name/label _groove for tendon of flexor hallucis longus muscle of calcaneus_.

1. In row _[185](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=185:185)_, no term id was found for the name/label _lateral process of tuberosity of calcaneus_.

1. In row _[186](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=186:186)_, no term id was found for the name/label _medial process of tuberosity of calcaneus_.

1. In row _[187](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=187:187)_, no term id was found for the name/label _middle talar articular surface of calcaneus_.

1. In row _[188](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=188:188)_, no term id was found for the name/label _posterior talar articular surface of calcaneus_.

1. In row _[189](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=189:189)_, no term id was found for the name/label _sustentaculum tali of calcaneus_.

1. In row _[191](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=191:191)_, no term id was found for the name/label _groove for fibularis longus tendon of cuboid_.

1. In row _[192](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=192:192)_, no term id was found for the name/label _tuberosity of cuboid_.

1. In row _[194](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=194:194)_, no term id was found for the name/label _base of first distal phalanx of foot_.

1. In row _[195](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=195:195)_, no term id was found for the name/label _head of first distal phalanx of foot_.

1. In row _[196](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=196:196)_, no term id was found for the name/label _shaft of first distal phalanx of foot_.

1. In row _[198](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=198:198)_, no term id was found for the name/label _base of second distal phalanx of foot_.

1. In row _[199](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=199:199)_, no term id was found for the name/label _head of second distal phalanx of foot_.

1. In row _[200](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=200:200)_, no term id was found for the name/label _shaft of second distal phalanx of foot_.

1. In row _[202](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=202:202)_, no term id was found for the name/label _base of third distal phalanx of foot_.

1. In row _[203](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=203:203)_, no term id was found for the name/label _head of third distal phalanx of foot_.

1. In row _[204](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=204:204)_, no term id was found for the name/label _shaft of third distal phalanx of foot_.

1. In row _[206](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=206:206)_, no term id was found for the name/label _base of fourth distal phalanx of foot_.

1. In row _[207](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=207:207)_, no term id was found for the name/label _head of fourth distal phalanx of foot_.

1. In row _[208](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=208:208)_, no term id was found for the name/label _shaft of fourth distal phalanx of foot_.

1. In row _[210](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=210:210)_, no term id was found for the name/label _base of fifth distal phalanx of foot_.

1. In row _[211](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=211:211)_, no term id was found for the name/label _head of fifth distal phalanx of foot_.

1. In row _[212](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=212:212)_, no term id was found for the name/label _shaft of fifth distal phalanx of foot_.

1. In row _[217](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=217:217)_, no term id was found for the name/label _base of first metatarsal bone_.

1. In row _[218](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=218:218)_, no term id was found for the name/label _head of first metatarsal bone_.

1. In row _[219](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=219:219)_, no term id was found for the name/label _shaft of first metatarsal bone_.

1. In row _[221](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=221:221)_, no term id was found for the name/label _base of second metatarsal bone_.

1. In row _[222](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=222:222)_, no term id was found for the name/label _head of second metatarsal bone_.

1. In row _[223](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=223:223)_, no term id was found for the name/label _shaft of second metatarsal bone_.

1. In row _[225](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=225:225)_, no term id was found for the name/label _base of third metatarsal bone_.

1. In row _[226](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=226:226)_, no term id was found for the name/label _head of third metatarsal bone_.

1. In row _[227](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=227:227)_, no term id was found for the name/label _shaft of third metatarsal bone_.

1. In row _[229](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=229:229)_, no term id was found for the name/label _base of fourth metatarsal bone_.

1. In row _[230](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=230:230)_, no term id was found for the name/label _head of fourth metatarsal bone_.

1. In row _[231](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=231:231)_, no term id was found for the name/label _shaft of fourth metatarsal bone_.

1. In row _[233](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=233:233)_, no term id was found for the name/label _base of fifth metatarsal bone_.

1. In row _[234](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=234:234)_, no term id was found for the name/label _head of fifth metatarsal bone_.

1. In row _[235](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=235:235)_, no term id was found for the name/label _shaft of fifth metatarsal bone_.

1. In row _[236](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=236:236)_, no term id was found for the name/label _tuberosity of fifth metatarsal bone_.

1. In row _[238](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=238:238)_, no term id was found for the name/label _base of second middle phalanx of foot_.

1. In row _[239](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=239:239)_, no term id was found for the name/label _head of second middle phalanx of foot_.

1. In row _[240](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=240:240)_, no term id was found for the name/label _shaft of second middle phalanx of foot_.

1. In row _[242](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=242:242)_, no term id was found for the name/label _base of third middle phalanx of foot_.

1. In row _[243](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=243:243)_, no term id was found for the name/label _head of third middle phalanx of foot_.

1. In row _[244](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=244:244)_, no term id was found for the name/label _shaft of third middle phalanx of foot_.

1. In row _[246](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=246:246)_, no term id was found for the name/label _base of fourth middle phalanx of foot_.

1. In row _[247](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=247:247)_, no term id was found for the name/label _head of fourth middle phalanx of foot_.

1. In row _[248](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=248:248)_, no term id was found for the name/label _shaft of fourth middle phalanx of foot_.

1. In row _[250](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=250:250)_, no term id was found for the name/label _base of fifth middle phalanx of foot_.

1. In row _[251](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=251:251)_, no term id was found for the name/label _head of fifth middle phalanx of foot_.

1. In row _[252](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=252:252)_, no term id was found for the name/label _shaft of fifth middle phalanx of foot_.

1. In row _[254](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=254:254)_, no term id was found for the name/label _tuberosity of navicular_.

1. In row _[256](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=256:256)_, no term id was found for the name/label _base of first proximal phalanx of foot_.

1. In row _[257](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=257:257)_, no term id was found for the name/label _head of first proximal phalanx of foot_.

1. In row _[258](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=258:258)_, no term id was found for the name/label _shaft of first proximal phalanx of foot_.

1. In row _[260](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=260:260)_, no term id was found for the name/label _base of second proximal phalanx of foot_.

1. In row _[261](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=261:261)_, no term id was found for the name/label _head of second proximal phalanx of foot_.

1. In row _[262](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=262:262)_, no term id was found for the name/label _shaft of second proximal phalanx of foot_.

1. In row _[264](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=264:264)_, no term id was found for the name/label _base of third proximal phalanx of foot_.

1. In row _[265](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=265:265)_, no term id was found for the name/label _head of third proximal phalanx of foot_.

1. In row _[266](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=266:266)_, no term id was found for the name/label _shaft of third proximal phalanx of foot_.

1. In row _[268](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=268:268)_, no term id was found for the name/label _base of fourth proximal phalanx of foot_.

1. In row _[269](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=269:269)_, no term id was found for the name/label _head of fourth proximal phalanx of foot_.

1. In row _[270](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=270:270)_, no term id was found for the name/label _shaft of fourth proximal phalanx of foot_.

1. In row _[272](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=272:272)_, no term id was found for the name/label _base of fifth proximal phalanx of foot_.

1. In row _[273](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=273:273)_, no term id was found for the name/label _head of fifth proximal phalanx of foot_.

1. In row _[274](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=274:274)_, no term id was found for the name/label _shaft of fifth proximal phalanx of foot_.

1. In row _[276](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=276:276)_, no term id was found for the name/label _head of talus_.

1. In row _[277](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=277:277)_, no term id was found for the name/label _lateral process of talus_.

1. In row _[279](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=279:279)_, no term id was found for the name/label _posterior process of talus_.

1. In row _[280](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=280:280)_, no term id was found for the name/label _trochlea of talus_.

1. In row _[281](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=281:281)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[282](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=282:282)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[283](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=283:283)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[283](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=283:283)_, no term id was found for the name/label _adductor tubercle of femur_.

1. In row _[284](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=284:284)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[284](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=284:284)_, no term id was found for the name/label _gluteal tuberosity of femur_.

1. In row _[285](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=285:285)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[285](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=285:285)_, no term id was found for the name/label _greater trochanter of femur_.

1. In row _[286](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=286:286)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[287](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=287:287)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[287](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=287:287)_, no term id was found for the name/label _intercondylar fossa of femur_.

1. In row _[288](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=288:288)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[288](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=288:288)_, no term id was found for the name/label _intercondylar notch of femur_.

1. In row _[289](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=289:289)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[289](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=289:289)_, no term id was found for the name/label _intertrochanteric crest of femur_.

1. In row _[290](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=290:290)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[291](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=291:291)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[292](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=292:292)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[292](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=292:292)_, no term id was found for the name/label _lateral lip of linea aspera of femur_.

1. In row _[293](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=293:293)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[293](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=293:293)_, no term id was found for the name/label _lesser trochanter of femur_.

1. In row _[294](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=294:294)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[294](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=294:294)_, no term id was found for the name/label _linea aspera of femur_.

1. In row _[295](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=295:295)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[296](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=296:296)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[297](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=297:297)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[297](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=297:297)_, no term id was found for the name/label _medial lip of linea aspera of femur_.

1. In row _[298](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=298:298)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[299](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=299:299)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[299](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=299:299)_, no term id was found for the name/label _pectinal line of femur_.

1. In row _[300](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=300:300)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[300](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=300:300)_, no term id was found for the name/label _popliteal surface of femur_.

1. In row _[301](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=301:301)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[301](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=301:301)_, no term id was found for the name/label _quadrate tubercle of femur_.

1. In row _[302](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=302:302)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[302](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=302:302)_, no term id was found for the name/label _shaft of femur_.

1. In row _[303](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=303:303)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[303](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=303:303)_, no term id was found for the name/label _trochanteric fossa of femur_.

1. In row _[304](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=304:304)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[305](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=305:305)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[305](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=305:305)_, no term id was found for the name/label _head of fibula_.

1. In row _[306](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=306:306)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[307](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=307:307)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[308](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=308:308)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[308](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=308:308)_, no term id was found for the name/label _shaft of fibula_.

1. In row _[309](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=309:309)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[310](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=310:310)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[311](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=311:311)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[311](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=311:311)_, no term id was found for the name/label _anterolateral tubercle of tibia_.

1. In row _[312](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=312:312)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[312](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=312:312)_, no term id was found for the name/label _fibular facet of tibia_.

1. In row _[313](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=313:313)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[313](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=313:313)_, no term id was found for the name/label _fibular notch of tibia_.

1. In row _[314](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=314:314)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[314](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=314:314)_, no term id was found for the name/label _intercondylar eminence of tibia_.

1. In row _[315](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=315:315)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[315](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=315:315)_, no term id was found for the name/label _interosseus border of tibia_.

1. In row _[316](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=316:316)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[317](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=317:317)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[318](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=318:318)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[318](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=318:318)_, no term id was found for the name/label _medial malleolus of tibia_.

1. In row _[319](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=319:319)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[319](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=319:319)_, no term id was found for the name/label _shaft of tibia_.

1. In row _[320](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=320:320)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[320](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=320:320)_, no term id was found for the name/label _soleal line of tibia_.

1. In row _[321](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=321:321)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[321](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=321:321)_, no term id was found for the name/label _tibial plateau of tibia_.

1. In row _[322](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=322:322)_, no term id was found for the name/label _free part of leg bone_.

1. In row _[322](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=322:322)_, no term id was found for the name/label _tibial tuberosity of tibia_.

1. In row _[325](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=325:325)_, no term id was found for the name/label _acetabular fossa of os coxa_.

1. In row _[326](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=326:326)_, no term id was found for the name/label _acetabular notch of os coxa_.

1. In row _[327](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=327:327)_, no term id was found for the name/label _acetabulum of os coxa_.

1. In row _[328](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=328:328)_, no term id was found for the name/label _anterior gluteal line of ilium of os coxa_.

1. In row _[329](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=329:329)_, no term id was found for the name/label _anterior inferior iliac spine of ilium of os coxa_.

1. In row _[330](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=330:330)_, no term id was found for the name/label _anterior superior iliac spine of ilium of os coxa_.

1. In row _[331](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=331:331)_, no term id was found for the name/label _arcuate line of ilium of os coxa_.

1. In row _[332](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=332:332)_, no term id was found for the name/label _auricular surface of ilium of os coxa_.

1. In row _[333](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=333:333)_, no term id was found for the name/label _gluteal surface of ilium of os coxa_.

1. In row _[334](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=334:334)_, no term id was found for the name/label _greater sciatic notch of ilium of os coxa_.

1. In row _[335](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=335:335)_, no term id was found for the name/label _iliac crest of ilium of os coxa_.

1. In row _[336](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=336:336)_, no term id was found for the name/label _iliac fossa of ilium of os coxa_.

1. In row _[337](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=337:337)_, no term id was found for the name/label _iliac tubercle of ilium of os coxa_.

1. In row _[338](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=338:338)_, no term id was found for the name/label _iliac tuberosity of ilium of os coxa_.

1. In row _[339](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=339:339)_, no term id was found for the name/label _iliopubic ramus of os coxa_.

1. In row _[340](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=340:340)_, no term id was found for the name/label _inferior pubic ramus of pubis of os coxa_.

1. In row _[341](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=341:341)_, no term id was found for the name/label _ischial body of ischium of os coxa_.

1. In row _[342](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=342:342)_, no term id was found for the name/label _ischial ramus of ischium of os coxa_.

1. In row _[343](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=343:343)_, no term id was found for the name/label _ischial spine of ischium of os coxa_.

1. In row _[344](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=344:344)_, no term id was found for the name/label _ischial tuberosity of ischium of os coxa_.

1. In row _[345](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=345:345)_, no term id was found for the name/label _ischiopubic ramus of os coxa_.

1. In row _[346](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=346:346)_, no term id was found for the name/label _lesser sciatic notch of ischium of os coxa_.

1. In row _[347](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=347:347)_, no term id was found for the name/label _lunate surface of os coxa_.

1. In row _[348](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=348:348)_, no term id was found for the name/label _obturator foramen of os coxa_.

1. In row _[349](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=349:349)_, no term id was found for the name/label _obturator groove of pubis of os coxa_.

1. In row _[350](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=350:350)_, no term id was found for the name/label _pecten pubis of pubis of os coxa_.

1. In row _[351](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=351:351)_, no term id was found for the name/label _posterior gluteal line of ilium of os coxa_.

1. In row _[352](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=352:352)_, no term id was found for the name/label _posterior inferior iliac spine of ilium of os coxa_.

1. In row _[353](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=353:353)_, no term id was found for the name/label _posterior superior iliac spine of ilium of os coxa_.

1. In row _[354](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=354:354)_, no term id was found for the name/label _pubic body of pubis of os coxa_.

1. In row _[355](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=355:355)_, no term id was found for the name/label _pubic crest of pubis of os coxa_.

1. In row _[356](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=356:356)_, no term id was found for the name/label _pubic symphysis of pubis of os coxa_.

1. In row _[357](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=357:357)_, no term id was found for the name/label _pubic tubercle of pubis of os coxa_.

1. In row _[358](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=358:358)_, no term id was found for the name/label _superior pubic ramus of pubis of os coxa_.

1. In row _[361](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=361:361)_, no term id was found for the name/label _hyoid region bone_.

1. In row _[362](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=362:362)_, no term id was found for the name/label _hyoid region bone_.

1. In row _[363](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=363:363)_, no term id was found for the name/label _hyoid region bone_.

1. In row _[363](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=363:363)_, no term id was found for the name/label _body of hyoid bone_.

1. In row _[364](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=364:364)_, no term id was found for the name/label _hyoid region bone_.

1. In row _[364](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=364:364)_, no term id was found for the name/label _greater cornu of hyoid bone_.

1. In row _[365](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=365:365)_, no term id was found for the name/label _hyoid region bone_.

1. In row _[365](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=365:365)_, no term id was found for the name/label _lesser cornu of hyoid bone_.

1. In row _[368](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=368:368)_, no term id was found for the name/label _anterior ethmoidal foramen of ethmoid bone_.

1. In row _[369](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=369:369)_, no term id was found for the name/label _cribiform plate of ethmoid bone_.

1. In row _[370](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=370:370)_, no term id was found for the name/label _crista galla of ethmoid bone_.

1. In row _[371](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=371:371)_, no term id was found for the name/label _ethmoidal air cells of ethmoid bone_.

1. In row _[372](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=372:372)_, no term id was found for the name/label _ethmoidal bulla of ethmoid bone_.

1. In row _[373](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=373:373)_, no term id was found for the name/label _middle nasal concha of ethmoid bone_.

1. In row _[374](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=374:374)_, no term id was found for the name/label _olfactory foramina of ethmoid bone_.

1. In row _[375](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=375:375)_, no term id was found for the name/label _perpendicular plate of ethmoid bone_.

1. In row _[376](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=376:376)_, no term id was found for the name/label _posterior ethmoidal foramen of ethmoid bone_.

1. In row _[377](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=377:377)_, no term id was found for the name/label _superior nasal concha of ethmoid bone_.

1. In row _[379](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=379:379)_, no term id was found for the name/label _frontal crest of frontal bone_.

1. In row _[380](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=380:380)_, no term id was found for the name/label _frontal sinus of frontal bone_.

1. In row _[381](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=381:381)_, no term id was found for the name/label _glabella of frontal bone_.

1. In row _[382](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=382:382)_, no term id was found for the name/label _groove for superior sagittal sinus of frontal bone_.

1. In row _[383](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=383:383)_, no term id was found for the name/label _lacrimal fossa of frontal bone_.

1. In row _[384](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=384:384)_, no term id was found for the name/label _orbital surface of frontal bone_.

1. In row _[385](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=385:385)_, no term id was found for the name/label _supercilary arch of frontal bone_.

1. In row _[386](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=386:386)_, no term id was found for the name/label _supraorbital margin of frontal bone_.

1. In row _[387](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=387:387)_, no term id was found for the name/label _supraorbital notch or foramen of frontal bone_.

1. In row _[390](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=390:390)_, no term id was found for the name/label _external occipital protuberance of squamous part of occipital bone_.

1. In row _[391](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=391:391)_, no term id was found for the name/label _foramen magnum of basilar part of occipital bone_.

1. In row _[392](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=392:392)_, no term id was found for the name/label _groove for transverse sinus of squamous part of occipital bone_.

1. In row _[393](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=393:393)_, no term id was found for the name/label _hypoglossal canal of basilar part of occipital bone_.

1. In row _[394](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=394:394)_, no term id was found for the name/label _inferior nuchal line of squamous part of occipital bone_.

1. In row _[395](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=395:395)_, no term id was found for the name/label _internal occipital protuberance of squamous part of occipital bone_.

1. In row _[396](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=396:396)_, no term id was found for the name/label _jugular foramen of basilar part of occipital bone_.

1. In row _[397](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=397:397)_, no term id was found for the name/label _occipital condyle of basilar part of occipital bone_.

1. In row _[398](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=398:398)_, no term id was found for the name/label _superior nuchal line of squamous part of occipital bone_.

1. In row _[400](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=400:400)_, no term id was found for the name/label _granula foveaolae of parietal bone_.

1. In row _[401](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=401:401)_, no term id was found for the name/label _groove for middle meningeal a. of parietal bone_.

1. In row _[402](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=402:402)_, no term id was found for the name/label _groove for superior sagittal sinus of parietal bone_.

1. In row _[403](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=403:403)_, no term id was found for the name/label _inferior temporal line of parietal bone_.

1. In row _[404](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=404:404)_, no term id was found for the name/label _superior temporal line of parietal bone_.

1. In row _[405](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=405:405)_, no term id was found for the name/label _temporal fossa of parietal bone_.

1. In row _[407](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=407:407)_, no term id was found for the name/label _anterior clinoid process of sphenoid bone_.

1. In row _[408](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=408:408)_, no term id was found for the name/label _body of sphenoid bone_.

1. In row _[409](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=409:409)_, no term id was found for the name/label _dorsum sellae of sphenoid bone_.

1. In row _[410](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=410:410)_, no term id was found for the name/label _foramen lacerum of sphenoid bone_.

1. In row _[411](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=411:411)_, no term id was found for the name/label _foramen ovale of sphenoid bone_.

1. In row _[412](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=412:412)_, no term id was found for the name/label _foramen rotundum of sphenoid bone_.

1. In row _[414](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=414:414)_, no term id was found for the name/label _greater wings of sphenoid bone_.

1. In row _[415](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=415:415)_, no term id was found for the name/label _hypophyseal fossa of sphenoid bone_.

1. In row _[416](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=416:416)_, no term id was found for the name/label _lateral pterygoid plate of sphenoid bone_.

1. In row _[417](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=417:417)_, no term id was found for the name/label _lesser wings of sphenoid bone_.

1. In row _[418](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=418:418)_, no term id was found for the name/label _medial pterygoid plate of sphenoid bone_.

1. In row _[419](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=419:419)_, no term id was found for the name/label _optic canal of sphenoid bone_.

1. In row _[420](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=420:420)_, no term id was found for the name/label _posterior clinoid process of sphenoid bone_.

1. In row _[421](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=421:421)_, no term id was found for the name/label _pterygoid canal of sphenoid bone_.

1. In row _[422](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=422:422)_, no term id was found for the name/label _pterygoid fossa of sphenoid bone_.

1. In row _[423](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=423:423)_, no term id was found for the name/label _pterygoid hamulus of sphenoid bone_.

1. In row _[424](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=424:424)_, no term id was found for the name/label _pterygoid process of sphenoid bone_.

1. In row _[425](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=425:425)_, no term id was found for the name/label _sella turcica of sphenoid bone_.

1. In row _[426](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=426:426)_, no term id was found for the name/label _sphenoid sinus of sphenoid bone_.

1. In row _[427](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=427:427)_, no term id was found for the name/label _superior orbital fissure of sphenoid bone_.

1. In row _[429](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=429:429)_, no term id was found for the name/label _articular tubercle of squamous part of temporal bone_.

1. In row _[430](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=430:430)_, no term id was found for the name/label _carotid canal of petrous part of temporal bone_.

1. In row _[431](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=431:431)_, no term id was found for the name/label _external auditory meatus of squamous part of temporal bone_.

1. In row _[432](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=432:432)_, no term id was found for the name/label _groove for posterior deep temporal artery of squamous part of temporal bone_.

1. In row _[433](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=433:433)_, no term id was found for the name/label _groove for sigmoid sinus of mastoid part of temporal bone_.

1. In row _[434](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=434:434)_, no term id was found for the name/label _hiatus and groove of petrous part of temporal bone for greater petrosal nerve_.

1. In row _[435](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=435:435)_, no term id was found for the name/label _hiatus and groove of petrous part of temporal bone for lesser petrosal nerve_.

1. In row _[436](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=436:436)_, no term id was found for the name/label _internal auditory meatus of petrous part of temporal bone_.

1. In row _[437](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=437:437)_, no term id was found for the name/label _jugular foramen of petrous part of temporal bone_.

1. In row _[438](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=438:438)_, no term id was found for the name/label _mandibular fossa of squamous part of temporal bone_.

1. In row _[439](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=439:439)_, no term id was found for the name/label _mastoid foramen of mastoid part of temporal bone_.

1. In row _[440](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=440:440)_, no term id was found for the name/label _mastoid notch of mastoid part of temporal bone_.

1. In row _[441](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=441:441)_, no term id was found for the name/label _mastoid process of mastoid part of temporal bone_.

1. In row _[442](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=442:442)_, no term id was found for the name/label _petrotympanic fissure of squamous part of temporal bone_.

1. In row _[443](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=443:443)_, no term id was found for the name/label _postglenoid tubercle of squamous part of temporal bone_.

1. In row _[444](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=444:444)_, no term id was found for the name/label _styloid process of petrous part of temporal bone_.

1. In row _[445](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=445:445)_, no term id was found for the name/label _stylomastoid foramen of petrous part of temporal bone_.

1. In row _[446](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=446:446)_, no term id was found for the name/label _supramastoid crest of squamous part of temporal bone_.

1. In row _[447](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=447:447)_, no term id was found for the name/label _trigeminal impression of petrous part of temporal bone_.

1. In row _[448](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=448:448)_, no term id was found for the name/label _tympanic caniliculus of petrous part of temporal bone_.

1. In row _[449](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=449:449)_, no term id was found for the name/label _zygomatic process of squamous part of temporal bone_.

1. In row _[457](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=457:457)_, no term id was found for the name/label _fossa for lacrimal sac of lacrimal bone_.

1. In row _[459](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=459:459)_, no term id was found for the name/label _alveolar border of mandible_.

1. In row _[461](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=461:461)_, no term id was found for the name/label _coronoid process of mandible_.

1. In row _[462](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=462:462)_, no term id was found for the name/label _digastric fossa of mandible_.

1. In row _[463](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=463:463)_, no term id was found for the name/label _inferior mental spine of mandible_.

1. In row _[464](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=464:464)_, no term id was found for the name/label _lingula of mandible_.

1. In row _[465](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=465:465)_, no term id was found for the name/label _mandibular angle of mandible_.

1. In row _[466](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=466:466)_, no term id was found for the name/label _mandibular canal of mandible_.

1. In row _[467](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=467:467)_, no term id was found for the name/label _mandibular condyle of mandible_.

1. In row _[468](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=468:468)_, no term id was found for the name/label _mandibular foramen of mandible_.

1. In row _[469](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=469:469)_, no term id was found for the name/label _mandibular neck of mandible_.

1. In row _[470](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=470:470)_, no term id was found for the name/label _mandibular notch of mandible_.

1. In row _[471](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=471:471)_, no term id was found for the name/label _mental foramen of mandible_.

1. In row _[472](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=472:472)_, no term id was found for the name/label _mental protuberance of mandible_.

1. In row _[473](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=473:473)_, no term id was found for the name/label _mylohyoid groove of mandible_.

1. In row _[474](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=474:474)_, no term id was found for the name/label _mylohyoid line of mandible_.

1. In row _[475](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=475:475)_, no term id was found for the name/label _pterygoid fovea of mandible_.

1. In row _[476](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=476:476)_, no term id was found for the name/label _ramus of mandible_.

1. In row _[477](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=477:477)_, no term id was found for the name/label _sublingual fossa of mandible_.

1. In row _[478](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=478:478)_, no term id was found for the name/label _submandibular fossa of mandible_.

1. In row _[479](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=479:479)_, no term id was found for the name/label _superior mental spine of mandible_.

1. In row _[481](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=481:481)_, no term id was found for the name/label _alveolar canals of maxilla_.

1. In row _[485](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=485:485)_, no term id was found for the name/label _greater palatine canal of maxilla_.

1. In row _[486](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=486:486)_, no term id was found for the name/label _incisive foramen of maxilla_.

1. In row _[487](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=487:487)_, no term id was found for the name/label _infraorbital canal of maxilla_.

1. In row _[488](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=488:488)_, no term id was found for the name/label _infraorbital foramen of maxilla_.

1. In row _[489](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=489:489)_, no term id was found for the name/label _infraorbital groove of maxilla_.

1. In row _[490](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=490:490)_, no term id was found for the name/label _intermaxillary suture of maxilla_.

1. In row _[491](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=491:491)_, no term id was found for the name/label _maxillary sinus of maxilla_.

1. In row _[492](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=492:492)_, no term id was found for the name/label _nasal surface of maxilla_.

1. In row _[493](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=493:493)_, no term id was found for the name/label _nasolacrimal canal of maxilla_.

1. In row _[498](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=498:498)_, no term id was found for the name/label _greater palatine foramen of palatine bone_.

1. In row _[499](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=499:499)_, no term id was found for the name/label _horizontal plate of palatine bone_.

1. In row _[500](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=500:500)_, no term id was found for the name/label _lesser palatine foramen of palatine bone_.

1. In row _[501](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=501:501)_, no term id was found for the name/label _perpendicular plate of palatine bone_.

1. In row _[503](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=503:503)_, no term id was found for the name/label _ala of vomer_.

1. In row _[504](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=504:504)_, no term id was found for the name/label _groove for nasopalatine nerve of vomer_.

1. In row _[507](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=507:507)_, no term id was found for the name/label _maxillary process of zygomatic bone_.

1. In row _[509](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=509:509)_, no term id was found for the name/label _zygomaticofacial foramen of zygomatic bone_.

1. In row _[511](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=511:511)_, no term id was found for the name/label _costal region bone_.

1. In row _[512](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=512:512)_, no term id was found for the name/label _costal region bone_.

1. In row _[513](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=513:513)_, no term id was found for the name/label _costal region bone_.

1. In row _[513](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=513:513)_, no term id was found for the name/label _angle of first rib_.

1. In row _[514](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=514:514)_, no term id was found for the name/label _costal region bone_.

1. In row _[514](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=514:514)_, no term id was found for the name/label _articular facet of tubercle of first rib_.

1. In row _[515](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=515:515)_, no term id was found for the name/label _costal region bone_.

1. In row _[515](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=515:515)_, no term id was found for the name/label _body of first rib_.

1. In row _[516](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=516:516)_, no term id was found for the name/label _costal region bone_.

1. In row _[516](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=516:516)_, no term id was found for the name/label _costal groove of first rib_.

1. In row _[517](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=517:517)_, no term id was found for the name/label _costal region bone_.

1. In row _[517](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=517:517)_, no term id was found for the name/label _facet of first rib_.

1. In row _[518](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=518:518)_, no term id was found for the name/label _costal region bone_.

1. In row _[518](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=518:518)_, no term id was found for the name/label _groove for subclavian artery of first rib_.

1. In row _[519](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=519:519)_, no term id was found for the name/label _costal region bone_.

1. In row _[519](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=519:519)_, no term id was found for the name/label _groove for subclavian vein of first rib_.

1. In row _[520](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=520:520)_, no term id was found for the name/label _costal region bone_.

1. In row _[520](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=520:520)_, no term id was found for the name/label _head of first rib_.

1. In row _[521](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=521:521)_, no term id was found for the name/label _costal region bone_.

1. In row _[521](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=521:521)_, no term id was found for the name/label _neck of first rib_.

1. In row _[522](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=522:522)_, no term id was found for the name/label _costal region bone_.

1. In row _[522](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=522:522)_, no term id was found for the name/label _non-articular facet of tubercle of first rib_.

1. In row _[523](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=523:523)_, no term id was found for the name/label _costal region bone_.

1. In row _[523](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=523:523)_, no term id was found for the name/label _scalene tubercle of first rib_.

1. In row _[524](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=524:524)_, no term id was found for the name/label _costal region bone_.

1. In row _[524](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=524:524)_, no term id was found for the name/label _sternal end of first rib_.

1. In row _[525](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=525:525)_, no term id was found for the name/label _costal region bone_.

1. In row _[525](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=525:525)_, no term id was found for the name/label _tubercle of first rib_.

1. In row _[526](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=526:526)_, no term id was found for the name/label _costal region bone_.

1. In row _[527](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=527:527)_, no term id was found for the name/label _costal region bone_.

1. In row _[527](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=527:527)_, no term id was found for the name/label _angle of tenth rib_.

1. In row _[528](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=528:528)_, no term id was found for the name/label _costal region bone_.

1. In row _[528](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=528:528)_, no term id was found for the name/label _articular facet of tubercle of tenth rib_.

1. In row _[529](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=529:529)_, no term id was found for the name/label _costal region bone_.

1. In row _[529](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=529:529)_, no term id was found for the name/label _body of tenth rib_.

1. In row _[530](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=530:530)_, no term id was found for the name/label _costal region bone_.

1. In row _[530](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=530:530)_, no term id was found for the name/label _costal groove of tenth rib_.

1. In row _[531](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=531:531)_, no term id was found for the name/label _costal region bone_.

1. In row _[531](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=531:531)_, no term id was found for the name/label _facet of tenth rib_.

1. In row _[532](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=532:532)_, no term id was found for the name/label _costal region bone_.

1. In row _[532](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=532:532)_, no term id was found for the name/label _head of tenth rib_.

1. In row _[533](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=533:533)_, no term id was found for the name/label _costal region bone_.

1. In row _[533](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=533:533)_, no term id was found for the name/label _neck of tenth rib_.

1. In row _[534](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=534:534)_, no term id was found for the name/label _costal region bone_.

1. In row _[534](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=534:534)_, no term id was found for the name/label _non-articular facet of tubercle of tenth rib_.

1. In row _[535](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=535:535)_, no term id was found for the name/label _costal region bone_.

1. In row _[535](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=535:535)_, no term id was found for the name/label _sternal end of tenth rib_.

1. In row _[536](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=536:536)_, no term id was found for the name/label _costal region bone_.

1. In row _[536](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=536:536)_, no term id was found for the name/label _tubercle of tenth rib_.

1. In row _[537](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=537:537)_, no term id was found for the name/label _costal region bone_.

1. In row _[538](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=538:538)_, no term id was found for the name/label _costal region bone_.

1. In row _[538](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=538:538)_, no term id was found for the name/label _body of eleventh rib_.

1. In row _[539](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=539:539)_, no term id was found for the name/label _costal region bone_.

1. In row _[539](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=539:539)_, no term id was found for the name/label _costal groove of eleventh rib_.

1. In row _[540](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=540:540)_, no term id was found for the name/label _costal region bone_.

1. In row _[540](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=540:540)_, no term id was found for the name/label _facet of eleventh rib_.

1. In row _[541](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=541:541)_, no term id was found for the name/label _costal region bone_.

1. In row _[541](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=541:541)_, no term id was found for the name/label _head of eleventh rib_.

1. In row _[542](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=542:542)_, no term id was found for the name/label _costal region bone_.

1. In row _[542](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=542:542)_, no term id was found for the name/label _sternal end of eleventh rib_.

1. In row _[543](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=543:543)_, no term id was found for the name/label _costal region bone_.

1. In row _[544](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=544:544)_, no term id was found for the name/label _costal region bone_.

1. In row _[544](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=544:544)_, no term id was found for the name/label _body of twelfth rib_.

1. In row _[545](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=545:545)_, no term id was found for the name/label _costal region bone_.

1. In row _[545](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=545:545)_, no term id was found for the name/label _costal groove of twelfth rib_.

1. In row _[546](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=546:546)_, no term id was found for the name/label _costal region bone_.

1. In row _[546](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=546:546)_, no term id was found for the name/label _facet of twelfth rib_.

1. In row _[547](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=547:547)_, no term id was found for the name/label _costal region bone_.

1. In row _[547](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=547:547)_, no term id was found for the name/label _head of twelfth rib_.

1. In row _[548](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=548:548)_, no term id was found for the name/label _costal region bone_.

1. In row _[548](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=548:548)_, no term id was found for the name/label _sternal end of twelfth rib_.

1. In row _[549](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=549:549)_, no term id was found for the name/label _costal region bone_.

1. In row _[550](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=550:550)_, no term id was found for the name/label _costal region bone_.

1. In row _[550](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=550:550)_, no term id was found for the name/label _angle of second rib_.

1. In row _[551](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=551:551)_, no term id was found for the name/label _costal region bone_.

1. In row _[551](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=551:551)_, no term id was found for the name/label _articular facet of tubercle of second rib_.

1. In row _[552](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=552:552)_, no term id was found for the name/label _costal region bone_.

1. In row _[552](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=552:552)_, no term id was found for the name/label _body of second rib_.

1. In row _[553](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=553:553)_, no term id was found for the name/label _costal region bone_.

1. In row _[553](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=553:553)_, no term id was found for the name/label _costal groove of second rib_.

1. In row _[554](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=554:554)_, no term id was found for the name/label _costal region bone_.

1. In row _[554](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=554:554)_, no term id was found for the name/label _head of second rib_.

1. In row _[555](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=555:555)_, no term id was found for the name/label _costal region bone_.

1. In row _[555](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=555:555)_, no term id was found for the name/label _inferior articular facet of second rib_.

1. In row _[556](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=556:556)_, no term id was found for the name/label _costal region bone_.

1. In row _[556](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=556:556)_, no term id was found for the name/label _neck of second rib_.

1. In row _[557](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=557:557)_, no term id was found for the name/label _costal region bone_.

1. In row _[557](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=557:557)_, no term id was found for the name/label _non-articular facet of tubercle of second rib_.

1. In row _[558](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=558:558)_, no term id was found for the name/label _costal region bone_.

1. In row _[558](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=558:558)_, no term id was found for the name/label _sternal end of second rib_.

1. In row _[559](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=559:559)_, no term id was found for the name/label _costal region bone_.

1. In row _[559](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=559:559)_, no term id was found for the name/label _superior articular facet of second rib_.

1. In row _[560](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=560:560)_, no term id was found for the name/label _costal region bone_.

1. In row _[560](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=560:560)_, no term id was found for the name/label _tubercle of second rib_.

1. In row _[561](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=561:561)_, no term id was found for the name/label _costal region bone_.

1. In row _[562](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=562:562)_, no term id was found for the name/label _costal region bone_.

1. In row _[562](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=562:562)_, no term id was found for the name/label _angle of third rib_.

1. In row _[563](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=563:563)_, no term id was found for the name/label _costal region bone_.

1. In row _[563](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=563:563)_, no term id was found for the name/label _articular facet of tubercle of third rib_.

1. In row _[564](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=564:564)_, no term id was found for the name/label _costal region bone_.

1. In row _[564](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=564:564)_, no term id was found for the name/label _body of third rib_.

1. In row _[565](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=565:565)_, no term id was found for the name/label _costal region bone_.

1. In row _[565](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=565:565)_, no term id was found for the name/label _costal groove of third rib_.

1. In row _[566](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=566:566)_, no term id was found for the name/label _costal region bone_.

1. In row _[566](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=566:566)_, no term id was found for the name/label _crest of head of third rib_.

1. In row _[567](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=567:567)_, no term id was found for the name/label _costal region bone_.

1. In row _[567](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=567:567)_, no term id was found for the name/label _head of third rib_.

1. In row _[568](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=568:568)_, no term id was found for the name/label _costal region bone_.

1. In row _[568](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=568:568)_, no term id was found for the name/label _inferior articular facet of third rib_.

1. In row _[569](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=569:569)_, no term id was found for the name/label _costal region bone_.

1. In row _[569](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=569:569)_, no term id was found for the name/label _neck of third rib_.

1. In row _[570](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=570:570)_, no term id was found for the name/label _costal region bone_.

1. In row _[570](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=570:570)_, no term id was found for the name/label _non-articular facet of tubercle of third rib_.

1. In row _[571](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=571:571)_, no term id was found for the name/label _costal region bone_.

1. In row _[571](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=571:571)_, no term id was found for the name/label _sternal end of third rib_.

1. In row _[572](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=572:572)_, no term id was found for the name/label _costal region bone_.

1. In row _[572](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=572:572)_, no term id was found for the name/label _superior articular facet of third rib_.

1. In row _[573](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=573:573)_, no term id was found for the name/label _costal region bone_.

1. In row _[573](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=573:573)_, no term id was found for the name/label _tubercle of third rib_.

1. In row _[574](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=574:574)_, no term id was found for the name/label _costal region bone_.

1. In row _[575](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=575:575)_, no term id was found for the name/label _costal region bone_.

1. In row _[575](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=575:575)_, no term id was found for the name/label _angle of fourth rib_.

1. In row _[576](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=576:576)_, no term id was found for the name/label _costal region bone_.

1. In row _[576](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=576:576)_, no term id was found for the name/label _articular facet of tubercle of fourth rib_.

1. In row _[577](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=577:577)_, no term id was found for the name/label _costal region bone_.

1. In row _[577](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=577:577)_, no term id was found for the name/label _body of fourth rib_.

1. In row _[578](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=578:578)_, no term id was found for the name/label _costal region bone_.

1. In row _[578](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=578:578)_, no term id was found for the name/label _costal groove of fourth rib_.

1. In row _[579](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=579:579)_, no term id was found for the name/label _costal region bone_.

1. In row _[579](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=579:579)_, no term id was found for the name/label _crest of head of fourth rib_.

1. In row _[580](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=580:580)_, no term id was found for the name/label _costal region bone_.

1. In row _[580](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=580:580)_, no term id was found for the name/label _head of fourth rib_.

1. In row _[581](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=581:581)_, no term id was found for the name/label _costal region bone_.

1. In row _[581](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=581:581)_, no term id was found for the name/label _inferior articular facet of fourth rib_.

1. In row _[582](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=582:582)_, no term id was found for the name/label _costal region bone_.

1. In row _[582](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=582:582)_, no term id was found for the name/label _neck of fourth rib_.

1. In row _[583](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=583:583)_, no term id was found for the name/label _costal region bone_.

1. In row _[583](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=583:583)_, no term id was found for the name/label _non-articular facet of tubercle of fourth rib_.

1. In row _[584](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=584:584)_, no term id was found for the name/label _costal region bone_.

1. In row _[584](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=584:584)_, no term id was found for the name/label _sternal end of fourth rib_.

1. In row _[585](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=585:585)_, no term id was found for the name/label _costal region bone_.

1. In row _[585](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=585:585)_, no term id was found for the name/label _superior articular facet of fourth rib_.

1. In row _[586](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=586:586)_, no term id was found for the name/label _costal region bone_.

1. In row _[586](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=586:586)_, no term id was found for the name/label _tubercle of fourth rib_.

1. In row _[587](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=587:587)_, no term id was found for the name/label _costal region bone_.

1. In row _[588](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=588:588)_, no term id was found for the name/label _costal region bone_.

1. In row _[588](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=588:588)_, no term id was found for the name/label _angle of fifth rib_.

1. In row _[589](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=589:589)_, no term id was found for the name/label _costal region bone_.

1. In row _[589](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=589:589)_, no term id was found for the name/label _articular facet of tubercle of fifth rib_.

1. In row _[590](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=590:590)_, no term id was found for the name/label _costal region bone_.

1. In row _[590](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=590:590)_, no term id was found for the name/label _body of fifth rib_.

1. In row _[591](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=591:591)_, no term id was found for the name/label _costal region bone_.

1. In row _[591](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=591:591)_, no term id was found for the name/label _costal groove of fifth rib_.

1. In row _[592](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=592:592)_, no term id was found for the name/label _costal region bone_.

1. In row _[592](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=592:592)_, no term id was found for the name/label _crest of head of fifth rib_.

1. In row _[593](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=593:593)_, no term id was found for the name/label _costal region bone_.

1. In row _[593](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=593:593)_, no term id was found for the name/label _head of fifth rib_.

1. In row _[594](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=594:594)_, no term id was found for the name/label _costal region bone_.

1. In row _[594](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=594:594)_, no term id was found for the name/label _inferior articular facet of fifth rib_.

1. In row _[595](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=595:595)_, no term id was found for the name/label _costal region bone_.

1. In row _[595](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=595:595)_, no term id was found for the name/label _neck of fifth rib_.

1. In row _[596](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=596:596)_, no term id was found for the name/label _costal region bone_.

1. In row _[596](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=596:596)_, no term id was found for the name/label _non-articular facet of tubercle of fifth rib_.

1. In row _[597](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=597:597)_, no term id was found for the name/label _costal region bone_.

1. In row _[597](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=597:597)_, no term id was found for the name/label _sternal end of fifth rib_.

1. In row _[598](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=598:598)_, no term id was found for the name/label _costal region bone_.

1. In row _[598](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=598:598)_, no term id was found for the name/label _superior articular facet of fifth rib_.

1. In row _[599](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=599:599)_, no term id was found for the name/label _costal region bone_.

1. In row _[599](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=599:599)_, no term id was found for the name/label _tubercle of fifth rib_.

1. In row _[600](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=600:600)_, no term id was found for the name/label _costal region bone_.

1. In row _[601](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=601:601)_, no term id was found for the name/label _costal region bone_.

1. In row _[601](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=601:601)_, no term id was found for the name/label _angle of sixth rib_.

1. In row _[602](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=602:602)_, no term id was found for the name/label _costal region bone_.

1. In row _[602](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=602:602)_, no term id was found for the name/label _articular facet of tubercle of sixth rib_.

1. In row _[603](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=603:603)_, no term id was found for the name/label _costal region bone_.

1. In row _[603](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=603:603)_, no term id was found for the name/label _body of sixth rib_.

1. In row _[604](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=604:604)_, no term id was found for the name/label _costal region bone_.

1. In row _[604](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=604:604)_, no term id was found for the name/label _costal groove of sixth rib_.

1. In row _[605](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=605:605)_, no term id was found for the name/label _costal region bone_.

1. In row _[605](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=605:605)_, no term id was found for the name/label _crest of head of sixth rib_.

1. In row _[606](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=606:606)_, no term id was found for the name/label _costal region bone_.

1. In row _[606](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=606:606)_, no term id was found for the name/label _head of sixth rib_.

1. In row _[607](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=607:607)_, no term id was found for the name/label _costal region bone_.

1. In row _[607](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=607:607)_, no term id was found for the name/label _inferior articular facet of sixth rib_.

1. In row _[608](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=608:608)_, no term id was found for the name/label _costal region bone_.

1. In row _[608](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=608:608)_, no term id was found for the name/label _neck of sixth rib_.

1. In row _[609](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=609:609)_, no term id was found for the name/label _costal region bone_.

1. In row _[609](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=609:609)_, no term id was found for the name/label _non-articular facet of tubercle of sixth rib_.

1. In row _[610](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=610:610)_, no term id was found for the name/label _costal region bone_.

1. In row _[610](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=610:610)_, no term id was found for the name/label _sternal end of sixth rib_.

1. In row _[611](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=611:611)_, no term id was found for the name/label _costal region bone_.

1. In row _[611](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=611:611)_, no term id was found for the name/label _superior articular facet of sixth rib_.

1. In row _[612](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=612:612)_, no term id was found for the name/label _costal region bone_.

1. In row _[612](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=612:612)_, no term id was found for the name/label _tubercle of sixth rib_.

1. In row _[613](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=613:613)_, no term id was found for the name/label _costal region bone_.

1. In row _[614](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=614:614)_, no term id was found for the name/label _costal region bone_.

1. In row _[614](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=614:614)_, no term id was found for the name/label _angle of seventh rib_.

1. In row _[615](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=615:615)_, no term id was found for the name/label _costal region bone_.

1. In row _[615](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=615:615)_, no term id was found for the name/label _articular facet of tubercle of seventh rib_.

1. In row _[616](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=616:616)_, no term id was found for the name/label _costal region bone_.

1. In row _[616](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=616:616)_, no term id was found for the name/label _body of seventh rib_.

1. In row _[617](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=617:617)_, no term id was found for the name/label _costal region bone_.

1. In row _[617](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=617:617)_, no term id was found for the name/label _costal groove of seventh rib_.

1. In row _[618](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=618:618)_, no term id was found for the name/label _costal region bone_.

1. In row _[618](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=618:618)_, no term id was found for the name/label _crest of head of seventh rib_.

1. In row _[619](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=619:619)_, no term id was found for the name/label _costal region bone_.

1. In row _[619](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=619:619)_, no term id was found for the name/label _head of seventh rib_.

1. In row _[620](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=620:620)_, no term id was found for the name/label _costal region bone_.

1. In row _[620](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=620:620)_, no term id was found for the name/label _inferior articular facet of seventh rib_.

1. In row _[621](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=621:621)_, no term id was found for the name/label _costal region bone_.

1. In row _[621](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=621:621)_, no term id was found for the name/label _neck of seventh rib_.

1. In row _[622](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=622:622)_, no term id was found for the name/label _costal region bone_.

1. In row _[622](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=622:622)_, no term id was found for the name/label _non-articular facet of tubercle of seventh rib_.

1. In row _[623](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=623:623)_, no term id was found for the name/label _costal region bone_.

1. In row _[623](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=623:623)_, no term id was found for the name/label _sternal end of seventh rib_.

1. In row _[624](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=624:624)_, no term id was found for the name/label _costal region bone_.

1. In row _[624](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=624:624)_, no term id was found for the name/label _superior articular facet of seventh rib_.

1. In row _[625](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=625:625)_, no term id was found for the name/label _costal region bone_.

1. In row _[625](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=625:625)_, no term id was found for the name/label _tubercle of seventh rib_.

1. In row _[626](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=626:626)_, no term id was found for the name/label _costal region bone_.

1. In row _[627](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=627:627)_, no term id was found for the name/label _costal region bone_.

1. In row _[627](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=627:627)_, no term id was found for the name/label _angle of eighth rib_.

1. In row _[628](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=628:628)_, no term id was found for the name/label _costal region bone_.

1. In row _[628](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=628:628)_, no term id was found for the name/label _articular facet of tubercle of eighth rib_.

1. In row _[629](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=629:629)_, no term id was found for the name/label _costal region bone_.

1. In row _[629](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=629:629)_, no term id was found for the name/label _body of eighth rib_.

1. In row _[630](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=630:630)_, no term id was found for the name/label _costal region bone_.

1. In row _[630](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=630:630)_, no term id was found for the name/label _costal groove of eighth rib_.

1. In row _[631](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=631:631)_, no term id was found for the name/label _costal region bone_.

1. In row _[631](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=631:631)_, no term id was found for the name/label _crest of head of eighth rib_.

1. In row _[632](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=632:632)_, no term id was found for the name/label _costal region bone_.

1. In row _[632](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=632:632)_, no term id was found for the name/label _head of eighth rib_.

1. In row _[633](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=633:633)_, no term id was found for the name/label _costal region bone_.

1. In row _[633](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=633:633)_, no term id was found for the name/label _inferior articular facet of eighth rib_.

1. In row _[634](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=634:634)_, no term id was found for the name/label _costal region bone_.

1. In row _[634](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=634:634)_, no term id was found for the name/label _neck of eighth rib_.

1. In row _[635](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=635:635)_, no term id was found for the name/label _costal region bone_.

1. In row _[635](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=635:635)_, no term id was found for the name/label _non-articular facet of tubercle of eighth rib_.

1. In row _[636](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=636:636)_, no term id was found for the name/label _costal region bone_.

1. In row _[636](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=636:636)_, no term id was found for the name/label _sternal end of eighth rib_.

1. In row _[637](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=637:637)_, no term id was found for the name/label _costal region bone_.

1. In row _[637](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=637:637)_, no term id was found for the name/label _superior articular facet of eighth rib_.

1. In row _[638](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=638:638)_, no term id was found for the name/label _costal region bone_.

1. In row _[638](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=638:638)_, no term id was found for the name/label _tubercle of eighth rib_.

1. In row _[639](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=639:639)_, no term id was found for the name/label _costal region bone_.

1. In row _[640](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=640:640)_, no term id was found for the name/label _costal region bone_.

1. In row _[640](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=640:640)_, no term id was found for the name/label _angle of ninth rib_.

1. In row _[641](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=641:641)_, no term id was found for the name/label _costal region bone_.

1. In row _[641](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=641:641)_, no term id was found for the name/label _articular facet of tubercle of ninth rib_.

1. In row _[642](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=642:642)_, no term id was found for the name/label _costal region bone_.

1. In row _[642](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=642:642)_, no term id was found for the name/label _body of ninth rib_.

1. In row _[643](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=643:643)_, no term id was found for the name/label _costal region bone_.

1. In row _[643](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=643:643)_, no term id was found for the name/label _costal groove of ninth rib_.

1. In row _[644](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=644:644)_, no term id was found for the name/label _costal region bone_.

1. In row _[644](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=644:644)_, no term id was found for the name/label _crest of head of ninth rib_.

1. In row _[645](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=645:645)_, no term id was found for the name/label _costal region bone_.

1. In row _[645](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=645:645)_, no term id was found for the name/label _head of ninth rib_.

1. In row _[646](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=646:646)_, no term id was found for the name/label _costal region bone_.

1. In row _[646](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=646:646)_, no term id was found for the name/label _inferior articular facet of ninth rib_.

1. In row _[647](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=647:647)_, no term id was found for the name/label _costal region bone_.

1. In row _[647](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=647:647)_, no term id was found for the name/label _neck of ninth rib_.

1. In row _[648](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=648:648)_, no term id was found for the name/label _costal region bone_.

1. In row _[648](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=648:648)_, no term id was found for the name/label _non-articular facet of tubercle of ninth rib_.

1. In row _[649](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=649:649)_, no term id was found for the name/label _costal region bone_.

1. In row _[649](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=649:649)_, no term id was found for the name/label _sternal end of ninth rib_.

1. In row _[650](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=650:650)_, no term id was found for the name/label _costal region bone_.

1. In row _[650](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=650:650)_, no term id was found for the name/label _superior articular facet of ninth rib_.

1. In row _[651](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=651:651)_, no term id was found for the name/label _costal region bone_.

1. In row _[651](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=651:651)_, no term id was found for the name/label _tubercle of ninth rib_.

1. In row _[652](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=652:652)_, no term id was found for the name/label _sternal region bone_.

1. In row _[653](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=653:653)_, no term id was found for the name/label _sternal region bone_.

1. In row _[654](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=654:654)_, no term id was found for the name/label _sternal region bone_.

1. In row _[654](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=654:654)_, no term id was found for the name/label _clavicular notch of sternum_.

1. In row _[655](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=655:655)_, no term id was found for the name/label _sternal region bone_.

1. In row _[655](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=655:655)_, no term id was found for the name/label _costal notches of sternum_.

1. In row _[656](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=656:656)_, no term id was found for the name/label _sternal region bone_.

1. In row _[656](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=656:656)_, no term id was found for the name/label _jugular notch of sternum_.

1. In row _[657](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=657:657)_, no term id was found for the name/label _sternal region bone_.

1. In row _[658](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=658:658)_, no term id was found for the name/label _sternal region bone_.

1. In row _[658](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=658:658)_, no term id was found for the name/label _sternal angle of sternum_.

1. In row _[659](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=659:659)_, no term id was found for the name/label _sternal region bone_.

1. In row _[659](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=659:659)_, no term id was found for the name/label _sternal body of sternum_.

1. In row _[660](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=660:660)_, no term id was found for the name/label _sternal region bone_.

1. In row _[660](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=660:660)_, no term id was found for the name/label _transverse ridges of sternum_.

1. In row _[661](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=661:661)_, no term id was found for the name/label _sternal region bone_.

1. In row _[661](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=661:661)_, no term id was found for the name/label _xiphoid process of sternum_.

1. In row _[665](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=665:665)_, no term id was found for the name/label _coccygeal cornu of coccyx_.

1. In row _[666](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=666:666)_, no term id was found for the name/label _transverse process of coccyx_.

1. In row _[669](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=669:669)_, no term id was found for the name/label _anterior arch of first cervical vertebra_.

1. In row _[670](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=670:670)_, no term id was found for the name/label _anterior tubercle of first cervical vertebra_.

1. In row _[671](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=671:671)_, no term id was found for the name/label _groove for vertebral artery of first cervical vertebra_.

1. In row _[672](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=672:672)_, no term id was found for the name/label _inferior articular facet of first cervical vertebra_.

1. In row _[673](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=673:673)_, no term id was found for the name/label _inferior articular process of first cervical vertebra_.

1. In row _[674](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=674:674)_, no term id was found for the name/label _inferior vertebral notch of first cervical vertebra_.

1. In row _[675](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=675:675)_, no term id was found for the name/label _lamina of first cervical vertebra_.

1. In row _[676](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=676:676)_, no term id was found for the name/label _pedicle of first cervical vertebra_.

1. In row _[677](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=677:677)_, no term id was found for the name/label _posterior arch of first cervical vertebra_.

1. In row _[678](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=678:678)_, no term id was found for the name/label _posterior tubercle of first cervical vertebra_.

1. In row _[679](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=679:679)_, no term id was found for the name/label _spinous process of first cervical vertebra_.

1. In row _[680](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=680:680)_, no term id was found for the name/label _superior articular facet of first cervical vertebra_.

1. In row _[681](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=681:681)_, no term id was found for the name/label _superior articular process of first cervical vertebra_.

1. In row _[682](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=682:682)_, no term id was found for the name/label _superior vertebral notch of first cervical vertebra_.

1. In row _[683](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=683:683)_, no term id was found for the name/label _transverse foramen of first cervical vertebra_.

1. In row _[684](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=684:684)_, no term id was found for the name/label _transverse process of first cervical vertebra_.

1. In row _[685](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=685:685)_, no term id was found for the name/label _vertebral body of first cervical vertebra_.

1. In row _[686](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=686:686)_, no term id was found for the name/label _vertebral foramen of first cervical vertebra_.

1. In row _[688](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=688:688)_, no term id was found for the name/label _body of second cervical vertebra_.

1. In row _[689](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=689:689)_, no term id was found for the name/label _inferior articular facet of second cervical vertebra_.

1. In row _[690](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=690:690)_, no term id was found for the name/label _inferior articular process of second cervical vertebra_.

1. In row _[691](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=691:691)_, no term id was found for the name/label _inferior vertebral notch of second cervical vertebra_.

1. In row _[692](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=692:692)_, no term id was found for the name/label _lamina of second cervical vertebra_.

1. In row _[694](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=694:694)_, no term id was found for the name/label _pedicle of second cervical vertebra_.

1. In row _[695](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=695:695)_, no term id was found for the name/label _spinous process of second cervical vertebra_.

1. In row _[696](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=696:696)_, no term id was found for the name/label _superior articular facet of second cervical vertebra_.

1. In row _[697](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=697:697)_, no term id was found for the name/label _superior articular process of second cervical vertebra_.

1. In row _[698](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=698:698)_, no term id was found for the name/label _superior vertebral notch of second cervical vertebra_.

1. In row _[699](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=699:699)_, no term id was found for the name/label _transverse foramen of second cervical vertebra_.

1. In row _[700](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=700:700)_, no term id was found for the name/label _transverse process of second cervical vertebra_.

1. In row _[701](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=701:701)_, no term id was found for the name/label _vertebral arch of second cervical vertebra_.

1. In row _[702](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=702:702)_, no term id was found for the name/label _vertebral body of second cervical vertebra_.

1. In row _[703](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=703:703)_, no term id was found for the name/label _vertebral foramen of second cervical vertebra_.

1. In row _[705](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=705:705)_, no term id was found for the name/label _inferior articular facet of third cervical vertebra_.

1. In row _[706](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=706:706)_, no term id was found for the name/label _inferior articular process of third cervical vertebra_.

1. In row _[707](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=707:707)_, no term id was found for the name/label _inferior vertebral notch of third cervical vertebra_.

1. In row _[708](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=708:708)_, no term id was found for the name/label _lamina of third cervical vertebra_.

1. In row _[709](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=709:709)_, no term id was found for the name/label _pedicle of third cervical vertebra_.

1. In row _[710](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=710:710)_, no term id was found for the name/label _spinous process of third cervical vertebra_.

1. In row _[711](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=711:711)_, no term id was found for the name/label _superior articular facet of third cervical vertebra_.

1. In row _[712](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=712:712)_, no term id was found for the name/label _superior articular process of third cervical vertebra_.

1. In row _[713](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=713:713)_, no term id was found for the name/label _superior vertebral notch of third cervical vertebra_.

1. In row _[714](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=714:714)_, no term id was found for the name/label _transverse foramen of third cervical vertebra_.

1. In row _[715](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=715:715)_, no term id was found for the name/label _transverse process of third cervical vertebra_.

1. In row _[716](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=716:716)_, no term id was found for the name/label _vertebral arch of third cervical vertebra_.

1. In row _[717](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=717:717)_, no term id was found for the name/label _vertebral body of third cervical vertebra_.

1. In row _[718](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=718:718)_, no term id was found for the name/label _vertebral foramen of third cervical vertebra_.

1. In row _[720](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=720:720)_, no term id was found for the name/label _inferior articular facet of fourth cervical vertebra_.

1. In row _[721](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=721:721)_, no term id was found for the name/label _inferior articular process of fourth cervical vertebra_.

1. In row _[722](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=722:722)_, no term id was found for the name/label _inferior vertebral notch of fourth cervical vertebra_.

1. In row _[723](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=723:723)_, no term id was found for the name/label _lamina of fourth cervical vertebra_.

1. In row _[724](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=724:724)_, no term id was found for the name/label _pedicle of fourth cervical vertebra_.

1. In row _[725](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=725:725)_, no term id was found for the name/label _spinous process of fourth cervical vertebra_.

1. In row _[726](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=726:726)_, no term id was found for the name/label _superior articular facet of fourth cervical vertebra_.

1. In row _[727](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=727:727)_, no term id was found for the name/label _superior articular process of fourth cervical vertebra_.

1. In row _[728](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=728:728)_, no term id was found for the name/label _superior vertebral notch of fourth cervical vertebra_.

1. In row _[729](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=729:729)_, no term id was found for the name/label _transverse foramen of fourth cervical vertebra_.

1. In row _[730](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=730:730)_, no term id was found for the name/label _transverse process of fourth cervical vertebra_.

1. In row _[731](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=731:731)_, no term id was found for the name/label _vertebral arch of fourth cervical vertebra_.

1. In row _[732](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=732:732)_, no term id was found for the name/label _vertebral body of fourth cervical vertebra_.

1. In row _[733](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=733:733)_, no term id was found for the name/label _vertebral foramen of fourth cervical vertebra_.

1. In row _[735](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=735:735)_, no term id was found for the name/label _inferior articular facet of fifth cervical vertebra_.

1. In row _[736](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=736:736)_, no term id was found for the name/label _inferior articular process of fifth cervical vertebra_.

1. In row _[737](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=737:737)_, no term id was found for the name/label _inferior vertebral notch of fifth cervical vertebra_.

1. In row _[738](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=738:738)_, no term id was found for the name/label _lamina of fifth cervical vertebra_.

1. In row _[739](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=739:739)_, no term id was found for the name/label _pedicle of fifth cervical vertebra_.

1. In row _[740](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=740:740)_, no term id was found for the name/label _spinous process of fifth cervical vertebra_.

1. In row _[741](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=741:741)_, no term id was found for the name/label _superior articular facet of fifth cervical vertebra_.

1. In row _[742](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=742:742)_, no term id was found for the name/label _superior articular process of fifth cervical vertebra_.

1. In row _[743](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=743:743)_, no term id was found for the name/label _superior vertebral notch of fifth cervical vertebra_.

1. In row _[744](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=744:744)_, no term id was found for the name/label _transverse foramen of fifth cervical vertebra_.

1. In row _[745](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=745:745)_, no term id was found for the name/label _transverse process of fifth cervical vertebra_.

1. In row _[746](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=746:746)_, no term id was found for the name/label _vertebral arch of fifth cervical vertebra_.

1. In row _[747](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=747:747)_, no term id was found for the name/label _vertebral body of fifth cervical vertebra_.

1. In row _[748](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=748:748)_, no term id was found for the name/label _vertebral foramen of fifth cervical vertebra_.

1. In row _[750](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=750:750)_, no term id was found for the name/label _inferior articular facet of sixth cervical vertebra_.

1. In row _[751](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=751:751)_, no term id was found for the name/label _inferior articular process of sixth cervical vertebra_.

1. In row _[752](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=752:752)_, no term id was found for the name/label _inferior vertebral notch of sixth cervical vertebra_.

1. In row _[753](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=753:753)_, no term id was found for the name/label _lamina of sixth cervical vertebra_.

1. In row _[754](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=754:754)_, no term id was found for the name/label _pedicle of sixth cervical vertebra_.

1. In row _[755](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=755:755)_, no term id was found for the name/label _spinous process of sixth cervical vertebra_.

1. In row _[756](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=756:756)_, no term id was found for the name/label _superior articular facet of sixth cervical vertebra_.

1. In row _[757](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=757:757)_, no term id was found for the name/label _superior articular process of sixth cervical vertebra_.

1. In row _[758](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=758:758)_, no term id was found for the name/label _superior vertebral notch of sixth cervical vertebra_.

1. In row _[759](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=759:759)_, no term id was found for the name/label _transverse foramen of sixth cervical vertebra_.

1. In row _[760](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=760:760)_, no term id was found for the name/label _transverse process of sixth cervical vertebra_.

1. In row _[761](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=761:761)_, no term id was found for the name/label _vertebral arch of sixth cervical vertebra_.

1. In row _[762](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=762:762)_, no term id was found for the name/label _vertebral body of sixth cervical vertebra_.

1. In row _[763](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=763:763)_, no term id was found for the name/label _vertebral foramen of sixth cervical vertebra_.

1. In row _[765](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=765:765)_, no term id was found for the name/label _inferior articular facet of seventh cervical vertebra_.

1. In row _[766](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=766:766)_, no term id was found for the name/label _inferior articular process of seventh cervical vertebra_.

1. In row _[767](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=767:767)_, no term id was found for the name/label _inferior vertebral notch of seventh cervical vertebra_.

1. In row _[768](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=768:768)_, no term id was found for the name/label _lamina of seventh cervical vertebra_.

1. In row _[769](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=769:769)_, no term id was found for the name/label _pedicle of seventh cervical vertebra_.

1. In row _[770](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=770:770)_, no term id was found for the name/label _spinous process of seventh cervical vertebra_.

1. In row _[771](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=771:771)_, no term id was found for the name/label _superior articular facet of seventh cervical vertebra_.

1. In row _[772](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=772:772)_, no term id was found for the name/label _superior articular process of seventh cervical vertebra_.

1. In row _[773](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=773:773)_, no term id was found for the name/label _superior vertebral notch of seventh cervical vertebra_.

1. In row _[774](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=774:774)_, no term id was found for the name/label _transverse foramen of seventh cervical vertebra_.

1. In row _[775](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=775:775)_, no term id was found for the name/label _transverse process of seventh cervical vertebra_.

1. In row _[776](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=776:776)_, no term id was found for the name/label _vertebra prominens of seventh cervical vertebra_.

1. In row _[777](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=777:777)_, no term id was found for the name/label _vertebral arch of seventh cervical vertebra_.

1. In row _[778](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=778:778)_, no term id was found for the name/label _vertebral body of seventh cervical vertebra_.

1. In row _[779](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=779:779)_, no term id was found for the name/label _vertebral foramen of seventh cervical vertebra_.

1. In row _[782](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=782:782)_, no term id was found for the name/label _accessory process of first lumbar vertebra_.

1. In row _[783](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=783:783)_, no term id was found for the name/label _inferior articular facet of first lumbar vertebra_.

1. In row _[784](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=784:784)_, no term id was found for the name/label _inferior articular process of first lumbar vertebra_.

1. In row _[785](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=785:785)_, no term id was found for the name/label _inferior vertebral notch of first lumbar vertebra_.

1. In row _[786](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=786:786)_, no term id was found for the name/label _lamina of first lumbar vertebra_.

1. In row _[787](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=787:787)_, no term id was found for the name/label _mammillary process of first lumbar vertebra_.

1. In row _[788](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=788:788)_, no term id was found for the name/label _pedicle of first lumbar vertebra_.

1. In row _[789](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=789:789)_, no term id was found for the name/label _spinous process of first lumbar vertebra_.

1. In row _[790](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=790:790)_, no term id was found for the name/label _superior articular facet of first lumbar vertebra_.

1. In row _[791](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=791:791)_, no term id was found for the name/label _superior articular process of first lumbar vertebra_.

1. In row _[792](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=792:792)_, no term id was found for the name/label _superior vertebral notch of first lumbar vertebra_.

1. In row _[793](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=793:793)_, no term id was found for the name/label _transverse process of first lumbar vertebra_.

1. In row _[794](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=794:794)_, no term id was found for the name/label _vertebral arch of first lumbar vertebra_.

1. In row _[795](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=795:795)_, no term id was found for the name/label _vertebral body of first lumbar vertebra_.

1. In row _[796](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=796:796)_, no term id was found for the name/label _vertebral foramen of first lumbar vertebra_.

1. In row _[798](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=798:798)_, no term id was found for the name/label _accessory process of second lumbar vertebra_.

1. In row _[799](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=799:799)_, no term id was found for the name/label _inferior articular facet of second lumbar vertebra_.

1. In row _[800](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=800:800)_, no term id was found for the name/label _inferior articular process of second lumbar vertebra_.

1. In row _[801](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=801:801)_, no term id was found for the name/label _inferior vertebral notch of second lumbar vertebra_.

1. In row _[802](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=802:802)_, no term id was found for the name/label _lamina of second lumbar vertebra_.

1. In row _[803](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=803:803)_, no term id was found for the name/label _mammillary process of second lumbar vertebra_.

1. In row _[804](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=804:804)_, no term id was found for the name/label _pedicle of second lumbar vertebra_.

1. In row _[805](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=805:805)_, no term id was found for the name/label _spinous process of second lumbar vertebra_.

1. In row _[806](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=806:806)_, no term id was found for the name/label _superior articular facet of second lumbar vertebra_.

1. In row _[807](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=807:807)_, no term id was found for the name/label _superior articular process of second lumbar vertebra_.

1. In row _[808](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=808:808)_, no term id was found for the name/label _superior vertebral notch of second lumbar vertebra_.

1. In row _[809](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=809:809)_, no term id was found for the name/label _transverse process of second lumbar vertebra_.

1. In row _[810](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=810:810)_, no term id was found for the name/label _vertebral arch of second lumbar vertebra_.

1. In row _[811](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=811:811)_, no term id was found for the name/label _vertebral body of second lumbar vertebra_.

1. In row _[812](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=812:812)_, no term id was found for the name/label _vertebral foramen of second lumbar vertebra_.

1. In row _[814](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=814:814)_, no term id was found for the name/label _accessory process of third lumbar vertebra_.

1. In row _[815](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=815:815)_, no term id was found for the name/label _inferior articular facet of third lumbar vertebra_.

1. In row _[816](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=816:816)_, no term id was found for the name/label _inferior articular process of third lumbar vertebra_.

1. In row _[817](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=817:817)_, no term id was found for the name/label _inferior vertebral notch of third lumbar vertebra_.

1. In row _[818](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=818:818)_, no term id was found for the name/label _lamina of third lumbar vertebra_.

1. In row _[819](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=819:819)_, no term id was found for the name/label _mammillary process of third lumbar vertebra_.

1. In row _[820](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=820:820)_, no term id was found for the name/label _pedicle of third lumbar vertebra_.

1. In row _[821](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=821:821)_, no term id was found for the name/label _spinous process of third lumbar vertebra_.

1. In row _[822](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=822:822)_, no term id was found for the name/label _superior articular facet of third lumbar vertebra_.

1. In row _[823](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=823:823)_, no term id was found for the name/label _superior articular process of third lumbar vertebra_.

1. In row _[824](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=824:824)_, no term id was found for the name/label _superior vertebral notch of third lumbar vertebra_.

1. In row _[825](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=825:825)_, no term id was found for the name/label _transverse process of third lumbar vertebra_.

1. In row _[826](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=826:826)_, no term id was found for the name/label _vertebral arch of third lumbar vertebra_.

1. In row _[827](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=827:827)_, no term id was found for the name/label _vertebral body of third lumbar vertebra_.

1. In row _[828](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=828:828)_, no term id was found for the name/label _vertebral foramen of third lumbar vertebra_.

1. In row _[830](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=830:830)_, no term id was found for the name/label _accessory process of fourth lumbar vertebra_.

1. In row _[831](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=831:831)_, no term id was found for the name/label _inferior articular facet of fourth lumbar vertebra_.

1. In row _[832](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=832:832)_, no term id was found for the name/label _inferior articular process of fourth lumbar vertebra_.

1. In row _[833](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=833:833)_, no term id was found for the name/label _inferior vertebral notch of fourth lumbar vertebra_.

1. In row _[834](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=834:834)_, no term id was found for the name/label _lamina of fourth lumbar vertebra_.

1. In row _[835](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=835:835)_, no term id was found for the name/label _mammillary process of fourth lumbar vertebra_.

1. In row _[836](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=836:836)_, no term id was found for the name/label _pedicle of fourth lumbar vertebra_.

1. In row _[837](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=837:837)_, no term id was found for the name/label _spinous process of fourth lumbar vertebra_.

1. In row _[838](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=838:838)_, no term id was found for the name/label _superior articular facet of fourth lumbar vertebra_.

1. In row _[839](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=839:839)_, no term id was found for the name/label _superior articular process of fourth lumbar vertebra_.

1. In row _[840](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=840:840)_, no term id was found for the name/label _superior vertebral notch of fourth lumbar vertebra_.

1. In row _[841](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=841:841)_, no term id was found for the name/label _transverse process of fourth lumbar vertebra_.

1. In row _[842](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=842:842)_, no term id was found for the name/label _vertebral arch of fourth lumbar vertebra_.

1. In row _[843](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=843:843)_, no term id was found for the name/label _vertebral body of fourth lumbar vertebra_.

1. In row _[844](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=844:844)_, no term id was found for the name/label _vertebral foramen of fourth lumbar vertebra_.

1. In row _[846](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=846:846)_, no term id was found for the name/label _accessory process of fifth lumbar vertebra_.

1. In row _[847](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=847:847)_, no term id was found for the name/label _inferior articular facet of fifth lumbar vertebra_.

1. In row _[848](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=848:848)_, no term id was found for the name/label _inferior articular process of fifth lumbar vertebra_.

1. In row _[849](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=849:849)_, no term id was found for the name/label _inferior vertebral notch of fifth lumbar vertebra_.

1. In row _[850](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=850:850)_, no term id was found for the name/label _lamina of fifth lumbar vertebra_.

1. In row _[851](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=851:851)_, no term id was found for the name/label _mammillary process of fifth lumbar vertebra_.

1. In row _[852](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=852:852)_, no term id was found for the name/label _pedicle of fifth lumbar vertebra_.

1. In row _[853](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=853:853)_, no term id was found for the name/label _spinous process of fifth lumbar vertebra_.

1. In row _[854](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=854:854)_, no term id was found for the name/label _superior articular facet of fifth lumbar vertebra_.

1. In row _[855](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=855:855)_, no term id was found for the name/label _superior articular process of fifth lumbar vertebra_.

1. In row _[856](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=856:856)_, no term id was found for the name/label _superior vertebral notch of fifth lumbar vertebra_.

1. In row _[857](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=857:857)_, no term id was found for the name/label _transverse process of fifth lumbar vertebra_.

1. In row _[858](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=858:858)_, no term id was found for the name/label _vertebral arch of fifth lumbar vertebra_.

1. In row _[859](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=859:859)_, no term id was found for the name/label _vertebral body of fifth lumbar vertebra_.

1. In row _[860](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=860:860)_, no term id was found for the name/label _vertebral foramen of fifth lumbar vertebra_.

1. In row _[863](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=863:863)_, no term id was found for the name/label _alae of sacrum_.

1. In row _[864](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=864:864)_, no term id was found for the name/label _anterior sacral foramina of sacrum_.

1. In row _[865](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=865:865)_, no term id was found for the name/label _auricular surface of sacrum_.

1. In row _[866](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=866:866)_, no term id was found for the name/label _intermediate sacral crest of sacrum_.

1. In row _[867](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=867:867)_, no term id was found for the name/label _lateral sacral crest of sacrum_.

1. In row _[868](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=868:868)_, no term id was found for the name/label _linea terminalis of sacrum_.

1. In row _[869](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=869:869)_, no term id was found for the name/label _median sacral crest of sacrum_.

1. In row _[870](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=870:870)_, no term id was found for the name/label _posterior sacral foramina of sacrum_.

1. In row _[871](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=871:871)_, no term id was found for the name/label _sacral apex of sacrum_.

1. In row _[872](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=872:872)_, no term id was found for the name/label _sacral canal of sacrum_.

1. In row _[873](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=873:873)_, no term id was found for the name/label _sacral cornu of sacrum_.

1. In row _[874](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=874:874)_, no term id was found for the name/label _sacral hiatus of sacrum_.

1. In row _[875](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=875:875)_, no term id was found for the name/label _sacral promontory of sacrum_.

1. In row _[876](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=876:876)_, no term id was found for the name/label _sacral spine of sacrum_.

1. In row _[877](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=877:877)_, no term id was found for the name/label _sacral tuberosity of sacrum_.

1. In row _[878](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=878:878)_, no term id was found for the name/label _superior articular facet of sacrum_.

1. In row _[879](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=879:879)_, no term id was found for the name/label _superior articular process of sacrum_.

1. In row _[880](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=880:880)_, no term id was found for the name/label _transverse ridges of sacrum_.

1. In row _[883](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=883:883)_, no term id was found for the name/label _inferior articular facet of first thoracic vertebra_.

1. In row _[884](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=884:884)_, no term id was found for the name/label _inferior articular process of first thoracic vertebra_.

1. In row _[885](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=885:885)_, no term id was found for the name/label _inferior costal facet of first thoracic vertebra_.

1. In row _[886](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=886:886)_, no term id was found for the name/label _inferior vertebral notch of first thoracic vertebra_.

1. In row _[887](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=887:887)_, no term id was found for the name/label _lamina of first thoracic vertebra_.

1. In row _[888](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=888:888)_, no term id was found for the name/label _pedicle of first thoracic vertebra_.

1. In row _[889](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=889:889)_, no term id was found for the name/label _spinous process of first thoracic vertebra_.

1. In row _[890](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=890:890)_, no term id was found for the name/label _superior articular facet of first thoracic vertebra_.

1. In row _[891](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=891:891)_, no term id was found for the name/label _superior articular process of first thoracic vertebra_.

1. In row _[892](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=892:892)_, no term id was found for the name/label _superior costal facet of first thoracic vertebra_.

1. In row _[893](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=893:893)_, no term id was found for the name/label _superior vertebral notch of first thoracic vertebra_.

1. In row _[894](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=894:894)_, no term id was found for the name/label _transverse costal facet of first thoracic vertebra_.

1. In row _[895](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=895:895)_, no term id was found for the name/label _transverse process of first thoracic vertebra_.

1. In row _[896](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=896:896)_, no term id was found for the name/label _vertebral arch of first thoracic vertebra_.

1. In row _[897](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=897:897)_, no term id was found for the name/label _vertebral body of first thoracic vertebra_.

1. In row _[898](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=898:898)_, no term id was found for the name/label _vertebral foramen of first thoracic vertebra_.

1. In row _[900](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=900:900)_, no term id was found for the name/label _inferior articular facet of tenth thoracic vertebra_.

1. In row _[901](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=901:901)_, no term id was found for the name/label _inferior articular process of tenth thoracic vertebra_.

1. In row _[902](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=902:902)_, no term id was found for the name/label _inferior costal facet of tenth thoracic vertebra_.

1. In row _[903](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=903:903)_, no term id was found for the name/label _inferior vertebral notch of tenth thoracic vertebra_.

1. In row _[904](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=904:904)_, no term id was found for the name/label _lamina of tenth thoracic vertebra_.

1. In row _[905](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=905:905)_, no term id was found for the name/label _pedicle of tenth thoracic vertebra_.

1. In row _[906](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=906:906)_, no term id was found for the name/label _spinous process of tenth thoracic vertebra_.

1. In row _[907](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=907:907)_, no term id was found for the name/label _superior articular facet of tenth thoracic vertebra_.

1. In row _[908](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=908:908)_, no term id was found for the name/label _superior articular process of tenth thoracic vertebra_.

1. In row _[909](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=909:909)_, no term id was found for the name/label _superior costal facet of tenth thoracic vertebra_.

1. In row _[910](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=910:910)_, no term id was found for the name/label _superior vertebral notch of tenth thoracic vertebra_.

1. In row _[911](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=911:911)_, no term id was found for the name/label _transverse costal facet of tenth thoracic vertebra_.

1. In row _[912](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=912:912)_, no term id was found for the name/label _transverse process of tenth thoracic vertebra_.

1. In row _[913](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=913:913)_, no term id was found for the name/label _vertebral arch of tenth thoracic vertebra_.

1. In row _[914](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=914:914)_, no term id was found for the name/label _vertebral body of tenth thoracic vertebra_.

1. In row _[915](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=915:915)_, no term id was found for the name/label _vertebral foramen of tenth thoracic vertebra_.

1. In row _[917](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=917:917)_, no term id was found for the name/label _inferior articular facet of eleventh thoracic vertebra_.

1. In row _[918](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=918:918)_, no term id was found for the name/label _inferior articular process of eleventh thoracic vertebra_.

1. In row _[919](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=919:919)_, no term id was found for the name/label _inferior costal facet of eleventh thoracic vertebra_.

1. In row _[920](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=920:920)_, no term id was found for the name/label _inferior vertebral notch of eleventh thoracic vertebra_.

1. In row _[921](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=921:921)_, no term id was found for the name/label _lamina of eleventh thoracic vertebra_.

1. In row _[922](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=922:922)_, no term id was found for the name/label _pedicle of eleventh thoracic vertebra_.

1. In row _[923](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=923:923)_, no term id was found for the name/label _spinous process of eleventh thoracic vertebra_.

1. In row _[924](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=924:924)_, no term id was found for the name/label _superior articular facet of eleventh thoracic vertebra_.

1. In row _[925](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=925:925)_, no term id was found for the name/label _superior articular process of eleventh thoracic vertebra_.

1. In row _[926](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=926:926)_, no term id was found for the name/label _superior costal facet of eleventh thoracic vertebra_.

1. In row _[927](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=927:927)_, no term id was found for the name/label _superior vertebral notch of eleventh thoracic vertebra_.

1. In row _[928](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=928:928)_, no term id was found for the name/label _transverse costal facet of eleventh thoracic vertebra_.

1. In row _[929](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=929:929)_, no term id was found for the name/label _transverse process of eleventh thoracic vertebra_.

1. In row _[930](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=930:930)_, no term id was found for the name/label _vertebral arch of eleventh thoracic vertebra_.

1. In row _[931](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=931:931)_, no term id was found for the name/label _vertebral body of eleventh thoracic vertebra_.

1. In row _[932](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=932:932)_, no term id was found for the name/label _vertebral foramen of eleventh thoracic vertebra_.

1. In row _[934](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=934:934)_, no term id was found for the name/label _costal facet of twelfth thoracic vertebra_.

1. In row _[935](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=935:935)_, no term id was found for the name/label _inferior articular facet of twelfth thoracic vertebra_.

1. In row _[936](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=936:936)_, no term id was found for the name/label _inferior articular process of twelfth thoracic vertebra_.

1. In row _[937](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=937:937)_, no term id was found for the name/label _inferior vertebral notch of twelfth thoracic vertebra_.

1. In row _[938](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=938:938)_, no term id was found for the name/label _lamina of twelfth thoracic vertebra_.

1. In row _[939](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=939:939)_, no term id was found for the name/label _pedicle of twelfth thoracic vertebra_.

1. In row _[940](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=940:940)_, no term id was found for the name/label _spinous process of twelfth thoracic vertebra_.

1. In row _[941](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=941:941)_, no term id was found for the name/label _superior articular facet of twelfth thoracic vertebra_.

1. In row _[942](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=942:942)_, no term id was found for the name/label _superior articular process of twelfth thoracic vertebra_.

1. In row _[943](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=943:943)_, no term id was found for the name/label _superior vertebral notch of twelfth thoracic vertebra_.

1. In row _[944](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=944:944)_, no term id was found for the name/label _transverse process of twelfth thoracic vertebra_.

1. In row _[945](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=945:945)_, no term id was found for the name/label _vertebral arch of twelfth thoracic vertebra_.

1. In row _[946](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=946:946)_, no term id was found for the name/label _vertebral body of twelfth thoracic vertebra_.

1. In row _[947](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=947:947)_, no term id was found for the name/label _vertebral foramen of twelfth thoracic vertebra_.

1. In row _[949](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=949:949)_, no term id was found for the name/label _inferior articular facet of second thoracic vertebra_.

1. In row _[950](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=950:950)_, no term id was found for the name/label _inferior articular process of second thoracic vertebra_.

1. In row _[951](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=951:951)_, no term id was found for the name/label _inferior costal facet of second thoracic vertebra_.

1. In row _[952](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=952:952)_, no term id was found for the name/label _inferior vertebral notch of second thoracic vertebra_.

1. In row _[953](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=953:953)_, no term id was found for the name/label _lamina of second thoracic vertebra_.

1. In row _[954](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=954:954)_, no term id was found for the name/label _pedicle of second thoracic vertebra_.

1. In row _[955](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=955:955)_, no term id was found for the name/label _spinous process of second thoracic vertebra_.

1. In row _[956](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=956:956)_, no term id was found for the name/label _superior articular facet of second thoracic vertebra_.

1. In row _[957](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=957:957)_, no term id was found for the name/label _superior articular process of second thoracic vertebra_.

1. In row _[958](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=958:958)_, no term id was found for the name/label _superior costal facet of second thoracic vertebra_.

1. In row _[959](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=959:959)_, no term id was found for the name/label _superior vertebral notch of second thoracic vertebra_.

1. In row _[960](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=960:960)_, no term id was found for the name/label _transverse costal facet of second thoracic vertebra_.

1. In row _[961](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=961:961)_, no term id was found for the name/label _transverse process of second thoracic vertebra_.

1. In row _[962](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=962:962)_, no term id was found for the name/label _vertebral arch of second thoracic vertebra_.

1. In row _[963](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=963:963)_, no term id was found for the name/label _vertebral body of second thoracic vertebra_.

1. In row _[964](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=964:964)_, no term id was found for the name/label _vertebral foramen of second thoracic vertebra_.

1. In row _[966](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=966:966)_, no term id was found for the name/label _inferior articular facet of third thoracic vertebra_.

1. In row _[967](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=967:967)_, no term id was found for the name/label _inferior articular process of third thoracic vertebra_.

1. In row _[968](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=968:968)_, no term id was found for the name/label _inferior costal facet of third thoracic vertebra_.

1. In row _[969](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=969:969)_, no term id was found for the name/label _inferior vertebral notch of third thoracic vertebra_.

1. In row _[970](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=970:970)_, no term id was found for the name/label _lamina of third thoracic vertebra_.

1. In row _[971](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=971:971)_, no term id was found for the name/label _pedicle of third thoracic vertebra_.

1. In row _[972](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=972:972)_, no term id was found for the name/label _spinous process of third thoracic vertebra_.

1. In row _[973](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=973:973)_, no term id was found for the name/label _superior articular facet of third thoracic vertebra_.

1. In row _[974](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=974:974)_, no term id was found for the name/label _superior articular process of third thoracic vertebra_.

1. In row _[975](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=975:975)_, no term id was found for the name/label _superior costal facet of third thoracic vertebra_.

1. In row _[976](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=976:976)_, no term id was found for the name/label _superior vertebral notch of third thoracic vertebra_.

1. In row _[977](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=977:977)_, no term id was found for the name/label _transverse costal facet of third thoracic vertebra_.

1. In row _[978](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=978:978)_, no term id was found for the name/label _transverse process of third thoracic vertebra_.

1. In row _[979](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=979:979)_, no term id was found for the name/label _vertebral arch of third thoracic vertebra_.

1. In row _[980](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=980:980)_, no term id was found for the name/label _vertebral body of third thoracic vertebra_.

1. In row _[981](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=981:981)_, no term id was found for the name/label _vertebral foramen of third thoracic vertebra_.

1. In row _[983](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=983:983)_, no term id was found for the name/label _inferior articular facet of fourth thoracic vertebra_.

1. In row _[984](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=984:984)_, no term id was found for the name/label _inferior articular process of fourth thoracic vertebra_.

1. In row _[985](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=985:985)_, no term id was found for the name/label _inferior costal facet of fourth thoracic vertebra_.

1. In row _[986](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=986:986)_, no term id was found for the name/label _inferior vertebral notch of fourth thoracic vertebra_.

1. In row _[987](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=987:987)_, no term id was found for the name/label _lamina of fourth thoracic vertebra_.

1. In row _[988](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=988:988)_, no term id was found for the name/label _pedicle of fourth thoracic vertebra_.

1. In row _[989](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=989:989)_, no term id was found for the name/label _spinous process of fourth thoracic vertebra_.

1. In row _[990](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=990:990)_, no term id was found for the name/label _superior articular facet of fourth thoracic vertebra_.

1. In row _[991](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=991:991)_, no term id was found for the name/label _superior articular process of fourth thoracic vertebra_.

1. In row _[992](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=992:992)_, no term id was found for the name/label _superior costal facet of fourth thoracic vertebra_.

1. In row _[993](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=993:993)_, no term id was found for the name/label _superior vertebral notch of fourth thoracic vertebra_.

1. In row _[994](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=994:994)_, no term id was found for the name/label _transverse costal facet of fourth thoracic vertebra_.

1. In row _[995](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=995:995)_, no term id was found for the name/label _transverse process of fourth thoracic vertebra_.

1. In row _[996](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=996:996)_, no term id was found for the name/label _vertebral arch of fourth thoracic vertebra_.

1. In row _[997](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=997:997)_, no term id was found for the name/label _vertebral body of fourth thoracic vertebra_.

1. In row _[998](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=998:998)_, no term id was found for the name/label _vertebral foramen of fourth thoracic vertebra_.

1. In row _[1000](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1000:1000)_, no term id was found for the name/label _inferior articular facet of fifth thoracic vertebra_.

1. In row _[1001](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1001:1001)_, no term id was found for the name/label _inferior articular process of fifth thoracic vertebra_.

1. In row _[1002](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1002:1002)_, no term id was found for the name/label _inferior costal facet of fifth thoracic vertebra_.

1. In row _[1003](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1003:1003)_, no term id was found for the name/label _inferior vertebral notch of fifth thoracic vertebra_.

1. In row _[1004](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1004:1004)_, no term id was found for the name/label _lamina of fifth thoracic vertebra_.

1. In row _[1005](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1005:1005)_, no term id was found for the name/label _pedicle of fifth thoracic vertebra_.

1. In row _[1006](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1006:1006)_, no term id was found for the name/label _spinous process of fifth thoracic vertebra_.

1. In row _[1007](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1007:1007)_, no term id was found for the name/label _superior articular facet of fifth thoracic vertebra_.

1. In row _[1008](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1008:1008)_, no term id was found for the name/label _superior articular process of fifth thoracic vertebra_.

1. In row _[1009](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1009:1009)_, no term id was found for the name/label _superior costal facet of fifth thoracic vertebra_.

1. In row _[1010](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1010:1010)_, no term id was found for the name/label _superior vertebral notch of fifth thoracic vertebra_.

1. In row _[1011](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1011:1011)_, no term id was found for the name/label _transverse costal facet of fifth thoracic vertebra_.

1. In row _[1012](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1012:1012)_, no term id was found for the name/label _transverse process of fifth thoracic vertebra_.

1. In row _[1013](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1013:1013)_, no term id was found for the name/label _vertebral arch of fifth thoracic vertebra_.

1. In row _[1014](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1014:1014)_, no term id was found for the name/label _vertebral body of fifth thoracic vertebra_.

1. In row _[1015](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1015:1015)_, no term id was found for the name/label _vertebral foramen of fifth thoracic vertebra_.

1. In row _[1017](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1017:1017)_, no term id was found for the name/label _inferior articular facet of sixth thoracic vertebra_.

1. In row _[1018](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1018:1018)_, no term id was found for the name/label _inferior articular process of sixth thoracic vertebra_.

1. In row _[1019](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1019:1019)_, no term id was found for the name/label _inferior costal facet of sixth thoracic vertebra_.

1. In row _[1020](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1020:1020)_, no term id was found for the name/label _inferior vertebral notch of sixth thoracic vertebra_.

1. In row _[1021](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1021:1021)_, no term id was found for the name/label _lamina of sixth thoracic vertebra_.

1. In row _[1022](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1022:1022)_, no term id was found for the name/label _pedicle of sixth thoracic vertebra_.

1. In row _[1023](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1023:1023)_, no term id was found for the name/label _spinous process of sixth thoracic vertebra_.

1. In row _[1024](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1024:1024)_, no term id was found for the name/label _superior articular facet of sixth thoracic vertebra_.

1. In row _[1025](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1025:1025)_, no term id was found for the name/label _superior articular process of sixth thoracic vertebra_.

1. In row _[1026](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1026:1026)_, no term id was found for the name/label _superior costal facet of sixth thoracic vertebra_.

1. In row _[1027](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1027:1027)_, no term id was found for the name/label _superior vertebral notch of sixth thoracic vertebra_.

1. In row _[1028](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1028:1028)_, no term id was found for the name/label _transverse costal facet of sixth thoracic vertebra_.

1. In row _[1029](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1029:1029)_, no term id was found for the name/label _transverse process of sixth thoracic vertebra_.

1. In row _[1030](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1030:1030)_, no term id was found for the name/label _vertebral arch of sixth thoracic vertebra_.

1. In row _[1031](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1031:1031)_, no term id was found for the name/label _vertebral body of sixth thoracic vertebra_.

1. In row _[1032](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1032:1032)_, no term id was found for the name/label _vertebral foramen of sixth thoracic vertebra_.

1. In row _[1034](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1034:1034)_, no term id was found for the name/label _inferior articular facet of seventh thoracic vertebra_.

1. In row _[1035](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1035:1035)_, no term id was found for the name/label _inferior articular process of seventh thoracic vertebra_.

1. In row _[1036](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1036:1036)_, no term id was found for the name/label _inferior costal facet of seventh thoracic vertebra_.

1. In row _[1037](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1037:1037)_, no term id was found for the name/label _inferior vertebral notch of seventh thoracic vertebra_.

1. In row _[1038](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1038:1038)_, no term id was found for the name/label _lamina of seventh thoracic vertebra_.

1. In row _[1039](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1039:1039)_, no term id was found for the name/label _pedicle of seventh thoracic vertebra_.

1. In row _[1040](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1040:1040)_, no term id was found for the name/label _spinous process of seventh thoracic vertebra_.

1. In row _[1041](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1041:1041)_, no term id was found for the name/label _superior articular facet of seventh thoracic vertebra_.

1. In row _[1042](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1042:1042)_, no term id was found for the name/label _superior articular process of seventh thoracic vertebra_.

1. In row _[1043](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1043:1043)_, no term id was found for the name/label _superior costal facet of seventh thoracic vertebra_.

1. In row _[1044](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1044:1044)_, no term id was found for the name/label _superior vertebral notch of seventh thoracic vertebra_.

1. In row _[1045](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1045:1045)_, no term id was found for the name/label _transverse costal facet of seventh thoracic vertebra_.

1. In row _[1046](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1046:1046)_, no term id was found for the name/label _transverse process of seventh thoracic vertebra_.

1. In row _[1047](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1047:1047)_, no term id was found for the name/label _vertebral arch of seventh thoracic vertebra_.

1. In row _[1048](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1048:1048)_, no term id was found for the name/label _vertebral body of seventh thoracic vertebra_.

1. In row _[1049](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1049:1049)_, no term id was found for the name/label _vertebral foramen of seventh thoracic vertebra_.

1. In row _[1051](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1051:1051)_, no term id was found for the name/label _inferior articular facet of eighth thoracic vertebra_.

1. In row _[1052](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1052:1052)_, no term id was found for the name/label _inferior articular process of eighth thoracic vertebra_.

1. In row _[1053](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1053:1053)_, no term id was found for the name/label _inferior costal facet of eighth thoracic vertebra_.

1. In row _[1054](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1054:1054)_, no term id was found for the name/label _inferior vertebral notch of eighth thoracic vertebra_.

1. In row _[1055](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1055:1055)_, no term id was found for the name/label _lamina of eighth thoracic vertebra_.

1. In row _[1056](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1056:1056)_, no term id was found for the name/label _pedicle of eighth thoracic vertebra_.

1. In row _[1057](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1057:1057)_, no term id was found for the name/label _spinous process of eighth thoracic vertebra_.

1. In row _[1058](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1058:1058)_, no term id was found for the name/label _superior articular facet of eighth thoracic vertebra_.

1. In row _[1059](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1059:1059)_, no term id was found for the name/label _superior articular process of eighth thoracic vertebra_.

1. In row _[1060](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1060:1060)_, no term id was found for the name/label _superior costal facet of eighth thoracic vertebra_.

1. In row _[1061](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1061:1061)_, no term id was found for the name/label _superior vertebral notch of eighth thoracic vertebra_.

1. In row _[1062](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1062:1062)_, no term id was found for the name/label _transverse costal facet of eighth thoracic vertebra_.

1. In row _[1063](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1063:1063)_, no term id was found for the name/label _transverse process of eighth thoracic vertebra_.

1. In row _[1064](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1064:1064)_, no term id was found for the name/label _vertebral arch of eighth thoracic vertebra_.

1. In row _[1065](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1065:1065)_, no term id was found for the name/label _vertebral body of eighth thoracic vertebra_.

1. In row _[1066](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1066:1066)_, no term id was found for the name/label _vertebral foramen of eighth thoracic vertebra_.

1. In row _[1068](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1068:1068)_, no term id was found for the name/label _inferior articular facet of ninth thoracic vertebra_.

1. In row _[1069](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1069:1069)_, no term id was found for the name/label _inferior articular process of ninth thoracic vertebra_.

1. In row _[1070](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1070:1070)_, no term id was found for the name/label _inferior costal facet of ninth thoracic vertebra_.

1. In row _[1071](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1071:1071)_, no term id was found for the name/label _inferior vertebral notch of ninth thoracic vertebra_.

1. In row _[1072](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1072:1072)_, no term id was found for the name/label _lamina of ninth thoracic vertebra_.

1. In row _[1073](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1073:1073)_, no term id was found for the name/label _pedicle of ninth thoracic vertebra_.

1. In row _[1074](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1074:1074)_, no term id was found for the name/label _spinous process of ninth thoracic vertebra_.

1. In row _[1075](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1075:1075)_, no term id was found for the name/label _superior articular facet of ninth thoracic vertebra_.

1. In row _[1076](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1076:1076)_, no term id was found for the name/label _superior articular process of ninth thoracic vertebra_.

1. In row _[1077](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1077:1077)_, no term id was found for the name/label _superior costal facet of ninth thoracic vertebra_.

1. In row _[1078](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1078:1078)_, no term id was found for the name/label _superior vertebral notch of ninth thoracic vertebra_.

1. In row _[1079](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1079:1079)_, no term id was found for the name/label _transverse costal facet of ninth thoracic vertebra_.

1. In row _[1080](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1080:1080)_, no term id was found for the name/label _transverse process of ninth thoracic vertebra_.

1. In row _[1081](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1081:1081)_, no term id was found for the name/label _vertebral arch of ninth thoracic vertebra_.

1. In row _[1082](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1082:1082)_, no term id was found for the name/label _vertebral body of ninth thoracic vertebra_.

1. In row _[1083](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1083:1083)_, no term id was found for the name/label _vertebral foramen of ninth thoracic vertebra_.


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



|      | row_number                                                                                                             | s              | slabel                       | user_slabel                  | o              | olabel                               | user_olabel       |   deltaIC |
|------|------------------------------------------------------------------------------------------------------------------------|----------------|------------------------------|------------------------------|----------------|--------------------------------------|-------------------|-----------|
|  964 | [126](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=126:126)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  965 | [140](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=140:140)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  966 | [134](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=134:134)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  967 | [145](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=145:145)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  968 | [143](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=143:143)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  969 | [132](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=132:132)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  970 | [142](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=142:142)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  971 | [122](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=122:122)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  972 | [141](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=141:141)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  973 | [144](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=144:144)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  974 | [146](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=146:146)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  975 | [133](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=133:133)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  976 | [139](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=139:139)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  977 | [130](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=130:130)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  978 | [124](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=124:124)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  979 | [121](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=121:121)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  980 | [138](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=138:138)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  981 | [123](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=123:123)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  982 | [137](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=137:137)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  983 | [129](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=129:129)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  984 | [127](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=127:127)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  985 | [136](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=136:136)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  986 | [128](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=128:128)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  987 | [135](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=135:135)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  988 | [131](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=131:131)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  989 | [113](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=113:113)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  990 | [120](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=120:120)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  991 | [83](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=83:83)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  992 | [89](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=89:89)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  993 | [60](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=60:60)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  994 | [88](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=88:88)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  995 | [59](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=59:59)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  996 | [87](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=87:87)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  997 | [86](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=86:86)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  998 | [58](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=58:58)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
|  999 | [85](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=85:85)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1000 | [66](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=66:66)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1001 | [57](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=57:57)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1002 | [56](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=56:56)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1003 | [84](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=84:84)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1004 | [55](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=55:55)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1005 | [75](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=75:75)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1006 | [74](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=74:74)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1007 | [119](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=119:119)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1008 | [82](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=82:82)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1009 | [73](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=73:73)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1010 | [81](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=81:81)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1011 | [72](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=72:72)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1012 | [67](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=67:67)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1013 | [71](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=71:71)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1014 | [80](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=80:80)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1015 | [70](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=70:70)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1016 | [79](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=79:79)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1017 | [78](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=78:78)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1018 | [77](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=77:77)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1019 | [69](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=69:69)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1020 | [68](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=68:68)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1021 | [76](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=76:76)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1022 | [61](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=61:61)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1023 | [90](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=90:90)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1024 | [91](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=91:91)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1025 | [92](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=92:92)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1026 | [118](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=118:118)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1027 | [117](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=117:117)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1028 | [63](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=63:63)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1029 | [116](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=116:116)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1030 | [115](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=115:115)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1031 | [64](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=64:64)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1032 | [114](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=114:114)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1033 | [112](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=112:112)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1034 | [111](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=111:111)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1035 | [110](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=110:110)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1036 | [109](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=109:109)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1037 | [65](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=65:65)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1038 | [108](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=108:108)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1039 | [107](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=107:107)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1040 | [106](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=106:106)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1041 | [105](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=105:105)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1042 | [104](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=104:104)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1043 | [103](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=103:103)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1044 | [102](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=102:102)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1045 | [101](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=101:101)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1046 | [100](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=100:100)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1047 | [99](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=99:99)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1048 | [98](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=98:98)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1049 | [62](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=62:62)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1050 | [97](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=97:97)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1051 | [96](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=96:96)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1052 | [95](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=95:95)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1053 | [94](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=94:94)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1054 | [93](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=93:93)       | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1055 | [125](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=125:125)    | UBERON:0005897 | manus bone                   | hand bone                    | UBERON:0003460 | arm bone                             | arm bone          |   6.0438  |
| 1056 | [246](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=246:246)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1057 | [280](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=280:280)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1058 | [215](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=215:215)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1059 | [223](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=223:223)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1060 | [222](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=222:222)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1061 | [221](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=221:221)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1062 | [220](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=220:220)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1063 | [253](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=253:253)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1064 | [219](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=219:219)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1065 | [254](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=254:254)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1066 | [218](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=218:218)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1067 | [217](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=217:217)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1068 | [255](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=255:255)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1069 | [216](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=216:216)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1070 | [214](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=214:214)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1071 | [224](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=224:224)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1072 | [213](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=213:213)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1073 | [212](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=212:212)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1074 | [211](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=211:211)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1075 | [256](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=256:256)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1076 | [210](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=210:210)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1077 | [209](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=209:209)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1078 | [208](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=208:208)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1079 | [207](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=207:207)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1080 | [257](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=257:257)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1081 | [206](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=206:206)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1082 | [205](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=205:205)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1083 | [252](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=252:252)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1084 | [225](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=225:225)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1085 | [258](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=258:258)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1086 | [237](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=237:237)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1087 | [245](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=245:245)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1088 | [244](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=244:244)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1089 | [243](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=243:243)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1090 | [242](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=242:242)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1091 | [241](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=241:241)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1092 | [247](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=247:247)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1093 | [240](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=240:240)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1094 | [239](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=239:239)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1095 | [248](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=248:248)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1096 | [238](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=238:238)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1097 | [249](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=249:249)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1098 | [236](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=236:236)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1099 | [226](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=226:226)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1100 | [235](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=235:235)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1101 | [234](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=234:234)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1102 | [250](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=250:250)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1103 | [233](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=233:233)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1104 | [232](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=232:232)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1105 | [231](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=231:231)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1106 | [230](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=230:230)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1107 | [251](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=251:251)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1108 | [229](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=229:229)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1109 | [228](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=228:228)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1110 | [227](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=227:227)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1111 | [279](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=279:279)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1112 | [204](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=204:204)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1113 | [188](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=188:188)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1114 | [272](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=272:272)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1115 | [266](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=266:266)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1116 | [187](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=187:187)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1117 | [267](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=267:267)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1118 | [186](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=186:186)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1119 | [185](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=185:185)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1120 | [184](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=184:184)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1121 | [268](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=268:268)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1122 | [183](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=183:183)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1123 | [269](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=269:269)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1124 | [270](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=270:270)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1125 | [271](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=271:271)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1126 | [273](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=273:273)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1127 | [189](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=189:189)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1128 | [274](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=274:274)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1129 | [182](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=182:182)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1130 | [275](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=275:275)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1131 | [181](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=181:181)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1132 | [180](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=180:180)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1133 | [179](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=179:179)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1134 | [276](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=276:276)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1135 | [178](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=178:178)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1136 | [177](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=177:177)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1137 | [277](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=277:277)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1138 | [278](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=278:278)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1139 | [203](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=203:203)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1140 | [176](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=176:176)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1141 | [265](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=265:265)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1142 | [262](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=262:262)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1143 | [202](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=202:202)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1144 | [201](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=201:201)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1145 | [259](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=259:259)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1146 | [200](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=200:200)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1147 | [260](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=260:260)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1148 | [199](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=199:199)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1149 | [261](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=261:261)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1150 | [190](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=190:190)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1151 | [197](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=197:197)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1152 | [198](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=198:198)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1153 | [196](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=196:196)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1154 | [194](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=194:194)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1155 | [191](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=191:191)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1156 | [192](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=192:192)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1157 | [193](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=193:193)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1158 | [264](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=264:264)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1159 | [263](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=263:263)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1160 | [195](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=195:195)    | UBERON:0005899 | pes bone                     | foot bone                    | UBERON:0005893 | leg bone                             | leg bone          |   5.54571 |
| 1162 | [377](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=377:377)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1163 | [371](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=371:371)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1164 | [374](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=374:374)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1165 | [376](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=376:376)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1166 | [373](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=373:373)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1167 | [375](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=375:375)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1168 | [370](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=370:370)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1169 | [372](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=372:372)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1170 | [378](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=378:378)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1171 | [422](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=422:422)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1172 | [379](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=379:379)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1173 | [440](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=440:440)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1174 | [442](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=442:442)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1175 | [443](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=443:443)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1176 | [444](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=444:444)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1177 | [445](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=445:445)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1178 | [446](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=446:446)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1179 | [447](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=447:447)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1180 | [448](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=448:448)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1181 | [449](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=449:449)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1182 | [421](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=421:421)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1183 | [366](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=366:366)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1184 | [420](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=420:420)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1185 | [419](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=419:419)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1186 | [418](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=418:418)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1187 | [417](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=417:417)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1188 | [367](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=367:367)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1189 | [441](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=441:441)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1190 | [439](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=439:439)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1191 | [380](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=380:380)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1192 | [438](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=438:438)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1193 | [423](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=423:423)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1194 | [424](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=424:424)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1195 | [425](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=425:425)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1196 | [426](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=426:426)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1197 | [427](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=427:427)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1198 | [428](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=428:428)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1199 | [429](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=429:429)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1200 | [430](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=430:430)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1201 | [431](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=431:431)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1202 | [432](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=432:432)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1203 | [433](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=433:433)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1204 | [434](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=434:434)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1205 | [435](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=435:435)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1206 | [436](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=436:436)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1207 | [437](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=437:437)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1208 | [415](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=415:415)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1209 | [414](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=414:414)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1210 | [413](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=413:413)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1211 | [412](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=412:412)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1212 | [393](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=393:393)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1213 | [392](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=392:392)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1214 | [369](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=369:369)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1215 | [391](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=391:391)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1216 | [390](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=390:390)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1217 | [389](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=389:389)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1218 | [368](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=368:368)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1219 | [388](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=388:388)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1220 | [387](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=387:387)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1221 | [386](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=386:386)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1222 | [385](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=385:385)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1223 | [384](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=384:384)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1224 | [383](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=383:383)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1225 | [382](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=382:382)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1226 | [381](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=381:381)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1227 | [394](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=394:394)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1228 | [395](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=395:395)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1229 | [396](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=396:396)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1230 | [405](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=405:405)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1231 | [411](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=411:411)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1232 | [410](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=410:410)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1233 | [409](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=409:409)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1234 | [408](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=408:408)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1235 | [407](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=407:407)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1236 | [406](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=406:406)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1237 | [404](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=404:404)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1238 | [397](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=397:397)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1239 | [403](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=403:403)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1240 | [402](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=402:402)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1241 | [401](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=401:401)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1242 | [400](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=400:400)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1243 | [399](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=399:399)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1244 | [398](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=398:398)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1245 | [416](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=416:416)    | UBERON:0001703 | neurocranium                 | neurocranium                 | UBERON:0004766 | cranial bone                         | cranial bone      |   5.32996 |
| 1262 | [862](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=862:862)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1263 | [879](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=879:879)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1264 | [880](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=880:880)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1265 | [863](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=863:863)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1266 | [869](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=869:869)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1267 | [878](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=878:878)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1268 | [877](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=877:877)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1269 | [875](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=875:875)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1270 | [874](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=874:874)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1271 | [873](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=873:873)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1272 | [872](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=872:872)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1273 | [871](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=871:871)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1274 | [870](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=870:870)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1275 | [876](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=876:876)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1276 | [868](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=868:868)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1277 | [867](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=867:867)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1278 | [866](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=866:866)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1279 | [865](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=865:865)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1280 | [864](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=864:864)    | UBERON:0003690 | fused sacrum                 | sacrum                       | UBERON:0001094 | sacral vertebra                      | sacral vertebra   |   4.59149 |
| 1320 | [455](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=455:455)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1321 | [454](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=454:454)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1322 | [467](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=467:467)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1323 | [456](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=456:456)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1324 | [485](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=485:485)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1325 | [487](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=487:487)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1326 | [488](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=488:488)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1327 | [489](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=489:489)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1328 | [490](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=490:490)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1329 | [491](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=491:491)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1330 | [492](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=492:492)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1331 | [493](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=493:493)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1332 | [494](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=494:494)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1333 | [495](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=495:495)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1334 | [496](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=496:496)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1335 | [497](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=497:497)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1336 | [498](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=498:498)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1337 | [499](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=499:499)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1338 | [500](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=500:500)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1339 | [501](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=501:501)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1340 | [502](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=502:502)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1341 | [503](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=503:503)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1342 | [504](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=504:504)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1343 | [505](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=505:505)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1344 | [506](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=506:506)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1345 | [507](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=507:507)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1346 | [508](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=508:508)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1347 | [509](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=509:509)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1348 | [486](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=486:486)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1349 | [484](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=484:484)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1350 | [457](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=457:457)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1351 | [483](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=483:483)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1352 | [458](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=458:458)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1353 | [459](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=459:459)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1354 | [460](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=460:460)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1355 | [461](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=461:461)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1356 | [463](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=463:463)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1357 | [464](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=464:464)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1358 | [465](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=465:465)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1359 | [466](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=466:466)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1360 | [468](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=468:468)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1361 | [469](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=469:469)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1362 | [470](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=470:470)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1363 | [471](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=471:471)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1364 | [472](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=472:472)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1365 | [473](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=473:473)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1366 | [474](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=474:474)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1367 | [475](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=475:475)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1368 | [476](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=476:476)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1369 | [477](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=477:477)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1370 | [478](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=478:478)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1371 | [479](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=479:479)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1372 | [480](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=480:480)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1373 | [481](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=481:481)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1374 | [482](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=482:482)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1375 | [462](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=462:462)    | UBERON:0008895 | splanchnocranium             | splanchnocranium             | UBERON:0004766 | cranial bone                         | cranial bone      |   1.76865 |
| 1379 | [147](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=147:147)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1380 | [148](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=148:148)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1381 | [149](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=149:149)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1382 | [150](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=150:150)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1383 | [151](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=151:151)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1384 | [152](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=152:152)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1385 | [153](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=153:153)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1386 | [154](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=154:154)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1387 | [155](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=155:155)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1388 | [156](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=156:156)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1389 | [157](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=157:157)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1390 | [158](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=158:158)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1391 | [159](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=159:159)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1392 | [160](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=160:160)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1393 | [161](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=161:161)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1394 | [162](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=162:162)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1395 | [163](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=163:163)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1396 | [164](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=164:164)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1397 | [165](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=165:165)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1398 | [166](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=166:166)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1399 | [167](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=167:167)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1400 | [168](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=168:168)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1401 | [169](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=169:169)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1402 | [170](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=170:170)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1403 | [171](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=171:171)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1404 | [172](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=172:172)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1405 | [173](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=173:173)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1406 | [174](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=174:174)    | UBERON:0007829 | pectoral girdle bone         | pectoral girdle bone         | UBERON:0003460 | arm bone                             | arm bone          | nan       |
| 1408 | [323](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=323:323)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1409 | [324](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=324:324)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1410 | [325](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=325:325)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1411 | [326](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=326:326)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1412 | [327](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=327:327)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1413 | [328](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=328:328)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1414 | [329](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=329:329)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1415 | [330](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=330:330)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1416 | [331](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=331:331)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1417 | [332](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=332:332)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1418 | [333](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=333:333)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1419 | [334](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=334:334)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1420 | [335](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=335:335)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1421 | [336](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=336:336)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1422 | [337](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=337:337)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1423 | [338](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=338:338)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1424 | [339](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=339:339)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1425 | [340](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=340:340)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1426 | [341](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=341:341)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1427 | [342](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=342:342)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1428 | [343](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=343:343)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1429 | [344](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=344:344)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1430 | [345](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=345:345)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1431 | [346](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=346:346)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1432 | [347](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=347:347)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1433 | [348](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=348:348)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1434 | [349](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=349:349)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1435 | [350](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=350:350)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1436 | [351](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=351:351)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1437 | [352](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=352:352)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1438 | [353](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=353:353)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1439 | [354](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=354:354)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1440 | [355](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=355:355)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1441 | [356](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=356:356)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1442 | [357](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=357:357)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1443 | [358](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=358:358)    | UBERON:0007830 | pelvic girdle bone/zone      | pelvic girdle bone/zone      | UBERON:0005893 | leg bone                             | leg bone          | nan       |
| 1445 | [360](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=360:360)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1447 | [361](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=361:361)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1449 | [362](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=362:362)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1450 | [363](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=363:363)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1451 | [364](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=364:364)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1452 | [365](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=365:365)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1453 | [366](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=366:366)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1454 | [367](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=367:367)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1455 | [368](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=368:368)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1456 | [369](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=369:369)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1457 | [370](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=370:370)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1458 | [371](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=371:371)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1459 | [372](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=372:372)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1460 | [373](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=373:373)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1461 | [374](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=374:374)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1462 | [375](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=375:375)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1463 | [376](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=376:376)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1464 | [377](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=377:377)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1465 | [378](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=378:378)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1466 | [379](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=379:379)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1467 | [380](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=380:380)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1468 | [381](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=381:381)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1469 | [382](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=382:382)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1470 | [383](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=383:383)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1471 | [384](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=384:384)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1472 | [385](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=385:385)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1473 | [386](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=386:386)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1474 | [387](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=387:387)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1475 | [388](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=388:388)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1476 | [389](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=389:389)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1477 | [390](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=390:390)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1478 | [391](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=391:391)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1479 | [392](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=392:392)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1480 | [393](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=393:393)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1481 | [394](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=394:394)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1482 | [395](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=395:395)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1483 | [396](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=396:396)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1484 | [397](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=397:397)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1485 | [398](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=398:398)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1486 | [399](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=399:399)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1487 | [400](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=400:400)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1488 | [401](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=401:401)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1489 | [402](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=402:402)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1490 | [403](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=403:403)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1491 | [404](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=404:404)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1492 | [405](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=405:405)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1493 | [406](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=406:406)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1494 | [407](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=407:407)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1495 | [408](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=408:408)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1496 | [409](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=409:409)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1497 | [410](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=410:410)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1498 | [411](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=411:411)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1499 | [412](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=412:412)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1500 | [413](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=413:413)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1501 | [414](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=414:414)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1502 | [415](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=415:415)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1503 | [416](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=416:416)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1504 | [417](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=417:417)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1505 | [418](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=418:418)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1506 | [419](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=419:419)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1507 | [420](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=420:420)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1508 | [421](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=421:421)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1509 | [422](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=422:422)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1510 | [423](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=423:423)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1511 | [424](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=424:424)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1512 | [425](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=425:425)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1513 | [426](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=426:426)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1514 | [427](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=427:427)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1515 | [428](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=428:428)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1516 | [428](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=428:428)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1517 | [429](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=429:429)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1518 | [429](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=429:429)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1519 | [430](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=430:430)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1520 | [430](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=430:430)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1521 | [431](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=431:431)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1522 | [431](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=431:431)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1523 | [432](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=432:432)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1524 | [432](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=432:432)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1525 | [433](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=433:433)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1526 | [433](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=433:433)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1527 | [434](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=434:434)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1528 | [434](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=434:434)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1529 | [435](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=435:435)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1530 | [435](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=435:435)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1531 | [436](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=436:436)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1532 | [436](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=436:436)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1533 | [437](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=437:437)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1534 | [437](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=437:437)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1535 | [438](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=438:438)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1536 | [438](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=438:438)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1537 | [439](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=439:439)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1538 | [439](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=439:439)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1539 | [440](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=440:440)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1540 | [440](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=440:440)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1541 | [441](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=441:441)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1542 | [441](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=441:441)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1543 | [442](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=442:442)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1544 | [442](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=442:442)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1545 | [443](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=443:443)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1546 | [443](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=443:443)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1547 | [444](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=444:444)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1548 | [444](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=444:444)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1549 | [445](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=445:445)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1550 | [445](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=445:445)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1551 | [446](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=446:446)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1552 | [446](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=446:446)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1553 | [447](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=447:447)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1554 | [447](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=447:447)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1555 | [448](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=448:448)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1556 | [448](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=448:448)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1557 | [449](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=449:449)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1558 | [449](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=449:449)    | UBERON:0001678 | temporal bone                | temporal bone                | UBERON:0001703 | neurocranium                         | neurocranium      | nan       |
| 1559 | [450](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=450:450)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1560 | [450](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=450:450)    | UBERON:0010911 | ossicle                      | ossicle                      | UBERON:0004766 | cranial bone                         | cranial bone      | nan       |
| 1561 | [451](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=451:451)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1562 | [451](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=451:451)    | UBERON:0010911 | ossicle                      | ossicle                      | UBERON:0004766 | cranial bone                         | cranial bone      | nan       |
| 1563 | [451](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=451:451)    | UBERON:0001688 | incus bone                   | incus bone                   | UBERON:0010911 | ossicle                              | ossicle           | nan       |
| 1564 | [452](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=452:452)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1565 | [452](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=452:452)    | UBERON:0010911 | ossicle                      | ossicle                      | UBERON:0004766 | cranial bone                         | cranial bone      | nan       |
| 1566 | [452](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=452:452)    | UBERON:0001689 | malleus bone                 | malleus bone                 | UBERON:0010911 | ossicle                              | ossicle           | nan       |
| 1567 | [453](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=453:453)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1568 | [453](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=453:453)    | UBERON:0010911 | ossicle                      | ossicle                      | UBERON:0004766 | cranial bone                         | cranial bone      | nan       |
| 1569 | [453](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=453:453)    | UBERON:0001687 | stapes bone                  | stapes bone                  | UBERON:0010911 | ossicle                              | ossicle           | nan       |
| 1570 | [454](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=454:454)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1572 | [455](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=455:455)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1573 | [455](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=455:455)    | UBERON:0005922 | inferior nasal concha        | inferior nasal concha        | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1574 | [456](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=456:456)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1575 | [456](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=456:456)    | UBERON:0001680 | lacrimal bone                | lacrimal bone                | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1576 | [457](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=457:457)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1577 | [457](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=457:457)    | UBERON:0001680 | lacrimal bone                | lacrimal bone                | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1578 | [458](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=458:458)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1579 | [458](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=458:458)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1580 | [459](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=459:459)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1581 | [459](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=459:459)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1582 | [460](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=460:460)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1583 | [460](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=460:460)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1584 | [461](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=461:461)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1585 | [461](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=461:461)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1586 | [462](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=462:462)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1587 | [462](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=462:462)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1588 | [463](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=463:463)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1589 | [463](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=463:463)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1590 | [464](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=464:464)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1591 | [464](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=464:464)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1592 | [465](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=465:465)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1593 | [465](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=465:465)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1594 | [466](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=466:466)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1595 | [466](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=466:466)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1596 | [467](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=467:467)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1597 | [467](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=467:467)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1598 | [468](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=468:468)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1599 | [468](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=468:468)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1600 | [469](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=469:469)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1601 | [469](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=469:469)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1602 | [470](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=470:470)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1603 | [470](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=470:470)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1604 | [471](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=471:471)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1605 | [471](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=471:471)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1606 | [472](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=472:472)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1607 | [472](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=472:472)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1608 | [473](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=473:473)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1609 | [473](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=473:473)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1610 | [474](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=474:474)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1611 | [474](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=474:474)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1612 | [475](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=475:475)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1613 | [475](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=475:475)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1614 | [476](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=476:476)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1615 | [476](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=476:476)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1616 | [477](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=477:477)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1617 | [477](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=477:477)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1618 | [478](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=478:478)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1619 | [478](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=478:478)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1620 | [479](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=479:479)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1621 | [479](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=479:479)    | UBERON:0001684 | mandible                     | mandible                     | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1622 | [480](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=480:480)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1623 | [480](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=480:480)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1624 | [481](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=481:481)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1625 | [481](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=481:481)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1626 | [482](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=482:482)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1627 | [482](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=482:482)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1628 | [483](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=483:483)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1629 | [483](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=483:483)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1630 | [484](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=484:484)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1631 | [484](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=484:484)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1632 | [485](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=485:485)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1633 | [485](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=485:485)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1634 | [486](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=486:486)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1635 | [486](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=486:486)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1636 | [487](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=487:487)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1637 | [487](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=487:487)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1638 | [488](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=488:488)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1639 | [488](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=488:488)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1640 | [489](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=489:489)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1641 | [489](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=489:489)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1642 | [490](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=490:490)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1643 | [490](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=490:490)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1644 | [491](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=491:491)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1645 | [491](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=491:491)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1646 | [492](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=492:492)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1647 | [492](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=492:492)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1648 | [493](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=493:493)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1649 | [493](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=493:493)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1650 | [494](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=494:494)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1651 | [494](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=494:494)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1652 | [495](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=495:495)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1653 | [495](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=495:495)    | UBERON:0002397 | maxilla                      | maxilla                      | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1654 | [495](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=495:495)    | UBERON:0016477 | zygomatic process of maxilla | zygomatic process of maxilla | UBERON:0002397 | maxilla                              | maxilla           | nan       |
| 1655 | [496](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=496:496)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1656 | [496](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=496:496)    | UBERON:0001681 | nasal bone                   | nasal bone                   | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1657 | [497](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=497:497)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1658 | [498](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=498:498)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1659 | [499](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=499:499)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1660 | [500](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=500:500)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1661 | [501](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=501:501)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1662 | [502](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=502:502)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1663 | [503](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=503:503)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1664 | [504](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=504:504)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1665 | [505](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=505:505)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1666 | [505](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=505:505)    | UBERON:0001683 | jugal bone                   | zygomatic bone               | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1667 | [506](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=506:506)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1668 | [506](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=506:506)    | UBERON:0001683 | jugal bone                   | zygomatic bone               | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1669 | [507](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=507:507)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1670 | [507](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=507:507)    | UBERON:0001683 | jugal bone                   | zygomatic bone               | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1671 | [508](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=508:508)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1672 | [508](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=508:508)    | UBERON:0001683 | jugal bone                   | zygomatic bone               | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1673 | [509](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=509:509)    | UBERON:0004766 | cranial bone                 | cranial bone                 | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1674 | [509](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=509:509)    | UBERON:0001683 | jugal bone                   | zygomatic bone               | UBERON:0008895 | splanchnocranium                     | splanchnocranium  | nan       |
| 1675 | [662](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=662:662)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1676 | [663](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=663:663)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1677 | [664](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=664:664)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1678 | [664](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=664:664)    | UBERON:0001350 | coccyx                       | coccyx                       | UBERON:0001095 | caudal vertebra                      | caudal vertebra   | nan       |
| 1679 | [665](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=665:665)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1680 | [665](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=665:665)    | UBERON:0001350 | coccyx                       | coccyx                       | UBERON:0001095 | caudal vertebra                      | caudal vertebra   | nan       |
| 1681 | [666](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=666:666)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1682 | [666](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=666:666)    | UBERON:0001350 | coccyx                       | coccyx                       | UBERON:0001095 | caudal vertebra                      | caudal vertebra   | nan       |
| 1683 | [667](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=667:667)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1684 | [668](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=668:668)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1685 | [668](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=668:668)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1686 | [669](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=669:669)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1687 | [669](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=669:669)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1688 | [670](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=670:670)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1689 | [670](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=670:670)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1690 | [671](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=671:671)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1691 | [671](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=671:671)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1692 | [672](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=672:672)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1693 | [672](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=672:672)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1694 | [673](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=673:673)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1695 | [673](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=673:673)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1696 | [674](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=674:674)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1697 | [674](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=674:674)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1698 | [675](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=675:675)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1699 | [675](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=675:675)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1700 | [676](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=676:676)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1701 | [676](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=676:676)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1702 | [677](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=677:677)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1703 | [677](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=677:677)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1704 | [678](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=678:678)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1705 | [678](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=678:678)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1706 | [679](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=679:679)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1707 | [679](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=679:679)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1708 | [680](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=680:680)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1709 | [680](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=680:680)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1710 | [681](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=681:681)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1711 | [681](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=681:681)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1712 | [682](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=682:682)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1713 | [682](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=682:682)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1714 | [683](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=683:683)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1715 | [683](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=683:683)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1716 | [684](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=684:684)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1717 | [684](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=684:684)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1718 | [685](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=685:685)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1719 | [685](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=685:685)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1720 | [686](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=686:686)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1721 | [686](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=686:686)    | UBERON:0001092 | vertebral bone 1             | cervical vertebra 1          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1722 | [687](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=687:687)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1723 | [687](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=687:687)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1724 | [688](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=688:688)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1725 | [688](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=688:688)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1726 | [689](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=689:689)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1727 | [689](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=689:689)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1728 | [690](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=690:690)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1729 | [690](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=690:690)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1730 | [691](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=691:691)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1731 | [691](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=691:691)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1732 | [692](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=692:692)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1733 | [692](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=692:692)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1734 | [693](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=693:693)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1735 | [693](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=693:693)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1736 | [694](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=694:694)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1737 | [694](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=694:694)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1738 | [695](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=695:695)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1739 | [695](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=695:695)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1740 | [696](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=696:696)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1741 | [696](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=696:696)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1742 | [697](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=697:697)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1743 | [697](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=697:697)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1744 | [698](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=698:698)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1745 | [698](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=698:698)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1746 | [699](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=699:699)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1747 | [699](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=699:699)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1748 | [700](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=700:700)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1749 | [700](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=700:700)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1750 | [701](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=701:701)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1751 | [701](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=701:701)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1752 | [702](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=702:702)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1753 | [702](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=702:702)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1754 | [703](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=703:703)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1755 | [703](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=703:703)    | UBERON:0001093 | vertebral bone 2             | cervical vertebra 2          | UBERON:0002413 | cervical vertebra                    | cervical vertebra | nan       |
| 1756 | [704](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=704:704)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1757 | [705](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=705:705)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1758 | [706](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=706:706)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1759 | [707](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=707:707)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1760 | [708](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=708:708)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1761 | [709](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=709:709)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1762 | [710](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=710:710)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1763 | [711](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=711:711)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1764 | [712](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=712:712)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1765 | [713](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=713:713)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1766 | [714](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=714:714)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1767 | [715](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=715:715)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1768 | [716](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=716:716)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1769 | [717](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=717:717)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1770 | [718](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=718:718)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1771 | [719](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=719:719)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1772 | [720](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=720:720)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1773 | [721](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=721:721)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1774 | [722](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=722:722)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1775 | [723](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=723:723)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1776 | [724](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=724:724)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1777 | [725](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=725:725)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1778 | [726](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=726:726)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1779 | [727](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=727:727)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1780 | [728](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=728:728)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1781 | [729](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=729:729)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1782 | [730](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=730:730)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1783 | [731](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=731:731)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1784 | [732](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=732:732)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1785 | [733](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=733:733)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1786 | [734](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=734:734)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1787 | [735](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=735:735)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1788 | [736](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=736:736)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1789 | [737](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=737:737)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1790 | [738](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=738:738)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1791 | [739](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=739:739)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1792 | [740](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=740:740)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1793 | [741](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=741:741)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1794 | [742](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=742:742)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1795 | [743](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=743:743)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1796 | [744](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=744:744)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1797 | [745](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=745:745)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1798 | [746](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=746:746)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1799 | [747](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=747:747)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1800 | [748](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=748:748)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1801 | [749](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=749:749)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1802 | [750](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=750:750)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1803 | [751](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=751:751)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1804 | [752](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=752:752)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1805 | [753](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=753:753)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1806 | [754](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=754:754)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1807 | [755](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=755:755)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1808 | [756](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=756:756)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1809 | [757](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=757:757)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1810 | [758](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=758:758)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1811 | [759](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=759:759)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1812 | [760](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=760:760)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1813 | [761](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=761:761)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1814 | [762](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=762:762)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1815 | [763](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=763:763)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1816 | [764](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=764:764)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1817 | [765](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=765:765)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1818 | [766](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=766:766)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1819 | [767](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=767:767)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1820 | [768](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=768:768)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1821 | [769](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=769:769)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1822 | [770](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=770:770)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1823 | [771](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=771:771)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1824 | [772](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=772:772)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1825 | [773](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=773:773)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1826 | [774](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=774:774)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1827 | [775](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=775:775)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1828 | [776](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=776:776)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1829 | [777](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=777:777)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1830 | [778](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=778:778)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1831 | [779](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=779:779)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1832 | [780](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=780:780)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1833 | [781](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=781:781)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1834 | [782](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=782:782)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1835 | [783](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=783:783)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1836 | [784](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=784:784)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1837 | [785](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=785:785)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1838 | [786](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=786:786)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1839 | [787](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=787:787)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1840 | [788](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=788:788)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1841 | [789](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=789:789)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1842 | [790](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=790:790)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1843 | [791](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=791:791)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1844 | [792](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=792:792)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1845 | [793](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=793:793)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1846 | [794](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=794:794)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1847 | [795](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=795:795)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1848 | [796](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=796:796)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1849 | [797](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=797:797)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1850 | [798](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=798:798)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1851 | [799](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=799:799)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1852 | [800](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=800:800)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1853 | [801](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=801:801)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1854 | [802](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=802:802)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1855 | [803](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=803:803)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1856 | [804](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=804:804)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1857 | [805](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=805:805)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1858 | [806](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=806:806)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1859 | [807](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=807:807)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1860 | [808](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=808:808)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1861 | [809](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=809:809)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1862 | [810](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=810:810)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1863 | [811](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=811:811)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1864 | [812](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=812:812)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1865 | [813](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=813:813)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1866 | [814](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=814:814)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1867 | [815](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=815:815)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1868 | [816](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=816:816)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1869 | [817](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=817:817)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1870 | [818](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=818:818)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1871 | [819](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=819:819)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1872 | [820](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=820:820)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1873 | [821](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=821:821)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1874 | [822](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=822:822)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1875 | [823](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=823:823)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1876 | [824](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=824:824)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1877 | [825](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=825:825)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1878 | [826](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=826:826)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1879 | [827](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=827:827)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1880 | [828](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=828:828)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1881 | [829](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=829:829)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1882 | [830](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=830:830)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1883 | [831](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=831:831)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1884 | [832](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=832:832)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1885 | [833](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=833:833)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1886 | [834](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=834:834)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1887 | [835](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=835:835)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1888 | [836](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=836:836)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1889 | [837](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=837:837)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1890 | [838](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=838:838)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1891 | [839](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=839:839)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1892 | [840](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=840:840)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1893 | [841](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=841:841)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1894 | [842](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=842:842)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1895 | [843](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=843:843)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1896 | [844](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=844:844)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1897 | [845](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=845:845)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1898 | [846](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=846:846)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1899 | [847](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=847:847)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1900 | [848](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=848:848)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1901 | [849](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=849:849)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1902 | [850](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=850:850)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1903 | [851](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=851:851)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1904 | [852](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=852:852)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1905 | [853](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=853:853)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1906 | [854](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=854:854)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1907 | [855](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=855:855)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1908 | [856](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=856:856)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1909 | [857](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=857:857)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1910 | [858](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=858:858)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1911 | [859](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=859:859)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1912 | [860](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=860:860)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1913 | [861](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=861:861)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1914 | [862](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=862:862)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1915 | [863](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=863:863)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1916 | [864](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=864:864)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1917 | [865](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=865:865)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1918 | [866](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=866:866)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1919 | [867](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=867:867)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1920 | [868](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=868:868)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1921 | [869](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=869:869)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1922 | [870](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=870:870)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1923 | [871](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=871:871)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1924 | [872](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=872:872)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1925 | [873](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=873:873)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1926 | [874](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=874:874)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1927 | [875](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=875:875)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1928 | [876](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=876:876)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1929 | [877](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=877:877)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1930 | [878](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=878:878)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1931 | [879](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=879:879)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1932 | [880](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=880:880)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1933 | [881](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=881:881)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1934 | [882](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=882:882)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1935 | [883](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=883:883)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1936 | [884](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=884:884)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1937 | [885](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=885:885)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1938 | [886](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=886:886)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1939 | [887](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=887:887)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1940 | [888](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=888:888)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1941 | [889](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=889:889)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1942 | [890](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=890:890)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1943 | [891](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=891:891)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1944 | [892](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=892:892)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1945 | [893](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=893:893)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1946 | [894](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=894:894)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1947 | [895](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=895:895)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1948 | [896](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=896:896)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1949 | [897](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=897:897)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1950 | [898](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=898:898)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1951 | [899](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=899:899)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1952 | [900](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=900:900)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1953 | [901](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=901:901)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1954 | [902](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=902:902)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1955 | [903](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=903:903)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1956 | [904](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=904:904)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1957 | [905](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=905:905)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1958 | [906](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=906:906)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1959 | [907](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=907:907)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1960 | [908](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=908:908)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1961 | [909](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=909:909)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1962 | [910](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=910:910)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1963 | [911](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=911:911)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1964 | [912](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=912:912)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1965 | [913](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=913:913)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1966 | [914](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=914:914)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1967 | [915](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=915:915)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1968 | [916](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=916:916)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1969 | [917](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=917:917)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1970 | [918](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=918:918)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1971 | [919](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=919:919)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1972 | [920](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=920:920)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1973 | [921](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=921:921)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1974 | [922](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=922:922)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1975 | [923](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=923:923)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1976 | [924](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=924:924)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1977 | [925](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=925:925)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1978 | [926](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=926:926)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1979 | [927](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=927:927)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1980 | [928](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=928:928)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1981 | [929](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=929:929)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1982 | [930](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=930:930)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1983 | [931](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=931:931)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1984 | [932](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=932:932)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1985 | [933](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=933:933)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1986 | [934](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=934:934)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1987 | [935](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=935:935)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1988 | [936](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=936:936)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1989 | [937](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=937:937)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1990 | [938](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=938:938)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1991 | [939](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=939:939)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1992 | [940](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=940:940)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1993 | [941](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=941:941)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1994 | [942](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=942:942)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1995 | [943](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=943:943)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1996 | [944](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=944:944)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1997 | [945](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=945:945)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1998 | [946](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=946:946)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 1999 | [947](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=947:947)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2000 | [948](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=948:948)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2001 | [949](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=949:949)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2002 | [950](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=950:950)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2003 | [951](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=951:951)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2004 | [952](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=952:952)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2005 | [953](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=953:953)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2006 | [954](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=954:954)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2007 | [955](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=955:955)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2008 | [956](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=956:956)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2009 | [957](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=957:957)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2010 | [958](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=958:958)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2011 | [959](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=959:959)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2012 | [960](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=960:960)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2013 | [961](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=961:961)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2014 | [962](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=962:962)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2015 | [963](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=963:963)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2016 | [964](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=964:964)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2017 | [965](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=965:965)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2018 | [966](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=966:966)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2019 | [967](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=967:967)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2020 | [968](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=968:968)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2021 | [969](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=969:969)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2022 | [970](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=970:970)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2023 | [971](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=971:971)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2024 | [972](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=972:972)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2025 | [973](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=973:973)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2026 | [974](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=974:974)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2027 | [975](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=975:975)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2028 | [976](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=976:976)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2029 | [977](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=977:977)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2030 | [978](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=978:978)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2031 | [979](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=979:979)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2032 | [980](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=980:980)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2033 | [981](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=981:981)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2034 | [982](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=982:982)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2035 | [983](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=983:983)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2036 | [984](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=984:984)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2037 | [985](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=985:985)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2038 | [986](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=986:986)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2039 | [987](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=987:987)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2040 | [988](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=988:988)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2041 | [989](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=989:989)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2042 | [990](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=990:990)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2043 | [991](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=991:991)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2044 | [992](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=992:992)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2045 | [993](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=993:993)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2046 | [994](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=994:994)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2047 | [995](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=995:995)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2048 | [996](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=996:996)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2049 | [997](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=997:997)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2050 | [998](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=998:998)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2051 | [999](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=999:999)    | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2052 | [1000](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1000:1000) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2053 | [1001](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1001:1001) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2054 | [1002](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1002:1002) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2055 | [1003](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1003:1003) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2056 | [1004](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1004:1004) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2057 | [1005](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1005:1005) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2058 | [1006](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1006:1006) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2059 | [1007](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1007:1007) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2060 | [1008](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1008:1008) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2061 | [1009](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1009:1009) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2062 | [1010](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1010:1010) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2063 | [1011](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1011:1011) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2064 | [1012](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1012:1012) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2065 | [1013](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1013:1013) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2066 | [1014](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1014:1014) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2067 | [1015](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1015:1015) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2068 | [1016](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1016:1016) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2069 | [1017](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1017:1017) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2070 | [1018](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1018:1018) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2071 | [1019](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1019:1019) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2072 | [1020](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1020:1020) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2073 | [1021](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1021:1021) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2074 | [1022](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1022:1022) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2075 | [1023](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1023:1023) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2076 | [1024](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1024:1024) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2077 | [1025](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1025:1025) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2078 | [1026](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1026:1026) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2079 | [1027](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1027:1027) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2080 | [1028](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1028:1028) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2081 | [1029](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1029:1029) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2082 | [1030](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1030:1030) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2083 | [1031](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1031:1031) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2084 | [1032](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1032:1032) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2085 | [1033](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1033:1033) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2086 | [1034](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1034:1034) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2087 | [1035](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1035:1035) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2088 | [1036](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1036:1036) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2089 | [1037](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1037:1037) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2090 | [1038](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1038:1038) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2091 | [1039](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1039:1039) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2092 | [1040](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1040:1040) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2093 | [1041](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1041:1041) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2094 | [1042](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1042:1042) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2095 | [1043](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1043:1043) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2096 | [1044](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1044:1044) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2097 | [1045](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1045:1045) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2098 | [1046](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1046:1046) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2099 | [1047](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1047:1047) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2100 | [1048](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1048:1048) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2101 | [1049](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1049:1049) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2102 | [1050](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1050:1050) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2103 | [1051](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1051:1051) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2104 | [1052](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1052:1052) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2105 | [1053](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1053:1053) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2106 | [1054](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1054:1054) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2107 | [1055](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1055:1055) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2108 | [1056](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1056:1056) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2109 | [1057](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1057:1057) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2110 | [1058](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1058:1058) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2111 | [1059](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1059:1059) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2112 | [1060](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1060:1060) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2113 | [1061](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1061:1061) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2114 | [1062](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1062:1062) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2115 | [1063](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1063:1063) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2116 | [1064](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1064:1064) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2117 | [1065](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1065:1065) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2118 | [1066](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1066:1066) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2119 | [1067](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1067:1067) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2120 | [1068](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1068:1068) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2121 | [1069](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1069:1069) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2122 | [1070](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1070:1070) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2123 | [1071](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1071:1071) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2124 | [1072](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1072:1072) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2125 | [1073](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1073:1073) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2126 | [1074](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1074:1074) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2127 | [1075](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1075:1075) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2128 | [1076](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1076:1076) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2129 | [1077](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1077:1077) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2130 | [1078](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1078:1078) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2131 | [1079](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1079:1079) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2132 | [1080](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1080:1080) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2133 | [1081](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1081:1081) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2134 | [1082](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1082:1082) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |
| 2135 | [1083](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1083:1083) | UBERON:0001130 | vertebral column             | vertebral column             | UBERON:0005944 | axial skeleton plus cranial skeleton | axial skeleton    | nan       |




## Relationship CT-CT report


In the case of the CT-CT relationship, for each couple of terms, we verify for _sub class of, part of and overlaps_ in the source ontologies. The **deltaIC** score is included because a high score (>50) can indicate that this order is reversed, e.g. TBA.



- No issues found.






## Relationship CT-AS report


In the case of the AS-CT relationship, for each couple of terms, we verify for _connected to and has part_ in the source ontologies.



|      | row_number                                                                                                             | s          | slabel    | user_slabel   | o              | olabel                                  | user_olabel                                  |
|------|------------------------------------------------------------------------------------------------------------------------|------------|-----------|---------------|----------------|-----------------------------------------|----------------------------------------------|
|    0 | [12](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=12:12)       | CL:0001035 | bone cell | bone cell     | UBERON:0004288 | skeleton                                | skeleton                                     |
|    1 | [718](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=718:718)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|    2 | [719](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=719:719)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|    3 | [720](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=720:720)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|    4 | [721](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=721:721)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|    5 | [722](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=722:722)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|    6 | [723](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=723:723)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|    7 | [724](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=724:724)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|    8 | [725](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=725:725)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|    9 | [726](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=726:726)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|   10 | [727](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=727:727)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|   11 | [728](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=728:728)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|   12 | [729](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=729:729)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|   13 | [730](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=730:730)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|   14 | [731](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=731:731)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|   15 | [732](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=732:732)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|   16 | [733](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=733:733)    | CL:0001035 | bone cell | bone cell     | UBERON:0004613 | mammalian cervical vertebra 4           | cervical vertebra 4                          |
|   17 | [734](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=734:734)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   18 | [735](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=735:735)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   19 | [736](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=736:736)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   20 | [737](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=737:737)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   21 | [738](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=738:738)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   22 | [739](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=739:739)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   23 | [740](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=740:740)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   24 | [741](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=741:741)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   25 | [742](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=742:742)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   26 | [743](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=743:743)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   27 | [744](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=744:744)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   28 | [745](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=745:745)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   29 | [746](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=746:746)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   30 | [717](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=717:717)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   31 | [716](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=716:716)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   32 | [715](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=715:715)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   33 | [714](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=714:714)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   34 | [684](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=684:684)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|   35 | [685](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=685:685)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|   36 | [686](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=686:686)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|   37 | [687](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=687:687)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   38 | [688](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=688:688)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   39 | [689](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=689:689)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   40 | [690](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=690:690)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   41 | [691](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=691:691)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   42 | [692](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=692:692)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   43 | [693](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=693:693)    | CL:0001035 | bone cell | bone cell     | UBERON:0004096 | odontoid process of cervical vertebra 2 | odontoid process of second cervical vertebra |
|   44 | [694](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=694:694)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   45 | [695](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=695:695)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   46 | [696](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=696:696)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   47 | [697](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=697:697)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   48 | [747](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=747:747)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   49 | [698](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=698:698)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   50 | [700](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=700:700)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   51 | [701](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=701:701)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   52 | [702](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=702:702)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   53 | [703](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=703:703)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   54 | [704](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=704:704)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   55 | [705](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=705:705)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   56 | [706](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=706:706)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   57 | [707](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=707:707)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   58 | [708](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=708:708)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   59 | [709](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=709:709)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   60 | [710](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=710:710)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   61 | [711](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=711:711)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   62 | [712](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=712:712)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   63 | [713](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=713:713)    | CL:0001035 | bone cell | bone cell     | UBERON:0004612 | mammalian cervical vertebra 3           | cervical vertebra 3                          |
|   64 | [699](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=699:699)    | CL:0001035 | bone cell | bone cell     | UBERON:0001093 | vertebral bone 2                        | cervical vertebra 2                          |
|   65 | [683](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=683:683)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|   66 | [748](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=748:748)    | CL:0001035 | bone cell | bone cell     | UBERON:0004614 | mammalian cervical vertebra 5           | cervical vertebra 5                          |
|   67 | [750](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=750:750)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|   68 | [785](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=785:785)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   69 | [786](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=786:786)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   70 | [787](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=787:787)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   71 | [788](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=788:788)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   72 | [789](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=789:789)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   73 | [790](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=790:790)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   74 | [791](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=791:791)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   75 | [792](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=792:792)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   76 | [793](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=793:793)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   77 | [794](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=794:794)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   78 | [795](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=795:795)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   79 | [796](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=796:796)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   80 | [797](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=797:797)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   81 | [798](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=798:798)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   82 | [799](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=799:799)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   83 | [800](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=800:800)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   84 | [801](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=801:801)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   85 | [802](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=802:802)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   86 | [803](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=803:803)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   87 | [804](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=804:804)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   88 | [805](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=805:805)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   89 | [806](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=806:806)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   90 | [807](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=807:807)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   91 | [808](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=808:808)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   92 | [809](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=809:809)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   93 | [810](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=810:810)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   94 | [811](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=811:811)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   95 | [812](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=812:812)    | CL:0001035 | bone cell | bone cell     | UBERON:0004618 | lumbar vertebra 2                       | lumbar vertebra 2                            |
|   96 | [813](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=813:813)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|   97 | [784](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=784:784)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   98 | [783](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=783:783)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|   99 | [782](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=782:782)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|  100 | [781](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=781:781)    | CL:0001035 | bone cell | bone cell     | UBERON:0004617 | lumbar vertebra 1                       | lumbar vertebra 1                            |
|  101 | [751](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=751:751)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  102 | [752](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=752:752)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  103 | [753](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=753:753)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  104 | [754](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=754:754)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  105 | [755](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=755:755)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  106 | [756](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=756:756)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  107 | [757](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=757:757)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  108 | [758](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=758:758)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  109 | [759](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=759:759)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  110 | [760](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=760:760)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  111 | [761](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=761:761)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  112 | [762](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=762:762)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  113 | [763](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=763:763)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  114 | [764](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=764:764)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  115 | [749](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=749:749)    | CL:0001035 | bone cell | bone cell     | UBERON:0004615 | mammalian cervical vertebra 6           | cervical vertebra 6                          |
|  116 | [765](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=765:765)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  117 | [767](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=767:767)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  118 | [768](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=768:768)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  119 | [769](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=769:769)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  120 | [770](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=770:770)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  121 | [771](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=771:771)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  122 | [772](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=772:772)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  123 | [773](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=773:773)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  124 | [774](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=774:774)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  125 | [775](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=775:775)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  126 | [776](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=776:776)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  127 | [777](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=777:777)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  128 | [778](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=778:778)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  129 | [779](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=779:779)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  130 | [780](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=780:780)    | CL:0001035 | bone cell | bone cell     | UBERON:0002414 | lumbar vertebra                         | lumbar vertebra                              |
|  131 | [766](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=766:766)    | CL:0001035 | bone cell | bone cell     | UBERON:0004616 | mammalian cervical vertebra 7           | cervical vertebra 7                          |
|  132 | [814](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=814:814)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  133 | [682](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=682:682)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  134 | [680](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=680:680)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  135 | [584](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=584:584)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  136 | [585](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=585:585)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  137 | [586](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=586:586)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  138 | [587](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=587:587)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  139 | [588](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=588:588)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  140 | [589](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=589:589)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  141 | [590](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=590:590)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  142 | [591](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=591:591)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  143 | [592](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=592:592)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  144 | [593](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=593:593)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  145 | [594](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=594:594)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  146 | [595](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=595:595)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  147 | [596](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=596:596)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  148 | [597](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=597:597)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  149 | [598](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=598:598)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  150 | [599](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=599:599)    | CL:0001035 | bone cell | bone cell     | UBERON:0004605 | rib 5                                   | rib 5                                        |
|  151 | [600](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=600:600)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  152 | [601](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=601:601)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  153 | [602](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=602:602)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  154 | [603](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=603:603)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  155 | [604](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=604:604)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  156 | [605](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=605:605)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  157 | [606](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=606:606)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  158 | [607](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=607:607)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  159 | [608](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=608:608)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  160 | [609](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=609:609)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  161 | [610](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=610:610)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  162 | [611](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=611:611)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  163 | [612](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=612:612)    | CL:0001035 | bone cell | bone cell     | UBERON:0004606 | rib 6                                   | rib 6                                        |
|  164 | [583](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=583:583)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  165 | [582](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=582:582)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  166 | [581](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=581:581)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  167 | [580](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=580:580)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  168 | [550](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=550:550)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  169 | [551](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=551:551)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  170 | [552](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=552:552)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  171 | [553](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=553:553)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  172 | [554](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=554:554)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  173 | [555](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=555:555)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  174 | [556](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=556:556)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  175 | [557](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=557:557)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  176 | [558](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=558:558)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  177 | [559](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=559:559)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  178 | [560](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=560:560)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  179 | [561](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=561:561)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  180 | [562](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=562:562)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  181 | [563](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=563:563)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  182 | [613](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=613:613)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  183 | [564](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=564:564)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  184 | [566](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=566:566)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  185 | [567](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=567:567)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  186 | [568](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=568:568)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  187 | [569](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=569:569)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  188 | [570](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=570:570)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  189 | [571](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=571:571)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  190 | [572](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=572:572)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  191 | [573](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=573:573)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  192 | [574](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=574:574)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  193 | [575](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=575:575)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  194 | [576](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=576:576)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  195 | [577](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=577:577)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  196 | [578](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=578:578)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  197 | [579](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=579:579)    | CL:0001035 | bone cell | bone cell     | UBERON:0004604 | rib 4                                   | rib 4                                        |
|  198 | [565](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=565:565)    | CL:0001035 | bone cell | bone cell     | UBERON:0004603 | rib 3                                   | rib 3                                        |
|  199 | [681](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=681:681)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  200 | [614](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=614:614)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  201 | [616](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=616:616)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  202 | [651](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=651:651)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  203 | [652](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=652:652)    | CL:0001035 | bone cell | bone cell     | UBERON:0014477 | thoracic skeleton                       | thoracic skeleton                            |
|  204 | [653](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=653:653)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |
|  205 | [654](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=654:654)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |
|  206 | [655](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=655:655)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |
|  207 | [656](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=656:656)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |
|  208 | [657](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=657:657)    | CL:0001035 | bone cell | bone cell     | UBERON:0002205 | manubrium of sternum                    | manubrium of sternum                         |
|  209 | [658](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=658:658)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |
|  210 | [659](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=659:659)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |
|  211 | [660](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=660:660)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |
|  212 | [661](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=661:661)    | CL:0001035 | bone cell | bone cell     | UBERON:0000975 | sternum                                 | sternum                                      |
|  213 | [662](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=662:662)    | CL:0001035 | bone cell | bone cell     | UBERON:0001130 | vertebral column                        | vertebral column                             |
|  214 | [663](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=663:663)    | CL:0001035 | bone cell | bone cell     | UBERON:0001095 | caudal vertebra                         | caudal vertebra                              |
|  215 | [664](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=664:664)    | CL:0001035 | bone cell | bone cell     | UBERON:0001350 | coccyx                                  | coccyx                                       |
|  216 | [665](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=665:665)    | CL:0001035 | bone cell | bone cell     | UBERON:0001350 | coccyx                                  | coccyx                                       |
|  217 | [666](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=666:666)    | CL:0001035 | bone cell | bone cell     | UBERON:0001350 | coccyx                                  | coccyx                                       |
|  218 | [667](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=667:667)    | CL:0001035 | bone cell | bone cell     | UBERON:0002413 | cervical vertebra                       | cervical vertebra                            |
|  219 | [668](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=668:668)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  220 | [669](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=669:669)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  221 | [670](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=670:670)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  222 | [671](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=671:671)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  223 | [672](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=672:672)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  224 | [673](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=673:673)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  225 | [674](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=674:674)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  226 | [675](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=675:675)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  227 | [676](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=676:676)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  228 | [677](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=677:677)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  229 | [678](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=678:678)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  230 | [679](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=679:679)    | CL:0001035 | bone cell | bone cell     | UBERON:0001092 | vertebral bone 1                        | cervical vertebra 1                          |
|  231 | [650](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=650:650)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  232 | [649](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=649:649)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  233 | [648](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=648:648)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  234 | [647](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=647:647)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  235 | [617](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=617:617)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  236 | [618](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=618:618)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  237 | [619](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=619:619)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  238 | [620](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=620:620)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  239 | [621](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=621:621)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  240 | [622](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=622:622)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  241 | [623](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=623:623)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  242 | [624](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=624:624)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  243 | [625](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=625:625)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  244 | [626](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=626:626)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  245 | [627](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=627:627)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  246 | [628](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=628:628)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  247 | [629](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=629:629)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  248 | [630](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=630:630)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  249 | [615](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=615:615)    | CL:0001035 | bone cell | bone cell     | UBERON:0004607 | rib 7                                   | rib 7                                        |
|  250 | [631](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=631:631)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  251 | [633](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=633:633)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  252 | [634](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=634:634)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  253 | [635](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=635:635)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  254 | [636](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=636:636)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  255 | [637](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=637:637)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  256 | [638](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=638:638)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  257 | [639](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=639:639)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  258 | [640](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=640:640)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  259 | [641](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=641:641)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  260 | [642](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=642:642)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  261 | [643](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=643:643)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  262 | [644](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=644:644)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  263 | [645](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=645:645)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  264 | [646](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=646:646)    | CL:0001035 | bone cell | bone cell     | UBERON:0004608 | rib 9                                   | rib 9                                        |
|  265 | [632](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=632:632)    | CL:0001035 | bone cell | bone cell     | UBERON:0010757 | rib 8                                   | rib 8                                        |
|  266 | [549](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=549:549)    | CL:0001035 | bone cell | bone cell     | UBERON:0004602 | rib 2                                   | rib 2                                        |
|  267 | [815](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=815:815)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  268 | [817](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=817:817)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  269 | [986](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=986:986)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  270 | [987](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=987:987)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  271 | [988](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=988:988)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  272 | [989](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=989:989)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  273 | [990](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=990:990)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  274 | [991](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=991:991)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  275 | [992](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=992:992)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  276 | [993](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=993:993)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  277 | [994](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=994:994)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  278 | [995](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=995:995)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  279 | [996](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=996:996)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  280 | [997](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=997:997)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  281 | [998](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=998:998)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  282 | [999](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=999:999)    | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  283 | [1000](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1000:1000) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  284 | [1001](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1001:1001) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  285 | [1002](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1002:1002) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  286 | [1003](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1003:1003) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  287 | [1004](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1004:1004) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  288 | [1005](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1005:1005) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  289 | [1006](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1006:1006) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  290 | [1007](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1007:1007) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  291 | [1008](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1008:1008) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  292 | [1009](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1009:1009) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  293 | [1010](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1010:1010) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  294 | [1011](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1011:1011) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  295 | [1012](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1012:1012) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  296 | [1013](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1013:1013) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  297 | [1014](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1014:1014) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  298 | [985](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=985:985)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  299 | [984](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=984:984)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  300 | [983](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=983:983)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  301 | [982](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=982:982)    | CL:0001035 | bone cell | bone cell     | UBERON:0004629 | thoracic vertebra 4                     | thoracic vertebra 4                          |
|  302 | [952](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=952:952)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  303 | [953](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=953:953)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  304 | [954](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=954:954)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  305 | [955](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=955:955)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  306 | [956](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=956:956)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  307 | [957](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=957:957)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  308 | [958](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=958:958)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  309 | [959](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=959:959)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  310 | [960](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=960:960)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  311 | [961](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=961:961)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  312 | [962](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=962:962)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  313 | [963](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=963:963)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  314 | [964](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=964:964)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  315 | [965](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=965:965)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  316 | [1015](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1015:1015) | CL:0001035 | bone cell | bone cell     | UBERON:0004630 | thoracic vertebra 5                     | thoracic vertebra 5                          |
|  317 | [966](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=966:966)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  318 | [968](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=968:968)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  319 | [969](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=969:969)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  320 | [970](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=970:970)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  321 | [971](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=971:971)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  322 | [972](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=972:972)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  323 | [973](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=973:973)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  324 | [974](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=974:974)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  325 | [975](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=975:975)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  326 | [976](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=976:976)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  327 | [977](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=977:977)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  328 | [978](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=978:978)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  329 | [979](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=979:979)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  330 | [980](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=980:980)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  331 | [981](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=981:981)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  332 | [967](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=967:967)    | CL:0001035 | bone cell | bone cell     | UBERON:0004628 | thoracic vertebra 3                     | thoracic vertebra 3                          |
|  333 | [951](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=951:951)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  334 | [1016](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1016:1016) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  335 | [1018](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1018:1018) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  336 | [1053](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1053:1053) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  337 | [1054](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1054:1054) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  338 | [1055](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1055:1055) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  339 | [1056](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1056:1056) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  340 | [1057](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1057:1057) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  341 | [1058](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1058:1058) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  342 | [1059](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1059:1059) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  343 | [1060](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1060:1060) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  344 | [1061](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1061:1061) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  345 | [1062](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1062:1062) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  346 | [1063](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1063:1063) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  347 | [1064](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1064:1064) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  348 | [1065](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1065:1065) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  349 | [1066](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1066:1066) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  350 | [1067](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1067:1067) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  351 | [1068](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1068:1068) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  352 | [1069](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1069:1069) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  353 | [1070](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1070:1070) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  354 | [1071](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1071:1071) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  355 | [1072](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1072:1072) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  356 | [1073](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1073:1073) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  357 | [1074](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1074:1074) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  358 | [1075](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1075:1075) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  359 | [1076](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1076:1076) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  360 | [1077](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1077:1077) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  361 | [1078](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1078:1078) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  362 | [1079](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1079:1079) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  363 | [1080](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1080:1080) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  364 | [1081](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1081:1081) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
|  365 | [1052](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1052:1052) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  366 | [1051](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1051:1051) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  367 | [1050](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1050:1050) | CL:0001035 | bone cell | bone cell     | UBERON:0011050 | thoracic vertebra 8                     | thoracic vertebra 8                          |
|  368 | [1049](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1049:1049) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  369 | [1019](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1019:1019) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  370 | [1020](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1020:1020) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  371 | [1021](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1021:1021) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  372 | [1022](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1022:1022) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  373 | [1023](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1023:1023) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  374 | [1024](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1024:1024) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  375 | [1025](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1025:1025) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  376 | [1026](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1026:1026) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  377 | [1027](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1027:1027) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  378 | [1028](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1028:1028) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  379 | [1029](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1029:1029) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  380 | [1030](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1030:1030) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  381 | [1031](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1031:1031) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  382 | [1032](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1032:1032) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  383 | [1017](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1017:1017) | CL:0001035 | bone cell | bone cell     | UBERON:0004631 | thoracic vertebra 6                     | thoracic vertebra 6                          |
|  384 | [1033](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1033:1033) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  385 | [1035](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1035:1035) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  386 | [1036](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1036:1036) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  387 | [1037](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1037:1037) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  388 | [1038](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1038:1038) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  389 | [1039](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1039:1039) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  390 | [1040](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1040:1040) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  391 | [1041](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1041:1041) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  392 | [1042](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1042:1042) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  393 | [1043](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1043:1043) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  394 | [1044](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1044:1044) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  395 | [1045](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1045:1045) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  396 | [1046](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1046:1046) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  397 | [1047](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1047:1047) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  398 | [1048](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1048:1048) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  399 | [1034](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1034:1034) | CL:0001035 | bone cell | bone cell     | UBERON:0004632 | thoracic vertebra 7                     | thoracic vertebra 7                          |
|  400 | [816](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=816:816)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  401 | [950](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=950:950)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  402 | [948](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=948:948)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  403 | [852](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=852:852)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  404 | [853](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=853:853)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  405 | [854](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=854:854)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  406 | [855](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=855:855)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  407 | [856](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=856:856)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  408 | [857](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=857:857)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  409 | [858](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=858:858)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  410 | [859](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=859:859)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  411 | [860](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=860:860)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  412 | [861](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=861:861)    | CL:0001035 | bone cell | bone cell     | UBERON:0001094 | sacral vertebra                         | sacral vertebra                              |
|  413 | [862](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=862:862)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  414 | [863](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=863:863)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  415 | [864](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=864:864)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  416 | [865](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=865:865)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  417 | [866](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=866:866)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  418 | [867](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=867:867)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  419 | [868](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=868:868)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  420 | [869](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=869:869)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  421 | [870](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=870:870)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  422 | [871](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=871:871)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  423 | [872](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=872:872)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  424 | [873](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=873:873)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  425 | [874](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=874:874)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  426 | [875](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=875:875)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  427 | [876](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=876:876)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  428 | [877](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=877:877)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  429 | [878](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=878:878)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  430 | [879](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=879:879)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  431 | [880](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=880:880)    | CL:0001035 | bone cell | bone cell     | UBERON:0003690 | fused sacrum                            | sacrum                                       |
|  432 | [851](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=851:851)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  433 | [850](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=850:850)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  434 | [849](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=849:849)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  435 | [848](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=848:848)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  436 | [818](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=818:818)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  437 | [819](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=819:819)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  438 | [820](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=820:820)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  439 | [821](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=821:821)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  440 | [822](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=822:822)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  441 | [823](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=823:823)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  442 | [824](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=824:824)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  443 | [825](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=825:825)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  444 | [826](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=826:826)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  445 | [827](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=827:827)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  446 | [828](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=828:828)    | CL:0001035 | bone cell | bone cell     | UBERON:0004619 | lumbar vertebra 3                       | lumbar vertebra 3                            |
|  447 | [829](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=829:829)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  448 | [830](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=830:830)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  449 | [831](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=831:831)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  450 | [881](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=881:881)    | CL:0001035 | bone cell | bone cell     | UBERON:0002347 | thoracic vertebra                       | thoracic vertebra                            |
|  451 | [832](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=832:832)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  452 | [834](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=834:834)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  453 | [835](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=835:835)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  454 | [836](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=836:836)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  455 | [837](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=837:837)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  456 | [838](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=838:838)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  457 | [839](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=839:839)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  458 | [840](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=840:840)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  459 | [841](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=841:841)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  460 | [842](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=842:842)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  461 | [843](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=843:843)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  462 | [844](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=844:844)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  463 | [845](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=845:845)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  464 | [846](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=846:846)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  465 | [847](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=847:847)    | CL:0001035 | bone cell | bone cell     | UBERON:0004621 | lumbar vertebra 5                       | lumbar vertebra 5                            |
|  466 | [833](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=833:833)    | CL:0001035 | bone cell | bone cell     | UBERON:0004620 | lumbar vertebra 4                       | lumbar vertebra 4                            |
|  467 | [949](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=949:949)    | CL:0001035 | bone cell | bone cell     | UBERON:0004627 | thoracic vertebra 2                     | thoracic vertebra 2                          |
|  468 | [882](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=882:882)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  469 | [884](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=884:884)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  470 | [919](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=919:919)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  471 | [920](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=920:920)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  472 | [921](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=921:921)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  473 | [922](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=922:922)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  474 | [923](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=923:923)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  475 | [924](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=924:924)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  476 | [925](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=925:925)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  477 | [926](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=926:926)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  478 | [927](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=927:927)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  479 | [928](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=928:928)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  480 | [929](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=929:929)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  481 | [930](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=930:930)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  482 | [931](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=931:931)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  483 | [932](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=932:932)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  484 | [933](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=933:933)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  485 | [934](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=934:934)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  486 | [935](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=935:935)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  487 | [936](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=936:936)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  488 | [937](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=937:937)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  489 | [938](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=938:938)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  490 | [939](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=939:939)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  491 | [940](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=940:940)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  492 | [941](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=941:941)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  493 | [942](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=942:942)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  494 | [943](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=943:943)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  495 | [944](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=944:944)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  496 | [945](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=945:945)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  497 | [946](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=946:946)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  498 | [947](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=947:947)    | CL:0001035 | bone cell | bone cell     | UBERON:0004636 | thoracic vertebra 12                    | thoracic vertebra 12                         |
|  499 | [918](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=918:918)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  500 | [917](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=917:917)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  501 | [916](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=916:916)    | CL:0001035 | bone cell | bone cell     | UBERON:0004635 | thoracic vertebra 11                    | thoracic vertebra 11                         |
|  502 | [915](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=915:915)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  503 | [885](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=885:885)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  504 | [886](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=886:886)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  505 | [887](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=887:887)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  506 | [888](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=888:888)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  507 | [889](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=889:889)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  508 | [890](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=890:890)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  509 | [891](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=891:891)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  510 | [892](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=892:892)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  511 | [893](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=893:893)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  512 | [894](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=894:894)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  513 | [895](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=895:895)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  514 | [896](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=896:896)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  515 | [897](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=897:897)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  516 | [898](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=898:898)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  517 | [883](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=883:883)    | CL:0001035 | bone cell | bone cell     | UBERON:0004626 | thoracic vertebra 1                     | thoracic vertebra 1                          |
|  518 | [899](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=899:899)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  519 | [901](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=901:901)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  520 | [902](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=902:902)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  521 | [903](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=903:903)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  522 | [904](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=904:904)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  523 | [905](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=905:905)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  524 | [906](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=906:906)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  525 | [907](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=907:907)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  526 | [908](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=908:908)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  527 | [909](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=909:909)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  528 | [910](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=910:910)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  529 | [911](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=911:911)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  530 | [912](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=912:912)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  531 | [913](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=913:913)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  532 | [914](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=914:914)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  533 | [900](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=900:900)    | CL:0001035 | bone cell | bone cell     | UBERON:0004634 | thoracic vertebra 10                    | thoracic vertebra 10                         |
|  534 | [548](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=548:548)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |
|  535 | [547](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=547:547)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |
|  536 | [546](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=546:546)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |
|  537 | [181](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=181:181)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  538 | [182](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=182:182)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  539 | [183](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=183:183)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  540 | [184](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=184:184)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  541 | [185](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=185:185)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  542 | [186](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=186:186)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  543 | [187](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=187:187)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  544 | [188](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=188:188)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  545 | [189](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=189:189)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  546 | [190](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=190:190)    | CL:0001035 | bone cell | bone cell     | UBERON:0001455 | cuboid bone                             | cuboid bone                                  |
|  547 | [191](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=191:191)    | CL:0001035 | bone cell | bone cell     | UBERON:0001455 | cuboid bone                             | cuboid bone                                  |
|  548 | [192](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=192:192)    | CL:0001035 | bone cell | bone cell     | UBERON:0001455 | cuboid bone                             | cuboid bone                                  |
|  549 | [193](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=193:193)    | CL:0001035 | bone cell | bone cell     | UBERON:0004315 | distal phalanx of pedal digit 1         | distal phalanx of digit of foot 1            |
|  550 | [194](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=194:194)    | CL:0001035 | bone cell | bone cell     | UBERON:0004315 | distal phalanx of pedal digit 1         | distal phalanx of digit of foot 1            |
|  551 | [195](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=195:195)    | CL:0001035 | bone cell | bone cell     | UBERON:0004315 | distal phalanx of pedal digit 1         | distal phalanx of digit of foot 1            |
|  552 | [196](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=196:196)    | CL:0001035 | bone cell | bone cell     | UBERON:0004315 | distal phalanx of pedal digit 1         | distal phalanx of digit of foot 1            |
|  553 | [197](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=197:197)    | CL:0001035 | bone cell | bone cell     | UBERON:0004316 | distal phalanx of pedal digit 2         | distal phalanx of digit of foot 2            |
|  554 | [198](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=198:198)    | CL:0001035 | bone cell | bone cell     | UBERON:0004316 | distal phalanx of pedal digit 2         | distal phalanx of digit of foot 2            |
|  555 | [199](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=199:199)    | CL:0001035 | bone cell | bone cell     | UBERON:0004316 | distal phalanx of pedal digit 2         | distal phalanx of digit of foot 2            |
|  556 | [200](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=200:200)    | CL:0001035 | bone cell | bone cell     | UBERON:0004316 | distal phalanx of pedal digit 2         | distal phalanx of digit of foot 2            |
|  557 | [201](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=201:201)    | CL:0001035 | bone cell | bone cell     | UBERON:0004317 | distal phalanx of pedal digit 3         | distal phalanx of digit of foot 3            |
|  558 | [202](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=202:202)    | CL:0001035 | bone cell | bone cell     | UBERON:0004317 | distal phalanx of pedal digit 3         | distal phalanx of digit of foot 3            |
|  559 | [203](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=203:203)    | CL:0001035 | bone cell | bone cell     | UBERON:0004317 | distal phalanx of pedal digit 3         | distal phalanx of digit of foot 3            |
|  560 | [204](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=204:204)    | CL:0001035 | bone cell | bone cell     | UBERON:0004317 | distal phalanx of pedal digit 3         | distal phalanx of digit of foot 3            |
|  561 | [205](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=205:205)    | CL:0001035 | bone cell | bone cell     | UBERON:0004318 | distal phalanx of pedal digit 4         | distal phalanx of digit of foot 4            |
|  562 | [206](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=206:206)    | CL:0001035 | bone cell | bone cell     | UBERON:0004318 | distal phalanx of pedal digit 4         | distal phalanx of digit of foot 4            |
|  563 | [207](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=207:207)    | CL:0001035 | bone cell | bone cell     | UBERON:0004318 | distal phalanx of pedal digit 4         | distal phalanx of digit of foot 4            |
|  564 | [208](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=208:208)    | CL:0001035 | bone cell | bone cell     | UBERON:0004318 | distal phalanx of pedal digit 4         | distal phalanx of digit of foot 4            |
|  565 | [209](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=209:209)    | CL:0001035 | bone cell | bone cell     | UBERON:0004319 | distal phalanx of pedal digit 5         | distal phalanx of digit of foot 5            |
|  566 | [180](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=180:180)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  567 | [179](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=179:179)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  568 | [178](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=178:178)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  569 | [177](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=177:177)    | CL:0001035 | bone cell | bone cell     | UBERON:0001450 | calcaneus                               | calcaneus                                    |
|  570 | [147](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=147:147)    | CL:0001035 | bone cell | bone cell     | UBERON:0007829 | pectoral girdle bone                    | pectoral girdle bone                         |
|  571 | [148](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=148:148)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                |
|  572 | [149](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=149:149)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                |
|  573 | [150](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=150:150)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                |
|  574 | [151](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=151:151)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                |
|  575 | [152](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=152:152)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                |
|  576 | [153](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=153:153)    | CL:0001035 | bone cell | bone cell     | UBERON:0006805 | sternal end of clavicle                 | sternal end of clavicle                      |
|  577 | [154](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=154:154)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                |
|  578 | [155](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=155:155)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                |
|  579 | [156](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=156:156)    | CL:0001035 | bone cell | bone cell     | UBERON:0001105 | clavicle bone                           | clavicle bone                                |
|  580 | [157](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=157:157)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  581 | [158](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=158:158)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  582 | [159](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=159:159)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  583 | [160](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=160:160)    | CL:0001035 | bone cell | bone cell     | UBERON:0006633 | coracoid process of scapula             | coracoid process of scapula                  |
|  584 | [210](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=210:210)    | CL:0001035 | bone cell | bone cell     | UBERON:0004319 | distal phalanx of pedal digit 5         | distal phalanx of digit of foot 5            |
|  585 | [161](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=161:161)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  586 | [163](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=163:163)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  587 | [164](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=164:164)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  588 | [165](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=165:165)    | CL:0001035 | bone cell | bone cell     | UBERON:0007173 | lateral border of scapula               | lateral border of scapula                    |
|  589 | [166](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=166:166)    | CL:0001035 | bone cell | bone cell     | UBERON:0007174 | medial border of scapula                | medial border of scapula                     |
|  590 | [167](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=167:167)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  591 | [168](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=168:168)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  592 | [169](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=169:169)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  593 | [170](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=170:170)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  594 | [171](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=171:171)    | CL:0001035 | bone cell | bone cell     | UBERON:0007176 | superior angle of scapula               | superior angle of scapula                    |
|  595 | [172](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=172:172)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  596 | [173](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=173:173)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  597 | [174](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=174:174)    | CL:0001035 | bone cell | bone cell     | UBERON:0006849 | scapula                                 | scapula                                      |
|  598 | [175](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=175:175)    | CL:0001035 | bone cell | bone cell     | UBERON:0005893 | leg bone                                | leg bone                                     |
|  599 | [176](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=176:176)    | CL:0001035 | bone cell | bone cell     | UBERON:0005899 | pes bone                                | foot bone                                    |
|  600 | [162](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=162:162)    | CL:0001035 | bone cell | bone cell     | UBERON:0007175 | inferior angle of scapula               | inferior angle of scapula                    |
|  601 | [146](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=146:146)    | CL:0001035 | bone cell | bone cell     | UBERON:0002445 | ulnare                                  | ulnare                                       |
|  602 | [211](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=211:211)    | CL:0001035 | bone cell | bone cell     | UBERON:0004319 | distal phalanx of pedal digit 5         | distal phalanx of digit of foot 5            |
|  603 | [213](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=213:213)    | CL:0001035 | bone cell | bone cell     | UBERON:0001452 | distal tarsal bone 1                    | distal tarsal bone 1                         |
|  604 | [248](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=248:248)    | CL:0001035 | bone cell | bone cell     | UBERON:0004326 | middle phalanx of pedal digit 4         | middle phalanx of digit of foot 4            |
|  605 | [249](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=249:249)    | CL:0001035 | bone cell | bone cell     | UBERON:0004327 | middle phalanx of pedal digit 5         | middle phalanx of digit of foot 5            |
|  606 | [250](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=250:250)    | CL:0001035 | bone cell | bone cell     | UBERON:0004327 | middle phalanx of pedal digit 5         | middle phalanx of digit of foot 5            |
|  607 | [251](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=251:251)    | CL:0001035 | bone cell | bone cell     | UBERON:0004327 | middle phalanx of pedal digit 5         | middle phalanx of digit of foot 5            |
|  608 | [252](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=252:252)    | CL:0001035 | bone cell | bone cell     | UBERON:0004327 | middle phalanx of pedal digit 5         | middle phalanx of digit of foot 5            |
|  609 | [253](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=253:253)    | CL:0001035 | bone cell | bone cell     | UBERON:0001451 | navicular bone of pes                   | navicular bone of foot                       |
|  610 | [254](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=254:254)    | CL:0001035 | bone cell | bone cell     | UBERON:0001451 | navicular bone of pes                   | navicular bone of foot                       |
|  611 | [255](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=255:255)    | CL:0001035 | bone cell | bone cell     | UBERON:0004332 | proximal phalanx of pedal digit 1       | proximal phalanx of digit of foot 1          |
|  612 | [256](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=256:256)    | CL:0001035 | bone cell | bone cell     | UBERON:0004332 | proximal phalanx of pedal digit 1       | proximal phalanx of digit of foot 1          |
|  613 | [257](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=257:257)    | CL:0001035 | bone cell | bone cell     | UBERON:0004332 | proximal phalanx of pedal digit 1       | proximal phalanx of digit of foot 1          |
|  614 | [258](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=258:258)    | CL:0001035 | bone cell | bone cell     | UBERON:0004332 | proximal phalanx of pedal digit 1       | proximal phalanx of digit of foot 1          |
|  615 | [259](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=259:259)    | CL:0001035 | bone cell | bone cell     | UBERON:0004333 | proximal phalanx of pedal digit 2       | proximal phalanx of digit of foot 2          |
|  616 | [260](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=260:260)    | CL:0001035 | bone cell | bone cell     | UBERON:0004333 | proximal phalanx of pedal digit 2       | proximal phalanx of digit of foot 2          |
|  617 | [261](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=261:261)    | CL:0001035 | bone cell | bone cell     | UBERON:0004333 | proximal phalanx of pedal digit 2       | proximal phalanx of digit of foot 2          |
|  618 | [262](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=262:262)    | CL:0001035 | bone cell | bone cell     | UBERON:0004333 | proximal phalanx of pedal digit 2       | proximal phalanx of digit of foot 2          |
|  619 | [263](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=263:263)    | CL:0001035 | bone cell | bone cell     | UBERON:0004334 | proximal phalanx of pedal digit 3       | proximal phalanx of digit of foot 3          |
|  620 | [264](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=264:264)    | CL:0001035 | bone cell | bone cell     | UBERON:0004334 | proximal phalanx of pedal digit 3       | proximal phalanx of digit of foot 3          |
|  621 | [265](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=265:265)    | CL:0001035 | bone cell | bone cell     | UBERON:0004334 | proximal phalanx of pedal digit 3       | proximal phalanx of digit of foot 3          |
|  622 | [266](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=266:266)    | CL:0001035 | bone cell | bone cell     | UBERON:0004334 | proximal phalanx of pedal digit 3       | proximal phalanx of digit of foot 3          |
|  623 | [267](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=267:267)    | CL:0001035 | bone cell | bone cell     | UBERON:0004335 | proximal phalanx of pedal digit 4       | proximal phalanx of digit of foot 4          |
|  624 | [268](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=268:268)    | CL:0001035 | bone cell | bone cell     | UBERON:0004335 | proximal phalanx of pedal digit 4       | proximal phalanx of digit of foot 4          |
|  625 | [269](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=269:269)    | CL:0001035 | bone cell | bone cell     | UBERON:0004335 | proximal phalanx of pedal digit 4       | proximal phalanx of digit of foot 4          |
|  626 | [270](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=270:270)    | CL:0001035 | bone cell | bone cell     | UBERON:0004335 | proximal phalanx of pedal digit 4       | proximal phalanx of digit of foot 4          |
|  627 | [271](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=271:271)    | CL:0001035 | bone cell | bone cell     | UBERON:0004336 | proximal phalanx of pedal digit 5       | proximal phalanx of digit of foot 5          |
|  628 | [272](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=272:272)    | CL:0001035 | bone cell | bone cell     | UBERON:0004336 | proximal phalanx of pedal digit 5       | proximal phalanx of digit of foot 5          |
|  629 | [273](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=273:273)    | CL:0001035 | bone cell | bone cell     | UBERON:0004336 | proximal phalanx of pedal digit 5       | proximal phalanx of digit of foot 5          |
|  630 | [274](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=274:274)    | CL:0001035 | bone cell | bone cell     | UBERON:0004336 | proximal phalanx of pedal digit 5       | proximal phalanx of digit of foot 5          |
|  631 | [275](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=275:275)    | CL:0001035 | bone cell | bone cell     | UBERON:0002395 | talus                                   | talus                                        |
|  632 | [276](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=276:276)    | CL:0001035 | bone cell | bone cell     | UBERON:0002395 | talus                                   | talus                                        |
|  633 | [247](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=247:247)    | CL:0001035 | bone cell | bone cell     | UBERON:0004326 | middle phalanx of pedal digit 4         | middle phalanx of digit of foot 4            |
|  634 | [246](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=246:246)    | CL:0001035 | bone cell | bone cell     | UBERON:0004326 | middle phalanx of pedal digit 4         | middle phalanx of digit of foot 4            |
|  635 | [245](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=245:245)    | CL:0001035 | bone cell | bone cell     | UBERON:0004326 | middle phalanx of pedal digit 4         | middle phalanx of digit of foot 4            |
|  636 | [244](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=244:244)    | CL:0001035 | bone cell | bone cell     | UBERON:0004325 | middle phalanx of pedal digit 3         | middle phalanx of digit of foot 3            |
|  637 | [214](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=214:214)    | CL:0001035 | bone cell | bone cell     | UBERON:0001453 | distal tarsal bone 2                    | distal tarsal bone 2                         |
|  638 | [215](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=215:215)    | CL:0001035 | bone cell | bone cell     | UBERON:0001454 | distal tarsal bone 3                    | distal tarsal bone 3                         |
|  639 | [216](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=216:216)    | CL:0001035 | bone cell | bone cell     | UBERON:0003650 | metatarsal bone of digit 1              | metatarsal bone of digit 1                   |
|  640 | [217](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=217:217)    | CL:0001035 | bone cell | bone cell     | UBERON:0003650 | metatarsal bone of digit 1              | metatarsal bone of digit 1                   |
|  641 | [218](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=218:218)    | CL:0001035 | bone cell | bone cell     | UBERON:0003650 | metatarsal bone of digit 1              | metatarsal bone of digit 1                   |
|  642 | [219](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=219:219)    | CL:0001035 | bone cell | bone cell     | UBERON:0003650 | metatarsal bone of digit 1              | metatarsal bone of digit 1                   |
|  643 | [220](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=220:220)    | CL:0001035 | bone cell | bone cell     | UBERON:0003651 | metatarsal bone of digit 2              | metatarsal bone of digit 2                   |
|  644 | [221](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=221:221)    | CL:0001035 | bone cell | bone cell     | UBERON:0003651 | metatarsal bone of digit 2              | metatarsal bone of digit 2                   |
|  645 | [222](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=222:222)    | CL:0001035 | bone cell | bone cell     | UBERON:0003651 | metatarsal bone of digit 2              | metatarsal bone of digit 2                   |
|  646 | [223](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=223:223)    | CL:0001035 | bone cell | bone cell     | UBERON:0003651 | metatarsal bone of digit 2              | metatarsal bone of digit 2                   |
|  647 | [224](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=224:224)    | CL:0001035 | bone cell | bone cell     | UBERON:0003652 | metatarsal bone of digit 3              | metatarsal bone of digit 3                   |
|  648 | [225](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=225:225)    | CL:0001035 | bone cell | bone cell     | UBERON:0003652 | metatarsal bone of digit 3              | metatarsal bone of digit 3                   |
|  649 | [226](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=226:226)    | CL:0001035 | bone cell | bone cell     | UBERON:0003652 | metatarsal bone of digit 3              | metatarsal bone of digit 3                   |
|  650 | [227](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=227:227)    | CL:0001035 | bone cell | bone cell     | UBERON:0003652 | metatarsal bone of digit 3              | metatarsal bone of digit 3                   |
|  651 | [212](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=212:212)    | CL:0001035 | bone cell | bone cell     | UBERON:0004319 | distal phalanx of pedal digit 5         | distal phalanx of digit of foot 5            |
|  652 | [228](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=228:228)    | CL:0001035 | bone cell | bone cell     | UBERON:0003653 | metatarsal bone of digit 4              | metatarsal bone of digit 4                   |
|  653 | [230](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=230:230)    | CL:0001035 | bone cell | bone cell     | UBERON:0003653 | metatarsal bone of digit 4              | metatarsal bone of digit 4                   |
|  654 | [231](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=231:231)    | CL:0001035 | bone cell | bone cell     | UBERON:0003653 | metatarsal bone of digit 4              | metatarsal bone of digit 4                   |
|  655 | [232](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=232:232)    | CL:0001035 | bone cell | bone cell     | UBERON:0003654 | metatarsal bone of digit 5              | metatarsal bone of digit 5                   |
|  656 | [233](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=233:233)    | CL:0001035 | bone cell | bone cell     | UBERON:0003654 | metatarsal bone of digit 5              | metatarsal bone of digit 5                   |
|  657 | [234](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=234:234)    | CL:0001035 | bone cell | bone cell     | UBERON:0003654 | metatarsal bone of digit 5              | metatarsal bone of digit 5                   |
|  658 | [235](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=235:235)    | CL:0001035 | bone cell | bone cell     | UBERON:0003654 | metatarsal bone of digit 5              | metatarsal bone of digit 5                   |
|  659 | [236](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=236:236)    | CL:0001035 | bone cell | bone cell     | UBERON:0003654 | metatarsal bone of digit 5              | metatarsal bone of digit 5                   |
|  660 | [237](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=237:237)    | CL:0001035 | bone cell | bone cell     | UBERON:0004324 | middle phalanx of pedal digit 2         | middle phalanx of digit of foot 2            |
|  661 | [238](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=238:238)    | CL:0001035 | bone cell | bone cell     | UBERON:0004324 | middle phalanx of pedal digit 2         | middle phalanx of digit of foot 2            |
|  662 | [239](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=239:239)    | CL:0001035 | bone cell | bone cell     | UBERON:0004324 | middle phalanx of pedal digit 2         | middle phalanx of digit of foot 2            |
|  663 | [240](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=240:240)    | CL:0001035 | bone cell | bone cell     | UBERON:0004324 | middle phalanx of pedal digit 2         | middle phalanx of digit of foot 2            |
|  664 | [241](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=241:241)    | CL:0001035 | bone cell | bone cell     | UBERON:0004325 | middle phalanx of pedal digit 3         | middle phalanx of digit of foot 3            |
|  665 | [242](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=242:242)    | CL:0001035 | bone cell | bone cell     | UBERON:0004325 | middle phalanx of pedal digit 3         | middle phalanx of digit of foot 3            |
|  666 | [243](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=243:243)    | CL:0001035 | bone cell | bone cell     | UBERON:0004325 | middle phalanx of pedal digit 3         | middle phalanx of digit of foot 3            |
|  667 | [229](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=229:229)    | CL:0001035 | bone cell | bone cell     | UBERON:0003653 | metatarsal bone of digit 4              | metatarsal bone of digit 4                   |
|  668 | [277](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=277:277)    | CL:0001035 | bone cell | bone cell     | UBERON:0002395 | talus                                   | talus                                        |
|  669 | [145](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=145:145)    | CL:0001035 | bone cell | bone cell     | UBERON:0001427 | radiale                                 | scaphoid                                     |
|  670 | [143](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=143:143)    | CL:0001035 | bone cell | bone cell     | UBERON:0004331 | proximal phalanx of manual digit 5      | proximal phalanx of digit of hand 5          |
|  671 | [47](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=47:47)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |
|  672 | [48](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=48:48)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |
|  673 | [49](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=49:49)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |
|  674 | [50](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=50:50)       | CL:0001035 | bone cell | bone cell     | UBERON:0011575 | styloid process of ulna                 | styloid process of ulna                      |
|  675 | [51](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=51:51)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |
|  676 | [52](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=52:52)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |
|  677 | [53](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=53:53)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |
|  678 | [54](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=54:54)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |
|  679 | [55](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=55:55)       | CL:0001035 | bone cell | bone cell     | UBERON:0005897 | manus bone                              | hand bone                                    |
|  680 | [56](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=56:56)       | CL:0001035 | bone cell | bone cell     | UBERON:0001430 | distal carpal bone 1                    | distal carpal bone 1                         |
|  681 | [57](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=57:57)       | CL:0001035 | bone cell | bone cell     | UBERON:0001431 | distal carpal bone 2                    | distal carpal bone 2                         |
|  682 | [58](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=58:58)       | CL:0001035 | bone cell | bone cell     | UBERON:0001432 | distal carpal bone 3                    | distal carpal bone 3                         |
|  683 | [59](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=59:59)       | CL:0001035 | bone cell | bone cell     | UBERON:0001433 | distal carpal bone 4                    | distal carpal bone 4                         |
|  684 | [60](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=60:60)       | CL:0001035 | bone cell | bone cell     | UBERON:0001433 | distal carpal bone 4                    | distal carpal bone 4                         |
|  685 | [61](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=61:61)       | CL:0001035 | bone cell | bone cell     | UBERON:0004337 | distal phalanx of manual digit 1        | distal phalanx of digit of hand 1            |
|  686 | [62](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=62:62)       | CL:0001035 | bone cell | bone cell     | UBERON:0004337 | distal phalanx of manual digit 1        | distal phalanx of digit of hand 1            |
|  687 | [63](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=63:63)       | CL:0001035 | bone cell | bone cell     | UBERON:0004337 | distal phalanx of manual digit 1        | distal phalanx of digit of hand 1            |
|  688 | [64](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=64:64)       | CL:0001035 | bone cell | bone cell     | UBERON:0004337 | distal phalanx of manual digit 1        | distal phalanx of digit of hand 1            |
|  689 | [65](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=65:65)       | CL:0001035 | bone cell | bone cell     | UBERON:0004337 | distal phalanx of manual digit 1        | distal phalanx of digit of hand 1            |
|  690 | [66](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=66:66)       | CL:0001035 | bone cell | bone cell     | UBERON:0004311 | distal phalanx of manual digit 2        | distal phalanx of digit of hand 2            |
|  691 | [67](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=67:67)       | CL:0001035 | bone cell | bone cell     | UBERON:0004311 | distal phalanx of manual digit 2        | distal phalanx of digit of hand 2            |
|  692 | [68](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=68:68)       | CL:0001035 | bone cell | bone cell     | UBERON:0004311 | distal phalanx of manual digit 2        | distal phalanx of digit of hand 2            |
|  693 | [69](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=69:69)       | CL:0001035 | bone cell | bone cell     | UBERON:0004311 | distal phalanx of manual digit 2        | distal phalanx of digit of hand 2            |
|  694 | [70](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=70:70)       | CL:0001035 | bone cell | bone cell     | UBERON:0004311 | distal phalanx of manual digit 2        | distal phalanx of digit of hand 2            |
|  695 | [71](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=71:71)       | CL:0001035 | bone cell | bone cell     | UBERON:0004312 | distal phalanx of manual digit 3        | distal phalanx of digit of hand 3            |
|  696 | [72](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=72:72)       | CL:0001035 | bone cell | bone cell     | UBERON:0004312 | distal phalanx of manual digit 3        | distal phalanx of digit of hand 3            |
|  697 | [73](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=73:73)       | CL:0001035 | bone cell | bone cell     | UBERON:0004312 | distal phalanx of manual digit 3        | distal phalanx of digit of hand 3            |
|  698 | [74](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=74:74)       | CL:0001035 | bone cell | bone cell     | UBERON:0004312 | distal phalanx of manual digit 3        | distal phalanx of digit of hand 3            |
|  699 | [75](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=75:75)       | CL:0001035 | bone cell | bone cell     | UBERON:0004312 | distal phalanx of manual digit 3        | distal phalanx of digit of hand 3            |
|  700 | [46](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=46:46)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |
|  701 | [45](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=45:45)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |
|  702 | [44](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=44:44)       | CL:0001035 | bone cell | bone cell     | UBERON:0010994 | coronoid process of ulna                | coronoid process of ulna                     |
|  703 | [43](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=43:43)       | CL:0001035 | bone cell | bone cell     | UBERON:0001424 | ulna                                    | ulna                                         |
|  704 | [13](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=13:13)       | CL:0001035 | bone cell | bone cell     | UBERON:0002091 | appendicular skeleton                   | appendicular skeleton                        |
|  705 | [14](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=14:14)       | CL:0001035 | bone cell | bone cell     | UBERON:0003460 | arm bone                                | arm bone                                     |
|  706 | [15](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=15:15)       | CL:0001035 | bone cell | bone cell     | UBERON:0003460 | arm bone                                | arm bone                                     |
|  707 | [16](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=16:16)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  708 | [17](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=17:17)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  709 | [18](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=18:18)       | CL:0001035 | bone cell | bone cell     | UBERON:0010853 | capitulum of humerus                    | capitulum of humerus                         |
|  710 | [19](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=19:19)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  711 | [20](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=20:20)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  712 | [21](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=21:21)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  713 | [22](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=22:22)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  714 | [23](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=23:23)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  715 | [24](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=24:24)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  716 | [25](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=25:25)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  717 | [26](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=26:26)       | CL:0001035 | bone cell | bone cell     | UBERON:0011188 | lesser tubercle of humerus              | lesser tubercle of humerus                   |
|  718 | [76](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=76:76)       | CL:0001035 | bone cell | bone cell     | UBERON:0004313 | distal phalanx of manual digit 4        | distal phalanx of digit of hand 4            |
|  719 | [27](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=27:27)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  720 | [29](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=29:29)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  721 | [30](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=30:30)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  722 | [31](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=31:31)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  723 | [32](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=32:32)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  724 | [33](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=33:33)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  725 | [34](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=34:34)       | CL:0001035 | bone cell | bone cell     | UBERON:0000144 | trochlea of humerus                     | trochlea of humerus                          |
|  726 | [35](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=35:35)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |
|  727 | [36](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=36:36)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |
|  728 | [37](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=37:37)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |
|  729 | [38](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=38:38)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |
|  730 | [39](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=39:39)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |
|  731 | [40](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=40:40)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |
|  732 | [41](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=41:41)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |
|  733 | [42](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=42:42)       | CL:0001035 | bone cell | bone cell     | UBERON:0001423 | radius bone                             | radius bone                                  |
|  734 | [28](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=28:28)       | CL:0001035 | bone cell | bone cell     | UBERON:0000976 | humerus                                 | humerus                                      |
|  735 | [144](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=144:144)    | CL:0001035 | bone cell | bone cell     | UBERON:0001427 | radiale                                 | scaphoid                                     |
|  736 | [77](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=77:77)       | CL:0001035 | bone cell | bone cell     | UBERON:0004313 | distal phalanx of manual digit 4        | distal phalanx of digit of hand 4            |
|  737 | [79](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=79:79)       | CL:0001035 | bone cell | bone cell     | UBERON:0004313 | distal phalanx of manual digit 4        | distal phalanx of digit of hand 4            |
|  738 | [114](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=114:114)    | CL:0001035 | bone cell | bone cell     | UBERON:0004321 | middle phalanx of manual digit 3        | middle phalanx of digit of hand 3            |
|  739 | [115](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=115:115)    | CL:0001035 | bone cell | bone cell     | UBERON:0004322 | middle phalanx of manual digit 4        | middle phalanx of digit of hand 4            |
|  740 | [116](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=116:116)    | CL:0001035 | bone cell | bone cell     | UBERON:0004322 | middle phalanx of manual digit 4        | middle phalanx of digit of hand 4            |
|  741 | [117](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=117:117)    | CL:0001035 | bone cell | bone cell     | UBERON:0004322 | middle phalanx of manual digit 4        | middle phalanx of digit of hand 4            |
|  742 | [118](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=118:118)    | CL:0001035 | bone cell | bone cell     | UBERON:0004322 | middle phalanx of manual digit 4        | middle phalanx of digit of hand 4            |
|  743 | [119](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=119:119)    | CL:0001035 | bone cell | bone cell     | UBERON:0004323 | middle phalanx of manual digit 5        | middle phalanx of digit of hand 5            |
|  744 | [120](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=120:120)    | CL:0001035 | bone cell | bone cell     | UBERON:0004323 | middle phalanx of manual digit 5        | middle phalanx of digit of hand 5            |
|  745 | [121](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=121:121)    | CL:0001035 | bone cell | bone cell     | UBERON:0004323 | middle phalanx of manual digit 5        | middle phalanx of digit of hand 5            |
|  746 | [122](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=122:122)    | CL:0001035 | bone cell | bone cell     | UBERON:0004323 | middle phalanx of manual digit 5        | middle phalanx of digit of hand 5            |
|  747 | [123](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=123:123)    | CL:0001035 | bone cell | bone cell     | UBERON:0001429 | pisiform                                | pisiform                                     |
|  748 | [124](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=124:124)    | CL:0001035 | bone cell | bone cell     | UBERON:0004338 | proximal phalanx of manual digit 1      | proximal phalanx of digit of hand 1          |
|  749 | [125](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=125:125)    | CL:0001035 | bone cell | bone cell     | UBERON:0004338 | proximal phalanx of manual digit 1      | proximal phalanx of digit of hand 1          |
|  750 | [126](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=126:126)    | CL:0001035 | bone cell | bone cell     | UBERON:0004338 | proximal phalanx of manual digit 1      | proximal phalanx of digit of hand 1          |
|  751 | [127](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=127:127)    | CL:0001035 | bone cell | bone cell     | UBERON:0004338 | proximal phalanx of manual digit 1      | proximal phalanx of digit of hand 1          |
|  752 | [128](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=128:128)    | CL:0001035 | bone cell | bone cell     | UBERON:0004328 | proximal phalanx of manual digit 2      | proximal phalanx of digit of hand 2          |
|  753 | [129](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=129:129)    | CL:0001035 | bone cell | bone cell     | UBERON:0004328 | proximal phalanx of manual digit 2      | proximal phalanx of digit of hand 2          |
|  754 | [130](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=130:130)    | CL:0001035 | bone cell | bone cell     | UBERON:0004328 | proximal phalanx of manual digit 2      | proximal phalanx of digit of hand 2          |
|  755 | [131](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=131:131)    | CL:0001035 | bone cell | bone cell     | UBERON:0004328 | proximal phalanx of manual digit 2      | proximal phalanx of digit of hand 2          |
|  756 | [132](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=132:132)    | CL:0001035 | bone cell | bone cell     | UBERON:0004329 | proximal phalanx of manual digit 3      | proximal phalanx of digit of hand 3          |
|  757 | [133](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=133:133)    | CL:0001035 | bone cell | bone cell     | UBERON:0004329 | proximal phalanx of manual digit 3      | proximal phalanx of digit of hand 3          |
|  758 | [134](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=134:134)    | CL:0001035 | bone cell | bone cell     | UBERON:0004329 | proximal phalanx of manual digit 3      | proximal phalanx of digit of hand 3          |
|  759 | [135](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=135:135)    | CL:0001035 | bone cell | bone cell     | UBERON:0004329 | proximal phalanx of manual digit 3      | proximal phalanx of digit of hand 3          |
|  760 | [136](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=136:136)    | CL:0001035 | bone cell | bone cell     | UBERON:0004330 | proximal phalanx of manual digit 4      | proximal phalanx of digit of hand 4          |
|  761 | [137](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=137:137)    | CL:0001035 | bone cell | bone cell     | UBERON:0004330 | proximal phalanx of manual digit 4      | proximal phalanx of digit of hand 4          |
|  762 | [138](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=138:138)    | CL:0001035 | bone cell | bone cell     | UBERON:0004330 | proximal phalanx of manual digit 4      | proximal phalanx of digit of hand 4          |
|  763 | [139](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=139:139)    | CL:0001035 | bone cell | bone cell     | UBERON:0004330 | proximal phalanx of manual digit 4      | proximal phalanx of digit of hand 4          |
|  764 | [140](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=140:140)    | CL:0001035 | bone cell | bone cell     | UBERON:0004331 | proximal phalanx of manual digit 5      | proximal phalanx of digit of hand 5          |
|  765 | [141](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=141:141)    | CL:0001035 | bone cell | bone cell     | UBERON:0004331 | proximal phalanx of manual digit 5      | proximal phalanx of digit of hand 5          |
|  766 | [142](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=142:142)    | CL:0001035 | bone cell | bone cell     | UBERON:0004331 | proximal phalanx of manual digit 5      | proximal phalanx of digit of hand 5          |
|  767 | [113](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=113:113)    | CL:0001035 | bone cell | bone cell     | UBERON:0004321 | middle phalanx of manual digit 3        | middle phalanx of digit of hand 3            |
|  768 | [112](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=112:112)    | CL:0001035 | bone cell | bone cell     | UBERON:0004321 | middle phalanx of manual digit 3        | middle phalanx of digit of hand 3            |
|  769 | [111](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=111:111)    | CL:0001035 | bone cell | bone cell     | UBERON:0004321 | middle phalanx of manual digit 3        | middle phalanx of digit of hand 3            |
|  770 | [110](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=110:110)    | CL:0001035 | bone cell | bone cell     | UBERON:0004320 | middle phalanx of manual digit 2        | middle phalanx of digit of hand 2            |
|  771 | [80](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=80:80)       | CL:0001035 | bone cell | bone cell     | UBERON:0004313 | distal phalanx of manual digit 4        | distal phalanx of digit of hand 4            |
|  772 | [81](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=81:81)       | CL:0001035 | bone cell | bone cell     | UBERON:0004314 | distal phalanx of manual digit 5        | distal phalanx of digit of hand 5            |
|  773 | [82](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=82:82)       | CL:0001035 | bone cell | bone cell     | UBERON:0004314 | distal phalanx of manual digit 5        | distal phalanx of digit of hand 5            |
|  774 | [83](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=83:83)       | CL:0001035 | bone cell | bone cell     | UBERON:0004314 | distal phalanx of manual digit 5        | distal phalanx of digit of hand 5            |
|  775 | [84](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=84:84)       | CL:0001035 | bone cell | bone cell     | UBERON:0004314 | distal phalanx of manual digit 5        | distal phalanx of digit of hand 5            |
|  776 | [85](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=85:85)       | CL:0001035 | bone cell | bone cell     | UBERON:0004314 | distal phalanx of manual digit 5        | distal phalanx of digit of hand 5            |
|  777 | [86](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=86:86)       | CL:0001035 | bone cell | bone cell     | UBERON:0001428 | intermedium                             | lunate                                       |
|  778 | [87](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=87:87)       | CL:0001035 | bone cell | bone cell     | UBERON:0003645 | metacarpal bone of digit 1              | metacarpal bone of digit 1                   |
|  779 | [88](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=88:88)       | CL:0001035 | bone cell | bone cell     | UBERON:0003645 | metacarpal bone of digit 1              | metacarpal bone of digit 1                   |
|  780 | [89](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=89:89)       | CL:0001035 | bone cell | bone cell     | UBERON:0003645 | metacarpal bone of digit 1              | metacarpal bone of digit 1                   |
|  781 | [90](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=90:90)       | CL:0001035 | bone cell | bone cell     | UBERON:0003645 | metacarpal bone of digit 1              | metacarpal bone of digit 1                   |
|  782 | [91](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=91:91)       | CL:0001035 | bone cell | bone cell     | UBERON:0003646 | metacarpal bone of digit 2              | metacarpal bone of digit 2                   |
|  783 | [92](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=92:92)       | CL:0001035 | bone cell | bone cell     | UBERON:0003646 | metacarpal bone of digit 2              | metacarpal bone of digit 2                   |
|  784 | [93](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=93:93)       | CL:0001035 | bone cell | bone cell     | UBERON:0003646 | metacarpal bone of digit 2              | metacarpal bone of digit 2                   |
|  785 | [78](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=78:78)       | CL:0001035 | bone cell | bone cell     | UBERON:0004313 | distal phalanx of manual digit 4        | distal phalanx of digit of hand 4            |
|  786 | [94](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=94:94)       | CL:0001035 | bone cell | bone cell     | UBERON:0003646 | metacarpal bone of digit 2              | metacarpal bone of digit 2                   |
|  787 | [96](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=96:96)       | CL:0001035 | bone cell | bone cell     | UBERON:0003647 | metacarpal bone of digit 3              | metacarpal bone of digit 3                   |
|  788 | [97](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=97:97)       | CL:0001035 | bone cell | bone cell     | UBERON:0003647 | metacarpal bone of digit 3              | metacarpal bone of digit 3                   |
|  789 | [98](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=98:98)       | CL:0001035 | bone cell | bone cell     | UBERON:0003647 | metacarpal bone of digit 3              | metacarpal bone of digit 3                   |
|  790 | [99](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=99:99)       | CL:0001035 | bone cell | bone cell     | UBERON:0003648 | metacarpal bone of digit 4              | metacarpal bone of digit 4                   |
|  791 | [100](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=100:100)    | CL:0001035 | bone cell | bone cell     | UBERON:0003648 | metacarpal bone of digit 4              | metacarpal bone of digit 4                   |
|  792 | [101](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=101:101)    | CL:0001035 | bone cell | bone cell     | UBERON:0003648 | metacarpal bone of digit 4              | metacarpal bone of digit 4                   |
|  793 | [102](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=102:102)    | CL:0001035 | bone cell | bone cell     | UBERON:0003648 | metacarpal bone of digit 4              | metacarpal bone of digit 4                   |
|  794 | [103](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=103:103)    | CL:0001035 | bone cell | bone cell     | UBERON:0003649 | metacarpal bone of digit 5              | metacarpal bone of digit 5                   |
|  795 | [104](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=104:104)    | CL:0001035 | bone cell | bone cell     | UBERON:0003649 | metacarpal bone of digit 5              | metacarpal bone of digit 5                   |
|  796 | [105](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=105:105)    | CL:0001035 | bone cell | bone cell     | UBERON:0003649 | metacarpal bone of digit 5              | metacarpal bone of digit 5                   |
|  797 | [106](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=106:106)    | CL:0001035 | bone cell | bone cell     | UBERON:0003649 | metacarpal bone of digit 5              | metacarpal bone of digit 5                   |
|  798 | [107](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=107:107)    | CL:0001035 | bone cell | bone cell     | UBERON:0004320 | middle phalanx of manual digit 2        | middle phalanx of digit of hand 2            |
|  799 | [108](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=108:108)    | CL:0001035 | bone cell | bone cell     | UBERON:0004320 | middle phalanx of manual digit 2        | middle phalanx of digit of hand 2            |
|  800 | [109](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=109:109)    | CL:0001035 | bone cell | bone cell     | UBERON:0004320 | middle phalanx of manual digit 2        | middle phalanx of digit of hand 2            |
|  801 | [95](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=95:95)       | CL:0001035 | bone cell | bone cell     | UBERON:0003647 | metacarpal bone of digit 3              | metacarpal bone of digit 3                   |
|  802 | [278](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=278:278)    | CL:0001035 | bone cell | bone cell     | UBERON:0015180 | neck of talus                           | neck of talus                                |
|  803 | [279](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=279:279)    | CL:0001035 | bone cell | bone cell     | UBERON:0002395 | talus                                   | talus                                        |
|  804 | [280](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=280:280)    | CL:0001035 | bone cell | bone cell     | UBERON:0002395 | talus                                   | talus                                        |
|  805 | [450](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=450:450)    | CL:0001035 | bone cell | bone cell     | UBERON:0010911 | ossicle                                 | ossicle                                      |
|  806 | [451](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=451:451)    | CL:0001035 | bone cell | bone cell     | UBERON:0001688 | incus bone                              | incus bone                                   |
|  807 | [452](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=452:452)    | CL:0001035 | bone cell | bone cell     | UBERON:0001689 | malleus bone                            | malleus bone                                 |
|  808 | [453](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=453:453)    | CL:0001035 | bone cell | bone cell     | UBERON:0001687 | stapes bone                             | stapes bone                                  |
|  809 | [454](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=454:454)    | CL:0001035 | bone cell | bone cell     | UBERON:0008895 | splanchnocranium                        | splanchnocranium                             |
|  810 | [455](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=455:455)    | CL:0001035 | bone cell | bone cell     | UBERON:0005922 | inferior nasal concha                   | inferior nasal concha                        |
|  811 | [456](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=456:456)    | CL:0001035 | bone cell | bone cell     | UBERON:0001680 | lacrimal bone                           | lacrimal bone                                |
|  812 | [457](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=457:457)    | CL:0001035 | bone cell | bone cell     | UBERON:0001680 | lacrimal bone                           | lacrimal bone                                |
|  813 | [458](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=458:458)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  814 | [459](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=459:459)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  815 | [460](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=460:460)    | CL:0001035 | bone cell | bone cell     | UBERON:0011309 | body of mandible                        | body of mandible                             |
|  816 | [461](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=461:461)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  817 | [462](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=462:462)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  818 | [463](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=463:463)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  819 | [464](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=464:464)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  820 | [465](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=465:465)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  821 | [466](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=466:466)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  822 | [467](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=467:467)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  823 | [468](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=468:468)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  824 | [469](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=469:469)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  825 | [470](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=470:470)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  826 | [471](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=471:471)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  827 | [472](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=472:472)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  828 | [473](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=473:473)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  829 | [474](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=474:474)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  830 | [475](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=475:475)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  831 | [476](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=476:476)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  832 | [477](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=477:477)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  833 | [478](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=478:478)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  834 | [449](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=449:449)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  835 | [448](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=448:448)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  836 | [447](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=447:447)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  837 | [446](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=446:446)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  838 | [416](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=416:416)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  839 | [417](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=417:417)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  840 | [418](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=418:418)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  841 | [419](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=419:419)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  842 | [420](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=420:420)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  843 | [421](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=421:421)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  844 | [422](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=422:422)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  845 | [423](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=423:423)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  846 | [424](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=424:424)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  847 | [425](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=425:425)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  848 | [426](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=426:426)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  849 | [427](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=427:427)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  850 | [428](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=428:428)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  851 | [429](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=429:429)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  852 | [479](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=479:479)    | CL:0001035 | bone cell | bone cell     | UBERON:0001684 | mandible                                | mandible                                     |
|  853 | [430](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=430:430)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  854 | [432](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=432:432)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  855 | [433](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=433:433)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  856 | [434](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=434:434)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  857 | [435](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=435:435)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  858 | [436](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=436:436)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  859 | [437](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=437:437)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  860 | [438](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=438:438)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  861 | [439](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=439:439)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  862 | [440](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=440:440)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  863 | [441](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=441:441)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  864 | [442](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=442:442)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  865 | [443](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=443:443)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  866 | [444](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=444:444)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  867 | [445](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=445:445)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  868 | [431](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=431:431)    | CL:0001035 | bone cell | bone cell     | UBERON:0001678 | temporal bone                           | temporal bone                                |
|  869 | [415](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=415:415)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  870 | [480](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=480:480)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |
|  871 | [482](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=482:482)    | CL:0001035 | bone cell | bone cell     | UBERON:0004527 | alveolar process of maxilla             | alveolar process of maxilla                  |
|  872 | [517](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=517:517)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  873 | [518](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=518:518)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  874 | [519](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=519:519)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  875 | [520](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=520:520)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  876 | [521](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=521:521)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  877 | [522](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=522:522)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  878 | [523](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=523:523)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  879 | [524](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=524:524)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  880 | [525](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=525:525)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  881 | [526](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=526:526)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |
|  882 | [527](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=527:527)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |
|  883 | [528](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=528:528)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |
|  884 | [529](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=529:529)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |
|  885 | [530](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=530:530)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |
|  886 | [531](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=531:531)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |
|  887 | [532](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=532:532)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |
|  888 | [533](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=533:533)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |
|  889 | [534](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=534:534)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |
|  890 | [535](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=535:535)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |
|  891 | [536](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=536:536)    | CL:0001035 | bone cell | bone cell     | UBERON:0004609 | rib 10                                  | rib 10                                       |
|  892 | [537](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=537:537)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |
|  893 | [538](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=538:538)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |
|  894 | [539](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=539:539)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |
|  895 | [540](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=540:540)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |
|  896 | [541](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=541:541)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |
|  897 | [542](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=542:542)    | CL:0001035 | bone cell | bone cell     | UBERON:0004610 | rib 11                                  | rib 11                                       |
|  898 | [543](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=543:543)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |
|  899 | [544](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=544:544)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |
|  900 | [545](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=545:545)    | CL:0001035 | bone cell | bone cell     | UBERON:0004611 | rib 12                                  | rib 12                                       |
|  901 | [516](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=516:516)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  902 | [515](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=515:515)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  903 | [514](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=514:514)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  904 | [513](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=513:513)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  905 | [483](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=483:483)    | CL:0001035 | bone cell | bone cell     | UBERON:0035139 | anterior nasal spine of maxilla         | anterior nasal spine of maxilla              |
|  906 | [484](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=484:484)    | CL:0001035 | bone cell | bone cell     | UBERON:0013767 | frontal process of maxilla              | frontal process of maxilla                   |
|  907 | [485](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=485:485)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |
|  908 | [486](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=486:486)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |
|  909 | [487](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=487:487)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |
|  910 | [488](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=488:488)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |
|  911 | [489](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=489:489)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |
|  912 | [490](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=490:490)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |
|  913 | [491](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=491:491)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |
|  914 | [492](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=492:492)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |
|  915 | [493](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=493:493)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |
|  916 | [494](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=494:494)    | CL:0001035 | bone cell | bone cell     | UBERON:0005871 | palatine process of maxilla             | palatine process of maxilla                  |
|  917 | [495](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=495:495)    | CL:0001035 | bone cell | bone cell     | UBERON:0016477 | zygomatic process of maxilla            | zygomatic process of maxilla                 |
|  918 | [496](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=496:496)    | CL:0001035 | bone cell | bone cell     | UBERON:0001681 | nasal bone                              | nasal bone                                   |
|  919 | [481](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=481:481)    | CL:0001035 | bone cell | bone cell     | UBERON:0002397 | maxilla                                 | maxilla                                      |
|  920 | [497](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=497:497)    | CL:0001035 | bone cell | bone cell     | UBERON:0001682 | palatine bone                           | palatine bone                                |
|  921 | [499](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=499:499)    | CL:0001035 | bone cell | bone cell     | UBERON:0001682 | palatine bone                           | palatine bone                                |
|  922 | [500](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=500:500)    | CL:0001035 | bone cell | bone cell     | UBERON:0001682 | palatine bone                           | palatine bone                                |
|  923 | [501](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=501:501)    | CL:0001035 | bone cell | bone cell     | UBERON:0001682 | palatine bone                           | palatine bone                                |
|  924 | [502](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=502:502)    | CL:0001035 | bone cell | bone cell     | UBERON:0002396 | vomer                                   | vomer                                        |
|  925 | [503](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=503:503)    | CL:0001035 | bone cell | bone cell     | UBERON:0002396 | vomer                                   | vomer                                        |
|  926 | [504](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=504:504)    | CL:0001035 | bone cell | bone cell     | UBERON:0002396 | vomer                                   | vomer                                        |
|  927 | [505](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=505:505)    | CL:0001035 | bone cell | bone cell     | UBERON:0001683 | jugal bone                              | zygomatic bone                               |
|  928 | [506](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=506:506)    | CL:0001035 | bone cell | bone cell     | UBERON:0012110 | frontal process of zygomatic bone       | frontal process of zygomatic bone            |
|  929 | [507](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=507:507)    | CL:0001035 | bone cell | bone cell     | UBERON:0001683 | jugal bone                              | zygomatic bone                               |
|  930 | [508](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=508:508)    | CL:0001035 | bone cell | bone cell     | UBERON:0004654 | temporal process of zygomatic bone      | temporal process of zygomatic bone           |
|  931 | [509](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=509:509)    | CL:0001035 | bone cell | bone cell     | UBERON:0001683 | jugal bone                              | zygomatic bone                               |
|  932 | [510](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=510:510)    | CL:0001035 | bone cell | bone cell     | UBERON:0014477 | thoracic skeleton                       | thoracic skeleton                            |
|  933 | [511](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=511:511)    | CL:0001035 | bone cell | bone cell     | UBERON:0014477 | thoracic skeleton                       | thoracic skeleton                            |
|  934 | [512](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=512:512)    | CL:0001035 | bone cell | bone cell     | UBERON:0004601 | rib 1                                   | rib 1                                        |
|  935 | [498](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=498:498)    | CL:0001035 | bone cell | bone cell     | UBERON:0001682 | palatine bone                           | palatine bone                                |
|  936 | [414](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=414:414)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  937 | [413](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=413:413)    | CL:0001035 | bone cell | bone cell     | UBERON:0016492 | foramen spinosum of sphenoid bone       | foramen spinosum of sphenoid bone            |
|  938 | [412](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=412:412)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
|  939 | [315](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=315:315)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |
|  940 | [316](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=316:316)    | CL:0001035 | bone cell | bone cell     | UBERON:0009991 | lateral condyle of tibia                | lateral condyle of tibia                     |
|  941 | [317](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=317:317)    | CL:0001035 | bone cell | bone cell     | UBERON:0009990 | medial condyle of tibia                 | medial condyle of tibia                      |
|  942 | [318](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=318:318)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |
|  943 | [319](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=319:319)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |
|  944 | [320](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=320:320)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |
|  945 | [321](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=321:321)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |
|  946 | [322](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=322:322)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |
|  947 | [323](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=323:323)    | CL:0001035 | bone cell | bone cell     | UBERON:0007830 | pelvic girdle bone/zone                 | pelvic girdle bone/zone                      |
|  948 | [324](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=324:324)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  949 | [325](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=325:325)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  950 | [326](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=326:326)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  951 | [327](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=327:327)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  952 | [328](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=328:328)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  953 | [329](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=329:329)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  954 | [330](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=330:330)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  955 | [331](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=331:331)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  956 | [332](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=332:332)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  957 | [333](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=333:333)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  958 | [334](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=334:334)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  959 | [335](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=335:335)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  960 | [336](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=336:336)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  961 | [337](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=337:337)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  962 | [338](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=338:338)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  963 | [339](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=339:339)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  964 | [340](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=340:340)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  965 | [341](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=341:341)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  966 | [342](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=342:342)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  967 | [343](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=343:343)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  968 | [314](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=314:314)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |
|  969 | [313](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=313:313)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |
|  970 | [312](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=312:312)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |
|  971 | [311](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=311:311)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |
|  972 | [281](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=281:281)    | CL:0001035 | bone cell | bone cell     | UBERON:0005893 | leg bone                                | leg bone                                     |
|  973 | [282](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=282:282)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  974 | [283](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=283:283)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  975 | [284](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=284:284)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  976 | [285](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=285:285)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  977 | [286](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=286:286)    | CL:0001035 | bone cell | bone cell     | UBERON:0006767 | head of femur                           | head of femur                                |
|  978 | [287](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=287:287)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  979 | [288](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=288:288)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  980 | [289](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=289:289)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  981 | [290](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=290:290)    | CL:0001035 | bone cell | bone cell     | UBERON:0009985 | lateral condyle of femur                | lateral condyle of femur                     |
|  982 | [291](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=291:291)    | CL:0001035 | bone cell | bone cell     | UBERON:0009986 | lateral epicondyle of femur             | lateral epicondyle of femur                  |
|  983 | [292](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=292:292)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  984 | [293](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=293:293)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  985 | [294](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=294:294)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  986 | [344](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=344:344)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
|  987 | [295](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=295:295)    | CL:0001035 | bone cell | bone cell     | UBERON:0009984 | medial condyle of femur                 | medial condyle of femur                      |
|  988 | [297](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=297:297)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  989 | [298](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=298:298)    | CL:0001035 | bone cell | bone cell     | UBERON:0007119 | neck of femur                           | neck of femur                                |
|  990 | [299](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=299:299)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  991 | [300](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=300:300)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  992 | [301](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=301:301)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  993 | [302](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=302:302)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  994 | [303](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=303:303)    | CL:0001035 | bone cell | bone cell     | UBERON:0000981 | femur                                   | femur                                        |
|  995 | [304](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=304:304)    | CL:0001035 | bone cell | bone cell     | UBERON:0001446 | fibula                                  | fibula                                       |
|  996 | [305](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=305:305)    | CL:0001035 | bone cell | bone cell     | UBERON:0001446 | fibula                                  | fibula                                       |
|  997 | [306](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=306:306)    | CL:0001035 | bone cell | bone cell     | UBERON:0012291 | lateral malleolus of fibula             | lateral malleolus of fibula                  |
|  998 | [307](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=307:307)    | CL:0001035 | bone cell | bone cell     | UBERON:0018673 | neck of fibula                          | neck of fibula                               |
|  999 | [308](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=308:308)    | CL:0001035 | bone cell | bone cell     | UBERON:0001446 | fibula                                  | fibula                                       |
| 1000 | [309](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=309:309)    | CL:0001035 | bone cell | bone cell     | UBERON:0002446 | patella                                 | patella                                      |
| 1001 | [310](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=310:310)    | CL:0001035 | bone cell | bone cell     | UBERON:0000979 | tibia                                   | tibia                                        |
| 1002 | [296](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=296:296)    | CL:0001035 | bone cell | bone cell     | UBERON:0009987 | medial epicondyle of femur              | medial epicondyle of femur                   |
| 1003 | [345](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=345:345)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1004 | [346](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=346:346)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1005 | [347](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=347:347)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1006 | [382](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=382:382)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 |
| 1007 | [383](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=383:383)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 |
| 1008 | [384](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=384:384)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 |
| 1009 | [385](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=385:385)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 |
| 1010 | [386](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=386:386)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 |
| 1011 | [387](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=387:387)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 |
| 1012 | [388](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=388:388)    | CL:0001035 | bone cell | bone cell     | UBERON:0012109 | zygomatic process of frontal bone       | zygomatic process of frontal bone            |
| 1013 | [389](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=389:389)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |
| 1014 | [390](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=390:390)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |
| 1015 | [391](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=391:391)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |
| 1016 | [392](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=392:392)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |
| 1017 | [393](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=393:393)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |
| 1018 | [394](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=394:394)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |
| 1019 | [395](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=395:395)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |
| 1020 | [381](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=381:381)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 |
| 1021 | [396](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=396:396)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |
| 1022 | [398](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=398:398)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |
| 1023 | [399](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=399:399)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |
| 1024 | [400](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=400:400)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |
| 1025 | [401](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=401:401)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |
| 1026 | [402](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=402:402)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |
| 1027 | [403](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=403:403)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |
| 1028 | [404](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=404:404)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |
| 1029 | [405](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=405:405)    | CL:0001035 | bone cell | bone cell     | UBERON:0000210 | tetrapod parietal bone                  | parietal bone                                |
| 1030 | [406](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=406:406)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
| 1031 | [407](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=407:407)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
| 1032 | [408](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=408:408)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
| 1033 | [409](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=409:409)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
| 1034 | [410](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=410:410)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
| 1035 | [411](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=411:411)    | CL:0001035 | bone cell | bone cell     | UBERON:0001677 | sphenoid bone                           | sphenoid bone                                |
| 1036 | [397](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=397:397)    | CL:0001035 | bone cell | bone cell     | UBERON:0001676 | occipital bone                          | occipital bone                               |
| 1037 | [1082](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1082:1082) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |
| 1038 | [380](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=380:380)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 |
| 1039 | [378](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=378:378)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 |
| 1040 | [348](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=348:348)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1041 | [349](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=349:349)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1042 | [350](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=350:350)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1043 | [351](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=351:351)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1044 | [352](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=352:352)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1045 | [353](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=353:353)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1046 | [354](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=354:354)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1047 | [355](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=355:355)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1048 | [356](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=356:356)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1049 | [357](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=357:357)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1050 | [358](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=358:358)    | CL:0001035 | bone cell | bone cell     | UBERON:0001272 | innominate bone                         | os coxa                                      |
| 1051 | [359](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=359:359)    | CL:0001035 | bone cell | bone cell     | UBERON:0005944 | axial skeleton plus cranial skeleton    | axial skeleton                               |
| 1052 | [360](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=360:360)    | CL:0001035 | bone cell | bone cell     | UBERON:0004766 | cranial bone                            | cranial bone                                 |
| 1053 | [361](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=361:361)    | CL:0001035 | bone cell | bone cell     | UBERON:0004766 | cranial bone                            | cranial bone                                 |
| 1054 | [379](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=379:379)    | CL:0001035 | bone cell | bone cell     | UBERON:0000209 | tetrapod frontal bone                   | frontal bone                                 |
| 1055 | [362](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=362:362)    | CL:0001035 | bone cell | bone cell     | UBERON:0001685 | hyoid bone                              | hyoid bone                                   |
| 1056 | [364](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=364:364)    | CL:0001035 | bone cell | bone cell     | UBERON:0001685 | hyoid bone                              | hyoid bone                                   |
| 1057 | [365](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=365:365)    | CL:0001035 | bone cell | bone cell     | UBERON:0001685 | hyoid bone                              | hyoid bone                                   |
| 1058 | [366](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=366:366)    | CL:0001035 | bone cell | bone cell     | UBERON:0001703 | neurocranium                            | neurocranium                                 |
| 1059 | [367](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=367:367)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |
| 1060 | [368](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=368:368)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |
| 1061 | [369](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=369:369)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |
| 1062 | [370](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=370:370)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |
| 1063 | [371](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=371:371)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |
| 1064 | [372](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=372:372)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |
| 1065 | [373](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=373:373)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |
| 1066 | [374](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=374:374)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |
| 1067 | [375](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=375:375)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |
| 1068 | [376](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=376:376)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |
| 1069 | [377](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=377:377)    | CL:0001035 | bone cell | bone cell     | UBERON:0001679 | ethmoid bone                            | ethmoid bone                                 |
| 1070 | [363](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=363:363)    | CL:0001035 | bone cell | bone cell     | UBERON:0001685 | hyoid bone                              | hyoid bone                                   |
| 1071 | [1083](https://docs.google.com/spreadsheets/d/1090VgpMYtAcLPUa_4ITh3hwJBZkQKGKATrZu0hc8EVg/edit#gid=0&range=1083:1083) | CL:0001035 | bone cell | bone cell     | UBERON:0004633 | thoracic vertebra 9                     | thoracic vertebra 9                          |




# New CL terms
[**Report**](new_cl_terms_Skeleton.tsv)




# New UBERON terms
[**Report**](new_uberon_terms_Skeleton.tsv)




# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Skeleton_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Skeleton_AS_has_part_CT_log.tsv)