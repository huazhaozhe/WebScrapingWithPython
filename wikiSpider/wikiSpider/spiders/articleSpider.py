# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/7 17:05
# @Author   : zhe
# @FileName : articleSpider.py
# @Project  : PyCharm

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from wikiSpider.items import Article


class ArticleSpider(CrawlSpider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Python_%28programming_language%29']
    rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'), ),
                  callback='parse_item', follow=True)]

    def parse_item(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print('Title: ', title)
        item['title'] = title
        return item
