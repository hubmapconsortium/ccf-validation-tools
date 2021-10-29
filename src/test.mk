ROBOT = robot # Set this to your local path (Need to switch this to take input!)

JOBS = Kidney

OWL_CLASS_FILES = $(patsubst %, ../owl/ccf_%_classes.owl, $(JOBS))
OWL_ANNOTATION_FILES = $(patsubst %, ../owl/%_annotations.owl, $(JOBS))

all: ../owl/CCF_AS_CT.owl

FORCE:

../resources/ASCT-b_tables/%.csv: FORCE
	python download_resource.py $* $@

../templates/class_template_%.csv: ../resources/ASCT-b_tables/%.csv
	python template_runner.py $* $< $@ 2> ../logs/error_class_$*.log

.PRECIOUS: ../class_template_%.tsv

../owl/ccf_%_classes.owl: ../templates/class_template_%.csv
	echo ; echo "*** Building "$@" ***" ; echo ;
	${ROBOT} template --add-prefix "CCFH: http://ccf_tools_helpers/class_helper.owl#" \
		--add-prefix "dc: http://purl.org/dc/elements/1.1/" \
		--add-prefix "skos: http://www.w3.org/2004/02/skos/core#" \
		--input helper.owl --template $< \
		--output $@

../owl/CCF_AS_CT.owl: ${OWL_CLASS_FILES} ${OWL_ANNOTATION_FILES}
	${ROBOT} merge $(patsubst %, -i %, $^)  -o $@
	rm ${OWL_ANNOTATION_FILES}

