n, m, k = 3, 4, 12

num = 1
youpiao = list()
youpiao.append([n, m])
res = 0
while num < k:
    sort1 = sorted(youpiao, key=lambda x:-x[0])
    sort2 = sorted(youpiao, key=lambda x:-x[1])
    if sort1[-1][0] < sort2[-1][1]:
        bian = sort1[-1][0]
        chang = sort1[-1][1]
        sort1.pop()
        youpiao = sort1
        res += bian ** 2
        num += 1
        if bian !=1 or chang-1 != 1:
            youpiao.append([bian, chang-1])
        if bian != 1:
            youpiao.append([bian, 1])

    else:
        bian = sort2[-1][1]
        chang = sort2[-1][0]
        sort2.pop()
        youpiao = sort2
        res += bian ** 2
        num += 1
        if bian !=1 or chang-1 != 1:
            youpiao.append([chang-1, bian])
        if bian != 1:
            youpiao.append([1, bian])

print(res)
