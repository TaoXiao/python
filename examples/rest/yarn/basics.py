__author__ = 'tao'

import requests
import json

baseurl = "http://ecs2.njzd.com:8088"

def killApp(appId):
    url = baseurl + "/ws/v1/cluster/apps/" + appId  + "/KILLED"
    print "url = " + url

    response = requests.put(url)
    print "status_code = " + str(response.status_code)
    print "content = " + response.content
   # print json.dumps(json.loads(response.content), indent=4)


killApp("application_1438849897472_0011")