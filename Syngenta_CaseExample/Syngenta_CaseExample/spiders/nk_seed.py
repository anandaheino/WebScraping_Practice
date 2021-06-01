import scrapy
from Syngenta_CaseExample.items import SyngentaCaseItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join, TakeFirst
import urllib.parse
import datetime
import socket


class SyngentaNKSpider(scrapy.Spider):

    name = 'syngenta_1'
    allowed_domains = ['web']
    start_urls = ['https://www.portalsyngenta.com.br/sementes/nk-soja/nk-8770-ipro']

    def parse(self, response):
        item = SyngentaCaseItem()

        item['nome_semente'] = response.xpath('//*[@class="sementes link-page active"]/text()').extract()
        item['habito_crescimento'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').extract()[0]
        item['cor_flor'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').extract()[1]
        item['grupo_maturacao'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').extract()[2]

        item['beneficios'] = response.xpath('//*[@class="titulo-beneficios color-sementesNk-1"]/text()').extract()

        item['url'] = response.url
        # item['project'] = self.settings.get('BOT_NAME')
        # item['server'] = socket.gethostname()
        item['date'] = datetime.datetime.now()

        return item