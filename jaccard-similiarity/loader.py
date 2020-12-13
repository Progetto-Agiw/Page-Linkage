import os

class Loader:

	def __init__(self):
		self.__id_counter = 0

	def load_pages(self, path, site, limit):
		pages = []
		path = os.path.join(path, site)
		files = sorted(os.listdir(path))[:limit]
		for filename in files:
			filename = os.path.join(path, filename)
			pages.append( (self.__id_counter, filename) )
			self.__id_counter += 1	
		return pages

	def load_pages_from_links(self, path, site, limit):
		path = os.path.join(path, site)
		file = open(path, "r", encoding="utf8")
		content = file.read()
		file.close()
		lines = content.split(",")

		pages = []
		lines = lines[:limit]

		for url in lines:
			pages.append( (self.__id_counter, url ) )
			self.__id_counter += 1

		return pages

	def get_last_page_id(self):
		return self.__id_counter