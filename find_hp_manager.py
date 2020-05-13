# coding:utf-8
# author:liil
import requests


def get_plugin_info():
    plugin_info = {
        "name": "HP管理后台",
        "info": "用于发现HP管理后台，便于后续测试。",
        "level": "低危",
        "type": "信息探测",
        "author": "liil",
        "url": "",
        "keyword": "port:2381",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    if int(port) == 443:
        url = 'https://%s' % host
    else:
        url = "https://%s:%d" % (host, int(port))
    try:
        res = requests.get(url,timeout=timeout,verify=False)
        if 'HP System Management' in res.text:
            info = 'HP管理后台：%s' % url
            return info
    except Exception,e:
        pass
