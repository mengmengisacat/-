# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from taobao1.items import Taobao1Item


class TaobaospiderSpider(scrapy.Spider):
    name = 'taobaospider'
    allowed_domains = ['taobao.com']
    start_urls = ['https://s.taobao.com/search?spm=a230r.1.1998181369.d4919860.26e22914HgtKhx&q=%E9%93%82%E9%87%91&imgfile=&js=1&initiative_id=staobaoz_20160129&ie=utf8&tab=mall&cps=yes&ppath=20000%3A3650283%3B20000%3A59957%3B20000%3A59958%3B20000%3A3582020%3B20000%3A4166906%3B20000%3A225094921']
    def parse(self, response):
        sel = Selector(response)
		sites = sel.xpath('//section/div/div/div/div[@class="item J_MouserOnverReq"]')
        items = []
        for site in sites:
            item = Taobao1Item()
            item['title'] = site.xpath('a/span/text()').extract()
			item['price'] = site.xpath('div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]/div/div/strong/text()').extract()
			item['link'] = site.xpath('a/@href').extract()
			item['deal_cnt'] = site.xpath('div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]/div/div[@class="deal-cnt"]/text()').extract()
			item['location'] = site.xpath('div[@class="location"]/text()').extract()
            items.append(item)

        return items
