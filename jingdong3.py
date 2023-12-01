string = '())())'

ans = 0
for i in range(len(string)):
    for j in range(i + 1, len(string)):
        if "()" in string[i:j]:
            sub = string[i:j]
            i = 1
            while "()" in sub:
                sub = sub.replace("()", '')
                i += 1
            ans += i * 2
print(ans)
