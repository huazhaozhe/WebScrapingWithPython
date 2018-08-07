# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/7 11:11
# @Author   : zhe
# @FileName : WebCrawler.py
# @Project  : PyCharm

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html)
for link in bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).*$)')):
    if 'href' in link.attrs:
        print(link.attrs['href'])