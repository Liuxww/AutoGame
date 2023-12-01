X = [0, 1]
m = len(X)


class solution:
    def sx(self, m, X):
        res = 0
        for i in range(m):
            res += i * X[i] % m

        return res

    def simp_ws_fuc(self, X, m):
        index = self.sx(m, X)
        return X[index]

    def av(self, X, m):
        res = 0
        for i in range(m):
            for s in range(m+1):
                if self.sx(m, X) == s and X[i] == 0 and X[s] == 1 and X[s+i] == 0 and s < m:
                    res += 1
                elif self.sx(m, X) == s and X[i] == 0 and X[s] == 1 and X[s+i] == 1:
                    res += 1

        return res

solu = solution()
print(solu.av(X, m))