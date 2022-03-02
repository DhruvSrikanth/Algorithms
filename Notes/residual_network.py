'''

Residual Network - 
Given a flow f on a network G = (V, E), for each pair of vertices u,v in V, the residual capacity c_f(u,v) = c(u,v) - f(u,v) if (u,c) if (u,v) in E, c_f(u,v) = f(u,v) if (v,u) in E and 0 otherwise.

Let f be a flow on a network G = (V, E), the residual graph G_f = (V, E_f), E_f = {(u,v) in VxV given C_f(u,v) > 0}


Forward Edges - 
For each edge (u,v) for which f(u,v) < c(u,v), create an edge (u,v) in G_f, with a capacity c_f(u,v) = c(u,v) - f(u,v).

Backward Edges - 
For each edge (u,v) for which f(u,v) > 0, create an edge (v,u) in G_f, with a capacity c_f(u,v) = f(u,v).


'''
