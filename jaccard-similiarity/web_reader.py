import requests

class WebReader:

	def get_page(self, uri):
		print("[DEBUG] starting request url: ", uri)
		page = requests.get(uri)
		print("[DEBUG] page downloaded")
		return page.text