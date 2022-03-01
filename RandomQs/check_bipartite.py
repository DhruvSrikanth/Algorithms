def set_color(c):
    if c == 1:
        return -1
    else:
        return 1
    
def is_bip(graph, root):
    visited = set()
    queue = [root]
    colors = {root:1}
    while queue:
        v = queue.pop(0)
        for u in graph[v]:
            if u not in visited:
                queue.append(u)
                visited.add(u)
                colors[u] = set_color(colors[v])
            else:
                if colors[u] == colors[v]:
                    return False
    return True

graph = {1:[2], 2:[1, 3], 3:[2, 4], 4:[3, 5], 5:[4]}
print(is_bip(graph, 1))
