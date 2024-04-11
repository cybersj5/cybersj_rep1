import telebot
from telebot import types
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
    bot.send_message(message.chat.id, "Введите СНИЛС")
    bot.register_next_step_handler(message, reg3)



def reg3(message): #кнопка главное меню
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Открыть главное меню"))
    bot.send_message(message.chat.id, "Отлично,вы зарегестрированы, откройте главное меню",reply_markup=markup)
    bot.register_next_step_handler(message, reg4)
def reg4(message): #Главное меню
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Место в списке абитуриентов",callback_data="place"))
    markup.add(types.InlineKeyboardButton("Подать аттестат", callback_data="docs"))
    markup.add(types.InlineKeyboardButton("АИС Абитуриент", url="https://abiturient.sfu-kras.ru"))
    markup.add(types.InlineKeyboardButton("Группа в ВК",url="https://vk.com/dovuz_sfu?from=search"))
    if message.text == "Открыть главное меню":
        bot.send_message(message.chat.id, "Ты находишься в главном меню, воспользуйся одной из функций", reply_markup=markup)

#def callback(callback):
#    if callback.data == "docs":
#    elif callback.data == "place":

bot.polling(none_stop = True)