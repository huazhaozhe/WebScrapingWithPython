# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/7 9:21
# @Author   : zhe
# @FileName : beautifulsoup.py
# @Project  : PyCharm

from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
from config import *

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll('span', {'class': ['green', ]})
for name in nameList:
    print(name.get_text())