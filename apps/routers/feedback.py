from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext

from apps.keyboards.default.user import back_user_main_keyboard, user_main_keyboard
from apps.states.user import Feedback
from core.config import DEVELOPER

router = Router()


@router.message(F.text.in_(["✍ Send feedback", "✍ Отправить отзыв", "✍ Fikr bildirish"]))
async def send_feedback_handler(message: types.Message, state: FSMContext):
    text = "Please enter your message in one text"
    await message.answer(text=text, reply_markup=await back_user_main_keyboard())

    await state.set_state(Feedback.feedback)


@router.message(Feedback.feedback)
async def get_feedback_handler(message: types.Message, state: FSMContext, bot: Bot):
    full_name = message.from_user.full_name or "Unknown User"

    feedback = f"""
User: {message.from_user.mention_html(full_name)}
Feedback: {message.text}
    """
    await bot.send_message(text=feedback, chat_id=DEVELOPER, parse_mode="HTML")

    await message.answer(text="Your feedback is sent to admins ✅", reply_markup=await user_main_keyboard())

    await state.clear()
