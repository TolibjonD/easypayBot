from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

startDefBtns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👨‍💻 EasyPAY xizmatlari ro'yxati"),
        ],
        [
            KeyboardButton("💱 Bugungi valyuta kursi"),
        ],
    ],
    resize_keyboard=True
)