import os
import time
import sys
import heapq

# ──────────────────────────────────────────────
# Configurações
# ──────────────────────────────────────────────

from config import CAMINHO_DIJ10
from config import CAMINHO_DIJ20
from config import CAMINHO_DIJ40
from config import CAMINHO_DIJ50
from config import OUTPUT_DIR
from kruskal import kruskal
from prim import prim
from dijkstra import dijkstra

# ──────────────────────────────────────────────
# Utilitários
# ──────────────────────────────────────────────
def ler_grafo_triangular(caminho_arquivo):
    edges = []

    with open(caminho_arquivo, "r") as f:
        linhas = f.readlines()

    n = int(linhas[0].strip())

    for i in range(n - 1):
        valores = list(map(int, linhas[i + 1].split()))
        
        for k, peso in enumerate(valores):
            j = i + k + 1
            edges.append((i, j, peso))

    return n, edges

def edges_para_adjacencia(n, edges):
    adj = [[] for _ in range(n)]

    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))  # grafo não direcionado

    return adj

def salvar_resultados_txt(resultados):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    caminho_saida = os.path.join(OUTPUT_DIR, "resultados.txt")

    with open(caminho_saida, "w", encoding="utf-8") as f:

        for problema, dados in resultados.items():

            # título do problema (usa a chave diretamente)
            f.write(f"Problema: {problema}\n")

            f.write("Instância - solução\n")

            for instancia, valor in dados.items():
                f.write(f"{instancia} - {valor}\n")

            f.write("\n")  # linha em branco entre blocos

# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────
def main():
    
    # 1. teste inicial
    n, edges = ler_grafo_triangular(CAMINHO_DIJ10)

    total, mst = kruskal(n, edges)

    print("Caminho:", CAMINHO_DIJ10)
    print("Custo MST:", total)
    print("Arestas na MST:", len(mst))
    print("Arestas da MST:")
    for u, v, w in mst:
        print(f"{u} - {v} (peso: {w})")
    print("OK!!! FUNCIONA!!!")

    # 2. Produção de resultados para as instâncias
         
    instancias = [
        ("dij10", CAMINHO_DIJ10),
        ("dij20", CAMINHO_DIJ20),
        ("dij40", CAMINHO_DIJ40),
        ("dij50", CAMINHO_DIJ50),
    ]

    ## 2.1. Kruskal
    resultados = {
        "Arvore de espalhamento minimo (MSTP) - Kruskal": {}
    }
   
    for nome, caminho in instancias:
        
        n, edges = ler_grafo_triangular(caminho)
        total, mst = kruskal(n, edges)

        resultados["Arvore de espalhamento minimo (MSTP) - Kruskal"][nome] = total
    
    print("\nResultados finais Kruskal:")
    print(resultados)

    ## 2.2. Prim
    resultados["Arvore de espalhamento minimo (MSTP) - Prim"] = {}

    for nome, caminho in instancias:
        
        n, edges = ler_grafo_triangular(caminho)
        adj = edges_para_adjacencia(n, edges)

        total, mst = prim(adj)

        resultados["Arvore de espalhamento minimo (MSTP) - Prim"][nome] = total
    
    print("\nResultados finais Prim:")
    print(resultados)   

    ## 2.3. Dijkstra
    resultados["Caminho minimo (Dijkstra)"] = {}

    for nome, caminho in instancias:
        
        n, edges = ler_grafo_triangular(caminho)
        adj = edges_para_adjacencia(n, edges)

        dist_destino = dijkstra(n, adj, 0, n-1)

        resultados["Caminho minimo (Dijkstra)"][nome] = dist_destino
    
    print("\nResultados finais Dijkstra:")
    print(resultados)

    salvar_resultados_txt(resultados)  


if __name__ == "__main__":
    main()
