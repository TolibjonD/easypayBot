from aiogram.dispatcher.filters.state import State, StatesGroup

class ServiceState(StatesGroup):
    name = State()
    percent= State()
class DeleteServiceState(StatesGroup):
    ID = State()