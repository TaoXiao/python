# -*- coding:utf-8 -*- 

# 列表生成式

L1 = [x*x for x in range(10)]
print L1  # 输出 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print type(L1)  # 输出 <type 'list'>

print '-----------  带循环条件  -----------'
L2 = [x*x for x in range(10) if x % 2 == 0]
print L2 # 输出 [0, 4, 16, 36, 64]

print '-----------  多层循环  -----------'
L3 = [m+n for m in 'ABC' for n in '123']
print L3 # 输出 ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# 应用

print '-----------  求出当前目录下全部的文件和目录  -----------'
import os
F = os.listdir(".")
print type(F) # 输出 <type 'list'>
print F       # 输出 ['iteration.py', 'listComprehension.py', 'slice.py']


print '-----------  迭代读取字典中的key-value pair -----------'
d = {'A':'a', 'B':'b', 'C':'c', 'D':'d'}
L4 = [key + " = " + value  for key, value in d.iteritems()]
print L4


print '----------- 将所有字符串整体转换为大写  -----------'
ls = ['hello', 'world', 100, 'hi', 200, 'python']
lg = [s.upper() for s in ls if isinstance(s, str)]
print lg


