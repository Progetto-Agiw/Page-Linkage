class RelationshipWrapper:

	def __init__(self, sites, page_wrapper):
		self.__wrapper = page_wrapper
		self.__leaves_sites = self.__get_leaves_from_sites(sites)

	def __get_leaves_from_sites(self, sites):
		leaves_sites = []
		for site in sites:
			site_leaves = []
			for label, page in site:
				extracted_leaves = self.__wrapper.get_all_leaves(page)
				site_leaves.append( (label, extracted_leaves) )
			leaves_sites.append(site_leaves)

		return leaves_sites


	def __get_unique_leaves(self):
		unique_leaves_sites = []
		for leaves_site in self.__leaves_sites:
			unique_leaves_site = self.__wrapper.diff(leaves_site)
			unique_leaves_sites.append(unique_leaves_site)	

		return unique_leaves_sites

	def __similiarity(self, page1, page2):
		intersection = self.__wrapper.intersection([page1, page2])
		return len(intersection)/(len(page1) + len(page2))

	def get_associations(self):
		unique_leaves = self.__get_unique_leaves()
		site1, site2 = unique_leaves[0], unique_leaves[1]
		
		associations = []

		for label1, page1 in site1:
			max_sim, max_label1, max_label2 = 0, 0, 0
			for label2, page2 in site2:
				sim = self.__similiarity(page1, page2)
				if sim > max_sim:
					max_sim, max_label1, max_label2 = sim, label1, label2
			associations.append( (max_label1, max_label2) )

		return associations