n = 8

# i = 0
#
#
# def func(n):
#     global i
#     i += 1
#     if n <= 3:
#         return 1
#     else:
#         return func(n - 1) + func(n - 2) + func(n - 3)
#         a = func(n)
# print(a % 1000000007)
# import functools
#
# mod = 10 ** 9 + 7
#
#
# @functools.lru_cache(None)
# def func(n):
#     if n <= 3:
#         return 1
#     else:
#         return (func(n - 1) + func(n - 2) + func(n - 3)) % mod
#
#
# print(func(n))
#
#
#
# dp = [0] * n
# dp[0], dp[1], dp[2] = 1, 1, 1
# for i in range(3, n):
#     dp[i] = (1+dp[i-1]+dp[i-2]+dp[i-3])%mod
#
# print(dp[-1]%mod)
from collections import deque

mod = 10 ** 9 + 7
dp = deque()
for i in range(3):
    dp.append(1)
for i in range(3, n):
    dp.append(1 + dp[0] + dp[1] + dp[2])
    dp.popleft()

print(dp[-1]%mod)