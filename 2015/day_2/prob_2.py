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
    p1 = 2*x+2*y
    p2 = 2*x+2*z
    p3 = 2*y+2*z
    v = x*y*z
    total += smallest(p1, p2, p3) + v

print(f"Total {total}")