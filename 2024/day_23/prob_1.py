import sys
import re


def parse_input(f):
  result = {}

  for line in f:
    cur_line = line.strip()
    parts = cur_line.split("-")
    if parts[0] in result.keys():
      result[parts[0]].append(parts[1])
    else:
      result[parts[0]] = [parts[1]]
    if parts[1] in result.keys():
      result[parts[1]].append(parts[0])
    else:
      result[parts[1]] = [parts[0]]
  return result

def find_three_way(links):
  three = set()
  for mc1 in links:
    current = links[mc1]
    for mc2 in current:
      next_links = links.get(mc2, None)
      for mc3 in next_links:
        next_next_link = links.get(mc3, None)
        if next_next_link is not None and mc1 in next_next_link:
          add_me = [mc1,mc2,mc3]
          add_me.sort()
          three.add("{},{},{}".format(add_me[0],add_me[1],add_me[2]))
  return three




with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  links = parse_input(f)
  found = find_three_way(links)
  print(f"links: {links}")
  print(f"found: {found}")
  ts = []
  for threes in found:
    if re.search("t[a-z]",threes) is not None:
      ts.append(threes)
  ts.sort()
  for t in ts:
    print(t)
  print(f"ts len: {len(ts)}")

