import sys
import re

math_funcs = '+*'
def parse(f):
  nums = []
  funcs = ""
  for line in f:
    nums.append(line.rstrip("\n"))
  funcs = nums[len(nums) - 1]
  nums.pop()
  #nums.reverse()
  ret_funcs = []
  col_cnt = 0
  my_func = None
  print(f"funcs: {funcs} len: {len(funcs)}")
  for i in range (0, len(funcs)):
    print(f"at: {funcs[i]}")
    if funcs[i] in math_funcs:
      print("Found operand")
      if i == 0:
        #BEGINNING
        print("At beginning")
        my_func = funcs[i]
      else:
        print("Found next operand")
        ret_funcs.append({'func': my_func, 'cols': col_cnt})
        my_func = funcs[i]
        col_cnt = 0
    else:
      col_cnt += 1
  ret_funcs.append({'func': my_func, 'cols': col_cnt + 1})


  return nums, ret_funcs

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

def find_num_col(nums, funcs):
  ret_nums = []
  ret_funcs = []
  for i in range(0, len(funcs)):
    print(f"On funct: {i}")
    cols = funcs[i]['cols']
    prev_cols = 0
    func = funcs[i]['func']
    ret_funcs.append(func)
    for j in range(0, i):
      prev_cols += funcs[j]['cols']
    cur_nums = ( [0 for _ in range(cols)])

    for j in range(0, len(nums)):
      for k in range(0, cols):
        cur_num = nums[j][prev_cols + i + k]
        if cur_num != " ":
          print(f"cur_nums: {cur_nums}")
          print(f"cur_num: {cur_num} k: {k} j: {j} prev_cols: {prev_cols}")
          cur_nums[k] = int(cur_num) + cur_nums[k] * 10
          print(f"cur_nums: {cur_nums}")
    ret_nums.append(cur_nums)
  return ret_nums, ret_funcs

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  nums, funcs = parse(f)
  print(f"nums: {nums} funcs: {funcs}")
  nums, funcs = find_num_col(nums, funcs)
  print(f"nums: {nums} funcs: {funcs}")
  answer = solve(nums, funcs)
  print(f"answer: {answer}")