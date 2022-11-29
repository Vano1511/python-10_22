import model
import viewer
import telebot

bot = telebot.TeleBot(some_token)
person = None
mess = None
@bot.message_handler(commands=['start', 'help'])
def welcome_methode(message):
    global mess
    mess = message
    text = f"Привет, {message.from_user.first_name}, я бот, который отвечает за твой телефонный справочник"
    bot.send_message(message.chat.id, text)
    menu()

def menu():
    global mess
    text = '\nвыбери пункт из меню'
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    all_inf = telebot.types.KeyboardButton('Показать всю кгигу')
    find_smb = telebot.types.KeyboardButton('Найти контакт(потом можно удалить)')
    add_to_db = telebot.types.KeyboardButton('Добавить контакт')
    exit = telebot.types.KeyboardButton('Выйти из справочника')
    markup.add(all_inf, add_to_db, find_smb, exit)
    bot.send_message(mess.chat.id, text, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def working_methode(message):
    global person
    if message.text == 'Показать всю кгигу':
        text = viewer.show_all()
        bot.send_message(message.chat.id, text)
    elif message.text == 'Найти контакт(потом можно удалить)':
        bot.send_message(message.chat.id, text='введи что будем искать')
    elif message.text == 'Добавить контакт':
        data = bot.send_message(message.chat.id, 'введите данные(Фамилия Имя Телефон Описание)\n по порядку и через пробел')
        bot.register_next_step_handler(data, enter_contact)
    elif message.text == 'Выйти из справочника':
        bot.send_message(message.chat.id, 'до свидания, чтоб опять меня позвать, нажми /start')
        exit()
    else:
        text, person = viewer.finder(message.text)
        if text != 'по вашему запросу ничего не найдено':
            text += '\n\nЖелаете удалить?(если контактов несколько, то последнего удалю)'
            yes_no = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            yes_no.add(telebot.types.KeyboardButton('Да'), telebot.types.KeyboardButton('Нет'))
            msg = bot.send_message(message.chat.id, text, reply_markup=yes_no)
            bot.register_next_step_handler(msg, deleter)
        else:
            bot.send_message(message.chat.id, text)
            menu()

def deleter(message):
    global person
    if message.text == 'Да':
        if person:
            bot.send_message(message.chat.id, model.delete_contact(person))
        else:
            bot.send_message(message.chat.id, 'нечего удалять')
    else:
        bot.send_message(message.chat.id, 'как скажешь')
    menu()

def enter_contact(msg):
    new_string = msg.text.split()
    with open('phones.csv', 'a', encoding='utf-8') as file: # непосредственно запись в справочник
        new_row = ''
        for item in new_string:
            new_row += str(item).title() + ','
        new_row = new_row[:len(new_row)-1]   #    убираем последнюю запятую
        file.write(new_row + '\n')
        bot.send_message(msg.chat.id, 'Запись добавлена успешно ')
    model.sorting()
    menu()



# bot.polling(non_stop=True)
