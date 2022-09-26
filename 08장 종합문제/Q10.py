# 사칙연산 계산기

import numbers


class Calculator:
	def __init__(self, numbers):
		self.numbers = numbers
	def sum(self):
		result = 0
		for i in self.numbers:
			result += i
		return result
	def avg(self):
		for i in self.numbers:
			result = self.sum() / len(self.numbers)
		return result

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())