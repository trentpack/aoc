import sys
g_len = 1000
g_wid = 1000
grid = bytearray(g_len*g_wid)

def play ():
  g_len = 5
  g_wid = 5
  grid = bytearray(g_len*g_wid)
  total = 0
  for x in range(g_len):
      for y in range(g_wid):
          grid[x * g_len + y] = 1
  # grid[0] = 1
  for x in range(len(grid)):
      total += 1 if grid[x] == 1 else 0
  print (f"Total: {total}")
  print (f"grid: {grid}")

def toggle (start_pos_x, start_pos_y, end_pos_x, end_pos_y):
  x_range = range(start_pos_x, end_pos_x + 1)
  y_range = range(start_pos_y, end_pos_y + 1)
  print (x_range)
  print (y_range)
  for x in x_range:
    for y in y_range:
        grid[x * g_len + y] = 0 if grid[x * g_len + y] == 1 else 1
  return

def set_grid (value, start_pos_x, start_pos_y, end_pos_x, end_pos_y):
  x_range = range(start_pos_x, end_pos_x + 1)
  y_range = range(start_pos_y, end_pos_y + 1)
  for x in x_range:
    for y in y_range:
        grid[x * g_len + y] = value
  return

def parse (line):
    tokens = line.split()
    tok_len = len(tokens)
    print(f"Tokens: {tokens}")
    start_pos_x = int(tokens[tok_len-3].split(',')[0])
    start_pos_y = int(tokens[tok_len-3].split(',')[1])
    end_pos_x = int(tokens[tok_len-1].split(',')[0])
    end_pos_y = int(tokens[tok_len-1].split(',')[1])

    print(f"Positions: start: ({start_pos_x},{start_pos_y}), end ({end_pos_x},{end_pos_y})")
    if (tokens[0] == 'turn'):
      value = 1 if tokens[1] == "on" else 0
      set_grid (value, start_pos_x, start_pos_y, end_pos_x, end_pos_y)
    elif (tokens[0] == 'toggle'):
      toggle (start_pos_x, start_pos_y, end_pos_x, end_pos_y)
    else:
      print(f"Bad command: {line}")

def print_total():
  total = 0
  for x in range(len(grid)):
    total += 1 if grid[x] == 1 else 0
  print (f"Total: {total}")
  return
with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:

  for line in f:
    parse(line)
    print_total()
  print_total()

