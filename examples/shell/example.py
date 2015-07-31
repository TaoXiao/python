# *-* encoding: utf-8 -*-
__author__ = 'tao'

import subprocess

print "开始执行shell命令\n"

"""
subprocess.call(["command", "agr1", "arg2", "agr3", ...])
第一个字段是命令，后面的字段都是该命令的参数
"""
subprocess.call("pwd")
subprocess.call(["cat", "/Users/tao/IdeaProjects/guizhou_food_security/README.md"])




"""
执行带pipeline的几个命令时,
如：cat /Users/tao/IdeaProjects/guizhou_food_security/README.md | grep Forked

需要用如下的方式
"""
p1 = subprocess.Popen(["cat", "/Users/tao/IdeaProjects/guizhou_food_security/README.md"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "Forked"], stdin=p1.stdout)

