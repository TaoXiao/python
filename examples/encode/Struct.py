__author__ = 'tao'

import struct


def encodeInt(n):
    return struct.pack("i", n)


str =  encodeInt(12)

print [x for x in str]



