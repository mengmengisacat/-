import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ['dmoztools.net']
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/"
        ]
    def parse(self,response):
        #弹幕说可以在cmd中scrapy genspider 项目名称 域名
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//section/div/div/div/div[@class="title-and-desc"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/div/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('div[@class="site-descr "]/text()').extract()
            items.append(item)

        return items
    
