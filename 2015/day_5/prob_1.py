import sys

def is_nice(line):
  vcount = 0
  prev = ''
  found_double = False
  vowels = "aeiou"
  bad_strs=["ab","cd", "pq", "xy"]
  found_bad = False
  for c in line:
    if c in vowels:
      vcount += 1
    if c == prev:
      found_double = True
    prev = c
  if vcount >= 3 and found_double is True:
    for bad_str in bad_strs:
      if bad_str in line:
        found_bad = True
  #print (f"Checks: vowels={vcount} found_double={found_double} found_bad={found_bad}")
  return vcount >= 3 and found_double and found_bad is not True



with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  line = None
  total = 0
  for line in f:
    nice = is_nice(line)
    if nice is True:
      total += 1
print(f"Total: {total}")