from leaves_wrapper import LeavesWrapper 
from relationship_wrapper import RelationshipWrapper
from ranker import Ranker
import itertools

siteA = [
	(0, "dataset/john-wall-rotoworld.html"),
	(1, "dataset/luguentz-dort-rotoworld.html"),
	(2, "dataset/danilo-gallinari-rotoworld.html"),
]

siteB = [
	(3, "dataset/danilo-gallinari-nba.html"),
	(4, "dataset/john-wall-nba.html"),
	(5, "dataset/luguentz-dort-nba.html"),
]

true_relationship = [(2,3), (1,5), (0,4)]

sites = [siteA, siteB]


wrapper = LeavesWrapper()
ranker = Ranker()
relationship_wrapper = RelationshipWrapper(sites, wrapper, ranker)
relationship_wrapper.fit()
prediction = relationship_wrapper.predict()

print(relationship_wrapper.accuracy(prediction, true_relationship))
