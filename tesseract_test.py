# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/11 14:49
# @Author   : zhe
# @FileName : tesseract_test.py
# @Project  : PyCharm

import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

tesseract_path = 'D:\\Tesseract-OCR\\tesseract'

driver = webdriver.Chrome()
driver.get(
    "http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(5)
driver.find_element_by_id('sitbLogoImg').click()
imageList = set()
time.sleep(5)
while 'pointer' in driver.find_element_by_id(
        'sitbReaderRightPageTurner').get_attribute('style'):
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(5)
    pages = driver.find_elements_by_xpath('//div[@class="pageImage"]/div/img')
    for page in pages:
        image = page.get_attribute('src')
        imageList.add(image)

driver.quit()

for image in sorted(imageList):
    urlretrieve(image, 'page.jpg')
    p = subprocess.Popen([tesseract_path, 'page.jpg', 'page'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open('page.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()
