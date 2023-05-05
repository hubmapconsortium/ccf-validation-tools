---
comments: true
---

# Suggestions on the AS-AS relations in lung table v1.3 (03/05/2023)

Please, add a comment below if you want to address any of the actions to be taken. Please, indicate the number before the comment.



## AS-AS

**1 - Lobe of Lung --> immune system**


**2 - Secondary Pulmonary Lobule --> terminal bronchiole**

`secondary pulmonary lobule` should have a `'has part' some 'terminal bronchiole'` PMID:3259815

**3 - carina of trachea --> trachea cartilage**

The relationship in Uberon is on the opposite direction, needs further revision.

**4 - pulmonary alveolar duct --> alveolus of lung**

This relationship is difficult to validate, because single alveolus can be found as scattered outpockets of the respiratory bronchiole. I would recommend to have the `alveolus of lung` in the next column of `pulmonary acinus`. [See issue 286](https://github.com/obophenotype/uberon/issues/2864)

**5 - Main Bronchus --> Intrapulmonary Bronchus**

It is missing a connected to relationship

**6 - pulmonary alveolar duct --> pulmonary alveolar parenchyma**

`pulmonary alveolar parenchyma` is `parenchyma and (part of some alveolus of lung)`. Therefore, mapping to `alveolus of lung` instead of `pulmonary alveolar duct` will validate.

**7 - trachea blood vessel --> bronchial artery**


**8 - bronchial artery --> respiratory system arterial endothelium**


**9 - bronchial artery --> respiratory system arterial smooth muscle**


**10 - trachea blood vessel --> bronchial vein**


**11 - bronchial vein --> respiratory system venous endothelium**


**12 - bronchial vein --> respiratory system venous smooth muscle**


**13 - lobar bronchus --> bronchus smooth muscle**

It needs a 'has part' relationship.

**14 - lobar bronchus --> cartilage of main bronchus**

It needs a 'has part' relationship.

**15 - lobar bronchus vasculature --> bronchial artery**


**16 - lobar bronchus vasculature --> bronchial vein**


**17 - lobar bronchus --> bronchus submucosal gland**

It needs a 'has part' relationship.

**18 - lobar bronchus --> bronchus connective tissue**

It needs a 'has part' relationship.

**19 - pulmonary artery --> respiratory system arterial endothelium**

It needs a 'has part' relationship.

**20 - pulmonary artery --> respiratory system arterial smooth muscle**

It needs a 'has part' relationship.

**21 - pulmonary vein --> respiratory system venous endothelium**

It needs a 'has part' relationship.

**22 - pulmonary vein --> respiratory system venous smooth muscle**

It needs a 'has part' relationship.

**23 - lobar bronchus --> bronchial submucosal gland**

Change name to `bronchus submucosal gland` in V13-V18 and then same as number 17.

**24 - Segmental Bronchus --> bronchus smooth muscle**

It needs a 'has part' relationship.

**25 - Segmental Bronchus --> lobar bronchus mesenchyme**

This can't validate, as the `lobar bronchus masenchyme` should map to `lobar bronchus` only. This problem will also occur for `subsegmental bronchus` once Ubergraph gets the new release. I can add for both structures a `'has part' some 'lung mesenchyme'` axiom (UBERON:0004883) and that terms substitutes `lobar bronchus mesenchyme`.

**26 - Segmental Bronchus --> cartilage of main bronchus**

This can't validate, as the `cartilage of main bronchus` should map to `main bronchus` only. This problem will also occur for `subsegmental bronchus` once Ubergraph gets the new release. I can add for both structures a `'has part' some 'cartilage of bronchus'` axiom (UBERON:0001956) and that terms substitutes `cartilage of main bronchus`.

**27 - Segmental Bronchus --> lobar bronchus vasculature**

This can't validate, as the `lobar bronchus vasculature` should map to `lobar bronchus` only. I can add a relationship with `lung vasculature` (UBERON:0000102) and that terms substitutes `lobar bronchus vasculature`.

**28 - lobar bronchus vasculature' --> respiratory system arterial endothelium**

It needs a 'has part' relationship.

**29 - lobar bronchus vasculature' --> respiratory system arterial smooth muscle**

It needs a 'has part' relationship.

**30 - Segmental Bronchus --> lobar bronchus vasculature'**

It is the same as 27, however the name is not correct (it has an apostrophe at the end). These are cells V131, V132, Z135 and Z136.

**31 - lobar bronchus vasculature --> respiratory system venous endothelium**

It needs a 'has part' relationship.

**32 - lobar bronchus vasculature --> respiratory system venous smooth muscle**

It needs a 'has part' relationship.

**33 - lobar bronchus --> Segmental Pulmonary Artery**


**34 - Segmental Pulmonary Artery --> wall of pulmonary artery**


**35 - respiratory bronchiole --> pulmonary alveolar duct**

There should be a `connected to` relationship.

**36 - pulmonary lymphatic vessel --> respiratory system lymphatic vessel endothelium**

It needs a 'has part' relationship.

**37 - immune system --> Pulmonary Acinus**

We are still working for a solution for the immune system, but pulmonary acinus (and all child terms) are not part of the immune system. I would recommend to delete it.

**38 - Lobe of Lung --> pulmonary nerve plexus**

It `innervates` `respiratory system` (UBERON:3010524) or `bronchial tube` (UBERON:3010524), but not `lobe of lung`. However, `innervates` does not validate.

**39 - Lobe of Lung --> pulmonary capillary plexus**

'part of' some 'pulmonary vascular system', which lacks relationship with respiratory system, and it needs to be added.

**40 - Lobe of Lung --> lung mesenchyme**

It needs a 'has part' relationship.

**41 - Lobe of Lung --> lung connective tissue**

It needs a 'has part' relationship.


## CT-CT



**1 - epithelial cell of tracheobronchial tree --> airway submucosal gland duct basal cell**

This can be solved if `airway submucosal gland duct basal cell` is in CT1, and we include `'has part' some 'airway submucosal gland duct basal cell'` to `terminal ciliated ducts for tracheal submucosal gland` (term under review, so I will add before it is merged).

**2 - epithelial cell of tracheobronchial tree --> serous cell of epithelium of bronchus**

`tracheobronchial serous cell` should be an 'epithelial cell', but is is not. Once this is resolved, `serous cell of epithelium of bronchus` will be inferred as an `epithelial cell of tracheobronchial tree`

**3 - epithelial cell of tracheobronchial tree --> airway submucosal gland collecting duct epithelial cell**

Same approach as CT-CT1

**4 - epithelial cell of tracheobronchial tree --> mucus secreting cell of bronchus submucosal gland**

Same approach as CT-CT1

**5 - pulmonary interstitial fibroblast --> tracheobronchial chondrocyte**

The ID used is wrong. CL:0019002 is tracheobronchial condrocyte. `lung perichondrial fibroblast` is CL:4033026 (Cell DN21)

**6 - epithelial cell of lung --> club cell**

After [some disccussion wish Joshua](https://github.com/obophenotype/cell-ontology/pull/1934), `club cell` is now an `epithelial cell of tracheobronchial tree` (CL:0002202). The recommendation is to use it as a parent term

**7 - epithelial cell of tracheobronchial tree --> lung goblet cell**

`lung goblet cell` is an `epithelial cell of lung`

**8 - epithelial cell of lung --> lung ciliated cell**

Not all ciliated cells are epithelial cells. In the lung, are all ciliated cells also epithelial cells? If yes, the axiom can fe included.

**9 - lung endothelial cell --> vein endothelial cell of respiratory system**

The respiratory system is too broad, best solution is to add a new term (vein endothelial cell pf lung).

**10 - lung endothelial cell --> endothelial cell of respiratory system lymphatic vessel**

The respiratory system is more general than lung, probably creating a new term is the best solution (lymphatic endothelial cell of lung).


**11 - connective tissue cell --> myofibroblast cell**

A `myofibroblast cell` is primarily found in connective tissue, but not exclusively, and therefore it can't be a `connective tissue cell`. If `secondary crest myofibroblast` is moved to CT1, it will solved this validation and the `lung connective tissue` --> `connective tissue cell` validation.

**12 - myeloid dendritic cell --> plasmacytoid dendritic cell**

This relationship is tricky, as it is not clear if `plasmacytoid dendritic cell` has myeloid, lymphoid or both precursors. Alternatively, the following terms from the hierarchy can be used as parental terms:
> hematopoietic cell > leukocyte > dendritic cell > plasmacytoid dendritic cell

**13 - myeloid leukocyte --> megakaryocyte**

`myeloid leukocyte` should be substituted for `myeloid cell`(CL:0000763)

**14 - lung endothelial cell --> vein endothelial cell of respiratory system**

The respiratory system is more general than lung, probably creating a new term is the best solution (pulmonary vein endothelial cell).

**15 - lung endothelial cell --> endothelial cell of artery**

`pulmonary artery endothelial cell` CL:1001568 is more adequate. `pulmonary vascular system` has to be fixed still, as it doesn't show a relationship with lung.
