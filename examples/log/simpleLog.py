# -*- encoding: utf-8 -*-

__author__ = 'tao'


import logging
import sys

from configLogging import setup_logging

def main(args):
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    logger.info("start to log")
    logger.debug("This is debug")
    logger.warn("This is WARN")
    logger.error("This is ERROR")
    logger.critical("This is critical")


    setup_logging()

    file_logger = logging.getLogger('rotatingFileLogger')
    file_logger.debug("DEBUG from [simpleLog.py]")
    file_logger.info("INFO from [simpleLog.py]")
    file_logger.warn("WARN from [simpleLog.py]")
    file_logger.error("ERROR from [simpleLog.py]")
    file_logger.critical("CRITICAL from [simpleLog.py]")


if __name__ == "__main__":
    main(sys.argv)






