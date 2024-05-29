import app.keyboards as kb
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, command
import sqlite3
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class User_states(StatesGroup):
    no_reg = State()
    reg = State()
    full_name = State()
    exam_scores = State()
    snils = State()
    docs = State()
    choice_institute = State()
    choice_direction = State()
    list_contains = State()
    change_snils = State()
    change_full_name = State()
    change_scores = State()











# Начало, команда СТАРТ
@router.message(CommandStart(), User_states.reg)
async def start(message: Message, state: FSMContext):
    await state.set_state(User_states.no_reg)
    await message.answer(
                        "Привет! С помощью этого бота ты можешь отслеживать свою позицию в конкурсных списках абитуриентов СФУ. Для начала давай зарегистрируемся.", reply_markup=kb.start_reg)

# Команда СТАРТ после регистрации
# @router.message(CommandStart(), User_states.reg)
# async def start_menu(message: Message):
#     await message.answer(
#         "Вы находитесь в главном меню!\n\n Чтобы узнать свое место в списках поступающих, нажмите <b>Место в списке абитуриентов</b>\n\n Если вы подали аттестат в СФУ, то нажмите <b>Подать аттестат</b>\n\n Чтобы перейти в АИС Абитуриент, нажмите <b>АИС Абитуриент</b>\n\n Чтобы перейти в группу в ВК <i>Поступай в СФУ</i>, нажмите <b>Группа в ВК</b>\n\n",
#         reply_markup=kb.menu, parse_mode='html')

"""ОБРАБОТЧИКИ ТЕКСТА"""

# Открытие главного меню по кнопке
@router.message(F.text == '🛠 Вывести главное меню', User_states.reg)
async def menu(message: Message):
    await message.answer("Вы находитесь в главном меню!\n\n Чтобы узнать свое место в списках поступающих, нажмите <b>Место в списке абитуриентов</b>\n\n Если вы подали аттестат в СФУ, то нажмите <b>Подать аттестат</b>\n\n Чтобы перейти в АИС Абитуриент, нажмите <b>АИС Абитуриент</b>\n\n Чтобы перейти в группу в ВК <i>Поступай в СФУ</i>, нажмите <b>Группа в ВК</b>\n\n",
                         reply_markup=kb.menu, parse_mode='html')
# Просмотр данных
@router.message(F.text == '👨‍💻 Посмотреть мои данные')
async def watch_data(message: Message, state: FSMContext):
    user_data = await state.get_data()
    full_name = user_data['full_name']
    snils = user_data['snils']
    exam_scores = user_data['exam_scores']
    await message.answer(f'<b>Ваше ФИО:</b> {full_name}\n<b>Ваш номер СНИЛС:</b> {snils}\n<b>Ваши Баллы ЕГЭ:</b> {exam_scores}', parse_mode='html')

# ИЗМЕНЕНИЕ ДАННЫХ
@router.message(F.text == 'Изменить\nСНИЛС')
async def change_snils_start(message: Message, state: FSMContext):
    await state.set_state(User_states.change_snils)
    await message.answer('Введите номер СНИЛС')
@router.message(User_states.change_snils)
async def change_snils(message: Message, state: FSMContext):
    await state.set_state(User_states.reg)
    await state.update_data(snils=message.text)
    await message.answer('Готово!')

@router.message(F.text == 'Изменить\nФИО')
async def change_full_name_start(message: Message, state: FSMContext):
    await state.set_state(User_states.change_full_name)
    await message.answer('Введите ФИО')
@router.message(User_states.change_full_name)
async def change_full_name(message: Message, state: FSMContext):
    await state.set_state(User_states.reg)
    await state.update_data(full_name=message.text)
    await message.answer('Готово!')

@router.message(F.text == 'Изменить\nбаллы ЕГЭ')
async def change_scores_start(message: Message, state: FSMContext):
    await state.set_state(User_states.change_scores)
    await message.answer('Введите количество баллов ЕГЭ')
