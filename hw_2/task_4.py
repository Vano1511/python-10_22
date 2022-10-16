from random import randint, choice
def shake(list):   # функция перемешивания элементов в списке
    new_list = []
    copy_list = list[:]  #  создаем копию, чтоб не испортить исходник
    for i in range(len(list)):
        el = choice(copy_list)
        copy_list.remove(el)
        new_list.append(el)
    return new_list

number = int(input('введите число элементов для массива: '))
array = [i for i in range(-number, number+1)]  # создаем первоначальный массив из которого будем делать выборку
result = []    # итоговый массив
write = open("file.txt", "w")
for digit in range(number): #  делаем выборку элементов
    el = randint(-number, number)
    result.append(el)
    index = randint(0, len(array))    # записываем  произволные индексы в файл
    write.write(str(index) + '\n')
write.close()      # закроем файл и откроем на чтение(у меня не получилось все это сделать в одном открытии)
read = open("file.txt", "r")

mult = 1   # задаем показатель произведения элементов
new_arr = [] # выведем новый массив для проверки
for i in range(number):
    element = int(read.readline().replace('\n', ''))
    new_arr.append(array[element])
    if element == number:
        print('произведение равно 0, так как хотя бы один элемент равен 0 ')
        break
    else:
        mult *= array[element]
read.close()
print(f' первый список чисел: {result}')
print(f' новый список(индексы взяты из файла): {new_arr}')
print(f' перемешанный новый список: {shake(new_arr)}')
print('произведение равно ' + str(mult) + '.')
