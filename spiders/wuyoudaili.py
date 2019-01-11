#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
__author__ = 'Ahrli Tao'

import random
import time

import requests
from lxml import etree

class WuyoudailiSpider(object):

    def get_url_list(self):

        # 网络对西刺网站进行爬取免费代理利用 yield 返回给上层
        return ["https://www.kuaidaili.com/free/inha/{}/".format(i) for i in range(1, 20)]
        pass

    def get_proxies(self):
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
            yield "http://{}:{}".format(ip, port)
            yield "https://{}:{}".format(ip, port)