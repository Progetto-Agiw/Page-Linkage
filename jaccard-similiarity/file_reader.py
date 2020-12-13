class FileReader:

	def get_page(self, uri):
		file = open(uri, "r", encoding="utf8")
		page = file.read()
		file.close()
		return page