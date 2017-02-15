class A:
	def __init__(self, a):
		self.variable = a

	def print_a(self):
		print("This is a's print function")

class B:
	def __init__(self, b):
		self.variable = 10

	def print_b(self):
		print("This is b's")

class C(A, B):
	def print_c(self):
		print("This is c's")

class D(B, A):
	pass

a = A(5)

b = B(2)

c = C(5)

d = D(2)

c.print_a()
c.print_b()
c.print_c()

print("c.variable:", c.variable)

print("d.variable:", d.variable)
