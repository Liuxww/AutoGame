n, k = 6, 3
weights = [1, 3, 1, 5, 3, 1]

from collections import Counter
weights.sort()
count = Counter(weights)
res = 0

for key in count:
    min_num = key
    max_num = key + k
    temp = 0
    for i in range(min_num, max_num+1):
        if i in count:
            temp += count[i]
    if temp > res:
        res = temp

print(res)