def topo_util(graph, v, visited, stack):
    visited.add(v)
    for u in graph[v]:
        if u not in visited:
            visited, stack = topo_util(graph, u, visited, stack)
    stack.append(v)
    return visited, stack


def topo_sort(graph):
    visited = set()
    stack = []
    for v in graph:
        if v not in visited:
            visited, stack = topo_util(graph, v, visited, stack)
    return stack[::-1]



graph = {1:[2], 2:[1, 3], 3:[2, 4], 4:[3, 5], 5:[4]}
print(topo_sort(graph))
