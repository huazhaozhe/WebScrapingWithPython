# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/11 10:00
# @Author   : zhe
# @FileName : ajax.py
# @Project  : PyCharm

from selenium import webdriver
import time
import os

BASE_DIR = os.path.dirname(__file__)
phantomJS_path = os.path.join(BASE_DIR, 'phantomjs-2.1.1-windows', 'bin',
                              'phantomjs.exe')
chromedriver_path = os.path.join(BASE_DIR, 'chromedriver.exe')

# driver = webdriver.PhantomJS(executable_path=phantomJS_path)
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
# print(driver.page_source)
print(driver.find_element_by_id('content').text)
time.sleep(4)
# print(driver.page_source)
print(driver.find_element_by_id('content').text)
driver.close()
