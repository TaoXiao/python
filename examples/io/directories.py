__author__ = 'tao'

import os

Dir = "/Users/tao/Desktop/schema"

for dir in os.listdir(Dir):
    print dir
    for file in os.listdir(os.path.join(Dir, dir)):
        print file ,
    print("\n")

print 'drop table "%s" if exists ' % "abc"