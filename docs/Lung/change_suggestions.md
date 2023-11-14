---
comments: true
---

# Suggestions to make valid relationships in the lung table v1.3 (30/05/2023)

Please, add a comment below if you want to address any of the actions to be taken. Please, indicate the number before the comment.
**IMPORTANT** The order of the two classes in these pages is the same as it is found in the tables (e.g. AS4 &rarr; AS5)



## AS&rarr;AS

**1 - Secondary Pulmonary Lobule &rarr; terminal bronchiole**

`secondary pulmonary lobule` should be `'part of' some 'terminal bronchiole'` PMID:3259815 Status: [#2953](https://github.com/obophenotype/uberon/pull/2953)

**2 - subsegmental bronchus &rarr; cartilage of bronchus**

It needs a 'has part' relationship. Status: Completed [PR 204](https://github.com/obophenotype/uberon/issues/2904)

**3 - pulmonary alveolar duct &rarr; alveolus of lung**

This relationship is difficult to validate, because single alveolus can be found as scattered outpockets of the respiratory bronchiole. I would recommend to have the `alveolus of lung` in the next column of `pulmonary acinus`. [See issue 286](https://github.com/obophenotype/uberon/issues/2864)

New hierarchy proposed (03/06/2023): 
*Secondary pulmonary lobule &rarr; terminal bronchiole &rarr; with cells and ECM that compose that structure*

*Secondary pulmonary lobule &rarr;terminal bronchiole &rarr; pulmonary acinus &rarr; respiratory bronchiole &rarr; with the cells and ECM that compose the respiratory bronchiole*

*Secondary pulmonary lobule &rarr;terminal bronchiole &rarr; pulmonary acinus &rarr; respiratory bronchiole &rarr; alveolus of respiratory bronchiole (new term - or leave as alveolus of lung but this will come up again as part for the pulmonary acinus) &rarr; with the cells and ECM that compose that simple alveolar structure*

*Secondary pulmonary lobule &rarr;terminal bronchiole &rarr; pulmonary acinus &rarr; alveolar duct (that are vital to but not part for respiratory bronchioles) &rarr; with the cells and ECM that compose the alveolar ducts*

*Secondary pulmonary lobule &rarr;terminal bronchiole &rarr; pulmonary acinus &rarr; alveolus of lung &rarr;pulmonary alveolar parenchyma &rarr; with the cells and ECM that compose the parenchyma*



**4 - subsegmental bronchus &rarr; lobar bronchus mesenchyme**

It needs a new term (either general `bronchus mesenchyme` and add 'has part' axiom, or `subsegmental bronchus mesenchyme`).  Status: temporally it has been added 'has part' some 'lung mesenchyme' [PR 204](https://github.com/obophenotype/uberon/issues/2904). However, GP requested NTR “mesenchyme of subsegmental bronchus”.

**5 - subsegmental bronchus &rarr; bronchus smooth muscle**

It needs a 'has part' relationship. Status: Completed [PR 204](https://github.com/obophenotype/uberon/issues/2904)

**6 - lung &rarr; immune system**

No actions for now.

**7 - epithelium of segmental bronchus &rarr; bronchus submucosal gland**

The `bronchus submucosal gland` are not part of an epithelium. I can add a `'has part' some 'bronchus sumucosal gland'` to `segmental bronchus`, and this term replaces `epithelium of segmental bronchus`. Status: Has part completed, class needs to be changed [PR 204](https://github.com/obophenotype/uberon/issues/2904)

**8 - pulmonary alveolar duct &rarr; pulmonary alveolar parenchyma**

`pulmonary alveolar parenchyma` is `parenchyma and (part of some alveolus of lung)`. Therefore, mapping to `alveolus of lung` instead of `pulmonary alveolar duct` will validate. Status: completed

**9 - Tracheobronchial tree &rarr; pulmonary nerve plexus**

It should have an `overlaps` relation.

**10 - lobar bronchus &rarr; bronchus submucosal gland**

It needs a 'has part' relationship. Status: Completed [PR 204](https://github.com/obophenotype/uberon/issues/2904)

**11 - lobar bronchus &rarr; bronchus connective tissue**

There is a `lobar bronchus connective tissue` UBERON:0003591. Status: completed

**12 - lobar bronchus &rarr; bronchus smooth muscle**

It needs a 'has part' relationship. Status: Completed [PR 204](https://github.com/obophenotype/uberon/issues/2904)

**13 - lobar bronchus &rarr; cartilage of bronchus**

It needs a 'has part' relationship. Status: Completed [PR 204](https://github.com/obophenotype/uberon/issues/2904)

**14 - Segmental Bronchus &rarr; bronchus smooth muscle**

It needs a 'has part' relationship. Status: Completed [PR 204](https://github.com/obophenotype/uberon/issues/2904)

**15 - Segmental Bronchus &rarr; cartilage of bronchus**

I can add for both structures a `'has part' some 'cartilage of bronchus'` axiom (UBERON:0001956) (also for subsegmental bronchus). Status: Completed [PR 204](https://github.com/obophenotype/uberon/issues/2904)

**16 - Segmental Bronchus &rarr; lobar bronchus mesenchyme**

This can't validate, as the `lobar bronchus masenchyme` should map to `lobar bronchus` only. This problem will also occur for `subsegmental bronchus` once Ubergraph gets the new release. I can add for both structures a `'has part' some 'lung mesenchyme'` axiom (UBERON:0004883) and that terms substitutes `lobar bronchus mesenchyme`. Second part  Status: Completed [PR 204](https://github.com/obophenotype/uberon/issues/2904)

**17 - subsegmental bronchus &rarr; epithelium of segmental bronchus**

The correct term would be `epithelium of bronchus` (UBERON:0002031). It needs a `has part` axiom. However, in this case a new term might be beneficial.

**18 - subsegmental bronchus &rarr; primary bronchiole**

Primary bronchiole needs to be edited. This is tricky, because according of some literature, there is a ssub-subsegmental bronchus, and therefore any axiom would be not true.

**19 - respiratory bronchiole &rarr; pulmonary alveolar duct**

There should be a `connected to` relationship.

**20 - pulmonary alveolar parenchyma &rarr; pulmonary capillary**

Not sure of the expected relationship expected.

**21 - pulmonary lymphatic vessel &rarr; respiratory system lymphatic vessel endothelium**

It needs a 'has part' relationship. Status: Completed [PR 204](https://github.com/obophenotype/uberon/issues/2904)

**22 - immune system &rarr; Pulmonary Acinus**

We are still working for a solution for the immune system, but pulmonary acinus (and all child terms) are not part of the immune system. I would recommend to delete it or 'immune system' as last AS column.



## CT&rarr;CT



**No issues**



## AS&rarr;CT

**1 - terminal bronchiole epithelium &rarr; club cell**

It needs a 'has part' relationship.

**2 - epithelium of segmental bronchus &rarr; club cell**

It needs a 'has part' relationship.

**3 - epithelium of respiratory bronchiole &rarr; club cell**

It needs a 'has part' relationship.

**4 - epithelium of bronchiole &rarr; club cell**

It needs a 'has part' relationship.

**5 - pulmonary alveolar parenchyma &rarr; type I pneumocyte**

It needs a 'has part' relationship.

**6 - pulmonary alveolar parenchyma &rarr; type II pneumocyte**

It needs a 'has part' relationship.

**7 - epithelium of segmental bronchus &rarr; brush cell of bronchus**

It needs a 'has part' relationship.

**8 - epithelium of segmental bronchus &rarr; basal epithelial cell of tracheobronchial tree**

It needs a 'has part' relationship.

**9 - epithelium of lobar bronchus &rarr; basal epithelial cell of tracheobronchial tree**

It needs a 'has part' relationship.

**10 - epithelium of lobar bronchus &rarr; ciliated cell of the bronchus**

It needs a 'has part' relationship.

**11 - epithelium of segmental bronchus &rarr; ciliated cell of the bronchus**

It needs a 'has part' relationship.

**12 - bronchus smooth muscle &rarr; bronchial smooth muscle cell**

It needs a 'has part' relationship.

**13 - respiratory system venous endothelium &rarr; adult endothelial progenitor cell**

The textual definition of an `adult endothelial progenitor cell` is the following:
> An adult angioblastic cell released from the bone marrow, or from the kidney in some teleost species, capable of blood circulation and participation in angiogenesis by differentiating into blood vessel endothelial cells.

Is this cell type meant to be resident or circulating? In case it is a resident type, it would need a new term. In case it is circulating, we will need a similar soultion as immune cells.

**14 - respiratory system lymphatic vessel endothelium &rarr; endothelial cell of respiratory system lymphatic vessel**

It is missing a `part of` relationship.

**15- pulmonary alveolar parenchyma &rarr; lung pericyte**

It needs a 'has part' relationship.

**16 - pulmonary nerve plexus &rarr; sympathetic neuron**

It needs a 'has part' relationship.

**17 - epithelium of segmental bronchus &rarr; pulmonary ionocyte**

It needs a 'has part' relationship.

**18 - epithelium of lobar bronchus &rarr; pulmonary ionocyte**

It needs a 'has part' relationship.

**19 - cartilage of bronchus &rarr; tracheobronchial chondrocyte**

It needs a 'has part' relationship.

**20 - lobar bronchus mesenchyme &rarr; tracheobronchial smooth muscle cell**

It needs a 'has part' relationship.

**21 - epithelium of segmental bronchus &rarr; lung goblet cell**

It needs a 'has part' relationship.

**22 - epithelium of segmental bronchus &rarr; lung neuroendocrine cell**

It needs a 'has part' relationship. This is a very general term, are there lung neuroendocrine cell subtypes needed?

**23 - epithelium of bronchiole &rarr; lung ciliated cell**

It needs a 'has part' relationship.

**24 - terminal bronchiole epithelium &rarr; lung ciliated cell**

It needs a 'has part' relationship.

**25 - pulmonary capillary &rarr; alveolar capillary type 1 endothelial cell**

According to  [this reference](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7721049/) it is probably missing a `part of` relationship.

**26 - pulmonary capillary &rarr; alveolar capillary type 2 endothelial cell**

According to  [this reference](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7721049/) it is probably missing a `part of` relationship.


**27 - pulmonary alveolar parenchyma &rarr; alveolar type 1 fibroblast cell**

It is missing a `part of` [relationship](https://www.annualreviews.org/doi/10.1146/annurev.physiol.59.1.43?url_ver=Z39.88-2003&rfr_id=ori%3Arid%3Acrossref.org&rfr_dat=cr_pub++0pubmed).

**28 - pulmonary alveolar parenchyma &rarr; alveolar type 2 fibroblast cell**

It is missing a `part of` [relationship](https://pubmed.ncbi.nlm.nih.gov/33624948/). Include synonym 'resident interstitial lung fibroblasts'.

**29 - respiratory system venous endothelium &rarr; vein endothelial cell of respiratory system**

It is missing a `part of` relationship.

**30 - smooth muscle tissue of terminal bronchiole &rarr; bronchiolar smooth muscle cell**

It needs a 'has part' relationship.

**31 - smooth muscle tissue of bronchiole &rarr; bronchiolar smooth muscle cell**

It is missing a `part of` relationship.

**32 - smooth muscle tissue of respiratory bronchiole &rarr; bronchiolar smooth muscle cell**

It needs a 'has part' relationship.

**33 - immune system &rarr; lung megakaryocyte**

Megakaryocytes are not considered to be part of the immune system. It can directly map to lung.