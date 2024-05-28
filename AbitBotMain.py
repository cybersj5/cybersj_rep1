from aiogram import Bot, Dispatcher, types
import asyncio
from app.handlers import router
import telebot
import sqlite3
from telebot import types
from aiogram.filters import CommandStart, Command
from time import sleep






registration = False
docs = False
full_name = None
snils = None


async def main():
    bot = Bot(token='7006292589:AAFikVQR1SSuXX5RsHxmWrYba3tgpHc265M')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == ' __ main __ ':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')






