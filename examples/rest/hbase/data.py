# -*- coding: utf-8 -*-

import requests
import base64
import json
from collections import OrderedDict

baseurl='http://ecs5.njzd.com:20550'
headers={'Accept':'application/json', "Content-Type" : "application/json"}




"""
查询满足rowkey条件的record
rowkey可以是精确匹配，也可以是带*的模糊匹配
(*只能放在rowkey的最后一个字符)
"""
def queryOneRecord(rowkey, table):
    rowkey64 = base64.b32encode(rowkey)

    url = baseurl + "/" + table + "/" + rowkey
    print "url = " + url

    response = requests.get(url, headers={'Accept':'application/json'})

    print "status_code = " + str(response.status_code)

    # response.content 是JSON形式的字符串
    results = json.loads(response.content)

    """ json.dumps(results, sort_keys=True, indent=4)的结果
    {
        "Row": [
            {
                "Cell": [
                    {
                        "$": "cm93MS1GMS1DMQ==",
                        "column": "RjE6QzE=",
                        "timestamp": 1437727629694
                    },
                    {
                        "$": "cm93MS1GMS1DMg==",
                        "column": "RjE6QzI=",
                        "timestamp": 1437727629767
                    }
                ],
                "key": "cm93LTE="
            },
            {
                "Cell": [
                    {
                        "$": "cm93Mi1GMS1DMQ==",
                        "column": "RjE6QzE=",
                        "timestamp": 1437727629841
                    },
                    {
                        "$": "cm93Mi1GMS1DMw==",
                        "column": "RjE6QzM=",
                        "timestamp": 1437727629912
                    }
                ],
                "key": "cm93LTI="
            }
        ]
    }

    """
    print "results = " +  json.dumps(results, sort_keys=True, indent=4)

    print "\n经过解析、转码后的查询结果为"

    for row in results["Row"]:
        print "rowkey = " + base64.b64decode(row['key'])

        for cell in row["Cell"]:
            column = base64.b64decode(cell['column'])
            value  = base64.b64decode(cell['$'])
            print "\t\tColumn = " + column + "\t | value = " + value





"""
插入一条record
"""
def insertOneRecord(rowkey, table, family, qualifier, value):
    rows = []
    jsonOut = {"Row" : rows }

    """ We have to use an `OrderedDict` instead of a normal dict
        because we have to maintain the order of the keys in the dictionary.
        This works around an issue in the REST daemon for JSON. The bug is that
        the “key” entry must come before the “Cell” entry
    """
    cell = OrderedDict([
        ("key", base64.b64encode(rowkey)),  # 这里是真正起作用的rowkey
        ("Cell", [
            {"column" : base64.b64encode(family + ":" + qualifier), "$" : base64.b64encode(value)}]
        )
    ])

    rows.append(cell)

    # URL里的rowkey是不起作用的
    url = baseurl + "/" + table + "/" + "rowkey"
    print "url = " + url

    payload = json.dumps(jsonOut, sort_keys=True, indent=4)
    print "payload = " + payload

    response = requests.post(url, data=payload, headers=headers)
    print "status_code = " + str(response.status_code)






"""
从table中删除一条记录
"""
def deleteOneRecord(rowkey, table, family, qualifier):
    url = baseurl + "/" + table + "/" + rowkey + "/" + family + ":" + qualifier
    print "url = " + url

    response = requests.delete(url)
    print "status_code = " + str(response.status_code)



# deleteOneRecord("row-1", "X", "F1", "C1")

"""
insertOneRecord("row-1", "X", "F1", "C1", "row1-F1-C1")
insertOneRecord("row-1", "X", "F1", "C2", "row1-F1-C2")
insertOneRecord("row-2", "X", "F1", "C1", "row2-F1-C1")
insertOneRecord("row-2", "X", "F1", "C3", "row2-F1-C3")
"""

#queryOneRecord("row*", "X")

queryOneRecord("row-1", "X")