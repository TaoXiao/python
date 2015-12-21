# -*- encoding: utf-8 -*-
__author__ = 'tao'

from ftpClient import FtpClient

HOST = "fsnrec.com"
USER = "xt"
PASS = "Q592901703q"


# 创建一个FTP实例并登录

# ftp = FtpClient(HOST, USER, PASS)

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

# ftp.downloadDir("/ganlan", "/Users/tao/code")

#print ftpClientUtils.nlist(ftp, "/lims/ArchiveReport/general")


import ftplib
import sys

s = "abcd\nedf"
print s.find("xx")

ftp = FtpClient("fsnrec.com", "xt", "Q592901703q")
# ftp.downloadFile("/lims/LIMS4/BusinessUnits/publish/1/RawRecord/1228/放射性（内照指数）-贵州通用原始记录_1228_1435561478324.pdf", "./")
#ftp.downloadFile("/lims/LIMS4/BusinessUnits/publish/1/RawRecord/1193/环己基氨基磺酸钠（甜蜜素)-色谱分析（单项多样）原始记录_1193_1435561621909.pdf", "./")

"""
try:
    ftp.downloadFile("/lims/LIMS4/BusinessUnits/publish/1/RawRecord/1191/（甜蜜素）以环己基氨基磺\n酸计-色谱分析（单项多样）原始记录_1191_1435561451267.pdf", "./")
except ftplib.error_perm as ex :
    print str(ex)
    print "下载一个正常的文件"
    ftp.downloadFile("/lims/LIMS4/BusinessUnits/publish/1/RawRecord/1193/环己基氨基磺酸钠（甜蜜素)-色谱分析（单项多样）原始记录_1193_1435561621909.pdf", "./")
"""
ftp.close()


