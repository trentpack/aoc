import sys

def createGraph (f):
  result_graph = [[-1] * 100] * 100
  result_index = {}
  idxCnt = 0
  for line in f:
    print(line)
    l_r = line.split('=')
    print(f"l_r: {l_r}")
    dist = int(l_r[1].strip())
    l_r = l_r[0].split("to")
    left = l_r[0].strip()
    right = l_r[1].strip()
    li = result_index.get(left, None)
    if li == None:
      li = idxCnt
      result_index[left] = li
      idxCnt += 1
    ri = result_index.get(right, None)
    if ri == None:
      ri = idxCnt
      result_index[right] = ri
      idxCnt += 1
    result_graph[li][ri] = dist
    result_graph[ri][li] = dist
  return result_graph,result_index

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
  min_dist = sys.maxsize
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
      ret_min = find_shortest(g, next, list(path), list(left), total_dist)
      if ret_min < min_dist:
        min_dist = ret_min
  if len(left) == 0:
    print(f"Path: {path} Dist: {total_dist}")
    if total_dist < min_dist:
      min_dist = total_dist
      #print(f"Found Min: {min_dist}")
      return min_dist
  return min_dist




with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  g = create_g_dict(f)
  print(f"Graph: {g}")
  min = sys.maxsize
  for city in g.keys():
    new_min = find_shortest(g, city)
    if new_min < min:
      min = new_min
  print(f"Min: {min}")