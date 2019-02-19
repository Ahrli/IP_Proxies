# IP_Proxies
免费代理爬取
## 环境
Python3.6
## 设置
#设置redis存储
REDIS_HOST = '192.168.80.188' #redis IP地址

REDIS_PORT = 6379             #端口

REDIS_PASSWORD = 'LOOP2themoon' #密码

REDIS_DB = 2                    #数据库名称

PROXIES_REDIS_KEY = "proxies"   #redis 存储键

#要启动的爬虫,不启动就注释掉

PROXIES_SPIDERS = [
    "spiders.daili66.Daili66ProxySpider",
    "spiders.xici.XiciSpider",    
    "spiders.xici透明.XiciSpider",
    "spiders.kuaidaili.KuaidailiSpider",
    'spiders.wuyoudaili.WuyoudailiSpider'
]
