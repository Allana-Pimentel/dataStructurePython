class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacencia = [[0] * vertices for _ in range(vertices)]

    def adicionar_estrada(self, cidade_origem, cidade_destino, distancia):
        self.adjacencia[cidade_origem][cidade_destino] = distancia
        self.adjacencia[cidade_destino][cidade_origem] = distancia  # grafo não direcionado

    def matriz_adjacencia_com_distancias(self):
        print("Matriz de Adjacência com Distâncias:")
        for linha in self.adjacencia:
            print(" ".join(map(str, linha)))

    def existe_caminho_para_todas_cidades(self):
        for cidade_origem in range(self.vertices):
            distancias = self.dijkstra(cidade_origem)
            if None in distancias:
                return False
            print(f"\nDistâncias a partir da cidade {cidade_origem}:")
            for cidade_destino, distancia in enumerate(distancias):
                print(f"Até a cidade {cidade_destino}: {distancia} km")
        return True

    def dijkstra(self, cidade_origem):
        visitados = [False] * self.vertices
        distancias = [float('inf')] * self.vertices
        distancias[cidade_origem] = 0

        for _ in range(self.vertices):
            menor = float('inf')
            menor_indice = -1

            for i in range(self.vertices):
                if not visitados[i] and distancias[i] < menor:
                    menor = distancias[i]
                    menor_indice = i

            if menor_indice == -1:
                break

            visitados[menor_indice] = True

            for i in range(self.vertices):
                if (not visitados[i] and self.adjacencia[menor_indice][i] != 0 and
                        distancias[menor_indice] + self.adjacencia[menor_indice][i] < distancias[i]):
                    distancias[i] = distancias[menor_indice] + self.adjacencia[menor_indice][i]

        return distancias

def main():
    num_cidades = int(input("Digite o número de cidades: "))
    grafo = Grafo(num_cidades)

    print("Digite as estradas no formato 'cidade_origem cidade_destino distancia (em km)':")
    while True:
        estrada = input("Estrada (ou 'fim' para terminar): ").strip().lower()
        if estrada == 'fim':
            break
        origem, destino, distancia = map(int, estrada.split())
        grafo.adicionar_estrada(origem, destino, distancia)

    grafo.matriz_adjacencia_com_distancias()

    if grafo.existe_caminho_para_todas_cidades():
        print("\nExiste um caminho de uma cidade para todas as outras cidades.")
    else:
        print("\nNão existe um caminho de uma cidade para todas as outras cidades.")

if __name__ == "__main__":
    main()

