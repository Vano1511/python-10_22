def dellimiter(text):  # функция раскладывает многочлен на члены и выдает в виде словаря
    list = text.split()
    for el in list:
        if el == '+' or el == '=' or el == '0':
            list.remove(el)
    list.pop()  #  не понимаю, почему у меня не удаляется ноль, поэтому выкрутился так
    new_dict = {}  # попробую через словарь, где ключ это х в степени
    for element in list:
        index = element.find('X')
        if index == -1:
            new_dict[0] = int(element)
        else:
            new_dict[int(element[index+2:])] = int(element[:index])
    return new_dict

def summ_poly(dic1, dic2): # функция, которая складывает значения двух словарей исходя из ключей
    exit_dict = {}
    maxim = 0
    for key1 in dic1.keys():    # найдем максимальную степень многочлена
        for key2 in dic2.keys():
            if key1 > maxim:
                maxim = key1
            elif key2 > maxim:
                maxim = key2
    while maxim >= 0:     # заполлним итоговый словарь нулями
        exit_dict[maxim] = 0
        maxim -= 1
    for key1, value1 in dic1.items():      # сложим коэффициенты в итоговом словаре
        for key2, value2 in dic2.items():
            for key in exit_dict.keys():
                if key1 == key2 == key:
                    exit_dict[key2] = value2 + value1
                elif key == key2 and not dic1.get(key):
                    exit_dict[key] = value2
                elif key == key1 and not dic2.get(key):
                    exit_dict[key] = value1


    return exit_dict


file = open('polynomial.txt')
polynomial_1 = file.read()
file.close()
file = open('polynomial(1).txt')
polynomial_2 = file.read()
file.close()

dict_poly1 = dellimiter(polynomial_1)
dict_poly2 = dellimiter(polynomial_2)
summ = summ_poly(dict_poly2, dict_poly1)
result = ''                                   # создадим итоговую строку и запишем в файл "finish.txt"
for key, value in summ.items():
    if key == 0:
        result += f'{value} = 0'
    else:
        result += f'{value}X^{key} + '
with open('finish.txt', 'w') as file:
    file.write(result)

