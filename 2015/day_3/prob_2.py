#!/bin/python3
import sys

def set_pos(dir, x, y):
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
  return x, y

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  x = 0
  y = 0
  pres_map = {}
  pres_map[f"{x},{y}"] = 2
  ps_x = 0
  ps_y = 0
  pr_x = 0
  pr_y = 0


  while c := f.read(1):
    if not c:
      break
    ps_x, ps_y = set_pos(c, ps_x, ps_y)
    print (f"Santa Position: {ps_x},{ps_y}")
    pres_map[f"{ps_x},{ps_y}"] = 1
    c = f.read(1)
    if not c:
      break
    pr_x, pr_y = set_pos(c, pr_x, pr_y)
    print (f"Robot Position: {pr_x},{pr_y}")
    pres_map[f"{pr_x},{pr_y}"] = 1


  print (f"Total: {len(pres_map.keys())}")