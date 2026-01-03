import sys


def parseAndSolve(f):
  cur_loc = 50
  retval = 0
  for line in f:
    prev_loc = cur_loc
    dir = line[0]
    num = int(line[1:])
    print(f"dir: {dir} num: {num}")
    if num >= 100:
      print(f"large num, adding {num // 100}")
      retval += num // 100
      num = num - ((num // 100) * 100)
    if dir == 'L':
      cur_loc -= num
    elif dir == 'R':
      cur_loc += num
    else:
      print("Unexpected input! {line}")
    #print(f"cur_loc: {cur_loc}")
    if (cur_loc < 0 and prev_loc != 0) or cur_loc > 100:
      print(f"Rotated on line: {line}")
      retval += 1
    if cur_loc < 0:
      cur_loc = 100 + cur_loc
    #print(f"cur_loc: {cur_loc}")
    cur_loc %= 100
    print(f"cur_loc: {cur_loc}")
    if cur_loc == 0:
      retval += 1
  return retval

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  answer = parseAndSolve(f)
  print(f"answer: {answer}")