import sys

def parse_line(line):
  result = [0]*len(line)
  for i in range(0, len(line)):
    if line[i] != '.':
      result[i] = 1
  return result


def parse_floor(f):
  line = f.readline().strip()
  cur_row = parse_line(line)
  row_len = len(cur_row)
  print(f"cur_row: {cur_row}")
  buffer_len = row_len + 2
  buffer = [0]*buffer_len
  buffer_line = [0]*buffer_len
  #buffer.extend(buffer_line)
  for i in range(0, row_len):
    buffer_line[i+1] = cur_row[i]
  buffer.extend(buffer_line)
  print(f"buffer len: {len(buffer)}")
  last_time = False
  row_cnt = 2

  while not last_time:
    line = f.readline().strip()
    if not line:
      print("Expected EOF")
      last_time = True
      cur_row = [0]* row_len
    else:
      cur_row = parse_line(line)
    for i in range(0, row_len):
      buffer_line[i+1] = cur_row[i]
    buffer.extend(buffer_line)
    row_cnt += 1
  # SHOW FLOOR
  for i in range(0, row_cnt):
    print(f"{buffer[i*(row_len + 2):(i+1)*(row_len + 2)]}")
  return row_len, row_cnt, buffer


def solve_iter(row_len, row_cnt, buffer):
  buffer_len = row_len + 2
  counter = 0
  buffer_copy = buffer.copy()
  for j in range(1, row_cnt -1 ):
    for i in range(1, row_len+1):
      s_pos = buffer_len*j + i
      if buffer_copy[s_pos] == 1:
        n_cnt = 0
        for y in range(-1, 2):
          for x in range(i-1, i+2):
            b_pos = (y+j)*buffer_len + x
            if b_pos != s_pos and buffer_copy[b_pos] == 1:
              #print(f"Found neighbor at x: {x} y: {y}")
              n_cnt += 1
        #print(f"n_cnt: {n_cnt}")
        if n_cnt < 4:
          print(f"roll can be removed: {i-1}")
          buffer[s_pos] = 0
          counter +=1
  return counter


def solve_it(row_len, row_cnt, buffer):
  buffer_len = row_len + 2
  counter = 0
  last_time = False
  iter_cnt = 0
  while True:
    found = solve_iter(row_len, row_cnt, buffer)
    iter_cnt += 1
    print(f"Found: {found} iter: {iter_cnt}")
    if found == 0:
      break
    counter += found
  return counter


with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  row_len, row_cnt, buffer = parse_floor(f)
  answer = solve_it(row_len, row_cnt, buffer)
  print(f"answer: {answer}")