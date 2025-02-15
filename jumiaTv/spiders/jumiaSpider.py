import scrapy
from jumiaTv.items import JumiatvItem
class JumiaspiderSpider(scrapy.Spider):
    name = "jumiaSpider"
    number_page = 2
    start_urls = ["https://www.jumia.ma/tv-home-cinema-lecteurs/#catalog-listing"]

    custom_settings = {
            'FEEDS': {
                'Jumiadata.json': {'format': 'json', 'overwrite': True},
            }
    }
    def parse(self, response):
        articles = response.css("article.prd")
        for article in articles :
            relative_article_url = article.css("article a.core ::attr(href)").get()
            article_url = 'https://www.jumia.ma'  + relative_article_url
            yield response.follow(article_url, callback = self.parse_page) 

        if 2 > self.number_page :
            next_page_url = 'https://www.jumia.ma/tv-home-cinema-lecteurs/?page=' + str(self.number_page) + '#catalog-listing'
            self.number_page = self.number_page + 1
            yield response.follow(next_page_url, callback = self.parse)


    def parse_page(self, response):
        
        article_item = JumiatvItem()
        Descriptif_technique = response.css(".-lsn ::text").getall()
        article_item['name'] = response.css("h1.-fs20.-pts.-pbxs ::text").get()
        article_item['marque'] = response.css("div.-phs ._more:nth-child(1) ::text").get()
        article_item['price'] = response.css(".-prxs ::text").get()
        article_item['n_stars'] =  response.css(".-plxs ::text").get()
        article_item['image'] = response.css("img.-fw.-fh::attr(data-src)").get()
        article_item['sku'] = Descriptif_technique[1]
        yield article_item