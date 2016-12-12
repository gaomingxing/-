#!/usr/bin/python
# -*- coding: utf-8 -*-

list_1 = list("123456789")
list_2 = list("abcdefghi")
print zip(list_1,list_2)  # （并行迭代）当最短的序列“用完”的时候就会停止

map(func, seq)  # 对序列中的每个元素应用函数
filter(func, seq)  # 返回其函数为真的元素的列表
reduce(func, seq)  # 等同于func(func(func(seq[0], seq[1]), seq[2]), ...)