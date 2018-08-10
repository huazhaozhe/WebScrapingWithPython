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


def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it",
                   "i", "that", "for", "you", "he", "with", "on", "do", "say",
                   "this",
                   "they", "is", "an", "at", "but", "we", "his", "from",
                   "that", "not",
                   "by", "she", "or", "as", "what", "go", "their", "can",
                   "who", "get",
                   "if", "would", "her", "all", "my", "make", "about", "know",
                   "will",
                   "as", "up", "one", "time", "has", "been", "there", "year",
                   "so",
                   "think", "when", "which", "them", "some", "me", "people",
                   "take",
                   "out", "into", "just", "see", "him", "your", "come",
                   "could", "now",
                   "than", "like", "other", "how", "then", "its", "our", "two",
                   "more",
                   "these", "want", "way", "look", "first", "also", "new",
                   "because",
                   "day", "more", "use", "no", "man", "find", "here", "thing",
                   "give",
                   "many", "well"]
    if ngram.lower() in commonWords:
        return False
    return True


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
    input = list(filter(isCommon, input))
    output = {}
    for i in range(len(input) - n + 1):
        ngramTemp = ' '.join(input[i:i + n])
        if ngramTemp in output:
            output[ngramTemp] += 1
        else:
            output[ngramTemp] = 1
    return output


content = str(
    urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read())
ngrams = ngrams(content, 2)
ngrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(ngrams)
print(len(ngrams))
