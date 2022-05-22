import scrapy
from scrapy.http import Request
from ForexInfo import ForexItem


import json

class ArticlescrapperSpider(scrapy.Spider):
    name = 'ArticleScrapper'
    allowed_domains = ['trtworld.com']
    start_urls = ['http://trtworld.com/']

    def parse(self, response):
        pass
