import telebot
from telebot import types
import constants as c
import game_candies as gc

bot = telebot.TeleBot(c.TOKEN)
msg = None
candies = 0


@bot.message_handler(commands=['start', 'help'])
def welcome_methode(message):
    global msg
    msg = message
    text = f"Привет, {message.from_user.first_name}, я бот, с которым ты можешь поиграть в игру с конфетками. "
    client_choice = types.InlineKeyboardMarkup()
    ask_for_rules = types.InlineKeyboardButton('a правила?', callback_data='rules')
    lets_go = types.InlineKeyboardButton('погнали!!', callback_data='go')
    exiter = types.InlineKeyboardButton('не, это без меня', callback_data='exiting')
    client_choice.add(ask_for_rules, lets_go, exiter)
    bot.send_message(message.chat.id, text, reply_markup=client_choice)

@bot.callback_query_handler(func=lambda c:True)
def check_for_choice(query):
    if query.data == 'rules':
        decision = types.InlineKeyboardMarkup()
        decision.add(types.InlineKeyboardButton('Да', callback_data='yes'), types.InlineKeyboardButton('Нет', callback_data='no'))
        question = c.RULES + '\nНу что, играем?'
        bot.send_message(query.message.chat.id, question, reply_markup=decision)
    elif query.data in ('go', 'yes'):
        game()
    else:
        bot.send_message(query.message.chat.id, 'ну, тогда мне не о чем с тобой разговаривать) пока!')
        exit()


def game():
    global msg, candies
    candies = c.CANDIES  # ресетуем глобальное количество к первоначальному
    turn = gc.choose_turn()   #  выбор первого хода
    start_msg = f'всего конфет : {candies}, за ход можно взять от 1 до {c.MAX_TURN} конфет'
    if candies == c.CANDIES:
        start_msg += '\nкто будет ходить первым определяется случайным образом'
    bot.send_message(msg.chat.id, start_msg)
    if turn == 1:  #  обработка первого хода
        first_entry = bot.send_message(msg.chat.id, 'ты ходишь первый')
        bot.register_next_step_handler(first_entry, validate_player_entry)
    else:
        bot.send_message(msg.chat.id, 'я хожу первый')
        bot.send_message(msg.chat.id, f'я беру конфет : {gc.bot_turn(candies, c.MAX_TURN)} ')
        candies -= gc.bot_turn(candies, c.MAX_TURN)
        bot.send_message(msg.chat.id, f'остаток конфет: {candies}')
        bot.send_message(msg.chat.id, f'твой ход')


@bot.message_handler(content_types=['text'])
def validate_player_entry(message): # проверяем ввод игрока и и когда ввод валидный - пускаем дальше
    global candies
    try:
        if 0 < int(message.text) < 29:
            if int(message.text) <= candies:
                player_turn(message)
            else:
                new_entry = bot.send_message(message.chat.id, 'ты указал количество, большее, чем остаток конфет')
                bot.register_next_step_handler(new_entry, validate_player_entry)
        else:
            new_entry = bot.send_message(message.chat.id, f'ты указал невозмодное количество, надо от 1 до {c.MAX_TURN}')
            bot.register_next_step_handler(new_entry, validate_player_entry)
    except:
        new_entry = bot.send_message(message.chat.id, 'жду пока введешь')
        bot.register_next_step_handler(new_entry, validate_player_entry)

def player_turn(message): # непосредственно пара ходов, начиная с игрока
    global candies
    candies -= int(message.text)
    if candies == 0:  #  проверка на победу
        bot.send_message(message.chat.id, 'поздравляю, ты победил!')
        decision = types.InlineKeyboardMarkup()
        decision.add(types.InlineKeyboardButton('Да', callback_data='yes'),
                     types.InlineKeyboardButton('Нет', callback_data='no'))
        question = '\nНу что, играем еще раз?'
        bot.send_message(message.chat.id, question, reply_markup=decision)
        exit()
    else:
        bot_choice = gc.bot_turn(candies, c.MAX_TURN)
        bot.send_message(msg.chat.id, f'я беру конфет : {bot_choice} ')
        candies -= bot_choice
        if candies == 0:
            bot.send_message(message.chat.id, 'я победил, не отчаивася )')
            decision = types.InlineKeyboardMarkup()
            decision.add(types.InlineKeyboardButton('Да', callback_data='yes'),
                         types.InlineKeyboardButton('Нет', callback_data='no'))
            question = 'Ну что, играем еще раз?'
            bot.send_message(message.chat.id, question, reply_markup=decision)
            exit()
    bot.send_message(message.chat.id, f'остаток конфет: {candies}')
    bot.send_message(message.chat.id, f'твой ход')


bot.polling(none_stop=True)