n, b = 3, 5
powers = [6, 2, 3]
times = [7, 5, 3]

def compute(n, b, powers, times):
    if powers[0] > b:
        return [-1]
    ress = list()
    res = times[0]
    cur_power = powers[0]
    min_time = times[0]
    for i in range(1, n):
        if times[i] < min_time and cur_power+powers[i]<=b:
            ress.append(res)
            res = times[i]
            min_time = times[i]
            cur_power += powers[i]
        else:
            res += min_time
    ress.append(res)
    return ress

print(max(compute(n,b,powers,times)))