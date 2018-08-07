# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/7 9:21
# @Author   : zhe
# @FileName : beautifulsoup.py
# @Project  : PyCharm

from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
import re
from config import *

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html)
imgList = bsObj.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for img in imgList:
    print(img)