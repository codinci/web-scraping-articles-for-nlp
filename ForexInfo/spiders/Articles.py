from requests import request
import scrapy
from scrapy.http import Request
from ForexInfo.items import ForexinfoItem


class ArticlesSpider(scrapy.Spider):
    name = 'Articles'
    allowed_domains = ['trtworld.com']
    start_urls = ['http://trtworld.com/']

    def start_requests(self):

#Hardcoded URL that contains Turkey related subjects
        url = "https://www.trtworld.com/turkey?page={}"
        link_urls = [url.format(i) for i in range(0,500)]
#Loops through 500 pages to get the article links 
        for link_url in link_urls:
            print(link_url)
#Request to get the HTML content
        request = Request(link_url, cookies={'store_language':'en'},
        callback = self.parse_main_pages)

        yield request

    def parse_main_pages(self,response):
        item=ForexinfoItem

#Gets HTML content where the article links are stored
        content=response.xpath('//div[@id="items"]//div[@class="article-meta"]')
#Loops through each and every article link in HTML 'content'
        for article_link in content.xpath('.//a'):

#Extracts the href info of the link to store in scrapy item
            item['article_url'] = "https://www.trtworld.com"+item['article_url']
            yield(item)

    def parse(self, response):
        pass
