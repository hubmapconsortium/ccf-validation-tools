
ASCT+B Validation Reports for Brain (2022-11-30)
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
  
1. In row _41_, the term _[PCL:0015030](Phttp://purl.obolibrary.org/obo/CL_0015030)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 VIP HS3ST3A1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 VIP HS3ST3A1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 VIP HS3ST3A1_. Please correct it in the ASCT+B table.

1. In row _74_, the term _[PCL:0015063](Phttp://purl.obolibrary.org/obo/CL_0015063)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2-5 PVALB HHIPL1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2-5 PVALB HHIPL1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2-5 PVALB HHIPL1_. Please correct it in the ASCT+B table.

1. In row _44_, the term _[PCL:0015033](Phttp://purl.obolibrary.org/obo/CL_0015033)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2-5 VIP BSPRY primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2-5 VIP BSPRY primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2-5 VIP BSPRY_. Please correct it in the ASCT+B table.

1. In row _135_, the term _[PCL:0015124](Phttp://purl.obolibrary.org/obo/CL_0015124)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Astro L1-6 FGFR3 PLCG1 primary motor cortex glial cell (Homo sapiens)_ and the one in the ontology is _Astro L1-6 FGFR3 PLCG1 primary motor cortex astrocyte (Hsap)_. For reference, the given name/label by SMEs is _Astro L1-6 FGFR3 PLCG1_. Please correct it in the ASCT+B table.

1. In row _76_, the term _[PCL:0015065](Phttp://purl.obolibrary.org/obo/CL_0015065)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3 PVALB SAMD13 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3 PVALB SAMD13 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3 PVALB SAMD13_. Please correct it in the ASCT+B table.

1. In row _14_, the term _[PCL:0015003](Phttp://purl.obolibrary.org/obo/CL_0015003)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 LAMP5 AARD primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 LAMP5 AARD primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 LAMP5 AARD_. Please correct it in the ASCT+B table.

1. In row _43_, the term _[PCL:0015032](Phttp://purl.obolibrary.org/obo/CL_0015032)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-5 VIP CD27-AS1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-5 VIP CD27-AS1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-5 VIP CD27-AS1_. Please correct it in the ASCT+B table.

1. In row _110_, the term _[PCL:0015100](Phttp://purl.obolibrary.org/obo/CL_0015100)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 THEMIS RGPD6 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 THEMIS RGPD6 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 THEMIS RGPD6_. Please correct it in the ASCT+B table.

1. In row _90_, the term _[PCL:0015080](Phttp://purl.obolibrary.org/obo/CL_0015080)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2-3 RORB CCDC68 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2-3 RORB CCDC68 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2-3 RORB CCDC68_. Please correct it in the ASCT+B table.

1. In row _124_, the term _[PCL:0015114](Phttp://purl.obolibrary.org/obo/CL_0015114)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 FEZF2 NREP-AS1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 FEZF2 NREP-AS1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 FEZF2 NREP-AS1_. Please correct it in the ASCT+B table.

1. In row _61_, the term _[PCL:0015050](Phttp://purl.obolibrary.org/obo/CL_0015050)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 SST CCNJL primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 SST CCNJL primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 SST CCNJL_. Please correct it in the ASCT+B table.

1. In row _106_, the term _[PCL:0015096](Phttp://purl.obolibrary.org/obo/CL_0015096)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 THEMIS SNTG2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 THEMIS SNTG2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 THEMIS SNTG2_. Please correct it in the ASCT+B table.

1. In row _83_, the term _[PCL:0015072](Phttp://purl.obolibrary.org/obo/CL_0015072)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 PVALB COL15A1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 PVALB COL15A1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 PVALB COL15A1 (Chandelier)_. Please correct it in the ASCT+B table.

1. In row _78_, the term _[PCL:0015067](Phttp://purl.obolibrary.org/obo/CL_0015067)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2 PVALB FRZB primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2 PVALB FRZB primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2 PVALB FRZB_. Please correct it in the ASCT+B table.

1. In row _105_, the term _[PCL:0015095](Phttp://purl.obolibrary.org/obo/CL_0015095)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 THEMIS SLN primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 THEMIS SLN primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 THEMIS SLN_. Please correct it in the ASCT+B table.

1. In row _47_, the term _[PCL:0015036](Phttp://purl.obolibrary.org/obo/CL_0015036)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-5 VIP PHLDB3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-5 VIP PHLDB3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-5 VIP PHLDB3_. Please correct it in the ASCT+B table.

1. In row _131_, the term _[PCL:0015120](Phttp://purl.obolibrary.org/obo/CL_0015120)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Oligo L2-6 OPALIN FTH1P3 primary motor cortex oligodendrocyte (Homo sapiens)_ and the one in the ontology is _Oligo L2-6 OPALIN FTH1P3 primary motor cortex oligodendrocyte precursor cell (Hsap)_. For reference, the given name/label by SMEs is _Oligo L2-6 OPALIN FTH1P3_. Please correct it in the ASCT+B table.

1. In row _84_, the term _[PCL:0015073](Phttp://purl.obolibrary.org/obo/CL_0015073)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2 LAMP5 KCNG3 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2 LAMP5 KCNG3 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2 LAMP5 KCNG3_. Please correct it in the ASCT+B table.

1. In row _115_, the term _[PCL:0015105](Phttp://purl.obolibrary.org/obo/CL_0015105)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 FEZF2 FFAR4 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 FEZF2 FFAR4 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 FEZF2 FFAR4_. Please correct it in the ASCT+B table.

1. In row _113_, the term _[PCL:0015103](Phttp://purl.obolibrary.org/obo/CL_0015103)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 SH2D1B primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 SH2D1B primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 SH2D1B_. Please correct it in the ASCT+B table.

1. In row _21_, the term _[PCL:0015015](Phttp://purl.obolibrary.org/obo/CL_0015015)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 LAMP5 NMBR primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 LAMP5 NMBR primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 LAMP5 NMBR_. Please correct it in the ASCT+B table.

1. In row _118_, the term _[PCL:0015108](Phttp://purl.obolibrary.org/obo/CL_0015108)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 FEZF2 KLK7 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 FEZF2 KLK7 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 FEZF2 KLK7_. Please correct it in the ASCT+B table.

1. In row _32_, the term _[PCL:0015021](Phttp://purl.obolibrary.org/obo/CL_0015021)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-3 VIP HSPB6 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-3 VIP HSPB6 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-3 VIP HSPB6_. Please correct it in the ASCT+B table.

1. In row _66_, the term _[PCL:0015055](Phttp://purl.obolibrary.org/obo/CL_0015055)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST C4orf26 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST C4orf26 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST C4orf26_. Please correct it in the ASCT+B table.

1. In row _116_, the term _[PCL:0015106](Phttp://purl.obolibrary.org/obo/CL_0015106)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 FEZF2 PROKR2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 FEZF2 PROKR2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 FEZF2 PROKR2_. Please correct it in the ASCT+B table.

1. In row _60_, the term _[PCL:0015049](Phttp://purl.obolibrary.org/obo/CL_0015049)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST PIK3CD primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST PIK3CD primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST PIK3CD_. Please correct it in the ASCT+B table.

1. In row _119_, the term _[PCL:0015109](Phttp://purl.obolibrary.org/obo/CL_0015109)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 FEZF2 POGK primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 FEZF2 POGK primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 FEZF2 POGK_. Please correct it in the ASCT+B table.

1. In row _62_, the term _[PCL:0015051](Phttp://purl.obolibrary.org/obo/CL_0015051)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-3 SST FAM20A primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-3 SST FAM20A primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-3 SST FAM20A_. Please correct it in the ASCT+B table.

1. In row _95_, the term _[PCL:0015085](Phttp://purl.obolibrary.org/obo/CL_0015085)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 THEMIS VILL primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 THEMIS VILL primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 THEMIS VILL_. Please correct it in the ASCT+B table.

1. In row _34_, the term _[PCL:0015023](Phttp://purl.obolibrary.org/obo/CL_0015023)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 VIP SCML4 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 VIP SCML4 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 VIP SCML4_. Please correct it in the ASCT+B table.

1. In row _120_, the term _[PCL:0015110](Phttp://purl.obolibrary.org/obo/CL_0015110)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 FEZF2 CSN1S1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 FEZF2 CSN1S1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 FEZF2 CSN1S1_. Please correct it in the ASCT+B table.

1. In row _65_, the term _[PCL:0015054](Phttp://purl.obolibrary.org/obo/CL_0015054)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST DNAJC14 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST DNAJC14 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST DNAJC14_. Please correct it in the ASCT+B table.

1. In row _42_, the term _[PCL:0015031](Phttp://purl.obolibrary.org/obo/CL_0015031)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 VIP COL4A3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 VIP COL4A3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 VIP COL4A3_. Please correct it in the ASCT+B table.

1. In row _52_, the term _[PCL:0015041](Phttp://purl.obolibrary.org/obo/CL_0015041)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 SST CDH3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 SST CDH3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 SST CDH3_. Please correct it in the ASCT+B table.

1. In row _102_, the term _[PCL:0015092](Phttp://purl.obolibrary.org/obo/CL_0015092)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 RORB MED8 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 RORB MED8 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 RORB MED8_. Please correct it in the ASCT+B table.

1. In row _50_, the term _[PCL:0015039](Phttp://purl.obolibrary.org/obo/CL_0015039)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 VIP TAC3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 VIP TAC3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 VIP TAC3_. Please correct it in the ASCT+B table.

1. In row _92_, the term _[PCL:0015082](Phttp://purl.obolibrary.org/obo/CL_0015082)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3 THEMIS ENPEP primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3 THEMIS ENPEP primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3 THEMIS ENPEP_. Please correct it in the ASCT+B table.

1. In row _33_, the term _[PCL:0015022](Phttp://purl.obolibrary.org/obo/CL_0015022)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 VIP PTGER3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 VIP PTGER3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 VIP PTGER3_. Please correct it in the ASCT+B table.

1. In row _125_, the term _[PCL:0015115](Phttp://purl.obolibrary.org/obo/CL_0015115)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 FEZF2 RNF144A-AS1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 FEZF2 RNF144A-AS1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 FEZF2 RNF144A-AS1_. Please correct it in the ASCT+B table.

1. In row _51_, the term _[PCL:0015040](Phttp://purl.obolibrary.org/obo/CL_0015040)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 SST NPY primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 SST NPY primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 SST NPY (Sst Chodl)_. Please correct it in the ASCT+B table.

1. In row _108_, the term _[PCL:0015098](Phttp://purl.obolibrary.org/obo/CL_0015098)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 OR1L8 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 OR1L8 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 OR1L8_. Please correct it in the ASCT+B table.

1. In row _97_, the term _[PCL:0015087](Phttp://purl.obolibrary.org/obo/CL_0015087)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 RORB LINC01202 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 RORB LINC01202 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 RORB LINC01202_. Please correct it in the ASCT+B table.

1. In row _104_, the term _[PCL:0015094](Phttp://purl.obolibrary.org/obo/CL_0015094)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 THEMIS LINC00343 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 THEMIS LINC00343 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 THEMIS LINC00343_. Please correct it in the ASCT+B table.

1. In row _111_, the term _[PCL:0015101](Phttp://purl.obolibrary.org/obo/CL_0015101)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 C9orf135-AS1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 C9orf135-AS1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 C9orf135-AS1_. Please correct it in the ASCT+B table.

1. In row _35_, the term _[PCL:0015024](Phttp://purl.obolibrary.org/obo/CL_0015024)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-3 VIP FNDC1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-3 VIP FNDC1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-3 VIP FNDC1_. Please correct it in the ASCT+B table.

1. In row _37_, the term _[PCL:0015026](Phttp://purl.obolibrary.org/obo/CL_0015026)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2 VIP SLC6A16 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2 VIP SLC6A16 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2 VIP SLC6A16_. Please correct it in the ASCT+B table.

1. In row _13_, the term _[PCL:0015002](Phttp://purl.obolibrary.org/obo/CL_0015002)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 LAMP5 RAB11FIP1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 LAMP5 RAB11FIP1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 LAMP5 RAB11FIP1_. Please correct it in the ASCT+B table.

1. In row _30_, the term _[PCL:0015019](Phttp://purl.obolibrary.org/obo/CL_0015019)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-3 VIP CBLN1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-3 VIP CBLN1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-3 VIP CBLN1_. Please correct it in the ASCT+B table.

1. In row _68_, the term _[PCL:0015057](Phttp://purl.obolibrary.org/obo/CL_0015057)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST KLHL1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST KLHL1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST KLHL1_. Please correct it in the ASCT+B table.

1. In row _107_, the term _[PCL:0015097](Phttp://purl.obolibrary.org/obo/CL_0015097)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 THEMIS SMYD1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 THEMIS SMYD1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 THEMIS SMYD1 (L6 IT Car3)_. Please correct it in the ASCT+B table.

1. In row _16_, the term _[PCL:0015005](Phttp://purl.obolibrary.org/obo/CL_0015005)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 LAMP5 CA1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 LAMP5 CA1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 LAMP5 CA1_. Please correct it in the ASCT+B table.

1. In row _18_, the term _[PCL:0015007](Phttp://purl.obolibrary.org/obo/CL_0015007)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-6 PAX6 LINC01497 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-6 PAX6 LINC01497 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-6 PAX6 LINC01497_. Please correct it in the ASCT+B table.

1. In row _141_, the term _[UBERON:0002629](http://purl.obolibrary.org/obo/UBERON_0002629)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _riangular part of inferior frontal gyrus_ and the one in the ontology is _triangular part of inferior frontal gyrus_. For reference, the given name/label by SMEs is _inferior frontal gyrus, triangular part_. Please correct it in the ASCT+B table.

1. In row _73_, the term _[PCL:0015062](Phttp://purl.obolibrary.org/obo/CL_0015062)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5 PVALB LRIG3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5 PVALB LRIG3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5 PVALB LRIG3_. Please correct it in the ASCT+B table.

1. In row _40_, the term _[PCL:0015029](Phttp://purl.obolibrary.org/obo/CL_0015029)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-5 VIP SMOC1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-5 VIP SMOC1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-5 VIP SMOC1_. Please correct it in the ASCT+B table.

1. In row _133_, the term _[PCL:0015122](Phttp://purl.obolibrary.org/obo/CL_0015122)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Astro L1-6 FGFR3 AQP1 primary motor cortex glial cell (Homo sapiens)_ and the one in the ontology is _Astro L1-6 FGFR3 AQP1 primary motor cortex astrocyte (Hsap)_. For reference, the given name/label by SMEs is _Astro L1-6 FGFR3 AQP1_. Please correct it in the ASCT+B table.

1. In row _64_, the term _[PCL:0015053](Phttp://purl.obolibrary.org/obo/CL_0015053)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST BEAN1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST BEAN1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST BEAN1_. Please correct it in the ASCT+B table.

1. In row _121_, the term _[PCL:0015111](Phttp://purl.obolibrary.org/obo/CL_0015111)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 FEZF2 ASGR2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 FEZF2 ASGR2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 FEZF2 ASGR2_. Please correct it in the ASCT+B table.

1. In row _112_, the term _[PCL:0015102](Phttp://purl.obolibrary.org/obo/CL_0015102)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 FILIP1L primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 FILIP1L primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 FILIP1L_. Please correct it in the ASCT+B table.

1. In row _77_, the term _[PCL:0015066](Phttp://purl.obolibrary.org/obo/CL_0015066)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 PVALB CDK20 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 PVALB CDK20 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 PVALB CDK20_. Please correct it in the ASCT+B table.

1. In row _24_, the term _[PCL:0015011](Phttp://purl.obolibrary.org/obo/CL_0015011)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2 PAX6 FREM2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2 PAX6 FREM2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2 PAX6 FREM2_. Please correct it in the ASCT+B table.

1. In row _59_, the term _[PCL:0015048](Phttp://purl.obolibrary.org/obo/CL_0015048)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST PAWR primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST PAWR primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST PAWR_. Please correct it in the ASCT+B table.

1. In row _29_, the term _[PCL:0015018](Phttp://purl.obolibrary.org/obo/CL_0015018)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 SST DEFB108B primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 SST DEFB108B primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 SST DEFB108B_. Please correct it in the ASCT+B table.

1. In row _93_, the term _[PCL:0015083](Phttp://purl.obolibrary.org/obo/CL_0015083)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 RORB TNNT2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 RORB TNNT2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 RORB TNNT2_. Please correct it in the ASCT+B table.

1. In row _138_, the term _[PCL:0015127](Phttp://purl.obolibrary.org/obo/CL_0015127)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Micro L1-6 TYROBP CD74 primary motor cortex microglial cell (Homo sapiens)_ and the one in the ontology is _Micro L1-6 TYROBP CD74 primary motor cortex microglial cell (Hsap)_. For reference, the given name/label by SMEs is _Micro L1-6 TYROBP CD74_. Please correct it in the ASCT+B table.

1. In row _127_, the term _[PCL:0015117](Phttp://purl.obolibrary.org/obo/CL_0015117)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 LPO primary motor cortex oligodendrocyte precursor cell (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 LPO primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 LPO_. Please correct it in the ASCT+B table.

1. In row _38_, the term _[PCL:0015027](Phttp://purl.obolibrary.org/obo/CL_0015027)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 VIP KLHDC8B primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 VIP KLHDC8B primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 VIP KLHDC8B_. Please correct it in the ASCT+B table.

1. In row _57_, the term _[PCL:0015046](Phttp://purl.obolibrary.org/obo/CL_0015046)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 SST GGTLC3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 SST GGTLC3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 SST GGTLC3_. Please correct it in the ASCT+B table.

1. In row _49_, the term _[PCL:0015038](Phttp://purl.obolibrary.org/obo/CL_0015038)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-6 VIP UG0898H09 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-6 VIP UG0898H09 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-6 VIP UG0898H09_. Please correct it in the ASCT+B table.

1. In row _101_, the term _[PCL:0015091](Phttp://purl.obolibrary.org/obo/CL_0015091)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 RORB RPRM primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 RORB RPRM primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 RORB RPRM_. Please correct it in the ASCT+B table.

1. In row _96_, the term _[PCL:0015086](Phttp://purl.obolibrary.org/obo/CL_0015086)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3 RORB OTOGL primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3 RORB OTOGL primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3 RORB OTOGL_. Please correct it in the ASCT+B table.

1. In row _123_, the term _[PCL:0015113](Phttp://purl.obolibrary.org/obo/CL_0015113)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 FEZF2 PKD2L1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 FEZF2 PKD2L1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 FEZF2 PKD2L1_. Please correct it in the ASCT+B table.

1. In row _55_, the term _[PCL:0015044](Phttp://purl.obolibrary.org/obo/CL_0015044)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB SST CRHR2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB SST CRHR2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB SST CRHR2_. Please correct it in the ASCT+B table.

1. In row _12_, the term _[PCL:0015001](Phttp://purl.obolibrary.org/obo/CL_0015001)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 LAMP5 PVRL2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 LAMP5 PVRL2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 LAMP5 PVRL2_. Please correct it in the ASCT+B table.

1. In row _85_, the term _[PCL:0015074](Phttp://purl.obolibrary.org/obo/CL_0015074)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2 LINC00507 ATP7B primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2 LINC00507 ATP7B primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2 LINC00507 ATP7B_. Please correct it in the ASCT+B table.

1. In row _134_, the term _[PCL:0015123](Phttp://purl.obolibrary.org/obo/CL_0015123)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Astro L1 FGFR3 SERPINI2 primary motor cortex glial cell (Homo sapiens)_ and the one in the ontology is _Astro L1 FGFR3 SERPINI2 primary motor cortex astrocyte (Hsap)_. For reference, the given name/label by SMEs is _Astro L1 FGFR3 SERPINI2_. Please correct it in the ASCT+B table.

1. In row _46_, the term _[PCL:0015035](Phttp://purl.obolibrary.org/obo/CL_0015035)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-6 VIP ZIM2-AS1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-6 VIP ZIM2-AS1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-6 VIP ZIM2-AS1_. Please correct it in the ASCT+B table.

1. In row _88_, the term _[PCL:0015077](Phttp://purl.obolibrary.org/obo/CL_0015077)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2-3 LINC00507 DSG3 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2-3 LINC00507 DSG3 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2-3 LINC00507 DSG3_. Please correct it in the ASCT+B table.

1. In row _126_, the term _[PCL:0015116](Phttp://purl.obolibrary.org/obo/CL_0015116)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 IFNG-AS1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 IFNG-AS1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 IFNG-AS1_. Please correct it in the ASCT+B table.

1. In row _82_, the term _[PCL:0015071](Phttp://purl.obolibrary.org/obo/CL_0015071)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB MEPE primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB MEPE primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB MEPE_. Please correct it in the ASCT+B table.

1. In row _136_, the term _[PCL:0015125](Phttp://purl.obolibrary.org/obo/CL_0015125)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Endo L2-5 NOSTRIN SRGN primary motor cortex endothelial cell (Homo sapiens)_ and the one in the ontology is _Endo L2-5 NOSTRIN SRGN primary motor cortex endothelial cell (Hsap)_. For reference, the given name/label by SMEs is _Endo L2-5 NOSTRIN SRGN_. Please correct it in the ASCT+B table.

1. In row _79_, the term _[PCL:0015068](Phttp://purl.obolibrary.org/obo/CL_0015068)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 SST CLIC6 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 SST CLIC6 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 SST CLIC6_. Please correct it in the ASCT+B table.

1. In row _20_, the term _[PCL:0015014](Phttp://purl.obolibrary.org/obo/CL_0015014)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 LAMP5 BMP2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 LAMP5 BMP2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 LAMP5 BMP2_. Please correct it in the ASCT+B table.

1. In row _137_, the term _[PCL:0015126](Phttp://purl.obolibrary.org/obo/CL_0015126)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _VLMC L1-5 PDGFRA COLEC12 primary motor cortex vascular leptomeningeal cell (Homo sapiens)_ and the one in the ontology is _VLMC L1-5 PDGFRA COLEC12 primary motor cortex vascular leptomeningeal cell (Hsap)_. For reference, the given name/label by SMEs is _VLMC L1-5 PDGFRA COLEC12_. Please correct it in the ASCT+B table.

1. In row _129_, the term _[PCL:0015079](Phttp://purl.obolibrary.org/obo/CL_0015079)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Oligo L2-6 OPALIN MAP6D1 primary motor cortex oligodendrocyte (Homo sapiens)_ and the one in the ontology is _Oligo L2-6 OPALIN MAP6D1 primary motor cortex oligodendrocyte precursor cell (Hsap)_. For reference, the given name/label by SMEs is _Oligo L2-6 OPALIN MAP6D1_. Please correct it in the ASCT+B table.

1. In row _19_, the term _[PCL:0015008](Phttp://purl.obolibrary.org/obo/CL_0015008)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 PAX6 MIR101-1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 PAX6 MIR101-1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 PAX6 MIR101-1_. Please correct it in the ASCT+B table.

1. In row _67_, the term _[PCL:0015056](Phttp://purl.obolibrary.org/obo/CL_0015056)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST FBN2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST FBN2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST FBN2_. Please correct it in the ASCT+B table.

1. In row _26_, the term _[PCL:0015013](Phttp://purl.obolibrary.org/obo/CL_0015013)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 VIP WNT4 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 VIP WNT4 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 VIP WNT4_. Please correct it in the ASCT+B table.

1. In row _128_, the term _[PCL:0015118](Phttp://purl.obolibrary.org/obo/CL_0015118)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _OPC L1-6 PDGFRA COL20A1 primary motor cortex glial cell (Homo sapiens)_ and the one in the ontology is _OPC L1-6 PDGFRA COL20A1 primary motor cortex oligodendrocyte precursor cell (Hsap)_. For reference, the given name/label by SMEs is _OPC L1-6 PDGFRA COL20A1_. Please correct it in the ASCT+B table.

1. In row _15_, the term _[PCL:0015004](Phttp://purl.obolibrary.org/obo/CL_0015004)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 LAMP5 NES primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 LAMP5 NES primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 LAMP5 NES_. Please correct it in the ASCT+B table.

1. In row _54_, the term _[PCL:0015043](Phttp://purl.obolibrary.org/obo/CL_0015043)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST ISX primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST ISX primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST ISX_. Please correct it in the ASCT+B table.

1. In row _109_, the term _[PCL:0015099](Phttp://purl.obolibrary.org/obo/CL_0015099)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 THEMIS LINC01116 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 THEMIS LINC01116 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 THEMIS LINC01116_. Please correct it in the ASCT+B table.

1. In row _48_, the term _[PCL:0015037](Phttp://purl.obolibrary.org/obo/CL_0015037)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-5 VIP LINC01013 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-5 VIP LINC01013 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-5 VIP LINC01013_. Please correct it in the ASCT+B table.

1. In row _89_, the term _[PCL:0015078](Phttp://purl.obolibrary.org/obo/CL_0015078)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3 LAMP5 CARM1P1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3 LAMP5 CARM1P1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3 LAMP5 CARM1P1_. Please correct it in the ASCT+B table.

1. In row _72_, the term _[PCL:0015061](Phttp://purl.obolibrary.org/obo/CL_0015061)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 PVALB ISG20 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 PVALB ISG20 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 PVALB ISG20_. Please correct it in the ASCT+B table.

1. In row _80_, the term _[PCL:0015069](Phttp://purl.obolibrary.org/obo/CL_0015069)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB GAPDHP60 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB GAPDHP60 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB GAPDHP60_. Please correct it in the ASCT+B table.

1. In row _71_, the term _[PCL:0015060](Phttp://purl.obolibrary.org/obo/CL_0015060)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB ZFPM2-AS1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB ZFPM2-AS1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB ZFPM2-AS1_. Please correct it in the ASCT+B table.

1. In row _94_, the term _[PCL:0015084](Phttp://purl.obolibrary.org/obo/CL_0015084)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 RORB LAMA4 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 RORB LAMA4 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 RORB LAMA4_. Please correct it in the ASCT+B table.

1. In row _122_, the term _[PCL:0015112](Phttp://purl.obolibrary.org/obo/CL_0015112)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 FEZF2 LINC01107 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 FEZF2 LINC01107 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 FEZF2 LINC01107_. Please correct it in the ASCT+B table.

1. In row _103_, the term _[PCL:0015093](Phttp://purl.obolibrary.org/obo/CL_0015093)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 THEMIS FGF10 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 THEMIS FGF10 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 THEMIS FGF10_. Please correct it in the ASCT+B table.

1. In row _31_, the term _[PCL:0015020](Phttp://purl.obolibrary.org/obo/CL_0015020)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 VIP EXPH5 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 VIP EXPH5 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 VIP EXPH5_. Please correct it in the ASCT+B table.

1. In row _69_, the term _[PCL:0015058](Phttp://purl.obolibrary.org/obo/CL_0015058)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L6 SST TH primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L6 SST TH primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L6 SST TH_. Please correct it in the ASCT+B table.

1. In row _56_, the term _[PCL:0015045](Phttp://purl.obolibrary.org/obo/CL_0015045)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 SST OR5AH1P primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 SST OR5AH1P primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 SST OR5AH1P_. Please correct it in the ASCT+B table.

1. In row _70_, the term _[PCL:0015059](Phttp://purl.obolibrary.org/obo/CL_0015059)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB KCNIP2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB KCNIP2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB KCNIP2_. Please correct it in the ASCT+B table.

1. In row _28_, the term _[PCL:0015017](Phttp://purl.obolibrary.org/obo/CL_0015017)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 SST P4HA3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 SST P4HA3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 SST P4HA3_. Please correct it in the ASCT+B table.

1. In row _91_, the term _[PCL:0015081](Phttp://purl.obolibrary.org/obo/CL_0015081)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2-3 RORB PTPN3 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2-3 RORB PTPN3 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2-3 RORB PTPN3_. Please correct it in the ASCT+B table.

1. In row _81_, the term _[PCL:0015070](Phttp://purl.obolibrary.org/obo/CL_0015070)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB FAM150B primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB FAM150B primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB FAM150B_. Please correct it in the ASCT+B table.

1. In row _114_, the term _[PCL:0015104](Phttp://purl.obolibrary.org/obo/CL_0015104)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 FEZF2 PDYN primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 FEZF2 PDYN primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 FEZF2 PDYN_. Please correct it in the ASCT+B table.

1. In row _98_, the term _[PCL:0015088](Phttp://purl.obolibrary.org/obo/CL_0015088)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 THEMIS SLC22A18 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 THEMIS SLC22A18 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 THEMIS SLC22A18_. Please correct it in the ASCT+B table.

1. In row _39_, the term _[PCL:0015028](Phttp://purl.obolibrary.org/obo/CL_0015028)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 VIP IGDCC3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 VIP IGDCC3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 VIP IGDCC3_. Please correct it in the ASCT+B table.

1. In row _100_, the term _[PCL:0015090](Phttp://purl.obolibrary.org/obo/CL_0015090)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 RORB LNX2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 RORB LNX2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 RORB LNX2_. Please correct it in the ASCT+B table.

1. In row _75_, the term _[PCL:0015064](Phttp://purl.obolibrary.org/obo/CL_0015064)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2-5 PVALB RPH3AL primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2-5 PVALB RPH3AL primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2-5 PVALB RPH3AL_. Please correct it in the ASCT+B table.

1. In row _22_, the term _[PCL:0015009](Phttp://purl.obolibrary.org/obo/CL_0015009)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 PAX6 CHRFAM7A primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 PAX6 CHRFAM7A primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 PAX6 CHRFAM7A_. Please correct it in the ASCT+B table.

1. In row _86_, the term _[PCL:0015075](Phttp://purl.obolibrary.org/obo/CL_0015075)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2 LINC00507 GLRA3 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2 LINC00507 GLRA3 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2 LINC00507 GLRA3_. Please correct it in the ASCT+B table.

1. In row _25_, the term _[PCL:0015012](Phttp://purl.obolibrary.org/obo/CL_0015012)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 VIP HTR3A primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 VIP HTR3A primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 VIP HTR3A_. Please correct it in the ASCT+B table.

1. In row _99_, the term _[PCL:0015089](Phttp://purl.obolibrary.org/obo/CL_0015089)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 THEMIS TNFAIP6 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 THEMIS TNFAIP6 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 THEMIS TNFAIP6_. Please correct it in the ASCT+B table.

1. In row _45_, the term _[PCL:0015034](Phttp://purl.obolibrary.org/obo/CL_0015034)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2-5 VIP SOX11 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2-5 VIP SOX11 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2-5 VIP SOX11_. Please correct it in the ASCT+B table.

1. In row _17_, the term _[PCL:0015006](Phttp://purl.obolibrary.org/obo/CL_0015006)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 LAMP5 CRABP1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 LAMP5 CRABP1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 LAMP5 CRABP1_. Please correct it in the ASCT+B table.

1. In row _132_, the term _[PCL:0015121](Phttp://purl.obolibrary.org/obo/CL_0015121)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Oligo L5-6 OPALIN LDLRAP1 primary motor cortex oligodendrocyte (Homo sapiens)_ and the one in the ontology is _Oligo L5-6 OPALIN LDLRAP1 primary motor cortex oligodendrocyte (Hsap)_. For reference, the given name/label by SMEs is _Oligo L5-6 OPALIN LDLRAP1_. Please correct it in the ASCT+B table.

1. In row _117_, the term _[PCL:0015107](Phttp://purl.obolibrary.org/obo/CL_0015107)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 CFTR primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 CFTR primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 CFTR_. Please correct it in the ASCT+B table.

1. In row _53_, the term _[PCL:0015042](Phttp://purl.obolibrary.org/obo/CL_0015042)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5 SST RPL35AP11 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5 SST RPL35AP11 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5 SST RPL35AP11_. Please correct it in the ASCT+B table.

1. In row _27_, the term _[PCL:0015016](Phttp://purl.obolibrary.org/obo/CL_0015016)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 PVALB-like SST ASIC4 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 PVALB-like SST ASIC4 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 PVALB SST ASIC4_. Please correct it in the ASCT+B table.

1. In row _36_, the term _[PCL:0015025](Phttp://purl.obolibrary.org/obo/CL_0015025)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-3 VIP CHRNA2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-3 VIP CHRNA2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-3 VIP CHRNA2_. Please correct it in the ASCT+B table.

1. In row _63_, the term _[PCL:0015052](Phttp://purl.obolibrary.org/obo/CL_0015052)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 SST PRRT4 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 SST PRRT4 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 SST PRRT4_. Please correct it in the ASCT+B table.

1. In row _130_, the term _[PCL:0015119](Phttp://purl.obolibrary.org/obo/CL_0015119)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Oligo L3-6 OPALIN-like ENPP6 primary motor cortex oligodendrocyte (Homo sapiens)_ and the one in the ontology is _Oligo L3-6 OPALIN-like ENPP6 primary motor cortex oligodendrocyte precursor cell (Hsap)_. For reference, the given name/label by SMEs is _Oligo L3-6 OPALIN ENPP6_. Please correct it in the ASCT+B table.

1. In row _87_, the term _[PCL:0015076](Phttp://purl.obolibrary.org/obo/CL_0015076)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2-3 RORB RTKN2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2-3 RORB RTKN2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2-3 RORB RTKN2_. Please correct it in the ASCT+B table.

1. In row _58_, the term _[PCL:0015047](Phttp://purl.obolibrary.org/obo/CL_0015047)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2-3 SST NMU primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2-3 SST NMU primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2-3 SST NMU_. Please correct it in the ASCT+B table.

1. In row _23_, the term _[PCL:0015010](Phttp://purl.obolibrary.org/obo/CL_0015010)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 VIP SLC7A6OS primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 VIP SLC7A6OS primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 VIP SLC7A6OS_. Please correct it in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _156_, no term id was found for the name/label _frontomarginal gyrus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _159_, no term id was found for the name/label _supraparietal lobule_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _160_, no term id was found for the name/label _inferior parietal lobule_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _160_, no term id was found for the name/label _inferior parietal lobule_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _161_, no term id was found for the name/label _inferior parietal lobule_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _161_, no term id was found for the name/label _inferior parietal lobule_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _163_, no term id was found for the name/label _paracentral lobule, caudal part_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _169_, no term id was found for the name/label _transverse temporal gyrus (Heschl's gyrus)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _169_, no term id was found for the name/label _transverse temporal gyrus (Heschl's gyrus)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _170_, no term id was found for the name/label _transverse temporal gyrus (Heschl's gyrus)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _170_, no term id was found for the name/label _transverse temporal gyrus (Heschl's gyrus)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _172_, no term id was found for the name/label _perirhinal lobule_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _175_, no term id was found for the name/label _occipitoparietal transition region_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _176_, no term id was found for the name/label _occipitotemporal transition region_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _179_, no term id was found for the name/label _occipitotemporal (fusiform) gyrus, occipital part_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _186_, no term id was found for the name/label _cingulate gyrus, retrospleninal part_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _192_, no term id was found for the name/label _uncus of parahippocampal gyrus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _193_, no term id was found for the name/label _hippocampal gyrus (formation)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _193_, no term id was found for the name/label _hippocampal gyrus (formation)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _193_, no term id was found for the name/label _head of hippocampus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _194_, no term id was found for the name/label _hippocampal gyrus (formation)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _194_, no term id was found for the name/label _hippocampal gyrus (formation)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _194_, no term id was found for the name/label _body of hippocampus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _195_, no term id was found for the name/label _hippocampal gyrus (formation)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _195_, no term id was found for the name/label _hippocampal gyrus (formation)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _195_, no term id was found for the name/label _subicular complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _198_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _198_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _198_, no term id was found for the name/label _anterior amygdalar area_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _199_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _199_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _199_, no term id was found for the name/label _anterior cortical nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _200_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _200_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _200_, no term id was found for the name/label _posterior cortical nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _201_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _201_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _201_, no term id was found for the name/label _medial nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _202_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _202_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _202_, no term id was found for the name/label _lateral nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _203_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _203_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _203_, no term id was found for the name/label _basolateral nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _204_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _204_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _204_, no term id was found for the name/label _basomedial nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _205_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _205_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _205_, no term id was found for the name/label _central nuclear group_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _206_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _206_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _206_, no term id was found for the name/label _amygdalohippocampal area_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _207_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _207_, no term id was found for the name/label _amygdaloid complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _207_, no term id was found for the name/label _bed nucleus of stria terminalis_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _208_, no term id was found for the name/label _caudate nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _210_, no term id was found for the name/label _mucleus accumbens_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _214_, no term id was found for the name/label _septal nuclei_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _216_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _216_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _216_, no term id was found for the name/label _anterior nuclear complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _217_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _217_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _217_, no term id was found for the name/label _mediodorsal nucleus of thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _218_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _218_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _218_, no term id was found for the name/label _reunions nucleus of thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _219_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _219_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _219_, no term id was found for the name/label _lateral posterior nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _220_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _220_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _220_, no term id was found for the name/label _pulvinar of thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _221_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _221_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _221_, no term id was found for the name/label _ventral anterior nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _222_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _222_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _222_, no term id was found for the name/label _ventral lateral nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _223_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _223_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _223_, no term id was found for the name/label _ventral posterior medial nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _224_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _224_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _224_, no term id was found for the name/label _ventral posterior lateral nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _225_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _225_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _225_, no term id was found for the name/label _lateral geniculate nuclei_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _226_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _226_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _226_, no term id was found for the name/label _medial geniculate nuclei_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _227_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _227_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _227_, no term id was found for the name/label _parafascicular nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _228_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _228_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _228_, no term id was found for the name/label _centromedian nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _229_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _229_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _229_, no term id was found for the name/label _midline nuclear complex_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _230_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _230_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _231_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _231_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _231_, no term id was found for the name/label _habenular nuclei_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _232_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _232_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _232_, no term id was found for the name/label _paraventricular nucleus of thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _233_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _233_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _234_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _234_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _234_, no term id was found for the name/label _reticular formation of thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _235_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _235_, no term id was found for the name/label _thalamus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _235_, no term id was found for the name/label _subthalamic nucleus (subthalamus)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _237_, no term id was found for the name/label _supraoptic region_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _238_, no term id was found for the name/label _tuberal region_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _239_, no term id was found for the name/label _mammillary region_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _239_, no term id was found for the name/label _mammillary region_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _239_, no term id was found for the name/label _mammillary nucleus_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _241_, no term id was found for the name/label _corpus callosum (midline portion)_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _243_, no term id was found for the name/label _internal capsule_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _244_, no term id was found for the name/label _mammillothalamic tract_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _248_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _248_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _249_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _249_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _250_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _250_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _250_, no term id was found for the name/label _atrium of lateral ventricle_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _251_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _251_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _252_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _252_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _253_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _253_, no term id was found for the name/label _ventricle of forebrain_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _264_, no term id was found for the name/label _paravermis of cerebellum_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _265_, no term id was found for the name/label _lateral hemisphere of cerebellum_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _267_, no term id was found for the name/label _cerebellar deep nuclei_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).

1. In row _272_, no term id was found for the name/label _inferior olive_. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request.  
  
- No issues found.


# Relationship reports

## Relationship AS-AS report
[**Report**](../logs/Brain/class_Brain_log.tsv)
## Relationship CT-CT report
[**Report**](../logs/Brain/class_Brain_log.tsv)
## Relationship CT-AS report
[**Report**](../logs/Brain/Brain_AS__CT_strict_log.tsv)
# New CL terms
[**Report**](../logs/Brain/new_cl_terms_Brain.tsv)
# New UBERON terms
[**Report**](../logs/Brain/new_uberon_terms_Brain.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](../logs/Brain/class_Brain_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](../logs/Brain/Brain_AS_has_part_CT_log.tsv)