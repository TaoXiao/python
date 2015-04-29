# -*- coding:utf-8 -*-

d = {"name":"xiao", "gender":"male", "age":"30", "name":"tao"}
# "name"的值为"tao"
print d # 输出 {'gender': 'male', 'age': '30', 'name': 'tao'}
print d['name'] # 输出tao

print '---------------------'

d['city'] = 'NJ'
print d['city']     # 输出NJ 
#print d['province'] # 异常

print '---------------------'

# 测试某个key是否存在
print d.get('province') # 输出 None
print d.get('province', 'does not exist') # 输出does not exist
if ('province' in d):   # 输出 NO
	print 'YES'
else:
	print 'NO'


print '---------------------'

# 删除某个key-value pair
x = d.pop('city')
print x  # 输出NJ
print d  # 输出{'gender': 'male', 'age': '30', 'name': 'tao'}

# 查看字典中的kv的数量
print len(d) # 输出3

print '---------------------'

# 字典允许存储不同类型的key
d1 = {'A': 'A00', "a" : 'a100', 100:888, 200:999}
print d1 # {'A': 'A00', 'a': 'a100', 100: 888, 200: 999}

