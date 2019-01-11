#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
import requests
from lxml import etree

__author__ = 'Ahrli Tao'





def get_proxies():
    headers = {
        'Host': 'www.data5u.com',
        'Referer': 'http://www.data5u.com/free/gnpt/index.shtml',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

    }
    url = 'http://www.data5u.com/free/gnpt/index.shtml'

    response = requests.get(url, headers=headers)
    print(response.text)
    edata = etree.HTML(response.text)


    for idx in range(2, 16):
        row = edata.xpath('/html/body/div[5]/ul/li[2]/ul[%s]/span[1]/li/text()' % idx)

        port = edata.xpath('/html/body/div[5]/ul/li[2]/ul[%s]/span[2]/li/text()' % idx)[0]
        ip = row[0]

        print(ip, port)



get_proxies()
# a = {"https":'https://67.135.155.98:5220'}yd_cookie=68a29a2e-026c-4ee33d538a5b5d1dc60cf1989f214390e575; _ydclearance=8aab5284f1eb8f42cd34d870-d0e1-4426-b638-9cfa713be502-1545730534; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1545723335; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1545723335
#
# requests.post(proxies=a,timeout=10,)
