import scrapy

class S24HSpider(scrapy.Spider):
    name = "s24h_stocks"
    

    def start_requests(self):
        s = 'https://mercati.ilsole24ore.com/azioni/borsa-italiana/listino-completo/'
        urls = []
        for i in range(1,17):
            urls.append(s+str(i))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
       filename = 'url_s24h.txt'
       file = open(filename, 'a')
       for player in response.xpath("//a[contains(@href, '/mercati.ilsole24ore.com/azioni/')]"):
           yield{
            'url': player.xpath("./@href").extract_first()
               }
           file.write(player.xpath("./@href").extract_first())
           file.write("\n")
       file.close() 

       
       
 
