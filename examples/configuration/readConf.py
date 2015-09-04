# -*- encoding: utf-8 -*-
__author__ = 'tao'

import sys
import ConfigParser

# 配置文件的路径
# 根目录是执行python命令时所在的目录
CONF_FILE = "./conf/conf.ini"

def main(args):
    cnf = ConfigParser.ConfigParser()
    cnf.read(CONF_FILE)

    """ 所有的section
    输出 sections :  ['person', 'city']
    """
    secs = cnf.sections()
    print "sections : ", secs

    """ `person`这个section下的所有key
    输出 options :  ['name', 'age', 'city']
    """
    opts = cnf.options("person")
    print "options : ", opts

    """ `city`这个section下的所有的键值对
    输出items :  [('city', '\xe5\x8d\x97\xe4\xba\xac'), ('district', '\xe5\xbb\xba\xe9\x82\xba'), ('corp', '\xe5\x8d\x97\xe4\xba\xac\xe6\x99\xba\xe5\xa4\xa7')]
    """
    items = cnf.items("city")
    print "items : ", items

    """ getint可以返回整型
    输出 31
    """
    print cnf.getint("person", "age")

    print cnf.get("person", "name")

    """
    """
    print cnf.get("city", "corp")



if __name__ == "__main__":
    main(sys.argv)