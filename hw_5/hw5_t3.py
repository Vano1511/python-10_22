from random import randint, choice
from termcolor import colored   # для обрисовки цветом

x = colored('X', 'red', attrs=['bold'])
o = colored('O', 'green', attrs=['bold'])

def main(pl1, pl2):   # тело игры
    print('сейчас выберем, кто первый будет ходить: кидаю монетку...')
    first = randint(0, 1)
    player = pl1
    draw_board()
    if first == 1:
        player = pl2  # меняем местами, так как ходит первым Игрок2
    if player == 'SUPERBOT':
        print('Я хожу первым')
    else:
        print(f'{player} ходит первым')
    char = x  # Х всегда ходит первым
    counter = 1  # считаем ходы
    while True:
        turn = take_turn(player, char)
        board[turn - 1] = char
        draw_board()
        if counter > 4:  # есть смысл проверять только на пятом ходу
            result = check_win(board)
            if result:
                if player == 'SUPERBOT':
                    print(f'Я победил на {counter}-м ходу! не расстраивайся, повезет в другой раз')
                else:
                    print(f'на {counter}-м ходу победил {player}, поздравляем!')
                break
        char, player = char_player_change(char, player)  # смена хода
        counter += 1
        if counter > 9:
            print('ходы закончились, ничья')
            break

def draw_board(): #рисуем поле
    print('-'* 19)
    for i in range(3):
        print(f'|  {board[0+i*3]}  |  {board[1+i*3]}  |  {board[2+i*3]}  |')
        print('-' * 19)

def take_turn(player, char):  # ввод и проверка хода
    flag = True
    while flag:
        if player == 'SUPERBOT':
            vision = []
            for element in board:
                if element != x and element != o:
                    vision.append(element)
            turn = choice(vision)
            print(f'я ставлю в поле {turn}')
        else:
            turn = input(f'{player}, куда поставишь {char} ? ')
        try:                                           #  введено ли число
            turn = int(turn)
        except:
            print('введено не число!')
            continue
        if turn not in range(1, 10):           # входит ли в диапазон
            print('введено некорректное число, повтори')
            continue
        elif str(board[turn-1]) in (x, o):           # проверка не занята ли клетка
            print('клетка уже занята! повтори')
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


print('приветствую вас в игре крестики-нолики!\n')
decision = input('ну что, начнем? (0 - нет, 1 - да) ')
while True:   #  запускаем игру
    if decision == '0':
        break
    elif decision != '1':
        decision = input('вы ввели некорректный выбор 1- да, 0- нет ')
        continue
    while True:            # проверка правильности ввода данных
        mode = input('\nвведите номер режима игры(1- с игроком, 0 - со мной): ')
        if mode == '1' or mode == '0':
            break
        print('вы ввели некорректные данные')
    board = [el for el in range(1, 10)]  # поля с результатом
    if mode == '1':
        main('Игрок1', 'Игрок2')
    else:
        print('ну что, я играю с вами, я SUPERBOT')
        main('Игрок', 'SUPERBOT')
    decision = input('\nну что, хотите сыграть еще раз? 1 - да, 0 - нет ')
print('\nспасибо, что заглянули!')


