# -*- encoding: utf-8 -*-

class MyClass:
    """一个定义class的例子"""
    i = 12345

    def f(self):
        print "i = " , str(self.i)
        print "doc = ", __doc__

    """
    When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance
    """
    def __init__(self, c):
        self.i = self.i*c



x = MyClass(10)

x.f()