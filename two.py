"""

Problem: Even Fibonacci numbers
URL: https://projecteuler.net/problem=2
Solution author: Samael Olascoaga

"""
def fib(maxima):
	x = 1
	y = 0
	n = []
	for i in range(maxima):
		x, y = y, x + y
		if y < maxima:
			n.append(y)
		else:
			break
	sumatorio = 0
	for i in n:
		if i % 2 == 0:
			sumatorio += i
	print (sumatorio)