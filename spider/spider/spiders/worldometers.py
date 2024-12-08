import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        rows = response.xpath('//tr')

        for row in rows:
            countries = row.xpath('./td/a/text()').get()
            population = row.xpath('./td[3]/text()').get()

            yield {
                'countries': countries,
                'population': population,
            }
