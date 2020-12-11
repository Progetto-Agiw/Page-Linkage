class Ranker:
	
	def __init__( self ):
		self.__ranking_by_page = {}
		self.__ranking_by_score = []

	def __add_to_page_rank(self, page_source, page_target, similiarity):
		if page_source in self.__ranking_by_page.keys():
			page_rank = self.__ranking_by_page[page_source]
			page_rank.append((page_target, similiarity))
			page_rank.sort( key= lambda rank: rank[1], reverse = True )
		else:
			self.__ranking_by_page[page_source] = [(page_target, similiarity)]

	def __add_to_score_rank(self, associations):
		self.__ranking_by_score = associations
		self.__ranking_by_score.sort(key=lambda association: association[2], reverse=True)


	def generate(self, associations):
		for page1, page2, sim in associations:
			self.__add_to_page_rank(page1, page2, sim)

		self.__add_to_score_rank(associations)

	def get_ranking_by_page(self):
		return self.__ranking_by_page

	def get_ranking_by_score(self):
		return self.__ranking_by_score