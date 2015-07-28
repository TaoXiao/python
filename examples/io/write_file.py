#!/usr/bin/env python
# -*- coding:utf-8 *-*

# 『-*- coding:utf-8 *-*』表示本源文件的编码是UTF-8
# u'xxx'则表示'xxx'用UTF-8编码
print u'## 请出输入你想创建的文件名:'
filename = raw_input()  # 这里即使用户键入的是中文也是可以的

# 创建并打开要写的文件
with open(filename, 'w') as f:
	for x in range(10000000): # 一千万条数据
		num = '%0.7d'%x
		f.write(num + ',c0-' + num + ',c1-' + num + ',c2-' + num + ',c3-' + num + ',c4-' + num + ',c5-' + num + ',c6-' + num + ',c7-' + num + ',c8-' + num + ',c9-' + num  +'\n')

print 'finished!'
