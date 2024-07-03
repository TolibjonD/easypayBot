from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

startBtns = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🍫 Botni ulashish", switch_inline_query="EasyPAY bilan to'lovlarni qulay amalga oshir !"),
            ],
        [
            InlineKeyboardButton("🌐 Bizning sahifa", url="https://plucky-salesman-34e.notion.site/EasyPay-nima-f84d9361b42143c0a9690271e1d2dfce"),
            ],
    ]
)