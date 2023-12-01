num = "1142"

book = {
    'o': 0,
    'y': 1,
    'e': 2,
    'a': 3,
    's': 4,
}

book_five = {
    0: 'o',
    1: 'y',
    2: 'e',
    3: 'a',
    4: 's',
}

def to_ten(num):
    n = len(num)
    res = 0
    for i in range(n):
        res += 5**(n-i-1) * book[num[i]]

    return str(res)

def to_five(num):
    num = int(num)
    s = []
    fivesting = ''
    while num > 0:
        rem = num % 5
        s.append(book_five[rem])
        num = num // 5
    while len(s) > 0:
        fivesting = fivesting + s.pop()

    return fivesting
try:
    num = int(num)
    print(to_five(num))
except:
    print(to_ten(num))
