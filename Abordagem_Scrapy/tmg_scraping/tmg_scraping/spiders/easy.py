import scrapy
from tmg_scraping.items import TmgScrapingItem
from scrapy.loader import ItemLoader
import datetime
import socket
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

class BasicSpider(scrapy.Spider):
    name = 'easy'
    allowed_domains = ['web']

    def urls():
        url = 'http://www.portalsyngenta.com.br/sementes/nk-soja'
        html = urlopen(url)
        scrap = BeautifulSoup(html, 'html.parser')
        class_card = "card-text-2 card-portfolio"
        cards = scrap.find_all('div', {'class': class_card})

        links = []
        principal = 'http://www.portalsyngenta.com.br'

        for link in cards:
            link = principal+(link.a['href'])
            links.append(link)

        return links

    start_urls = urls()

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
