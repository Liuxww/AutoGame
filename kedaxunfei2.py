N = 3
L, R = 10, 15
nums = [10, 20, 5]

upR = 0
downL = 0
inLRdownR = 0
inLRupL = 0
for i in range(N):
    if nums[i] > R:
        upR += nums[i] - R
    elif nums[i] < L:
        downL += L - nums[i]
    else:
        inLRdownR += R - nums[i]
        inLRupL += nums[i] - L

ans = 0
if upR > downL:
    ans += downL
    upR -= downL
    if upR > inLRdownR:
        ans = -1
    else:
        ans += upR
elif upR < downL:
    ans += upR
    downL -= upR
    if downL > inLRupL:
        ans = -1
    else:
        ans += upR
else:
    ans += upR

print(ans)