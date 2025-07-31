from search_a_star import search_a_star
from util import INITIAL_POSITION, FINAL_POSITION

DUNGEON_ENTRANCES = {
  'dangeon1.txt': (33, 6),
  'dangeon2.txt': (18, 40),
  'dangeon3.txt': (2, 25)
}

def journey(mapa, order):
  total_cost = 0
  current_pos = INITIAL_POSITION

  for dangeon_file in order:
    entrance = DUNGEON_ENTRANCES[dangeon_file]
    
    path, cost = search_a_star(mapa, current_pos, entrance)
    if not path:
      return float('inf')
    total_cost += cost

    total_cost += dangeon_path(dangeon_file)
    current_pos = entrance

  path, cost = search_a_star(mapa, current_pos, FINAL_POSITION)
  if not path:
    return float('inf')
  total_cost += cost

  return total_cost