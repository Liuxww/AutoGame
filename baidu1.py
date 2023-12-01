string = 'baiduoxiaojiabankanjiaran'

yuanyin = ['a', 'e', 'i', 'o', 'u']
book = [0] * 26

left = 0
right = 5
res = 0
for i in range(5):
    book[ord(string[i])-ord('a')] += 1
if string[left+1] in yuanyin and string[left+2] in yuanyin and string[right-1] in yuanyin and max(book) == 1:
    res += 1

for i in range(len(string)-5):
    book[ord(string[i]) - 97] -= 1
    book[ord(string[i+5]) - 97] += 1

    if string[i + 2] in yuanyin and string[i + 3] in yuanyin and string[i + 5] in yuanyin and max(book) == 1:
        res += 1

print(res)