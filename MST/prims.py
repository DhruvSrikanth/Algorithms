# Time Complexity - O (E log V)

import heapq

def prims(graph, root):
    mst = {}
    visited = set([root])
    pq = [(w, root, d) for d, w in graph[root].items()]
    heapq.heapify(pq)
    
    while pq:
        w, s, d = heapq.heappop(pq)
        if d not in visited:
            visited.add(d)
            if s not in mst:
                mst[s] = set()
            mst[s].add(d)
            for u, w in graph[d].items():
                if u not in visited:
                    heapq.heappush(pq, (w, d, u))
    return mst

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}

res = prims(graph, 'A')
for k in res:
    print(k, res[k])
