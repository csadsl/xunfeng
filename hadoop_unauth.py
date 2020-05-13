# coding:utf-8
import requests


def get_plugin_info():
    plugin_info = {
        "name": "Hadoop未授权访问",
        "info": "导致Hadoop集群敏感信息泄露。",
        "level": "高危",
        "type": "未授权访问",
        "author": "liil",
        "url": "",
        "keyword": "port%3A50030%3Bport%3A50060%3Bport%3A50070%3Bport%3A50075%3Bport%3A50076%3Bport%3A50082%3Bport%3A50090%3Bport%3A50105%3Bport%3A8042%3Bport%3A8088%3Bport%3A8480%3Bport%3A8483%3Bport%3A19888",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    url = "http://%s:%d/" % (host, int(port))
    payloads = ['cluster','node','dataNodeHome.jsp','dfshealth.html','journalstatus.jsp','jobhistory','status.html']
    try:
        for payload in payloads:
            payload_url = url + payload
            res = requests.get(payload_url, timeout=timeout)
            if 'Hadoop' in res.text and 'Cluster' in res.text:
                info = 'Hadoop信息泄露漏洞: %s' % payload_url
                return info
            elif 'NodeManager information' in res.text and 'Hadoop' in res.text:
                info = 'Hadoop信息泄露漏洞: %s' % payload_url
                return info
            elif 'DataNode' in res.text and 'Hadoop' in res.text:
                info = 'Hadoop信息泄露漏洞: %s' % payload_url
                return info
            elif 'JournalNode' in res.text and 'Hadoop' in res.text:
                info = 'Hadoop信息泄露漏洞: %s' % payload_url
                return info
            elif 'Overview' in res.text and 'Hadoop' in res.text:
                info = 'Hadoop信息泄露漏洞: %s' % payload_url
                return info
            elif 'JobHistory' in res.text and 'Hadoop' in res.text:
                info = 'Hadoop信息泄露漏洞: %s' % payload_url
                return info
    except Exception, e:
        pass
