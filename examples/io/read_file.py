# -*- encoding:utf-8 -*-

import sys
import codecs



"""
读取普通编码的文件
按行读
"""
def readRegularFile(path):
    with open(path) as f:
        for line in f.readlines():
            print line



def main(args):
    readRegularFile(args[1])

if __name__ == "__main__":
    main(sys.argv)

