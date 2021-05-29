# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


def remove_whitespace(value):
    return value.strip()

class JokeItem(scrapy.Item):
    # new field that will hold the joke text
    joke_text = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    # MapCompose: class that takes methods as arguments and applies to the data being scraped
    # Input and Output processors: they clean the data
    # TakeFirst() -> same as extract_first()

    # to remove white spaces before the jokes: add a function to the MapCompose
    # creating a remove_whitespace function and using inside MapCompose
