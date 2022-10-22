from random import randint

def coefficient():
    return randint(0, 100)

degree = int(input('Введите максимальную степень многочлена и я запишу его в файл "polynomial.txt" '))
answer = ''
while degree > 0:
    coeff = coefficient()
    if coeff == 0:
        break
    else:
        answer += (str(coeff) + f'X^{degree} + ')
    degree -= 1
answer += f'{coefficient()} = 0 '
with open('polynomial(1).txt', 'w') as file:
    file.write(answer)

