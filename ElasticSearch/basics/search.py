# -*- encoding: utf-8 -*-
__author__ = 'tao'

import requests
import json

baseurl = "http://ecs2.njzd.com:9200"



"""在指定的(index, type)范围内搜索所有的document（无条件）
"""
def search(index, type=None):
    if type != None:
        url = baseurl + "/" + index + "/" + type + "/_search"
    else:
        url = baseurl + "/" + index + "/_search"

    print "url = " + url

    response = requests.get(url)
    print json.dumps(json.loads(response.content), indent=4)






"""在指定的(index, type)范围内搜索所有的document（根据指定的field值）
使用了query-string search方法
"""
def matchSearch_queryString(index, type, fieldName, fieldValue):
    url = baseurl + "/" + index + "/" + type + "/_search?q=" + fieldName + ":" + fieldValue
    print "url = " + url

    response = requests.get(url)
    print "status_code = " + str(response.status_code)
    print "content = "
    print json.dumps(json.loads(response.content), indent=4)






"""在指定的(index, type)范围内搜索所有的document（根据指定的field值）
使用了DSL方法
"""
def matchSearch_DSL(index, type, fieldName, fieldValue):
    url = baseurl + "/" + index + "/" + type + "/_search"
    print "url = " + url

    payload = { "query": {
        "match": {
            fieldName : fieldValue }
        }
    }

    print "payload = " + json.dumps(payload, indent=4)

    response = requests.get(url, data=payload)
    print "status_code = " + str(response.status_code)

    print "content = "
    print json.dumps(json.loads(response.content), indent=4)




"""match query，但是加上了range filter
执行发现会报错：SearchPhaseExecutionException[Failed to execute phase [query], all shards failed; shardFailures 。。。
"""
def rangeFilterSearch(index, type, fieldName, fieldValue, rangeFilter):
    url = baseurl + "/" + index + "/" + type + "/_search"
    print "url = " + url

    payload = {
        "query" : {
            "filtered" : {
                "filter" : {
                    "range" : {
                        "age" : { "gt" : 30 }
                    }
                },
                "query" : {
                    "match" : {
                        "lastName" : "Smith"
                    }
                }
            }
        }
    }


    print "payload = " + json.dumps(payload, indent=4)

    response = requests.get(url, data=payload)
    print "status_code = " + str(response.status_code)

    print "content = "
    print json.dumps(json.loads(response.content), indent=4)





def fullTextSearch(index, type, fieldName, fieldValue):
    url = baseurl + "/" + index + "/" + type + "/_search"
    print "url = " + url

    payload = {"query" : {
            "match" : {
                fieldName : fieldValue
            }
        }
    }
    print "payload = " + json.dumps(payload, indent=4)

    response = requests.get(url, data=payload)
    print "status_code = " + str(response.status_code)

    print "content = "
    print json.dumps(json.loads(response.content), indent=4)




#search(index="megacorp", type="employee")
#matchSearch_queryString(index="megacorp", type="employee", fieldName="lastName", fieldValue="Smith")
#matchSearch_DSL(index="megacorp", type="employee", fieldName="lastName", fieldValue="Smith")
#rangeFilterSearch(index="megacorp", type="employee", fieldName="lastName", fieldValue="Smith", rangeFilter= { "age" : {"gt" : 30}} )
#fullTextSearch(index="megacorp", type="employee", fieldName="about", fieldValue="love")
search(index="blog")