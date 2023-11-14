---
comments: true
---

# Suggestions to make valid relationships in the Pancreas table v1.3 (12/09/2023)

Please, add a comment below if you want to address any of the actions to be taken. Please, indicate the number before the comment.
**IMPORTANT** The order of the two classes in these pages is the same as it is found in the tables (e.g. AS4 &rarr; AS5)



## AS&rarr;AS

**1 - stroma of pancreas &rarr; pancreas mesenchyme**

Given the definition of 'pancreas mesenchyme', it might not be suitable to be included on the table, as it refers to an embryonic tissue:
> The embryonic connective tissue made up of loosely aggregated mesenchymal cells, supported by interlaminar jelly, that gives rise to the developing pancreas.

**2 - extrapancreatic duct &rarr; common bile duct**

A `connected to` relationship can be added, especially with the `hepatopancreatic ampulla`.

**3 - uncinate process of pancreas &rarr; pancreatic lobule**

I can add an axiom to 'uncinate process of pancreas' `has part some pancreatic lobule`

**4 - ventral pancreas &rarr; head of pancreas**

I can add an `overlaps` relationship.

**5 - dorsal pancreas &rarr; head of pancreas**

I can add an `overlaps` relationship.

**6 - pancreatic lobule &rarr; parenchyma of pancreas**



**7 - Ventral pancreatic duct &rarr; interlobular duct**



**8 - Ventral pancreatic duct &rarr; sphincter of hepatopancreatic ampulla**



**9 - Ventral pancreatic duct &rarr; hepatopancreatic ampulla**



**10 - head of pancreas &rarr; pancreatic lobule**

I can add an axiom to 'head of pancreas' `has part some pancreatic lobule`

**11 - parenchyma of pancreas &rarr; exocrine pancreas**

There might be an 'overlaps' relation, but it would be better that this relationship is not added and that exocrine pancreas only has a direct relationship with pancreas. It needs discussion.

**12 - Ventral pancreatic duct &rarr; major duodenal papilla**



**13 - interlobular duct &rarr; intralobular duct**



**14 - Dorsal pancreatic duct &rarr; dorsal pancreatic duct**

It is the same term (use for Papilla of Santorini)

**15 - parenchyma of pancreas &rarr; endocrine pancreas**

There might be an 'overlaps' relation, but it would be better that this relationship is not added and that endocrine pancreas only has a direct relationship with pancreas. It needs discussion.

**16 - pancreatic lobule &rarr; stroma of pancreas**

While 'overlaps' could be used, it might be preferable to not add.

**17 - pancreas mesenchyme &rarr; basal lamina of epithelium**

