# -*- encoding: utf-8 -*-
__author__ = 'tao'

import sftpClient

sftp = sftpClient.SftpClient("ecs5.njzd.com", 22, "tao", "tao1234")

if sftp.exists("/home/tao/kafka/SimpleAPI-1.0-SNAPSHOT.jar"):
    print "Exists"
else:
    print "Does Not exist"

