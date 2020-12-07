import os

class Loader:

	def __init__(self):
		self.__id_counter = 0

	def load_pages(self, path, site):
		pages = []
		path = os.path.join(path, site)
		for filename in sorted(os.listdir(path)):
			filename = os.path.join(path, filename)
			pages.append( (self.__id_counter, filename) )
			self.__id_counter += 1	
		return pages

	def load_pages_from_links(self, path, site, limit):
		path = os.path.join(path, site)
		file = open(path, "r")
		content = file.read()
		file.close()
		lines = content.split(",")

		pages = []
		extracted_pages = 0
		for url in lines:
			pages.append( (self.__id_counter, url ) )
			self.__id_counter += 1
			extracted_pages += 1
			if extracted_pages >= limit:
				return pages

		return pages

	def get_last_page_id(self):
		return self.__id_counter