'basal lamina of epithelium' is too general, but a new term specific for pancreas can be used and be mapped to strom (in #1 I reccommend to remove 'pancreas mesenchyme' from the table)

**18 - pancreas mesenchyme &rarr; connective tissue**

'connective tissue' is a very general term. The definition of 'pancreas mesenchyme' is:
> The embryonic connective tissue made up of loosely aggregated mesenchymal cells, supported by interlaminar jelly, that gives rise to the developing pancreas.

Maybe this term is not appropriate for this table and there should be a new term 'pancreatic connective tissue'. If so, the subparts in the table should be evaluated to also be added in the ontology.

**19 - common bile duct &rarr; major duodenal papilla**



**20 - dorsal pancreas &rarr; body of pancreas**

I can add an `overlaps` relationship.

**21 - body of pancreas &rarr; pancreatic lobule**

I can add an axiom to 'body of pancreas' `has part some pancreatic lobule`

**22 - tail of pancreas &rarr; pancreatic lobule**

I can add an axiom to 'tail of pancreas' `has part some pancreatic lobule`


## CT&rarr;CT

**1 - pancreatic endocrine cell &rarr; gastrin secreting cell**

This relationship is missing in the ontology and it needs to be added. However, in CL there are [type G enteroendocrine cell](http://purl.obolibrary.org/obo/CL_0000508) (G cell or gastrin cell) and I can add a subtype 'pancreatic G cell' similarly as [pancreatic A cell](http://purl.obolibrary.org/obo/CL_0000171).

**2 - pancreatic ductal cell &rarr; epithelial cell of exocrine pancreas**

The order is inversed, a 'pancreatic ductal cell' is an 'epithelial cell of exocrine pancreas'.

**3 - pancreatic ductal cell &rarr; pancreatic centro-acinar cell**

According to this reference [PMID:26963675](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4834238/), they are ductal cells, although they are already inside the acinus. It needs to be added in the ontology.

**4 - pancreatic ductal cell &rarr; type EC enteroendocrine cell**

I can either add a new term or add a 'has part' relationship.

**5 - stromal cell of pancreas &rarr; fibroblast**

As fibroblast is very general, it should be CT1 and stromal cell of pancreas is not needed in this case. Another option is remove fibroblast and add a relationship between 'stromal cell of pancreas' and [pancreatic stellate cell](http://purl.obolibrary.org/obo/CL_0002410). **Warning**: This cell is repeated twice in the same AS but with different markers.

**6 - epithelial cell of exocrine pancreas &rarr; simple columnar epithelial cell**

This is a very general term, a specific term needs to be created, together with low columnar cell and cuboidal cell.

**7 - pancreatic ductal cell &rarr; pancreatic goblet cell**

The relationship needs to be added in CL.


## AS&rarr;CT

**1 - intercalated duct of pancreas &rarr; epithelial cell of exocrine pancreas**

This should be solved by CT-CT2. A new problem will arise as `pancreatic ductal cell` is a general term present in all pancreatic ducts. We need to discuss if this specific cell is different to all the other pancreatic ductal cells. From the tables it seems there are subtypes, therefore I could add new classes.

**2 - common bile duct &rarr; epithelial cell of exocrine pancreas**

This should be solved by CT-CT2. A new problem will arise as `pancreatic ductal cell` is a general term present in all pancreatic ducts. We need to discuss if this specific cell is different to all the other pancreatic ductal cells. From the tables it seems there are subtypes, therefore I could add new classes.

**3 - hepatopancreatic ampulla &rarr; epithelial cell of exocrine pancreas**

This should be solved by CT-CT2. A new problem will arise as `pancreatic ductal cell` is a general term present in all pancreatic ducts. We need to discuss if this specific cell is different to all the other pancreatic ductal cells. From the tables it seems there are subtypes, therefore I could add new classes.

**4 - intercalated duct of pancreas &rarr; pancreatic centro-acinar cell**



**5 - intercalated duct of pancreas &rarr; type EC enteroendocrine cell**



**6 - stroma of pancreas &rarr; pancreatic stellate cell**

The solution of CT-CT5 should resolve it.

**7 - stroma of pancreas &rarr; fat cell**

`fat cell` is a very general term, a new cell type can be added.

**8 - dorsal pancreatic duct &rarr; smooth muscle cell**

`smooth muscle cell` is a very general term. It probably needs a new term.

**9 - major duodenal papilla &rarr; simple columnar epithelial cell**



**10 - exocrine pancreas &rarr; T cell**

Immune system*

**11 - exocrine pancreas &rarr; B cell**

Immune system*

**12 - exocrine pancreas &rarr; dendritic cell**

Immune system*

**13 - islet of Langerhans &rarr; B cell**

Immune system*

**14 - islet of Langerhans &rarr; T cell**

Immune system*

**15 - sphincter of hepatopancreatic ampulla &rarr; smooth muscle cell**

`smooth muscle cell` is a very general term. It probably needs a new term.

**16 - intercalated duct of pancreas &rarr; pancreatic goblet cell**

These cells are present in all pancreatic ducts, and all produce mucin. Is there a specific reason why is it only present in this structure?

**17 - intercalated duct of pancreas &rarr; pancreatic ductal cell**

There are multiple cells that are subclasses of `pancreatic ductal cell`. Are the markers for this cell common in all other cells that are ductall cells and part of the `intercalated duct of pancreas`?

**18 - exocrine pancreas &rarr; neutrophil**

Immune system*

**19 - exocrine pancreas &rarr; macrophage**

Immune system*

**20 - islet of Langerhans &rarr; pancreatic epsilon cell**



**21 - islet of Langerhans &rarr; gastrin secreting cell**



**22 - islet of Langerhans &rarr; macrophage**

This needs a new term, as it is a resident macrophage that doesn't exchange with blood monocytes. PMID:27710840

**23 - islet of Langerhans &rarr; dendritic cell**

Immune system*


*Unless they are tissue resident cells (with a distinct signature from any other cell that is circulating or resident in another tissue), immune cells will not have a relation with a specific organ. For a relation to be valid, all cells of a certain cell type (e.g., dendritic cells) have to be part of a specific structure, otherwise the axiom cannot be added.