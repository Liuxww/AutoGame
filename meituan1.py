n, m = 7, 3
S = "abcaacc"
target = "a*c"

def is_match(str1, str2):
    for i in range(len(str1)):
        if str2[i] == '*':
            continue
        elif str1[i] != str2[i]:
            return False
    return True

res = 0
for i in range(n-m+1):
    sub = S[i:i+m]
    if is_match(sub, target):
        res += 1

print(res)
