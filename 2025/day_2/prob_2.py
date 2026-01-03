import sys

def find_pattern (nums):
  nums_len = len(nums)
  for i in range(0, nums_len // 2):
    cur_num = 0 #FIX ME

def parse_solve(f):
  large_str = f.readline()
  ranges = large_str.split(",")
  total = 0
  for my_range in ranges:
    range_arr = my_range.split("-")
    start = int(range_arr[0])
    end = int(range_arr[1])
    print(f"start: {start} end: {end}")
    for i in range(start, end + 1):
      i_str = str(i)
      half = len(i_str) // 2
      # if len(i_str) % 2 == 1:
      #   print(f"Odd sized string: {i_str}")
      if i_str[0:half] == i_str[half:]:
        print(f"Invalid id: {i_str}")
        total += i
  return total

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  total = parse_solve(f)
  print(f"answer: {total}")