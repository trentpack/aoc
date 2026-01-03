#!/bin/python3
import sys

def smallest (x,y,z):
  smallest = x
  if y <= x and y <= z:
    smallest = y
  if z <= x and z <= y:
    smallest = z
  return smallest


with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  line = None
  total = 0
  for line in f:
    sides = line.split("x")
    x = int(sides[0])
    y = int(sides[1])
    z = int(sides[2])
    print(f"Dims: {x}x{y}x{z}")
    print(f"Ans: {2*(x*y) + 2*(x*z) + 2*(y*z) + smallest((x*y),(x*z),(y*z))}")
    total += 2*(x*y) + 2*(x*z) + 2*(y*z) + smallest((x*y),(x*z),(y*z))

print(f"Total {total}")