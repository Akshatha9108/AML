import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
class MySpider(CrawlSpider):
    name="program2"
    aloowed_domains=['google.com']
    start_urls=['https://www.google.com/']
    rules=(Rule(LinkExtractor(),callback='parse_page',follow=True),)
    
    def parse_page(self,response):
        title=response.css('title::text').getall()
        paragraphs=response.css('p::text').getall()[:2]
        yield{
            'title':title,
            'paragraphs':paragraphs,
        }