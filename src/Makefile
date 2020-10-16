ROBOT = /Users/davidos/bin/robot

#class_template_Spleen_partonomy.tsv: ../resources/Spleen_partonomy.tsv
#	./template_runner.py $<

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