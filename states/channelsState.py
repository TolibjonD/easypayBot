from aiogram.dispatcher.filters.state import State, StatesGroup


class NewChannelState(StatesGroup):
    ID = State()
    name = State()

class DeleteChannelState(StatesGroup):
    ID = State()