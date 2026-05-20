import sys

def create_g_dict (f):
  result_graph = {}
  for line in f:
    #print(line)
    l_r = line.split('=')
    #print(f"l_r: {l_r}")
    dist = int(l_r[1].strip())
    l_r = l_r[0].split("to")
    left = l_r[0].strip()
    right = l_r[1].strip()
    li = result_graph.get(left, None)
    if li == None:
      li = {right: dist}
      result_graph[left] = li
    else:
      li[right] = dist
    ri = result_graph.get(right, None)
    if ri == None:
      ri = {left: dist}
      result_graph[right] = ri
    else:
      ri[left] = dist
  return result_graph

def find_shortest (g, start, path = None, left = None, prev_dist = 0):
  max_dist = -1
  if left == None:
    cities = g.keys()
    left = list(cities)
  if path == None:
    path = []
  path.append(start)
  left.remove(start)
  #print(f"Start: {start} Path: {path}")
  total_dist = prev_dist
  for next in g[start]:
    if next not in path:
      total_dist = prev_dist
      total_dist += g[start][next]
      ret_max = find_shortest(g, next, list(path), list(left), total_dist)
      if ret_max > max_dist:
        max_dist = ret_max
  if len(left) == 0:
    print(f"Path: {path} Dist: {total_dist}")
    if total_dist > max_dist:
      max_dist = total_dist
      #print(f"Found max: {max_dist}")
      return max_dist
  return max_dist

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  g = create_g_dict(f)
  print(f"Graph: {g}")
  max = -1
  for city in g.keys():
    new_max = find_shortest(g, city)
    if new_max > max:
      max = new_max
  print(f"max: {max}")