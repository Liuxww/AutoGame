nums = [5, 1, 8, 3, 12, 30, 4, 14]

dp = [0] * len(nums)
dp[0] = nums[0]
for i in range(1, len(nums)):
    dp[i] = max(dp[i-1], dp[i-2]+nums[i])

print(dp)