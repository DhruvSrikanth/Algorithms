'''

Graph Searching Algorithms:
    -> If graph G = (V,E), either an undirected or directed graph with source vertex s in V,
    -> Visit every vertex reachable from s
    -> If u is reachable from s and v in Adj[u], then v is reachable from s
    -> If u is reachable from s, then there exists a path s -> v1 -> v2 -> vk -> u
    -> This results in a path of length k+1 leading from s to u

'''
