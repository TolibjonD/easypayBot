from data import connector
from loader import dp 
from data.config import ADMINS
from aiogram import types
from utils.get_today_currency import get_currency_today

@dp.message_handler(chat_id=ADMINS, commands="update_currency")
async def currency_update(message: types.Message):
    data_try = get_currency_today()
    data_uzs = get_currency_today(from_="USD", to_="UZS")
    if data_try:
        usd_to_try = data_try['result']
        amount = data_try['amount']
        date = data_try['date']
    else:
        usd_to_try = None
        amount = None
        date = None
    if data_uzs:
        usd_to_uzs = data_uzs['result']
    else:
        usd_to_uzs=None
    currency = connector.Currency(
        usd_to_try = usd_to_try,
        usd_to_uzs = usd_to_uzs,
        amount = amount,
        updated_at=date
    )
    connector.session.add(currency)
    connector.session.commit()
    await message.answer("Muvaffaqiyatli yangilandi !...")