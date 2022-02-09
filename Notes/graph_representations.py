'''

Graph Representations:
    1. Adjacency list representation - 
    -> V (set of vertices)
    -> Array of |V| linked lists for each vertex v in V, Adj[v] = list of vertices adjacent to v
    -> This is good for a sparse graph (graph where |E| << |V^2|)
    -> Space Complexity - O(V + E)
    
    -> Adjacency Matrix - 
       -> Let A = aij = 1 if (i,j) is an edge in the graph, 0 otherwise
       -> Good for dense graphs (|E| approx = |V^2|)
       -> Space Complexity - O (V^2)
'''

