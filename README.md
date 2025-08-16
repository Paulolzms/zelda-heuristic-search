# Trabalho Prático - Busca Heurística: A Jornada de Link em Hyrule

## 🔎 Descrição do Problema

Este projeto implementa um agente autônomo para resolver o problema de busca heurística no universo do jogo *The Legend of Zelda*. O objetivo é guiar o herói Link em uma jornada de menor custo para reunir os três Pingentes da Virtude, que estão localizados em masmorras perigosas espalhadas pelo reino de Hyrule, e, em seguida, viajar para Lost Woods para encontrar a lendária Master Sword.

O desafio consiste em encontrar a melhor rota para visitar as masmorras e chegar ao destino final, considerando os diferentes custos de locomoção por terreno.

---

## 📦 Algoritmo e Funcionalidades

O projeto utiliza o algoritmo de busca heurística **A\*** para calcular a rota de menor custo. As principais funcionalidades implementadas são:

* **Agente Inteligente**: Capaz de se locomover de forma autônoma pelo mapa e pelas masmorras.
* **Busca Ótima**: O agente calcula a melhor rota para visitar as três masmorras e chegar ao seu destino. O problema é tratado de forma semelhante ao do Caixeiro Viajante para garantir o custo mínimo.
* **Custo de Terreno**: O custo de cada movimento é determinado pelo tipo de terreno do local de destino. Os custos são: Grama (`+10`), Areia (`+20`), Floresta (`+100`), Montanha (`+150`), e Água (`+180`).
* **Visualização no Console**: Uma interface simples que desenha o mapa no console e atualiza o movimento do agente em tempo real, deixando um rastro do caminho percorrido.
* **Mapas Configuráveis**: Os mapas podem ser facilmente editados em arquivos de texto.
* **Relatórios de Custo**: O programa exibe o custo do caminho percorrido e o custo total da jornada.

---

## ▶️ Como Rodar o Projeto

### 🐍 Pré-requisitos
* Python 3.x

### 📂 Estrutura de Arquivos
Certifique-se de que a estrutura de pastas e arquivos seja a seguinte:

```
zelda-heuristic-search/
├──docs/    # Documentação
│   └── util.py
├── src/    
│   ├── agent.py 
│   ├── app.py 
│   ├── mapa.py 
│   ├── search_a_star.py 
│   └── util.py
├── maps/    
│   ├── dungeon1.txt
│   ├── dungeon2.txt
│   ├── dungeon3.txt
│   └── hylure_map.txt    
└── README.md   # Este arquivo
```
### Execução

Para iniciar a jornada, basta executar o arquivo `app.py` a partir do terminal:

```sh
python app.py
```

---

### 📝 Descrição dos Arquivos

* **agent.py**: Contém a lógica principal do agente, incluindo as funções para calcular a melhor ordem de visita às masmorras (best_order) e construir o caminho completo (get_full_path). É o arquivo principal a ser executado.

* **search_a_star.py**: Implementa o algoritmo de busca heurística A* com uma fila de prioridade (heapq), responsável por encontrar o caminho de menor custo entre dois pontos.

* **mapa.py**: Gerencia a leitura dos arquivos de mapa e a visualização no console. Define as propriedades de cada tipo de terreno e inclui funções para animar o caminho do agente.

* **util.py**: Contém funções utilitárias, como a definição da posição inicial ([25, 28]) e final ([7, 6]), os movimentos permitidos (somente horizontal e vertical), e a heurística de distância de Manhattan.

* **maps/hyrule_map.txt**: Representação do mapa do reino de Hyrule, em uma matriz de 42x42.

* **maps/dungeon1.txt, maps/dungeon2.txt, maps/dungeon3.txt**: Representações dos mapas das masmorras, em matrizes de 28x28.

---

## 👨‍💻 Autor

**Paulo Luiz M. Souza**  
Universidade Federal de Ouro Preto  
João Monlevade - MG - Brasil

---

### 📃 Licença

Este projeto é acadêmico e não possui uma licença específica. Sinta-se livre para estudar, modificar e compartilhar para fins educacionais.
