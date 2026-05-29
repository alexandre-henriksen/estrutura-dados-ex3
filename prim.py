import heapq

def prim(adj):

    n = len(adj)
    visitado = [False] * n
    heap = [(0, 0, -1)]  # (peso, nó, pai)

    total = 0
    mst = []

    while heap and len(mst) < n - 1:
        peso, u, pai = heapq.heappop(heap)

        if visitado[u]:
            continue

        visitado[u] = True
        total += peso

        if pai != -1:
            mst.append((pai, u, peso))

        for v, w in adj[u]:
            if not visitado[v]:
                heapq.heappush(heap, (w, v, u))

    return total, mst


''' #### Pseudocódigo do algoritmo de Prim ####
Algoritmo Prim(Grafo G, Peso w, Raiz r)
Para cada vértice u em G.V
    u.chave = INFINITO
    u.pai = NULO

r.chave = 0
Q = G.V // Fila de prioridade com todos os vértices do grafo

Enquanto Q não estiver vazia
    u = Extrair-Min(Q) // Vértice com a menor chave na fila
    
    Para cada vértice v na lista de adjacências de u
        Se v está em Q e w(u, v) < v.chave
            v.pai = u
            v.chave = w(u, v) // Atualiza o custo mínimo para conectar o vértice v
'''