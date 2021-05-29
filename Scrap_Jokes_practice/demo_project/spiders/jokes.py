import scrapy


class JokesSpider(scrapy.Spider):
    name = 'jokes'   # we can call/launch this spider from the terminal using this name
    start_urls = [
        'http://www.laughfactory.com/jokes/family-jokes'
    ]

    def parse(self, response):
        for joke in response.xpath("//div[@class='jokes']"):
            yield {
                'joke_text': joke.xpath(".//div[@class='joke-text']/p/text()").extract_first()
            }
        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)