def isCycleExist(graph):
    in_degree=[0]*len(graph)
    for v in range(len(graph)):
        for u in graph[v]:
            in_degree[u] += 1
    
    queue = []
    for v in range(len(graph)):
        if in_degree[v] == 0:
            queue.append(v)
    
    cnt = 0
    while queue:
        v = queue.pop(0)
        for u in graph[v]:
            in_degree[u] -= 1
            if in_degree[u] == 0:
                queue.append(u)
        cnt += 1

    return not cnt == n
