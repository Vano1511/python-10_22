import csv

names = ('Фамилия', 'Имя', 'Телефон', 'Описание')

def finder(findword):
    global names
    with open('phones.csv', encoding='utf-8') as file:
        flag = 0
        res = ''
        file_reader = csv.DictReader(file, delimiter=',')
        for row in file_reader:
            if findword.title() in row[names[0]] or findword.title() in row[names[1]] \
                    or findword.title() in row[names[3]] or findword in row[names[2]]:
                res += f'{row[names[0]]} {row[names[1]]} - тел. {row[names[2]]}, - {row[names[3]]}\n '
                person = (row[names[0]], row[names[1]], row[names[2]], row[names[3]]) # сохраняем найденное в память
                flag = 1
        if flag == 0:
            return 'по вашему запросу ничего не найдено', None
        else:
            return res, ','.join(person)


def show_all():
    global names
    with open('phones.csv', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        res = f'{names[0]:20} {names[1]:20} {names[2]:20} {names[3]}\n'
        res += '-' * 80 + '\n'
        for row in file_reader:
            res += f'{row[names[0]]:20} {row[names[1]]:20} {row[names[2]]:20} {row[names[3]]} \n'
    return res


# print(finder('пень'))
# print(show_all())