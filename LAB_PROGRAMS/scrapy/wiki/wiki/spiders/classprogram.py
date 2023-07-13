import scrapy
class program(scrapy.Spider):
    name='program'
    def request(self):
        urls=['http://www.google.com','http://www.news.google.com']
        return[scrapy.Request(url=url,callback=self.parse)for url in urls]
    def parse(self,response):
        url=response.url
        para=response.css('p::text').getall()
        print('url in:{}'.format(url))
        for p in para:
            print(para)
    