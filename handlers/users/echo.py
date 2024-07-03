from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.reply("Noto'g'ri kommandani yuboryabsz ! \nIltimos to'g'ri kommandani yuboring yoki kerakli bo'limni tanlang.")
