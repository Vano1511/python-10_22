from easygui import *
import constants as c
import json

with open(c.path, encoding='utf-8') as json_file:  # определяем id , чтобы не повторялись
    foo = json.load(json_file)
id = int(list(foo)[-1]) + 1
db = [value for value in foo.values()]  # создаем список для удобства вывода информации



def empty_list_of_staff():  # медот очистки БД
    with open(c.path, 'w', encoding='utf-8') as json_file:
        json.dump({}, json_file, indent=4, ensure_ascii=False)

def add_new_staff(quantity): # добавляем сотрудников
    global id
    count = 1
    new_characters_list = {}
    while count <= quantity:
        new_character = {c.CHARACTER[0]: id, c.CHARACTER[1]: ' ', c.CHARACTER[2]: ' ', c.CHARACTER[3]: ' ',
                         c.CHARACTER[4]: ' ', c.CHARACTER[5]: ' ', c.CHARACTER[6]: ' '}   # создаем шаблончик
        titel = f'create emplotee №{id}'
        for chapter in c.CHARACTER:
            if chapter == c.CHARACTER[1]:
                msg = 'enter name and surname of new employee'
                name, surname = multenterbox(msg, titel, c.NAMES)
                new_character[chapter] = [name.title(), surname.title()]
            elif chapter == c.CHARACTER[2]:
                msg = f'enter a {chapter} of  new employee'
                new_character[chapter] = choicebox(msg, titel, c.GENDER)
            elif chapter == c.CHARACTER[3]:
                flag = 1
                while flag:
                    msg = f'enter a {chapter} of  new employee(use ".")'
                    birth = enterbox(msg, titel)
                    date = birth.split('.')
                    if 1 <= int(date[0]) <= 31 and 1 <= int(date[1]) <= 12 and 1950 <= int(date[2]) <= 2004:
                        new_character[chapter] = list(map(int, date))
                        flag = 0
                    else:
                        msgbox('please input coorect birthday', titel)
            elif chapter == c.CHARACTER[4]:
                msg = 'enter a departure of new employee'
                departure = choicebox(msg, titel, c.DEPARTMENTS)
                msg = 'enter a job of new employee'
                if departure == c.DEPARTMENTS[0]:
                    job = choicebox(msg, titel, c.DIR_TITLES)
                elif departure == c.DEPARTMENTS[1]:
                    job = choicebox(msg, titel, c.SPEC_TITLES)
                else:
                    job = choicebox(msg, titel, c.WORK_TITLES)
                new_character[chapter] = [departure, job]
            elif chapter == c.CHARACTER[5]:
                quantity_phones = enterbox('quantity of phones', titel, [1])
                numbers = [number + 1 for number in range(int(quantity_phones))]
                new_character[chapter] = multenterbox('enter phones', titel, numbers)
            elif chapter == c.CHARACTER[6]:
                msg = f'enter a {chapter} squad of new employee'
                new_character[chapter] = list(map(int, multenterbox(msg, titel, c.SALLARY, [0,0])))
        new_characters_list[id] = new_character
        count += 1
        id += 1
    return new_characters_list


def add_to_list(dictionary):  # метод добавления записи в БД
    with open(c.path, encoding='utf-8') as json_file:
        spam = json.load(json_file)
    for key, value in dictionary.items():
        spam[key] = value
    with open(c.path, 'w', encoding='utf-8') as json_file:
        json.dump(spam, json_file, indent=4, ensure_ascii=False)
    msgbox('new staff added successfull \nrestart the DB for refresh', 'SUCCESS')

