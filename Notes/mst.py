'''

Minimum Spanning Trees:
    1. Input -> Connected undirected graph - G(V,E)
             -> Weight function w
             -> No constraint on weights like in Dijkstra
    2. Output -> A spanning tree contains all vertices and a subset of the edges


Greedy Choice Property:
    -> Locally optimal choices lead to a globally optimal solution


Steps for Kruskals:
    -> Sort the edges by weight
    -> Choose any edge with the smallest weight
    -> Put it in the tree we are building
    -> Successively consider the remaining edges in order of increasing weight
    -> Add edge to the tree if it doesnt create a cycle with edges already present in the tree (since a tree cannot have cycles)

Steps for Prims:
    -> Take a random vertex to be the root of the tree
    -> Look at the edges from this vertex and take the one with the cheapest cost (weight)
    -> Add this edge to the mst set


Cut Property:
    -> A cut in G=(V,E) is any partition of vertices V into two non empty sets, S and V - S

Theorem (Using Cut Property):
    -> For any cut (S, V - S) in a connected undirected weighted graph G = (V,E,w), any least-weight edge  e=(u,v) crossing the cut where u belongs to S and v belongs to V - S is in some MST of G.


'''
