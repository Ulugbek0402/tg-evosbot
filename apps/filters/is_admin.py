from aiogram.filters import BaseFilter
from aiogram import types
from aiogram.utils.chat_member import ADMINS


class IsAdmin(BaseFilter):
    async def __call__(self, message: types.Message):
        return message.from_user.id in ADMINS
