# Mapeando Rotas Eficientes

## Visão Geral
O projeto **Mapeando Rotas Eficientes** implementa o algoritmo de Dijkstra para calcular os caminhos mais curtos em um grafo não dirigido que representa um sistema de logística. O objetivo é determinar as rotas mais curtas a partir de um ponto de origem escolhido pelo usuário (depósito central `D` ou pontos de entrega `A`, `B`, `C`, `E`, `F`) para todos os outros pontos de uma rede de entrega. As arestas do grafo possuem pesos que representam as distâncias entre os pontos.

Desenvolvido em Python, o projeto oferece uma interface interativa para seleção do vértice de origem, tornando-o flexível para diferentes cenários de logística. É ideal para aplicações em planejamento de rotas, otimização de transporte e logística.

## Funcionalidades
- **Algoritmo de Dijkstra**: Calcula os caminhos mais curtos a partir de um vértice de origem para todos os outros vértices.
- **Escolha Interativa do Ponto de Origem**: Permite ao usuário selecionar o vértice inicial (`D`, `A`, `B`, `C`, `E` ou `F`) via entrada de texto.
- **Grafo Não Dirigido**: Modela conexões bidirecionais entre o depósito e os pontos de entrega, com pesos baseados nas distâncias fornecidas.
- **Saída Clara**: Exibe uma tabela com o nome do vértice, a distância mínima e o caminho correspondente (ex.: `D -> A -> C`).
- **Tratamento de Erros**: Valida entradas do usuário e exibe "Infinito" para vértices inalcançáveis.

## Contexto do Problema
O projeto simula um cenário de logística onde um veículo parte de um ponto de origem (depósito `D` ou pontos de entrega `A`, `B`, `C`, `E`, `F`) e precisa alcançar outros pontos com o menor percurso possível. O grafo é definido pela seguinte matriz de adjacência:

- `D → A`: 2
- `D → B`: 4
- `A → B`: 3
- `A → C`: 1
- `B → E`: 2
- `C → F`: 4
- `E → F`: 3

O algoritmo de Dijkstra calcula as distâncias mínimas e os caminhos a partir do vértice de origem escolhido, fornecendo uma base para otimização de rotas.

## Pré-requisitos
- **Python 3.x**: O projeto foi desenvolvido e testado em Python 3.
- **Bibliotecas**: Apenas o módulo padrão `sys` é necessário.

## Instruções de Uso
1. **Baixe o Código**:
   - Copie o código para um arquivo local (ex.: `mapeando_rotas_eficientes.py`).
2. **Execute o Programa**:
   - No terminal, navegue até o diretório do arquivo e execute:
     ```bash
     python mapeando_rotas_eficientes.py
     ```
3. **Escolha o Ponto de Origem**:
   - O programa lista os vértices disponíveis: `0: D`, `1: A`, `2: B`, `3: C`, `4: E`, `5: F`.
   - Digite o número do vértice de origem (0 a 5).
4. **Visualize os Resultados**:
   - O programa exibe uma tabela com:
     - Nome do vértice de destino.
     - Distância mínima a partir da origem.
     - Caminho correspondente.
5. **Exemplo de Saída** (para origem `D`):
   Escolha o vértice de origem:
   0: D
   1: A
   2: B
   3: C
   4: E
   5: F
   Nos informe o número do vértice de origem (0 a 5): 0   Executando Dijkstra a partir de D:
   Vértice    Distância    Caminho
   D          0            D
   A          2            D -> A
   B          4            D -> B
   C          3            D -> A -> C
   E          6            D -> B -> E
   F          7            D -> A -> C -> F
