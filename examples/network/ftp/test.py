# -*- encoding: utf-8 -*-
__author__ = 'tao'

from ftpClient import FtpClient

HOST = "fsnrec.com"
USER = "xt"
PASS = "Q592901703q"


# 创建一个FTP实例并登录

ftp = FtpClient(HOST, USER, PASS)

# 获取预设的欢迎消息
# 220 (vsFTPd 2.2.2)
#print ftp.getwelcome()

# 进入目录『/0calibration』
#ftp.cwd("/0calibration")

# 列出该目录下的所有内容，以行的形式输出
#ftp.retrlines('LIST LH004.pdf')

#ftp.nlst()

# print ftpClientUtils.isDirectory(ftp, "/0calibration")

# print ftpClientUtils.checkExisting(ftp, "/0calibratio")

#ftpClientUtils.downloadFile(ftp, "/0calibration/LH004.pdf", "/Users/tao/Downloads/ftp/LH004.pdf")

#print ftpClientUtils.checkFileExists(ftp, "/lims/ArchiveReport/general/FZ20137001.pdf")

# ftpClientUtils.listOneFile(ftp, "/lims/ArchiveReport/general")

ftp.downloadDir("/ganlan", "/Users/tao/code")

#print ftpClientUtils.nlist(ftp, "/lims/ArchiveReport/general")

