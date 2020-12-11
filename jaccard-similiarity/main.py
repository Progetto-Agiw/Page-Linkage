import sys
import jaccard_similiarity 
import utility


print("ENTITY LINKAGE 3000 \n")
try:
	dataset_folder, source_a, source_b, max_page = utility.read_cli_input(sys.argv)
except:
	print("usage: entity-linkage <dataset-folder> <web-site-a> <web-site-b> <page-limit>")
	exit()

jaccard_similiarity.entity_linkage(dataset_folder, source_a, source_b, max_page)