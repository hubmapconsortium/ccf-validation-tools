ROBOT = robot # Set this to your local path (Need to switch this to take input!)

JOBS = Bone-Marrow Blood Brain Eye Fallopian_tube Heart Kidney Knee Large_intestine Liver Lung Lymph_node Lymph_vasculature Ovary Pancreas Peripheral_nervous_system Prostate Skin Small_intestine Spleen Thymus Ureter Urinary_bladder Uterus Blood_vasculature 
TODAY ?= $(shell date +%Y-%m-%d)
VERSION = $(TODAY)


OWL_CLASS_FILES = $(patsubst %, ../owl/ccf_%_classes.owl, $(JOBS))
OWL_ANNOTATION_FILES = $(patsubst %, ../owl/%_annotations.owl, $(JOBS))

all: ../owl/CCF_AS_CT.owl

FORCE:

../resources/ASCT-b_tables/%.json: FORCE
	python download_resource.py $* $@

../owl/%_annotations.owl ../templates/class_template_%.csv: ../resources/ASCT-b_tables/%.json
	python template_runner.py $* $< ../templates/class_template_$*.csv 2> ../logs/error_class_$*.log

.PRECIOUS: ../class_template_%.tsv

../owl/ccf_%_classes_t.owl: ../templates/class_template_%.csv
	echo ; echo "*** Building "$@" ***" ; echo ;
	${ROBOT} template --add-prefix "CCFH: http://ccf_tools_helpers/class_helper.owl#" \
		--add-prefix "dc: http://purl.org/dc/elements/1.1/" \
		--add-prefix "skos: http://www.w3.org/2004/02/skos/core#" \
		--input helper.owl --template $< \
		--output $@

../owl/ccf_%_classes.owl: ../owl/ccf_%_classes_t.owl ../owl/%_annotations.owl
	${ROBOT} merge --input helper.owl $(patsubst %, -i %, $^) -o $@ \
					convert --format json -o $*.json
	og2dot.js -s ../style/ubergraph-style.json $*.json > $*.dot 
	dot $*.dot -Tpng -Grankdir=LR > ../graphs/ccf_$*_graph.png
	rm $*.json
	rm $*.dot
	
../owl/CCF_AS_CT.owl: ${OWL_CLASS_FILES}
	${ROBOT} merge $(patsubst %, -i %, $^) \
					 annotate --ontology-iri "http://purl.org/ccf/latest/CCF_AS_CT.owl" \
					 					--version-iri "http://purl.org/ccf/releases/$(VERSION)/CCF_AS_CT.owl" \
										--output $@
	rm ${OWL_ANNOTATION_FILES}