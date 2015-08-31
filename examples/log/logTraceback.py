__author__ = 'tao'

import logging
import sys

print 'Current directory :', __package__
print 'Current module : ', __name__

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler("xt.log")
fileHandler.setLevel(logging.WARN)

logger.addHandler(fileHandler)

def main(argv):
    for a in argv:
        print a
    try:
        print 'Trying to open a file ...'
        open(argv[1])
    except Exception:
        logger.error('Failed to open file', exc_info=True)


if __name__ == "__main__":
    main(sys.argv)


""" xt.log文件中会输出

Traceback (most recent call last):
  File "/Users/tao/IdeaProjects/Python/examples/log/logTraceback.py", line 22, in main
    open(argv[1])
IOError: [Errno 2] No such file or directory: '100'

说明： By calling logger method with `exc_info = True`, traceback is
dumped to the logger.
"""