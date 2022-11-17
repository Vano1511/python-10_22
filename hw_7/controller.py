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
        elif choise == '8':
            break
        else:
            print('вы ввели некорректные данные, попробуйте еще')
        menu_check = input('если нужно еще раз показать меню - нажмите 1, если нет - любой другой ввод  > ')
        if menu_check == '1':
            print('\n' + menu_msg)
    print('\nСпасибо за использование нашего справочника. Всего хорошего!!')










main()
