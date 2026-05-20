import sys
with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  num_chars = 0
  num_bytes = 0
  line_num = 0
  for line in f:
    print(f"On line num: {line_num}")
    line_num += 1
    line = line.strip()
    print(line)
    num_chars = num_chars + len(line)

    pos = 0
    line_len = len(line)
    new_line = '"'
    while pos < line_len:
      if line[pos] == '\\':
        # HANDLE '\'
        new_line = new_line + '\\\\'
        pos += 1
      elif line[pos] == '"':
        # HANDLE '"'
        new_line = new_line + '\\"'
        pos += 1
      else:
        new_line = new_line + line[pos]
        pos += 1
    line = new_line + '"'
    print(line)
    num_bytes = num_bytes + len(line)
    print(f"num_bytes: {len(line)}")
  print(f"Answer: {num_bytes - num_chars}")