# -*- encoding: utf-8 -*-

__author__ = 'tao'

import requests
from requests.auth import HTTPBasicAuth
import json
import cm

auth = HTTPBasicAuth("admin", "admin")
version = cm.queryCMVersion()
baseurl = "http://ecs1.njzd.com:7180/api/" + version



"""获取time series数据
其中，query是必须的参数，start和end是可选的参数
"""
def retrieveTS(query, start=None, stop=None):
    url = baseurl + "/timeseries?query=" + query
    if start != None:
        url += "&from=" + start
    if stop != None:
        url += "&to=" + stop


    response = requests.get(url, auth=auth)

    print "url = " + url
    print "status_code = " + str(response.status_code)
    print "content = " + response.content




def retrieveDashboards():
    url = baseurl + "/timeseries/dashboards"
    response = requests.get(url, auth=auth)

    print "url = " + url
    print "status_code = " + str(response.status_code)
    print response.content
    #print "content = " + json.dumps(json.loads(response.content), indent=4)




retrieveTS("select physical_memory_used")