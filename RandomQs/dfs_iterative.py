def dfs(graph, root):
    visited = set([root])
    stack = [root]
    tree = []
    levels = {root:0}
    while stack:
        v = stack.pop(0)
        tree.append(v)
        for u in graph[v]:
            if u not in visited:
                stack.insert(0, u)
                levels[u] = levels[v] + 1
                visited.add(u)
    return tree, levels


graph = {0: [1, 2], 1: [2], 2: [3], 3: [4], 4:[]}
dfs_tree, levels = dfs(graph, 0)
print(dfs_tree, levels)
