# -*- coding: utf-8 *-*

import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("admin", "admin")


"""
查询Clouder Manager 的API版本
"""
def queryCMVersion():
    url = "http://ecs1.njzd.com:7180/api/version"
    response = requests.get(url, auth=auth)
    return response.content

# 全局变量，获取API的版本
version = queryCMVersion()
baseurl = "http://ecs1.njzd.com:7180/api/" + version


"""
查询该Cloudera Manager管理了哪些clusters，输出如下
status_code = 200
content = {
  "items" : [ {
    "name" : "cluster",
    "displayName" : "Cluster 1",
    "version" : "CDH5",
    "fullVersion" : "5.3.5",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "clusterUrl" : "http://ecs1.njzd.com:7180/cmf/clusterRedirect/cluster"
  } ]
}
"""
def queryClusters():
    url = baseurl + "/clusters"
    response = requests.get(url, auth=auth)

    print "status_code = " + str(response.status_code)
    print "content = " + response.content




#queryCMVersion()
queryClusters()
