# coding:utf-8
import requests

def get_plugin_info():
    plugin_info = {
        "name": "Nexus未授权访问",
        "info": "导致敏感信息泄露。",
        "level": "高危",
        "type": "未授权访问",
        "author": "taro",
        "url": "",
        "keyword": "Nexus",
        "source": 1
    }
    return plugin_info

def check(host, port, timeout):
    url = "http://%s:%d" % (host, int(port)) + '/#admin/repository'
    try:
        res = requests.get(url, timeout=timeout)
        if res.status_code == 200:
            info = 'Nexus未授权访问: %s' % url
            return info
    except Exception, e:
        pass
