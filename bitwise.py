x = 5 	# 0000 0101
y = 12 	# 0000 1100 

# Left bit shift
print(x << 2) 	# 20

# Right bit shift
print(y >> 2)	# 3

# AND
print(x & y)	# 4

# OR
print(x | y)	# 13

# Complement
print(~x)		# -6 = -x - 1

# XOR
print(x ^ y)	# 9