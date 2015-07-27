# -*- coding: utf-8 -*-

import requests
import base64
import json
import struct
from collections import OrderedDict




# 将int转为二进制字节数组后再转为base64编码的字符串
def b64encodeInt(n):
    data = struct.pack("i", n)
    return base64.b64encode(data)



# 转换float类型的数据
def b64encodeFloat(x):
    data = struct.pack("f", x)
    return base64.b64encode(data)




# 转换double类型的数据
def b64encodeDouble(x):
    data = struct.pack("d", x)
    return base64.b64encode(data)


def b64encode(data):
    if type(data) == str:      # data为str类型
        return base64.b64encode(data)
    elif type(data) == int:    # data为int类型
        return b64encodeInt(data)
    elif type(data) == float:   # data为float
        return b64encodeFloat(data)




"""
查询HBase中的表数据
插入数据
删除数据
"""

baseurl='http://ecs5.njzd.com:20550'
headers={'Accept':'application/json', "Content-Type" : "application/json"}





"""
查询满足rowkey条件的record
rowkey可以是精确匹配，也可以是带*的模糊匹配
(*只能放在rowkey的最后一个字符)
"""
def queryOneRecord(rowkey, table):
    rowkey64 = base64.b64encode(rowkey)

    url = baseurl + "/" + table + "/" + rowkey
    print "url = " + url

    response = requests.get(url, headers={'Accept':'application/json'})

    print "status_code = " + str(response.status_code)

    # response.content 是JSON形式的字符串
    results = json.loads(response.content)

    """ json.dumps(results, sort_keys=True, indent=4)输出的结果
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
    """
    经过解析、转码后的查询结果为
    rowkey = row-1
    Column = F1:C1	 | value = row1-F1-C1
    Column = F1:C2	 | value = row1-F1-C2
    """

    for row in results["Row"]:
        print "rowkey = " + base64.b64decode(row['key'])

        for cell in row["Cell"]:
            column = base64.b64decode(cell['column'])
            value  = base64.b64decode(cell['$'])
            print "\t\tColumn = " + column + "\t | value = " + value


"""
从table中删除一列数据
"""
def deleteOneColumn(rowkey, table, family, qualifier):
    print '描述：从名为 "' + table + '" 的表中删除一列数据，其行列坐标为：("' + str(rowkey) + '", "' + family + ':' + qualifier + '")'

    url = baseurl + "/" + table + "/" + (rowkey if type(rowkey) == str else b64encode(rowkey) ) +  "/" + family + ":" + qualifier

    print "url = " + url
    print "method = DELETE"

    response = requests.delete(url)
    print "status_code = " + str(response.status_code)




"""
插入新的record
"""
def insertOneColumn(rowkey, table, family, qualifier, value):
    rows = []
    jsonOutput = { "Row" : rows }

    cell = OrderedDict([
        ("key", b64encode(rowkey)),
        ("Cell", [
            { "column" : b64encode(family + ":" + qualifier), "$" : b64encode(value) }
        ])
    ])

    rows.append(cell)

    # URL里的rowkey不起作用
    url = baseurl + "/" + table + "/" + str(rowkey)
    print "url = " + url

    payload = json.dumps(jsonOutput, sort_keys=True, indent=4)
    print "payload = " + payload

    response = requests.post(url, data=payload, headers={ "Content-Type": "application/json", "Accept" : "application/json" })

    print "status_code = " + str(response.status_code)


"""
insertOneColumn("row-1", "X", "A", "a1", "110")
insertOneColumn("row-1", "X", "B", "b1", "120")
insertOneColumn("row-2", "X", "A", "a1", "210")
insertOneColumn("row-2", "X", "C", "c1", "220")
deleteOneColumn("row-1", "X", "A", "a1")
insertOneColumn(100, "X", "C", "c1", 200)
"""

#insertOneColumn(100, "X", "C", "c1", "one hundred")
deleteOneColumn(100, "X", "C", "c1")


