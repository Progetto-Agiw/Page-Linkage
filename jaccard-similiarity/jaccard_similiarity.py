from leaves_wrapper import LeavesWrapper 
from relationship_wrapper import RelationshipWrapper
from ranker import Ranker
from loader import Loader
from file_reader import FileReader
from web_reader import WebReader
import metrics

def entity_linkage(dataset_folder, noise_folder, source_a, source_b, max_pages):
	loader = Loader()
	site_a = loader.load_pages(dataset_folder, source_a, max_pages)
	last_page = loader.get_last_page_id()
	print("Number of pages: ", last_page)
	site_b = loader.load_pages(dataset_folder, source_b, max_pages)
	true_relationship = [ (i,i+last_page) for i in range(last_page)  ]

	noise_a = loader.load_pages(noise_folder, source_a, max_pages)
	noise_b = loader.load_pages(noise_folder, source_b, max_pages)

	site_a = site_a + noise_a
	site_b = site_b + noise_b

	sites = [site_a, site_b]

	reader = FileReader()
	wrapper = LeavesWrapper(reader)
	ranker = Ranker()
	relationship_wrapper = RelationshipWrapper(sites, wrapper, ranker)

	relationship_wrapper.fit()

	prediction = relationship_wrapper.predict()
	prediction.sort(key=lambda x: x[0])
	prediction = prediction[:max_pages]
	print("Prediction: ", prediction)
	print("Prediction accuracy: ", metrics.accuracy(prediction, true_relationship))
	print("Wrong matches: ", set(prediction) - set(true_relationship))

	associations = relationship_wrapper.predict_scores()
	associations = associations[:max_pages]
	precision, recall = metrics.precision_recall(associations, true_relationship)
	print(precision)
	print(recall)
	return precision, recall