import sys

def parse_input(f):
  result = []

  for line in f:
    result.append(int(line))
  return result

def next_secret(in1):
  result = in1 * 64
  temp = in1
  result = result ^ temp
  result = result % 16777216
  temp = int(result / 32)
  result = result ^ temp
  result = result % 16777216
  temp = result * 2048
  result = result ^ temp
  result = result % 16777216
  return result

def calc2000th(secret):
  for i in range(0,2000):
    secret = next_secret(secret)
  return secret

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  print(f"test XOR (should be 37): {42^15}")
  print(f"test mod (should be 16113920): {100000000%16777216}")
  print(f"next_secret (should be 15887950): {next_secret(123)}")

  secrets = parse_input(f)
  final_secrets = []
  for secret in secrets:
    ans = calc2000th(secret)
    final_secrets.append(ans)
    #print(f"{secret}: {ans}")
  f_sum = 0
  for fs in final_secrets:
    f_sum += fs
  print(f"Final sum: {f_sum}")