from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationUser(StatesGroup):
    LName = State()
    Email = State()

    LinkBOT = State()
    Budget = State()
    Phone = State()

