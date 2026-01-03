#!/bin/python3
import sys

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  x = 0
  y = 0
  pres_map = {}
  pres_map[f"{x},{y}"] = 1
  while c := f.read(1):
    if not c:
      break
    if c == '<':
      y -= 1
    elif c == '>':
      y += 1
    elif c == '^':
      x += 1
    elif c == 'v':
      x -= 1
    else:
      print(f"Bad Char? {c}")
    print (f"Position: {x},{y}")
    pres_map[f"{x},{y}"] = 1

  print (f"Total: {len(pres_map.keys())}")