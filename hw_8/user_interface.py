import viewer as v
import constants as c
from easygui import *

def main():
    while True:
        menu_msg = 'Greetings in database of SuperStaff! \n'
        menu_msg += 'choose operation'
        choice = choicebox(menu_msg, 'DATABASE OF OUR CORPORATION', c.MENU)   # выбираем вариант
        if choice == c.MENU[4]:
            exit()
        elif choice == c.MENU[0]:
            find_list, decision = v.find_in_list()
            if decision == 'delete':
                v.delete_from_book(find_list)
            elif decision == 'show info':
                v.show_info(find_list)
        elif choice == c.MENU[1]:
            v.show_info(v.db)
        elif choice == c.MENU[2]:
            quantity = enterbox('please enter quantity of employees', 'ADD employee')
            v.add_to_list(v.add_new_staff(int(quantity)))
        elif choice == c.MENU[3]:
            v.empty_list_of_staff()

