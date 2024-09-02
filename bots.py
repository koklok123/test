import logging
import random
import asyncio
from aiogram import Bot, Dispatcher, types


API_TOKEN = '7350431741:AAFawplWEL4ArfIeleEUkzWQAdVVgAhVrZg'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Угадай число от 1 до 3")

@dp.message_handler()
async def guess_number(message: types.Message):
    try:
        guessed_number = int(message.text)
        if guessed_number < 1 or guessed_number > 3:
            await message.reply("Введите число от 1 до 3")
            return

        random_number = random.randint(1, 3)
        if guessed_number == random_number:
            await message.reply("Вы отгадали")
            await bot.send_photo(message.chat.id, 'https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
        else:
            await message.reply(f"Неправильно, я загадал {random_number}.")
            await bot.send_photo(message.chat.id, 'https://media.makeameme.org/created/sorry-you-lose.jpg')
    except ValueError:
        await message.reply("Пожалуйста, введите число")

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
