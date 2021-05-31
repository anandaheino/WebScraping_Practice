import scrapy
from Learning_scrapy_Basic.items import PropertiesItem
from scrapy.loader import ItemLoader

class BasicSpider(scrapy.Spider):

    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://web:9312/properties/property_000000.html']

    def parse(self, response):

        loader = ItemLoader(item = PropertiesItem(), response= response)  # instantiating

        loader.add_xpath('//*[@itemprop="name"][1]/text()').extract()
        loader.add_xpath('//*[@itemprop="price"][1]/text()').re('[.0-9]+')
        loader.add_xpath('//*[@itemprop="description"][1]/text()').extract()
        loader.add_xpath('//*[@itemtype="http://schema.org/"Place"][1]/text()').extract()
        loader.add_xpath('//*[@itemprop="image"][1]/@src').extract()

        return loader.load_item()
    