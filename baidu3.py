qipan = ['red', 'der', 'rdr']
import math
import heapq
n, m = 3, 3
graph = dict()
for i in range(len(qipan)):
    for j in range(len(qipan[0])):
        if qipan[i][j] not in graph:
            graph[i*m+j] = list()
        if qipan[i][j] == 'r':
            if j-1 >= 0 and qipan[i][j-1] != 'd' and (i*m+j-1) > 0:
                graph[i*m+j].append(i*m+j-1)
            if j+1 < m and qipan[i][j+1] != 'd' and (i*m+j+1) > 0:
                graph[i*m+j].append(i*m+j+1)
            if i-1 >= 0 and qipan[i-1][j] != 'd' and ((i-1)*m+j) > 0:
                graph[i*m+j].append((i-1)*m+j)
            if i+1 < n and qipan[i+1][j] != 'd' and ((i+1)*m+j) > 0:
                graph[i*m+j].append((i+1)*m+j)
        if qipan[i][j] == 'e':
            if j-1 >= 0 and qipan[i][j-1] != 'r' and (i*m+j-1) > 0:
                graph[i*m+j].append(i*m+j-1)
            if j+1 < m and qipan[i][j+1] != 'r' and (i*m+j+1) > 0:
                graph[i*m+j].append(i*m+j+1)
            if i-1 >= 0 and qipan[i-1][j] != 'r' and ((i-1)*m+j) > 0:
                graph[i*m+j].append((i-1)*m+j)
            if i+1 < n and qipan[i+1][j] != 'r'  and ((i+1)*m+j) > 0:
                graph[i*m+j].append((i+1)*m+j)
        if qipan[i][j] == 'd':
            if j-1 >= 0 and qipan[i][j-1] != 'e' and (i*m+j-1) > 0:
                graph[i*m+j].append(i*m+j-1)
            if j+1 < m and qipan[i][j+1] != 'e' and (i*m+j+1) > 0:
                graph[i*m+j].append(i*m+j+1)
            if i-1 >= 0 and qipan[i-1][j] != 'e' and ((i-1)*m+j) > 0:
                graph[i*m+j].append((i-1)*m+j)
            if i+1 < n and qipan[i+1][j] != 'e' and ((i+1)*m+j) > 0:
                graph[i*m+j].append((i+1)*m+j)

def init_dist(graph, s):
    distance = {s: 0}
    for v in graph:
        if v != s:
            distance[v] = math.inf
    return distance

def bfs(npp, x):
    pqueue = []
    heapq.heappush(pqueue, (0, x))
    seen = set()
    parent = {x: None}
    distence = init_dist(graph, x)
    while (len(pqueue) > 0):
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                if dist + 1 < distence[w]:
                    heapq.heappush(pqueue, (dist + 1, w))
                    parent[w] = vertex
                    distence[w] = dist + 1
    return parent, distence

p, d = bfs(graph, 0)
end = n*m-1
print(d[end])