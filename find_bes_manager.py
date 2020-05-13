# coding:utf-8
# author:liil
import requests


def get_plugin_info():
    plugin_info = {
        "name": "BES管理后台",
        "info": "用于发现BES管理后台，便于后续测试。",
        "level": "低危",
        "type": "信息探测",
        "author": "liil",
        "url": "",
        "keyword": "all:web",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    url = "http://%s:%d" % (host, int(port))
    try:
        res_1 = requests.get(url + '/console/home',
                             timeout=timeout, allow_redirects=False)
        res = requests.get(url + '/', timeout=timeout, allow_redirects=False)
        if 'BES Console --' in res_1.text:
            info = 'BES管理后台：%s/console/home' % url
            return info
        if 'BES Console --' in res.text:
            info = 'BES管理后台：%s/' % url
            return info
    except Exception,e:
        pass
