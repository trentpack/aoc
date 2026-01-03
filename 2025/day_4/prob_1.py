import sys

def parse_line(line):
  result = [0]*len(line)
  for i in range(0, len(line)):
    if line[i] != '.':
      result[i] = 1
  return result


def solve_it(f):
  #Prep
  line = f.readline().strip()
  cur_row = parse_line(line)
  row_len = len(cur_row)
  print(f"cur_row: {cur_row}")
  buffer_len = row_len + 2
  buffer = [0]*4*(buffer_len)
  for i in range(0, row_len):
    buffer[(buffer_len) + i+1] = cur_row[i]
  line = f.readline().strip()
  cur_row = parse_line(line)
  print(f"cur_row: {cur_row}")
  for i in range(0, row_len):
    buffer[2*(buffer_len) + i+1] = cur_row[i]

  counter = 0
  last_time = False
  while True:
    #CHECK NEIGHBORS
    # for i in range(0, 4):
    #   print(f"{buffer[i*(row_len + 2):(i+1)*(row_len + 2)]}")
    for i in range(1, row_len+1):
      s_pos = buffer_len + i
      if buffer[s_pos] == 1:
        n_cnt = 0
        for y in range(0, 3):
          for x in range(i-1, i+2):
            b_pos = y*buffer_len + x
            if b_pos != s_pos and buffer[b_pos] == 1:
              #print(f"Found neighbor at x: {x} y: {y}")
              n_cnt += 1
        #print(f"n_cnt: {n_cnt}")
        if n_cnt < 4:
          print(f"roll can be removed: {i-1}")
          counter +=1

    #MOVE LINES UP
    for i in range(0, row_len):
      buffer[i+1] = buffer[buffer_len+i+1]
    for i in range(0, row_len):
      buffer[(buffer_len) + i+1] = buffer[2*(buffer_len) + i+1]
    if last_time:
      break
    line = f.readline().strip()
    if not line:
      print("Expected EOF")
      last_time = True
      cur_row = [0]* row_len
    else:
      cur_row = parse_line(line)
    print(f"cur_row: {cur_row}")
    for i in range(0, row_len):
      buffer[2*(buffer_len) + i+1] = cur_row[i]
  return counter


with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  answer = solve_it(f)
  print(f"answer: {answer}")