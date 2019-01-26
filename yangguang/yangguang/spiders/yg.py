# -*- coding: utf-8 -*-
import scrapy
from yangguang.items import YangguangItem

class YgSpider(scrapy.Spider):
    name = "yg"
    allowed_domains = ["sun0769.com"]
    start_urls = ['http://wz.sun0769.com/html/top/ruse.shtml']

    def parse(self, response):
        td_list = response.xpath("//div[@class='newsHead clearfix']/table[2]/tr/td")
        for td in td_list:
            item = YangguangItem()
            item["title"] = td.xpath("./td[2]/a[@target='_blank']/@title").extract_first()
            item["href"] = td.xpath("./td[2]/a[@target='_blank']/@href").extract_first()
            item["publish_date"]=td.xpath("./td[last()]/text()").extract_first()

            #到详情页
            yield scrapy.Request(
                item["href"],
                callback=self.parse_detail,
                meta = {"item":item}
            )
    def parse_detail(self,response):#处理详情页
        item = response.meta["item"]
        item["content"] = response.xpath("//div[@class='txt16_3'/td[@class='txt16_3'/text()").extract()
