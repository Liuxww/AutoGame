NM = [2, 1]
qipan = ['.','*']
n, m = NM[0], NM[1]
dp = [[0] * m for _ in range(n)]
num = 0
if n>2 and m>2:
    for i in range(2):
        for j in range(2):
            if qipan[i][j] == '*':
                num += 1
                dp[i][j] = num

    for i in range(2):
        for j in range(2, m):
            if qipan[i][j] == '*':
                if dp[i][j-2] != 0:
                    dp[i][j] = num
                else:
                    num += 1
                    dp[i][j] = num
    for j in range(2):
        for i in range(2, n):
            if qipan[i][j] == '*':
                if dp[i-2][j] != 0:
                    dp[i][j] = num
                else:
                    num += 1
                    dp[i][j] = num
    for i in range(2, n):
        for j in range(2, m):
            if qipan[i][j] == '*':
                if dp[i-2][j] != 0 or dp[i][j-2] != 0:
                    dp[i][j] = num
                else:
                    num += 1
                    dp[i][j] = num

elif n==1 and m==1:
    for i in range(1):
        for j in range(1):
            if qipan[i][j] == '*':
                num += 1
                dp[i][j] = num
elif n==1 and m>1:
    for i in range(1):
        for j in range(2):
            if qipan[i][j] == '*':
                num += 1
                dp[i][j] = num
    for i in range(1):
        for j in range(2, m):
            if qipan[i][j] == '*':
                if dp[i][j-2] != 0:
                    dp[i][j] = num
                else:
                    num += 1
                    dp[i][j] = num
if n>1 and m==1:
    for i in range(2):
        for j in range(1):
            if qipan[i][j] == '*':
                num += 1
                dp[i][j] = num
    for j in range(1):
        for i in range(2, n):
            if qipan[i][j] == '*':
                if dp[i-2][j] != 0:
                    dp[i][j] = num
                else:
                    num += 1
                    dp[i][j] = num
elif n==2 and m==2:
    for i in range(2):
        for j in range(2):
            if qipan[i][j] == '*':
                num += 1
                dp[i][j] = num
elif n==2 and m>2:
    for i in range(2):
        for j in range(2):
            if qipan[i][j] == '*':
                num += 1
                dp[i][j] = num
    for i in range(2):
        for j in range(2, m):
            if qipan[i][j] == '*':
                if dp[i][j-2] != 0:
                    dp[i][j] = num
                else:
                    num += 1
                    dp[i][j] = num
if n>2 and m==2:
    for i in range(2):
        for j in range(2):
            if qipan[i][j] == '*':
                num += 1
                dp[i][j] = num
    for j in range(2):
        for i in range(2, n):
            if qipan[i][j] == '*':
                if dp[i-2][j] != 0:
                    dp[i][j] = num
                else:
                    num += 1
                    dp[i][j] = num
print(num)