import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from checkWord import chechWord
import asyncio

API_token = '8016762769:AAHDtOi6gOhLJlDiacQE5QN8XdTvHRooY6U'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_token)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def send_welcome(message: Message):
    await message.reply("uz_imlo Botiga xush kelibsiz 👋!")

@dp.message(Command(commands=["help"]))
async def help_user(message: Message):
    await message.reply("Botdan foydalanish uchun soz yuboring 😁")

@dp.message()
async def check_imlo(message: Message):
    word = message.text
    result = chechWord(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌ {word.capitalize()}\n"
        # for text in result["matches"]:
        #     response += f"✅ {text.capitalize()}\n"
    await message.answer(response)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
