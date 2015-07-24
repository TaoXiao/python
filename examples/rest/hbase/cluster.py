# -*- coding: utf-8  -*-

import requests
import json

"""
如果没有[http://]则会报错[
requests.exceptions.InvalidSchema: No connection adapters were found for 'ecs5.njzd.com:20550/EXAMPLE/schema']
"""
baseurl='http://ecs5.njzd.com:20550'
tablename="food:products"
headers={'Accept':'application/json'}




"""
查询HBase中有哪些表
"""
def queryAllTables() :
    url = baseurl
    response = requests.get(url, headers=headers)
    print "url = " + url
    print "status_code = " + str(response.status_code)
    print "content = " + json.dumps(response.json(), sort_keys=True, indent=4)





"""
查询HBase的版本
"""
def queryVersion():
    url = baseurl + "/version"
    response = requests.get(url, headers=headers)
    print "url = " + url
    print "status_code = " + str(response.status_code)
    print "response = " + json.dumps(response.json(), sort_keys=True, indent=4)





"""
查询HBase的cluster状态
"""
def queryClusterStatus():
    url = baseurl + "/status/cluster"
    response = requests.get(url, headers=headers)
    print "url = " + url
    print "status_code = " + str(response.status_code)
    print "response = " + json.dumps(response.json(), indent=4, sort_keys=True)








