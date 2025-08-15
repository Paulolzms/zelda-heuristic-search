from mapa import load_map, show_map
from search_a_star import search_a_star
from agent import best_order, get_full_path, DUNGEON_EXITS, DUNGEON_PINGS
from util import INITIAL_POSITION, FINAL_POSITION

def main():
  mapa = load_map("mapa_principal.txt")
  # show_map(mapa)

  # path, cost = search_a_star(mapa, INITIAL_POSITION, FINAL_POSITION)

  # if path:
  #   print("\nCaminho encontrado:")
  #   for pos in path:
  #     print(pos, end=" -> ")
  #   print(f"\nCusto total: {cost}")
  # else:
  #   print("Nenhum caminho encontrado.")


  print("Calculando a melhor sequência de masmorras...")
  best_order_result, best_cost = best_order(mapa)
  print(f"A melhor sequência de masmorras é: {best_order_result}")
  print(f"O custo total da jornada é: {best_cost}")

  print("\nVisualizando o caminho da jornada:")
  full_path = get_full_path(mapa, best_order_result)
  if full_path:
    for pos in full_path:
      print(pos, end=" -> ")
  else:
    print("Não foi possível encontrar o caminho da jornada.")

  for dungeon_file in best_order_result:
    dungeon_map = load_map(dungeon_file)
    dungeon_exit = DUNGEON_EXITS[dungeon_file]
    ping_pos = DUNGEON_PINGS[dungeon_file]

    path_to_ping, oneway_cost = search_a_star(dungeon_map, dungeon_exit, ping_pos)
    path_back, return_cost = search_a_star(dungeon_map, ping_pos, dungeon_exit)

    if path_to_ping and path_back:
      print(f"\nCusto da ida da masmorra {dungeon_file}: {oneway_cost}")
      print(f"Custo da volta da masmorra {dungeon_file}: {return_cost}")
      full_dungeon_path = path_to_ping + path_back
      print(f"\nCaminho da masmorra {dungeon_file}:")
      for pos in full_dungeon_path:
        print(pos, end=" -> ")
    else:
      print(f"Não foi possível encontrar o caminho da masmorra {dungeon_file}.")

if __name__ == "__main__":
  main()