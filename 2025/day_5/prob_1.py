import sys

def parse(f):
  fresh = []
  stock = []
  on_fresh = True
  for line in f:
    line = line.strip()
    #print(f"line: {line}")
    if line == "":
      on_fresh = False
      #print(f"Off fresh")
      continue

    if on_fresh == True:
      my_ran = line.split("-")
      new_ran = [int(my_ran[0]), int(my_ran[1])+1]
      fresh.append(new_ran)
    else:
      stock.append(int(line))
  return fresh, stock

def solve(fresh, stock):

  result = 0
  for i in stock:
    for j in fresh:
      if j[0] <= i and j[1] >= i:
        result += 1
        break
  return result

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  fresh, stock = parse(f)
  print(f"fresh: {fresh}")
  print(f"stock: {stock}")
  answer = solve(fresh, stock)
  print(f"answer: {answer}")