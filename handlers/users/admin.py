from aiogram import types

from loader import dp
from data import connector
from data.config import ADMINS
from utils.misc import textmaker
from aiogram.dispatcher import FSMContext
from data.config import get_admins
from states.makeAdmin import MakeAdmin, KickAdmin
from states.servislarState import ServiceState, DeleteServiceState
from loader import bot
from keyboards.default import servislar
from aiogram.dispatcher.filters import Text
from utils.misc.getdatetime import get_date_time
from keyboards.default.startsDefBtns import startDefBtns

@dp.message_handler(chat_id=ADMINS,commands=["users", "list"])
async def show_users_to_admins(message: types.Message):
    await get_admins()
    users = await connector.selection(connector.User)
    if users and type(users) == list:
        count = await connector.count_users()
        file = textmaker.makeUser(users)
        await message.answer("Hurmatli Admin ! Botda foydalanuvchilar mavjud. Ularning ro'yxatini ko'rishingiz mumkin.\n")
        file = types.InputFile(path_or_bytesio="data/users/users.txt")
        await message.answer_document(file, caption=f"Foydalanuvchilar ro'yxati.  ( Jami: {count} ).")
    else:
        await message.answer("Foydalanuvchilar mavjud emas.")

@dp.message_handler(chat_id=ADMINS,commands=["admins"])
async def show_admins_to_admins(message: types.Message):
    await get_admins()
    users = await connector.selection(connector.User,admins=True)
    if users and type(users) == list:
        count = await connector.count_admins()
        file = textmaker.makeUser(users)
        file = types.InputFile(path_or_bytesio="data/users/users.txt")
        await message.answer_document(file, caption=f"Adminlar ro'yxati ( Jami: {count} ).")
    else:
        await message.answer("Adminlar mavjud emas.")

@dp.message_handler(chat_id=ADMINS, commands=['makeAdmin'])
async def make_admin(message: types.Message):
    await get_admins()
    users = await connector.selection(connector.User)
    if users and type(users) == list:
        await MakeAdmin.userID.set()
        file = textmaker.makeUser(users)
        file = types.InputFile(path_or_bytesio="data/users/users.txt")
        await message.answer_document(file, caption="Foydalanuvchilar ro'yxati ")
        await message.answer("<i>Ro'yxatdan userID ni oling va menga yuboring ! Bu yangi admin tayinlash uchun kerak !</i>")
    else:
        await message.answer("Foydalanyvchilar qo'shilishini kuting !, Admin tayinlash uchun botda birorta ham foydalanuvchi <b>mavjud emas</b>.")
    

@dp.message_handler(chat_id=ADMINS, state=MakeAdmin.userID)
async def make_admin_userID(message: types.Message, state: FSMContext):
    await get_admins()
    enteredUserID = message.text
    users = await connector.selection(connector.User)
    if enteredUserID.isdigit():
        enteredUserID = int(enteredUserID)
        if enteredUserID in await connector.select_admins():
            await message.answer("Ushbu foydalanuvchi allaqachon ADMIN. Boshqa userID kiritng !")
            await state.finish()
        if await connector.select_users_id() == await connector.select_admins():
            await message.answer("Barcha foydalanuvchilar shundoq ham ADMIN ekan. Boshqa buyruqlardan foydalanib ko'ring !...")
            await state.finish()
        else:
            user_is_exist = await connector.check_user_existence(connector.session,connector.User, enteredUserID)
            if user_is_exist:
                user = await connector.makeAdmin(enteredUserID, status=True)
                if user:
                    text = "Yangi admin muvaffaqiyatli tayinlandi: \n\n"
                    text+=textmaker.makeUser([user])
                    await message.answer(text, reply_markup=startDefBtns)
                    try:
                        await bot.send_message(enteredUserID, f"Siz <a href='https://t.me/{message.from_user.username}'>{message.from_user.full_name}</a> tomonidan Admin qilib saylandingiz !...")
                    except:
                        await bot.send_message(enteredUserID, f"Siz SUPERUSER tomonidan Admin qilib saylandingiz !...")
                    await state.finish()
                else:
                    await message.answer("Admin qo'shilmadi ! Server xatosi. Dasturchiga murojaat qiling !")
            else:
                await message.answer("Siz kiritgan UserID ro'yxatda mavjud emas yoki siz xatolikga yo'l qo'ymoqdasz !...")
    else:
        users = await connector.selection(connector.User)
        file = textmaker.makeUser(users)
        file = types.InputFile(path_or_bytesio="data/users/users.txt")
        await message.answer_document(file, caption="Foydalanuvchilar ro'yxati ")
        await message.answer("<i>Ro'yxatdan userID ni oling va menga yuboring ! Faqat userID ni yuboring. Siz UserID yubormayabsz ? Admin tayinlash uchun to'g'ri userID ni yuboring.</i>")

@dp.message_handler(chat_id=ADMINS, commands=['kickAdmin'])
async def kick_admin(message: types.Message):
    await get_admins()
    users = await connector.selection(connector.User, admins=True)
    if users and type(users) == list:
        await KickAdmin.userID.set()
        file = textmaker.makeUser(users)
        file = types.InputFile(path_or_bytesio="data/users/users.txt")
        await message.answer_document(file, caption="Foydalanuvchilar ro'yxati ")
        await message.answer("<i>Adminni olib tashlash uchun Ro'yxatdan userID ni oling va menga yuboring !</i>")
    else:
        await message.answer("<i>Botda o'chirishingiz uchun bironta ham adminlar mavjud emas. !</i>")

