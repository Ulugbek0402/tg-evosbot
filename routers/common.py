from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.default.user import user_main_keyboard
from keyboards.inline.user import languages
from queries.user import get_user
from states.user import Register

router = Router()


@router.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    user = get_user(chat_id=message.chat.id)
    if not user:
        text = "Assalomu alaykum, please select the language !"
        await message.answer(text=text, reply_markup=languages)
        await state.set_state(Register.language)
    else:
        text = "Assalomu alaykum, welcome back"
        await message.answer(text=text, reply_markup=user_main_keyboard)
