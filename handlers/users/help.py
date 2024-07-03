from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from data.config import ADMINS
from loader import dp
from data.config import get_admins


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await get_admins()
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
    userID = message.from_user.id
    commands = [ 
               {"/users":"Barcha foydalanuvchilar ro'yxati."},
               {"/admins":"Barcha adminlar ro'yxati."},
               {"/makeAdmin":"Admin tayinlash."},
               {"/kickAdmin":"Adminni olib tashlash."},
               {"/servislar":"EasyPay servislari ro'yxati."},
               {"/channels":"EasyPay botiga ulangan kanallar ro'yxati."},
               {"/update_currency":"Valyuta ma'lumotlarini yangilash"},
               {"/sendcurrency_channels":"Valyuta ma'lumotlarini kanalga yuborish"},
                ]
    if userID in ADMINS:
        txt= "Admin buyruqlari: \n\n"
        for command in commands:
            for key, value in command.items():
                 txt+=f"\t{key} - {value}\n"
        await message.answer(txt)