A = [3, 2, 1, 4, 5]
B = [3, 2, 1, 3, 3]


res = list()
for i in range(len(A)):
    if A[i] in res:
        res.append(A[i])
    elif B[i] in res:
        res.append(B[i])
    else:
        res.append(max(A[i], B[i]))
for i in range(1, 10**6+1):
    if i not in res:
        print(i)
        break