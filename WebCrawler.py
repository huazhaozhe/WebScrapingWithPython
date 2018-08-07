# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/7 11:11
# @Author   : zhe
# @FileName : WebCrawler.py
# @Project  : PyCharm

from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())


def getLink(articleUrl):
    try:
        html = urlopen('http://en.wikipedia.org' + articleUrl)
    except HTTPError as e:
        print(e)
        return
    bsObj = BeautifulSoup(html)
    return bsObj.find(
        'div',
        {'id': 'bodyContent'}
    ).findAll(
        'a',
        href=re.compile('^(/wiki/)((?!:).*$)')
    )


links = getLink('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLink(newArticle)
