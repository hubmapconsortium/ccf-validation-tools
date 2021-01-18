ROBOT = robot # Set this to your local path (Need to switch this to take input!)

jobs = Heart


all: ccf_Kidney_classes.owl ccf_kidney_ind.owl

class_template_Kidney_partonomy.tsv: ../resources/Kidney_partonomy.tsv
	python template_runner.py $<

ccf_Kidney_classes.owl: class_template_Kidney_partonomy.tsv
	${ROBOT} template --add-prefix "CCFH: http://ccf_tools_helpers/class_helper.owl#" \
		--add-prefix "dc: http://purl.org/dc/elements/1.1/" \
		--input helper.owl --template $< \
		--output $@

ccf_kidney_ind.owl: ind_template_Kidney_partonomy.tsv
	${ROBOT} template --add-prefix "CCF: http://ccf_tools_helpers/class_helper.owl#" \
		--add-prefix "dc: http://purl.org/dc/elements/1.1/" \
		--add-prefix "ccf: https://purl.org/ccf/latest/ccf.owl" \
		--input helper.owl --template $< \
		--output $@

