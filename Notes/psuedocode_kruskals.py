'''

# Time Complexity - O(E log E) for the sorting which can be written as O(E log V)
                  - O(V) for each edge from 1 to m
                  - O(VE) for checking if there is a cycle with the edges present in the MST set
                  - Results in O(VE) total time comlplexity for Kruskals algorithm

def Kruskals(G, m):
    # G is the graph
    # m is the number of edges
    
    sort the edges by weight (such that w(e1) <= w(e2) ... <= w(em))
    mst_set = empty set
    for i=1 to m:
       if ei does not create a cycle with edges present in mst_set:
         add ei to mst_set

    return mst_set


'''
