# Documentation

# SHA256
print("SHA256")
from Crypto.Hash import SHA256

hash = SHA256.new()
hash.update(b'My name is Dalton')
dig = hash.digest()

print(dig)

# MD5
print("MD5")
from Crypto.Hash import MD5

h = MD5.new()
h.update(b'This is an md5 hash after being hashed')
print(h.hexdigest())

# AES
print("AES")
from Crypto.Cipher import AES

obj = AES.new('key, the best key, FitSammie2016', AES.MODE_ECB, 'IV, James IV 16b') # IV is 16 bytes long
message = "Dalton Cole says he is 5 foot eight inches, but he is really 5 foot 7.75 inches." # Message is a multiple of 16 bytes
ciphertext = obj.encrypt(message)

print(ciphertext) # Ha ha, now no one will know my secret

obj2 = AES.new('key, the best key, FitSammie2016', AES.MODE_CBC, 'IV, James IV 16b') # ;)
print(obj2.decrypt(ciphertext))

'''
MODE_ECB = 1
Electronic Code Book (ECB). See blockalgo.MODE_ECB.
 	MODE_CBC = 2
Cipher-Block Chaining (CBC). See blockalgo.MODE_CBC.
 	MODE_CFB = 3
Cipher FeedBack (CFB). See blockalgo.MODE_CFB.
 	MODE_PGP = 4
This mode should not be used.
 	MODE_OFB = 5
Output FeedBack (OFB). See blockalgo.MODE_OFB.
 	MODE_CTR = 6
CounTer Mode (CTR). See blockalgo.MODE_CTR.
 	MODE_OPENPGP = 7
OpenPGP Mode. See blockalgo.MODE_OPENPGP.
 	block_size = 16
Size of a data block (in bytes)
 	key_size = (16, 24, 32)
 '''


 # RSA
print("RSA")

import rsa

key_size = 1024

(bob_pub, bob_priv) = rsa.newkeys(key_size)
text = b"PIZZZZZZZZZZZZZZZzzzzzZZZzza"
e = rsa.encrypt(text, bob_pub)
print(e)

d = rsa.decrypt(e, bob_priv)
print(d)

# Random (crypto secure)
print("Random")
from Crypto.Random.random import randint

print(randint(0,100))

# String XOR
print("String XOR")
from   Crypto.Util.strxor import strxor

print(strxor(b'hii', b'bye'))
