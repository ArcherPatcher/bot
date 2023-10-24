from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.methods import AnswerCallbackQuery
import utils
import kb
import text
from aiogram import flags
from aiogram.fsm.context import FSMContext
from states import user_input
from aiogram.types import FSInputFile
import logging


router = Router()




@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)
@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")





async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)


@router.callback_query(F.data == "get_config")


async def input_text_prompt(clbck: AnswerCallbackQuery, state: FSMContext):
    async with state.proxy() as data:
     data['user_name'] = Message.text
    await state.set_state(data)
    await clbck.Message.edit_text(text.cfg_text)
    await clbck.Message.answer(text.cfg_exit, reply_markup=kb.exit_kb)
    


@router.message(user_input)
@flags.chat_action("typing")


async def check_user(msg: Message, state: FSMContext):
    try:
        async with state.proxy() as data:
         user_name = data['user_name']
        prompt = msg.text
        mesg = await msg.answer(text.cfg_wait)
        print(type(data))
        # Вызываем функцию для проверки пользователя
        user = await utils.check_user(data)
        
        if not user:
            await mesg.edit_text(text.gen_error, reply_markup=kb.iexit_kb)
        else:
            await mesg.edit_text(text.text_watermark, disable_web_page_preview=True)
            
            # Отправляем файл из локального хранилища
            with open('zagluh.txt', 'rb') as file:
                await msg.reply_document(file)
    except Exception as e:
        logging.error(e)




