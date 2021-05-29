import scrapy
from demo_project.items import JokeItem
from scrapy.loader import ItemLoader

class JokesSpider(scrapy.Spider):
    name = 'jokes'   # we can call/launch this spider from the terminal using this name
    start_urls = [
        'http://www.laughfactory.com/jokes/family-jokes'
    ]

    def parse(self, response):
        for joke in response.xpath("//div[@class='jokes']"):
            # Instatiating the ItemLoader class:
            loader = ItemLoader(item = JokeItem(), selector=joke)
            loader.add_xpath('joke_text', ".//div[@class='joke-text']/p")    # add_xpath('field_name', 'xpath_expression')
            yield loader.load_item()    # calling this method from ItemLoader class

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)