from math import sin, cos


def roots(start, finish):  # для нахождения корней
    def func(x):
        return 0.6 * x ** 3 + 5.5 * x ** 2 + 10 * x - 5
    flag = start
    step = 0.001
    res = []
    while finish >= flag:
        if -0.1 < func(flag) < 0.1:
            res.append(round(flag, 2))
        flag += step
    return sorted(set(res))

def peaks(start, finish):   # для нахождения вершин
    def func(x):
        return 0.6 * x ** 3 + 5.5 * x ** 2 + 10 * x - 5
    flag = start
    step = 0.001
    res = []
    while finish >= flag:
        if func(flag - step) < func(flag) > func(flag + step) or func(flag - step) > func(flag) < func(flag + step):
            res.append(round(flag, 2))
        flag += step
    return sorted(set(res))


print(roots(-30, 30))
print(peaks(-30, 30))
