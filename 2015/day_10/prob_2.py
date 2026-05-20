import sys

def parse (f):
  result = None
  for line in f:
    result = line.strip()
  return result

def count_runs(input):
  result = ""
  runlen = 0
  curChar = None
  for c in input:
    if c == curChar:
      runlen += 1
    elif curChar == None:
      # Special case at begin
      curChar = c
      runlen = 1
    else:
      result += "{}{}".format(runlen, curChar)
      curChar = c
      runlen = 1
  # ADD LAST RUN
  result += "{}{}".format(runlen, curChar)
  return result



with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  line = parse(f)
  result = line
  for i in range(0,50):
    result = count_runs(result)
  print(f"Input: {line} Out len: {len(result)}")