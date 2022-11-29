import csv
import json

names = ('Фамилия', 'Имя', 'Телефон', 'Описание')

def sorting():  # метод, сортирующий телефонный справочник по алфавиту
    file = open('phones.csv', encoding='utf-8')   # открываем, чтобы считать
    strings = file.readlines()
    spam = strings.pop(0)  # удаляем шапку
    strings = list(set(strings))  #  избавляемся от одинаковых записей
    strings.sort()
    strings.insert(0, spam)  # вставляем шапку в отсортированный справочник
    file.close()
    file = open('phones.csv', 'w', encoding='utf-8')  # перезаписываем файл
    for string in strings:
        file.write(string)
    file.close()

def export_to_json(json_filename):  #  метод, экспортирующий наш справочник в json-файл
    global names
    phones_dict = {}   #  будем экспортировать в виде словаря
    with open('phones.csv', encoding='utf-8') as file:  # открываем, чтобы его преобразовать в словарь
        file_reader = csv.DictReader(file, delimiter=',')
        counter = 1
        for row in file_reader:  # построчно создаем контакты
            person_dict = {names[0]:row[names[0]], names[1]:row[names[1]], names[2]:row[names[2]], names[3]: row[names[3]]}
            phones_dict[counter] = person_dict
            counter += 1
    with open(json_filename, 'w') as json_file:
        json.dump(phones_dict, json_file, indent=4, ensure_ascii=False) # непосредственно запись


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

def import_new_book(filename):
    with open(filename, encoding='utf-8') as file_output: # читаем с добавляемого файла
        strings_out = file_output.readlines()
    with open('phones.csv', encoding='utf-8') as file_input:  # читаем с нашей книги
        strings_in = file_input.readlines()
    for string in strings_out:   # проверяем нет ли одинаковых контаков
        if string in strings_in:
            strings_out.remove(string)   # удаляем, если есть
    with open('phones.csv', 'a', encoding='utf-8') as file: # непосредственно запись в справочник
        file.writelines(strings_out)
    print('новые контакты успешно добавлены')

def delete_contact(person):
    file = open('phones.csv', encoding='utf-8')  # открываем, чтобы считать
    strings = file.readlines()
    file.close()
    for string in strings:
        if person in string:
            strings.remove(string)
            break                    # как удалили - заканчиваем поиск
    person = person.split(sep=',')
    str_person = str(person[0]) + ' ' + str(person[1])
    file = open('phones.csv', 'w', encoding='utf-8')  # перезаписываем файл
    file.writelines(strings)
    file.close()
    return f'Пользователь {str_person} удален '


# add_contact()

# export_to_json('phones.csv', 'phones.json')
# import_from_json('new.json')
# delete_contact('Ботан,Андрей')
# import_new_book('new_phones.csv')
# sorting()