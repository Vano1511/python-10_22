import csv

names = ('Фамилия', 'Имя', 'Телефон', 'Описание')

def finder(findword):
    global names
    with open('phones.csv', encoding='utf-8') as file:
        flag = 0
        file_reader = csv.DictReader(file, delimiter = ',')
        for row in file_reader:
            if findword.title() in row[names[0]] or findword.title() in row[names[1]] \
                    or findword.title() in row[names[3]] or findword in row[names[2]]:
                print(f'{row[names[0]]} {row[names[1]]} - тел. {row[names[2]]}, - {row[names[3]]} ')
                flag = 1
        if flag == 0:
            print('по вашему запросу ничего не найдено')

def show_all():
    global names
    with open('phones.csv', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        print(f'{names[0]:20} {names[1]:20} {names[2]:20} {names[3]}')
        print('-' * 80)
        for row in file_reader:
            print(f'{row[names[0]]:20} {row[names[1]]:20} {row[names[2]]:20} {row[names[3]]} ')


#finder('342')
#show_all()