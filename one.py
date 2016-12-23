"""

Problem: Multiples of 3 and 5
URL: https://projecteuler.net/problem=1
Solution author: Samael Olascoaga

"""
result = 0
for i in range(1000):
	if i % 3 == 0 or i % 5 == 0:
		result += i

print(result)
