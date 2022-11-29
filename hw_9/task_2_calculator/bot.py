import telebot
from const import TOKEN
from calculator import summ, division, mult, substraction
import logger

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def welcome_handler(message):
    text = 'привет, я бот калькулятор, который может произвести простые операции с введенными вами двумя числами :)'
    text += '\nвыберите с какими числами мы будем работать: '
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    comp = telebot.types.KeyboardButton('/complex')
    irr = telebot.types.KeyboardButton('/irracional')
    markup.add(irr, comp)
    bot.reply_to(message, text, reply_markup=markup)

@bot.message_handler(commands=['complex', 'irracional'])
def calculatoin_handler(message):
    if message.text == '/irracional':
        text = 'Введите выражения типа a+b'
        bot.reply_to(message, text)
        bot.register_next_step_handler(message, irr_calc)
    else:
        text = 'Введите выражения типа (complex)+(complex)'
        bot.reply_to(message, text)
        bot.register_next_step_handler(message, complex_calc)


def irr_calc(msg):
    text = msg.text
    for char in text[1:]:
        if char in '+-/*':
            operation = char
    a, b = list(map(float, text.split(operation)))
    bot.send_message(msg.chat.id, text + f' = {round(finish_operation(a, b, operation), 4)}')
    logger.logging(text + f' = {round(finish_operation(a, b, operation), 4)}')

def complex_calc(msg):
    text = msg.text
    for index, char in enumerate(text):
        if char == 'j':
            operation = text[index+2]
            a = complex(text[:index+2])
            b = complex(text[index+3:])
            break
    bot.send_message(msg.chat.id, text + f' = {finish_operation(a, b, operation)}')
    logger.logging(text + f' = {finish_operation(a, b, operation)}')

def finish_operation(a,b, operation):
    if operation == '+':
        return summ(a, b)
    elif operation == '-':
        return substraction(a, b)
    elif operation == '*':
        return mult(a, b)
    else:
        return division(a, b)

