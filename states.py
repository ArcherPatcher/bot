from aiogram.fsm.state import StatesGroup, State
#Тут задаю стейт на инпут юзернейма
class Gen (StatesGroup):
    user_input=State()