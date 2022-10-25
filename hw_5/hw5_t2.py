from random import randint
from time import sleep

def game_candies_players(p1, p2):   # для игры с другим игроком
    candies = 2021
    turn = 1
    min = 1
    max = 278     #для ускорения процесса
    while candies > 0:
        if turn % 2 == 1:
            choise = int(input(f'на столе лежит конфет: {candies} \n{p1}, возьмите от {min} до {max} конфет: '))
            while choise < min or choise > max or choise > candies:
                choise = int(input('вы ввели некорректное количество, прошу повторите: '))
            candies -= choise
            if candies == 0:
                return p1
            turn += 1
        else:
            choise = int(input(f'на столе лежит конфет: {candies} \n{p2}, возьмите от {min} до {max} конфет: '))
            while choise < min or choise > max or choise > candies:
                choise = int(input('вы ввели некорректное количество, прошу повторите: '))
            candies -= choise
            if candies == 0:
                return p2
            turn += 1


def game_candies_comp(p1, turn_p1): #для игры с компьютером
    candies = 2021
    turn = turn_p1
    min = 1
    max = 278     # для ускорения процесса
    while candies > 0:
        if turn % 2 == 1:
            choise = int(input(f'на столе лежит конфет: {candies} \n{p1}, возьмите от {min} до {max} конфет: '))
            while choise < min or choise > max or choise > candies:
                choise = int(input('вы ввели некорректное количество, прошу повторите: '))
            candies -= choise
            if candies == 0:
                return p1
            turn += 1
        else:
            if turn < 5:
                choise = randint(min, max) # сделаем поблажку для игрока
            else:
                choise = candies % (max + min)
                if choise == 0:   # преимущество не у компьютера
                    choise = randint(min, max)
            print(f'мой ход, я беру конфет: {choise}')
            candies -= choise
            if candies == 0:
                return 'SUPERCOMP'
            turn += 1

first_message = 'ПРИВЕТСВУЮ вас в игре "забери конфеты"!\n'
first_message += 'На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n' \
                 'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n' \
                 'Все конфеты оппонента достаются сделавшему последний ход.'
print(first_message)
sleep(7)
mode = input('выберите режим игры (1 - с другим игроком, 0 - со мной): ')
if mode == '1':
    print('вы играете с другим человеком, сейчас жребий определит, кто будет ходить (игрок1 - тот, кто старше)')
    sleep(3)
    player_1 = input('но для начала представьтесь: как зовут игрока1? ')
    player_2 = input('как зовут игрока2? ')
    print(f'приятно познакомиться, {player_1} и {player_2}! подкидываю монетку....')
    sleep(5)
    start_turn = randint(0,1)
    if start_turn == 0:
        print(f'{player_1} ходит первым')
        winner = game_candies_players(player_1, player_2)
    else:
        print(f'{player_2} ходит первым')
        winner = game_candies_players(player_2, player_1)
if mode == '0':
    player_1 = input('Вы играете со мной, позвольте представится, меня зовут SUPERCOMP, а вас: ')
    print(f'приятно познакомиться, {player_1}, сейчас жребий определит, кто будет ходить первый \nкидаю мнетку....')
    sleep(5)
    start_turn = randint(0, 1)
    if start_turn == 0:
        print(f'{player_1} ходит первым')
        winner = game_candies_comp(player_1, 1)
    else:
        print(f'я хожу первым')
        winner = game_candies_comp(player_1, 2)
if winner == 'SUPERCOMP':
    print('Ураа! я поюедил! все конфеты мои! не расстраивайтесь - повезет в следующий раз.')
else:
    print(f'конец игры. победитель: . Победитель забирает все конфеты с собой!')