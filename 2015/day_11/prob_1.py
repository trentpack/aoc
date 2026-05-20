import sys

alpha = 'abcdefghijklmnopqrstuvwxyz'
ord_base = 97
alpha_len = 26

def inc_char(c):
  c_int = ord(c) - ord_base + 1
  res_a = c_int % alpha_len
  res_c = (c_int / alpha_len) == 1
  #print(f"c_int: {c_int} res_a: {res_a} res_c: {res_c} result: {chr(res_c + ord_base)}")
  return res_c, chr(res_a + ord_base)
  

def increment_str(input):
  flipped = input[::-1]
  result = ""
  print(f"Flipped: {flipped}")
  carry = True
  count = 0
  while carry and count < len(flipped):
    carry, c = inc_char(flipped[count])
    result = result + c
    count += 1
    #print(f"carry: {carry}, c: {c}: result: {result}")
  for c in flipped[count:]:
    result = result + c
  return result[::-1]


def check_pw(input)
  inpad = input + "  "
  # Rule 1, atleast one run of three
  pass_r1 = False
  for i in range(len(input):
    ord_i0 = ord(inpad[i]) + 2
    ord_i1 = ord(inpad[i+1]) + 1
    ord_i2 = ord(inpad[i+2])
    if ord_i0 == ord_i1 and ord_i0 == ord_i2:
      pass_r1 = True
      break
  
  #Rule 2, no i, o, or l
  bad = "iol"
  pass_r2 = True
  for i in input:
    if i in bad:
      pass_r2 = False
      break

  #Rule 3, atleast two different, non-overlapping pairs
  pair_cnt = 0
  c_cnt = 0
  pass_r3 = False
  while c_cnt < len(input):
    c1 = inpad[c_cnt]
    c2 = inpad[c_cnt + 1]
    if c1 == c2:
      pair_cnt += 1
      c_cnt += 2
    else
      c_cnt +=1
    if pair_cnt > 1:
      pass_r3 = True
      break

  return pass_r1 and pass_r2 and pass_r3


def main ():
  input = sys.argv[1]
  print(f"Input: {input}")
  result = increment_str(input)
  print(f"Result: {result}")
  # for i in range(len(alpha)):
  #     print(f"alpha pos: {i} char: {alpha[i]} int: {ord(alpha[i])}")






if __name__ == "__main__":
  main()
