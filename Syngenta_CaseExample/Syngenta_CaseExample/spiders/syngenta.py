import scrapy
from Syngenta_CaseExample.items import SyngentaCaseItem
from urllib.parse import urljoin
import datetime
from Syngenta_CaseExample.funcoes import abre_e_scrap, find_links_in_cards


class SyngentaSpider(scrapy.Spider):

    name = 'syngenta'
    allowed_domains = ['web']

    scrap = abre_e_scrap('https://www.portalsyngenta.com.br/sementes/syngenta-soja')
    links = find_links_in_cards(scrap, "card-text-2 card-portfolio")
    start=[]
    for link in links:
        l = urljoin('https://www.portalsyngenta.com.br/sementes/nk-soja', link)
        start.append(l)

    start_urls = start

    def parse(self, response):

        item = SyngentaCaseItem()

        item['nome_semente'] = response.xpath('//a[@class="sementes link-page active"]/text()').extract()
        item['habito_crescimento'] = response.xpath('//div[@class="prop-soja-descricao"]/p/text()').extract()[0]
        item['cor_flor'] = response.xpath('//div[@class="prop-soja-descricao"]/p/text()').extract()[1]
        item['grupo_maturacao'] = response.xpath('//div[@class="prop-soja-descricao"]/p/text()').extract()[2]
        item['pubescencia'] = response.xpath('//div[@class="prop-soja-descricao"]/p/text()').extract()[3]
        item['acamamento'] = response.xpath('//div[@class="prop-soja-descricao"]/p/text()').extract()[4]
        item['hilo'] = response.xpath('//div[@class="prop-soja-descricao"]/p/text()').extract()[5]
        item['altura_planta'] = response.xpath('//div[@class="prop-soja-descricao"]/p/text()').extract()[6]
        item['pms_medio'] = response.xpath('//div[@class="prop-soja-descricao"]/p/text()').extract()[7]
        item['insercao_vagem'] = 'null'
        item['beneficios'] = response.xpath('//*[@class="titulo-beneficios color-lightOrange-50"]/text()').extract()

        item['url'] = response.url
        item['date'] = datetime.datetime.now()

        return item
