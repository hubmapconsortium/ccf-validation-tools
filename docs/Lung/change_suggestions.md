---
comments: true
---

# Suggestions on the AS-AS relations in lung table v1.3 (03/05/2023)

Please, add a comment below if you want to address any of the actions to be taken. Please, indicate the number before the comment.



## AS-AS

1. Lobe of Lung --> immune system


2. Secondary Pulmonary Lobule --> terminal bronchiole

`secondary pulmonary lobule` should have a `'has part' some 'terminal bronchiole'` PMID:3259815

3. carina of trachea --> trachea cartilage

The relationship in Uberon is on the opposite direction, needs further revision.

4. pulmonary alveolar duct --> alveolus of lung

This relationship is difficult to validate, because single alveolus can be found as scattered outpockets of the respiratory bronchiole. I would recommend to have the `alveolus of lung` in the next column of `pulmonary acinus`. [See issue 286](https://github.com/obophenotype/uberon/issues/2864)

5. Main Bronchus --> Intrapulmonary Bronchus

It is missing a connected to relationship

6. pulmonary alveolar duct --> pulmonary alveolar parenchyma

`pulmonary alveolar parenchyma` is `parenchyma and (part of some alveolus of lung)`. Therefore, mapping to `alveolus of lung` instead of `pulmonary alveolar duct` will validate.

7. trachea blood vessel --> bronchial artery


8. bronchial artery --> respiratory system arterial endothelium


9. bronchial artery --> respiratory system arterial smooth muscle


10. trachea blood vessel --> bronchial vein


11. bronchial vein --> respiratory system venous endothelium


12. bronchial vein --> respiratory system venous smooth muscle


13. lobar bronchus --> bronchus smooth muscle

It needs a 'has part' relationship.

14. lobar bronchus --> cartilage of main bronchus

It needs a 'has part' relationship.

15. lobar bronchus vasculature --> bronchial artery


16. lobar bronchus vasculature --> bronchial vein


17. lobar bronchus --> bronchus submucosal gland

It needs a 'has part' relationship.

18. lobar bronchus --> bronchus connective tissue

It needs a 'has part' relationship.

19. pulmonary artery --> respiratory system arterial endothelium

It needs a 'has part' relationship.

20. pulmonary artery --> respiratory system arterial smooth muscle

It needs a 'has part' relationship.

21. pulmonary vein --> respiratory system venous endothelium

It needs a 'has part' relationship.

22. pulmonary vein --> respiratory system venous smooth muscle

It needs a 'has part' relationship.

23. lobar bronchus --> bronchial submucosal gland

Change name to `bronchus submucosal gland` in V13-V18 and then same as number 17.

24. Segmental Bronchus --> bronchus smooth muscle

It needs a 'has part' relationship.

25. Segmental Bronchus --> lobar bronchus mesenchyme

This can't validate, as the `lobar bronchus masenchyme` should map to `lobar bronchus` only. This problem will also occur for `subsegmental bronchus` once Ubergraph gets the new release. I can add for both structures a `'has part' some 'lung mesenchyme'` axiom (UBERON:0004883) and that terms substitutes `lobar bronchus mesenchyme`.

26. Segmental Bronchus --> cartilage of main bronchus

This can't validate, as the `cartilage of main bronchus` should map to `main bronchus` only. This problem will also occur for `subsegmental bronchus` once Ubergraph gets the new release. I can add for both structures a `'has part' some 'cartilage of bronchus'` axiom (UBERON:0001956) and that terms substitutes `cartilage of main bronchus`.

27. Segmental Bronchus --> lobar bronchus vasculature

This can't validate, as the `lobar bronchus vasculature` should map to `lobar bronchus` only. I can add a relationship with `lung vasculature` (UBERON:0000102) and that terms substitutes `lobar bronchus vasculature`.

28. lobar bronchus vasculature' --> respiratory system arterial endothelium

It needs a 'has part' relationship.

29. lobar bronchus vasculature' --> respiratory system arterial smooth muscle

It needs a 'has part' relationship.

30. Segmental Bronchus --> lobar bronchus vasculature'

It is the same as 27, however the name is not correct (it has an apostrophe at the end). These are cells V131, V132, Z135 and Z136.

31. lobar bronchus vasculature --> respiratory system venous endothelium

It needs a 'has part' relationship.

32. lobar bronchus vasculature --> respiratory system venous smooth muscle

It needs a 'has part' relationship.

33. lobar bronchus --> Segmental Pulmonary Artery


34. Segmental Pulmonary Artery --> wall of pulmonary artery


35. respiratory bronchiole --> pulmonary alveolar duct

There should be a `connected to` relationship.

36. pulmonary lymphatic vessel --> respiratory system lymphatic vessel endothelium

It needs a 'has part' relationship.

37. immune system --> Pulmonary Acinus

We are still working for a solution for the immune system, but pulmonary acinus (and all child terms) are not part of the immune system. I would recommend to delete it.

38. Lobe of Lung --> pulmonary nerve plexus

It `innervate`s `respiratory system` (UBERON:3010524) or `bronchial tube` (UBERON:3010524), but not `lobe of lung`. However, `innervates` does not validate.

39. Lobe of Lung --> pulmonary capillary plexus

'part of' some 'pulmonary vascular system', which lacks relationship with respiratory system, and it needs to be added.

40. Lobe of Lung --> lung mesenchyme

It needs a 'has part' relationship.

41. Lobe of Lung --> lung connective tissue

It needs a 'has part' relationship.