import telebot
import sqlite3

bot=telebot.TeleBot("7006292589:AAFikVQR1SSuXX5RsHxmWrYba3tgpHc265M")

@bot.message_handler(comands=['start'])
def start(message):
    connection = sqlite3.connect("Users.db")
    curse = connection.cursor()


    curse.execute('CREATE TABLE IF NOT EXISTS '
                  'Users'
                  '(id int auto_increment primary key, '
                  'full_name varchar(100),'
                  'snils varchar(11),'
                  'exam_scores int)')
    connection.commit()
    curse.close
    connection.close

    bot.send_message(message.chat.id,"Данные внесены")






bot.polling(none_stop=True)