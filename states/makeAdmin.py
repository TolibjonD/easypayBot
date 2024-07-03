from aiogram.dispatcher.filters.state import State, StatesGroup

class MakeAdmin(StatesGroup):
    userID = State()
class KickAdmin(StatesGroup):
    userID = State()