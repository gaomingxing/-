    #!/usr/bin/python
# -*- coding: utf-8 -*-

# 函数

print pow(2,3)  # 取谁的几次方
print abs(-1)  # 取绝对值
print round(4.5)  # 四舍五入
print float("44")  # 取浮点数
print int(44.0)  # 取整型
long(44)  # 取长整型（交互式环境显示L）


import math
from math import sqrt
print math.floor(4.9)  # 向下取整（浮点型）
print math.ceil(4.1)  # 向上取整（浮点型 ）
print sqrt(9)  # 取平方根

import cmath
print cmath.sqrt(-4)  # 取负数的平方根（虚数）
print cmath.sqrt(4)  # 取正数的平方根（复数）


print r"hello \nworld"  # 不能在原始字符串结尾输入反斜线
print u"hello world"
print "hello world"

