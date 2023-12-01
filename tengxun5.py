n = 6
w = [2, 2, 3, 4, 5, 6]
nums = [[1, 2, 2], [1, 3, 1], [3, 4, 5], [3, 5, 10], [3, 6, 4]]
graph = dict()
for item in nums:
    if item[0] not in graph:
        graph[item[0]] = [[item[1], item[2]]]
    else:
        graph[item[0]].append([item[1], item[2]])
for item in nums:
    if item[1] not in graph:
        graph[item[1]] = [[item[0], item[2]]]
    else:
        graph[item[1]].append([item[0], item[2]])
res = list()
resum = list()
def backtravel(i, path, next_node, seen, resum):
    for node in next_node:
        next_node = node[-2]
        dist = node[-1]
        resum.append(next_node)
        if next_node not in graph or next_node in seen:
            res.append(sum(path) + w[i - 1] + w[resum[-2] - 1])
            return
        if next_node in graph and next_node not in seen:
            seen.append(next_node)
            path.append(dist)
            backtravel(i, path, graph[next_node], seen, resum)
            seen.pop()
            path.pop()


for i in range(1, n+1):
    seen = list()
    seen.append(i)
    backtravel(i, list(), graph[i], seen, resum)
print(max(res))