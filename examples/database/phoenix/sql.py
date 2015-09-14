# -*- encoding: utf-8 -*-
__author__ = 'tao'

import jaydebeapi

conn = jaydebeapi.connect('org.apache.phoenix.jdbc.PhoenixDriver',
                          ['jdbc:phoenix:hadoop1.com:2181', '', ''],
                          '/Users/tao/百度云同步盘/中转站/sentiment-etl/jars/phoenix-4.3.1-client.jar')

curs = conn.cursor()


""" 查询全部的fields
"""
curs.execute('select * from "FsnLims:lims.t_sys_resource" where ASSIGN_ID = \'28b6928f899a4f4ca604cf4cf95a1ef3\' ')
ret = curs.fetchall()

# ret 是List类型
type(ret)
for x in ret:
    # x 是 tuple 类型
    print type(x)

""" 查询特定的fields
"""
curs.execute('select "RESURCE_ID" from "FsnLims:lims.t_sys_resource" where ')


print "down"

