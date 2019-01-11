#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
__author__ = 'Ahrli Tao'


IP_URL = 'http://127.0.0.1:6868/proxies/random'
def get_proxies():
    url = IP_URL
    response = requests.get(url=url)
    if response is None:
        time.sleep(1)
        get_proxies()
    proxies_ip = response.text
    proxies = {proxies_ip.split(':')[0]: proxies_ip}
    return proxies