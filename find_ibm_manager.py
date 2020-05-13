# coding:utf-8
# author:liil
import requests


def get_plugin_info():
    plugin_info = {
        "name": "IBM管理后台",
        "info": "用于发现IBM管理后台，便于后续测试。",
        "level": "低危",
        "type": "信息探测",
        "author": "liil",
        "url": "",
        "keyword": "all:web",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    if int(port) == 80:
        url = "http://%s" % host
    else:
        url = "http://%s:%d" % (host, int(port))
    try:
        res = requests.get(url, timeout=timeout)
        if 'Welcome to the Advanced Management Module' in res.text and 'IBM' in res.text:
            info = 'IBM管理后台：%s' % url
            print info
            return info
    except Exception, e:
        pass
