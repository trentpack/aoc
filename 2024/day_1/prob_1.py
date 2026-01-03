import sys
l_and_k_max = 5
num_tum = 5
lock_ident= '#####'
key_ident= "....."

def parse (my_file):
  keys = []
  locks = []

  while True:
    is_key = True
    cur_item = [0,0,0,0,0]
    line = my_file.readline().strip()
    if not line:
      print("Expected EOF")
      return keys, locks
    if line == lock_ident:
      is_key = False
    elif line != key_ident:
      print(f"Bad ident line: {line}")
      return None, None
    for i in range(l_and_k_max):
      line = my_file.readline()
      if not line:
        print("UnExpected EOF")
        return None, None
      print(f"Tokens: {line}")
      if (len(line.strip()) != num_tum and i == l_and_k_max - 1):
        print(f"Found end of key/lock")
        break
      for i in range(num_tum):
        if line[i] == '#':
          cur_item[i] += 1
    line = my_file.readline() # ignore top/bottom
    line = my_file.readline() # read spacer
    if is_key:
      keys.append(cur_item)
    else:
      locks.append(cur_item)



with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  keys, locks = parse(f)
  total_pairs = 0
  print(f"Keys: {keys}")
  print(f"Locks: {locks}")
  # Further processing here
  for lock in locks:
    print(f"Processing lock: {lock}")
    for key in keys:
      print(f"  Trying key: {key}")
      can_open = True
      for i in range(num_tum):
        #print(f"col {i} sum: {key[i]} + {lock[i]} = {key[i] + lock[i]}")
        if (key[i] + lock[i]) > l_and_k_max:
          can_open = False
          break
      if can_open:
        print(f"Lock {lock} can be opened by key {key}")
        total_pairs += 1
  print(f"Total pairs: {total_pairs}")