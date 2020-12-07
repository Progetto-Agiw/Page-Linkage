class FileReader:

	def get_page(self, uri):
		file = open(uri, "r")
		page = file.read()
		file.close()
		return page