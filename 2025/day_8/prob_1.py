import sys

def parse(f):
  result = []
  for line in f:
    line = line.strip().split(",")
    result.append([int(line[0]),int(line[1]),int(line[2])])
  return result

def find_3d_dist(a,b):
  dx = abs(a[0]-b[0])
  dy = abs(a[1]-b[1])
  dz = abs(a[2]-b[2])
  return (dx**2 + dy**2 + dz**2)**0.5


def find_dists(coords):
  result = []
  for i in range(0,len(coords)):
    dist = [0]*(len(coords)-(i+1))
    cur_coord = coords[i]
    for j in range(i+1, len(coords)):
      dist[j-i-1] = find_3d_dist(cur_coord, coords[j])
    result.append(dist)
  return result

def find_min_d(dists):
  result = dists.copy()
  min_i = 0
  min_j = 0
  min = result[0][0]
  for i in range(0,len(result)):
    dist_tmp = result[i]
    for j in range(i+1, len(result)):
      if dist_tmp[j-i-1] != -1 and dist_tmp[j-i-1] < min:
        min_i = i
        min_j = j
        min = dist_tmp[j-i-1]
  result[min_i][min_j-min_i-1] = -1
  return min, min_i, min_j, result


with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
  coords = parse(f)
  print(f"coords: {coords}")
  dists = find_dists(coords)
  print(f"dists: {dists}")
  min, min_i, min_j, result = find_min_d(dists)
  print(f"Result: {result}")
  print(f"Min: {min} min_i: {min_i} min_j: {min_j}")
  print(f"coord_i: {coords[min_i]} coord_j: {coords[min_j]}")