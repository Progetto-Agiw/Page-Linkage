import scrapy
import time
from Filereader import Filereader


class NbaSpider(scrapy.Spider):
    name = "bskNBA_players"

    def start_requests(self):
        
        filereader = Filereader()
        urls = filereader.get_page("url_nba.txt")
        #urls = ['https://www.nba.com/player/1628035/alfonzo-mckinnie/','https://www.nba.com/player/1630173/precious-achiuwa/']
        new_urls = []
        for url in urls:
            url = url[ : (url.rfind('/')-1)]
            new_url = url[ :(url.rfind('.com/')+5)] + 'stats/' + url[(url.rfind('.com/')+5):(url.rfind('/'))] + '/career'
            new_urls.append(new_url)
                
        for url in new_urls:
            time.sleep(0.5)
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
       #filename = response.url.split("/")[-1] + '.html'
       filename = response.url[33:(response.url.rfind('/'))] + '.html'
       with open(filename, 'wb') as f:
           f.write(response.body)
       

           
        
        
