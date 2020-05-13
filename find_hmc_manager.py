# coding:utf-8
# author:liil
import requests


def get_plugin_info():
    plugin_info = {
        "name": "HMC管理后台",
        "info": "用于发现HMC管理后台，便于后续测试。",
        "level": "低危",
        "type": "信息探测",
        "author": "liil",
        "url": "",
        "keyword": "all:web",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    if int(port) == 443:
        url = 'https://%s' % host
    else:
        url = "https://%s:%d" % (host, int(port))
    payload_url = url + '/hmc/connect'
    try:
        print payload_url
        res_1 = requests.get(payload_url,timeout=timeout,verify=False)
        if 'hmcBanner' in res_1.text:
            info = 'HMC管理后台：%s' % payload_url
            print info
            return info
    except Exception,e:
        pass
