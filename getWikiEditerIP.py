# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/9 18:58
# @Author   : zhe
# @FileName : getWikiEditerIP.py
# @Project  : PyCharm

from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re
import json
from config import *

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    url = 'http://en.wikipedia.org' + articleUrl
    print(url)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a',
                                                            href=re.compile(
                                                                '^(/wiki/)((?!:).)*$'))


def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'http://en.wikipedia.org/w/index.php?title=' + pageUrl + '&action=history'
    print('history url is:' + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    ipAddresses = bsObj.findAll('a', {'class': 'mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


def getCountry(ip):
    url = 'http://api.ipstack.com/' + ip + '?access_key=' + ipstacKey
    try:
        response = urlopen(url).read().decode()
    except HTTPError as e:
        print(e)
        return 'None'
    responseJson = json.loads(response)
    return responseJson.get('country_code')


links = getLinks('/wiki/Python_(programming_language)')

while len(links) > 0:
    for link in links:
        print('-' * 50)
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            print(historyIP, country)
    new_link = links[random.randint(0, len(links) - 1)].attrs['href']
    links = getLinks(new_link)
