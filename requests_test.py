# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/10 19:14
# @Author   : zhe
# @FileName : requests_test.py
# @Project  : PyCharm

import requests

session = requests.Session()

s = session.get('http://www.example.com/')

print(s.text)
print('cookie is set to:', s.cookies.get_dict())
params = {
    'username': '***',
    'password': '***',
    'csrfmiddlewaretoken': s.cookies.get_dict()['***'],
    'next': '***',
}
print(params)
r = session.post(
    "http://www.example.com/login/",
    data=params)
print(r.text)
print(r.cookies.get_dict())
