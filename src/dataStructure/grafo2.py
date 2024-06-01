
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacencia = [[] for _ in range(vertices)]

    def adicionar_aresta(self, origem, destino):
        self.adjacencia[origem].append(destino)
        self.adjacencia[destino].append(origem)  # grafo não direcionado

    def existe_caminho_para_todos(self):
        for origem in range(self.vertices):
            visitados = [False] * self.vertices
            self.dfs(origem, visitados)
            if not all(visitados):
                return False
        return True

    def dfs(self, vertice, visitados):
        visitados[vertice] = True
        for vizinho in self.adjacencia[vertice]:
            if not visitados[vizinho]:
                self.dfs(vizinho, visitados)

def main():
    vertices = int(input("Digite o número de vértices: "))
    arestas = int(input("Digite o número de arestas: "))
    grafo = Grafo(vertices)

    print("Digite as arestas no formato 'origem destino':")
    for _ in range(arestas):
        origem, destino = map(int, input().split())
        grafo.adicionar_aresta(origem, destino)

    if grafo.existe_caminho_para_todos():
        print("Existe um caminho de um vértice para todos os outros vértices.")
    else:
        print("Não existe um caminho de um vértice para todos os outros vértices.")

if __name__ == "__main__":
    main()


