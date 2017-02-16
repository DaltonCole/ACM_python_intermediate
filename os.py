import os

print(os.name) # posix

print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('./ACM_python_intermediate/')

# Run a command
ls = os.system('ls')
print(ls)

# Subprocess
import subprocess
proc = subprocess.run(['ls', '-al']) # subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False)
print(proc)
proc = subprocess.run(['python', 'bitwise.py'])
print(proc)
proc = subprocess.Popen(['python', 'helper_os.py'], stdin=subprocess.PIPE)
proc.communicate(input=b'This will be printed\n')


# Wild card
import glob
print(glob.glob('*.txt'))

# Regular Expression
import re
r = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(r)

r = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(r)

r = 'I like pie'.replace('pie', '$$$$$') # Or the string way
print(r)

# Statistics
import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

# Internet
from urllib.request import urlopen

html = ''
with urlopen('http://daltonrussellcole.com') as response:
	for line in response:
		html += line.decode('utf-8')

print(html)

# Email
'''
import smtplib
fromaddr = 'darcnessmatters.not@gmail.com'
toaddrs  = 'drcgy5@mst.edu'
msg = "\r\n".join([
  "From: darcnessmatters.not@gmail.com",
  "To: drcgy5@gmst.edu",
  "Subject: Hey cootie",
  "",
  "Meeeeow! I pet a bird today!"
  ])
username = 'darcnessmatters.not@gmail.com'
password = 'FitSammie2016'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
'''

# Date time
from datetime import date
print(date.today())

# Data Compression
import zlib

s = ''
with open('test.txt', 'r') as f:
	s = f.read()

s = s.encode('ascii') # Converts string to binary string. Or we could have done 'rb' above

print("Before compression:", len(s))

t = zlib.compress(s)

print("After  compression:", len(t))

t = zlib.decompress(t)

print("Equal before and after:", s == t)

# timeit, compare speeds between commands
from timeit import Timer
print( Timer('t=a; a=b; b=t', 'a=1; b=2').timeit() )
# 0.045239608007250354
print( Timer('a,b = b,a', 'a=1; b=2').timeit() ) # Unpacking is infact faster! :D
# 0.02434529800666496

# Built in
print(dir()) # Returns list of imported moduels