import csv
import json

names = ('Фамилия', 'Имя', 'Телефон', 'Описание')

def add_unit():   #  функция добавляет одну запись в справочник, введенную вручную
    global names
    new_string = []
    for element in names:  # сначала запросим у пользователя новый контакт
        if element == 'Телефон':  # проверка на ввод числа
            flag = 1
            while flag:
                try:
                    new_string.append(int(input(f'введите данные: {element} > ')))
                    flag = 0
                except:
                    print('вы ввели неверный формат телефона')

        else:
            new_string.append(input(f'введите данные: {element} > '))

    with open('phones.csv', 'a', encoding='utf-8') as file: # непосредственно запись в справочник
        new_row = ''
        for item in new_string:
            new_row += str(item).title() + ','
        new_row = new_row[:len(new_row)-1]   #    убираем последнюю запятую
        file.write(new_row + '\n')
        print('Запись добавлена успешно ')

def sorting():  # метод, сортирующий телефонный справочник по алфавиту
    file = open('phones.csv', encoding='utf-8')   # открываем, чтобы считать
    strings = file.readlines()
    spam = strings.pop(0)   # удаляем шапку
    strings.sort()
    strings.insert(0, spam)  # вставляем шапку в отсортированный справочник
    file.close()
    file = open('phones.csv', 'w', encoding='utf-8')  # перезаписываем файл
    for string in strings:
        file.write(string)
    print('справочник отсортирован ')

def export_to_json(filename, json_filename):  #  метод, экспортирующий наш справочник в json-файл
    global names
    phones_dict = {}   #  будем экспортировать в виде словаря
    with open(filename, encoding='utf-8') as file:  # открываем, чтобы его преобразовать в словарь
        file_reader = csv.DictReader(file, delimiter=',')
        counter = 1
        for row in file_reader:  # построчно создаем контакты
            person_dict = {names[0]:row[names[0]], names[1]:row[names[1]], names[2]:row[names[2]], names[3]: row[names[3]]}
            phones_dict[counter] = person_dict
            counter += 1
    with open(json_filename, 'w') as json_file:
        json.dump(phones_dict, json_file, indent=4, ensure_ascii=False) # непосредственно запись
    print('перенос справочника в phones.json осуществлен, файл перезаписан')

def import_from_json(json_filename): # метод, импортирующий новый спрвочник из json формата
    with open(json_filename) as json_file:
        new_dict = json.load(json_file)   # считываем файл в виде словаря
        with open('phones.csv', 'a', encoding='utf-8') as file:
            for value in new_dict.values():   # нам нужны только значения
                new_row = ''
                for value1 in value.values():   #  здесь тоже только значения для записи в строку
                    new_row += value1 + ','
                new_row = new_row[:len(new_row)-1]
                file.write(new_row + '\n')    # записываем новую строку в файл
    print('импорт из json-файла совершен успешно ')



#add_unit()
#sorting()
#export_to_json('phones.csv', 'phones.json')
#import_from_json('new.json')