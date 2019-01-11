#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import time

import requests
from lxml import etree

from .xici_cookies import get_cookies


class XiciSpider(object):

    def get_url_list(self):

        # 网络对西刺网站进行爬取免费代理利用 yield 返回给上层
        return ["https://www.xicidaili.com/nt/{}".format(i) for i in range(1, 20)]
        pass

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
            response = requests.get(url, headers=headers)
            print(response.text)
            edata = etree.HTML(response.text)

            for idx in range(2, 100):
                row = edata.xpath('//*[@id="ip_list"]/tr[%s]/td/text()' % idx)

                ip = row[0]
                port = row[1]
                print('xici',ip, port)
                yield "http://{}:{}".format(ip, port)
                yield "https://{}:{}".format(ip, port)
