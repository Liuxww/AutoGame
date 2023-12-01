
S = "bdaaadadb"

n = len(S)
book = dict()
mask = 0
book[0] = -1

ans = 0
for i in range(n):
    val = ord(S[i]) - ord('a')
    mask ^= (1<<val)
    if mask in book:
        ans = max(ans, i-book.get(mask))
    else:
        book[mask] = i
print(ans)