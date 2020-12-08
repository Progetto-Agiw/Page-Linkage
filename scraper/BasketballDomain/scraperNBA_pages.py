import scrapy
from Filereader import Filereader


class NbaSpider(scrapy.Spider):
    name = "bskNBA_players"

    def start_requests(self):
        
        filereader = Filereader()
        urls = filereader.get_page("url_nba.txt")
        
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
       filename = response.url.split("/")[-1] + '.html'
       with open(filename, 'wb') as f:
           f.write(response.body)
       

           
        
        
