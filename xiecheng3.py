# a, b, l, r = 1, 6, 2, 5
#
# max_num, min_num = 0, 0
# res = list()
# sub = b - a
# temp = sub % l
# if temp == 0:
#     res.append(sub // l)
# elif l <= temp and temp <= r:
#     res.append(sub // l + 1)
#
# while l < r:
#     temp = sub % r
#     if temp == 0:
#         res.append(sub // r)
#     elif l <= temp and temp <= r:
#         res.append(sub // r + 1)
#     r = l + r >> 1
#
# a, b, l, r = 1, 6, 2, 5
# while l < r:
#     temp = sub % l
#     if temp == 0:
#         res.append(sub // l)
#     elif l <= temp and temp <= r:
#         res.append(sub // l + 1)
#     l = l + r // 2
#
# if res:
#     print(min(res), max(res))
# else:
#     print(-1)
# # for i in range(l, r + 1):
#     # temp = sub % i
#     # if temp == 0:
#     #     res.append(sub // i)
#     # elif l <= temp and temp <= r:
#     #     res.append(sub // i + 1)
def reverse(ss):
    left = 0
    right = len(ss) - 1
    while left <= right:
        ss[left], ss[right] = ss[right], ss[left]
        left += 1
        right -= 1
    return ss


def Inverse(string):
    s = list(string.split())
    s = reverse(s)
    last = 0
    for i in range(len(s)):
        if s[i] == ' ':
            s[last:i] = reversed(s[last:i])
            last += 1
    return ' '.join(s)

print(Inverse('Tom and Rose.'))