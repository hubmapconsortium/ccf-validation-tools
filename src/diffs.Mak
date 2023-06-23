JOBS = Bone-Marrow Blood Brain Eye Fallopian_tube Heart Kidney Knee Large_intestine Liver Lung Lymph_node Lymph_vasculature Ovary Pancreas Placenta Peripheral_nervous_system Prostate Skin Small_intestine Spleen Thymus Ureter Urinary_bladder Uterus

diffs: $(patsubst %, ../diffs/%-diffs.md, $(JOBS))

../diffs/%-diffs.md: ../owl/ccf_%_classes.owl
	robot diff --labels True --left $< --right ../owl/$*_extended.owl -f markdown -o $@