# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/11 10:46
# @Author   : zhe
# @FileName : redirect.py
# @Project  : PyCharm

from selenium import webdriver
import time
import os
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException


def waitForLoad(driver):
    text = driver.find_element_by_tag_name('html').text
    start_time = time.time()
    while True:
        try:
            if driver.find_element_by_tag_name('html').text != text:
                return
        except StaleElementReferenceException:
            return
        if time.time() - start_time > 10:
            print('Timing out afger 10 seconds and returning')
            return


BASE_DIR = os.path.dirname(__file__)

chromedriver_path = os.path.join(BASE_DIR, 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
print(driver.page_source)
waitForLoad(driver)
print(driver.page_source)
driver.close()
