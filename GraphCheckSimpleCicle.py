class Grafo:

    # Estrutura do grafo
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        # estrutura para grafos direcionados simples
        self.grafo[u - 1][v - 1] = 1  # trocar = por += ser for grafo múltiplo

    # self.grafo[v-1][u-1] = 1 (caso o grafo não seja direcionado)

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print("(", i + 1, ")", " ", self.grafo[i])

    def is_simple_cicle(self):
        raiz = 0
        for i in range(self.vertices):
            for j in range(len(self.grafo[i])):
                if raiz == 0:
                    if self.grafo[i][j] > 0:
                        raiz = self.grafo[i][j]
                if len(self.grafo[i]) - 1 == i:
                    if self.grafo[i][0] > 0:
                        return True
                    else:
                        return False

    def is_passeio(self):
        vertices = 0
        if len(self.grafo) > 0:
            for i in range(len(self.grafo)):
                for j in range(len(self.grafo[i])):
                    if self.grafo[i][j] > 0:
                        vertices += 1
            if vertices >= 1:
                return True
            else:
                return False

    def is_trilha(self):
        for i in range(len(self.grafo)):
            for j in range(len(self.grafo[i])):
                if self.grafo[i][j] > 0:
                    v = i
                    u = j
                    if self.grafo[u][v] > 0:
                        return True
                    else:
                        return False


g = Grafo(4)
g.adiciona_aresta(1, 2)
g.adiciona_aresta(2, 3)
g.adiciona_aresta(3, 4)
g.adiciona_aresta(4, 1)
g.mostra_matriz()

print("É um ciclo? ", g.is_simple_cicle())
print("É um passeio? ", g.is_passeio())
print("É uma trilha? ", g.is_trilha())
