from aiogram import Bot, Dispatcher, types
from aiogram import executor
import sqlite3
from telebot import types
from time import sleep






registration = False
docs = False
full_name = None
snils = None


bot = Bot('7006292589:AAFikVQR1SSuXX5RsHxmWrYba3tgpHc265M')
dp = Dispatcher(bot)







@dp.message_handler(commands = ['start'])
async def start(message):
    if registration == True:
        await bot.send_message(message.chat.id,
                         "Привет! Я бот Abit-SFU, я помогу тебе отслеживать твою позицию в списках абитуриентов СФУ.")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 Место в списке абитуриентов", callback_data='place'))
        markup.add(types.InlineKeyboardButton("📝 Подать/Забрать аттестат", callback_data='docs'))
        markup.add(types.InlineKeyboardButton("⚙ АИС Абитуриент", url='https://abiturient.sfu-kras.ru'))
        markup.add(types.InlineKeyboardButton(f"🐿 Группа в ВК {"Поступай в СФУ"}", url='https://vk.com/dovuz_sfu?from=search'))
        await bot.send_message(message.chat.id, "Вы находитесь в главном меню!\n\n Чтобы узнать свое место в списках поступающих, нажмите <b>Место в списке абитуриентов</b>\n\n Если вы подали аттестат в СФУ, то нажмите <b>Подать аттестат</b>\n\n Чтобы перейти в АИС Абитуриент, нажмите <b>АИС Абитуриент</b>\n\n Чтобы перейти в группу в ВК, нажмите <b>Группа в ВК</b>\n\n", reply_markup=markup, parse_mode='html')
    if registration == False:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('🚀 Зарегистрироваться', callback_data='reg'))
        await bot.send_message(message.chat.id,
                         "Привет! Я бот Abit-SFU, я помогу тебе отслеживать твою позицию в списках абитуриентов СФУ. Для начала давай зарегистрируемся.", reply_markup=markup)



@dp.message_handler()
async def menu(message):
    if message.text.lower() == 'открыть главное меню':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 Место в списке абитуриентов", callback_data='place'))
        markup.add(types.InlineKeyboardButton("📝 Подать/Забрать аттестат", callback_data='docs'))
        markup.add(types.InlineKeyboardButton("⚙ АИС Абитуриент", url='https://abiturient.sfu-kras.ru'))
        markup.add(types.InlineKeyboardButton(f"🐿 Группа в ВК {"Поступай в СФУ"}", url='https://vk.com/dovuz_sfu?from=search'))
        await bot.send_message(message.chat.id,
                         "Вы находитесь в главном меню!\n\n Чтобы узнать свое место в списках поступающих, нажмите <b>Место в списке абитуриентов</b>\n\n Если вы подали аттестат в СФУ, то нажмите <b>Подать аттестат</b>\n\n Чтобы перейти в АИС Абитуриент, нажмите <b>АИС Абитуриент</b>\n\n Чтобы перейти в группу в ВК, нажмите <b>Группа в ВК</b>\n\n",
                         reply_markup=markup, parse_mode='html')


@dp.callback_query_handler(func=lambda callback: True)


async def callback_message(callback):

    if callback.data == 'reg':
        main_message = callback.message
        await bot.send_message(main_message.chat.id, "Введите ФИО")
        await bot.register_next_step_handler(main_message, reg2)

    if callback.data == 'menu':
        main_message = callback.message
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 Место в списке абитуриентов", callback_data='place'))
        markup.add(types.InlineKeyboardButton("📝 Подать/Забрать аттестат", callback_data='docs'))
        markup.add(types.InlineKeyboardButton("⚙ АИС Абитуриент", url='https://abiturient.sfu-kras.ru'))
        markup.add(
            types.InlineKeyboardButton(f"🐿 Группа в ВК {"Поступай в СФУ"}", url='https://vk.com/dovuz_sfu?from=search'))
        await bot.send_message(main_message.chat.id,
                         "Вы находитесь в главном меню!\n\n Чтобы узнать свое место в списках поступающих, нажмите <b>Место в списке абитуриентов</b>\n\n Если вы подали аттестат в СФУ, то нажмите <b>Подать аттестат</b>\n\n Чтобы перейти в АИС Абитуриент, нажмите <b>АИС Абитуриент</b>\n\n Чтобы перейти в группу в ВК, нажмите <b>Группа в ВК</b>\n\n",
                         reply_markup=markup, parse_mode='html')

    global docs
    global full_name
    if callback.data == 'docs':
        if docs == True:
            docs = False
            await bot.send_message(callback.message.chat.id, '<b>Позиция аттестата:</b> Аттестат не подан!', parse_mode='html')
        else:
            docs = True
            await bot.send_message(callback.message.chat.id, '<b>Позиция аттестата:</b> Аттестат подан!', parse_mode='html')


    if callback.data == 'place':
        main_message = callback.message
        global snils
        markup = types.ReplyKeyboardMarkup()
        institutes = ['ИКИТ']
        for mark in institutes:
            markup.add(types.KeyboardButton(f"{mark}"))
        await bot.send_message(main_message.chat.id, "Выберите институт", reply_markup=markup)
        await bot.register_next_step_handler(main_message, place1)




