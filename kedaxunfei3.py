points = [[-1, -1, -1, 1, 1, -1, 0, -1],
          [-1,  0,  0, 0, 0,  0, 0,  1],
          [-1,  0, -1, 0,-1, -1, 0, -1],
          [-1,  0,  1, 0, 1,  0, 0, -1],
          [-1,  1, -1,-1, 0, -1, 0, -1],
          [-1,  0, -1, 0,-1,  0, 0, -1],
          [-1,  0, -1, 0,-1,  0, 0, -1]]
r, c = 7, 8
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class A:
    def __init__(self):
        self.res = [-1, -1]

    def dfs(self, points, row, col, cur, ans, res):
        if ans != math.inf and cur > ans:
            return
        if points[row][col] == 1:
            if cur < ans:
                ans = cur
                self.res = [row, col]
            return
        for i in range(4):
            next_row = row + d[i][0]
            next_col = col + d[i][1]
            if next_row < 0 or next_row >= len(points) or next_col < 0 or next_col >= len((points[0])) or points[next_row][next_col] == -1:
                continue
            points[row][col] = -1
            self.dfs(points, next_row, next_col, cur+1, ans, res)
            points[row][col] = 0
    def call(self):
        return self.res

import math
global res
res = [-1, -1]
ans = math.inf
a = A()
a.dfs(points, 5, 5, 0, ans, res)
print(a.call())