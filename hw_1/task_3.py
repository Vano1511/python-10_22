comment = 'введите координаты X и Y через пробел, и я подскажу, где искать эту точку: '
coordinats = [int(i) for i in input(comment).split()]
x = coordinats[0]
y = coordinats[1]
if x == 0:
    if y == 0:
        print('точка лежит в начале координат')
    elif y < 0:
        print('точка лежит на оси Y между 3 и 4 четвертью')
    elif y > 0:
        print('точка лежит на оси Y между 1 и 2 четвертью')
elif x > 0:
    if y == 0:
        print('точка лежит на оси X между 1 и 4 четвертью')
    elif y < 0:
        print('точка лежит в 4 четверти')
    elif y > 0:
        print('точка лежит в 1 четверти')
else:
    if y == 0:
        print('точка лежит на оси X между 2 и 3 четвертью')
    elif y < 0:
        print('точка лежит в 3 четверти')
    elif y > 0:
        print('точка лежит в 2 четверти')