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
  j_cnt = 0

  for j in fresh:
    min = j[0]
    max = j[1]
    for k in fresh[0: j_cnt]:
      if min >= k[0] and min <= k[1]:
        min = k[1]
      if max >= k[0] and max <= k[1]:
        max = k[0]
    print(f"j: {j} max: {max} min: {min} j_cnt: {j_cnt} diff: {(max - min)}")
    if (max - min) > 0:
      result += max - min
    j_cnt +=1
  # for j in fresh:
  #   for i in range(j[0], j[1]):
  #     found_prev = False
  #     for k in range(0, j_cnt):
  #       if fresh[k][0] <= i and fresh[k][1] > i:
  #         found_prev = True
  #         break
  #     if not found_prev:

  #       result += 1
  #   j_cnt += 1
  return result

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  fresh, stock = parse(f)
  print(f"fresh: {fresh}")
  print(f"stock: {stock}")
  answer = solve(fresh, stock)
  print(f"answer: {answer}")