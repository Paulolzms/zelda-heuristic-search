INITIAL_POSITION = (28,25)
FINAL_POSITION = (6,7)

MOVS = [
  (-1, 0),
  (1, 0),
  (0, -1),
  (0, 1)
]

def neighbors_allowed(mapa, pos):
  rows, cols = len(mapa), len(mapa[0])
  x, y = pos
  neighbors = []
  for dx, dy in MOVS:
    nx, ny = x + dx, y + dy
    if 0 <= nx <= rows and 0 <= ny <= cols:
      neighbors.append((nx, ny))
  return neighbors

def heuristic(pos1, pos2):
  x1, y1 = pos1
  x2, y2 = pos2
  return abs(x1 - x2) + abs(y1 - y2)