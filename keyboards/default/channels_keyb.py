from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

new_channel_or_delete = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("✍🏻 Yangi kanal qo'shish")],
        [KeyboardButton("🙅🏻‍♂️ Mavjud kanalni o'chirish")],
        [KeyboardButton("🔙 Bosh sahifa")],
    ],
    resize_keyboard=True
)
new_channel_only = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("✍🏻 Yangi kanal qo'shish")],
        [KeyboardButton("🔙 Bosh sahifa")],
    ],
    resize_keyboard=True
)
