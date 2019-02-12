# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 16:05:34 2019

@author: 明天怎样
"""
import requests
url = 'http://www.baidu.com/'
res = requests.get(url)
html = res.text        # 网页源码
with open('web.html', 'w', encoding='utf-8') as f:
    f.write(html)
