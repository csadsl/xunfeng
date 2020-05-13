# coding:utf-8
# author:taro
# 巡风存在该插件

import requests
def get_plugin_info():
    plugin_info = {
        "name": "ElasticSearch 未授权访问",
        "info": "未授权访问导致数据信息泄露，部分版本或插件存在漏洞，严重可导致服务器被入侵",
        "level": "高危",
        "type": "未授权访问",
        "author": "taro",
        "url": "",
        "keyword": "port:9200",
        "source": 1
    }
    return plugin_info

def check(host, port, timeout):
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/_cat/'
    url = u + payload_url
    try:
        res = requests.get(url, timeout=timeout)
        if '/_cat/master' in res.text:
            info = '存在未授权访问: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
