# -*- encoding: utf-8 -*-


"""
需要下载 `mysql connector for python`
    地址 - http://dev.mysql.com/downloads/connector/python/

参考代码 http://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
"""


import mysql.connector




def query():
    conn = mysql.connector.connect(user="root", password="njzd2014", host="ecs5.njzd.com", database="platform")
    cursor = conn.cursor()


    """
    查询全部的数据
    """
    print "\n\n查询全部的数据"
    query = "select * from Test"
    cursor.execute(query)
    for (id, c1, c2, time) in cursor:
        print id, c1, c2, time



    """
    查询某个最大值
    """
    print "\n\n查询某个列的最大值"
    query = "select max(time) from Test"
    cursor.execute(query)
    for x in cursor:
        print x[0]


    """
    条件查询
    """
    print "\n\n条件查询"
    query = "select * from Test where time between %s and %s "
    cursor.execute(query, ("2015-07-28 11:27:27", "2015-07-28 11:28:17"))
    for (id, c1, c2, time) in cursor:
        print id, c1, c2, time




    """
    dump数据到文件
    """
    print "\n\ndump数据到文件"
    query = ("select id, c1, to_base64(c2) from Test where time >= %s and time < %s into outfile 'dump.data' fields terminated by X'01' lines terminated by X'02'")
    cursor.execute(query, ("2015-07-28 11:27:27", "2015-07-28 11:28:17"))
    # 现在cursor中没有任何数据了


    conn.close()


query()