@dp.message_handler(chat_id=ADMINS, state=KickAdmin.userID)
async def kick_admin_userID(message: types.Message, state: FSMContext):
    await get_admins()
    users = await connector.selection(connector.User, admins=True)
    enteredUserID = message.text
    if enteredUserID.isdigit():
        enteredUserID = int(enteredUserID)
        if enteredUserID == 5944280734:
            await message.answer("Bu SUPERUSER uni hechkim olib tashlay olmaydi !...")
            await state.finish()
        else:
            if enteredUserID in await connector.select_admins():
                user = await connector.makeAdmin(enteredUserID, status=False)
                if user:
                    text = "Admin muvaffaqiyatli olib tashlandi: \n\n"
                    text+=textmaker.makeUser([user])
                    await message.answer(text)
                    try:
                        await bot.send_message(enteredUserID, f"Siz <a href='https://t.me/{message.from_user.username}'>{message.from_user.full_name}</a> tomonidan Adminlik huquqidan mahrum bo'ldingiz !...")
                    except:
                        await bot.send_message(enteredUserID, f"Siz SUPERUSER tomonidan Adminlik huquqidan mahrum bo'ldingiz !...")
                    await state.finish()
                else:
                    await message.answer("Admin olib tashlanmadi ! Server xatosi. Dasturchiga murojaat qiling !")
            else:
                await message.answer("Kiritilgan foydalanuvchi shundoq ham admin emas !")
                await state.finish()
    else:
        file = textmaker.makeUser(users)
        file = types.InputFile(path_or_bytesio="data/users/users.txt")
        await message.answer_document(file, caption="Foydalanuvchilar ro'yxati ")
        await message.answer("<i>Ro'yxatdan userID ni oling va menga yuboring ! Faqat userID ni yuboring. Men adminni adminlar ro'yxatidan olib tashlayman.</i>")


# ? Services section
@dp.message_handler(chat_id=ADMINS,commands=["servislar"])
async def show_services(message: types.Message):
    await get_admins()
    services = await connector.selection(connector.Services)
    if services:
        text = textmaker.makeService(services)
        await message.answer("EasyPay servislar ro'yxati: \n")
        await message.answer(text, reply_markup=servislar.servislar_keyboard)
    else:
        await message.answer("Servislar mavjud emas.", reply_markup=servislar.servis_add_keyboard)

@dp.message_handler(Text(equals="➕ Servis qo'shish"), chat_id=ADMINS)
async def add_service_name(message: types.Message):
    await get_admins()
    await ServiceState.name.set()
    await message.answer("Yangi servis qo'shish uchun servis nomini kiriting: ", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=ServiceState.name, chat_id=ADMINS)
async def add_service_percent(message: types.Message, state: FSMContext):
    await get_admins()
    name = message.text
    if name and len(name) > 5:
        if not await connector.check_service_existence(name):
            await state.update_data(
                {"name": name}
            )
            await ServiceState.next()
            await message.answer("Endi Servis uchun xizmat haqqi foiz miqdorini kiriting. Miqdor faqat o'nli yoki butun son ko'rinishida bo'lsin.\nMisol uchun: 5 yoki 5.5", reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.answer("Bu servis allaqachon EasyPayda mavjud. /servislar", reply_markup=startDefBtns)
            await state.finish()
    else:
        await message.answer("Servis nomi xato kiritilyabdi. Kamida 5 ta belgidan iborat bo'lishi kerak !...", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=ServiceState.percent, chat_id=ADMINS)
async def add_service(message: types.Message, state: FSMContext):
    await get_admins()
    percent = message.text
    if percent:
        await state.update_data(
            {"percent": percent}
        )
        data = await state.get_data()

        service = connector.Services(
            name=data.get("name"),
            percent=data.get("percent"),
            date_joined = get_date_time()
        )
        connector.session.add(service)
        connector.session.commit()
        await state.finish()
        await message.answer("Yangi servis muvaffaqiyatli qo'shildi !", reply_markup=startDefBtns)
    else:
        await message.answer("Qiymatni to'g'ri kiriting !...", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals="🗑 Servisni o'chirish"), chat_id=ADMINS)
async def service_delete(message: types.Message):
    await get_admins()
    await DeleteServiceState.ID.set()
    await message.answer("Servisni o'chrish uchun ID ni kiriting. /servislar", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=DeleteServiceState.ID, chat_id=ADMINS)
async def service_delete_by_id(message: types.Message, state: FSMContext):
    ID = message.text
    if ID:
        try:
            ID = int(ID)
        except:
            pass
        if await connector.check_service_existence_by_id(ID):
            await connector.delete_service_by_id(ID)
            await message.answer("Servis muvaffaqiyatli olib tashlandi !...", reply_markup=startDefBtns)
            await state.finish()
        else:
            await message.answer("Bunday ID ga ega servis xizmati yo'q. Adashdigiz. /servislar")
            await state.finish()
