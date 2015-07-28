# -*- encoding: utf-8 -*-

import time


"""
范围
second: 00 ~ 59
minute: 00 ~ 59
hour  : 00 ~ 23
"""
class Clock:
    second = -1
    minute = -1
    hour   = -1

    def __init__(self, h=0, m=0, s=0):
        self.second = s
        self.minute = m
        self.hour = h


    def toSring(self):
        return str(self.hour) + " Hour, " +  str(self.minute) + " Minute, " +  str(self.second) + " Second"

    """
    加上一个interval的结果，返回一个新的实例，不影响当前的数据
    """
    def addInterval(self, h=0, m=0, s=0):
        newSecond = (self.second + s)%60
        secCarry = (self.second + s)/60  # 秒数相加引起的分钟的进位

        newMinute = (self.minute + m + secCarry)%60
        minCarry = (self.minute + m + secCarry)/60

        newHour = (self.hour + h + minCarry)%60

        return Clock(newHour, newMinute, newSecond)




"""
现在离c指定的时间还有多少秒
如果今天这个时间点已经过去了，就要从明天开始计算
"""
def secondsUntilNow(c):
    now = time.localtime(time.time())

    # 首先计算今天这个时间点有没有过去
    if now.tm_hour > c.hour:
        p = True
    elif now.tm_hour < c.hour:
        p = False
    else:
        if now.tm_min > c.minute:
            p = True
        elif now.tm_min < c.minute:
            p = False
        else:
            if now.tm_sec > c.second:
                p = True
            else:
                p = False

    dist = (c.hour - now.tm_hour)*60*60 + (c.minute - now.tm_min)*60 + (c.second - now.tm_sec)

    if p:
        return dist + 24*60*60
    else:
        return dist



"""
basePoint - 第一次运行的时间（单位为clock）
interval  - 后续运行的间隔(单位为秒)
"""
class IntervalBasedSched:

    def __init__(self, basePoint, interval):
        self.interval = interval
        # 还要等多少秒可以开始第一次运行
        self.waitingSeconds = secondsUntilNow(basePoint)
        self.count = 0
        print "离第一次运行还有" + str(self.waitingSeconds) + '秒'


    # 开始调度
    def start(self, action, *args):
        while True:
            if 0 == self.waitingSeconds:
                self.count += 1
                action(args)
                # 辅助调试信息  print '第' + str(self.count) + '次运行'
            else:
                time.sleep(self.waitingSeconds)
                start = time.time()
                self.count += 1
                action(args)    # action
                # 辅助调试信息  print '第' + str(self.count) + '次运行'
                end = time.time()

                # 从start到end共流逝了多少秒
                elapsed = int(end - start)
                self.waitingSeconds = self.interval - elapsed





"""
用法示例：
从9点56分0秒开始，每隔3秒执行一个函数
目标函数是F，传入的参数是Hi
"""

def F(arg):
    print "hello"


sch = IntervalBasedSched(Clock(9,56,0), 3)


sch.start(F)


