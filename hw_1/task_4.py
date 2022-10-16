quarters = {'1': [1, 1], '2': [0, 1], '3': [0, 0], '4': [1, 0]}
quarter = input('выберите четверть координатной плоскости (от 1 до 4) и я вам подскажу диапазон координат: ')
cor_range = quarters[quarter]
print(f' Вы выбрали {quarter}-ю четверть координатной плоскости, диапазон решений: ')
if cor_range[0] == 1:   # 1 - это больше 0, а 0 - меньше 0
    if cor_range[1] == 1:
        print('x > 0, y > 0')
    else:
        print('x > 0, y < 0')
else:
    if cor_range[1] == 1:
        print('x < 0, y > 0')
    else:
        print('x < 0, y < 0')
