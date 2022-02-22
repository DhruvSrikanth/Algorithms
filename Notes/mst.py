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


'''
