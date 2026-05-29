# ──────────────────────────────────────────────
# Union-Find
# ──────────────────────────────────────────────
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


# ──────────────────────────────────────────────
# Kruskal
# ──────────────────────────────────────────────
def kruskal(n, edges):
    edges = sorted(edges, key=lambda x: x[2])

    uf = UnionFind(n)
    total = 0
    mst = []

    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total += w

    return total, mst

''' #### Pseudocódigo de Kruskal ####
// Entrada: Um grafo G = (V, E) onde V são os vértices e E são as arestas
// Saída: Uma Árvore Geradora Mínima (MST)

1. A = ∅                   // Inicializa o conjunto de arestas da solução
2. Para cada vértice v ∈ G.V faça:
3.     CRIAR-CONJUNTO(v)   // Cria conjuntos disjuntos para cada vértice

4. Ordenar as arestas de G.E em ordem crescente de seus pesos (w)

5. Para cada aresta (u, v) ∈ G.E (em ordem crescente de peso) faça
6.     Se BUSCAR-CONJUNTO(u) ≠ BUSCAR-CONJUNTO(v) então
7.         A = A ∪ {(u, v)}       // Adiciona a aresta à solução
8.         UNIR(u, v)             // Une os conjuntos dos vértices u e v

9. Retorna A
'''