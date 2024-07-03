from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

new_channel_or_delete = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("✍🏻 Yangi kanal qo'shish")],
        [KeyboardButton("🙅🏻‍♂️ Mavjud kanalni o'chirish")]
    ],
    resize_keyboard=True
)
new_channel_only = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("✍🏻 Yangi kanal qo'shish")],
    ],
    resize_keyboard=True
)
