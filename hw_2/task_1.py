number = input('введите любое вещественное число и я посчитаю сумму его цифр: ')
summ = 0
for digit in number:
    if digit.isdigit():
        summ += int(digit)
print(f'сумма всех цифр введенного вами числа будет равна {summ}')