n, x, y, K = 4, 1, 5, 1
a = [2, 6, 3, 8]

res = 0
a = sorted(a, key=lambda x: -x)
for i in range(len(a)):
    ren = x * a[i]
    if ren > y and K > 0:
        res += y
        K -= 1
    else:
        res += x * a[i]

print(res)
