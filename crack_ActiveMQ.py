# coding:utf-8
import urllib2
import base64

def get_plugin_info():
    plugin_info = {
        "name": "ActiveMQ弱口令",
        "info": "攻击者通过此漏洞可以登陆管理控制台，甚至能够获取GetShell。",
        "level": "高危",
        "type": "弱口令",
        "author": "liil",
        "url": "",
        "keyword": "title:ActiveMQ",
        "source": 1
    }
    return plugin_info


def check(host, port, timeout):
    url = "http://%s:%d" % (host, int(port))
    flag_list = ['ActiveMQ Console', 'Welcome']
    user_list = ['admin']
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    for user in user_list:
        for password in PASSWORD_DIC:
            try:
                base64string = base64.encodestring('%s:%s' % (user, password))[:-1]
                authheader = "Basic %s" % base64string
                opener.addheaders = [('Authorization', authheader)]
                request = opener.open(url + '/admin/', timeout=timeout)
                res_html = request.read()
                print res_html
            except Exception, e:
                continue
            for flag in flag_list:
                if flag in res_html:
                    info = u'%s/admin/ 账号：%s，密码：%s' % (url, user, password)
                    return info
