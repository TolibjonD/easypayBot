from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from data import connector

services = connector.session.query(connector.Services).all()

services_names = []
for service in services:
    services_names.append(service.name)

services_list= ReplyKeyboardMarkup(resize_keyboard=True)
for service in services_names:
    services_list.add(KeyboardButton(service))

services_list.add(KeyboardButton("🔙 Bosh sahifa"))

servislar_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("➕ Servis qo'shish")],
        [KeyboardButton("🗑 Servisni o'chirish")],
        [KeyboardButton("🔙 Bosh sahifa")],
    ],
    resize_keyboard=True
)
servis_add_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("➕ Servis qo'shish")],
        [KeyboardButton("🔙 Bosh sahifa")],
    ],
    resize_keyboard=True
)

apply_btn = ReplyKeyboardMarkup(
    keyboard=
    [
        [KeyboardButton("📞 Xizmatdan foydalanish")],
        [KeyboardButton("🔙 Xizmatlarga qaytish")]
    ],
    resize_keyboard=True
)