async def reg2(message):
    global full_name
    full_name = message.text.strip()
    await bot.send_message(message.chat.id, "Введите СНИЛС")
    await bot.register_next_step_handler(message, reg3)

async def reg3(message):  # кнопка главное меню
    global snils
    global registration
    snils = message.text.strip()
    connection = sqlite3.connect("Users.db")  # запись в бд пользователй
    curse = connection.cursor()
    userNote = [full_name, snils]
    curse.execute("INSERT OR IGNORE INTO Users  VALUES (?,?)", userNote)
    connection.commit()
    curse.close
    connection.close
    registration = True

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Открыть главное меню", callback_data= 'menu'))
    await bot.send_message(message.chat.id, "Отлично,вы зарегестрированы, откройте главное меню",
                     reply_markup=markup)
async def place1(message):
    if message.text.lower() == 'икит':
        directions = ['Прикладная информатика', 'Программная инженерия']
        markup = types.ReplyKeyboardMarkup()
        for mark in directions:
            markup.add(types.KeyboardButton(f'{mark}'))
        await bot.send_message(message.chat.id, "Выберите направление", reply_markup=markup)
        await bot.register_next_step_handler(message, place2)
async def place2(message):
    if message.text.lower() == 'прикладная информатика':
        place = 0
        check = False
        if docs == False:
            connection = sqlite3.connect('applicants_of_AppInformatics.db')
            cursor = connection.cursor()
            cursor.execute("""SELECT full_name, snils, exam_scores
                                     FROM Applied_Informatics
                                     ORDER BY exam_scores
                                     DESC""")
            connection.commit()
            for rec in cursor:
                place += 1
                if str(rec[0]) == str(full_name) and str(rec[1]) == str(snils):
                    check = True
                    markup = types.InlineKeyboardMarkup()
                    markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
                    await bot.send_message(message.chat.id, f'Твоё место в списке: {place}', reply_markup=markup)
                    break
            if check == False:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
                await bot.send_message(message.chat.id, '<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, обратитесть за решением проблемы в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>', reply_markup=markup, parse_mode='html')


        else:
            connection = sqlite3.connect('applicants_of_AppInformatics.db')
            cursor = connection.cursor()
            cursor.execute("""SELECT full_name, snils, exam_scores
                              FROM Applied_Informatics
                              WHERE certificate = true
                              ORDER BY exam_scores
                              DESC""")
            connection.commit()
            for rec in cursor:
                place += 1
                if str(rec[0]) == str(full_name) and str(rec[1]) == str(snils):
                    check = True
                    markup = types.InlineKeyboardMarkup()
                    markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
                    await bot.send_message(message.chat.id, f'Твоё место в списке: {place}', reply_markup=markup)
                    break
            if check == False:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
                await bot.send_message(message.chat.id,
                                 '<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, обратитесть за решением проблемы в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>',
                                 reply_markup=markup, parse_mode = 'html')


    if message.text.lower() == 'программная инженерия':
        place = 0
        check = False
        if docs == False:
            connection = sqlite3.connect('applicants_of_SoftEngineering.db')
            cursor = connection.cursor()
            cursor.execute("""SELECT full_name, snils, exam_scores
                              FROM Software_Engineering
                              ORDER BY exam_scores
                              DESC""")
            connection.commit()
            for rec in cursor:
                place += 1
                if str(rec[0]) == str(full_name) and str(rec[1]) == str(snils):
                    check = True
                    markup = types.InlineKeyboardMarkup()
                    markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
                    await bot.send_message(message.chat.id, f'Твоё место в списке: {place}', reply_markup=markup)
                    break
            if check == False:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
                await bot.send_message(message.chat.id,
                                        '<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, обратитесть за решением проблемы в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>',
                                         reply_markup=markup, parse_mode='html')


        else:
            connection = sqlite3.connect('applicants_of_SoftEngineering.db')
            cursor = connection.cursor()
            cursor.execute("""SELECT full_name, snils, exam_scores
                              FROM Software_Engineering
                              WHERE certificate = true
                              ORDER BY exam_scores
                              DESC""")
            connection.commit()
            for rec in cursor:
                place += 1
                if str(rec[0]) == str(full_name) and str(rec[1]) == str(snils):
                    check = True
                    markup = types.InlineKeyboardMarkup()
                    markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
                    await bot.send_message(message.chat.id, f'Твоё место в списке: {place}', reply_markup=markup)
                    break
            if check == False:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
                await bot.send_message(message.chat.id,
                                         '<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, обратитесть за решением проблемы в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>',
                                         reply_markup=markup, parse_mode='html')






while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(15)

"""bot.polling(none_stop = True)"""