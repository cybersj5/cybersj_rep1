import telebot
import sqlite3
from telebot import types
from time import sleep







docs = False
full_name = None
snils = None

bot = telebot.TeleBot('7006292589:AAFikVQR1SSuXX5RsHxmWrYba3tgpHc265M')







@bot.message_handler(commands = ['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Зарегестрироваться" ))

    bot.reply_to(message,"Привет! Я бот Abit-SFU, я помогу тебе отслеживать твою позицию в списках абитуриентов СФУ, начнём с регистрации! Вам понадобится ввести свои ФИО и номер СНИЛС",reply_markup=markup)
    bot.register_next_step_handler(message,reg1)

def reg1(message):
    if message.text == "Зарегестрироваться":
        bot.send_message(message.chat.id,"Введите ФИО")
    bot.register_next_step_handler(message, reg2)

def reg2(message):
    global full_name
    full_name = message.text.strip()
    bot.send_message(message.chat.id, "Введите СНИЛС")
    bot.register_next_step_handler(message, reg3)



def reg3(message): #кнопка главное меню
    global snils
    snils = message.text.strip()
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Открыть главное меню"))
    bot.send_message(message.chat.id, "Отлично,вы зарегестрированы, откройте главное меню",reply_markup=markup)
    bot.register_next_step_handler(message, reg4)



    connection = sqlite3.connect("Users.db")  # запись в бд пользователй
    curse = connection.cursor()
    userNote = [full_name, snils]
    curse.execute("INSERT OR IGNORE INTO Users  VALUES (?,?)", userNote)

    connection.commit()

    curse.close
    connection.close
def reg4(message): #Главное меню
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Место в списке абитуриентов",callback_data="place"))
    markup.add(types.InlineKeyboardButton("Подать аттестат", callback_data="docs"))
    markup.add(types.InlineKeyboardButton("АИС Абитуриент", url="https://abiturient.sfu-kras.ru"))
    markup.add(types.InlineKeyboardButton("Группа в ВК",url="https://vk.com/dovuz_sfu?from=search"))
    if message.text == "Открыть главное меню":
        bot.send_message(message.chat.id, "Ты находишься в главном меню, воспользуйся одной из функций", reply_markup=markup)

@bot.message_handler()
def menu(message):
    if message.text.lower() == 'открыть главное меню':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Место в списке абитуриентов", callback_data='place'))
        markup.add(types.InlineKeyboardButton("Подать аттестат", callback_data='docs'))
        markup.add(types.InlineKeyboardButton("АИС Абитуриент", url='https://abiturient.sfu-kras.ru'))
        markup.add(types.InlineKeyboardButton("Группа в ВК", url='https://vk.com/dovuz_sfu?from=search'))
        bot.send_message(message.chat.id, 'Ты находишься в главном меню, воспользуйся одной из функций',
                         reply_markup=markup)



# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     global docs
#     place = 0
#     if callback.data == 'docs':
#         if docs == True:
#             docs = False
#         else:
#             docs = True
#
#     elif callback.data == 'place':
#         global full_name
#         global snils
#         if docs == False:
#             connection = sqlite3.connect('applicants_of_AppInformatics.db')
#             cursor = connection.cursor()
#             cursor.execute("""SELECT full_name, snils, exam_scores
#                              FROM Applied_Informatics
#                              ORDER BY exam_scores
#                              DESC""")
#             connection.commit()
#             # for i in cursor: print(i)
#             for rec in cursor:
#                 for element in rec:
#                     if str(element) == str(full_name):
#
#
#             bot.send_message(callback.message.chat.id, f'Твоё место в списке:{place}')













while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(15)

"""bot.polling(none_stop = True)"""