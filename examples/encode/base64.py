# -*- coding:utf-8 -*-

import base64

"""
base64可以对字符串编码
也可以对Byte Array进行编码
"""

# String 与 base64 的转换
s = "你好， base64"
b = base64.b64encode(s)

print b
print base64.b64decode(b) , "\n\n"




# byte array 与 base64 的转换
A = bytearray()
A.extend(s)
"""输出
type of `A` is  <type 'bytearray'>
`A`中的内容是 [228, 189, 160, 229, 165, 189, 239, 188, 140, 32, 98, 97, 115, 101, 54, 52]
"""
print "type of `A` is ", type(A)
print "`A`中的内容是",  [b for b in A] , "\n\n"





# 将 byte array 中的二进制字节数组用base64编码
encodedA = base64.b64encode(A)
"""输出
type of `encodedA` is  <type 'str'>
`encodedA`中的内容是 ['5', 'L', '2', 'g', '5', 'a', 'W', '9', '7', '7', 'y', 'M', 'I', 'G', 'J', 'h', 'c', '2', 'U', '2', 'N', 'A', '=', '=']
"""
print "type of `encodedA` is ", type(encodedA)
print "`encodedA`中的内容是", [b for b in encodedA], "\n\n"





# 将base64编码后的内容转回二进制的byte array
decodedA = base64.b64decode(encodedA)
"""输出
type of `decodedA` is  <type 'str'>
`decodedA`中的内容是 ['\xe4', '\xbd', '\xa0', '\xe5', '\xa5', '\xbd', '\xef', '\xbc', '\x8c', ' ', 'b', 'a', 's', 'e', '6', '4']
"""
print "type of `decodedA` is ", type(decodedA)
print "`decodedA`中的内容是", [b for b in decodedA]
