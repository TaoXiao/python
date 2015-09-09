# -*- encoding: utf-8 -*-
__author__ = 'tao'

import sftpClient

sftp = sftpClient.SftpClient("ecs5.njzd.com", "tao", "tao1234")

if sftp.exists("/home/tao/kafka/SimpleAPI-1.0-SNAPSHOT.jar"):
    print "Exists"
else:
    print "Does Not exist"


print sftp.isDirectory("/home/tao/")

#print sftp.isDirectory("/home/tao/platform.xt.sql")

#print sftp.listDir("/home/tao/test/a.txt")
sftp.delete("/home/tao/test")




