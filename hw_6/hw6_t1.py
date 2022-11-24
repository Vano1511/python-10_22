# Исходный код

# numbers = [int(el) for el in input('введите последовательнось чисел через пробел и я посчитаю сумму тех, что стоят на нечетных позициях: ').split()]
# summ = 0
# for i in range(len(numbers)):
#     if i % 2 == 1:
#         summ += numbers[i]
#
# print(f'сумма всех чисел на нечетных позициях равна: {summ}')

# апгрейдженный код
numbers = [int(el) for el in input('введите последовательнось чисел через пробел и я посчитаю сумму тех, что стоят на нечетных позициях: ').split()]
print(f'сумма всех чисел на нечетных позициях равна: {sum([number for index, number in enumerate(numbers) if index % 2 == 1 ])}')
