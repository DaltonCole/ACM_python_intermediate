# Generators
# More info: http://stackoverflow.com/questions/1756096/understanding-generators-in-python

### Fibonacci Sequence
def fib():
	a, b = 0, 1
	while True:
		yield a # Key part of a generator
		a, b = b, a + b


f = fib()

for i in range(100):
	print(next(f), end=', ')

print('\n\n')

### Prime
import itertools
import math

def is_prime(number):
	if number > 1:
		if number == 2:
			return True
		if number % 2 == 0:
			return False
		for current in range(3, int(math.sqrt(number) + 1), 2):
			if number % current == 0: 
				return False
		return True
	return False

prime = (n for n in itertools.count() if is_prime(n)) # generator expression
# This is similar to List Comprehensions
# prime = [n for n in range(1000) if is_prime(n)]
# print(prime)

for i in range(100):
	print(next(prime), end=', ')
print('\n\n')

### With a return

def with_return():
	i = 0
	while i != 100:
		i += 1
		yield i
	return i

r = with_return()

'''
for i in range(101):
	print(next(r), end=', ')
'''

'''
### Send the generator a value

def get_primes(number):
	print(number)
	while True:
		print(number)
		if is_prime(number):
			number = yield number
		number += 1

p = get_primes(1)

for i in range(100):
	print(next(p), end=', ')

'''