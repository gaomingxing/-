#!/usr/bin/python
# -*- coding: utf-8 -*-

# reload(模块名)  # 可以重新导入模块

def hello():
	print "hello world!"

def test():
	hello()

if __name__ == "__main__":  # 而在导入模块中，这个值就被设定为模块的名字（model_test.__name__）
	hello()