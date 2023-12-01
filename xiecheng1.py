num = 103
k = 2

num = str(num)
def reverse(string):
    start = 0
    end = len(string) - 1
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1
    for i in range(len(string)):
        if string[i] != '0':
            return ''.join(string[i:])
temp = list()
for i in range(k):
    temp.append(num[i])
num = reverse(temp) + num[k:]
print(num)