import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptsSpider(CrawlSpider):
    name = "transcripts"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["https://subslikescript.com/movies"]

    rules = (
        # Navega entre as páginas da listagem
        Rule(
            LinkExtractor(
                restrict_xpaths="//nav[@class='pagination_pages']//a"
            ),
            follow=True,
        ),

        # Acessa as páginas individuais dos filmes
        Rule(
            LinkExtractor(
                restrict_xpaths="//ul[@class='scripts-list']/li/a"
            ),
            callback="parse_item",
            follow=False,
        ),
    )

    
    def parse_item(self, response):
        article = response.xpath(
            "//article[@class='main-article']"
        )

        yield {
            "title": article.xpath("./h1/text()").get(),
            "plot": article.xpath("./p/text()").get(),
            "transcript": " ".join(
                article.xpath(
                    "./div[@class='full-script']/text()"
                ).getall()
            ).strip(),
            "url": response.url,
        }

    def parse_start_url(self, response):
        print("URL recebida:", response.url)
        print("Título:", response.xpath("//title/text()").get())
        print("Início do HTML:", response.text[:500])

