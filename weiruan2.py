M = 8
A = [7, 1, 11, 8, 4, 10]
book = dict()

for item in A:
    num = item % M
    if num not in book:
        book[num] = 1
    else:
        book[num] += 1

print(max(book.values(), key=lambda x:x))