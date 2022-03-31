ROBOT = robot # Set this to your local path (Need to switch this to take input!)

JOBS = Bone-Marrow Blood Brain Eye Fallopian_tube Heart Kidney Knee Large_intestine Liver Lung Lymph_node Lymph_vasculature Ovary Pancreas Placenta Peripheral_nervous_system Prostate Skin Small_intestine Spleen Spinal_Cord Thymus Ureter Urinary_bladder Uterus Blood_vasculature
JOBS_OLD = Bone-Marrow Blood Brain Eye Fallopian_tube Heart Kidney Knee Large_intestine Liver Lung Lymph_node Lymph_vasculature Ovary Pancreas Peripheral_nervous_system Prostate Skin Small_intestine Spleen Thymus Ureter Urinary_bladder Uterus Blood_vasculature 
OLD_VERSION = False

TODAY ?= $(shell date +%Y-%m-%d)
VERSION = $(TODAY)

OWL_CLASS_FILES_OLD = $(patsubst %, ../owl/last_official_ASCTB_release/ccf_%_classes.owl, $(JOBS_OLD))
OWL_ANNOTATION_FILES_OLD = $(patsubst %, ../owl/%_annotations.owl, $(JOBS_OLD))
OWL_CLASS_FILES = $(patsubst %, ../owl/ccf_%_classes.owl, $(JOBS))
OWL_CLASS_SEC_FILES = $(patsubst %, ../owl/%_sec.owl, $(JOBS))
OWL_ANNOTATION_FILES = $(patsubst %, ../owl/%_annotations.owl, $(JOBS))
OWL_UB_SUBSET_FILES = $(patsubst %, ../owl/ub_%_ASCTB_subset.owl, $(JOBS))
OWL_CL_SUBSET_FILES = $(patsubst %, ../owl/cl_%_ASCTB_subset.owl, $(JOBS))
JSON_CLASSES_SUBSET = $(patsubst %, ../owl/%_ASCTB_subset.json, $(JOBS))

all: ../owl/CCF_AS_CT.owl ../owl/last_official_ASCTB_release/CCF_AS_CT.owl ../owl/UB_ASCTB_subset.owl ../owl/CL_ASCTB_subset.owl

../resources/ASCT-b_tables/%.json:
	python download_resource.py $* $@ $(OLD_VERSION)

../owl/%_annotations.owl ../owl/%_sec.owl ../templates/class_template_%.csv ../templates/temp_ub_%_ASCTB_subset.csv ../templates/temp_cl_%_ASCTB_subset.csv ../templates/%_no-valid.csv: ../resources/ASCT-b_tables/%.json
	python template_runner.py $* $< ../templates/class_template_$*.csv $(OLD_VERSION) 2> ../logs/error_class_$*.log

../owl/ccf_%_classes_t.owl: ../templates/class_template_%.csv
	${ROBOT} template --add-prefix "CCFH: http://ccf_tools_helpers/class_helper.owl#" \
			--add-prefix "dc: http://purl.org/dc/elements/1.1/" \
			--add-prefix "skos: http://www.w3.org/2004/02/skos/core#" \
			--input helper.owl --template $< \
			--output $@

../owl/ub_%_ASCTB_subset.owl: ../templates/temp_ub_%_ASCTB_subset.csv
	if [ $(OLD_VERSION) = False ]; then ${ROBOT} template --input helper.owl --template $< --output $@ && \
		rm $<; fi

../owl/cl_%_ASCTB_subset.owl: ../templates/temp_cl_%_ASCTB_subset.csv
	if [ $(OLD_VERSION) = False ]; then ${ROBOT} template --input helper.owl --template $< --output $@ && \
		rm $<; fi

../owl/%_no-valid.owl: ../templates/%_no-valid.csv
	if [ $(OLD_VERSION) = False ]; then ${ROBOT} template --input helper.owl --template $< --output $@ && \
		rm $<; fi

../owl/%_ASCTB_subset.json: ../owl/ub_%_ASCTB_subset.owl ../owl/cl_%_ASCTB_subset.owl
	if [ $(OLD_VERSION) = False ]; then ${ROBOT} merge $(patsubst %, -i %, $^) \
					 convert --format json -o $@; fi

.PRECIOUS: ../owl/%_ASCTB_subset.json

