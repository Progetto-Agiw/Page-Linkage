import sys

import tf_idf

if len(sys.argv) < 4:
	print("usage: entity-linkage <dataset-folder> <site-a> <site-b> <page-limit>")
	exit()

dataset_folder = sys.argv[1]

site_a = sys.argv[2]
site_b = sys.argv[3]

if len(sys.argv) >= 5:
	max_page = int(sys.argv[4])
else:
	max_page = None


tf_idf.entity_linkage(dataset_folder, site_a, site_b, max_page)
