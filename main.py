from mapa import load_map, show_map
from search_a_star import search_a_star
from util import INITIAL_POSITION, FINAL_POSITION

def main():
  mapa = load_map("mapa_principal.txt")
  show_map(mapa)

  path, cost = search_a_star(mapa, INITIAL_POSITION, FINAL_POSITION)

  if path:
    print("\nCaminho encontrado:")
    for pos in path:
      print(pos, end=" -> ")
    print(f"\nCusto total: {cost}")
  else:
    print("Nenhum caminho encontrado.")

if __name__ == "__main__":
  main()