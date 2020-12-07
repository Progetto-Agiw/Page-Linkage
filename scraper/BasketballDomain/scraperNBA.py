import scrapy


class NbaSpider(scrapy.Spider):
    name = "bsk_players"

    def start_requests(self):
        urls = ['file:///home/ilaria/git/scraper/NBA_Players.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       filename = 'url_nba.txt'
       file = open(filename, 'w')
       for player in response.xpath("//a[contains(@href, '/player/')]"):
           yield{
            'url': player.xpath("./@href").extract_first()
               }
           file.write(player.xpath("./@href").extract_first())
           file.write("\n")
       file.close()
    
           


           
        
        