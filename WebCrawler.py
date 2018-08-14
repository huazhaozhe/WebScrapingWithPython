# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/7 11:11
# @Author   : zhe
# @FileName : WebCrawler.py
# @Project  : PyCharm

from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
import re

pages = set()
def getLink(pageUrl):
    global pages
    url = 'http://en.wikipedia.org' + pageUrl
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e, pageUrl)
        pages.remove(pageUrl)
        return
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLink(newPage)
getLink('')
print(pages)