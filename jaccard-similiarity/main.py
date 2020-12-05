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

sites = [siteA, siteB]


wrapper = LeavesWrapper()
ranker = Ranker()
relationship_wrapper = RelationshipWrapper(sites, wrapper, ranker)
relationship_wrapper.fit()
print(relationship_wrapper.predict())