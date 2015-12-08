# -*- encoding: utf-8 -*-
__author__ = 'tao'


#############################################
# 自定义的异常
#############################################

##############################################################
# User-defined exceptions should typically be derived from
# the Exception class, either directly or indirectly.
##############################################################
class MyException(Exception):
    # In this example, the default __init__() of Exception
    # has been overridden. The new behavior simply creates
    # the `value` attribute. This replaces the default
    # behavior of creating the `args` attribute.
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)



try:
    raise MyException(2*3)
except MyException as ex:
    print ex.value


raise MyException(4*5)






