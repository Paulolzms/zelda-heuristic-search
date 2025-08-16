import time
import os

MAPS_FOLDER = 'maps'

LAND_COSTS = {
  'G': 10,
  'A': 20,
  'F': 100,
  'M': 150,
  'W': 180,
  'C': 10,
  'X': float('inf')
}

def load_map(file_name):
  path = os.path.join(os.pardir, MAPS_FOLDER, file_name)
  with open(path, 'r') as f:
    lines = f.read().splitlines()
    mapa = [list(line.strip()) for line in lines if line.strip()]
    return mapa
  
def land_cost(mapa, pos):
  x, y = pos
  letter = mapa[x - 1][y - 1]
  return LAND_COSTS.get(letter, float('inf'))

def show_map(mapa):
  for row in mapa:
    print(''.join(row))

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def animate_path(mapa, path, start_pos, end_pos, delay=0.1):
  start = (start_pos[0] - 1, start_pos[1] - 1)
  end = (end_pos[0] - 1, end_pos[1] - 1)
  original_map = [row[:] for row in mapa]
  
  # Cria o mapa de exibição para manter o rastro
  display_map = [row[:] for row in original_map]
  
  # Marca os pontos de início e fim
  display_map[start[0]][start[1]] = 'S'
  display_map[end[0]][end[1]] = 'E'

  for step in path:
    clear_console()
    
    # Marca a posição atual do Link com 'L'
    display_map[step[0] - 1][step[1] - 1] = 'L'
    
    print("Caminho do Link:")
    show_map(display_map)
    time.sleep(delay)
    
    # Depois do atraso, muda o 'L' para '-' para deixar o rastro
    display_map[step[0] - 1][step[1] - 1] = '-'
  