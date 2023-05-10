---
comments: true
---

# Suggestions to make valid relationships in the eye table v1.3 (08/05/2023)

Please, add a comment below if you want to address any of the actions to be taken. Please, indicate the number before the comment.

 

## AS-AS

**1 - neuron projection bundle connecting eye with brain --> cranial neuron projection bundle**

Substitute `cranial neuron projection bundle` with `cranial nerve II` UBERON:0000941 (aka optic nerve).

**2 - neuron projection bundle connecting eye with brain --> retinal neural layer**

This will be solved with AS-AS1.

**3 - neuron projection bundle connecting eye with brain --> sclera**

What relationship is expected here? 

**4 - corneo-scleral junction --> basal lamina of epithelium**

Needs a NTR 'basal epithelial layer of limbus'.

**5 - retina --> vasculature of eye**

Should be `vasculature of retina` UBERON:0004864.

**6 - lens --> suspensory ligament of lens**

Correct relationship is continuous_with @anitacaron to add to checks. https://github.com/hubmapconsortium/ccf-validation-tools/issues/221

**7 - eye --> neuron projection bundle connecting eye with brain**

AS-AS1 might solve it.

**8 - neuron projection bundle connecting eye with brain --> scleral lamina cribrosa**

`scleral lamina cribrosa` is a part of `sclera`.

**9 - neuron projection bundle connecting eye with brain --> unmyelinated nerve fiber**

It needs a 'has part' relationship.

**10 - eye --> lamina of spiral limbus**

`lamina of spiral limbus` is a ear structure, not sure why is in this table.

**11 - lamina of spiral limbus --> corneo-scleral junction**

`lamina of spiral limbus` is a ear structure, not sure why is in this table.



## CT-CT

**1 - Amacrine Cell --> GABAergic interneuron**

`GABAergic amacrine cell` CL:4030027 is more specific and validates.

~~**2 - ON-bipolar cell --> rod bipolar cell**~~

It has been fixed

**3 - medium field retinal amacrine cell --> wide field retinal amacrine cell**

A `wide field retinal amacrine cell` is not a `medium field retinal amacrine cell`

**4 - neuron --> microglial cell**

Microglial cell is not a neuron. It can be classified under `neural cell` or `central nervous system macrophage`.

**5 - neuron --> Mueller cell**

Müller cell is not a neuron. It can be classified under `neural cell`, `neuron associated cell` or `glial cell`.



## AS-CT

**1 - iris epithelium --> epithelial cell**

High level cell.

**2 - retina --> microglial cell**

High level cell.

**3 - inner nuclear layer of retina --> Amacrine Cell**

`amacrine cell` is all lowercase. `inner nuclear layer of retina` has part some `amacrine cell`, and should validate.

**4 - outer nuclear layer of retina --> retinal cone cell**

Missing 'has soma location' some 'outer nuclear layer of retina'.

**5 - outer nuclear layer of retina --> retinal rod cell**

Missing 'has soma location' some 'outer nuclear layer of retina'.

**6 - inner nuclear layer of retina --> Mueller cell**

[MCs cover the entire thickness of the retina](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8784480/#:~:text=MCs%20cover%20the%20entire%20thickness%20of%20the%20retina). The AS should be `retine` and then it will validate.

**7 - vasculature of retina --> pericyte**

It needs a NTR `retinal pericyte`.

**8 - ganglionic layer of retina --> retinal ganglion cell**

Need to validate `'has soma location' some retina`.

**9 - inner nuclear layer of retina --> retina horizontal cell**

`inner nuclear layer of retina` has part some `retina horizontal cell`, and should validate.

**10 - inner nuclear layer of retina --> retinal bipolar neuron**

`inner nuclear layer of retina` has part some `retinal bipolar neuron`, and should validate.

**11 - inner nuclear layer of retina --> ON-bipolar cell**

It will be fixed with AS-CT10.

**12 - inner nuclear layer of retina --> rod bipolar cell**

It will be fixed with AS-CT10.

**13 - lens nucleus --> secondary lens fiber**

All lens fibers structures and cells need revision.

**14 - lens fiber --> primary lens fiber**

All lens fibers structures and cells need revision.

**15 - anterior stroma of cornea --> keratocyte**

`keratocyte` is `'part of' some 'substantia propria of cornea'`(UBERON:0001777).

**16 - vasculature of retina --> retinal blood vessel endothelial cell**

it needs a SubclassOf `'part of' some 'vasculature of retina'`

**17 - inner nuclear layer of retina --> A2 amacrine cell**

It will be fixed with AS-CT3.

**18 - inner nuclear layer of retina --> starburst amacrine cell**

It will be fixed with AS-CT3.

**19 - inner nuclear layer of retina --> wide field retinal amacrine cell**

It will be fixed with AS-CT3.

**20 - lens fiber --> lens fiber cell**

All lens fibers structures and cells need revision.

**21 - lens nucleus --> lens fiber cell**

All lens fibers structures and cells need revision.

**22 - lens cortex --> lens fiber cell**

All lens fibers structures and cells need revision.

**23 - inner nuclear layer of retina --> GABAergic interneuron**

It will be fixed with AS-CT3 and CT-CT1.

**24 - anterior stroma of cornea --> telocyte**

Looking at [this reference](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5706519/), telocytes are not only in the anterior stroma of cornea.

**25 - ganglionic layer of retina --> Midget ganglion cell of retina**

It will be fixed with AS-CT8.

**26 - ganglionic layer of retina --> Parasol ganglion cell of retina**

It will be fixed with AS-CT8.

**27 - inner nuclear layer of retina --> glycinergic amacrine cell**

It will be fixed with AS-CT3.