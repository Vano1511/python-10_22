from random import randint

board = [el for el in range(1,10)] # поля с результатом

def draw_board(): #рисуем поле
    print('-'* 19)
    for i in range(3):
        print(f'|  {board[0+i*3]}  |  {board[1+i*3]}  |  {board[2+i*3]}  |')
        print('-' * 19)

def take_turn(player, char):  # ввод и проверка хода
    flag = True
    while flag:
        choise = input(f'{player}, куда поставишь {char}? ')
        try:                                           #  введено ли число
            choise = int(choise)
        except:
            print('введено не число!')
            continue
        if choise not in range(1, 10):           # входит ли в диапазон
            print('введено некорректное число, повтори')
            continue
        elif str(board[choise]) in 'XO':           # проверка не занята ли клетка
            print('клетка уже занята! повтори')
            continue

        flag = False
    return choise

def check_win(board):    # проверка на выигрыш
    win = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))  # все варианты выигрыша
    for variant in win:
        if board[variant[0]] == board[variant[1]] == board[variant[2]]:
            return True
    return False


print('приветствую вас в игре крестики-нолики!\n')
while True:            # проверка правильности ввода данных
    mode = input('введите номер режима игры(1- с игроком, 0 - со мной): ')
    if mode == '1' or mode == '0':
        break
    print('вы ввели некорректные данные')
if mode == '1':
    player_1 = 'Игрок1'
    player_2 = 'Игрок2'
    turn = take_turn(player_1, 'X')

draw_board()