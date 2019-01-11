#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
from redis import StrictRedis
import time
import re
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

'''
自动抓取aicoin的请求cookie
Python==3.6
selenium==3.0.0
chrom==70.3588.90
redis=<2.8
'''


import sys




def get_cookies():
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'performance': 'ALL'}

    # 创建 chrome 参数对象
    options = webdriver.ChromeOptions()
    # 设置 chrome 参数为无界面
    options.add_argument('--headless')
    # 无界面可能会出现其他的一些状况，一般禁用 GPU 计算
    options.add_argument('--disable-gpu')
    # / home / ahrli / PycharmProjects / untitled / aicoin / history_spider / history_spider
    #
    # driver = webdriver.Chrome(executable_path='/home/ahrli/PycharmProjects/untitled/aicoin/history_spider/history_spider/chromedriver',
    #                           chrome_options=options)
    PATH = sys.path[0]+'/spiders/chromedriver'

    driver = webdriver.Chrome(
        executable_path=PATH,
    )

    driver.get("https://www.xicidaili.com/nn")

    time.sleep(2)
    try:
        time.sleep(8)
        driver.refresh()
        time.sleep(2)
        performance_log = driver.get_log('performance')
        a = str(performance_log).strip('[]')
        print(a)
        data_cookie = re.findall('''"Cache-Control":"max-age=0","Connection":"keep-alive","Cookie":"(.*?)","Host"''', a)[0]
        print(data_cookie)

    finally:
        # time.sleep(1000)

        driver.quit()
        print('关闭')
        return data_cookie


def main():
    """"""


    a = get_cookies()
    print(a)


if __name__ == '__main__':
    main()
