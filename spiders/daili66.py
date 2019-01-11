#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time

import requests
from lxml import etree
from redis import StrictRedis

from .dali66_cookies import get_cookies


class Daili66ProxySpider(object):

    def get_url_list(self):
        return ["http://www.66ip.cn/{}.html".format(i) for i in range(1,10)]

    # def get_cookies(self):
    #     '''获取'''
    #     rd = StrictRedis(host="192.168.80.188", port=6379, db=2, password='LOOP2themoon')
    #     pip = rd.lpop('66ip.cn')
    #
    #     if pip is None:
    #         time.sleep(5)
    #         self.get_cookies()
    #     else:
    #         if len(pip.decode('utf-8')) < 1:
    #             self.get_proxies()
    #         else:
    #             return pip.decode('utf-8')


    def get_proxies(self):

        cookies = get_cookies()

        headers = {

            'Cookie': cookies,

            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.66ip.cn',
            'Referer': 'http://www.66ip.cn/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }

        for url in self.get_url_list():
            time.sleep(random.random())
            response = requests.get(url,headers=headers)
            print(response.text)
            edata = etree.HTML(response.text)
            rows = edata.xpath('//table//tr')

            for idx in range(2,len(rows)):
                row = rows[idx]
                ip = row.xpath('./td[1]/text()')[0]
                port = row.xpath('./td[2]/text()')[0]
                print(ip,port)
                yield "http://{}:{}".format(ip,port)
                yield "https://{}:{}".format(ip,port)


