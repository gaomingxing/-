#!/usr/bin/python
# -*- coding: utf-8 -*-

# 子类的构造方法必须调用其超累的构造方法来确保进行基本的初始化，有如下两个方法：
# 1.调用超类的未绑定版本  用法：超类.__init__(self, ...)
# 2.使用super函数  用法: super(子类, self).__init__()

# 内建函数iter可以从可迭代的对象中获得迭代器  it = iter([1,2,3])

# 创建生成器
def flatten(nested):  # 任何包含yield语句的函数成为生成器   生成器是一种用普通的函数语法定义的迭代器
	for sublist in nested:
		for element in sublist:
			yield element

nested = [[1,2],[3,4],[5]]
for i in flatten(nested):
	print i

# g = (i for i in range(10))  和  sum(i for i in range(10))  # 循环生成器

def flatten(nested):  # 递归生成器(模板 )
    try:
    	try: 
            nested + ""
        except TypeError:
            pass
        else:
        	raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except Exception, e:
            yield nested

nested = [[[1],2],3,40,[5,[6,7]],8]
nested = [[[1],2],3,40,"iii",[5,[6,7]],8]
for i in flatten(nested):
	print i,