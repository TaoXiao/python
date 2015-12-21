# -*- encoding: utf-8 -*-
__author__ = 'tao'


##############################################
# 对日期进行处理
##############################################

import datetime
import time

"""
例1： 用字符串来初始化time object
参考 http://importpython.blogspot.com/2009/12/how-to-get-todays-date-in-yyyymmdd.html
"""
t1 = time.strptime("2015-08-30", "%Y-%m-%d")
print t1 # 输出time.struct_time(tm_year=2015, tm_mon=8, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=242, tm_isdst=-1)

t2 = datetime.datetime.strptime("2015-12-01", "%Y-%m-%d")
print t2  # 输出 2015-12-01 00:00:00
print str(t2)

t3 = t2 + datetime.timedelta(days=10) # 输出 2015-12-11 00:00:00
print t3

if t2 < t3 :    # 正确
    print "t2 < t3"


t4 = datetime.datetime.strptime("2015-12-01 0:0:00", "%Y-%m-%d %H:%M:%S")
print t4
print t4.strftime("%Y%m%d%H%M%S")

if t2 == t4:    # 正确
    print "t2 == t4"



