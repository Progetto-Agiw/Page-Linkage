import scrapy

class RealmSpider(scrapy.Spider):
    name = "bskRealm_players"
    

    def start_requests(self):
        urls = ['https://basketball.realgm.com/nba/players']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
       filename = 'url_realm.txt'
       file = open(filename, 'w')
       for player in response.xpath("//a[contains(@href, '/player/')]"):
           yield{
            'url': player.xpath("./@href").extract_first()
               }
           file.write("https://basketball.realgm.com/")
           file.write(player.xpath("./@href").extract_first())
           file.write(",")
       file.close() 
