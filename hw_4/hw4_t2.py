def simple_numbers(num):  # алгоритм нахождения простых числ до числа num
    result = [1]
    for element in range(1, num+1):
        counter = 0
        for i in range(1, element+1):
            if element % i == 0:
                counter +=1
        if counter == 2:
            result.append(element)
    return result

number = int(input('введите натуральное число и я выдам список его простых множителей: '))
chek_list = simple_numbers(number)[::-1]  # переворачиваю проверочный список
finish_list = []
for element in chek_list: # нахожу вхождение простых чисел в множители
    if number % element == 0:
        finish_list.append(element)
        number //= element


print(finish_list[::-1])
