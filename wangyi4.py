n, k = 5, 2
nums = [2, 3, 4, 6, 5]

left = 0
right = k
max_num = 0
while right <= len(nums):
    res = nums[left]
    for i in range(1, k):
        res &= nums[left + i]
    if res > max_num:
        max_num = res
    left += 1
    right += 1
print(max_num)