from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Место в списке абитуриентов', callback_data='place')],
        [InlineKeyboardButton(text='📝 Подать/Забрать аттестат', callback_data='docs')],
        [InlineKeyboardButton(text='⚙ АИС Абитуриент', url='https://abiturient.sfu-kras.ru')],
        [InlineKeyboardButton(text="🐿 Группа в ВК", url= 'https://vk.com/dovuz_sfu?from=search')]])
start_reg = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='🚀 Зарегистрироваться', callback_data='reg')]])


institutes = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ИКИТ')],
                                           [KeyboardButton(text='ГИ')]], resize_keyboard=True, input_field_placeholder='Выберите институт...', one_time_keyboard=True)

directions_IKIT = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Прикладная информатика')],
                                           [KeyboardButton(text='Программная инженерия')]], resize_keyboard=True, input_field_placeholder='Выберите Специальность...', one_time_keyboard=True)
directions_GI = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Прикладная информатика')],
                                           [KeyboardButton(text='Религиоведение')]], resize_keyboard=True, input_field_placeholder='Выберите Специальность...', one_time_keyboard=True)

open_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='🛠 Вывести главное меню')],
                                          [KeyboardButton(text='Изменить\nСНИЛС'),
                                          KeyboardButton(text='Изменить\nФИО'),
                                          KeyboardButton(text='Изменить\nбаллы ЕГЭ')],
                                          [KeyboardButton(text='👨‍💻 Посмотреть мои данные')]], resize_keyboard=True)


