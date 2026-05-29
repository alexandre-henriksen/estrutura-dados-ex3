import heapq

def dijkstra(n, adj, origem=0, destino=None):
    
    if destino is None:
        destino = n - 1

    dist = [float('inf')] * n
    dist[origem] = 0

    heap = [(0, origem)]

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]:
            continue

        if u == destino:
            return dist[u]

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist[destino]