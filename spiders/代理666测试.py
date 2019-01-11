#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
import requests
from lxml import etree

__author__ = 'Ahrli Tao'


def get_url_list():
    return ["http://www.66ip.cn/{}.html".format(i) for i in range(1, 10)]


def get_proxies():

    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'yd_cookie=1ef4e79a-d824-434c2e6c58dc3e4056076e34f21c63f70b99; _ydclearance=1da72664ae81a191ee649303-26cd-445c-beff-142616716adb-1545815818; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1545808619; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1545808619',




'Host':'www.66ip.cn',
'Referer':'http://www.66ip.cn/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    for url in get_url_list():

        response = requests.get(url, headers=headers)
        print(response.text)
        edata = etree.HTML(response.text)
        rows = edata.xpath('//table//tr')

        for idx in range(2, len(rows)):
            row = rows[idx]
            ip = row.xpath('./td[1]/text()')[0]
            port = row.xpath('./td[2]/text()')[0]
            print(ip, port)
            # yield "http://{}:{}".format(ip, port)
            # yield "https://{}:{}".format(ip, port)
        break

get_proxies()
# a = {"https":'https://67.135.155.98:5220'}yd_cookie=68a29a2e-026c-4ee33d538a5b5d1dc60cf1989f214390e575; _ydclearance=8aab5284f1eb8f42cd34d870-d0e1-4426-b638-9cfa713be502-1545730534; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1545723335; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1545723335
#
# requests.post(proxies=a,timeout=10,)




