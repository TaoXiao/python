# -*- encoding: utf-8 -*-
__author__ = 'tao'

import codecs
import sys



""" 读取UTF-8编码的文件
    关于Unicode和UTF-8，请阅读：https://docs.python.org/2/howto/unicode.html
"""
def readUTF8File(path):
    f = codecs.open(path, encoding='utf-8', errors='strict')
    for line in f:
        print repr(line)




""" 读取一个UTF-8编码的文件
    一行一行地读，但是换行符可以指定特殊的字符，不一定是`\r`, `\n`, 或者`\r\n`

    对于两个连续的分隔符，不会输出空值(已经过滤掉了)

    本函数的实现： 将指定的文件中的内容，按照设定的分隔符，切分后放入List中返回
    注意：返回的结果中不含None
"""
def readLinesBySep(path, separator, size=100):
    f = codecs.open(path, encoding='utf-8', errors='strict')
    partialLine = ''

    while True:
        charsJustRead = f.read(size)
        if not charsJustRead:
            break

        partialLine += charsJustRead
        lines = partialLine.split(separator)
        partialLine = lines.pop()

        for line in lines:
            if line:
                yield line

    yield partialLine



""" 用法：
   reader = ReadingFileUtils("data.utf8", "|")

   while True:
       line = reader.nextLine()
       if None == line:
           break
       else:
           print line

    reader.close()
"""
class ReadingFileUtils:
    import codecs

    def __init__(self, path, sep, encoding='utf-8', size=200):
            self.f = codecs.open(path, encoding=encoding, errors='strict')
            self.separator = sep
            self.partialLine = ''
            self.size = size
            self.tokens = []


    """ 从文件中读取下一行（以指定的分隔符来决定换行）
        如果已经读完了，则返回None
    """
    def nextLine(self):
        if len(self.tokens) > 0:
            return self.tokens.pop(0)

        while True:
            charsJustRead = self.f.read(self.size)
            if not charsJustRead:
                break

            self.partialLine += charsJustRead
            lines = self.partialLine.split(self.separator)
            self.partialLine = lines.pop()

            for line in lines:
                if line:
                    self.tokens.append(line)

            if len(self.tokens) > 0:
                return self.tokens.pop(0)

        if self.partialLine:
            tmp = self.partialLine
            self.partialLine = None
            return tmp
        else:
            return None


    def close(self):
        self.f.close()






def main(args):
    pass



if __name__ == '__main__':
    main(sys.argv)