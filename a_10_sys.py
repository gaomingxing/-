#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
sys的用法:

使用sys模块获得脚本的参数、处理模块、使用sys模块操作模块搜索路径、使用sys模块查找内建模块、使用sys模块查找已导入的模块等使用案例
'''
import sys

------------------------------------------------------------------------------------------------------
# 处理命令行参数
'''
在解释器启动后, argv 列表包含了传递给脚本的所有参数, 列表的第一个元素为脚本自身的名称.
'''

print "script name is", sys.argv[0]        # 使用sys.argv[0]采集脚本名称

if len(sys.argv) > 1:
    print "there are", len(sys.argv)-1, "arguments:"  # 使用len(sys.argv)-1采集参数个数-1为减去[0]脚本名称
    for arg in sys.argv[1:]:            #输出除了[0]外所有参数
        print arg
else:
    print "there are no arguments!"


------------------------------------------------------------------------------------------------------
# 使用sys模块查找内建模块
'''
builtin_module_names 列表包含 Python 解释器中所有内建模块的名称
'''
def dump(module):
    print module, "=>",
    if module in sys.builtin_module_names:  #查找内建模块是否存在
        print "<BUILTIN>"
    else:
        module = __import__(module)         #非内建模块输出模块路径
        print module.__file__
dump("os")
dump("sys")
dump("string")
dump("strop")
dump("zlib")


------------------------------------------------------------------------------------------------------
# 使用sys模块查找已导入的模块
'''
modules 字典包含所有加载的模块. import 语句在从磁盘导入内容之前会先检查这个字典.
Python 在处理你的脚本之前就已经导入了很多模块.
'''
print sys.modules.keys()


------------------------------------------------------------------------------------------------------
# 查找平台系统
'''
sys.platform
大家都知道，当今的程序比较流行的是跨平台。简单的说就是这段程序既可以在windows下，换到linux下也可以不加修改的运行起来，听起来就不错。所以，这个函数就可以派上用场了。
假设，我们想实现一个清除终端，linux下用clear, windows下用cls
'''
Ostype = sys.platform()
if ostype == "linux" or ostype == "linux2":
	Cmd = "clear"
else:
	Cmd = "cls"



