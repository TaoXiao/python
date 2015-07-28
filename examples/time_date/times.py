# -*- encoding: utf-8 -*-

import time

"""
 The function time.time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch).
"""
print time.time()   # 1437988187.23





"""
time tuple
"""
localtime = time.localtime(time.time())
print localtime  # time.struct_time(tm_year=2015, tm_mon=7, tm_mday=27, tm_hour=17, tm_min=9, tm_sec=47, tm_wday=0, tm_yday=208, tm_isdst=0)






"""
formatted time
"""
localtime = time.asctime(time.localtime(time.time()))
print localtime # Mon Jul 27 17:12:21 2015




"""
延迟,计算时间间隔（秒）
"""
start = time.time()
time.sleep(3)
end = time.time()
print "ok, difference = " , int(end - start)    # 单位是秒



print start