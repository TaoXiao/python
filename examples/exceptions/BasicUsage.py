# -*- encoding: utf-8 -*-
__author__ = 'tao'

import sys


#############################################
# 例子1：嵌套try语句
#############################################
def example1():
    print "例子1：嵌套try语句"
    while True:
        try:
            x = int(raw_input("请输入第1个整数"))
            y = int(raw_input("请输入第2个整数"))
            try:
                print "%d/%d = %d" % (x, y, x/y)
            except ZeroDivisionError:
                print "第2个输入（分母）不得为0，请重新输入"
        except ValueError:
            print "非法输入，请输入整数"




#############################################
# 例子2: 多个except语句
#############################################
def example2():
    print "例子2: 多个except语句"
    while True:
        try:
            x = int(raw_input("请输入第1个整数"))
            y = int(raw_input("请输入第2个整数"))
            print "%d/%d = %d" % (x, y, x/y)
        except ValueError, ex1: # 相当于 except ValueError as ex1
            print ex1.message, "非法输入，请输入整数"
        except ZeroDivisionError, ex2:
            print ex2.message, "第2个输入（分母）不得为0，请重新输入"




#############################################
# 例子：except中含多种异常
#############################################
def example3():
    print "例子：except中含多种异常"
    while True:
        try:
            x = int(raw_input("请输入第1个整数"))
            y = int(raw_input("请输入第2个整数"))
            print "%d/%d = %d" % (x, y, x/y)
        except (ValueError, ZeroDivisionError):  # 能同时拦截两类异常
            print "可能的两类异常之一"



#############################################
# 例子：默认异常的处理
#############################################
def example4():
    print "例子默认异常的处理"
    while True:
        try:
            x = int(raw_input("请输入第1个整数"))
            y = int(raw_input("请输入第2个整数"))
            print "%d/%d = %d" % (x, y, x/y)
        except ValueError:
            print "非法输入，请输入整数"
        except: # 未能被匹配到的异常都在这里被拦截
            print "未知类型的异常：",  sys.exc_info() # 从异常信息可以看出其真正的异常类型
            raise # 应该重新将其抛出至上层应用



#############################################
# 例子： try ··· except ··· else
#############################################
def example5():
    print "例子: try ··· except ··· else"
    while True:
        try:
            x = int(raw_input("请输入第1个整数"))
            y = int(raw_input("请输入第2个整数"))
            print "%d/%d = %d" % (x, y, x/y)
        except ValueError, ex1: # 相当于 except ValueError as ex1
            print ex1.message, "非法输入，请输入整数"
        except ZeroDivisionError, ex2:
            print ex2.message, "第2个输入（分母）不得为0，请重新输入"
        else:
            print "一切正常"




#############################################
# 例子：带参数的异常
#############################################
def example6():
    print "例子：带参数的异常"
    try:
        raise ValueError('arg1', 'arg2')
    except ValueError as ex:
        print type(ex)      # <type 'exceptions.ValueError'>
        print ex.args       # ('arg1', 'arg2')
        print ex.__str__()  # ('arg1', 'arg2')
        x, y = ex.args
        print 'x = ', x     # x =  arg1
        print 'y = ', y     # y =  arg2







#############################################
# 例子：Clean-up Actions: finally
# When an exception has occurred in the `try` clause and has not been handled by
# an `except` clause (or it has occurred in a except or else clause), it is re-raised
# after the `finally` clause has been executed. The `finally` clause is also executed
# “on the way out” when any other clause of the `try` statement is left via a `break`, `continue` or `return` statement.
#############################################
def example7():
    print "例子2: 多个except语句"
    while True:
        try:
            x = int(raw_input("请输入第1个整数"))
            y = int(raw_input("请输入第2个整数"))
            print "%d/%d = %d" % (x, y, x/y)
        except ValueError, ex1: # 相当于 except ValueError as ex1
            print ex1.message, "非法输入，请输入整数"
        finally:
            print "finally clause"  # finally 执行完后，未被处理的异常会被re-raised



# try:
#    example6()
# except ZeroDivisionError:
#    print "捕捉到了下层抛出的异常"



try:
    example7()
except ZeroDivisionError:
    print "不能被0除"
