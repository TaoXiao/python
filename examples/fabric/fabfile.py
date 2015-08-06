# -*- encoding: utf-8 -*-
#from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, env, hosts
from fabric.contrib.console import confirm
from fabric.operations import sudo


"""
Fabric依赖于paramiko

安装Fabric :
$ sudo pip install fabric

关于Fabric的文档：
http://fabric-docs.readthedocs.org/en/1.10/
"""


"""在console运行：
$ fab hello
"""
def hello():
    print "Hello, Fabric !"






"""在console运行:
$ fab bye:name=tao
"""
def bye(name="unknown"):
    print "Bye %s !" % name






"""执行本地shell的命令
"""
def localShellCommands():
    local("pwd")
    local("ls -al ./")






"""连接远程host，并在其上执行命令
We never specified any connection info in our fabfile,
so Fabric doesn’t know on which host(s) the remote command
should be executed.
When this happens, Fabric prompts us at runtime.

`run`是在远程主机上运行的, 如果没有指定host，那么运行时，控制台上会要求用户输入host及passwd

指定host的几个方法：

a) 在运行时指定主机,如下
    $  fab -H host1,host2  makeConnections

b). 在 makeConnections 中指定主机，如下
    env.hosts=["host1", "host2"]

    或者

    my_hosts = ('host1','host2')
    @hosts(my_hosts)
    def mytask():
        # ...

c). $ fab makeConnections:hosts="host1;host2"

以上a)和b)方法指定的主机是对所有的task生效的，方法c)可以针对特性的task指定主机

详见 http://fabric-docs.readthedocs.org/en/1.10/usage/execution.html#host-lists

"""
def makeConnections():
    destDir = "/disk2/code"
    with cd(destDir):   # This is similar to `lcd` which does the same locally.
        run("pwd")
        run("touch XXXXXXXXXXXXXX.txt")





"""以特定用户来登录主机
要指定各个主机的hostname - user - password
"""

env.hosts=['root@ecs2.njzd.com:22']
env.password={'root@ecs2.njzd.com:22' : 'Root1234NJ'}

def login():
    run("who am i")
    run("pwd")
    run("ls -al ./")





"""
Fabric’s contrib.console submodule contains the `confirm` function, used for simple "yes/no" prompts.
the abort function is used to manually abort execution
"""
def handleFailure():
    with settings(warn_only=True):
        result = local("test -d ./abc", capture=True)
    # 要求用户输入`Y/y'或者'N/n'
    if result.failed and not confirm ("Test failed. Continue anyway ?"):
        abort("Aboring at user request...")



"""在远程主机上执行sudo命令
"""
def sudoTest():
    run("who am i")