def detect_cycle(graph, root):
    visited = set([root])
    queue = [root]
    parent = {root:-1}
    while queue:
        v = queue.pop(0)
        for u in graph[v]:
            if u in visited and parent[u] != v:
                return True
            if u not in visited:
                visited.add(u)
                parent[u] = v
                queue.append(u)
    return False

graph = {0:[1], 1:[2], 2:[0,3],3:[4],4:[]}
res = detect_cycle(graph, 0)
print(res)
