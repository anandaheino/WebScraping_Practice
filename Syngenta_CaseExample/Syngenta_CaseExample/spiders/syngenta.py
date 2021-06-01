import scrapy
from Syngenta_CaseExample.items import SyngentaCaseItem
from scrapy.loader.processors import Join, TakeFirst
import urllib.parse
import datetime
import socket


class SyngentaSpider(scrapy.Spider):

    name = 'syngenta'
    allowed_domains = ['web']
    start_urls = ['https://www.portalsyngenta.com.br/sementes/nk-soja']

    def parse(self, response):
        # get the corresponding seed URL and yield Requests:
        for url in response.xpath('.//div[@class="card-text-2 card-portfolio"]/a/@href').extract():
            yield response.follow_all(url, callback=self.parse_item)


    def parse_item(self, response):

        """This function parses a soy-seed company named Syngenta.
        @url https://www.portalsyngenta.com.br/sementes/syngenta-soja
        @returns items
        @scrapes habito_crescimento grupo_maturacao acamamento altura_planta insercao_vagem
        @scrapes cor_flor pubescencia hilo pms_medio beneficios
        @scrapes url project spider server date"""

        item = SyngentaCaseItem()
        # by using the loader, it is easier to combine, clean and format data with MapCompose or Join

        item['nome_semente'] = response.xpath('//a[@class="sementes link-page active"]/text()').get()
        item['habito_crescimento'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').get()[0]
        item['cor_flor'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').get()[1]
        item['grupo_maturacao'] = response.xpath('//div[@class="prop-nk-descricao"]/p/text()').get()[2]

        # loader.add_xpath('acamamento', './/*[@class="prop-nk-descricao"][4]/text()')
        # loader.add_xpath('altura_planta', './/*[@class="prop-nk-descricao"][6]/text()')
        # loader.add_xpath('insercao_vagem', './/*[@class="prop-nk-descricao"][8]/text()')
        #loader.add_xpath('pubescencia', './/*[@class="prop-nk-descricao"][3]/text()')
        #loader.add_xpath('hilo', './/*[@class="prop-nk-descricao"][5]/text()')
        #loader.add_xpath('pms_medio', './/*[@class="prop-nk-descricao"][7]/text()')

        item['beneficios'] = response.xpath('//*[@class="titulo-beneficios color-sementesNk-1"]/text()').Join()

        item['url'] = response.url
        # item['project'] = self.settings.get('BOT_NAME')
        # item['server'] = socket.gethostname()
        item['date'] = datetime.datetime.now()

        return item
