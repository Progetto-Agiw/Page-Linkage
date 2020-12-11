from leaves_wrapper import LeavesWrapper 
from relationship_wrapper import RelationshipWrapper
from ranker import Ranker
from loader import Loader
from file_reader import FileReader
from web_reader import WebReader
import metrics
import utility
import sys

print("ENTITY LINKAGE 3000 \n")
try:
	dataset_folder, source_a, source_b, max_page = utility.read_cli_input(sys.argv)
except:
	print("usage: entity-linkage <dataset-folder> <web-site-a> <web-site-b> <page-limit>")
	exit()

loader = Loader()
site_a = loader.load_pages(dataset_folder, source_a, max_page)
last_page = loader.get_last_page_id()
print("Number of pages: ", last_page)
site_b = loader.load_pages(dataset_folder, source_b, max_page)
true_relationship = [ (i,i+last_page) for i in range(last_page)  ]

sites = [site_a, site_b]

reader = FileReader()
wrapper = LeavesWrapper(reader)
ranker = Ranker()
relationship_wrapper = RelationshipWrapper(sites, wrapper, ranker)

relationship_wrapper.fit()

prediction = relationship_wrapper.predict()
print("Prediction: ", prediction)
print("Prediction accuracy: ", metrics.accuracy(prediction, true_relationship))
print("Wrong matches: ", set(prediction) - set(true_relationship))

print("\n\n")

associations = relationship_wrapper.predict_scores()
precision, recall = metrics.precision_recall(associations, true_relationship)

print(precision)
print(recall)