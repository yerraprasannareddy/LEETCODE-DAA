import heapq
def prim_mst(graph):
    n = len(graph)   
    in_mst = [False] * n
 
    pq = []
    
    mst = []
    total_weight = 0
 
    heapq.heappush(pq, (0, 0))   

    while pq:
        weight, u = heapq.heappop(pq)
 
        if in_mst[u]:
            continue
 
        in_mst[u] = True
        total_weight += weight
 
        if weight != 0:
            mst.append((u, weight))
 
        for v in range(n):
            if graph[u][v] != 0 and not in_mst[v]:
                 
                heapq.heappush(pq, (graph[u][v], v))

    return mst, total_weight

if __name__ == "__main__":
   
    graph = [[0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0]]
 
    mst, total_weight = prim_mst(graph)

    print("Edges in the MST and their weights:")
    for edge in mst:
        print(f"Edge: {edge[0]}, Weight: {edge[1]}")

    print(f"Total weight of the MST: {total_weight}")
