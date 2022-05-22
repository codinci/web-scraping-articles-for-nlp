from requests import request
import scrapy
from scrapy.http import Request
from ForexInfo.items import ForexinfoItem


import json

class ArticlescrapperSpider(scrapy.Spider):
    name = 'ArticleScrapper'
    allowed_domains = ['trtworld.com']
    start_urls = ['http://trtworld.com/']

    def start_requests(self):
#Open JSON file which contains article links
        with open('/home/davi3/Projects/PythonProjects/ForexInfo/spiders/Articles.py') as json_file:
            data = json.load(json_file)

            for p in data:
                print('URL: ' + p['article_url'])

#Request to get the HTML content
                request = Request(p['article_url'],
                            cookies={'store_language':'en'},
                            callback=self.parse_article_page)
                yield request

    def parse_article_page(self,response):
        item = ForexInfoItem()
        a_body = ""

#Extracts the article_title and stores in scrapy_item
        item['article_title'] = response.xpath('//h1[@class="article-title"]/text()').extract();

#Extracts the article_description and stores in scrapy_item
        item['article_description'] = response.xpath('//h3[@class="article-description"]/text()').extract();

#Extracts the article_body in <p> elements
        for p in response.xpath('//div[@class="contentBox bg-wnoMedia"]//p/text()').extract():

            a_body = a_body+p
            item['article_body'] = a_body
            yield(item)

        

    def parse(self, response):
        pass
