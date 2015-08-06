# -*- encoding: utf-8 -*-
__author__ = 'tao'

from fabric.api import *
from fabric.tasks import execute
from fabric.operations import sudo
from fabric.network import disconnect_all

env.hosts = ['root@ecs2.njzd.com:22']
env.password = {'root@ecs2.njzd.com:22' : 'Root1234NJ'}


def mytask():
    run("who am i")
    run("pwd")
    run("ls ./")


def sudoTask():
    sudo("hadoop dfs -put /home/tao/index.html /user/tao", user="hdfs")
    sudo("hadoop dfs -ls /user/tao")



print "\nstart !\n"
execute(sudoTask)
