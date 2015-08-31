# -*- encoding: utf-8 -*-
__author__ = 'tao'


print "Outside main(), __name__ == ", __name__


if __name__ == '__main__':
    print "This is ", __name__


def main():
    print "In main(), __name__ == ", __name__
    if __name__ == '__main__':
        print "Inside main, now __name__ is __main__ "




""" 执行 `python -m mainFunction.foo` 之后，输出如下：

Outside main(), __name__ ==  __main__
This is  __main__

说明：这种方式运行python文件时，不会去调用其中定义的任何函数，包括main函数
     只会执行在最外层定义的语句。

     如果要想调用main函数，可以如下：
     if __name__ == '__main__':
        main()
"""