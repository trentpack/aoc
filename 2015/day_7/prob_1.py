import sys

def parse(f):
  result = {}
  for l in f:
    l = l.strip()
    parts = l.split("->")
    #print (f"parts: {parts}")
    result[parts[1].strip()] = parts[0].strip()
  return result

def rules(state):
  finished = True
  for key in state.keys():
    # print(f"key {key}")
    data = state[key]
    op_parts = []
    if isinstance(data, str):
      print(f"data: '{data}'")
      op_parts = data.split(" ")
    operand = None
    params_good = False
    rule_result = None
    params = []
    if len(op_parts) == 1: # SCALAR (MAKE SURE ITS CONVERTED TO INT)
      if not isinstance(data, int):
        # SAVE BACK INT
        if data.isdigit():
          rule_result = int(data)
        elif isinstance(state[data], int): # PARAM is VAR
          rule_result = state[data]
        else:
          finished = False
          continue
    elif len(op_parts) == 2: # SINGLE PARAM
      print(f"SINGLE PARAM OP: {op_parts}")
      operand = op_parts[0]
      # VERIFY INPUTS ARE SCALARS
      if op_parts[1].isdigit():
        params.append(int(op_parts[1]))
        params_good = True
      elif isinstance(state[op_parts[1]], int):
        params.append(state[op_parts[1]])
        params_good = True
      else:
        finished = False
    elif len(op_parts) == 3: # 2 PARAM
      print(f"TWO PARAM OP: {op_parts}")
      operand = op_parts[1]
      # VERIFY INPUTS ARE SCALARS
      if op_parts[0].isdigit():
        params.append(int(op_parts[0]))
        params_good = True
      elif isinstance(state[op_parts[0]], int):
        params.append(state[op_parts[0]])
        params_good = True
      else:
        finished = False
        continue
      if op_parts[2].isdigit():
        params.append(int(op_parts[2]))
        params_good = True
      elif isinstance(state[op_parts[2]], int):
        params.append(state[op_parts[2]])
        params_good = True
      else:
        finished = False
        continue
    if key == 'f':
      print(f"operand: {operand}, params_good: {params_good}, params: {params}")
    if operand is not None and params_good:
      match operand:
        case 'AND':
          rule_result = params[0]&params[1]
        case 'OR':
          rule_result = params[0]|params[1]
        case 'LSHIFT':
          rule_result = params[0]<<params[1]
          print(f"Running LSHIFT, {params[0]}<<{params}[1] = {rule_result}")
        case 'RSHIFT':
          rule_result = params[0]>>params[1]
        case 'NOT':
          rule_result = ~params[0]
    if rule_result is not None:
      if rule_result < 0:
        rule_result = 65536 + rule_result
        print(f"rule_result was neg: {rule_result}")
      state[key] = rule_result
  return finished

def pretty_print_state(state):
  keys = list(state.keys())
  keys.sort()
  for key in keys:
    print(f"{key}: {state[key]}")

def main():
  state = None
  with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
    state = parse(f)
  print( f"state: {state}")
  finished = False
  round = 0
  while not finished:
    finished = rules(state)
    round = round + 1
    print( f"Round #{round} state: {state}")
  pretty_print_state(state)

if __name__ == "__main__":
    main()