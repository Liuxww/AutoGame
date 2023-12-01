string = 'ababa'

res = list()

def backtravel(start, path, nums):
    if len(path) > 1 and len(path)% 2 == 0:
        res.append(path[:])
    if start > len(nums):
        return

    for i in range(start, len(nums)):
        path.append(nums[i])
        backtravel(i+1, path, nums)
        path.pop()
backtravel(0, list(), string)

print(res)
result = 0
for item in res:
    temp = ord(item[0])
    for i in range(1, len(item)):
        temp = temp^ord(item[i])
    if temp == 0:
        result += 1
print(result)