../owl/ccf_%_classes.owl: ../owl/ccf_%_classes_t.owl ../owl/%_annotations.owl ../owl/%_no-valid.owl ../owl/%_sec.owl
	if [ $(OLD_VERSION) = False ]; then ${ROBOT} merge --input helper.owl -i ../owl/ccf_$*_classes_t.owl -i ../owl/$*_annotations.owl -o $@ \
					 merge --input ../owl/$*_sec.owl \
					 reduce --reasoner ELK -o ../owl/$*_extended.owl \
					 merge --input ../owl/$*_no-valid.owl \
					 convert --format json -o $*.json && \
		${ROBOT} convert --input ../owl/$*_sec.owl -o $*_sec.json && \
		python graph_construct.py $*.json $*_sec.json $*_f.json "color" "green" && \
		og2dot.js -s ../style/ubergraph-style.json $*_f.json > $*.dot && \
		dot $*.dot -Tpng -Grankdir=LR > ../graphs/ccf_$*_graph.png && \
		rm $*.json && \
		rm $*_sec.json && \
		rm $*_f.json && \
		rm $*.dot; fi

../owl/last_official_ASCTB_release/ccf_%_classes.owl: ../owl/ccf_%_classes_t.owl ../owl/%_annotations.owl
	if [ $(OLD_VERSION) = True ]; then ${ROBOT} merge --input helper.owl -i ../owl/ccf_$*_classes_t.owl -i ../owl/$*_annotations.owl -o $@ \
					 convert --format json -o $*.json && \
		og2dot.js -s ../style/ubergraph-style.json $*.json > $*.dot &&\
		dot $*.dot -Tpng -Grankdir=LR > ../graphs/last_official_ASCTB_release/ccf_$*_graph.png && \
		dot $*.dot -Tpdf -Grankdir=LR > ../graphs/last_official_ASCTB_release/ccf_$*_graph.pdf && \
		rm $*.json && \
		rm $*.dot; fi

release_notes:
	python release_notes_generation.py
	rm tables_version.txt
	
../owl/CCF_AS_CT.owl: ${OWL_CLASS_FILES} ${OWL_CLASS_SEC_FILES} release_notes
	if [ $(OLD_VERSION) = False ]; then ${ROBOT} merge $(patsubst %, -i %, ${OWL_CLASS_FILES}) \
					 merge $(patsubst %, -i %, ${OWL_CLASS_SEC_FILES}) \
					 reduce --reasoner ELK \
					 annotate --ontology-iri "http://purl.org/ccf/latest/CCF_AS_CT.owl" \
					 					--version-iri "http://purl.org/ccf/releases/$(VERSION)/CCF_AS_CT.owl" \
										--output $@ && \
		rm ${OWL_ANNOTATION_FILES} && \
		rm ${OWL_CLASS_SEC_FILES}; fi

../owl/last_official_ASCTB_release/CCF_AS_CT.owl: ${OWL_CLASS_FILES_OLD}
	if [ $(OLD_VERSION) = True ]; then ${ROBOT} merge $(patsubst %, -i %, $^) \
						annotate --ontology-iri "http://purl.org/ccf/latest/CCF_AS_CT.owl" \
											--version-iri "http://purl.org/ccf/releases/$(VERSION)/CCF_AS_CT.owl" \
											--output $@ && \
		rm ${OWL_ANNOTATION_FILES_OLD}; fi

../owl/UB_ASCTB_subset.owl: ${OWL_UB_SUBSET_FILES} ${JSON_CLASSES_SUBSET}
	if [ $(OLD_VERSION) = False ]; then ${ROBOT} merge $(patsubst %, -i %, ${OWL_UB_SUBSET_FILES}) --output $@ && \
		rm ${OWL_UB_SUBSET_FILES}; fi

../owl/CL_ASCTB_subset.owl: ${OWL_CL_SUBSET_FILES}
	if [ $(OLD_VERSION) = False ]; then ${ROBOT} merge $(patsubst %, -i %, $^) --output $@ && \
		rm ${OWL_CL_SUBSET_FILES}; fi

official_release:
	make ../owl/CCF_AS_CT.owl ../owl/UB_ASCTB_subset.owl ../owl/CL_ASCTB_subset.owl -B
.PHONY: official_release

last_official_release:
	make ../owl/last_official_ASCTB_release/CCF_AS_CT.owl OLD_VERSION=True -B
.PHONY: last_official_release
