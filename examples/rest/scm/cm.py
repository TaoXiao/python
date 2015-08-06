# -*- coding: utf-8 *-*

import requests
from requests.auth import HTTPBasicAuth
import json

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
    print "url = " + url
    print "status_code = " + str(response.status_code)
    print "content = " + response.content







"""
查询SCM管理的所有节点

对于名字为"cluster"的集群而言，返回结果为：

url = http://ecs1.njzd.com:7180/api/v10/clusters/cluster/hosts
status_code = 200
content = {
  "items" : [ {
    "hostId" : "7c27cb35-1588-4b11-80d7-f2a541f3d7a5"
  }, {
    "hostId" : "f5e3aeae-8ca1-4a95-9ab0-54897a08faf9"
  }, {
    "hostId" : "ec0c70a1-475a-40f3-9f64-572b12c5374d"
  }, {
    "hostId" : "c74a08cc-3b8a-41e4-a836-acc66b9c4516"
  }, {
    "hostId" : "03509a31-1812-4ad4-915c-ab756a1b0ddc"
  } ]
}
"""
def queryAllHosts(clusterName):
    url = baseurl + "/clusters/" + clusterName + "/hosts"
    print "url = " + url

    response = requests.get(url, auth=auth)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content






"""
查询一个cluster中某个node的数据
"""
def queryOneHost(clusterName, hostId):
    url = baseurl + "/clusters/" + clusterName + "/hosts/" + hostId
    print "url = " + url

    response = requests.get(url, auth=auth)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content








""" 查询一个cluster中各个services的状态数据
"""
def queryServices(clusterName):
    url = baseurl + "/clusters/" + clusterName + "/services"
    print "url = " + url

    response = requests.get(url, auth=auth)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content




def queryOneService(clusterName, serviceName):
    url = baseurl + "/clusters/" + clusterName + "/services/" + serviceName
    print "url = " + url

    response = requests.get(url, auth=auth)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content



"""查询某个cluster上某个service的配置数据
例如，查询HDFS的配置数据
url = http://ecs1.njzd.com:7180/api/v10/clusters/cluster/services/hdfs/config
status_code = 200
content = {
  "items" : [ {
    "name" : "audit_event_log_dir",
    "value" : "/disk1/var/log/hadoop-hdfs/audit"
  }, {
    "name" : "dfs_block_size",
    "value" : "402653184"
  }, {
    "name" : "dfs_namenode_acls_enabled",
    "value" : "true"
  }, {
    "name" : "firehose_hdfs_canary_directory",
    "value" : "/disk2/tmp/.cloudera_health_monitoring_canary_files"
  }, {
    "name" : "hdfs_canary_health_enabled",
    "value" : "false"
  } ]
}
"""
def queryServiceConfig(clusterName, serviceName):
    url = baseurl + "/clusters/" + clusterName + "/services/" + serviceName + "/config"
    print "url = " + url

    response = requests.get(url, auth=auth)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content




""" 查询某个cluster的某个service的各个角色
"""
def queryServiceRoles(clusterName, serviceName):
    url = baseurl + "/clusters/" + clusterName + "/services/" + serviceName + "/roles"
    print "url = " + url

    response = requests.get(url, auth=auth)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content




def queryServiceRoleTypes(clusterName, serviceName):
    url = baseurl + "/clusters/" + clusterName + "/services/" + serviceName + "/roleTypes"
    print "url = " + url

    response = requests.get(url, auth=auth)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content



def queryOneServiceRole(clusterName, serviceName, roleName):
    url = baseurl + "/clusters/" + clusterName + "/services/" + serviceName + "/roles/" + roleName
    print "url = " + url

    response = requests.get(url, auth=auth)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content




def queryRoleConfig(clusterName, serviceName, roleName):
    url = baseurl + "/clusters/" + clusterName + "/services/" + serviceName + "/roles/" + roleName + "/config"
    print "url = " + url

    response = requests.get(url, auth=auth)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content



def queryRoleMetrics(clusterName, serviceName, roleName):
    url = baseurl + "/clusters/" + clusterName + "/services/" + serviceName + "/roles/" + roleName + "/commands"
    print "url = " + url

    response = requests.get(url, auth=auth)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content



"""
查询HBase Rest Server的IP和Port

步骤
1） 通过/clusters/"cluster"/services/"hbase"/roles查询HBase的roles，在返回结果中找到 "type" = "HBASERESTSERVER"的那一项，
    然后在该项中取出"hostRef"中的"hostId"的值（例如是"hbase-HBASERESTSERVER-a83a274ef0acd1dc7ed885dbd8f89def"），
    这个值就是HBase Rest Server所在节点的hostId
2)  通过/hosts/{hostId}找出该host的HOSTNAME和IP
3)  通过/clusters/{clusterName}/services/{serviceName}/roles/{roleName}/config?view=full来找出
    "name" == "hbase_restserver_port"的哪一项，其中的"default"就是port
"""
def queryHBaseRestServer(clusterName):
    # step 1 : query hostId of HBase Rest Server
    url = baseurl + "/clusters/" + clusterName + "/services/hbase/roles"
    content = json.loads(requests.get(url, auth=auth).content)
    for item in content["items"]:
        if item["type"] == "HBASERESTSERVER":
            roleName = item["name"]
            hostId = item["hostRef"]["hostId"]
            break

    # step 2 ：query hostname & ip of that host
    url = baseurl + "/hosts/" + hostId
    content = json.loads(requests.get(url, auth=auth).content)
    hostname = content["hostname"]
    ip = content["ipAddress"]


    # step 3: query port of hbase rest server
    url = baseurl + "/clusters/" + clusterName + "/services/hbase/roles/" + roleName + "/config?view=full"
    content = json.loads(requests.get(url, auth=auth).content)
    for item in content["items"]:
        if item["name"] == "hbase_restserver_port":
            port = item["default"]

    return {"roleName" : roleName,
            "hostId"   : hostId,
            "hostName" : hostname,
            "ip"       : ip,
            "port"     : port}





def queryCMServices():
    url = baseurl + "/cm/service/roles"
    print "url = " + url

    response = requests.get(url, auth=auth)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content


"""
queryCMVersion()
queryClusters()
queryAllHosts("cluster")
queryOneHost("cluster", "7c27cb35-1588-4b11-80d7-f2a541f3d7a5")
queryServices("cluster")
queryServiceConfig("cluster", "hdfs")
queryServiceRoles("cluster", "hbase")
queryOneServiceRole("cluster", "hbase", "hbase-HBASERESTSERVER-a83a274ef0acd1dc7ed885dbd8f89def")
queryRoleConfig("cluster", "hbase", "hbase-HBASERESTSERVER-a83a274ef0acd1dc7ed885dbd8f89def")
queryHBaseRestServer("cluster", "hbase", "hbase-HBASERESTSERVER-a83a274ef0acd1dc7ed885dbd8f89def")
queryOneService("cluster", "hbase")
queryServiceRoles("cluster", "hbase")
"""

#queryOneService("cluster", "hbase")
#queryServiceRoles("cluster", "hbase")
#queryRoleConfig("cluster", "hbase", "hbase-HBASERESTSERVER-a83a274ef0acd1dc7ed885dbd8f89def")
#queryRoleMetrics("cluster", "hbase", "hbase-HBASERESTSERVER-a83a274ef0acd1dc7ed885dbd8f89def")
#queryServiceConfig("cluster", "hbase")
#queryServiceRoleTypes("cluster", "hbase")
#queryAllHosts("cluster")
print json.dumps(queryHBaseRestServer("cluster"), indent=4)
