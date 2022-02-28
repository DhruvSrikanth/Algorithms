# Time Complexity - O (E log V) using heap


import heapq as heap

def dijkstra(G, root):
	visited = set()
	parent = {}
	
	distance = {}
	for v in G:
	    distance[v] = float('inf')
	distance[root] = 0
	
	pq = []
	heap.heappush(pq, (0, root))
 
	while pq:
		_, v = heap.heappop(pq)
		visited.add(v)
		for u, weight in G[v].items():
			new_cost = distance[v] + weight
			if u not in visited and new_cost < distance[u]:
			    distance[u] = new_cost
			    parent[u] = v
			    heap.heappush(pq, (new_cost, u))

	return parent, distance


G = {1:{2:4,
        3:4},
     2:{1:4,
        3:2},
     3:{1:4,
        2:2,
        4:3,
        5:6,
        6:1},
     4:{3:3,
        5:2},
     5:{4:2,
        3:6,
        6:3},
     6:{3:1,
        5:3}}

source = 1
p, d = dijkstra(G, source)
print(p)
print(d)

def backtrack(parent, target):
    path = "{}".format(target)
    while True:
        step = p[target]
        path += ("-" + str(step))
        if step == source:
            break
        target = step
    return path[::-1]

target = 4
path = backtrack(parent, target)
print(path)

