# -*- encoding: utf-8 -*-
__author__ = 'tao'

from ftplib import FTP

"""
使用FTP来传数据必须要有FTP Server和FTP Client
FTP Server在CentOS上是默认不运行的，需要自己安装运行
FTP默认的端口是21


由于SFTP是SSH的一部分（与传统的FTP没有任何关系），
因此配置SFTP不需要传统的FTP服务器软件，仅需要OpenSSH服务器即可
SFTP的默认端口是22


如果不想安装FTP Server，那么可以直接利用SFTP来传文件，
这样，只要写一个SFTP Client即可
"""
