import sys

def parse_input(f):
  inputs_done = False
  inputs = {}
  funcs = {}

  for line in f:
    cur_line = line.strip()
    if cur_line == "":
      inputs_done = True
      continue
    if not inputs_done:
      key, val = cur_line.split(": ")
      inputs[key] = int(val)
    else:
      expr, key = cur_line.split(" -> ")
      funcs[key] = expr
  return inputs, funcs

def xor_op (lh, rh):
  return lh ^ rh

def and_op (lh, rh):
  return lh & rh

def or_op (lh, rh):
  return lh | rh


def process_function(func, func_results):
  #print(f"Processing func: {func}")
  parts = func.split(" ")
  result = None
  if len(parts) != 3:
    print(f"Unknown func def: {func}")
    sys.exit(1)
  lh = func_results.get(parts[0], None)
  rh = func_results.get(parts[2], None)
  op = parts[1]
  # CHECK INPUTS
  if rh == None or lh == None:
    #print("Don't have inputs yet")
    return None
  match op:
    case "AND":
      result = and_op(lh, rh)
    case "OR":
      result = or_op(lh, rh)
    case "XOR":
      result = xor_op(lh, rh)
    case _:
      print(f"Unknown op: {op}")
      sys.exit(1)
  return result

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  inputs, funcs = parse_input(f)
  print("Inputs:", inputs)
  print("Functions:", funcs)

  x_digs=""
  y_digs=""
  inputs_sorted = list(inputs.keys())
  inputs_sorted.sort(reverse=True)
  for input in inputs_sorted:
    if input[0] == 'x':
      x_digs = x_digs + str(inputs[input])
    if input[0] == 'y':
      y_digs = y_digs + str(inputs[input])
  print(f"x_digs: {x_digs}")
  print(f"y_digs: {y_digs}")

  x_val = int(x_digs, 2)
  y_val = int(y_digs, 2)

  print("Correct Binary Result:  {0:b}".format((x_val+y_val)))
  print(f"Correct Decimal Result: {str(x_val+y_val)}")

  functions_to_process = list(funcs.keys())
  func_results = {}
  for input in inputs:
    func_results[input] = inputs[input]
  for func in funcs:
    func_results[func] = None
  while len(functions_to_process) > 0:
    for func in functions_to_process:
      func_result = process_function(funcs[func], func_results)
      if func_result != None:
        func_results[func] = func_result
        functions_to_process.remove(func)
        break
  print("Function Results:", func_results)
  result_funcs = []
  for func in func_results:
    if func.startswith("z"):
      result_funcs.append(func)
  result_funcs.sort(reverse=True)
  print(f"Results for functions in order: {result_funcs}")
  result_str = ""
  for func in result_funcs:
    #print(func_results[func], end="", flush=False)
    result_str += str(func_results[func])
  print(f"Binary Result: {result_str}")
  print(f"Decimal Result: {int(result_str, 2)}")
