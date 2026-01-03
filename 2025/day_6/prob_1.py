import sys
math_funcs = "+*"
def parse(f):
  nums = []
  funcs = []
  for line in f:
    line = line.strip()
    parts = line.split()
    #print(f"parts: {parts}")
    if parts[0] in math_funcs:
      for part in parts:
        funcs.append(part)
    elif len(nums) == 0:
      for part in parts:
        nums.append([int(part)])
    else:
      for i in range(0,len(parts)):
        nums[i].append(int(parts[i]))
  return nums, funcs

def mult(nums):
  result = 1
  for num in nums:
    result *= num
  return result

def add(nums):
  result = 0
  for num in nums:
    result += num
  return result


def solve(nums, funcs):
  answer = 0
  for i in range(0,len(funcs)):
    match funcs[i]:
      case '*': answer += mult(nums[i])
      case '+': answer += add(nums[i])
  return answer

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  nums, funcs = parse(f)
  print(f"nums: {nums} funcs: {funcs}")
  answer = solve(nums, funcs)
  print(f"answer: {answer}")