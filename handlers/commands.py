from bot import bot, dp
from session import session
from aiogram import F
from aiogram.types import Message
from handlers.safesend import reply
@dp.message(F.text == "/start")
async def start_handler(message: Message):
    user_id = message.from_user.id
    if user_id in session.users:
        del session.users[user_id]
    user = session.short_init(user_id)
    await reply(message.reply, "Пришлите ваш текст!")