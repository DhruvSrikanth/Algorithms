'''

Time Complexity - O(V) for initialization
                - O(V) for inserting all vertices in to the queue Q
                - O(V*(insert + extract_min) + 2E*decrease_key)), each function using a min heap can be done in log V time
                - Total time complexity = O(V log V + E log V)

def Prim(G, w, r):
    # G is in the adjacency list format
    # r belongs to V
    for each u in V:
       key[u] = inf
       parent[u] = None
       color[u] = while => 0
    key[r] = 0
    color[r] = black => 1
    Q = V
    while Q is not empty:
         u = extract_min(Q)
         color[u] = black => 1
         for each v in G[u]:
            if color[v] == white AND w[u,v] < key[v]:
              parent[v] = u
              key[v] = w[u,v]




'''
