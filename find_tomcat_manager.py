# coding:utf-8
# author:liil
import requests


def get_plugin_info():
    plugin_info = {
        "name": "Tomcat管理后台",
        "info": "用于发现管理后台，便于后续测试。",
        "level": "低危",
        "type": "信息探测",
        "author": "liil",
        "url": "",
        "keyword": "all:web",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    login_url = 'http://' + host + ":" + str(port) + '/manager/html'
    res = requests.get(login_url, timeout=timeout)
    if res.status_code == 401:
        info = '发现Tomcat管理后台'
        return info
