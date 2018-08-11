# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/11 10:00
# @Author   : zhe
# @FileName : ajax.py
# @Project  : PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

BASE_DIR = os.path.dirname(__file__)

chromedriver_path = os.path.join(BASE_DIR, 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'loadedButton')))
finally:
    print(driver.find_element_by_id('content').text)
    driver.close()
