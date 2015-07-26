# -*- coding:utf-8 -*-

__author__ = 'tao'


import array

str = "你好，Python!"



# 将str中的每一个字符变成字节（十六进制表示）
bytes1 = [c.encode("hex") for c in str]
"""输出
type of bytes1 is  <type 'list'>
['e4', 'bd', 'a0', 'e5', 'a5', 'bd', 'ef', 'bc', '8c', '50', '79', '74', '68', '6f', '6e', '21']
"""
print "type of bytes1 is ", type(bytes1)
print bytes1, "\n\n"





# 用array module中的array来表示数组，
# 参见[array — Efficient arrays of numeric values](https://docs.python.org/2/library/array.html)
bytes2 = array.array('B', str)
"""输出
<type 'array.array'>
array('B', [228, 189, 160, 229, 165, 189, 239, 188, 140, 80, 121, 116, 104, 111, 110, 33])
"""
print "type of bytes2 is ", type(bytes2)
print bytes2, "\n\n"




# 利用内置的bytearray类
bytes3 = bytearray()
bytes3.extend(str)
"""输出
<type 'bytearray'>
你好，Python!
"""
print "type of bytes3 is ", type(bytes3)
print bytes3, "\n\n"


# 将 byte array 转回String
s2 = bytes2.tostring()
"""输出
你好，Python!
"""
print "bytes2.tostring() = ", s2