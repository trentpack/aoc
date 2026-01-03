#!/bin/python3
import sys

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  c = None
  left = 0
  right = 0
  while c := f.read(1):
    if not c:
      break
    print("I read ", c)
    if c == '(':
      left = left + 1
    elif c == ')':
      right = right + 1
    else:
      print("Bad character? ", c)
  print (f"Floor %", (left-right))
