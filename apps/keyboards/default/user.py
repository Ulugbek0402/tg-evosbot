from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


async def user_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("🍴 Menu"))],
            [KeyboardButton(text=_("🛍 My orders"))],
            [KeyboardButton(text=_("✍ Send feedback")), KeyboardButton(text="⚙ Settings")]
        ],
        resize_keyboard=True,
        is_persistent=True
    )


async def address_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("🗺 My address"))],
            [
                KeyboardButton(text=_("📍 Share location"), request_location=True),
                KeyboardButton(text=_("⬅ Back"))
            ]
        ],
        resize_keyboard=True,
        is_persistent=True
    )


async def back_user_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=_("⬅ Back"))]
        ],
        resize_keyboard=True,
        is_persistent=True
    )


phone_number_share = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Share phone number ☎️", request_contact=True)
    ]], resize_keyboard=True, one_time_keyboard=True
)

location_share = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Share location 🌏", request_location=True)
    ]], resize_keyboard=True, one_time_keyboard=True
)
