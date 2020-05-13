# coding:utf-8

import ldap

def get_plugin_info():
    plugin_info = {
        "name": "LDAP未授权访问",
        "info": "LDAP未授权访问，可能导致敏感信息泄露等",
        "level": "高危",
        "type": "未授权访问",
        "author": "taro",
        "url": "",
        "keyword": "port:389",
    }
    return plugin_info


def check(host, port, timeout):
    try:
        ldapObject = ldap.open(host=host, port=int(port),timeout=timeout)
        ldapObject.simple_bind_s()
#        print ldapObject
        if ldapObject != None:
            info = '%s:%s存在LDAP未授权访问' % (host, port)
            return info
    except Exception, e:
        pass

#if __name__ == '__main__':
#    check('10.182.26.149','389',10)

