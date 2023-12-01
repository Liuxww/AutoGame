S = "sswwrr"
target = 'swr'

result = [0]
def backtravel(start, target, path, S):
    if path == target:
        result[-1] += 1
        return
    for i in range(start, len(S)):
        if start >= 1 and S[i] in path:
            continue
        path += S[i]
        backtravel(i+1, target, path, S)
        path.replace(S[i], '')

backtravel(0, target, '', S)
print(result)