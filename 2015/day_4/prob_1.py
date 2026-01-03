#!/bin/python3
import sys
import hashlib

# s = "abcdef609043"
# res = hashlib.md5(s.encode())
# print("Bits: ", res.digest())
# print("Digest: ", res.hexdigest())

# result = res.digest()

# if result[0] == 0 and result[1] == 0 and result[2] & 0xF0 == 0:
#     print ("Yay!")


with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  line = None
  total = 0
  line = f.readline()
  #for line in f:
  print(f"Input: {line}")
  n = 1
  while n < 10489710000:
    s = line + str(n)
    # print (f"String: {s}")
    res = hashlib.md5(s.encode())
    # print("Bits: ", res.digest())
    # print("Digest: ", res.hexdigest())
    result = res.digest()
    if result[0] == 0 and result[1] == 0 and result[2] & 0xF0 == 0:
        print ("Yay!")
        print (f"Number: {n}")
    n += 1

