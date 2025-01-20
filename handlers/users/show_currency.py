from loader import dp
from data import connector
from aiogram import types
from utils.misc.getdatetime import get_todys_date
from data.config import ADMINS
from utils.get_today_currency import get_currency_today
from loader import bot
import time

@dp.message_handler(text="💱 Bugungi valyuta kursi")
async def show_todays_currency(message: types.Message):
    today = get_todys_date()
    data = await connector.get_today_currency_by_date()
    if data:
        text = "Bugungi valyutalar kursi bilan tanishing:\n\n"
        text += f"<b>{data.amount}$</b> USD (AQSH dollari) = <b>{round(float(data.usd_to_try),2)}</b> TRY (Turk Lirasi)\n\n"
        text += f"<b>{data.amount}$</b> USD (AQSH dollari) = <b>{round(float(data.usd_to_uzs),2)}</b> UZS so'm\n\n"
        text += f"<b>{round(float(data.usd_to_try),2)}</b> TRY Turk Lirasi = <b>{round(float(data.usd_to_uzs),2)}</b> UZS so'm.\n\n"
        text += f"<b>Ma'lumot olingan sana</b>: <code>{data.updated_at}</code>\n\n\n"
        text += f"Pul yuborish yoki to'lovlar uchun murojaat: @Easy_Pay_Uzbekistan\n\n"
        text += f"Manbaa: @EasyPay_Uzbekistan"
        await message.reply(text)
    else:
        data_uzs = get_currency_today("USD", "UZS")
        data_try = get_currency_today()
        usd_to_try = round(float(data_try['result']), 2)
        amount = data_try['amount']
        usd_to_uzs = round(float(data_uzs['result']), 2)
        date = data_uzs['date']
        if data_uzs and data_try:
            text = "Bugungi valyutalar kursi bilan tanishing:\n\n"
            text += f"<b>{amount}$</b> USD (AQSH dollari) = <b>{usd_to_try}</b> TRY (Turk Lirasi)\n\n"
            text += f"<b>{amount}$</b> USD (AQSH dollari) = <b>{usd_to_uzs}</b> UZS so'm\n\n"
            text += f"<b>{usd_to_try}</b> TRY Turk Lirasi = <b>{usd_to_uzs}</b> UZS so'm.\n\n"
            text += f"<b>Ma'lumot olingan sana</b>: <code>{date}</code>"
            text += f"Pul yuborish yoki to'lovlar uchun murojaat: @Easy_Pay_Uzbekistan\n\n"
            text += f"Manbaa: @EasyPay_Uzbekistan"

            await message.answer(text)

@dp.message_handler(chat_id=ADMINS, commands="sendcurrency_channels")
async def show_todays_currency(message: types.Message):
    data_uzs = get_currency_today("USD", "UZS")
    data_try = get_currency_today()
    usd_to_try = round(float(data_try['result']), 2)
    amount = data_try['amount']
    usd_to_uzs = round(float(data_uzs['result']), 2)
    date = data_uzs['date']
    if data_uzs and data_try:
        text = "💱 Bugungi valyutalar kursi bilan tanishing:\n\n"
        text += f"<b>{amount}$</b> USD (AQSH dollari) = <b>{usd_to_try}</b> TRY (Turk Lirasi)\n\n"
        text += f"<b>{amount}$</b> USD (AQSH dollari) = <b>{usd_to_uzs}</b> UZS so'm\n\n"
        text += f"<b>{usd_to_try}</b> TRY Turk Lirasi = <b>{usd_to_uzs}</b> UZS so'm.\n\n"
        text += f"📅 <b>Ma'lumot olingan sana</b>: <code>{date}</code>\n\n\n"
        text += f"🤙 Pul yuborish yoki to'lovlar uchun murojaat: @Easy_Pay_Uzbekistan\n\n"
        text += f"💬 Manbaa: @EasyPay_Uzbekistan"
        channels = await connector.get_all_channels_id()
        if channels and type(channels) == list:
            await message.answer("Kanallarga valyuta kursi yuborishni boshladim !...")
            for channel in channels:
                try:
                    await bot.send_message(channel, text)
                except:
                    print(channel)
                time.sleep(2)
            await message.answer("Barcha kanallarga valyuta kursi yuborildi !...")
    
