# -*- encoding : utf-8 -*-
__author__ = 'tao'


from fabric.operations import sudo
from fabric.api import local, settings, abort, run, cd, env, hosts
from fabric.contrib.console import confirm

env.hosts=['ecs2.njzd.com']

@hosts()
def sudoTest():
    run("pwd")