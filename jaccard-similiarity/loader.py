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