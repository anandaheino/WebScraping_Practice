import scrapy
from Learning_scrapy_Basic.items import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
import urllib.parse
import datetime
import socket


class ManualSpider(scrapy.Spider):

    name = 'manual'
    allowed_domains = ['web']
    start_urls = ['https://www.gumtree.com/engineering-jobs']

    def parse(self, response):
        # get the next URLs and yield Requests
        next_selector = response.xpath('//*[contains(@class, "next")]//@href')
        for url in next_selector.extract():
            yield scrapy.Request(urllib.parse.urljoin(response.url, url))

        # get item URLs and yield Requests
        item_selector = response.xpath('//*[@itemprop="url"]/@href')
        for url in item_selector.extract():
            yield scrapy.Request(urllib.parse.urljoin(response.url, url), callback=self.parse_item)


    def parse_item(self, response):

        """This function parses a property page.
        @url https://www.gumtree.com/engineering-jobs
        @returns items 1
        @scrapes title price description address image_urls
        @scrapes url project spider server date"""

        loader = ItemLoader(item = PropertiesItem(), response= response)  # instantiating

        loader.add_xpath('title', '//*[@class="listing-header"]/text()')
        loader.add_xpath('price', '//*[@class="listing-price"]/text()')
        loader.add_xpath('description', '//*[@class="listing-description txt-sub txt-tertiary truncate-paragraph hide-fully-to-m"]/text()')
        loader.add_xpath('address', '//*[@class="listing-location"]/text()')

        loader.add_value('url', response.url)
        loader.add_value('project', self.settings.get('BOT_NAME'))
        loader.add_value('server', socket.gethostname())
        loader.add_value('date', datetime.datetime.now())

        return loader.load_item()
