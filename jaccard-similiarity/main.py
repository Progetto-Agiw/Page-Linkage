from leaves_wrapper import LeavesWrapper 
from relationship_wrapper import RelationshipWrapper
from ranker import Ranker
from loader import Loader
from file_reader import FileReader
from web_reader import WebReader

import sys

print("ENTITY LINKAGE 3000 \n")

if len(sys.argv) < 2:
	print("usage: entity-linkage <dataset-folder> <page-limit>")
	exit()

dataset_folder = sys.argv[1]

if len(sys.argv) >= 3:
	max_page = int(sys.argv[2])
else:
	max_page = None


loader = Loader()
site_a = loader.load_pages(dataset_folder, "site-a", max_page)
last_page = loader.get_last_page_id()
print("Number of pages: ", last_page)
site_b = loader.load_pages(dataset_folder, "site-b", max_page)
true_relationship = [ (i,i+last_page) for i in range(last_page)  ]

sites = [site_a, site_b]

reader = FileReader()
wrapper = LeavesWrapper(reader)
ranker = Ranker()
relationship_wrapper = RelationshipWrapper(sites, wrapper, ranker)
relationship_wrapper.fit()
prediction = relationship_wrapper.predict()
print("Prediction: ", prediction)
print("Prediction accuracy: ", relationship_wrapper.accuracy(prediction, true_relationship))
print("Wrong matches: ", set(prediction) - set(true_relationship))