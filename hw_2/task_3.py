number = int(input('введите натуральное число N и я выдам вам список значений (1+1/n)^n от 0 до N: '))
result = {}
summ = 0
for digit in range(1, number+1):
    result[digit] = round((1 + (1/digit))**digit, 3)
    summ += result[digit]
print(result)
print('сумма всех элементов последовательности равна: '+ str(summ))