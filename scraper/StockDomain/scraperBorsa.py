import scrapy

class S24HSpider(scrapy.Spider):
    name = "s24h_stocks"
    

    def start_requests(self):
        urls = ['https://www.teleborsa.it/Quotazioni/Azioni-Italia',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/B',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/C',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/D',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/E',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/F',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/G',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/H',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/K',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/I',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/L',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/M',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/N',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/O',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/P',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/Q',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/R',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/S',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/T',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/U',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/V',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/W',
                'https://www.teleborsa.it/Quotazioni/Azioni-Italia/Z']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
       filename = 'url_teleborsa.txt'
       file = open(filename, 'a')
       for player in response.xpath("//a[contains(@href, '/azioni/')]"):
           yield{
            'url': player.xpath("./@href").extract_first()
               }
           file.write('https://teleborsa.it')
           file.write(player.xpath("./@href").extract_first())
           file.write("\n")
       file.close() 

    
  
    
    
