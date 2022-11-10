from math import sqrt
def distance(cord_a, cord_b):
    dist = sqrt((cord_a[0] - cord_b[0])**2 + (cord_a[1] - cord_b[1])**2)
    return dist

cord_A = [float(i) for i in input('Введите координаты точки А через пробел: ').split()]
cord_B = [float(i) for i in input('Введите координаты точки B через пробел: ').split()]

print(f' Расстояние между точками А и В равно {round(distance(cord_A, cord_B), 2)}')