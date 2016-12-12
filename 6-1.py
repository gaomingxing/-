#!/usr/bin/python
# -*- coding: utf-8 -*-

# 阶乘递归
def test1(n):
	if n == 1:
		return 1
	else:
		return n * test1(n-1)

# 幂递归
def test2(x, n):
	if n == 0:
		return 1
	else:
		return x * test2(x, n-1)

# 二元查找递归
def search(sequence, number, lower=0, upper=None):
	if upper is None: upper = len(sequence)-1
	if lower == upper:
		assert number == sequence[upper]
		print "成功找到"
		return upper
	else:
		middle = (lower + upper) // 2
		if number > sequence[middle]:
			return search(sequence, number, middle+1, upper)
		else:
			return search(sequence, number, lower, middle)

if __name__ == "__main__":
	# print test1(4);
	# print test2(2, 4);
	print search([4,8,34,67,95,100,123], 100);
