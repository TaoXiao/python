# -*- encoding: utf-8 -*-
from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm

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
"""
def makeConnections():
    destDir = "/disk2/code"
    with cd(destDir):   # This is similar to `lcd` which does the same locally.
        run("pwd")
        run("touch XXXXXXXXXXXXXX.txt")



