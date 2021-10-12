### Functional spec:

1. Retrieve tables from google sheets
2. Convert to triples (include user provided ontology labels and user preferred labels)
3. Validate against UberGraph & dump warnings to log files:
    * Check relations: subClassOf (closure graph) ; part_of & overlaps (redundant graph)   
    * Cross check ontology term labels provided (we might want to review this if too noisy)
    * Cross check expert preferred names against names and synonyms associated with provided ID
4. OWL generation:
    * Add validated terms (declarations)  # Do we need to integrate this with temp new term ID generation system?
    * validated triples -> annotated OWL axioms.  Tech spec: use ROBOT templates.  It is convenient to generate robot template TSVs as part of the validation step.  # Open question - how do we deal with triples that don't validate?
    * Annotations on ontology terms (and annotations on these annotations).  Tech spec: Use SPARQL query -> SPARQL construct.
    * Merge all OWL files -> product (Naming co-ordinated with @JosefHardi) Tech Spec: Use ROBOT merge.