@router.message(User_states.change_scores)
async def change_scores(message: Message, state: FSMContext):
    await state.set_state(User_states.reg)
    await state.update_data(exam_scores=message.text)
    await message.answer('Готово!')


"""CALLBACK_DATA"""
# Начальная регистрация пользователя
@router.callback_query(F.data == 'reg', User_states.no_reg)
async def reg(callback: CallbackQuery, state: FSMContext):
    await state.set_state(User_states.full_name)
    await callback.message.answer('Введите ваше ФИО')
@router.message(User_states.full_name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(User_states.exam_scores)
    await message.answer('Введите своё количество баллов ЕГЭ')
@router.message(User_states.exam_scores)
async def register_scores(message: Message, state: FSMContext):
    await state.update_data(exam_scores=int(message.text))
    await state.set_state(User_states.snils)
    await message.answer('Введите свой номер СНИЛС')
@router.message(User_states.snils)
async def register_snils(message: Message, state: FSMContext):
    await state.update_data(snils=message.text)
    await state.update_data(no_reg=False)
    await state.update_data(docs=False)
    await state.update_data(list_contains=False)
    await state.set_state(User_states.reg)
    await message.answer('Отлично, вы зарегистрированы!\nПерейдите в главное меню', reply_markup=kb.open_menu)

# Кнопка подачи аттестата
@router.callback_query(F.data == 'docs', User_states.reg)
async def docs(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    if user_data['docs'] == False:
        await state.update_data(docs=True)
        await callback.answer('Режим подачи аттестата: ✅')
        await callback.message.answer('Режим подачи аттестата: ✅')
    if user_data['docs'] == True:
        await state.update_data(docs=False)
        await callback.answer('Режим подачи аттестата: 🚫')
        await callback.message.answer('Режим подачи аттестата: 🚫')

# Кнопка показа места в списке
@router.callback_query(F.data == 'place', User_states.reg)
async def get_place_choice_institute(callback: CallbackQuery, state: FSMContext):
    await state.set_state(User_states.choice_institute)
    await callback.message.answer("Выберите институт", reply_markup=kb.institutes)
    await callback.answer('Выберите институт')
    """Институты и их направления"""
# ГИ
@router.message(F.text == 'ГИ', User_states.choice_institute)
async def get_place_choice_direction(message: Message, state: FSMContext):
    await state.set_state(User_states.choice_direction)
    await message.answer('Выберите направление', reply_markup=kb.directions_GI)

@router.message(F.text == 'Прикладная информатика', User_states.choice_direction)
async def get_place(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await state.set_state(User_states.reg)
    place = 0
    _names = user_data["full_name"]
    snils = user_data["snils"]
    exam_scores = user_data["exam_scores"]
    list_contains = user_data["list_contains"]
    connection = sqlite3.connect('applicants_of_AppInformatics.db')
    cursor = connection.cursor()
    cursor.execute("""SELECT *
                      FROM Applied_Informatics""")
    connection.commit()
    for rec in cursor:
        if str(rec[2]) == str(_names) and str(rec[3]) == str(snils):
            list_contains = True
            break
    if user_data["docs"] == False and list_contains == True:
        cursor.execute("""SELECT full_name, snils, exam_scores
                          FROM Applied_Informatics
                          ORDER BY exam_scores
                          DESC""")
        connection.commit()
        for rec in cursor:
            place += 1
            if str(rec[0]) == str(_names) and str(rec[1]) == str(snils) and str(rec[2]) == str(exam_scores):
                await message.answer(f'Твоё место в списке: {place}', reply_markup=kb.open_menu)
                break
    if list_contains == False:
        await message.answer('<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, проверьте правильность ваших данных в боте.\nЕсли всё данные верны, проверьте наличие поданных документов, позвонив в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>', reply_markup=kb.open_menu, parse_mode='html')
    if user_data["docs"] == True and list_contains == True:
        connection = sqlite3.connect('applicants_of_AppInformatics.db')
        cursor = connection.cursor()
        count_recs = int(list(cursor.execute("SELECT count (*) FROM Applied_Informatics"))[0][0])
        applicant_user = [count_recs+1, True, _names, snils, exam_scores]
        cursor.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_user)
        connection.commit()
        cursor.execute("""SELECT full_name, snils, exam_scores
                                  FROM Applied_Informatics
                                  WHERE certificate = True
                                  ORDER BY exam_scores
                                  DESC""")
        connection.commit()
        for rec in cursor:
            place += 1
            if str(rec[0]) == str(_names) and str(rec[1]) == str(snils) and str(rec[2]) == str(exam_scores):
                await message.answer(f'Твоё место в списке: {place}', reply_markup=kb.open_menu)
                break
        cursor.execute(f"DELETE FROM Applied_Informatics WHERE full_name=? AND certificate=?", (str(_names), 1))
        connection.commit()
@router.message(F.text == "Религиоведение", User_states.choice_direction)
async def get_place(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await state.set_state(User_states.reg)
    place = 0
    _names = user_data["full_name"]
    snils = user_data["snils"]
    exam_scores = user_data["exam_scores"]
    list_contains = user_data["list_contains"]
    connection = sqlite3.connect('applicants_of_Religious_studies.db')
    cursor = connection.cursor()
    cursor.execute("""SELECT *
                      FROM Religious_studies""")
    connection.commit()
    for rec in cursor:
        if str(rec[2]) == str(_names) and str(rec[3]) == str(snils):
            list_contains = True
            break
    if user_data["docs"] == False and list_contains == True:
        cursor.execute("""SELECT full_name, snils, exam_scores
                              FROM Religious_studies
                              ORDER BY exam_scores
                              DESC""")
        connection.commit()
        for rec in cursor:
            place += 1
            if str(rec[0]) == str(_names) and str(rec[1]) == str(snils) and str(rec[2]) == str(exam_scores):
                await message.answer(f'Твоё место в списке: {place}', reply_markup=kb.open_menu)
                break
    if list_contains == False:
        await message.answer(
            '<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, проверьте правильность ваших данных в боте.\nЕсли всё данные верны, проверьте наличие поданных документов, позвонив в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>',
            reply_markup=kb.open_menu, parse_mode='html')
    if user_data["docs"] == True and list_contains == True:
        count_recs = int(list(cursor.execute("SELECT count (*) FROM Religious_studies"))[0][0])
        applicant_user = [count_recs + 1, True, _names, snils, exam_scores]
        cursor.execute("INSERT OR IGNORE INTO Religious_studies VALUES(?,?,?,?,?);", applicant_user)
        connection.commit()
        cursor.execute("""SELECT full_name, snils, exam_scores
                                      FROM Religious_studies
                                      WHERE certificate = True
                                      ORDER BY exam_scores
                                      DESC""")
        connection.commit()
        for rec in cursor:
            place += 1
            if str(rec[0]) == str(_names) and str(rec[1]) == str(snils) and str(rec[2]) == str(exam_scores):
                await message.answer(f'Твоё место в списке: {place}', reply_markup=kb.open_menu)
                break
        cursor.execute(f"DELETE FROM Religious_studies WHERE full_name=? AND certificate=?", (str(_names), 1))
        connection.commit()






# ИКИТ
@router.message(F.text == 'ИКИТ', User_states.choice_institute)
async def get_place_choice_direction(message: Message, state: FSMContext):
    await state.set_state(User_states.choice_direction)
    await message.answer('Выберите направление', reply_markup=kb.directions_IKIT)
@router.message(F.text == 'Прикладная информатика', User_states.choice_direction)
async def get_place(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await state.set_state(User_states.reg)
    place = 0
    _names = user_data["full_name"]
    snils = user_data["snils"]
    exam_scores = user_data["exam_scores"]
    list_contains = user_data["list_contains"]
    connection = sqlite3.connect('applicants_of_AppInformatics.db')
    cursor = connection.cursor()
    cursor.execute("""SELECT *
                      FROM Applied_Informatics""")
    connection.commit()
    for rec in cursor:
        if str(rec[2]) == str(_names) and str(rec[3]) == str(snils):
            list_contains = True
            break
    if user_data["docs"] == False and list_contains == True:
        cursor.execute("""SELECT full_name, snils, exam_scores
                          FROM Applied_Informatics
                          ORDER BY exam_scores
                          DESC""")
        connection.commit()
        for rec in cursor:
            place += 1
            if str(rec[0]) == str(_names) and str(rec[1]) == str(snils) and str(rec[2]) == str(exam_scores):
                await message.answer(f'Твоё место в списке: {place}', reply_markup=kb.open_menu)
                break
    if list_contains == False:
        await message.answer('<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, проверьте правильность ваших данных в боте.\nЕсли всё данные верны, проверьте наличие поданных документов, позвонив в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>', reply_markup=kb.open_menu, parse_mode='html')
    if user_data["docs"] == True and list_contains == True:
        connection = sqlite3.connect('applicants_of_AppInformatics.db')
        cursor = connection.cursor()
        count_recs = int(list(cursor.execute("SELECT count (*) FROM Applied_Informatics"))[0][0])
        applicant_user = [count_recs+1, True, _names, snils, exam_scores]
        cursor.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_user)
        connection.commit()
        cursor.execute("""SELECT full_name, snils, exam_scores
                                  FROM Applied_Informatics
                                  WHERE certificate = True
                                  ORDER BY exam_scores
                                  DESC""")
        connection.commit()
        for rec in cursor:
            place += 1
            if str(rec[0]) == str(_names) and str(rec[1]) == str(snils) and str(rec[2]) == str(exam_scores):
                await message.answer(f'Твоё место в списке: {place}', reply_markup=kb.open_menu)
                break
        cursor.execute(f"DELETE FROM Applied_Informatics WHERE full_name=? AND certificate=?", (str(_names), 1))
        connection.commit()
@router.message(F.text == "Программная инженерия", User_states.choice_direction)
async def get_place(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await state.set_state(User_states.reg)
    place = 0
    _names = user_data["full_name"]
    snils = user_data["snils"]
    exam_scores = user_data["exam_scores"]
    list_contains = user_data["list_contains"]
    connection = sqlite3.connect('applicants_of_SoftEngineering.db')
    cursor = connection.cursor()
    cursor.execute("""SELECT *
                          FROM Software_Engineering""")
    connection.commit()
    for rec in cursor:
        if str(rec[2]) == str(_names) and str(rec[3]) == str(snils):
            list_contains = True
            break
    if user_data["docs"] == False and list_contains == True:
        cursor.execute("""SELECT full_name, snils, exam_scores
                              FROM Software_Engineering
                              ORDER BY exam_scores
                              DESC""")
        connection.commit()
        for rec in cursor:
            place += 1
            if str(rec[0]) == str(_names) and str(rec[1]) == str(snils) and str(rec[2]) == str(exam_scores):
                await message.answer(f'Твоё место в списке: {place}', reply_markup=kb.open_menu)
                break
    if list_contains == False:
        await message.answer(
            '<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, проверьте правильность ваших данных в боте.\nЕсли всё данные верны, проверьте наличие поданных документов, позвонив в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>',
            reply_markup=kb.open_menu, parse_mode='html')
    if user_data["docs"] == True and list_contains == True:
        count_recs = int(list(cursor.execute("SELECT count (*) FROM Software_Engineering"))[0][0])
        applicant_user = [count_recs + 1, True, _names, snils, exam_scores]
        cursor.execute("INSERT OR IGNORE INTO Software_Engineering VALUES(?,?,?,?,?);", applicant_user)
        connection.commit()
        cursor.execute("""SELECT full_name, snils, exam_scores
                                      FROM Software_Engineering
                                      WHERE certificate = True
                                      ORDER BY exam_scores
                                      DESC""")
        connection.commit()
        for rec in cursor:
            place += 1
            if str(rec[0]) == str(_names) and str(rec[1]) == str(snils) and str(rec[2]) == str(exam_scores):
                await message.answer(f'Твоё место в списке: {place}', reply_markup=kb.open_menu)
                break
        cursor.execute(f"DELETE FROM Software_Engineering WHERE full_name=? AND certificate=?", (str(_names), 1))
        connection.commit()





















# async def callback_message(callback):
#
#     if callback.data == 'reg':
#         main_message = callback.message
#         await bot.send_message(main_message.chat.id, "Введите ФИО")
#         await bot.register_next_step_handler(main_message, reg2)
#
#     if callback.data == 'menu':
#         main_message = callback.message
#         markup = types.InlineKeyboardMarkup()
#         markup.add(types.InlineKeyboardButton("📍 Место в списке абитуриентов", callback_data='place'))
#         markup.add(types.InlineKeyboardButton("📝 Подать/Забрать аттестат", callback_data='docs'))
#         markup.add(types.InlineKeyboardButton("⚙ АИС Абитуриент", url='https://abiturient.sfu-kras.ru'))
#         markup.add(
#             types.InlineKeyboardButton(f"🐿 Группа в ВК {"Поступай в СФУ"}", url='https://vk.com/dovuz_sfu?from=search'))
#         await bot.send_message(main_message.chat.id,
#                          "Вы находитесь в главном меню!\n\n Чтобы узнать свое место в списках поступающих, нажмите <b>Место в списке абитуриентов</b>\n\n Если вы подали аттестат в СФУ, то нажмите <b>Подать аттестат</b>\n\n Чтобы перейти в АИС Абитуриент, нажмите <b>АИС Абитуриент</b>\n\n Чтобы перейти в группу в ВК, нажмите <b>Группа в ВК</b>\n\n",
#                          reply_markup=markup, parse_mode='html')
#
#     global docs
#     global full_name
#     if callback.data == 'docs':
#         if docs == True:
#             docs = False
#             await bot.send_message(callback.message.chat.id, '<b>Позиция аттестата:</b> Аттестат не подан!', parse_mode='html')
#         else:
#             docs = True
#             await bot.send_message(callback.message.chat.id, '<b>Позиция аттестата:</b> Аттестат подан!', parse_mode='html')
#
#
#     if callback.data == 'place':
#         main_message = callback.message
#         global snils
#         markup = types.ReplyKeyboardMarkup()
#         institutes = ['ИКИТ']
#         for mark in institutes:
#             markup.add(types.KeyboardButton(f"{mark}"))
#         await bot.send_message(main_message.chat.id, "Выберите институт", reply_markup=markup)
#         await bot.register_next_step_handler(main_message, place1)
#
#
#
#
# async def reg2(message):
#     global full_name
#     full_name = message.text.strip()
#     await bot.send_message(message.chat.id, "Введите СНИЛС")
#     await bot.register_next_step_handler(message, reg3)
#
# async def reg3(message):  # кнопка главное меню
#     global snils
#     global registration
#     snils = message.text.strip()
#     connection = sqlite3.connect("Users.db")  # запись в бд пользователй
#     curse = connection.cursor()
#     userNote = [full_name, snils]
#     curse.execute("INSERT OR IGNORE INTO Users  VALUES (?,?)", userNote)
#     connection.commit()
#     curse.close
#     connection.close
#     registration = True
#
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Открыть главное меню", callback_data= 'menu'))
#     await bot.send_message(message.chat.id, "Отлично,вы зарегестрированы, откройте главное меню",
#                      reply_markup=markup)
# async def place1(message):
#     if message.text.lower() == 'икит':
#         directions = ['Прикладная информатика', 'Программная инженерия']
#         markup = types.ReplyKeyboardMarkup()
#         for mark in directions:
#             markup.add(types.KeyboardButton(f'{mark}'))
#         await bot.send_message(message.chat.id, "Выберите направление", reply_markup=markup)
#         await bot.register_next_step_handler(message, place2)
# async def place2(message):
#     if message.text.lower() == 'прикладная информатика':
#         place = 0
#         check = False
#         if docs == False:
#             connection = sqlite3.connect('applicants_of_AppInformatics.db')
#             cursor = connection.cursor()
#             cursor.execute("""SELECT full_name, snils, exam_scores
#                                      FROM Applied_Informatics
#                                      ORDER BY exam_scores
#                                      DESC""")
#             connection.commit()
#             for rec in cursor:
#                 place += 1
#                 if str(rec[0]) == str(full_name) and str(rec[1]) == str(snils):
#                     check = True
#                     markup = types.InlineKeyboardMarkup()
#                     markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
#                     await bot.send_message(message.chat.id, f'Твоё место в списке: {place}', reply_markup=markup)
#                     break
#             if check == False:
#                 markup = types.InlineKeyboardMarkup()
#                 markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
#                 await bot.send_message(message.chat.id, '<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, обратитесть за решением проблемы в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>', reply_markup=markup, parse_mode='html')
#
#
#         else:
#             connection = sqlite3.connect('applicants_of_AppInformatics.db')
#             cursor = connection.cursor()
#             cursor.execute("""SELECT full_name, snils, exam_scores
#                               FROM Applied_Informatics
#                               WHERE certificate = true
#                               ORDER BY exam_scores
#                               DESC""")
#             connection.commit()
#             for rec in cursor:
#                 place += 1
#                 if str(rec[0]) == str(full_name) and str(rec[1]) == str(snils):
#                     check = True
#                     markup = types.InlineKeyboardMarkup()
#                     markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
#                     await bot.send_message(message.chat.id, f'Твоё место в списке: {place}', reply_markup=markup)
#                     break
#             if check == False:
#                 markup = types.InlineKeyboardMarkup()
#                 markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
#                 await bot.send_message(message.chat.id,
#                                  '<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, обратитесть за решением проблемы в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>',
#                                  reply_markup=markup, parse_mode = 'html')
#
#
#     if message.text.lower() == 'программная инженерия':
#         place = 0
#         check = False
#         if docs == False:
#             connection = sqlite3.connect('applicants_of_SoftEngineering.db')
#             cursor = connection.cursor()
#             cursor.execute("""SELECT full_name, snils, exam_scores
#                               FROM Software_Engineering
#                               ORDER BY exam_scores
#                               DESC""")
#             connection.commit()
#             for rec in cursor:
#                 place += 1
#                 if str(rec[0]) == str(full_name) and str(rec[1]) == str(snils):
#                     check = True
#                     markup = types.InlineKeyboardMarkup()
#                     markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
#                     await bot.send_message(message.chat.id, f'Твоё место в списке: {place}', reply_markup=markup)
#                     break
#             if check == False:
#                 markup = types.InlineKeyboardMarkup()
#                 markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
#                 await bot.send_message(message.chat.id,
#                                         '<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, обратитесть за решением проблемы в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>',
#                                          reply_markup=markup, parse_mode='html')
#
#
#         else:
#             connection = sqlite3.connect('applicants_of_SoftEngineering.db')
#             cursor = connection.cursor()
#             cursor.execute("""SELECT full_name, snils, exam_scores
#                               FROM Software_Engineering
#                               WHERE certificate = true
#                               ORDER BY exam_scores
#                               DESC""")
#             connection.commit()
#             for rec in cursor:
#                 place += 1
#                 if str(rec[0]) == str(full_name) and str(rec[1]) == str(snils):
#                     check = True
#                     markup = types.InlineKeyboardMarkup()
#                     markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
#                     await bot.send_message(message.chat.id, f'Твоё место в списке: {place}', reply_markup=markup)
#                     break
#             if check == False:
#                 markup = types.InlineKeyboardMarkup()
#                 markup.add(types.InlineKeyboardButton('Открыть главное меню', callback_data='menu'))
#                 await bot.send_message(message.chat.id,
#                                          '<b>Вас нет в списках!</b>\nЕсли вы подавали документы в СФУ, обратитесть за решением проблемы в приёмную комиссию по телефону:\n<i><b>8 800 550-22-24</b></i>',
#                                          reply_markup=markup, parse_mode='html')