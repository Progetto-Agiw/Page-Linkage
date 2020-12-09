

class Filereader:
    
    def get_page(self, url):
        file = open(url, "r")
        content = file.read()
        content_list = content.split(",")
        file.close()
        return content_list

