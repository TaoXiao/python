# -*- encoding: utf-8 *-*


# 基于delay的调度器

import time
import sched

def print_event(name):
    print "Event: ",  time.asctime(time.localtime(time.time())),  name


# 创建scheduler
scheduler = sched.scheduler(time.time, time.sleep)

"""
3 - 延迟3秒
1 - 优先级为1
print_event - 要调用的函数
("Hello", ) - 传给函数的参数，必须是tuple形式的
"""
scheduler.enter(3, 1, print_event, ("Hello", ))

scheduler.enter(5, 1, print_event, ("Scheduler", ))


print "start"

# 启动延迟调度器
scheduler.run()

print "end"


"""最后输出为
start
Event:  Mon Jul 27 17:21:30 2015 Hello
Event:  Mon Jul 27 17:21:32 2015 Scheduler
end
"""