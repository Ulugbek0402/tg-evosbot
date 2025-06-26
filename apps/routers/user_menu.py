from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from loader import _
from apps.keyboards.default.user import user_main_keyboard

router = Router()


@router.message(F.text.in_(["🍴 Menu", "🍴 Меню"]))
async def user_menu_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    language = data.get("language")

    await message.answer(
        text=_("User menu is tapped.\n\n📍 Please share your location to proceed:", locale=language),
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[[types.KeyboardButton(text=_("📍 Share location", locale=language), request_location=True)]],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )


@router.message(F.location)
async def location_received_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    language = data.get("language")

    await message.answer(
        text=_("📍 Location received successfully. Thanks!", locale=language),
        reply_markup=await user_main_keyboard()
    )
