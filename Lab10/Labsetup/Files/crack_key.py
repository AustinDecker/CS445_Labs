#!/usr/bin/python3
from sys import argv
from Crypto.Util import Padding
from Crypto.Cipher import AES

MAX_CHARS = 21

_, first, second, third = argv

if len(argv) != 4:
	print("ERROR: Not Enough Arguments")
	exit(-1)

if len(first) > MAX_CHARS:
	print(f"ERROR: plaintext exceeds {MAX_CHARS} characters")
	exit(-2)
	
data = bytearray(first, encoding='utf-8')
ciphertext = bytearray.fromhex(second)
iv = bytearray.fromhex(third)

with open('./words.txt') as f:
    keys = f.readlines()

for k in keys:
    k = k.rstrip('\n')
    if len(k) <= 16:
        key = k + '#'*(16-len(k))
        cipher = AES.new(key=bytearray(key,encoding='utf-8'), mode=AES.MODE_CBC, iv=iv)
        guess = cipher.encrypt(Padding.pad(data, 16))
        if guess == ciphertext:
            print("find the key:",key)
            exit(0)

print("cannot find the key!")
