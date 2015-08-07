# -*- encoding: utf-8 -*-
__author__ = 'tao'


import json
import requests
import search


baseurl = "http://ecs2.njzd.com:9200"

"""
查看系统的健康状况
"""
def checkHealth():
    url = baseurl + "/_cluster/health"
    print "url = " + url

    response = requests.get(url)
    print "status code = " + str(response.status_code)

    print "content = " + json.dumps(json.loads(response.content), indent=4)




"""创建一个index，可以指定shard和replica的数量
"""
def createIndex(indexName, numShards, numReplicas):
    url = baseurl + "/" + indexName
    print "url = " + url

    payload = {
        "settings" : {
            "number_of_shards" : numShards,
            "number_of_replicas" : numReplicas
        }
    }

    response = requests.put(url, data=payload)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content




#checkHealth()
#createIndex("blog", 3, 1)
search.search(index="blog")
