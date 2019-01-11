#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
import requests
from lxml import etree

__author__ = 'Ahrli Tao'


def get_url_list():
    return ["https://www.xicidaili.com/nn/{}.html".format(i) for i in range(1, 10)]


def get_proxies():
    headers = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Connection': 'keep-alive',
        'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWI4M2ZlYWNiYWU4NjU5YjAxOWYyOWZhZjUwMGY3NDNmBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVh5QWxlOU9SMnA2ZGdxNmR5eE5CVXdzaUlhZmtVUlVSRnVna0ZHUFM4S3c9BjsARg%3D%3D--23bcce33aaedd4fe5438549fed2805473fd98d91; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1545811188; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1545811188',







        'Host': 'www.xicidaili.com',
        'Referer': 'https://www.xicidaili.com/nn/16',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

    }
    # url = 'https://www.xicidaili.com/nn/2'
    for url in get_url_list():
        response = requests.get(url, headers=headers)
        print(response.text)
        edata = etree.HTML(response.text)


        for idx in range(2, 100):
            row = edata.xpath('//*[@id="ip_list"]/tr[%s]/td/text()' % idx)


            ip = row[0]
            port = row[1]
            print(ip, port)
        break

get_proxies()
# a = {"https":'https://67.135.155.98:5220'}yd_cookie=68a29a2e-026c-4ee33d538a5b5d1dc60cf1989f214390e575; _ydclearance=8aab5284f1eb8f42cd34d870-d0e1-4426-b638-9cfa713be502-1545730534; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1545723335; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1545723335
#
# requests.post(proxies=a,timeout=10,)
