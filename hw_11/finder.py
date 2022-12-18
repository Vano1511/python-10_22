from math import sin, cos


def roots(start, finish):  # для нахождения корней
    def func(x):
        return -12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
    flag = start
    step = 0.000001
    res = []
    while finish >= flag:
        if -8 < flag < 8:  # на этом промежутке уменьшим чувствительность
            if -0.1 < func(flag) < 0.1:
                res.append(round(flag, 1))
        else:
            if -1000 < func(flag) < 1000:  #  большая чувствительность, чтоб попадали корни
                res.append(round(flag, 0))
        flag += step
    return sorted(set(res))

def peaks(start, finish):   # для нахождения вершин
    def func(x):
        return -12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
    flag = start
    step = 0.0001
    res = []
    while finish >= flag:
        if func(flag - step) < func(flag) > func(flag + step) or func(flag - step) > func(flag) < func(flag + step):
            res.append(round(flag, 0))
        flag += step
    return sorted(set(res))


print(roots(-30, 30))
print(peaks(-30, 30))
