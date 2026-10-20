import scrapy


class WorldmetersSpider(scrapy.Spider):
    name = "worldmeters"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        contries = response.xpath('//td/a')

        for country in contries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # yield {
            #     'title': country_name,
            #     'countries': link
            # }

            yield response.follow(url=link, callback=self.parse_country, meta={ 'country': country_name })


    def parse_country(self, response):
        # response.xpath('/html/body/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[3]/table')
        country = response.request.meta['country']
        rows = response.xpath("(//table[contains(@class, 'table')])[1]/tbody/tr")

        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath('.//td[2]/text()').get()

            yield {
                'country': country,
                'year': year,
                'population': population
            }