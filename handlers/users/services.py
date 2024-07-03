from loader import dp
from aiogram import types
from keyboards.default.servislar import services_list, apply_btn
from data import connector
from utils.misc.textmaker import makeService
from keyboards.default.startsDefBtns import startDefBtns
from loader import bot
import time

services = connector.session.query(connector.Services).all()
@dp.message_handler(text="👨‍💻 EasyPAY xizmatlari ro'yxati")
async def service_show_handler(message: types.Message):
    services = connector.session.query(connector.Services).all()
    if services and type(services) == list:
        await message.answer("Pastdan kerakli xizmatni tanglang: ", reply_markup=services_list)
    else:
        await message.answer("Bizda hozirda xizmatlar vaqtinchalik mavjud emas.")

@dp.message_handler(text="📞 Xizmatdan foydalanish")
async def service_show_handler(message: types.Message):
    username = "Nomalum"
    fullname = "Nomalum"
    userID = message.from_user.id
    ADMINS = [5944280734] + await connector.select_admins()
    try:
        username=message.from_user.username
    except:
        username=username
    try:
        fullname=message.from_user.full_name
    except:
        fullname=fullname
    text = "Hurmatli ADMIN xizmat uchun murojaat kelib tushdi:\n\n"
    text += f"Foydalanuvchi ma'lumotlari quyidagicha:\n"
    text += f"<b>Username</b>: @{username}\n"
    text += f"<b>To'liq ismi</b>: {fullname}\n"
    text += f"<b>ID</b>: <code>{userID}</code>\n"
    if ADMINS and type(await connector.select_admins()) == list:
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=text)
            time.sleep(1)
    user_message = "Xizmatlarimizdan foydalanganingiz uchun tashakkur !\n"
    user_message += "Xodimlarimiz tez orada sizga a'loqaga chiqishadi !.\n"
    user_message += "Agar kutib qolishni istamasangiz @Saidkodirov ga a'loqaga chiqing !..."
    await message.answer(user_message, reply_markup=startDefBtns)

services_names = []
for service in services:
    services_names.append(service.name)

for service in services:
    @dp.message_handler(text=f"{service.name}")
    async def service_info(message: types.Message):
        text = makeService([service])
        await message.answer(text, reply_markup=apply_btn)

@dp.message_handler(text="🔙 Bosh sahifa")
async def home_keybr(message: types.Message):
    await message.reply("Bo'limni tanlang: ", reply_markup=startDefBtns)

@dp.message_handler(text="🔙 Xizmatlarga qaytish")
async def home_keybr(message: types.Message):
    await message.reply("Servislar ro'yxati: ", reply_markup=services_list)