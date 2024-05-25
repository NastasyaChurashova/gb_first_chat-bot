import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import config
import random

# Словарь с шуточными прогнозами для каждого знака зодиака
horoscopes = {
    "Овен": "Сегодня отличный день для новых начинаний! Или хотя бы для начала того, что вы откладывали всю неделю.",
    "Телец": "Вам предстоит удивительное открытие: холодильник не заполняется сам.",
    "Близнецы": "Сегодня вы будете настолько многозадачны, что сможете одновременно смотреть сериал и не делать ничего полезного.",
    "Рак": "Звезды говорят, что сегодня лучший день для просмотра милых видео с котиками.",
    "Лев": "Ваше обаяние сегодня на высоте. Только постарайтесь не обжечься от собственного сияния.",
    "Дева": "Идеальный день для планирования будущего. Или хотя бы для планирования того, что вы будете есть на ужин.",
    "Весы": "Ваш внутренний мир будет гармоничен. Главное — не смотреть новости.",
    "Скорпион": "Сегодня вас ждут загадочные события. Начните с разгадки тайны пропавшего носка.",
    "Стрелец": "Сегодня отличный день для приключений! Но сначала доведите до конца приключение с уборкой квартиры.",
    "Козерог": "Вы будете настолько продуктивны, что даже ваш список дел начнет уменьшаться. Возможно.",
    "Водолей": "Сегодня вы найдете ответы на все вопросы. Кроме того, почему вы не можете найти ключи.",
    "Рыбы": "Идеальный день для творчества. Создайте шедевр, даже если это просто красивая картинка на обоях."
}

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer("Привет, {0.first_name}! Введите ваш знак зодиака для получения прогноза.".format(message.from_user))

@dp.message(Command(commands=['stop']))
async def stop(message: types.Message):
    await message.answer("До встречи, {0.first_name}!".format(message.chat))

@dp.message(Command(commands=['info']))
async def info(message: types.Message):
    await message.answer("Этот бот дает шуточные гороскопы. Введите ваш знак зодиака, чтобы получить прогноз.")

@dp.message(lambda message: message.text)
async def get_horoscope_message(message: types.Message):
    sign = message.text.capitalize()
    horoscope = horoscopes.get(sign, "Простите, я не знаю такого знака зодиака. Попробуйте еще раз.")
    await message.answer(horoscope)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
