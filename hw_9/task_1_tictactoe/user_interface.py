import controller as c
from easygui import *


def main():
    msgbox('приветствую вас в игре крестики-нолики!', 'HELLO!')
    decision = buttonbox('начнем?', '', ("Да", "Нет"))
    while True:   #  запускаем игру
        if decision == "Нет":
            break
        mode = buttonbox('выберите режим игры', 'enter your choice', ("С игроком", "С тобой"))
        board = [el for el in range(1, 10)]  # поля с результатом
        if mode == "С игроком":
            c.main_game('Игрок1', 'Игрок2', board)
        else:
            msgbox('ну что, я играю с вами, я SUPERBOT')
            c.main_game('Игрок', 'SUPERBOT', board)
        decision = buttonbox('ну что, хотите сыграть еще раз?', 'enter choice', ("Да", "Нет"))
    msgbox('спасибо, что заглянули!', 'BYE BYE')



