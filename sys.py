import sys

print(sys.argv) # input arguments, VERY USEFUL

print(sys.base_exec_prefix)

print(sys.base_prefix)

print(sys.copyright) # Python interpreter copyright

print(sys.executable) # Prints path to python binary executable

# sys.exit() # Exits 

print(sys.flags)

print(sys.float_info) # max / min num info

###############################
print(sys.getallocatedblocks()) # See memory blocks currently allocated. Good for debugging memory leaks

t = []
for i in range(100000):
	t.append(i)

print(sys.getallocatedblocks())
###############################

print(sys.getdefaultencoding()) # Deafult string encoding (utf-8)

print(sys.getsizeof(float)) # Size of object in bytes

print(sys.hash_info)

print(sys.int_info) # Holds info about interpreters internal representation of int

print(sys.maxsize) # Max int for type Py_ssize_t

print(sys.path) # Search path for modules

print(sys.platform) # Platform Identifier

print(sys.thread_info)

print(sys.version) # Interpreter and compile version

