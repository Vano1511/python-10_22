# Исходный код
# from random import randint
# num = int(input('введите количество элементов в исходном списке: '))
# start_list = [randint(-num, num) for counter in range(num)]
# print(f' вот исходный список : {start_list} ')
# check_dict = {} # создадим пустой словарь для подсчета встречающихся элементов
# for element in start_list:
#     if element not in check_dict.keys():
#         check_dict[element] = 1
#     else:
#         check_dict[element] += 1
# finish_list = []   # создадим итоговый список
# for key, value in check_dict.items():
#     if value == 1:
#         finish_list.append(key)
#
# print(f'вот список из неповторяющихся элементов в исходном списке: {finish_list} ')

# Upgrade
from random import randint
num = int(input('введите количество элементов в исходном списке: '))
start_list = [randint(-num, num) for counter in range(num)]
print(f' вот исходный список : {start_list} ')
check_dict = {} # создадим пустой словарь для подсчета встречающихся элементов
for element in start_list:
    if element not in check_dict.keys():
        check_dict[element] = 1
    else:
        check_dict[element] += 1
finish_list = [key for key, value in check_dict.items() if value == 1 ]   # создадим итоговый список
print(f'вот список из неповторяющихся элементов в исходном списке: {finish_list} ')
