# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/10 9:13
# @Author   : zhe
# @FileName : DataCleaning.py
# @Project  : PyCharm

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict
import operator


def cleanInput(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]', '', input)
    input = re.sub(' +', ' ', input)
    cleanInputList = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInputList.append(item)
    return cleanInputList


def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input) - n + 1):
        ngramTemp = ' '.join(input[i:i + n])
        if ngramTemp in output:
            output[ngramTemp] += 1
        else:
            output[ngramTemp] = 1
    return output


html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html)
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
ngrams = ngrams(content, 2)
ngrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(ngrams)
print(len(ngrams))
