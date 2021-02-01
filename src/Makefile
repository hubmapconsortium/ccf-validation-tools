ROBOT = robot # Set this to your local path (Need to switch this to take input!)

jobs = Heart

# TODO - add simple patsub to run this from jobs.

all: ccf_Heart_classes.owl ccf_Heart_ind.owl

class_template_Heart.tsv: ../resources/ASCT-b_tables/Heart.tsv
	python template_runner.py $<

ccf_Heart_classes.owl: class_template_Heart.tsv
	${ROBOT} template --add-prefix "CCFH: http://ccf_tools_helpers/class_helper.owl#" \
		--add-prefix "dc: http://purl.org/dc/elements/1.1/" \
		--input helper.owl --template $< \
		--output $@

ccf_Heart_ind.owl: ind_template_Heart.tsv
	${ROBOT} template --add-prefix "CCF: http://ccf_tools_helpers/class_helper.owl#" \
		--add-prefix "dc: http://purl.org/dc/elements/1.1/" \
		--add-prefix "ccf: https://purl.org/ccf/latest/ccf.owl" \
		--input helper.owl --template $< \
		--output $@

