from mapa import load_map, animate_path
from search_a_star import search_a_star
from agent import best_order, get_full_path, DUNGEON_EXITS, DUNGEON_PINGS
from util import INITIAL_POSITION, FINAL_POSITION

def main():
  mapa = load_map("mapa_principal.txt")

  print("Calculando a melhor sequência de masmorras...")
  best_order_result, best_cost = best_order(mapa)

  # Visualização animada
  if best_order_result:
    print("\n\nVisualizando o caminho da jornada:")
    best_path_result = get_full_path(mapa, best_order_result)
    if best_path_result:
      animate_path(mapa, best_path_result, INITIAL_POSITION, FINAL_POSITION)
    else:
      print("Não foi possível encontrar o caminho da jornada.")
  else:
    print("Não foi possível encontrar a melhor sequência de masmorras.")

  print("\nJornada completa!")
  print(f"A melhor sequência de masmorras é: {best_order_result}")
  print(f"O custo total da jornada é: {best_cost}")

  choice = input("\\nDeseja visualizar os caminhos dentro das masmorras? (s/n): ").lower()
  
  if choice == 's':
    for dungeon_file in best_order_result:
      dungeon_map = load_map(dungeon_file)
      dungeon_exit = DUNGEON_EXITS[dungeon_file]
      ping_pos = DUNGEON_PINGS[dungeon_file]

      path_to_ping, oneway_cost = search_a_star(dungeon_map, dungeon_exit, ping_pos)
      path_back, return_cost = search_a_star(dungeon_map, ping_pos, dungeon_exit)

      if path_to_ping and path_back:
        full_dungeon_path = path_to_ping + path_back

        print("\n\nVisualizando o caminho da jornada:")
        if full_dungeon_path:
          animate_path(dungeon_map, full_dungeon_path, DUNGEON_EXITS[dungeon_file], DUNGEON_PINGS[dungeon_file])
          print(f"\nCusto da ida e volta da masmorra {dungeon_file}: {oneway_cost + return_cost}")
          choice = input("\n\nDeseja visualizar os caminhos dentro das outras masmorras? (s/n): ").lower()
          if choice == 's':
            continue
          else:
            break
        else:
          print("Não foi possível encontrar o caminho da jornada.")



if __name__ == "__main__":
  main()