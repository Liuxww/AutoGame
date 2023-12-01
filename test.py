def restoreIpAddresses(s):
    res = list()

    def backtravel(path, s, start, n):
        if n > 4:
            return
        if start >= len(s) and n == 4:
            res.append(".".join(path[:]))
            return

        for i in range(start, len(s)):
            temp = s[start:i + 1]
            if len(temp) > 1 and temp[0] == '0':
                continue
            if len(temp) > 3:
                return
            if 0 <= int(temp) and int(temp) <= 255:
                path.append(temp)
                n += 1
                backtravel(path, s, i + 1, n)
                path.pop()
                n -= 1

    backtravel(list(), s, 0, 0)
    return res

s = "101023"
print(restoreIpAddresses(s))