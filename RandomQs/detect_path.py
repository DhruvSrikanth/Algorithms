def path_exists(graph, source, destination):
    visited = set()
    queue = [source]
    visited.add(source)
    while queue:
        v = queue.pop(0)
        if v == destination:
            return True
        for u in graph[v]:
            if u not in visited:
                visited.add(u)
                queue.append(u)
    return False

graph = {1:[2], 2:[1, 3], 3:[2, 4], 4:[3, 5], 5:[4], 6:[]}
print(path_exists(graph, 1, 6))
