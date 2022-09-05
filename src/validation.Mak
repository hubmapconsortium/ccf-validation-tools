ROBOT = robot

JOBS = Ovary-anatomagram Heart-anatomagram Kidney-anatomagram Lymph-anatomagram 
OLD_VERSION = False
PARSE_ASCT = False

TODAY ?= $(shell date +%Y-%m-%d)
VERSION = $(TODAY)

OWL_CLASS_FILES = $(patsubst %, ../owl/anatomagram/%_classes.owl, $(JOBS))
OWL_CLASS_SEC_FILES = $(patsubst %, ../owl/%_sec.owl, $(JOBS))
OWL_ANNOTATION_FILES = $(patsubst %, ../owl/%_annotations.owl, $(JOBS))

all: ../owl/anatomagram/Validated_AS_CT.owl 

../owl/%_annotations.owl ../owl/%_sec.owl ../templates/class_template_%.csv ../templates/%_no-valid.csv: ../resources/%.csv
	python template_runner.py $* $< ../templates/class_template_$*.csv $(OLD_VERSION) $(PARSE_ASCT) 2> ../logs/error_class_$*.log

../owl/anatomagram/%_classes_t.owl: ../templates/class_template_%.csv
	${ROBOT} template --add-prefix "CCFH: http://ccf_tools_helpers/class_helper.owl#" \
			--add-prefix "dc: http://purl.org/dc/elements/1.1/" \
			--add-prefix "skos: http://www.w3.org/2004/02/skos/core#" \
			--input helper.owl --template $< \
			--output $@

../owl/anatomagram/%_no-valid.owl: ../templates/%_no-valid.csv
	if [ $(OLD_VERSION) = False ]; then ${ROBOT} template --input helper.owl --template $< --output $@ && \
		rm $<; fi

# reduce --reasoner ELK -o ../owl/anatomagram/$*_extended.owl 
../owl/anatomagram/%_classes.owl: ../owl/anatomagram/%_classes_t.owl ../owl/%_annotations.owl ../owl/anatomagram/%_no-valid.owl ../owl/%_sec.owl
	if [ $(OLD_VERSION) = False ]; then ${ROBOT} merge --input helper.owl -i ../owl/anatomagram/$*_classes_t.owl -i ../owl/$*_annotations.owl -o $@ \
					 merge --input ../owl/$*_sec.owl \
					 merge --input ../owl/anatomagram/$*_no-valid.owl \
					 annotate --ontology-iri http://purl.org/scao/latest/$*_classes.owl \
					 convert --format json -o $*.json && \
		${ROBOT} annotate --input ../owl/$*_sec.owl --ontology-iri http://purl.org/scao/latest/$*_sec.owl convert -o $*_sec.json && \
		python graph_construct.py $*.json $*_sec.json $*_f.json "color" "green" && \
		og2dot.js -s ../style/ubergraph-style.json $*_f.json > $*.dot && \
		dot $*.dot -Tpng -Grankdir=LR > ../graphs/anatomagram/$*_graph.png && \
		dot $*.dot -Tpdf -Grankdir=LR > ../graphs/anatomagram/$*_graph.pdf && \
		rm $*.json && \
		rm $*_sec.json && \
		rm $*_f.json && \
		rm $*.dot; fi

../owl/anatomagram/Validated_AS_CT.owl: ${OWL_CLASS_FILES} ${OWL_CLASS_SEC_FILES}
	if [ $(OLD_VERSION) = False ]; then ${ROBOT} merge $(patsubst %, -i %, ${OWL_CLASS_FILES}) \
					 merge $(patsubst %, -i %, ${OWL_CLASS_SEC_FILES}) \
					 reduce --reasoner ELK \
					 annotate --ontology-iri "http://purl.org/ccf/latest/CCF_AS_CT.owl" \
					 					--version-iri "http://purl.org/ccf/releases/$(VERSION)/CCF_AS_CT.owl" \
										--output $@ && \
		rm ${OWL_ANNOTATION_FILES} && \
		rm ${OWL_CLASS_SEC_FILES}; fi