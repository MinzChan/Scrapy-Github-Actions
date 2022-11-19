import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.css('.product_pod a::text').getall()
        prices = response.css('.price_color::text').getall()

        for book, price in zip(books, prices):
            yield {
                'book': book,
                'price': price
            }

        nextPath = response.xpath('//a[text()="next"]/@href').get()

        if nextPath:
            yield scrapy.Request(response.urljoin(nextPath))
