n = 5
m = 3
num = [2, 3, 4]
# org = list()
# for i in range(n, 0, -1):
#     org.append(i)
# for item in num:
#     index = org.index(item)
#     a = org.pop(index)
#     org.append(a)
# res = ''
# for i in range(n-1, -1, -1):
#     res += str(org[i]) + ' '

book = dict()
cur = 5 * 10 ** 6
for i in range(1, n + 1):
    book[i] = cur
    cur += 1
cur = 5 * 10 ** 6
for item in num:
    book[item] = cur - 1
    cur -= 1
book = sorted(book.items(), key=lambda x:x[1])
res = list()
for key in book:
    res.append(key[0])
print(res)