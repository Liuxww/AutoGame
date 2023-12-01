n = 6
nums = [7, 9, 5, 11, 2, 8]

def prmeNUM(min, max):
    zhishu = []
    if min == 1:
        min += 1
    for i in range(min, max +1):
        for j in range(2, i+1):
            if i%j == 0:
                break
        if j == i:
            zhishu.append(i)
    return zhishu
zs = prmeNUM(min(nums), max(nums))
# print(zs)
number = 10**6
for i in zs:
    opter = 0
    # if len(prmeNUM(i, i)) == 0:
    #     continue
#     # target_idx = zs.index(i)
    for j in nums:
        if len(prmeNUM(j, j)) != 0:
#             source_idx = zs.index(j)
            opter += len(prmeNUM(min([i, j]), max([i, j]))) - 1
        else:
            opter += len(prmeNUM(min([i, j]), max([i, j])))
        #     if j > i:
        #         while len(prmeNUM(j, j)) != 0:
        #             j -= 1
        #         # source_idx = zs.index(j)
        #         opter += len(prmeNUM(min([i, j]), max([i, j])))
        #     elif j < i:
        #         while len(prmeNUM(j, j)) != 0:
        #             j += 1
        #         # source_idx = zs.index(j)
        #         opter += len(prmeNUM(min([i, j]), max([i, j])))
    if opter < number:
        number = opter
print(number)