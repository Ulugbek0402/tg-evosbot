from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.default.user import user_main_keyboard
from states.user import Feedback

router = Router()


@router.message(Feedback.feedback, F.text == "⬅ Назад")
async def back_user_main_keyboard(message: types.Message, state: FSMContext):
    text = "Main menu"
    await message.answer(text=text, reply_markup=user_main_keyboard)
    await state.clear()
