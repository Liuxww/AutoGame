from collections import Counter, deque
stirngs = 'redrde'
res = 0
queue = deque()
book = dict()
for i in range(1, len(stirngs)):
    for i in range(i*3):
        queue.append(stirngs[i])
        if stirngs[i] not in book:
            book[stirngs[i]] = 1
        else:
            book[stirngs[i]] += 1
    while len(queue) == 3*i:
        if book['r'] == book['e'] == book['d']:
            res += 1
        a = queue.popleft()
        book[a] -= 1

    left = 0
    right = i * 3
    if right <= len(stirngs):
        while right <= len(stirngs):
            count = Counter(stirngs[left:right])
            if count['r'] == count['e'] == count['d']:
                res += 1
            left += 1
            right += 1
    else:
        break

print(res)