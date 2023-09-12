---
comments: true
---

# Suggestions to make valid relationships in the Pancreas table v1.3 (12/09/2023)

Please, add a comment below if you want to address any of the actions to be taken. Please, indicate the number before the comment.
**IMPORTANT** The order of the two classes in these pages is the same as it is found in the tables (e.g. AS4 --> AS5)



## AS-->AS

**1 - stroma of pancreas --> pancreas mesenchyme**



**2 - extrapancreatic duct --> common bile duct**



**3 - uncinate process of pancreas --> pancreatic lobule**



**4 - ventral pancreas --> head of pancreas**



**5 - dorsal pancreas --> head of pancreas**



**6 - pancreatic lobule --> parenchyma of pancreas**



**7 - Ventral pancreatic duct --> interlobular duct**



**8 - Ventral pancreatic duct --> sphincter of hepatopancreatic ampulla**



**9 - Ventral pancreatic duct --> hepatopancreatic ampulla**



**10 - head of pancreas --> pancreatic lobule**



**11 - parenchyma of pancreas --> exocrine pancreas**



**12 - Ventral pancreatic duct --> major duodenal papilla**



**13 - interlobular duct --> intralobular duct**



**14 - Dorsal pancreatic duct --> dorsal pancreatic duct**



**15 - parenchyma of pancreas --> endocrine pancreas**



**16 - pancreatic lobule --> stroma of pancreas**



**17 - pancreas mesenchyme --> basal lamina of epithelium**



**18 - pancreas mesenchyme --> connective tissue**



**19 - common bile duct --> major duodenal papilla**



**20 - dorsal pancreas --> body of pancreas**



**21 - body of pancreas --> pancreatic lobule**



**22 - tail of pancreas --> pancreatic lobule**




## CT-->CT

**1 - pancreatic endocrine cell --> gastrin secreting cell**

This relationship is missing in the ontology and it needs to be added. However, in CL there are [type G enteroendocrine cell](http://purl.obolibrary.org/obo/CL_0000508) (G cell or gastrin cell) and I can add a subtype 'pancreatic G cell' similarly as [pancreatic A cell](http://purl.obolibrary.org/obo/CL_0000171).

**2 - pancreatic ductal cell --> epithelial cell of exocrine pancreas**

The order is inversed, a 'pancreatic ductal cell' is an 'epithelial cell of exocrine pancreas'.

**3 - pancreatic ductal cell --> pancreatic centro-acinar cell**

According to this reference [PMID:26963675](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4834238/), they are ductal cells, although they are already inside the acinus. It needs to be added in the ontology.

**4 - pancreatic ductal cell --> type EC enteroendocrine cell**

I can either add a new term or add a 'has part' relationship.

**5 - stromal cell of pancreas --> fibroblast**

As fibroblast is very general, it should be CT1 and stromal cell of pancreas is not needed in this case. Another option is remove fibroblast and add a relationship between 'stromal cell of pancreas' and [pancreatic stellate cell](http://purl.obolibrary.org/obo/CL_0002410). **Warning**: This cell is repeated twice in the same AS but with different markers.

**6 - epithelial cell of exocrine pancreas --> simple columnar epithelial cell**

This is a very general term, a specific term needs to be created, together with low columnar cell and cuboidal cell.

**7 - pancreatic ductal cell --> pancreatic goblet cell**

The relationship needs to be added in CL.


## CT-->AS

**1 - intercalated duct of pancreas --> epithelial cell of exocrine pancreas**



**2 - common bile duct --> epithelial cell of exocrine pancreas**



**3 - hepatopancreatic ampulla --> epithelial cell of exocrine pancreas**



**4 - intercalated duct of pancreas --> pancreatic centro-acinar cell**



**5 - intercalated duct of pancreas --> type EC enteroendocrine cell**



**6 - stroma of pancreas --> pancreatic stellate cell**



**7 - stroma of pancreas --> fat cell**



**8 - dorsal pancreatic duct --> smooth muscle cell**



**9 - major duodenal papilla --> simple columnar epithelial cell**



**10 - exocrine pancreas --> T cell**

Immune system*

**11 - exocrine pancreas --> B cell**

Immune system*

**12 - exocrine pancreas --> dendritic cell**

Immune system*

**13 - islet of Langerhans --> B cell**

Immune system*

**14 - islet of Langerhans --> T cell**

Immune system*

**15 - sphincter of hepatopancreatic ampulla --> smooth muscle cell**



**16 - intercalated duct of pancreas --> pancreatic goblet cell**



**17 - intercalated duct of pancreas --> pancreatic ductal cell**



**18 - exocrine pancreas --> neutrophil**

Immune system*

**19 - exocrine pancreas --> macrophage**

Immune system*

**20 - islet of Langerhans --> pancreatic epsilon cell**



**21 - islet of Langerhans --> gastrin secreting cell**



**22 - islet of Langerhans --> macrophage**

Immune system*

**23 - islet of Langerhans --> dendritic cell**

Immune system*


*Unless they are tissue resident cells (with a distinct signature from any other cell that is circulating or resident in another tissue), immune cells will not have a relation with a specific organ. For a relation to be valid, all cells of a certain cell type (e.g., dendritic cells) have to be part of a specific structure, otherwise the axiom cannot be added.