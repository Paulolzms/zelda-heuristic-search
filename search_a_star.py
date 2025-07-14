import heapq
from util import neighbors_allowed, heuristic
from mapa import land_cost

def search_a_star(mapa, initial_pos, final_pos):
  open_set = []
  heapq.heappush(open_set, (0, initial_pos))
  came_from = {initial_pos: None}
  current_cost = {initial_pos: 0}

  while open_set:
    _, current = heapq.heappop(open_set)

    if current == final_pos:
      path = []

      while current:
        path.append(current)
        current = came_from[current]
      path.reverse()
      return path, current_cost[final_pos]

    for neighbor in neighbors_allowed(mapa, current):
      tentative_cost = current_cost[current] + land_cost(mapa, neighbor)
      if neighbor not in current_cost or tentative_cost < current_cost[neighbor]:
        current_cost[neighbor] = tentative_cost
        priority = tentative_cost + heuristic(neighbor, final_pos)
        heapq.heappush(open_set, (priority, neighbor))
        came_from[neighbor] = current

  return None, float('inf')


