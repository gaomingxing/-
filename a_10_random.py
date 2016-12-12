#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

# print random.random()  # 用于生成一个0到1的随机符点数;范围[0, 1)

# print random.uniform(10, 20)  # random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限
# print random.uniform(20, 10)

# print random.randint(10, 15)  # random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
#                               # printrandom.randint(20,10)#该语句是错误的。下限必须小于上限。

# print random.randrange(10, 100, 2)  # random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数
# print random.choice(xrange(10, 100, 2))  # random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效

# print random.choice("gaomingxing")  # random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence),list, tuple, 字符串都属于sequence

list_test = list("123456789")  
# random.shuffle(list_test)  # 用于将一个列表中的元素打乱,原序列发生改变
# print list_test

aa = random.sample(list_test, len(list_test))  # random.sample(sequence, k)，从指定序列中随机获取k个元素，作为一个片断返回。sample函数不会修改原有序列
print aa
print "".join(aa)
print list_test