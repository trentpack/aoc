import sys

def find_largest_dig(nums, start, out_size):
  max = 0
  max_pos = 0
  nums_len = len(nums)
  print(f"start: {start} end: {nums_len - out_size +1}")
  for i in range(start, nums_len - out_size + 1):
    if nums[i] > max:
      max = nums[i]
      max_pos = i
  return max, max_pos + 1

def find_largest_n_dig(nums, start, out_size):
  #pow_size = out_size - 1
  result = 0
  cur_pos = 0
  print (f"pow_size: {out_size}")
  for i in range(out_size, 0, -1):
    print(f"i: {i}")
    max, cur_pos = find_largest_dig(nums, cur_pos, i)
    print(f"max: {max} cur_pos: {cur_pos}")
    result += max * 10 ** (i - 1)
  return result


def parse_and_solve(f):
  total = 0
  for line in f:
    line = line.strip()
    nums = [0]*len(line)
    for i in range (0, len(line)):
      nums[i] = int(line[i])
    print(f"line: {line}")
    print(f"nums: {nums}")
    largest = find_largest_n_dig(nums, 0, 12)
    print(f"larget: {largest}")
    total += largest
  return total

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  answer = parse_and_solve(f)
  print(f"answer: {answer}")