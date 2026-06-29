from aiogram.fsm.state import StatesGroup, State

class UserState(StatesGroup):
    fullname = State()
    age = State()
    phone_number = State()
    location = State()
    login_phone = State()
