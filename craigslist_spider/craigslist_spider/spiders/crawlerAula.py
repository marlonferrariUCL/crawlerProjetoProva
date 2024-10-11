import scrapy


class CraigslistSpider(scrapy.Spider):
    name = 'craigslist_spider'
    allowed_domains = ['saopaulo.craigslist.org']
    start_urls = ['https://saopaulo.craigslist.org/search/apa#search=1~gallery~0~22']

    def parse(self, response):
        # Extract all links from the search results
        for a in response.css('ol.cl-static-search-results a::attr(href)').getall():
            yield {'link': a}
