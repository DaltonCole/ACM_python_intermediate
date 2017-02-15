import threading
import time
from random import randrange

def num_count(i):
	for num in range(5):
		t = randrange(3)
		print("Thread", i, ":", num, "stoping for", t, "seconds")
		time.sleep(t)

threads = []
# Create 5 threads
for i in range(5):
	t = threading.Thread(target=num_count, args=(i,))
	threads.append(t)
	t.start()
