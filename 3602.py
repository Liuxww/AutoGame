n, m = 3, 3
u = [1, 1, 2]
v = [2, 3, 3]
w = [885, 513, 817]

import math
import heapq

nodes = list()
for i in range(2, n+1):
    nodes.append(i)

graph = dict()
for i in range(m):
    if u[i] not in graph:
        graph[u[i]] = [[v[i], w[i]]]
    else:
        graph[u[i]].append([v[i], w[i]])
    if v[i] not in graph:
        graph[v[i]] = [[u[i], w[i]]]
    else:
        graph[v[i]].append([u[i], w[i]])

# def init_distance(graph, s):
#     distance = {s: 0}
#     for vertex in graph:
#         if vertex != s:
#             distance[vertex] = math.inf
#
#     return distance
#
# def bfs(g, x):
#     pqueue = []
#     heapq.heappush(pqueue, (0, x))
#     seen = set()
#     parent = {x: None}
#     distance = init_distance(graph, x)
#     while len(pqueue) > 0:
#         pair = heapq.heappop(pqueue)
#         dist = pair[0]
#         vertex = pair[1]
#         seen.add(vertex)
#
#         node = graph[vertex]
#         for n in node:
#             w, d = n[0], n[1]
#             if w not in seen:
#                 if dist + d < distance[w]:
#                     heapq.heappush(pqueue, (dist + d, w))
#                     parent[w] = vertex
#                     distance[w] = dist + d
#     return parent, distance
#
# p, d = bfs(graph, 1)
# print(p)
# print(d)
res = []
key = 1
seen = set()

def bfs(key, res):
    cur = graph[key]
    seen.add(key)
    cur = sorted(cur, key=lambda x:x[1])
    for i in range(len(cur)):
        if cur[i][0] not in seen:
            pink = cur[i]
            break
    res.append(pink[1])
    key = pink[0]
    nodes.remove(key)
    
bfs(key, res)
print(res)