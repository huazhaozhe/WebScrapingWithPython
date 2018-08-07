# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/7 9:21
# @Author   : zhe
# @FileName : beautifulsoup.py
# @Project  : PyCharm

from urllib.request import urlopen
from bs4 import BeautifulSoup
from config import *


html = urlopen(mysite_https)
bsObj = BeautifulSoup(html.read())
print(bsObj.meta)