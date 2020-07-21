# coding:utf-8
# author:taro

import requests
def get_plugin_info():
    plugin_info = {
        "name": "Weblogic 任意文件上传漏洞",
        "info": "配置中启用 Web 服务测试页后，未授权的两个页面存在任意上传getshell漏洞，利用该漏洞可以上传任意jsp文件，进而获取服务器权限",
        "level": "紧急",
        "type": "RCE",
        "author": "taro",
        "url": "",
        "keyword": "all:weblogic",
        "source": 1
    }
    return plugin_info

def check(host, port, timeout):
    u = "http://%s:%d/" % (host, int(port))
    payload_url = '/ws_utc/config.do'
    url = u + payload_url
    data = ""
    try:
        res = requests.post(url, data=data, timeout=timeout)
        if 'Work Home Dir' in res.text:
            info = 'Weblogic 任意文件上传漏洞: %s' % payload_url
            #print info
            return info
    except Exception, e:
        pass
