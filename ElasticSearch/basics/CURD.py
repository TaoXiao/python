# -*- encoding: utf-8 -*-
__author__ = 'tao'

import json
import requests

baseurl = "http://ecs2.njzd.com:9200/"


"""查询cluster中所有documents的数量
"""
def numOfDocs():
    url = baseurl + "_count?pretty"
    payload = { "query": {
        "match_all" : {
        }
    }}

    response = requests.post(url, data=json.dumps(payload))
    print "status_code = " +  str(response.status_code)
    print "content = " + response.content





""" 添加一个document
"""
def addDoc(dict, index, type, id):
    url = baseurl + "/" + index + "/" + type + "/" + id
    response = requests.put(url, data=json.dumps(dict))
    print "status_code = " +  str(response.status_code)
    print "content = " + response.content





"""返回原始的document
"""
def getDoc(index, type, id):
    url = baseurl + "/" + index + "/" + type + "/" + id
    response = requests.get(url)
    print "status_code = " +  str(response.status_code)
    print "content = "
    print json.dumps(json.loads(response.content), indent=4)




"""删除一个document
"""
def rmDoc(index, type, id):
    url = baseurl + "/" + index + "/" + type + "/" + id
    response = requests.delete(url)
    print "status_code = " +  str(response.status_code)
    print "content = "
    print json.dumps(json.loads(response.content), indent=4)





"""检测一个document是否存在
"""
def checkDoc(index, type, id):
    url = baseurl + "/" + index + "/" + type + "/" + id
    response = requests.head(url)
    print "status_code = " +  str(response.status_code)






addDoc({
        "firstName" : "John",
        "lastName"  : "Smith",
        "age"       : 25,
        "about"     : "I love you",
        "interests" : ["sports", "music"] },
    "megacorp", "employee", "1")

addDoc({
        "first_name" : "Jane",
        "last_name": "Smith",
        "age" : 32,
        "about" : "I like to collect rock albums", "interests": [ "music" ] },
    "megacorp", "employee", "2")


addDoc({
        "first_name" : "Douglas",
        "last_name": "Fir",
        "age" : 35,
        "about": "I like to build cabinets", "interests": [ "forestry" ]},
    "megacorp", "employee", "3")

"""
checkDoc("megacorp", "employee", "1")
rmDoc("megacorp", "employee", "3")
getDoc("megacorp", "employee", "3")"""


#numOfDocs()