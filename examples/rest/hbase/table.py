# -*- coding: utf-8 *-*

# HBase关于创建类的API，创建namespace和table

import json
import requests

from collections import OrderedDict

baseurl='http://ecs5.njzd.com:20550'
headers={'Accept':'application/json', "Content-Type" : "application/json"}




"""
查询指定表的schema
"""
def queryTable(name):
    url = baseurl + "/" + name + "/schema"
    response = requests.get(url, headers=headers)
    print "url =  " + url
    print "status_code = " + str(response.status_code)
    print "response = " + json.dumps(response.json(),sort_keys=True, indent=4)





"""
创建一个table，或者为一个table增加若干family (至少要指定一个column)
返回码：
    1) 创建新表，成功返回201
    2) 为一个已有表增加family，成功返回200
"""
def createTable(tableName, cf, *moreCF):
    families = cf
    for c in moreCF:
        families += ", " + c

    print '描述：新建一个名为 "' + tableName + '" 的table，并指定如下' + str(len(moreCF) + 1) + '个Family : ' + families

    columns = []
    jsonOutput = OrderedDict({"name": tableName ,
            "ColumnSchema" : columns
    })

    columns.append({"name":cf})

    for f in moreCF :
        columns.append({"name":f})

    url = baseurl + "/" + tableName + "/schema"
    print "url = " + url
    print 'method = POST'
    print "pay_load = " + json.dumps(jsonOutput, sort_keys=True, indent=4)

    """ post是修改table的schema,put是完全替换table原有的schema """
    response = requests.post(url, data=json.dumps(jsonOutput), headers=headers)
    print "status_code = " + str(response.status_code)



"""
为一张表新建一个family
"""
def addOneFamily(table, family):
    print "为表 " + table + " 增加一个名为 " + family + " 的family"
    columns = []
    jsonOutput = OrderedDict({"name" : table, "ColumnSchema" : columns})
    columns.append({"name" : family})

    url = baseurl + "/" + table + "/schema"
    print "url = " + url
    print "method = POST"

    pay_load=  json.dumps(jsonOutput, sort_keys=True, indent=4)
    print "payload = " + pay_load

    response = requests.post(url, data=pay_load, headers=headers)
    print "status code = " + str(response.status_code)



"""
删除一个table
删除成功的返回码是200
"""
def deleteTable(tableName):
    print '描述：删除表名为 "' + tableName + '" 的table'
    url = baseurl + "/" + tableName + "/schema"
    print "url = " + url

    response = requests.delete(url)
    print "method = DELETE"
    print "status_code = " + str(response.status_code)



# deleteTable("x")
# createTable("X", "A", "B", "C")
addOneFamily("X", "H")

