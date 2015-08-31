# -*- encoding: utf-8 -*-
__author__ = 'tao'

import foo

print "-------- after `import foo` --------"

foo.main()



"""用 `python -m mainFunction.bar` 执行后，输出如下：

Outside main(), __name__ ==  mainFunction.foo
-------- after `import foo` --------
In main(), __name__ ==  mainFunction.foo


说明：对于不在任何函数中的语句，当import某个python文件时，就会执行它们
"""


