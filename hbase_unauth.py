# coding:utf-8
import requests


def get_plugin_info():
    plugin_info = {
        "name": "HBase未授权访问",
        "info": "导致敏感信息泄露。",
        "level": "高危",
        "type": "未授权访问",
        "author": "liil",
        "url": "",
        "keyword": "port:60030",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    url = "http://%s:%d/" % (host, int(port))
    payloads = ['rs-status','conf']
    try:
        for payload in payloads:
            payload_url = url + payload
            res = requests.get(payload_url, timeout=timeout)
            if 'hbase' in res.text:
                info = 'HBase未授权访问: %s' % payload_url
                return info
    except Exception, e:
        pass
