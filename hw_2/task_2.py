def factorial(number):   # напишем функцию, вычисляющую факториал
    result = 1
    for el in range(1,number+1):
        result *= el
    return result

number = int(input('введите натуральное число N и я вам выдам список факториалов от 1 до N: '))
res = []

# можно было еще сделать кортеж, как в примере, но я понял, что он расписан только, чтобы понять, что в списке


for digit in range(1,number+1):
    res.append(factorial(digit))

print(res)