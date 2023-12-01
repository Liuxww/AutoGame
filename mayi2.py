n = 5
nums = [2, 3, 4, 4, 2]

# res = list()

# def backtravel(start, path, nums, flag):
#     if len(path) >= 1:
#         res.append(path[:])
#     if start > len(nums):
#         return
#
#     use = set()
#     for i in range(start, len(nums)):
#         if i > 0 and nums[i] in use:
#             continue
#         if not path or nums[i] > path[-1]:
#             path.append(nums[i])
#             use.add(nums[i])
#             backtravel(i+1, path, nums)
#             path.pop()
# backtravel(0, list(), nums)
#
# print(res)
res = [0] * n
res[0] = n
def isup(nums):
    for j in range(1, len(nums)):
        if nums[j] <= nums[j - 1]:
            return False
    return True
for i in range(2, n+1):
    left = 0
    right = i
    while right < n:
        if isup(nums[left:right]):
            res[i-1] += 1
        right += 1
        left += 1


print(res)