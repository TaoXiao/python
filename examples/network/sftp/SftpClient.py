# -*- encoding: utf-8 -*-
__author__ = 'tao'

import paramiko



"""  用法
    host = "ecs5.njzd.com"
    port = 22
    user = "root"
    passwd = "Root1234NJ"

    # 本地文件名
    localFilePath  = "/Users/tao/IdeaProjects/guizhou_food_security/bigdata/target/bigdata-1.0-SNAPSHOT.jar"
    # 远程目标文件名，必须是文件名
    remoteFilePath = "/bigdata-1.0-SNAPSHOT.jar.bak"


    # 传一个文件
    client = SftpClient(host, port, user, passwd)
    client.transfer(localFilePath, remoteFilePath)
    client.close()
"""



class SftpClient:
    def __init__(self, host, port, user, passwd):
        self.transport = paramiko.Transport((host, port))
        self.transport.connect(username=user, password=passwd)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    """ `paramiko` 不直接支持传输目录，需要自己实现 """
    def transfer(self, localPath, remotePath):
        self.sftp.put(localPath, remotePath)

    def close(self):
        self.sftp.close()
        self.transport.close()














