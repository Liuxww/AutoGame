# import random
# import copy
# w, h = 4, 4
# img = [[random.randint(0, 5)] * w for _ in range(h)]
# kernel = [[1, 2, 1], [2, 4, 2], [1, 2, 3]]
#
# out = copy.deepcopy(img)
# def compute(img, dic):
#     sum = 0
#     for i in [-1, 0, 1]:
#         for j in [-1, 0, 1]:
#             if dic[0]+i >= 0 and dic[1]+j >= 0 and dic[0]+i < w and dic[1]+j < h:
#                 sum += kernel[1+i][1+j] * img[dic[0]+i][dic[1]+j]
#     return sum / 16
#
#
# for i in range(h):
#     for j in range(w):
#         out[i][j] = compute(out, [i, j])
#
# print(img)
# print(out)


a, b = 5, 3

res = list()
res.append(a*4+b)
res.append(a*2+b*2)
res.append(a+b*4)
res = set(res)
ex = 0.
for item in res:
    ex += item/len(res)
ex = str(ex)
if len(ex.split('.')[1][:2]) >= 2:
    ex = ex.split('.')[0] + '.' + ex.split('.')[1][:2]
else:
    ex = ex + '0'
print(ex)
# print('{:.2f}'.format(ex))

# num = '103252'
# count = 0
# i = 0
# while i < len(num):
#     temp = num[:i] + num[i+1:]
#     temp = int(temp)
#     if temp != 0 and temp % 3 == 0:
#         count += 1
#         num = str(temp)
#     else:
#         i += 1
# print(count)