def find_in_list():  # метод поиска сотрудника
    with open(c.path, encoding='utf-8') as json_file:
        finder = [value for value in json.load(json_file).values()]
    msg = 'Please choose find_title'
    find_msg = 'now input what i must found'
    title = 'find the employee'
    choises = (c.CHARACTER[1], c.CHARACTER[0], c.CHARACTER[2], c.CHARACTER[4], c.CHARACTER[5])
    choice1 = choicebox(msg, title, choises)
    find_list = [] # если их будет несколько
    flag = 0
    employee = ''
    if choice1 == c.CHARACTER[0]:
        choice = enterbox(find_msg, title, [0])
        for character in finder:
            if choice in str(character[c.CHARACTER[0]]):
                employee += ' '.join(character[c.CHARACTER[1]]) + '\n'
                find_list.append(character)
                flag = 1
    elif choice1 == c.CHARACTER[1]:
        choice = enterbox(find_msg, title, [0])
        for character in finder:
            for name in character[c.CHARACTER[1]]:
                if choice.lower() in name.lower():
                    employee += ' '.join(character[c.CHARACTER[1]]) + '\n'
                    find_list.append(character)
                    flag = 1
                    break
    elif choice1 == c.CHARACTER[2]:
        choice = choicebox(find_msg, title, c.GENDER)
        for character in finder:
            if choice == character[c.CHARACTER[2]]:
                employee += ' '.join(character[c.CHARACTER[1]]) + '\n'
                find_list.append(character)
                flag = 1
    elif choice1 == c.CHARACTER[4]:
        choice = choicebox(find_msg, title, c.DEPARTMENTS)
        if choice == c.DEPARTMENTS[0]:
            choice2 = choicebox(find_msg, title, c.DIR_TITLES)
        elif choice == c.DEPARTMENTS[1]:
            choice2 = choicebox(find_msg, title, c.SPEC_TITLES)
        elif choice == c.DEPARTMENTS[2]:
            choice2 = choicebox(find_msg, title, c.WORK_TITLES)
        for character in finder:
            if choice2 in character[c.CHARACTER[4]]:
                employee += ' '.join(character[c.CHARACTER[1]]) + '\n'
                find_list.append(character)
                flag = 1
    elif choice1 == c.CHARACTER[5]:
        choice = enterbox(find_msg, title, [0])
        for character in finder:
            for number in character[c.CHARACTER[5]]:
                if choice in number:
                    employee += ' '.join(character[c.CHARACTER[1]]) + '\n'
                    find_list.append(character)
                    flag = 1
                    break
    if flag != 1:  # если ничего не нашли
        msgbox('i have not found anything from your request', 'NOTHING MATCHES')
        return 0, 0
    else:   # запрашиваем, что дальше делать
        decision = choicebox(employee, 'find success', ('delete', 'show info'))
        return find_list, decision

def show_info(list_of_staff): #   метод показа инфо о работниках
    character_row = ''
    for character in list_of_staff:
        for key, value in character.items():
            if key == 'birthday':
                value_row = ''
                for item in value:
                    value_row += f'{item:02}' + '.'
                character_row += f'{key:8} : {value_row[:-1]}\n'
            elif key == 'sallary':
                character_row += f'{key:8} : {sum(value)}\n'
            elif type(value) is list:
                value_row = ''
                for item in value:
                    value_row += str(item) + ' '
                character_row += f'{key:8} : {value_row}\n'
            elif key == 'sallary':
                character_row += f'{key:8} : {sum(value)}\n'
            else:
                character_row += f'{key:8} : {str(value)}\n'
        character_row += '\n\n'
    msg = character_row
    msgbox(msg, 'INFO')

def delete_from_book(character_list):  # метод удаления
    for character in character_list:
        with open(c.path, encoding='utf-8') as json_file:
            employees = json.load(json_file)
        for key, value in employees.items():
            if int(key) == int(character['id']):
                del_key = key
        spam = employees.pop(del_key)  # удаляем, но сохраняем для вывода
        with open(c.path, 'w', encoding='utf-8') as json_file:
            json.dump(employees, json_file, indent=4, ensure_ascii=False)
        name = ' '.join(spam[c.CHARACTER[1]])
        msgbox(f'{name} is deleted', 'COMPLETE')

# add_to_list(add_new_staff(2))
# add_to_list(add_new_staff(1))
# print(find_in_list())
# show_all_info(foo)
# delete_from_book([{'id': 2, 'names': ['Bridgette', 'Brown'], 'gender': 'female', 'birthday': [12, 1, 1999], 'jobtitle': ['specialists', 'HR'], 'phones': ['234234345', '353454355', '657456464'], 'sallary': [3200, 2000]}])
