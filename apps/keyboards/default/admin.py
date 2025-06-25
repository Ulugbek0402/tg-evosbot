from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍴 Products"),
            KeyboardButton(text="🍴 Categories")
        ],
        [
            KeyboardButton(text="👥 Users"),
            KeyboardButton(text="📝 Orders")
        ],
        [
            KeyboardButton(text="📊 Statistics"),
            KeyboardButton(text="⚙️ Settings")
        ]
    ],
    resize_keyboard=True,
    is_persistent=True
)