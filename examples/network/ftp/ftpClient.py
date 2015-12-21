# -*- encoding: utf-8 -*-
__author__ = 'tao'

from ftplib import FTP
from ftplib import error_perm
import os
import sys

"""
使用FTP来传数据必须要有FTP Server和FTP Client
FTP Server在CentOS上是默认不运行的，需要自己安装运行
FTP默认的端口是21


由于SFTP是SSH的一部分（与传统的FTP没有任何关系）
因此配置SFTP不需要传统的FTP服务器软件
SFTP的默认端口是22

主动模式：active mode
"""

class FtpClient:
    def __init__(self, host, user, passwd):
        self.ftp = FTP(host)
        self.ftp.login(user, passwd)


    """将FTP服务器上的文件下载到本地指定的路径
    不能改变文件的名字
    remoteFile必须是·文件名·
    localDir必须是·目录名·，且已存在
    """
    def downloadFile(self, remoteFile, localDir, localFileName=None):
        if os.path.exists(localDir) and not os.path.isdir(localDir):
            sys.stderr.write("Local path [" + localDir + "] is NOT directory.")
            return
        if not os.path.exists(localDir):
            sys.stderr.write("Local path [" + localDir + "] does NOT exist.")
            return
        if not os.path.isdir(localDir):
            sys.stderr.write("Local path [" + localDir + "] is NOT directory.")
            return
        if not self.exists(remoteFile):
            sys.stderr.write("Remote path [" + remoteFile + "] does NOT exist.")
            return
        if self.isDir(remoteFile):
            sys.stderr.write("Remote path [" + remoteFile + "] is NOT regular file.")
            return

        if None == localFileName:
            localFile = os.path.join(localDir, os.path.basename(remoteFile))
        else:
            localFile = os.path.join(localDir, localFileName)

        with open(localFile, 'wb') as f:
            try :
                self.ftp.retrbinary('RETR ' + remoteFile, f.write)
            except :
                sys.stderr.write("\n[ERROR]: FTP文件路径为 %s, 本地目标目录为 %s \n" %(remoteFile, localDir))
                raise




    """ 下载整个目录到本地
    remotePath必须是·目录名·，且已存在
    localPath必须是·目录名·，且已存在
    """
    def downloadDir(self, remoteDir, localDir):
        if os.path.exists(localDir) and not os.path.isdir(localDir):
            print "Error: Local path [" + localDir + "] is NOT directory."
            return
        if not os.path.exists(localDir):
            print "Error: Local path [" + localDir + "] does NOT exist."
            return
        if not os.path.isdir(localDir):
            print "Error: Local path [" + localDir + "] is NOT directory."
            return
        if not self.exists(remoteDir):
            print "Error: Remote path [" + remoteDir + "] does NOT exist."
            return
        if not self.isDir(remoteDir):
            print "Error: Remote path [" + remoteDir + "] is NOT directory."
            return

        L = self.nlist(remoteDir)

        # 根目录要特别对待
        if remoteDir != "/":
            newLocalDir = os.path.join(localDir, os.path.basename(remoteDir))
            os.mkdir(newLocalDir)
        else:
            newLocalDir = localDir

        for f in L:
            if not self.isDir(f):
                self.downloadFile(f, newLocalDir)
            else:
                self.downloadDir(f, newLocalDir)





    """ 返回NLIST的结果（只返回每一个文件/目录的全路径）
    结果放在一个list中返回
    """
    def nlist(self, path):
        L = []
        def callback(line):
            L.append(line)

        self.ftp.retrlines("NLST " + path, callback)
        return L




    """测试一个文件/目录是否存在
    """
    def exists(self, path):
        try:
            self.ftp.size(path)
        except error_perm: # 这里，可能path不存在，或者是文件
            try:
                self.ftp.cwd(path)
            except error_perm: # 现在，path肯定就是不存在了
                return False
        return True # 通过了以上的测试，path肯定是存在了






    """判断path是不是目录
    原理：试图利用cwd进入该path，如果是目录则可以进入；
         否则，会抛出异常
    """
    def isDir(self, path):
        try:
            self.ftp.cwd(path)
        except error_perm:
            return False
        return True



    """ 释放资源 """
    def close(self):
        self.ftp.close()
