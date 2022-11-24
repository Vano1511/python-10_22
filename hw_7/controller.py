import model
import viewer

def main():
    print('телефонный справочник в формате csv'.center(50))
    menu_msg = 'МЕНЮ:\n 1.найти контакт\n 2.добавить контакт\n 3.удалить контакт\n 4.экспортировать в JSON формат\n'
    menu_msg += ' 5.импортировать из JSON формата\n 6.импортировать другой справочник\n 7.показать весь справочник\n'
    menu_msg += ' 8.выход'
    print(menu_msg)
    while True:
        choise = input('Введите номер необходимой операции > ')
        if choise == '1':
            findword = input('Введите что будем искать > ')
            viewer.finder(findword)
        elif choise == '2':
            model.add_contact()
        elif choise =='3':
            person = viewer.finder(input('сначала давайте найдем, кого удалить > '))
            if person:
                answer = input(f'удаляем контакт {person}? (1-да) > ')
                if answer == '1':
                    model.delete_contact(person)
                else:
                    print('контакт не удален')
        elif choise == '4':
            json_filename = input('введите название файла, куда переносим > ')
            if json_filename[len(json_filename)-5:len(json_filename)-1].lower() == 'json':
                model.export_to_json('phones.csv', json_filename)
            else:
                json_filename += '.json'
                model.export_to_json('phones.csv', json_filename)
        elif choise == '5':
            json_filename = input('введите название файла, откуда переносим > ')
            if json_filename[len(json_filename) - 5:len(json_filename) - 1].lower() == 'json':
                model.import_from_json(json_filename)
            else:
                json_filename += '.json'
                model.import_from_json(json_filename)
            model.sorting()
        elif choise == '6':
            filename = input('введите название файла, откуда переносим > ')
            if filename[len(filename) - 4:len(filename) - 1].lower() == 'csv':
                model.import_new_book(filename)
            else:
                filename += '.csv'
                model.import_new_book(filename)
            model.sorting()
        elif choise == '7':
            viewer.show_all()
        elif choise == '8':
            break
        else:
            print('вы ввели некорректные данные, попробуйте еще')
        menu_check = input('\nесли нужно еще раз показать меню - нажмите 1, если нет - любой другой ввод  > ')
        if menu_check == '1':
            print('\n' + menu_msg)
    print('\nСпасибо за использование нашего справочника. Всего хорошего!!')


