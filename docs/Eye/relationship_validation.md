---
comments: true
---

# Suggestions on the AS-AS relations in eye table v1.3 (22/3/2023)

Please, add a comment below if you want to address any of the actions to be taken. Please, indicate the number before the comment.

 

## AS-AS

N | s | slabel | user_slabel | o | olabel | user_olabel | row_number | deltaIC
-- | -- | -- | -- | -- | -- | -- | -- | --
0 | UBERON:0034713 | cranial neuron projection bundle | cranial neuron projection bundle | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | 68 | 35.4785
1 | UBERON:0003902 | retinal neural layer | retinal neural layer | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | 67 | 27.1852
3 | UBERON:0001773 | sclera | sclera | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | 66 | 18.5758
10 | UBERON:0000482 | basal lamina of epithelium | basal epithelium | UBERON:0006761 | corneo-scleral junction | corneoscleral limbus | 74 | 2.22955
27 | UBERON:0002203 | vasculature of eye | vasculature of eye | UBERON:0000966 | retina | retina | 32 | nan
41 | UBERON:0006762 | suspensory ligament of lens | ciliary zonules | UBERON:0000965 | lens | lens | 59 | nan
44 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye | eye | 64 | nan
45 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye | eye | 65 | nan
46 | UBERON:0035966 | scleral lamina cribrosa | scleral lamina cribrosa | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | 65 | nan
47 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye | eye | 66 | nan
48 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye | eye | 67 | nan
49 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye | eye | 68 | nan
50 | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye | eye | 70 | nan
51 | UBERON:0006136 | unmyelinated nerve fiber | unmyelinated nerve fiber | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | 70 | nan
52 | UBERON:0002276 | lamina of spiral limbus | lamina of spiral limbus | UBERON:0000970 | eye | eye | 74 | nan
53 | UBERON:0006761 | corneo-scleral junction | corneoscleral limbus | UBERON:0002276 | lamina of spiral limbus | lamina of spiral limbus | 74 | nan



## Actions to be taken

1. 

UBERON:0034713 | cranial neuron projection bundle | cranial neuron projection bundle | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain
-- | -- | -- | -- | -- | --


neuron projection bundle connecting eye with brain --> cranial nerve II (AKA optic nerve).  This should then validate.

2.  Lots of connections for optic nerve:


<img width="405" alt="image" src="https://user-images.githubusercontent.com/112839/226932876-8c0ae06b-b4a0-45d7-9715-ccc563515cc5.png">

UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain | UBERON:0000970 | eye | eye
-- | -- | -- | -- | -- | --
retinal neural layer | retinal neural layer | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain
UBERON:0035966 | scleral lamina cribrosa | scleral lamina cribrosa | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain.


Update Uberon term as 1.   
- [ ] Looks like some of these should have some kind of connected_to relationship in Uberon. https://github.com/obophenotype/uberon/issues/2852
       **retinal neural layer connected_to optic nerve. scleral lamina cribrosa overlaps with optic nerve.**

4.  

UBERON:0001773 | sclera | sclera | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain
-- | -- | -- | -- | -- | --

- [ ] Add adjacent_to relationship
Hard to know what type of relationship was expected.  **sclera is adjacent_to some optic nerve**

5. 

UBERON:0000482 | basal lamina of epithelium | basal epithelium | UBERON:0006761 | corneo-scleral junction | corneoscleral limbus
-- | -- | -- | -- | -- | --

- [ ] NTR 'basal epithelial layer of limbus'
Generic term in specific location.  Is there a case for adding a specific basal lamina term to Uberon?
'Limbal stem cell' is part_of some 'basal epithelial layer of limbus' . Both terms need to be added.


6. 

UBERON:0002203 | vasculature of eye | vasculature of eye | UBERON:0000966 | retina | retina
-- | -- | -- | -- | -- | --

- [ ] Table error - should be vasculature of retina UBERON:0004864 . Request change. Comment from Ellen: 
> we are striving to remove all generic "vasculature of X" type entries from all tables in favor of any blood vasculature that already has a "part of" relationship to structures.

7. 

UBERON:0006762 | suspensory ligament of lens | ciliary zonules | UBERON:0000965 | lens | lens
-- | -- | -- | -- | -- | --

- [ ] Correct relationship is continuous_with @anitacaron  to add to checks. https://github.com/hubmapconsortium/ccf-validation-tools/issues/221

8. 

UBERON:0006136 | unmyelinated nerve fiber | unmyelinated nerve fiber | UBERON:0004904 | neuron projection bundle connecting eye with brain | neuron projection bundle connecting eye with brain
-- | -- | -- | -- | -- | --

May be fixed by updating Uberon term

- [ ] check classification in Uberon

9. 

UBERON:0002276 | lamina of spiral limbus | lamina of spiral limbus | UBERON:0000970 | eye | eye
-- | -- | -- | -- | -- | --
UBERON:0006761 | corneo-scleral junction | corneoscleral limbus | UBERON:0002276 | lamina of spiral limbus | lamina of spiral limbus

Incorrect Uberon term UBERON:0002276 - is in the ear!  

- [ ] Ask experts what they intended here.









 



