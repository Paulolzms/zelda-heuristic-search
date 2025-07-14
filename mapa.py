LAND_COSTS = {
  'G': 10,
  'A': 20,
  'F': 100,
  'M': 150,
  'W': 180
}

def load_map(path):
  with open(path, 'r') as f:
    lines = f.read().splitlines()
    mapa = [list(line.strip()) for line in lines if line.strip()]
    return mapa
  
def land_cost(mapa, pos):
  x, y = pos
  letter = mapa[x][y]
  return LAND_COSTS.get(letter, float('inf'))

def show_map(mapa):
  for row in mapa:
    print(''.join(row))