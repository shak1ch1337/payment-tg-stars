#!/usr/bin/python3

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


bot = Bot("8383832019:AAFoSKS4EsiK2TDpso_qXSvhHwxpWGXZH80")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(text = "Hello! I'm bot for VPN!")



async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

print("Hello World!")