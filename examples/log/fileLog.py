# -*- encoding: utf-8 -*-

__author__ = 'tao'


"""
将Log输出到指定的文件中
"""


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

fileLogHandler = logging.FileHandler("hi.log")
fileLogHandler.setLevel(logging.WARN)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileLogHandler.setFormatter(formatter)

logger.addHandler(fileLogHandler)
# log只会输出到文件中，且INFO级别的log不会输出
logger.info("This is info")
logger.warn("This is warn")
logger.error("This is error")
logger.critical("This is critical")


"""上面代码输出
2015-08-27 16:35:13,589 - __main__ - WARNING - This is warn
2015-08-27 16:35:13,589 - __main__ - ERROR - This is error
2015-08-27 16:35:13,589 - __main__ - CRITICAL - This is critical
"""
