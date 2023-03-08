
ASCT+B Validation Reports for Brain (2023-03-08)
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
  
1. In row _[124](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=124:124)_, the term _[PCL:0015114](Phttp://purl.obolibrary.org/obo/CL_0015114)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 FEZF2 NREP-AS1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 FEZF2 NREP-AS1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 FEZF2 NREP-AS1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[23](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=23:23)_, the term _[PCL:0015010](Phttp://purl.obolibrary.org/obo/CL_0015010)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 VIP SLC7A6OS primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 VIP SLC7A6OS primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 VIP SLC7A6OS_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[69](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=69:69)_, the term _[PCL:0015058](Phttp://purl.obolibrary.org/obo/CL_0015058)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L6 SST TH primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L6 SST TH primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L6 SST TH_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[33](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=33:33)_, the term _[PCL:0015022](Phttp://purl.obolibrary.org/obo/CL_0015022)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 VIP PTGER3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 VIP PTGER3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 VIP PTGER3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[17](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=17:17)_, the term _[PCL:0015006](Phttp://purl.obolibrary.org/obo/CL_0015006)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 LAMP5 CRABP1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 LAMP5 CRABP1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 LAMP5 CRABP1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[30](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=30:30)_, the term _[PCL:0015019](Phttp://purl.obolibrary.org/obo/CL_0015019)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-3 VIP CBLN1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-3 VIP CBLN1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-3 VIP CBLN1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[13](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=13:13)_, the term _[PCL:0015002](Phttp://purl.obolibrary.org/obo/CL_0015002)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 LAMP5 RAB11FIP1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 LAMP5 RAB11FIP1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 LAMP5 RAB11FIP1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[86](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=86:86)_, the term _[PCL:0015075](Phttp://purl.obolibrary.org/obo/CL_0015075)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2 LINC00507 GLRA3 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2 LINC00507 GLRA3 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2 LINC00507 GLRA3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[110](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=110:110)_, the term _[PCL:0015100](Phttp://purl.obolibrary.org/obo/CL_0015100)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 THEMIS RGPD6 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 THEMIS RGPD6 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 THEMIS RGPD6_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[67](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=67:67)_, the term _[PCL:0015056](Phttp://purl.obolibrary.org/obo/CL_0015056)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST FBN2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST FBN2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST FBN2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[132](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=132:132)_, the term _[PCL:0015121](Phttp://purl.obolibrary.org/obo/CL_0015121)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Oligo L5-6 OPALIN LDLRAP1 primary motor cortex oligodendrocyte (Homo sapiens)_ and the one in the ontology is _Oligo L5-6 OPALIN LDLRAP1 primary motor cortex oligodendrocyte (Hsap)_. For reference, the given name/label by SMEs is _Oligo L5-6 OPALIN LDLRAP1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[42](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=42:42)_, the term _[PCL:0015031](Phttp://purl.obolibrary.org/obo/CL_0015031)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 VIP COL4A3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 VIP COL4A3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 VIP COL4A3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[117](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=117:117)_, the term _[PCL:0015107](Phttp://purl.obolibrary.org/obo/CL_0015107)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 CFTR primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 CFTR primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 CFTR_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[131](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=131:131)_, the term _[PCL:0015120](Phttp://purl.obolibrary.org/obo/CL_0015120)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Oligo L2-6 OPALIN FTH1P3 primary motor cortex oligodendrocyte (Homo sapiens)_ and the one in the ontology is _Oligo L2-6 OPALIN FTH1P3 primary motor cortex oligodendrocyte precursor cell (Hsap)_. For reference, the given name/label by SMEs is _Oligo L2-6 OPALIN FTH1P3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[96](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=96:96)_, the term _[PCL:0015086](Phttp://purl.obolibrary.org/obo/CL_0015086)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3 RORB OTOGL primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3 RORB OTOGL primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3 RORB OTOGL_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[109](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=109:109)_, the term _[PCL:0015099](Phttp://purl.obolibrary.org/obo/CL_0015099)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 THEMIS LINC01116 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 THEMIS LINC01116 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 THEMIS LINC01116_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[38](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=38:38)_, the term _[PCL:0015027](Phttp://purl.obolibrary.org/obo/CL_0015027)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 VIP KLHDC8B primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 VIP KLHDC8B primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 VIP KLHDC8B_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[15](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=15:15)_, the term _[PCL:0015004](Phttp://purl.obolibrary.org/obo/CL_0015004)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 LAMP5 NES primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 LAMP5 NES primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 LAMP5 NES_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[40](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=40:40)_, the term _[PCL:0015029](Phttp://purl.obolibrary.org/obo/CL_0015029)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-5 VIP SMOC1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-5 VIP SMOC1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-5 VIP SMOC1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[25](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=25:25)_, the term _[PCL:0015012](Phttp://purl.obolibrary.org/obo/CL_0015012)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 VIP HTR3A primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 VIP HTR3A primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 VIP HTR3A_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[135](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=135:135)_, the term _[PCL:0015124](Phttp://purl.obolibrary.org/obo/CL_0015124)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Astro L1-6 FGFR3 PLCG1 primary motor cortex glial cell (Homo sapiens)_ and the one in the ontology is _Astro L1-6 FGFR3 PLCG1 primary motor cortex astrocyte (Hsap)_. For reference, the given name/label by SMEs is _Astro L1-6 FGFR3 PLCG1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[60](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=60:60)_, the term _[PCL:0015049](Phttp://purl.obolibrary.org/obo/CL_0015049)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST PIK3CD primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST PIK3CD primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST PIK3CD_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[63](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=63:63)_, the term _[PCL:0015052](Phttp://purl.obolibrary.org/obo/CL_0015052)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 SST PRRT4 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 SST PRRT4 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 SST PRRT4_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[104](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=104:104)_, the term _[PCL:0015094](Phttp://purl.obolibrary.org/obo/CL_0015094)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 THEMIS LINC00343 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 THEMIS LINC00343 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 THEMIS LINC00343_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[101](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=101:101)_, the term _[PCL:0015091](Phttp://purl.obolibrary.org/obo/CL_0015091)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 RORB RPRM primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 RORB RPRM primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 RORB RPRM_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[85](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=85:85)_, the term _[PCL:0015074](Phttp://purl.obolibrary.org/obo/CL_0015074)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2 LINC00507 ATP7B primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2 LINC00507 ATP7B primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2 LINC00507 ATP7B_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[134](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=134:134)_, the term _[PCL:0015123](Phttp://purl.obolibrary.org/obo/CL_0015123)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Astro L1 FGFR3 SERPINI2 primary motor cortex glial cell (Homo sapiens)_ and the one in the ontology is _Astro L1 FGFR3 SERPINI2 primary motor cortex astrocyte (Hsap)_. For reference, the given name/label by SMEs is _Astro L1 FGFR3 SERPINI2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[74](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=74:74)_, the term _[PCL:0015063](Phttp://purl.obolibrary.org/obo/CL_0015063)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2-5 PVALB HHIPL1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2-5 PVALB HHIPL1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2-5 PVALB HHIPL1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[61](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=61:61)_, the term _[PCL:0015050](Phttp://purl.obolibrary.org/obo/CL_0015050)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 SST CCNJL primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 SST CCNJL primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 SST CCNJL_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[55](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=55:55)_, the term _[PCL:0015044](Phttp://purl.obolibrary.org/obo/CL_0015044)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB SST CRHR2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB SST CRHR2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB SST CRHR2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[137](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=137:137)_, the term _[PCL:0015126](Phttp://purl.obolibrary.org/obo/CL_0015126)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _VLMC L1-5 PDGFRA COLEC12 primary motor cortex vascular leptomeningeal cell (Homo sapiens)_ and the one in the ontology is _VLMC L1-5 PDGFRA COLEC12 primary motor cortex vascular leptomeningeal cell (Hsap)_. For reference, the given name/label by SMEs is _VLMC L1-5 PDGFRA COLEC12_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[83](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=83:83)_, the term _[PCL:0015072](Phttp://purl.obolibrary.org/obo/CL_0015072)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 PVALB COL15A1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 PVALB COL15A1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 PVALB COL15A1 (Chandelier)_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[136](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=136:136)_, the term _[PCL:0015125](Phttp://purl.obolibrary.org/obo/CL_0015125)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Endo L2-5 NOSTRIN SRGN primary motor cortex endothelial cell (Homo sapiens)_ and the one in the ontology is _Endo L2-5 NOSTRIN SRGN primary motor cortex endothelial cell (Hsap)_. For reference, the given name/label by SMEs is _Endo L2-5 NOSTRIN SRGN_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[81](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=81:81)_, the term _[PCL:0015070](Phttp://purl.obolibrary.org/obo/CL_0015070)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB FAM150B primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB FAM150B primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB FAM150B_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[14](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=14:14)_, the term _[PCL:0015003](Phttp://purl.obolibrary.org/obo/CL_0015003)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 LAMP5 AARD primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 LAMP5 AARD primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 LAMP5 AARD_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[100](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=100:100)_, the term _[PCL:0015090](Phttp://purl.obolibrary.org/obo/CL_0015090)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 RORB LNX2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 RORB LNX2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 RORB LNX2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[129](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=129:129)_, the term _[PCL:0015079](Phttp://purl.obolibrary.org/obo/CL_0015079)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Oligo L2-6 OPALIN MAP6D1 primary motor cortex oligodendrocyte (Homo sapiens)_ and the one in the ontology is _Oligo L2-6 OPALIN MAP6D1 primary motor cortex oligodendrocyte precursor cell (Hsap)_. For reference, the given name/label by SMEs is _Oligo L2-6 OPALIN MAP6D1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[78](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=78:78)_, the term _[PCL:0015067](Phttp://purl.obolibrary.org/obo/CL_0015067)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2 PVALB FRZB primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2 PVALB FRZB primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2 PVALB FRZB_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[70](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=70:70)_, the term _[PCL:0015059](Phttp://purl.obolibrary.org/obo/CL_0015059)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB KCNIP2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB KCNIP2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB KCNIP2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[79](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=79:79)_, the term _[PCL:0015068](Phttp://purl.obolibrary.org/obo/CL_0015068)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 SST CLIC6 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 SST CLIC6 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 SST CLIC6_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[76](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=76:76)_, the term _[PCL:0015065](Phttp://purl.obolibrary.org/obo/CL_0015065)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3 PVALB SAMD13 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3 PVALB SAMD13 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3 PVALB SAMD13_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[126](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=126:126)_, the term _[PCL:0015116](Phttp://purl.obolibrary.org/obo/CL_0015116)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 IFNG-AS1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 IFNG-AS1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 IFNG-AS1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[113](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=113:113)_, the term _[PCL:0015103](Phttp://purl.obolibrary.org/obo/CL_0015103)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 SH2D1B primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 SH2D1B primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 SH2D1B_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[43](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=43:43)_, the term _[PCL:0015032](Phttp://purl.obolibrary.org/obo/CL_0015032)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-5 VIP CD27-AS1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-5 VIP CD27-AS1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-5 VIP CD27-AS1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[28](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=28:28)_, the term _[PCL:0015017](Phttp://purl.obolibrary.org/obo/CL_0015017)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 SST P4HA3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 SST P4HA3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 SST P4HA3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[99](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=99:99)_, the term _[PCL:0015089](Phttp://purl.obolibrary.org/obo/CL_0015089)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 THEMIS TNFAIP6 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 THEMIS TNFAIP6 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 THEMIS TNFAIP6_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[66](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=66:66)_, the term _[PCL:0015055](Phttp://purl.obolibrary.org/obo/CL_0015055)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST C4orf26 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST C4orf26 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST C4orf26_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[102](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=102:102)_, the term _[PCL:0015092](Phttp://purl.obolibrary.org/obo/CL_0015092)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 RORB MED8 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 RORB MED8 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 RORB MED8_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[125](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=125:125)_, the term _[PCL:0015115](Phttp://purl.obolibrary.org/obo/CL_0015115)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 FEZF2 RNF144A-AS1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 FEZF2 RNF144A-AS1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 FEZF2 RNF144A-AS1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[68](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=68:68)_, the term _[PCL:0015057](Phttp://purl.obolibrary.org/obo/CL_0015057)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST KLHL1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST KLHL1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST KLHL1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[46](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=46:46)_, the term _[PCL:0015035](Phttp://purl.obolibrary.org/obo/CL_0015035)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-6 VIP ZIM2-AS1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-6 VIP ZIM2-AS1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-6 VIP ZIM2-AS1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[65](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=65:65)_, the term _[PCL:0015054](Phttp://purl.obolibrary.org/obo/CL_0015054)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST DNAJC14 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST DNAJC14 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST DNAJC14_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[120](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=120:120)_, the term _[PCL:0015110](Phttp://purl.obolibrary.org/obo/CL_0015110)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 FEZF2 CSN1S1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 FEZF2 CSN1S1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 FEZF2 CSN1S1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[95](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=95:95)_, the term _[PCL:0015085](Phttp://purl.obolibrary.org/obo/CL_0015085)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 THEMIS VILL primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 THEMIS VILL primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 THEMIS VILL_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[111](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=111:111)_, the term _[PCL:0015101](Phttp://purl.obolibrary.org/obo/CL_0015101)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 C9orf135-AS1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 C9orf135-AS1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 C9orf135-AS1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[57](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=57:57)_, the term _[PCL:0015046](Phttp://purl.obolibrary.org/obo/CL_0015046)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 SST GGTLC3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 SST GGTLC3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 SST GGTLC3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[88](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=88:88)_, the term _[PCL:0015077](Phttp://purl.obolibrary.org/obo/CL_0015077)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2-3 LINC00507 DSG3 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2-3 LINC00507 DSG3 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2-3 LINC00507 DSG3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[94](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=94:94)_, the term _[PCL:0015084](Phttp://purl.obolibrary.org/obo/CL_0015084)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 RORB LAMA4 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 RORB LAMA4 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 RORB LAMA4_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[39](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=39:39)_, the term _[PCL:0015028](Phttp://purl.obolibrary.org/obo/CL_0015028)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 VIP IGDCC3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 VIP IGDCC3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 VIP IGDCC3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[72](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=72:72)_, the term _[PCL:0015061](Phttp://purl.obolibrary.org/obo/CL_0015061)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 PVALB ISG20 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 PVALB ISG20 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 PVALB ISG20_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[21](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=21:21)_, the term _[PCL:0015015](Phttp://purl.obolibrary.org/obo/CL_0015015)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 LAMP5 NMBR primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 LAMP5 NMBR primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 LAMP5 NMBR_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[123](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=123:123)_, the term _[PCL:0015113](Phttp://purl.obolibrary.org/obo/CL_0015113)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 FEZF2 PKD2L1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 FEZF2 PKD2L1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 FEZF2 PKD2L1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[121](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=121:121)_, the term _[PCL:0015111](Phttp://purl.obolibrary.org/obo/CL_0015111)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 FEZF2 ASGR2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 FEZF2 ASGR2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 FEZF2 ASGR2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[52](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=52:52)_, the term _[PCL:0015041](Phttp://purl.obolibrary.org/obo/CL_0015041)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 SST CDH3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 SST CDH3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 SST CDH3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[58](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=58:58)_, the term _[PCL:0015047](Phttp://purl.obolibrary.org/obo/CL_0015047)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2-3 SST NMU primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2-3 SST NMU primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2-3 SST NMU_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[12](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=12:12)_, the term _[PCL:0015001](Phttp://purl.obolibrary.org/obo/CL_0015001)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 LAMP5 PVRL2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 LAMP5 PVRL2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 LAMP5 PVRL2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[26](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=26:26)_, the term _[PCL:0015013](Phttp://purl.obolibrary.org/obo/CL_0015013)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 VIP WNT4 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 VIP WNT4 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 VIP WNT4_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[71](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=71:71)_, the term _[PCL:0015060](Phttp://purl.obolibrary.org/obo/CL_0015060)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB ZFPM2-AS1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB ZFPM2-AS1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB ZFPM2-AS1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[119](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=119:119)_, the term _[PCL:0015109](Phttp://purl.obolibrary.org/obo/CL_0015109)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 FEZF2 POGK primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 FEZF2 POGK primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 FEZF2 POGK_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[107](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=107:107)_, the term _[PCL:0015097](Phttp://purl.obolibrary.org/obo/CL_0015097)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 THEMIS SMYD1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 THEMIS SMYD1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 THEMIS SMYD1 (L6 IT Car3)_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[75](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=75:75)_, the term _[PCL:0015064](Phttp://purl.obolibrary.org/obo/CL_0015064)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2-5 PVALB RPH3AL primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2-5 PVALB RPH3AL primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2-5 PVALB RPH3AL_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[64](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=64:64)_, the term _[PCL:0015053](Phttp://purl.obolibrary.org/obo/CL_0015053)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST BEAN1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST BEAN1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST BEAN1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[32](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=32:32)_, the term _[PCL:0015021](Phttp://purl.obolibrary.org/obo/CL_0015021)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-3 VIP HSPB6 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-3 VIP HSPB6 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-3 VIP HSPB6_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[37](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=37:37)_, the term _[PCL:0015026](Phttp://purl.obolibrary.org/obo/CL_0015026)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2 VIP SLC6A16 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2 VIP SLC6A16 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2 VIP SLC6A16_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[27](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=27:27)_, the term _[PCL:0015016](Phttp://purl.obolibrary.org/obo/CL_0015016)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 PVALB-like SST ASIC4 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 PVALB-like SST ASIC4 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 PVALB SST ASIC4_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[115](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=115:115)_, the term _[PCL:0015105](Phttp://purl.obolibrary.org/obo/CL_0015105)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 FEZF2 FFAR4 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 FEZF2 FFAR4 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 FEZF2 FFAR4_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[89](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=89:89)_, the term _[PCL:0015078](Phttp://purl.obolibrary.org/obo/CL_0015078)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3 LAMP5 CARM1P1 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3 LAMP5 CARM1P1 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3 LAMP5 CARM1P1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[36](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=36:36)_, the term _[PCL:0015025](Phttp://purl.obolibrary.org/obo/CL_0015025)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-3 VIP CHRNA2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-3 VIP CHRNA2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-3 VIP CHRNA2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[29](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=29:29)_, the term _[PCL:0015018](Phttp://purl.obolibrary.org/obo/CL_0015018)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 SST DEFB108B primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 SST DEFB108B primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 SST DEFB108B_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[114](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=114:114)_, the term _[PCL:0015104](Phttp://purl.obolibrary.org/obo/CL_0015104)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 FEZF2 PDYN primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 FEZF2 PDYN primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 FEZF2 PDYN_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[80](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=80:80)_, the term _[PCL:0015069](Phttp://purl.obolibrary.org/obo/CL_0015069)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB GAPDHP60 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB GAPDHP60 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB GAPDHP60_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[108](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=108:108)_, the term _[PCL:0015098](Phttp://purl.obolibrary.org/obo/CL_0015098)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 OR1L8 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 OR1L8 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 OR1L8_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[45](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=45:45)_, the term _[PCL:0015034](Phttp://purl.obolibrary.org/obo/CL_0015034)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2-5 VIP SOX11 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2-5 VIP SOX11 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2-5 VIP SOX11_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[51](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=51:51)_, the term _[PCL:0015040](Phttp://purl.obolibrary.org/obo/CL_0015040)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 SST NPY primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 SST NPY primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 SST NPY (Sst Chodl)_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[106](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=106:106)_, the term _[PCL:0015096](Phttp://purl.obolibrary.org/obo/CL_0015096)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 THEMIS SNTG2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 THEMIS SNTG2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 THEMIS SNTG2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[24](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=24:24)_, the term _[PCL:0015011](Phttp://purl.obolibrary.org/obo/CL_0015011)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2 PAX6 FREM2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2 PAX6 FREM2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2 PAX6 FREM2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[84](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=84:84)_, the term _[PCL:0015073](Phttp://purl.obolibrary.org/obo/CL_0015073)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2 LAMP5 KCNG3 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2 LAMP5 KCNG3 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2 LAMP5 KCNG3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[19](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=19:19)_, the term _[PCL:0015008](Phttp://purl.obolibrary.org/obo/CL_0015008)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 PAX6 MIR101-1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 PAX6 MIR101-1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 PAX6 MIR101-1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[138](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=138:138)_, the term _[PCL:0015127](Phttp://purl.obolibrary.org/obo/CL_0015127)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Micro L1-6 TYROBP CD74 primary motor cortex microglial cell (Homo sapiens)_ and the one in the ontology is _Micro L1-6 TYROBP CD74 primary motor cortex microglial cell (Hsap)_. For reference, the given name/label by SMEs is _Micro L1-6 TYROBP CD74_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[87](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=87:87)_, the term _[PCL:0015076](Phttp://purl.obolibrary.org/obo/CL_0015076)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2-3 RORB RTKN2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2-3 RORB RTKN2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2-3 RORB RTKN2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[18](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=18:18)_, the term _[PCL:0015007](Phttp://purl.obolibrary.org/obo/CL_0015007)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-6 PAX6 LINC01497 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-6 PAX6 LINC01497 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-6 PAX6 LINC01497_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[62](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=62:62)_, the term _[PCL:0015051](Phttp://purl.obolibrary.org/obo/CL_0015051)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-3 SST FAM20A primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-3 SST FAM20A primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-3 SST FAM20A_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[48](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=48:48)_, the term _[PCL:0015037](Phttp://purl.obolibrary.org/obo/CL_0015037)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-5 VIP LINC01013 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-5 VIP LINC01013 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-5 VIP LINC01013_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[49](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=49:49)_, the term _[PCL:0015038](Phttp://purl.obolibrary.org/obo/CL_0015038)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-6 VIP UG0898H09 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-6 VIP UG0898H09 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-6 VIP UG0898H09_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[93](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=93:93)_, the term _[PCL:0015083](Phttp://purl.obolibrary.org/obo/CL_0015083)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 RORB TNNT2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 RORB TNNT2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 RORB TNNT2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[53](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=53:53)_, the term _[PCL:0015042](Phttp://purl.obolibrary.org/obo/CL_0015042)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5 SST RPL35AP11 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5 SST RPL35AP11 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5 SST RPL35AP11_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[54](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=54:54)_, the term _[PCL:0015043](Phttp://purl.obolibrary.org/obo/CL_0015043)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST ISX primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST ISX primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST ISX_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[59](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=59:59)_, the term _[PCL:0015048](Phttp://purl.obolibrary.org/obo/CL_0015048)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 SST PAWR primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 SST PAWR primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 SST PAWR_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[92](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=92:92)_, the term _[PCL:0015082](Phttp://purl.obolibrary.org/obo/CL_0015082)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3 THEMIS ENPEP primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3 THEMIS ENPEP primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3 THEMIS ENPEP_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[77](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=77:77)_, the term _[PCL:0015066](Phttp://purl.obolibrary.org/obo/CL_0015066)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 PVALB CDK20 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 PVALB CDK20 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 PVALB CDK20_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[91](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=91:91)_, the term _[PCL:0015081](Phttp://purl.obolibrary.org/obo/CL_0015081)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2-3 RORB PTPN3 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2-3 RORB PTPN3 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2-3 RORB PTPN3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[82](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=82:82)_, the term _[PCL:0015071](Phttp://purl.obolibrary.org/obo/CL_0015071)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5-6 PVALB MEPE primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5-6 PVALB MEPE primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5-6 PVALB MEPE_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[90](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=90:90)_, the term _[PCL:0015080](Phttp://purl.obolibrary.org/obo/CL_0015080)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L2-3 RORB CCDC68 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L2-3 RORB CCDC68 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L2-3 RORB CCDC68_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[47](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=47:47)_, the term _[PCL:0015036](Phttp://purl.obolibrary.org/obo/CL_0015036)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-5 VIP PHLDB3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-5 VIP PHLDB3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-5 VIP PHLDB3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[122](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=122:122)_, the term _[PCL:0015112](Phttp://purl.obolibrary.org/obo/CL_0015112)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 FEZF2 LINC01107 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 FEZF2 LINC01107 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 FEZF2 LINC01107_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[44](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=44:44)_, the term _[PCL:0015033](Phttp://purl.obolibrary.org/obo/CL_0015033)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L2-5 VIP BSPRY primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L2-5 VIP BSPRY primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L2-5 VIP BSPRY_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[105](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=105:105)_, the term _[PCL:0015095](Phttp://purl.obolibrary.org/obo/CL_0015095)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 THEMIS SLN primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 THEMIS SLN primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 THEMIS SLN_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[112](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=112:112)_, the term _[PCL:0015102](Phttp://purl.obolibrary.org/obo/CL_0015102)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 FILIP1L primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 FILIP1L primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 FILIP1L_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[56](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=56:56)_, the term _[PCL:0015045](Phttp://purl.obolibrary.org/obo/CL_0015045)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 SST OR5AH1P primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 SST OR5AH1P primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 SST OR5AH1P_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[20](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=20:20)_, the term _[PCL:0015014](Phttp://purl.obolibrary.org/obo/CL_0015014)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 LAMP5 BMP2 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 LAMP5 BMP2 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 LAMP5 BMP2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[98](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=98:98)_, the term _[PCL:0015088](Phttp://purl.obolibrary.org/obo/CL_0015088)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 THEMIS SLC22A18 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 THEMIS SLC22A18 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 THEMIS SLC22A18_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[22](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=22:22)_, the term _[PCL:0015009](Phttp://purl.obolibrary.org/obo/CL_0015009)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1 PAX6 CHRFAM7A primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1 PAX6 CHRFAM7A primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1 PAX6 CHRFAM7A_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[35](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=35:35)_, the term _[PCL:0015024](Phttp://purl.obolibrary.org/obo/CL_0015024)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-3 VIP FNDC1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-3 VIP FNDC1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-3 VIP FNDC1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[141](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=141:141)_, the term _[UBERON:0002629](http://purl.obolibrary.org/obo/UBERON_0002629)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _riangular part of inferior frontal gyrus_ and the one in the ontology is _triangular part of inferior frontal gyrus_. For reference, the given name/label by SMEs is _inferior frontal gyrus, triangular part_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[116](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=116:116)_, the term _[PCL:0015106](Phttp://purl.obolibrary.org/obo/CL_0015106)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 FEZF2 PROKR2 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 FEZF2 PROKR2 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 FEZF2 PROKR2_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[73](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=73:73)_, the term _[PCL:0015062](Phttp://purl.obolibrary.org/obo/CL_0015062)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L5 PVALB LRIG3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L5 PVALB LRIG3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L5 PVALB LRIG3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[31](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=31:31)_, the term _[PCL:0015020](Phttp://purl.obolibrary.org/obo/CL_0015020)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 VIP EXPH5 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 VIP EXPH5 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 VIP EXPH5_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[133](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=133:133)_, the term _[PCL:0015122](Phttp://purl.obolibrary.org/obo/CL_0015122)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Astro L1-6 FGFR3 AQP1 primary motor cortex glial cell (Homo sapiens)_ and the one in the ontology is _Astro L1-6 FGFR3 AQP1 primary motor cortex astrocyte (Hsap)_. For reference, the given name/label by SMEs is _Astro L1-6 FGFR3 AQP1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[130](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=130:130)_, the term _[PCL:0015119](Phttp://purl.obolibrary.org/obo/CL_0015119)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Oligo L3-6 OPALIN-like ENPP6 primary motor cortex oligodendrocyte (Homo sapiens)_ and the one in the ontology is _Oligo L3-6 OPALIN-like ENPP6 primary motor cortex oligodendrocyte precursor cell (Hsap)_. For reference, the given name/label by SMEs is _Oligo L3-6 OPALIN ENPP6_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[16](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=16:16)_, the term _[PCL:0015005](Phttp://purl.obolibrary.org/obo/CL_0015005)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-6 LAMP5 CA1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-6 LAMP5 CA1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-6 LAMP5 CA1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[50](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=50:50)_, the term _[PCL:0015039](Phttp://purl.obolibrary.org/obo/CL_0015039)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 VIP TAC3 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 VIP TAC3 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 VIP TAC3_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[128](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=128:128)_, the term _[PCL:0015118](Phttp://purl.obolibrary.org/obo/CL_0015118)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _OPC L1-6 PDGFRA COL20A1 primary motor cortex glial cell (Homo sapiens)_ and the one in the ontology is _OPC L1-6 PDGFRA COL20A1 primary motor cortex oligodendrocyte precursor cell (Hsap)_. For reference, the given name/label by SMEs is _OPC L1-6 PDGFRA COL20A1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[41](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=41:41)_, the term _[PCL:0015030](Phttp://purl.obolibrary.org/obo/CL_0015030)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L3-5 VIP HS3ST3A1 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L3-5 VIP HS3ST3A1 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L3-5 VIP HS3ST3A1_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[34](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=34:34)_, the term _[PCL:0015023](Phttp://purl.obolibrary.org/obo/CL_0015023)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Inh L1-2 VIP SCML4 primary motor cortex GABAergic interneuron (Homo sapiens)_ and the one in the ontology is _Inh L1-2 VIP SCML4 primary motor cortex GABAergic interneuron (Hsap)_. For reference, the given name/label by SMEs is _Inh L1-2 VIP SCML4_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[97](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=97:97)_, the term _[PCL:0015087](Phttp://purl.obolibrary.org/obo/CL_0015087)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L3-5 RORB LINC01202 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L3-5 RORB LINC01202 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L3-5 RORB LINC01202_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[118](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=118:118)_, the term _[PCL:0015108](Phttp://purl.obolibrary.org/obo/CL_0015108)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L6 FEZF2 KLK7 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L6 FEZF2 KLK7 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L6 FEZF2 KLK7_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[103](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=103:103)_, the term _[PCL:0015093](Phttp://purl.obolibrary.org/obo/CL_0015093)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5 THEMIS FGF10 primary motor cortex glutamatergic neuron (Homo sapiens)_ and the one in the ontology is _Exc L5 THEMIS FGF10 primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5 THEMIS FGF10_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.

1. In row _[127](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=127:127)_, the term _[PCL:0015117](Phttp://purl.obolibrary.org/obo/CL_0015117)_ has different name/label in the source ontology. The name/label in the ASCT+B table is _Exc L5-6 FEZF2 LPO primary motor cortex oligodendrocyte precursor cell (Homo sapiens)_ and the one in the ontology is _Exc L5-6 FEZF2 LPO primary motor cortex glutamatergic neuron (Hsap)_. For reference, the given name/label by SMEs is _Exc L5-6 FEZF2 LPO_. Please correct it in the columns AS/N/LABEL or CT/N/LABEL in the ASCT+B table.


## Blank ontology ID


This report provides a list of blank spreadsheet cells that often mean no ontology mapping found by the author. However, in some cases, a term with a synonym already exists. Please search in [OLS](https://www.ebi.ac.uk/ols/index).  
  
1. In row _[156](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=156:156)_, no term id was found for the name/label _frontomarginal gyrus_.

1. In row _[159](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=159:159)_, no term id was found for the name/label _supraparietal lobule_.

1. In row _[160](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=160:160)_, no term id was found for the name/label _inferior parietal lobule_.

1. In row _[160](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=160:160)_, no term id was found for the name/label _inferior parietal lobule_.

1. In row _[161](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=161:161)_, no term id was found for the name/label _inferior parietal lobule_.

1. In row _[161](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=161:161)_, no term id was found for the name/label _inferior parietal lobule_.

1. In row _[163](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=163:163)_, no term id was found for the name/label _paracentral lobule, caudal part_.

1. In row _[169](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=169:169)_, no term id was found for the name/label _transverse temporal gyrus (Heschl's gyrus)_.

1. In row _[169](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=169:169)_, no term id was found for the name/label _transverse temporal gyrus (Heschl's gyrus)_.

1. In row _[170](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=170:170)_, no term id was found for the name/label _transverse temporal gyrus (Heschl's gyrus)_.

1. In row _[170](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=170:170)_, no term id was found for the name/label _transverse temporal gyrus (Heschl's gyrus)_.

1. In row _[172](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=172:172)_, no term id was found for the name/label _perirhinal lobule_.

1. In row _[175](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=175:175)_, no term id was found for the name/label _occipitoparietal transition region_.

1. In row _[176](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=176:176)_, no term id was found for the name/label _occipitotemporal transition region_.

1. In row _[179](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=179:179)_, no term id was found for the name/label _occipitotemporal (fusiform) gyrus, occipital part_.

1. In row _[186](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=186:186)_, no term id was found for the name/label _cingulate gyrus, retrospleninal part_.

1. In row _[192](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=192:192)_, no term id was found for the name/label _uncus of parahippocampal gyrus_.

1. In row _[193](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=193:193)_, no term id was found for the name/label _hippocampal gyrus (formation)_.

1. In row _[193](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=193:193)_, no term id was found for the name/label _hippocampal gyrus (formation)_.

1. In row _[193](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=193:193)_, no term id was found for the name/label _head of hippocampus_.

1. In row _[194](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=194:194)_, no term id was found for the name/label _hippocampal gyrus (formation)_.

1. In row _[194](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=194:194)_, no term id was found for the name/label _hippocampal gyrus (formation)_.

1. In row _[194](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=194:194)_, no term id was found for the name/label _body of hippocampus_.

1. In row _[195](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=195:195)_, no term id was found for the name/label _hippocampal gyrus (formation)_.

1. In row _[195](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=195:195)_, no term id was found for the name/label _hippocampal gyrus (formation)_.

1. In row _[195](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=195:195)_, no term id was found for the name/label _subicular complex_.

1. In row _[198](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=198:198)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[198](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=198:198)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[198](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=198:198)_, no term id was found for the name/label _anterior amygdalar area_.

1. In row _[199](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=199:199)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[199](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=199:199)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[199](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=199:199)_, no term id was found for the name/label _anterior cortical nucleus_.

1. In row _[200](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=200:200)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[200](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=200:200)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[200](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=200:200)_, no term id was found for the name/label _posterior cortical nucleus_.

1. In row _[201](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=201:201)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[201](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=201:201)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[201](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=201:201)_, no term id was found for the name/label _medial nucleus_.

1. In row _[202](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=202:202)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[202](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=202:202)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[202](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=202:202)_, no term id was found for the name/label _lateral nucleus_.

1. In row _[203](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=203:203)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[203](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=203:203)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[203](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=203:203)_, no term id was found for the name/label _basolateral nucleus_.

1. In row _[204](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=204:204)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[204](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=204:204)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[204](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=204:204)_, no term id was found for the name/label _basomedial nucleus_.

1. In row _[205](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=205:205)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[205](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=205:205)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[205](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=205:205)_, no term id was found for the name/label _central nuclear group_.

1. In row _[206](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=206:206)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[206](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=206:206)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[206](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=206:206)_, no term id was found for the name/label _amygdalohippocampal area_.

1. In row _[207](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=207:207)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[207](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=207:207)_, no term id was found for the name/label _amygdaloid complex_.

1. In row _[207](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=207:207)_, no term id was found for the name/label _bed nucleus of stria terminalis_.

1. In row _[208](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=208:208)_, no term id was found for the name/label _caudate nucleus_.

1. In row _[210](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=210:210)_, no term id was found for the name/label _mucleus accumbens_.

1. In row _[214](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=214:214)_, no term id was found for the name/label _septal nuclei_.

1. In row _[216](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=216:216)_, no term id was found for the name/label _thalamus_.

1. In row _[216](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=216:216)_, no term id was found for the name/label _thalamus_.

1. In row _[216](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=216:216)_, no term id was found for the name/label _anterior nuclear complex_.

1. In row _[217](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=217:217)_, no term id was found for the name/label _thalamus_.

1. In row _[217](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=217:217)_, no term id was found for the name/label _thalamus_.

1. In row _[217](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=217:217)_, no term id was found for the name/label _mediodorsal nucleus of thalamus_.

1. In row _[218](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=218:218)_, no term id was found for the name/label _thalamus_.

1. In row _[218](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=218:218)_, no term id was found for the name/label _thalamus_.

1. In row _[218](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=218:218)_, no term id was found for the name/label _reunions nucleus of thalamus_.

1. In row _[219](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=219:219)_, no term id was found for the name/label _thalamus_.

1. In row _[219](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=219:219)_, no term id was found for the name/label _thalamus_.

1. In row _[219](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=219:219)_, no term id was found for the name/label _lateral posterior nucleus_.

1. In row _[220](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=220:220)_, no term id was found for the name/label _thalamus_.

1. In row _[220](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=220:220)_, no term id was found for the name/label _thalamus_.

1. In row _[220](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=220:220)_, no term id was found for the name/label _pulvinar of thalamus_.

1. In row _[221](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=221:221)_, no term id was found for the name/label _thalamus_.

1. In row _[221](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=221:221)_, no term id was found for the name/label _thalamus_.

1. In row _[221](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=221:221)_, no term id was found for the name/label _ventral anterior nucleus_.

1. In row _[222](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=222:222)_, no term id was found for the name/label _thalamus_.

1. In row _[222](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=222:222)_, no term id was found for the name/label _thalamus_.

1. In row _[222](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=222:222)_, no term id was found for the name/label _ventral lateral nucleus_.

1. In row _[223](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=223:223)_, no term id was found for the name/label _thalamus_.

1. In row _[223](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=223:223)_, no term id was found for the name/label _thalamus_.

1. In row _[223](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=223:223)_, no term id was found for the name/label _ventral posterior medial nucleus_.

1. In row _[224](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=224:224)_, no term id was found for the name/label _thalamus_.

1. In row _[224](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=224:224)_, no term id was found for the name/label _thalamus_.

1. In row _[224](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=224:224)_, no term id was found for the name/label _ventral posterior lateral nucleus_.

1. In row _[225](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=225:225)_, no term id was found for the name/label _thalamus_.

1. In row _[225](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=225:225)_, no term id was found for the name/label _thalamus_.

1. In row _[225](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=225:225)_, no term id was found for the name/label _lateral geniculate nuclei_.

1. In row _[226](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=226:226)_, no term id was found for the name/label _thalamus_.

1. In row _[226](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=226:226)_, no term id was found for the name/label _thalamus_.

1. In row _[226](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=226:226)_, no term id was found for the name/label _medial geniculate nuclei_.

1. In row _[227](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=227:227)_, no term id was found for the name/label _thalamus_.

1. In row _[227](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=227:227)_, no term id was found for the name/label _thalamus_.

1. In row _[227](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=227:227)_, no term id was found for the name/label _parafascicular nucleus_.

1. In row _[228](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=228:228)_, no term id was found for the name/label _thalamus_.

1. In row _[228](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=228:228)_, no term id was found for the name/label _thalamus_.

1. In row _[228](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=228:228)_, no term id was found for the name/label _centromedian nucleus_.

1. In row _[229](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=229:229)_, no term id was found for the name/label _thalamus_.

1. In row _[229](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=229:229)_, no term id was found for the name/label _thalamus_.

1. In row _[229](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=229:229)_, no term id was found for the name/label _midline nuclear complex_.

1. In row _[230](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=230:230)_, no term id was found for the name/label _thalamus_.

1. In row _[230](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=230:230)_, no term id was found for the name/label _thalamus_.

1. In row _[231](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=231:231)_, no term id was found for the name/label _thalamus_.

1. In row _[231](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=231:231)_, no term id was found for the name/label _thalamus_.

1. In row _[231](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=231:231)_, no term id was found for the name/label _habenular nuclei_.

1. In row _[232](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=232:232)_, no term id was found for the name/label _thalamus_.

1. In row _[232](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=232:232)_, no term id was found for the name/label _thalamus_.

1. In row _[232](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=232:232)_, no term id was found for the name/label _paraventricular nucleus of thalamus_.

1. In row _[233](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=233:233)_, no term id was found for the name/label _thalamus_.

1. In row _[233](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=233:233)_, no term id was found for the name/label _thalamus_.

1. In row _[234](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=234:234)_, no term id was found for the name/label _thalamus_.

1. In row _[234](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=234:234)_, no term id was found for the name/label _thalamus_.

1. In row _[234](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=234:234)_, no term id was found for the name/label _reticular formation of thalamus_.

1. In row _[235](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=235:235)_, no term id was found for the name/label _thalamus_.

1. In row _[235](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=235:235)_, no term id was found for the name/label _thalamus_.

1. In row _[235](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=235:235)_, no term id was found for the name/label _subthalamic nucleus (subthalamus)_.

1. In row _[237](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=237:237)_, no term id was found for the name/label _supraoptic region_.

1. In row _[238](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=238:238)_, no term id was found for the name/label _tuberal region_.

1. In row _[239](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=239:239)_, no term id was found for the name/label _mammillary region_.

1. In row _[239](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=239:239)_, no term id was found for the name/label _mammillary region_.

1. In row _[239](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=239:239)_, no term id was found for the name/label _mammillary nucleus_.

1. In row _[241](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=241:241)_, no term id was found for the name/label _corpus callosum (midline portion)_.

1. In row _[243](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=243:243)_, no term id was found for the name/label _internal capsule_.

1. In row _[244](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=244:244)_, no term id was found for the name/label _mammillothalamic tract_.

1. In row _[248](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=248:248)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[248](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=248:248)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[249](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=249:249)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[249](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=249:249)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[250](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=250:250)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[250](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=250:250)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[250](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=250:250)_, no term id was found for the name/label _atrium of lateral ventricle_.

1. In row _[251](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=251:251)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[251](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=251:251)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[252](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=252:252)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[252](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=252:252)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[253](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=253:253)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[253](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=253:253)_, no term id was found for the name/label _ventricle of forebrain_.

1. In row _[264](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=264:264)_, no term id was found for the name/label _paravermis of cerebellum_.

1. In row _[265](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=265:265)_, no term id was found for the name/label _lateral hemisphere of cerebellum_.

1. In row _[267](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=267:267)_, no term id was found for the name/label _cerebellar deep nuclei_.

1. In row _[272](https://docs.google.com/spreadsheets/d/1u0m_ktn6jy-V0l52pH1l_9H81nGClRbXygPEId4pU3c/edit#gid=2056967441&range=272:272)_, no term id was found for the name/label _inferior olive_.


## Terms from another ontology


This report provides a list of terms from another ontologies that we do not validate. Foundational Model of Anatomy (FMA) ontology IDs are provided when an adequate term is not found in UBERON. Also Anatomic Ontology for Human Lung Maturation (LMHA). You can also request cross-database request the same way a new term request. Please be sure if a term with a related synonym is already in the source ontologies [CL](https://www.ebi.ac.uk/ols/ontologies/cl) or [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) or [PCL](https://www.ebi.ac.uk/ols/ontologies/pcl).  
  
- No issues found.


# Relationship reports

## Relationship AS-AS report
[**Report**](class_Brain_log.tsv)
## Relationship CT-CT report
[**Report**](class_Brain_log.tsv)
## Relationship CT-AS report
[**Report**](Brain_AS_CT_strict_log.tsv)
# New CL terms
[**Report**](new_cl_terms_Brain.tsv)
# New UBERON terms
[**Report**](new_uberon_terms_Brain.tsv)
# Informative reports (valid relationships)

## Indirect relationship
[**Report**](class_Brain_indirect_log.tsv)
## Relationship AS has part CT
[**Report**](Brain_AS_has_part_CT_log.tsv)