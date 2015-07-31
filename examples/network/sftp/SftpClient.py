# -*- encoding: utf-8 -*-
__author__ = 'tao'

import errno

'''
使用SFTP的好处：
1. SFTP是SSH的一部分（与传统的FTP没有任何关系），因此使用SFTP不需要传统的FTP Server
2. 更安全


在windows上安装paramiko要麻烦一些，参考
1. http://linux5588.blog.51cto.com/65280/1275180
2. http://www.cnblogs.com/zhuyp1015/archive/2012/07/17/2596495.html
3. http://paramiko-www.readthedocs.org/en/latest/installing.html#pypm
4. https://pypi.python.org/pypi/setuptools#downloads
'''
import paramiko



"""  用法
    host = "some.host.com"
    port = 22
    user = "xxx"
    passwd = "xxx"

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


    """ 判断 某个文件/目录 是否存在 """
    def exists(self, path):
        try:
            self.sftp.stat(path)
        except IOError, e:
            if e.errno == errno.ENOENT:
                return False
        else:
            return True

    """ 使用完了必须关闭SFTP连接 """
    def close(self):
        self.sftp.close()
        self.transport.close()












