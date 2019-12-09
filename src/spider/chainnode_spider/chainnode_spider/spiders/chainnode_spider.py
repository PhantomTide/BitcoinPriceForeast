# -*- coding:utf-8 -*-

"""
chain node spider
"""

import scrapy
from scrapy.spiders import Spider


class ChainNodeSpider(Spider):
    """
    ChainNodeSpider 链节点爬虫
    """

    name = "chainnode_spider"
    start_urls = [
        "https://www.chainnode.com/"
    ]

    def parse(self, response):
        """
        解析数据
        :param response:
        :return:
        """
        # //*[@id="app"]/div[2]/div/div[2]/div[1]/section[2]/div[2]/div[3]/div[1]
        title01 = response.xpath('//*[@id="app"]/div[2]/div/div[2]/div[1]/section[2]/div[2]/div[3]/div[1]').extract()[0]
        title02 = response.xpath('//*[@id="app"]/div[2]/div/div[2]/div[1]/section[2]/div[2]/div[3]/div[36]').extract()[0]
        print(title01)
        print(title02)
