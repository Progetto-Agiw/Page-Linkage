import requests
from lxml import html

class Wrapper:

	def get_all_leaves(self, path):
		file = open(path, "r")
		page = file.read()
		file.close()
		dom_tree = html.fromstring(page)
		all_leaves = dom_tree.xpath("//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()")
		return all_leaves

	def remove_label_from_leaves(self, leaves):
		return list(map(lambda key_leaf: key_leaf[1], leaves))

	def intersection(self, site_leaves):
		intersection = set(site_leaves[0])
		for site in site_leaves:
			leaves_set = set(site)
			intersection = intersection & leaves_set
		return intersection

	def get_unique_leaves(self, site_leaves, intersection):
		unique_site_leaves = []
		for label, page in site_leaves:
			unique_page_leaves = []
			for element in page:
				if element not in intersection:
					unique_page_leaves.append(element)
			unique_site_leaves.append( (label, unique_page_leaves) )
		return unique_site_leaves

	def diff(self, site_leaves):
		site_leaves_pages = self.remove_label_from_leaves(site_leaves)
		intersection = self.intersection(site_leaves_pages)
		return self.get_unique_leaves(site_leaves, intersection)