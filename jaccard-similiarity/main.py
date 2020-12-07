from leaves_wrapper import LeavesWrapper 
from relationship_wrapper import RelationshipWrapper
from ranker import Ranker
from loader import Loader

import sys

print("ENTITY LINKAGE 3000 \n")

if len(sys.argv) != 2:
	print("usage: entity-linkage <dataset-folder>")
	exit()

dataset_folder = sys.argv[1]

loader = Loader()
site_a = loader.load_pages(dataset_folder, "site-a")
last_page = loader.get_last_page_id()
print("Number of pages: ", last_page)
site_b = loader.load_pages(dataset_folder, "site-b")

true_relationship = [ (i,i+last_page) for i in range(last_page)  ]

sites = [site_a, site_b]

wrapper = LeavesWrapper()
ranker = Ranker()
relationship_wrapper = RelationshipWrapper(sites, wrapper, ranker)
relationship_wrapper.fit()
prediction = relationship_wrapper.predict()
print("Prediction: ", prediction)
print("Prediction accuracy: ", relationship_wrapper.accuracy(prediction, true_relationship))
print("Wrong matches: ", set(prediction) - set(true_relationship))