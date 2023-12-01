import math

def yinzi(n):
    y = []
    if n <= 2:
        return y
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            y.append(n/i)

    return sorted(set(y))

print(yinzi(36))