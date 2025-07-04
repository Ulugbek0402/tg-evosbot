from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db_queries.user import register
from apps.keyboards.default.user import phone_number_share, user_main_keyboard
from apps.states.user import Register
from loader import _

router = Router()

@router.callback_query(Register.language)
async def get_user_language_handler(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(language=call.data, chat_id=call.message.chat.id)

    await call.message.answer(text=_("Please enter your full name", locale=call.data))
    await state.set_state(Register.full_name)

@router.message(Register.full_name)
async def get_user_full_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    data = await state.get_data()
    language = data.get('language')

    await message.answer(text=_("Please share your phone number", locale=language), reply_markup=phone_number_share)
    await state.set_state(Register.phone_number)

@router.message(Register.phone_number, F.contact)
async def get_user_phone_number_handler(message: types.Message, state: FSMContext, session: AsyncSession):
    await state.update_data(
        phone_number=message.contact.phone_number,
        username=message.from_user.username
    )
    data = await state.get_data()
    language = data.get('language')

    if await register(data=data, session=session):
        await message.answer(
            text=_("You have successfully registered 🎉", locale=language),
            reply_markup=await user_main_keyboard()
        )
    else:
        await message.answer(
            text=_("Please try again later, something went wrong 😔", locale=language)
        )

    await state.clear()
