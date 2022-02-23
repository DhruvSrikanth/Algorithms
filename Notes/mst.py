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

Proof:
    -> Let T be an MST of G. If T contains e = (u,v), the theorem has be proved. 
    -> If not, then since T is a tree, there exists a unique path between any two vertices in T in particular between u and v. Since u is in S and v is in V - S, this path contains some edge e'=(x,y) with x in S and y in V - S.
    -> If you add edge e = (u,v), this path and e form a cycle T Union {e}
    -> If you remove edge e', then the result is T - e' Union {e}
    -> T' = T - {(x,y)} Union {(u,v)} is a spanning tree
    -> T' must have the same weight as T
    -> w(T') = w(T) - w(e') + w(e)
    -> We know that w(e) <= w(e') therefore, w(T') <= w(T) by substituting w(e) in the previous equation
    -> Since T is a minimum spanning tree, w(T') = w(T)







'''
