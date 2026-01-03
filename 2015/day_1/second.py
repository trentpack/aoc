#!/bin/python3
import sys

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  c = None
  left = 0
  right = 0
  num = 0
  found_basement = False
  while c := f.read(1):
    if not c:
      break
    #print("I read ", c)
    if c == '(':
      left = left + 1
    elif c == ')':
      right = right + 1
    else:
      print("Bad character? ", c)
    num = num + 1
    if (left-right) < 0 and found_basement == False:
      print(f"Basement at pos %", num)
      found_basement = True
  print (f"End's on floor %", (left-right))
