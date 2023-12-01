n, m = 6, 2
S = "aaaaaa"
minlength = [4, 2]
mincontent = ["aa", "aaaa"]

res = []

def backtravel(s, start, path):
    if start >= len(s):
        res.append(path[:])
        return

    for i in range(start, len(s)):
        if s[start:i+1] in mincontent:
            mincontent.remove(s[start:i+1])
            path.append(s[start:i+1])
            backtravel(s, i+1, path)
            mincontent.append(s[start:i + 1])
            path.pop()
path = []
backtravel(S, 0, path)

print(len(res))