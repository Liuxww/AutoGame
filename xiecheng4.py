n, x = 7, 2
nums = [3, 5, 50, 2, 80, 10**9, 10**9]

res = list()
chushu = 10 ** x

def backtravel(start, path):
    if len(path) == 2:
        num = path[0] * path[1]
        if num % chushu == 0:
            res.append(path[:])

    for i in range(start, n):
        path.append(nums[i])
        backtravel(i+1, path)
        path.pop()

backtravel(0, list())
print(len(res))