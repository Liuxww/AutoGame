# nums = [[2, 8], [9, 10], [4, 7], [2, 5], [5, 7], [3, 6], [1, 4], [6, 9], [7, 8], [4, 6]]
nums = [[2, 5], [8, 9]]

maxnums = list()
maxnum = 1

res = []
nums.sort(key=lambda x: x[0])
res.append(nums[0])
for i in range(1, len(nums)):
    last = res[-1]
    if nums[i][0] <= last[1]:
        res[-1] = [max(last[0], nums[i][0]), min(nums[i][1], last[1])]
        maxnum += 1
    else:
        maxnums.append(maxnum)
        res.append(nums[i])
        maxnum = 1
maxnums.append(maxnum)
print(max(maxnums))