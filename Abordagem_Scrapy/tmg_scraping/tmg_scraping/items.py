# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TmgScrapingItem(scrapy.Item):
    # define the fields for your item here like:

    # Primary fields
    nome = scrapy.Field()
    hab_cresc = scrapy.Field()
    cor_flor = scrapy.Field()
    pub = scrapy.Field()
    acam = scrapy.Field()
    hilo = scrapy.Field()
    alt = scrapy.Field()
    pms = scrapy.Field()
    ins_vag = scrapy.Field()

    #  Housekeeping fields
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()
