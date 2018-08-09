# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/9 18:38
# @Author   : zhe
# @FileName : analysisJson.py
# @Project  : PyCharm

import json
from urllib.request import urlopen
from config import *

def getCounttry(ip):
    url = 'http://api.ipstack.com/'+ip+'?access_key='+ipstacKey
    response = urlopen(url).read().decode()
    responseJson = json.loads(response)
    return responseJson.get('country_code')
print(getCounttry('50.78.253.58'))