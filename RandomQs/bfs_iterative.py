def bfs(graph, root):
    visited = set([root])
    queue = [root]
    tree = []
    levels = {root:0}
    while queue:
        v = queue.pop(0)
        tree.append(v)
        for u in graph[v]:
            if u not in visited:
                queue.append(u)
                levels[u] = levels[v] + 1
                visited.add(u)
    return tree, levels

graph = {0: [1, 2], 1: [2], 2: [3], 3: [4], 4:[]}
bfs_tree, levels = bfs(graph, 0)
print(bfs_tree, levels)
