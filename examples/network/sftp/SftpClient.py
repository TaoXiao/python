# -*- encoding: utf-8 -*-
__author__ = 'tao'

import errno
import stat
import os
import socket
import time

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
    def __init__(self, host, user, passwd, port=22):
        Err_socket_gaierror = True  # 失败重试
        while Err_socket_gaierror:
            try:
                self.transport = paramiko.Transport((host, port))
                Err_socket_gaierror = False
            except socket.gaierror as ex:
                print "连接失败 ：%s ： 10秒后重试 ..." % ex
                time.sleep(5)
                Err_socket_gaierror = True

        self.transport.connect(username=user, password=passwd)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)


    """ 传输文件
    src 和 dest 都必须是文件名

    不能实现目录的传输

    传输方向：只能实现从本机向远程机器的文件分发
    """
    def transfer(self, src, dest):
        self.sftp.put(src, dest)


    """ 下载文件/目录
    destPath必须是目录（且已经存在），srcPath可以是文件或者目录
    传输方向：从远程机器下载文件到本地
    """
    def download(self, srcPath, destPath):
        if not os.path.exists(destPath):
            print "Dest path [" + srcPath + "] does NOT exist !"
            return
        if not os.path.isdir(destPath):
            print "Dest path [" + destPath + "] is NOT directory !"
            return
        if not self.exists(srcPath):
            print "Source path [" + srcPath + "] does NOT exist !"
            return

        if not self.isDirectory(srcPath):
            self.sftp.get(srcPath, os.path.join(destPath, os.path.basename(srcPath)))
        else:
            # sftp.listdir(srcPath) 只会返回文件或者目录本身的名字，不会返回全路径名
            for newSrcPath in [os.path.join(srcPath, path) for path in self.sftp.listdir(srcPath)]:
                if self.isDirectory(newSrcPath):
                    newDestPath = os.path.join(destPath, os.path.basename(newSrcPath))
                    os.mkdir(newDestPath)
                    self.download(newSrcPath, newDestPath)
                else:
                    self.download(newSrcPath, destPath)



    """ 删除远程主机上的文件或者目录 """
    def delete(self, path):
        if self.isDirectory(path):
            for f in self.listDir(path):
                self.delete(os.path.join(path, f))
            self.sftp.rmdir(path) # rmdir不能直接删除非空目录
        else:
            self.sftp.remove(path)



    """ 判断 某个文件/目录 是否存在 """
    def exists(self, path):
        try:
            self.sftp.stat(path)
        except IOError, e:
            if e.errno == errno.ENOENT:
                return False
        else:
            return True




    """ 判断是文件还是目录
    返回True表示是目录
    返回False表示是文件
    """
    def isDirectory(self, path):
        lstat = self.sftp.lstat(path)
        if stat.S_ISDIR(lstat.st_mode):
            return True
        else:
            return False





    """ 列出`path`中的文件名/目录名
    这里只会返回basename，不会返回全路径名
    `path`必须是目录
    """
    def listDir(self, path):
        return self.sftp.listdir(path)




    """ 创建一个目录 """
    def mkDir(self, path):
        if self.exists(path):
            raise Exception("目录[%s]已存在" % path)
        self.sftp.mkdir(path)




    """ 创建多级目录
        例如，如果参数path为 "/A/B/C/D"，但是目录"/A/B"并不存在,那么本函数将会创建目录 "/A/B/C/D"
        或者，如果参数path问 "C:\A\B\C\D",但是目录"C:\A\B"并不存在，那么本函数也会创建完整的目录
    """
    def makeDirs(self, path):
        if self.exists(path):
            raise Exception("目录 [%s] 已存在" % path)
        if path.endswith("/") or path.endswith("\\"):
            raise Exception(u"目录路径[%s]不能以字符 \\ 或者 / 结尾" % path)

        pDir  = os.path.dirname(path)  # C:\A  -->  C:\ , 或者 C:\A\B\C  -->  C:\A\B
        ppDir = os.path.dirname(pDir)  # C:\   -->  C:\ , 或者 C:\A\B    -->  C:\A
        if path == pDir :  # path类似于 C:\
            return
        elif pDir == ppDir : # path 类似于 C:\A
            self.mkDir(path)
        else : # path 类似于 C:\A\B
            if not self.exists(pDir) : # 如果 C:\A不存在
                self.makeDirs(pDir) # 则先创建 C:\A
            self.mkDir(path)


    """ 使用完了必须关闭SFTP连接 """
    def close(self):
        self.sftp.close()
        self.transport.close()












