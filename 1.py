# # 最大子序和：
# #
# # 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# #
# # 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# # 输出：6
# # 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# import math
# nums = [2, 4, 6]
# # max_num = 0
# # for i in range(len(nums)):
# #     for j in range(i+1, len((nums))):
# #         total = sum(nums[i:j])
# #         if total > max_num:
# #             max_num = total
# # print(max_num)
# dp = [-math.inf] * len(nums)
# dp[0] = nums[0]
# for i in range(1, len(nums)):
#     dp[i] = max(dp[i-1]+nums[i], nums[i])
# print(max(dp))

# 给定一个非负整数数组，a1, a2, …, an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
#
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
#
# 示例 1:
#
# 输入: nums: [1, 1, 1, 1, 1], S: 3
# 输出: 5
# 解释:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 一共有5种方法让最终目标和为3。

nums = [1, 1, 1, 1, 1]
target = 3

sumvalue = sum(nums)

if abs(target) > sumvalue or (sumvalue + target) % 2 == 1:
    print(0)

size = (sumvalue + target) // 2
dp = [0] * (size + 1)
dp[0] = 1
for i in range(len(nums)):
    for j in range(size, nums[i]-1, -1):
        dp[j] += dp[j - nums[i]]

print(dp[size])
