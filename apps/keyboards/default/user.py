from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


user_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍴 Меню")],
        [KeyboardButton(text="🛍 Мои заказы")],
        [KeyboardButton(text="✍ Оставить отзыв"), KeyboardButton(text="⚙ Настройки")]
    ],
    resize_keyboard=True,
    is_persistent=True
)


address_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🗺 Мои адреса")],
        [
            KeyboardButton(text="📍 Отправить геолокацию", request_location=True),
            KeyboardButton(text="⬅ Назад")
        ]
    ],
    resize_keyboard=True,
    is_persistent=True
)


back_user_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True,
    is_persistent=True
)


phone_number_share = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Share phone number", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Location keyboard
location_share = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Share location", request_location=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
