ROBOT = robot # Set this to your local path (Need to switch this to take input!)

JOBS = Bone-Marrow Blood Brain Eye Fallopian_tube Heart Kidney Knee Large_intestine Liver Lung Lymph_node Lymph_vasculature Ovary Pancreas Peripheral_nervous_system Prostate Skin Small_intestine Spleen Thymus Ureter Urinary_bladder Uterus Blood_vasculature 
TODAY ?= $(shell date +%Y-%m-%d)
VERSION = $(TODAY)
CATALOG = --catalog catalog-v001.xml

OWL_CLASS_FILES = $(patsubst %, ../owl/ccf_%_classes.owl, $(JOBS))
OWL_ANNOTATION_FILES = $(patsubst %, ../owl/%_annotations.owl, $(JOBS))
OWL_UB_SUBSET_FILES = $(patsubst %, ../owl/ub_%_ASCTB_subset.owl, $(JOBS))
OWL_CL_SUBSET_FILES = $(patsubst %, ../owl/cl_%_ASCTB_subset.owl, $(JOBS))

all: ../owl/CCF_AS_CT.owl ../owl/UB_ASCTB_subset.owl ../owl/CL_ASCTB_subset.owl

FORCE:

../resources/ASCT-b_tables/%.json: FORCE
	python download_resource.py $* $@

../owl/%_annotations.owl ../templates/class_template_%.csv ../templates/temp_ub_%_ASCTB_subset.csv ../templates/temp_cl_%_ASCTB_subset.csv ../templates/%_no-valid.csv: ../resources/ASCT-b_tables/%.json
	python template_runner.py $* $< ../templates/class_template_$*.csv 2> ../logs/error_class_$*.log

../owl/ccf_%_classes_t.owl: ../templates/class_template_%.csv
	echo ; echo "*** Building "$@" ***" ; echo ;
	${ROBOT} template --add-prefix "CCFH: http://ccf_tools_helpers/class_helper.owl#" \
		--add-prefix "dc: http://purl.org/dc/elements/1.1/" \
		--add-prefix "skos: http://www.w3.org/2004/02/skos/core#" \
		--input helper.owl --template $< \
		--output $@

../owl/ub_%_ASCTB_subset.owl: ../templates/temp_ub_%_ASCTB_subset.csv
	${ROBOT} template --input helper.owl --template $< --output $@
	rm $<

../owl/cl_%_ASCTB_subset.owl: ../templates/temp_cl_%_ASCTB_subset.csv
	${ROBOT} template --input helper.owl --template $< --output $@
	rm $<

../owl/%_no-valid.owl: ../templates/%_no-valid.csv
	${ROBOT} template --input helper.owl --template $< --output $@
	rm $<

../owl/%_ASCTB_subset.json: ../owl/ub_%_ASCTB_subset.owl ../owl/cl_%_ASCTB_subset.owl
	${ROBOT} merge $(patsubst %, -i %, $^) \
					 convert --format json -o $@

.PRECIOUS: ../owl/%_ASCTB_subset.json

../owl/ccf_%_classes.owl: ../owl/%_ASCTB_subset.json ../owl/ccf_%_classes_t.owl ../owl/%_annotations.owl ../owl/%_no-valid.owl
	${ROBOT} $(CATALOG) merge --input helper.owl -i ../owl/ccf_$*_classes_t.owl -i ../owl/$*_annotations.owl -o $@ \
					 merge --input ../owl/$*_no-valid.owl \
					 convert --format json -o $*.json
	og2dot.js -s ../style/ubergraph-style.json $*.json > $*.dot 
	dot $*.dot -Tpng -Grankdir=LR > ../graphs/ccf_$*_graph.png
	rm $*.json
	rm $*.dot

release_notes:
	python release_notes_generation.py
	rm tables_version.txt
	
../owl/CCF_AS_CT.owl: ${OWL_CLASS_FILES} release_notes
	${ROBOT} $(CATALOG) merge $(patsubst %, -i %, ${OWL_CLASS_FILES}) \
					 annotate --ontology-iri "http://purl.org/ccf/latest/CCF_AS_CT.owl" \
					 					--version-iri "http://purl.org/ccf/releases/$(VERSION)/CCF_AS_CT.owl" \
										--output $@
	rm ${OWL_ANNOTATION_FILES}

../owl/UB_ASCTB_subset.owl: ${OWL_UB_SUBSET_FILES}
	${ROBOT} $(CATALOG) merge $(patsubst %, -i %, $^) --output $@
	rm ${OWL_UB_SUBSET_FILES}

../owl/CL_ASCTB_subset.owl: ${OWL_CL_SUBSET_FILES}
	${ROBOT} $(CATALOG) merge $(patsubst %, -i %, $^) --output $@
	rm ${OWL_CL_SUBSET_FILES}


### Import ODK standard

mirror/ro.owl:
	curl -L http://purl.obolibrary.org/obo/ro.owl --create-dirs -o mirror/ro.owl --retry 4 --max-time 200 && $(ROBOT) convert -i mirror/ro.owl -o $@.tmp.owl && mv $@.tmp.owl $@
.PRECIOUS: mirror/ro.owl

imports/ro_import.owl: mirror/ro.owl imports/ro_terms.txt
	$(ROBOT) extract --input $< --term-file imports/ro_terms.txt --method BOT --output $@.tmp.owl && mv $@.tmp.owl $@
.PHONY: imports/ro_import.owl
