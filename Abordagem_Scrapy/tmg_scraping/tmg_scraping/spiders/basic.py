import scrapy
from tmg_scraping.items import TmgScrapingItem
from scrapy.loader import ItemLoader
import datetime
import socket

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://www.portalsyngenta.com.br/sementes/nk-soja/nk-8770-ipro',
                  'http://www.portalsyngenta.com.br/sementes/nk-soja/nk-7777-ipro',
                  'http://www.portalsyngenta.com.br/sementes/nk-soja/nk-8448-ipro',
                  'http://www.portalsyngenta.com.br/sementes/nk-soja/nk-8301-ipro',
                  'http://www.portalsyngenta.com.br/sementes/nk-soja/nk-7201-ipro',
                  'http://www.portalsyngenta.com.br/sementes/nk-soja/nk-6201-ipro']

    def parse(self, response):

        item = TmgScrapingItem()
        item['nome'] = response.xpath('//a[@class="sementes link-page active"]/text()').extract()[0]
        item['hab_cresc'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').extract()[0]
        item['cor_flor'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').extract()[1]
        item['pub'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').extract()[3]
        item['acam'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').extract()[4]
        item['hilo'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').extract()[5]
        item['alt'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').extract()[6]
        item['pms'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').extract()[7]
        item['ins_vag'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').extract()[8]

        item['url'] = response.url
        item['project'] = self.settings.get('BOT_NAME')
        item['spider'] =  self.name
        item['server'] = socket.gethostname()
        item['date'] = datetime.datetime.now()

        return item
        """
        dados = ItemLoader(item=TmgScrapingItem(), response=response)

        dados.add_xpath('nome', '//a[@class="sementes link-page active"]/text()')
        l.add_value('url', response.url)

        return dados.load_item()"""
