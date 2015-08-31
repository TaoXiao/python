# -*- encoding: utf-8 -*-
__author__ = 'tao'


"""
[Good logging practice in Python](http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python)
"""

import sys
import logging

from configLogging import setup_logging

def main(args):
    setup_logging() # 采用YAML中的默认配置

    """ 在YAML配置文件中没有`unspecified`这个logger,
    所以自动匹配到root中名为`console_handler`的handler。
    Console的输出为
        [2015-08-28 17:11:59,579] - [unspecified] - [INFO] :   INFO....
    """
    unspecified_logger = logging.getLogger('unspecified')
    unspecified_logger.debug("DEBUG....")
    unspecified_logger.info("INFO....")

    print "---------------------------------------------------------"


    """ rotatingFileLogger在YAML文件中能找到，因此会写入到对应的文件中
    warn.log的内容为
        [2015-08-28 17:15:28,001] - [rotatingFileLogger] - [WARNING] :   WARN+++
        [2015-08-28 17:15:28,001] - [rotatingFileLogger] - [ERROR] :   ERROR+++
        [2015-08-28 17:15:28,001] - [rotatingFileLogger] - [CRITICAL] :   CRITICAL+++
    """
    file_logger = logging.getLogger('rotatingFileLogger')
    file_logger.debug("DEBUG +++")
    file_logger.info("INFO+++")
    file_logger.warn("WARN+++")
    file_logger.error("ERROR+++")
    file_logger.critical("CRITICAL+++")


    print "---------------------------------------------------------"

    """ 在YAML中为日志文件配置了最大size和数量，会自动生成最多(5+1)个日志文件，如下
    warn.log
    warn.log.1
    warn.log.2
    warn.log.3
    warn.log.4
    warn.log.5
    """
    for  i in range(10000):
        file_logger.debug("DEBUG +++")
        file_logger.info("INFO+++")
        file_logger.warn("WARN+++")
        file_logger.error("ERROR+++")
        file_logger.critical("CRITICAL+++")


    print "---------------------------------------------------------"


    """一个logger同时向两个地方输出：
        将ERROR以上级别的日志输出在CONSOLE,
        同时将WARN以上的日志输出在文件中
    """
    file_logger = logging.getLogger('doubleLogger')
    file_logger.debug("DEBUG ***")
    file_logger.info("INFO ***")
    file_logger.warn("WARN ***")
    file_logger.error("ERROR ***")
    file_logger.critical("CRITICAL ***")



if __name__ == "__main__":
    main(sys.argv)