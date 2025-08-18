from search_a_star import search_a_star
from mapa import load_map
from util import INITIAL_POSITION, FINAL_POSITION, DUNGEON_ENTRANCES, DUNGEON_EXITS, DUNGEON_PINGS

def journey(mapa, order):
  total_cost = 0
  current_pos = INITIAL_POSITION
  
  # Viaja para a primeira masmorra
  first_dungeon = order[0]
  entrance = DUNGEON_ENTRANCES[first_dungeon]
  _, cost_to_first_dungeon = search_a_star(mapa, current_pos, entrance)

  if cost_to_first_dungeon == float('inf'):
    print(f"Erro: Não foi possível encontrar um caminho da posição inicial ({current_pos}) para {first_dungeon} ({entrance}).")
    return float('inf')
      
  total_cost += cost_to_first_dungeon
  
  # Calcula o custo da primeira masmorra
  dungeon_cost = dungeon_path_cost(first_dungeon)
  if dungeon_cost == float('inf'):
    print(f"Erro: Não foi possível encontrar um caminho na masmorra {first_dungeon}.")
    return float('inf')
  total_cost += dungeon_cost

  # Viaja entre as masmorras
  for i in range(len(order) - 1):
    from_dungeon = order[i]
    to_dungeon = order[i + 1]
    from_pos = DUNGEON_ENTRANCES[from_dungeon]
    to_pos = DUNGEON_ENTRANCES[to_dungeon]

    _, travel_cost = search_a_star(mapa, from_pos, to_pos)
    
    if travel_cost == float('inf'):
      print(f"Erro: Não foi possível encontrar um caminho de {from_dungeon} ({from_pos}) para {to_dungeon} ({to_pos}).")
      return float('inf')
    
    total_cost += travel_cost

    dungeon_cost = dungeon_path_cost(to_dungeon)
    if dungeon_cost == float('inf'):
      print(f"Erro: Não foi possível encontrar um caminho na masmorra {to_dungeon}.")
      return float('inf')
    total_cost += dungeon_cost

  # Viaja da ultima masmorra para Lost Woods
  last_dungeon = order[-1]
  last_entrance = DUNGEON_ENTRANCES[last_dungeon]
  _, final_travel_cost = search_a_star(mapa, last_entrance, FINAL_POSITION)
  if final_travel_cost == float('inf'):
      print(f"Erro: Não foi possível encontrar um caminho de {last_dungeon} ({last_entrance}) para Lost Woods ({FINAL_POSITION}).")
      return float('inf')
      
  total_cost += final_travel_cost
  
  return total_cost

# Encontra o custo da masmorra
def dungeon_path_cost(dungeon_file):
  dungeon_map = load_map(dungeon_file)
  dungeon_exits_pos = DUNGEON_EXITS[dungeon_file]
  ping_pos = DUNGEON_PINGS[dungeon_file]

  _, cost_to_ping = search_a_star(dungeon_map, dungeon_exits_pos, ping_pos)
  if cost_to_ping == float('inf'):
    print("Erro: Não foi possível encontrar o caminho da entrada para o pingente.")
    return float('inf')

  _, cost_to_exit = search_a_star(dungeon_map, ping_pos, dungeon_exits_pos)
  if cost_to_exit == float('inf'):
    print("Erro: Não foi possível encontrar o caminho do pingente para a saída.")
    return float('inf')

  return cost_to_ping + cost_to_exit

# Encontra a melhor sequência de masmorras para visitar
def best_order(mapa):
  dungeons = list(DUNGEON_ENTRANCES.keys())
  best_order = None
  best_cost = float('inf')

  for order in permutations(dungeons):
    cost = journey(mapa, order)
    print(f"Ordem: {order}, Custo: {cost}")
    if cost < best_cost:
      best_cost = cost
      best_order = order

  return best_order, best_cost

# Permutação da ordem das masmorras
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

# Encontra o caminho da jornada
def get_full_path(mapa, order):
  full_path = []
  current_pos = INITIAL_POSITION

  path_to_first = search_a_star(mapa, current_pos, DUNGEON_ENTRANCES[order[0]])[0]
  if path_to_first is None:
    return None
  full_path.extend(path_to_first)

  for i in range(len(order) - 1):
    path_between = search_a_star(mapa, DUNGEON_ENTRANCES[order[i]], DUNGEON_ENTRANCES[order[i + 1]])[0]
    if path_between is None:
      return None
    full_path.extend(path_between)

  path_to_end = search_a_star(mapa, DUNGEON_ENTRANCES[order[-1]], FINAL_POSITION)[0]
  if path_to_end is None:
    return None
  full_path.extend(path_to_end)

  return full_path
