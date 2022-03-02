'''


Greedy Algorithm - Locally optimal solution leads to globally optimal solution.

Greedy Algorithm to find the maximum flow in a network:
    1. Find s to t directed path in G. Always choose max capacity edge.
    2. Find minimum capcity edge along the path c(p) = min{c(u,v), (u,v) on path}
    3. Assign f(e) = c(p) for all edges e on path
    4. Repeat until no directed s-t path remains in G.




'''
