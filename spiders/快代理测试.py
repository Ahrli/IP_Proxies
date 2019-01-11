#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
import requests
from lxml import etree

__author__ = 'Ahrli Tao'


def get_url_list():
    return ["https://www.kuaidaili.com/free/inha/{}/".format(i) for i in range(1, 10)]


def get_proxies():
    headers = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Connection': 'keep-alive',
        # 'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWI4M2ZlYWNiYWU4NjU5YjAxOWYyOWZhZjUwMGY3NDNmBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVh5QWxlOU9SMnA2ZGdxNmR5eE5CVXdzaUlhZmtVUlVSRnVna0ZHUFM4S3c9BjsARg%3D%3D--23bcce33aaedd4fe5438549fed2805473fd98d91; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1545811188; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1545811188',







        # 'Host': 'www.xicidaili.com',
        # 'Referer': 'https://www.xicidaili.com/nn/16',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

    }
    # url = 'https://www.xicidaili.com/nn/2'
    for url in get_url_list():
        response = requests.get(url, headers=headers)
        edata = etree.HTML(response.text)
        rows = edata.xpath('//tbody//tr')

        for idx in range(2, len(rows)):
            row = rows[idx]
            ip = row.xpath('./td[1]/text()')[0]
            port = row.xpath('./td[2]/text()')[0]
            print(ip, port)
        # for idx in range(2, 100):
        #     row = edata.xpath('//*[@id="ip_list"]/tr[%s]/td/text()' % idx)
        #
        #
        #     ip = row[0]
        #     port = row[1]
        #     print(ip, port)
        break

get_proxies()
