from aiogram import types
from loader import dp
from loader import bot
from utils.misc.getdatetime import get_date_time
from data import connector
from time import sleep
from utils.misc.textmaker import makeChannel
from data.config import get_admins
from states.channelsState import NewChannelState, DeleteChannelState
from keyboards.default import channels_keyb
from aiogram.dispatcher import FSMContext
from data.config import offline_get_admins

ADMINS = offline_get_admins()
@dp.message_handler(chat_id=ADMINS, commands='channels')
async def channels_info(message: types.Message):
    await get_admins()
    global ADMINS
    ADMINS = await connector.select_admins()
    channels = await connector.selection(connector.Channels)
    if channels:
        text = makeChannel(channels)
        await message.answer("Mavjud kanallar ro'yxati: ")
        await message.answer(text, reply_markup=channels_keyb.new_channel_or_delete)
    else:
        await message.answer("Bot hech qanday kanalga qo'shilmagan.", reply_markup=channels_keyb.new_channel_only)

@dp.message_handler(chat_id=ADMINS, text="✍🏻 Yangi kanal qo'shish")
async def add_new_channel_handler_answer(message: types.Message):
    await message.answer("Yodda saqlang kanalni qo'shgandan so'ng, kanalga bot orqali habar yuborish uchun botni kanalga ADMIN qilish zarur.\n\nYaxshi endi kanal ID sini kiriting: ", reply_markup=types.ReplyKeyboardRemove())
    await NewChannelState.ID.set()

@dp.message_handler(state=NewChannelState.ID,chat_id=ADMINS)
async def ask_for_id_handler(message: types.Message, state: FSMContext):
    if message.text and message.text.split('-')[-1].isdigit() and message.text.startswith("-"):
        await state.update_data(
            {"id": message.text}
        )
        await NewChannelState.name.set()

        await message.answer("Yaxshi endi kanal uchun nom kiriting: ", reply_markup=types.ReplyKeyboardRemove())
    else:
        await state.finish()
        await message.answer("Kanal ID noto'g'ri kiritildi. Boshqattan urunib ko'ring 💁🏻‍♂️ /channels", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=NewChannelState.name,chat_id=ADMINS)
async def add_new_channel_handler(message: types.Message, state: FSMContext):
    if message.text and len(message.text) > 5:
        await state.update_data({
            "name": message.text
        }) 
        data = await state.get_data()
        if data.get("id") in await connector.get_all_channels_id():
            await message.answer("Bu ID li kanal hozirda bizga qo'shilgan. Iltimos boshqattan harakat qilib ko'ring !... /channels", reply_markup=types.ReplyKeyboardRemove())
            await state.finish()
        else:
            new_channel = connector.Channels(
                        id =data.get("id"),
                        name=data.get("name"),
                        date=get_date_time()
                    )
            connector.session.add(new_channel)
            connector.session.commit()
            await state.finish()

            await message.answer("Kanal muvaffaqiyatli qo'shildi ! 🎉", reply_markup=types.ReplyKeyboardRemove())
            text = f"Hurmatli admin yangi kanal {message.from_user.full_name} tomonidan qo'shildi.\nQuyida kanal ma'lumotlari bilan tanishing:\n\n"
            text += makeChannel([new_channel])
            for admin in ADMINS:
                await bot.send_message(admin, text)
                sleep(1)
    else:
        await message.answer("Kanal nomi uzunligi 5 dan yuori bo'lsin !...", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(chat_id=ADMINS, text="🙅🏻‍♂️ Mavjud kanalni o'chirish")
async def delete_channel_answer(message: types.Message):
    await message.answer("Yaxshi kanal ID sini kiriting: ", reply_markup=types.ReplyKeyboardRemove())
    await DeleteChannelState.ID.set()


@dp.message_handler(state=DeleteChannelState.ID,chat_id=ADMINS)
async def delete_channel(message: types.Message, state: FSMContext):
    if message.text and message.text.split('-')[-1].isdigit() and message.text.startswith("-"):
        await state.update_data(
            {"id": message.text}
        )
        channels_ids = await connector.get_all_channels_id()
        if message.text in channels_ids:
    
            await connector.delete_channel_by_id(message.text)
            await message.answer("Kanal muvaffaqiyatli o'chirildi ! 🎉", reply_markup=types.ReplyKeyboardRemove())
            await state.finish()
    else:
        await state.finish()

        await message.answer("Kanal ID noto'g'ri kiritildi. Boshqattan urunib ko'ring 💁🏻‍♂️", reply_markup=types.ReplyKeyboardRemove())