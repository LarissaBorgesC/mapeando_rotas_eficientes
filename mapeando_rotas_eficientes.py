import sys

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0]* vertex for _ in range(vertex)]
        self.vertex_names = ["D", "A", "B", "C", "E", "F"]

    def insert_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def shortest_distance(self, distances, visited):
        min_dist = sys.maxsize
        min_vertex = -1
        for v in range(self.V):
            if distances[v] < min_dist and not visited[v]:
                min_dist = distances[v]
                min_vertex = v
        return min_vertex
    
    def shortest_path(self, predecessors, j):
        if predecessors[j] == -1:
            print(self.vertex_names[j], end="")
            return
        self.shortest_path(predecessors, predecessors[j])
        print(f" -> {self.vertex_names[j]}", end="")
        
    def dijkstra(self, origem):
        distances = [sys.maxsize] * self.V
        distances[origem] = 0
        visited = [False] * self.V
        predecessors = [-1] * self.V

        for _ in range(self.V):
            u = self.shortest_distance(distances, visited)
            if u == -1:
                break
            visited[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == False and distances[v] > distances[u] + self.graph[u][v]:
                    distances[v] = distances[u] + self.graph[u][v]
                    predecessors[v] = u
        print("Vértice\tDistância\tCaminho")

        for i in range(self.V):
            distance = distances[i] if distances[i] != sys.maxsize else "Infinito"
            print(f"{self.vertex_names[i]}\t\t{distance}\t\t", end="")
            self.shortest_path(predecessors, i)
            print()

def main(vertex_names):
    print("Escolha o vértice de origem:")
    for i, name in enumerate(vertex_names):
        print(f"{i}: {name}")
    while True:
        try:
            choice = input("Nos informe o número do vértice de origem (0 a 5): ")
            origem = int(choice)
            if 0 <= origem < len(vertex_names):
                return origem
            else:
                print(f"Por favor, escolha um número entre 0 e {len(vertex_names)-1}.")
        except ValueError:
            print("Entrada inválida! Nos informe um número válido.")


g = Graph(6)

g.insert_edge(0, 1, 2) 
g.insert_edge(0, 2, 4)  
g.insert_edge(1, 2, 3)  
g.insert_edge(1, 3, 1)  
g.insert_edge(2, 4, 2)  
g.insert_edge(3, 5, 4)  
g.insert_edge(4, 5, 3)  


origem = main(g.vertex_names)


print(f"\nExecutando Dijkstra a partir de {g.vertex_names[origem]}:")
g.dijkstra(origem)