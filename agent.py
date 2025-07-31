from search_a_star import search_a_star
from util import INITIAL_POSITION, FINAL_POSITION

DUNGEON_ENTRANCES = {
  'dungeon1.txt': (33, 6),
  'dungeon2.txt': (18, 40),
  'dungeon3.txt': (2, 25)
}

def journey(mapa, order):
  total_cost = 0
  current_pos = INITIAL_POSITION

  for dungeon_file in order:
    entrance = DUNGEON_ENTRANCES[dungeon_file]
    
    path, cost = search_a_star(mapa, current_pos, entrance)
    if not path:
      return float('inf')
    total_cost += cost

    total_cost += dungeon_path(dungeon_file)
    current_pos = entrance

  path, cost = search_a_star(mapa, current_pos, FINAL_POSITION)
  if not path:
    return float('inf')
  total_cost += cost

  return total_cost

def best_order(mapa):
  dungeons = list(DUNGEON_ENTRANCES.keys())
  best_order = None
  best_cost = float('inf')

  for order in permutations(dungeons):
    cost = None
    if cost < best_cost:
      best_cost = cost
      best_order = order

  return best_order, best_cost

def permutations(elements):
  if len(elements) == 0:
    return []
  if len(elements) == 1:
    return [elements]
  perms = []

  for i in range(len(elements)):
    e = elements[i]
    perms_without_e = permutations(elements[:i] + elements[i+1:])
    for p in perms_without_e:
      perms.append([e] + p)
  return perms