import scrapy


class SquotesSpider(scrapy.Spider):
    name = "sQuotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    current = 1
    max_page = 2

    def parse(self, response):
        block_quote = response.xpath("//div[@class='quote']")
        for block in block_quote:
            quote = block.xpath(
                ".//span[@class='text']/text()"
            ).get()
            author = block.xpath(
                ".//small[@class='author']/text()"
            ).get()
            yield {
                "text": quote,
                "author": author,
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None and self.current < self.max_page:
            self.current += 1
            yield response.follow(next_page, callback=self.parse)
