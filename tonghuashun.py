nums = [5, 2, 3, 4, 9, 1]
k = 3

from collections import deque
queue = deque()
stack = deque()
res = list()
for i in range(k):
    queue.append(nums[i])
    while stack and stack[-1] < nums[i]:
        stack.pop()
    stack.append(nums[i])

res.append(stack[0])
for i in range(k, len(nums)):
    temp = queue.popleft()
    if temp == stack[0]:
        stack.popleft()
    while stack and stack[-1] < nums[i]:
        stack.pop()
    stack.append(nums[i])
    queue.append(nums[i])
    res.append(stack[0])

print(res)