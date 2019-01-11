#!/usr/bin/python3
# -*- coding: utf-8 -*-

#设置redis存储

REDIS_HOST = '192.168.80.188'
REDIS_PORT = 6379
REDIS_PASSWORD = 'LOOP2themoon'
REDIS_DB = 2
PROXIES_REDIS_KEY = "proxies"

#要启动的爬虫,不启动就注释掉
PROXIES_SPIDERS = [
    "spiders.daili66.Daili66ProxySpider",
    "spiders.xici.XiciSpider",
"spiders.xici透明.XiciSpider",
"spiders.kuaidaili.KuaidailiSpider",
    'spiders.wuyoudaili.WuyoudailiSpider'
]