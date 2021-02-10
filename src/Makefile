ROBOT = robot # Set this to your local path (Need to switch this to take input!)

JOBS = Lung

OWL_CLASS_FILES = $(patsubst %, ../owl/ccf_%_classes.owl, $(JOBS))
OWL_IND_FILES = $(patsubst %, ../owl/ccf_%_ind.owl, $(JOBS))


all: ../owl/ccf_classes.owl ../owl/ccf_ind.owl

../templates/class_template_%.tsv: ../resources/ASCT-b_tables/%.tsv
	python template_runner.py $< $@

../templates/ind_template_%.tsv: ../resources/ASCT-b_tables/%.tsv
	python template_runner.py --ind $< $@

.PRECIOUS: ../class_template_%.tsv

../owl/ccf_%_classes.owl: ../templates/class_template_%.tsv
	echo ; echo "*** Building "$@" ***" ; echo ;
	${ROBOT} template --add-prefix "CCFH: http://ccf_tools_helpers/class_helper.owl#" \
		--add-prefix "dc: http://purl.org/dc/elements/1.1/" \
		--input helper.owl --template $< \
		--output $@

../owl/ccf_%_ind.owl: ../templates/ind_template_%.tsv
	${ROBOT} template --add-prefix "CCF: http://ccf_tools_helpers/class_helper.owl#" \
		--add-prefix "dc: http://purl.org/dc/elements/1.1/" \
		--add-prefix "ccf: https://purl.org/ccf/latest/ccf.owl" \
		--input helper.owl --template $< \
		--output $@

../owl/ccf_classes.owl: ${OWL_CLASS_FILES}
	${ROBOT} merge $(patsubst %, -i %, $^)  -o $@

../owl/ccf_ind.owl: ${OWL_IND_FILES}
	${ROBOT} merge $(patsubst %, -i %, $^)  -o $@

