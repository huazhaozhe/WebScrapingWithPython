# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/10 13:28
# @Author   : zhe
# @FileName : markov.py
# @Project  : PyCharm


from urllib.request import urlopen
from random import randint
import operator


def wordListSum(wordList):
    sum = 0
    for woed, value in wordList.items():
        sum += value
    return sum


def retrieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))
    wordList = sorted(wordList.items(), key=operator.itemgetter(1))
    for word, value in wordList:
        randIndex -= value
        if randIndex <= 0:
            return word


def buildWordDict(text):
    text = text.replace('\n', ' ').replace('\'', '').replace('\"', '')
    punctuation = [',', ', ', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, ' ' + symbol + ' ')
    words = text.split(' ')
    words = [word for word in words if word != '']

    wordDict = {}
    for i in range(1, len(words)):
        if words[i - 1] not in wordDict:
            wordDict[words[i - 1]] = {}
        if words[i] not in wordDict[words[i - 1]]:
            wordDict[words[i - 1]][words[i]] = 0
        wordDict[words[i - 1]][words[i]] += 1
    return wordDict


text = str(
    urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read())
wordDict = buildWordDict(text)
length = 100
chain = ''
currentWord = 'A'
for i in range(0, length):
    chain += currentWord + ' '
    currentWord = retrieveRandomWord(wordDict[currentWord])
print(chain)
