from leaves_wrapper import LeavesWrapper 
from relationship_wrapper import RelationshipWrapper
from ranker import Ranker
from loader import Loader


loader = Loader()
site_a = loader.load_pages("dataset", "site-a")
site_b = loader.load_pages("dataset", "site-b")

true_relationship = [(0,3), (1,4), (2,5)]

sites = [site_a, site_b]

wrapper = LeavesWrapper()
ranker = Ranker()
relationship_wrapper = RelationshipWrapper(sites, wrapper, ranker)
relationship_wrapper.fit()
prediction = relationship_wrapper.predict()

print(relationship_wrapper.accuracy(prediction, true_relationship))
