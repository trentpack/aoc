import sys

def is_nice(line):
  line_len = len(line)
  pos = 0
  #print (f"line: {line}")
  dd = False
  dw = False
  while pos + 1 < line_len:
    pair = line[pos:pos + 2]
    #print (f"pair: {pair}")
    if pair in line[pos + 2:]:
      dd = True
      break
    pos += 1
  pos = 1
  while pos + 1 < line_len:
    if line[pos -1] == line[pos + 1]:
      dw = True
    pos +=1
  #print (f"Checks: dd={dd} dw={dw}")
  return dd and dw

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  line = None
  total = 0
  for line in f:
    nice = is_nice(line)
    if nice is True:
      total += 1
print(f"Total: {total}")