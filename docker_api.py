# coding:utf-8
# author:taro

import requests
def get_plugin_info():
    plugin_info = {
        "name": "Docker Remote API 未授权访问",
        "info": "Docker Remote API未授权访问可导致代码泄露，严重可导致服务器被入侵控制",
        "level": "高危",
        "type": "未授权访问",
        "author": "taro",
        "url": "",
        "keyword": "all:2375",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/info'
    url = u +payload_url
    try:
        res = requests.get(url, timeout=timeout)
        if 'ContainersRunning' in res.text:
            info = '存在未授权访问: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
