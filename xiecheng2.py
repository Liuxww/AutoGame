string = ['arc']

res = list()
n = len(string)


def backtravel(path, use):
    if len(path) == n:
        for i in range(n):
            if i > 0 and path[i] == path[i-1]:
                return
        res.append(path[:])
        return

    row_use = set()
    for i in range(n):
        if i in use or string[i] in row_use:
            continue
        # if len(use) > 0 and string[i] == path[-1]:
        #     continue
        path.append(string[i])
        use.add(i)
        row_use.add(string[i])
        backtravel(path, use)
        path.pop()
        use.remove(i)

use = set()
backtravel(list(), use)
print(len(res))