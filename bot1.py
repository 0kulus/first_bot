import logging
from aiogram import Bot,Dispatcher, types, executor

Token = '6046823301:AAEIUKTo-xAxYgq21rtHWetCvFAaKXzM-1U'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=Token, proxy=proxy_url)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp)
