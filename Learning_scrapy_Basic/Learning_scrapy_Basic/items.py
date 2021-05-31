from scrapy.item import Item, Field


class PropertiesItem(Item):
    # defyning the fields for the item here:
    title = Field()
    price = Field()
    description = Field()

    # Other fields that might be important:
    images = Field()
    location = Field()

    # other very usefull fields:
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
