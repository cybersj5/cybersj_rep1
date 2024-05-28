from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📍 Место в списке абитуриентов', callback_data='place')]
        [InlineKeyboardButton(text='📝 Подать/Забрать аттестат', callback_data='docs')]
        [InlineKeyboardButton(text='⚙ АИС Абитуриент', url='https://abiturient.sfu-kras.ru')]
        [InlineKeyboardButton(text=f"🐿 Группа в ВК {"Поступай в СФУ"}", url= 'https://vk.com/dovuz_sfu?from=search')]])
start_reg = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='🚀 Зарегистрироваться', callback_data='reg')]])


institutes = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ИКИТ')]], resize_keyboard=True, input_field_placeholder='Выберите институт...')

directions = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Прикладная информатика')]
                                           [KeyboardButton(text='Программная инженерия')]], resize_keyboard=True, input_field_placeholder='Выберите Специальность...')

open_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Открыть главное меню')]])

reply_menu = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='📍 Место в списке абитуриентов', callback_data='place')]
        [KeyboardButton(text='📝 Подать/Забрать аттестат', callback_data='docs')]
        [KeyboardButton(text='⚙ АИС Абитуриент', url='https://abiturient.sfu-kras.ru')]
        [KeyboardButton(text=f"🐿 Группа в ВК {"Поступай в СФУ"}", url= 'https://vk.com/dovuz_sfu?from=search')]], resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')
