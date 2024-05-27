from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Место в списке абитуриентов', callback_data='place')]
        [InlineKeyboardButton(text='📝 Подать/Забрать аттестат', callback_data='docs')]
        [InlineKeyboardButton(text='⚙ АИС Абитуриент', url='https://abiturient.sfu-kras.ru')]
        [InlineKeyboardButton(text=f"🐿 Группа в ВК {"Поступай в СФУ"}", url= 'https://vk.com/dovuz_sfu?from=search')]])
start_reg = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='🚀 Зарегистрироваться')]])


institutes = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ИКИТ')]])

directions = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Прикладная информатика')]
                                           [KeyboardButton(text='Программная инженерия')]])

open_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Открыть главное меню')]])

