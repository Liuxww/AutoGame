n = 6
start = [4, 1, 3, 2, 1, 2]
end = [4, 1, 3, 3, 2, 2]

book = []
for i in range(n):
    book.append([start[i], end[i]])
book.sort()
res = []
up = 0
down = 0

def backtravel(start_id, path, up, dowm):
    if len(path) == 3:
        res.append(path[:])
        return
    for i in range(start_id, n):
        if ((book[i][0] >= dowm and book[i][0] <= up) or (book[i][1] >= dowm and book[i][1] <= up)):
            continue
        if n-i < 3-len(path):
            return
        path.append(i)
        seen.append(book[i][0])
        seen.append(book[i][1])
        backtravel(i+1, path, seen)
        path.pop()
        seen.pop()
        seen.pop()

backtravel(0, list(), up, dowm)
print(len(res))