class Ranker:
	
	def __init__( self ):
		pass

	def __add_to_page_rank(self, page_source, page_target, similiarity):
		if page_source in self.__ranking.keys():
			page_rank = self.__ranking[page_source]
			page_rank.append((page_target, similiarity))
			page_rank.sort( key= lambda rank: rank[1], reverse = True )
		else:
			self.__ranking[page_source] = [(page_target, similiarity)]

	def generate(self, associations):
		self.__ranking = {}
		for page1, page2, sim in associations:
			self.__add_to_page_rank(page1, page2, sim)

	def get_ranking(self):
		return self.__ranking