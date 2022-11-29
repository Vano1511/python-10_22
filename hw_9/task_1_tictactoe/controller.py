from random import randint, choice
from easygui import *


x = 'X'
o = 'O'

def draw_board(board): #рисуем поле
    bord = '-'* 19 + '\n'
    for i in range(3):
        bord += f'|  {board[0+i*3]}  |  {board[1+i*3]}  |  {board[2+i*3]}  |\n'
        bord += '-' * 19 + '\n'
    msgbox(bord)

def take_turn(player, char, board):  # ввод и проверка хода
    flag = True
    while flag:
        vision = []
        for element in board:
            if element != x and element != o:
                vision.append(element)
        if player == 'SUPERBOT':
            turn = choice(vision)
            msgbox(f'я ставлю в поле {turn}', 'очередной ход')
        else:
            turn = buttonbox(f'{player}, куда поставишь {char} ? ', f'ходит {player}', tuple(map(str, vision)))
        try:                                           #  введено ли число
            turn = int(turn)
        except:
            msgbox('введено не число!', 'wrong input')
            continue
        if turn not in range(1, 10):           # входит ли в диапазон
            msgbox('введено некорректное число, повтори', 'wrong input')
            continue
        elif str(board[turn-1]) in (x, o):           # проверка не занята ли клетка
            msgbox('клетка уже занята! повтори', 'wrong choice')
            continue
        flag = False
    return turn

def char_player_change(char, player):  # функция смены хода
    if char == x:
        char = o
    else:
        char = x
    if player == 'Игрок1':
        player = 'Игрок2'
    elif player == 'Игрок2':
        player = 'Игрок1'
    elif player == 'Игрок':
        player = 'SUPERBOT'
    else:
        player = 'Игрок'
    return char, player

def check_win(board):    # проверка на выигрыш
    win = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))  # все варианты выигрыша
    for variant in win:
        if board[variant[0]-1] == board[variant[1]-1] == board[variant[2]-1]:
            return True
    return False


def main_game(pl1, pl2, board):   # тело игры
    msgbox('сейчас выберем, кто первый будет ходить: кидаю монетку...', '')
    first = randint(0, 1)
    player = pl1
    if first == 1:
        player = pl2  # меняем местами, так как ходит первым Игрок2
    if player == 'SUPERBOT':
        msgbox('Я хожу первым')
    else:
        msgbox(f'{player} ходит первым')
    char = x  # Х всегда ходит первым
    counter = 1  # считаем ходы
    while True:
        turn = take_turn(player, char,board)
        board[turn - 1] = char
        draw_board(board)
        if counter > 4:  # есть смысл проверять только на пятом ходу
            result = check_win(board)
            if result:
                if player == 'SUPERBOT':
                    msgbox(f'Я победил на {counter}-м ходу! не расстраивайся, повезет в другой раз', '')
                else:
                    msgbox(f'на {counter}-м ходу победил {player}, поздравляем!', '')
                break
        char, player = char_player_change(char, player)  # смена хода
        counter += 1
        if counter > 9:
            msgbox('ходы закончились, ничья', 'END OF GAME')
            break

