from search_a_star import search_a_star
from mapa import load_map
from util import INITIAL_POSITION, FINAL_POSITION

DUNGEON_ENTRANCES = {
  'dungeon1.txt': (33, 6),
  'dungeon2.txt': (18, 40),
  'dungeon3.txt': (2, 25)
}

DUNGEON_EXITS = {
  'dungeon1.txt': (27, 15), 
  'dungeon2.txt': (26, 14), 
  'dungeon3.txt': (26, 15)  
}

DUNGEON_PINGS = {
  'dungeon1.txt': (4, 14), 
  'dungeon2.txt': (3, 14), 
  'dungeon3.txt': (20, 16) 
}

def journey(mapa, order):
  total_cost = 0
  current_pos = INITIAL_POSITION

  # Viaja para a primeira masmorra
  first_dungeon = order[0]
  entrance = DUNGEON_ENTRANCES[first_dungeon]
  path, cost_to_first_dungeon = search_a_star(mapa, current_pos, entrance)
  total_cost += cost_to_first_dungeon

  # Calcula o custo da primeira masmorra
  dungeon_cost = dungeon_path(first_dungeon)
  total_cost += dungeon_cost

  # Viaja entre as masmorras
  for i in range(len(order) - 1):
    from_dungeon = order[i]
    to_dungeon = order[i + 1]
    from_pos = DUNGEON_ENTRANCES[from_dungeon]
    to_pos = DUNGEON_ENTRANCES[to_dungeon]

    _, travel_cost = search_a_star(mapa, from_pos, to_pos)
    total_cost += travel_cost

    dungeon_cost = dungeon_path(to_dungeon)
    if dungeon_cost == float('inf'):
      return float('inf')
    total_cost += dungeon_cost

  # Viaja da ultima masmorra para Lost Wood
  last_dungeon = order[-1]
  last_entrance = DUNGEON_ENTRANCES[last_dungeon]
  _, final_travel_cost = search_a_star(mapa, last_entrance, FINAL_POSITION)
  total_cost += final_travel_cost

  return total_cost

def dungeon_path(dungeon):
  dungeon_map = load_map(dungeon)
  dungeon_entrance = DUNGEON_EXITS[dungeon]
  ping_pos = DUNGEON_PINGS[dungeon]

  # Custo de ir da entrada até o pingente
  _, cost_to_ping = search_a_star(dungeon_map, dungeon_entrance, ping_pos)
  
  # Custo de voltar do pingente para a entrada
  _, cost_to_exit = search_a_star(dungeon_map, ping_pos, dungeon_entrance)

  if cost_to_ping == float('inf') or cost_to_exit == float('inf'):
      return float('inf')
  
  return cost_to_ping + cost_to_exit

# Encontra a melhor sequência de masmorras para visitar
def best_order(mapa):
  dungeons = list(DUNGEON_ENTRANCES.keys())
  best_order = None
  best_cost = float('inf')

  for order in permutations(dungeons):
    cost = journey(mapa, order)
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