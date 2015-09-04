# -*- encoding: utf-8 -*-
__author__ = 'tao'

from ftplib import FTP

"""
使用FTP来传数据必须要有FTP Server和FTP Client
FTP Server在CentOS上是默认不运行的，需要自己安装运行
FTP默认的端口是21


由于SFTP是SSH的一部分（与传统的FTP没有任何关系）
因此配置SFTP不需要传统的FTP服务器软件
SFTP的默认端口是22

主动模式：active mode
"""

"""将FTP服务器上的文件下载到本地指定的路径
"""
def downloadFile(ftp, remotePath, localPath):
    localfile = open(localPath, 'wb')
    ftp.retrbinary('RETR ' + remotePath, localfile.write)
    localfile.close()


