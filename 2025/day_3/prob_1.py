import sys



def find_largest_2dig(nums, start):
  max_tens = 0
  max_ones = 0
  max_pos = 0
  nums_len = len(nums)
  for i in range(start, nums_len - 1):
    if nums[i] > max_tens:
      max_tens = nums[i]
      max_pos = i
  for i in range(max_pos + 1, nums_len):
    if nums[i] > max_ones:
      max_ones = nums[i]
  return max_tens * 10 + max_ones


def parse_and_solve(f):
  total = 0
  for line in f:
    line = line.strip()
    nums = [0]*len(line)
    for i in range (0, len(line)):
      nums[i] = int(line[i])
    print(f"line: {line}")
    print(f"nums: {nums}")
    largest = find_largest_2dig (nums, 0)
    print(f"larget: {largest}")
    total += largest
  return total

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  answer = parse_and_solve(f)
  print(f"answer: {answer}")