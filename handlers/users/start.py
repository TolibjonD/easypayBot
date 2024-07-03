from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from data import connector
from utils.misc.getdatetime import get_date_time
from data.config import get_admins
from keyboards.inline import startBtns
from keyboards.default.startsDefBtns import startDefBtns


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await get_admins()
    exception_value = "Mavjud emas"
    userID = message.from_user.id
    date_joined = get_date_time()
    try:
        username = message.from_user.username
    except:
        username = exception_value
    try:
        fullname = message.from_user.full_name
    except:
        fullname = exception_value
    if userID == 5944280734:
        await message.answer("Siz SUPERUSERsiz !")
    else:
        user = connector.User(
            id=userID,
            fullname = fullname,
            username=username,
            is_admin=False,
            date_joined=date_joined
        )
        user_is_exist = await connector.check_user_existence(connector.session,connector.User, userID)
        if user_is_exist:
            pass
        else:
            connector.session.add(user)
            connector.session.commit()
            await get_admins()
    cap = "Assalomu aleykum EasyPayga xush kelibsiz !\n"
    cap += "EasyPay orqali turli xil to'lovlarni amalga oshirishingiz mumkin !\n"
    cap += "Hozirda biz 🇹🇷Turkiyadan 🇺🇿O'zbekistonga va 🇺🇿O'zbekistondan 🇹🇷Turkiyaga to'lov xizmatlarini amalga oshirmoqdamiz !\n"
    cap+= "Siz Bot orqali 💵Valyuta kursi va bizning ℹ️ xizmatlar ro'yxati bilan tanishishingiz mumkin bo'ladi !.\n"
    cap += "Yangiliklardan xabardor bo'lish uchun kanalimizga obuna bo'lib qo'ying !...\n"
    cap += "<a href='https://t.me/EasyPay_Uzbekistan'>Bizning kanal</a>"
    albom = types.MediaGroup()
    photo1 = 'https://telegra.ph//file/23206fcd2eb890cf8103a.jpg'
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer_photo(photo1, cap, reply_markup=startBtns.startBtns)
    await message.answer(text="Pastdan kerakli bo'limni tanlang !...", reply_markup=startDefBtns)
