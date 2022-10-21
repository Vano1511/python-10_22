message = 'введите последовательнось вещественных чисел(через точку) через пробел'
message += '\nи я найду разность max и min их дробных частей: '
numbers = [float(el) for el in input(message).split()]
min_part = 1   # задаем максимум и минимум
max_part = 0
for number in numbers:  # найдем все за один проход
    if number % 1 >= max_part:
        max_part = number % 1
    elif number % 1 <= min_part:
        min_part = number % 1

print(f' разность равна : {round(max_part - min_part, 3)}')