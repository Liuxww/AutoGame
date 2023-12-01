n = 5
nums = [[3, 1], [1, 1], [5, 1], [2, 0], [2, 0]]

res = 0
nums = sorted(nums, key=lambda x: -x[1])
zero = 0
for i in range(n-1, -1, -1):
    if nums[i][1] == 0:
        res += nums[i][0]
        zero += 1
    else:
        break
nums = sorted(nums[:5-zero], key=lambda x: -x[0])
for i in range(len(nums)):
    if nums[i][0] > res:
        res += nums[i][0]
    else:
        res *= 2

print(res)