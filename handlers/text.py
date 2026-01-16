from bot import bot, dp
from session import session
from program import program 
from handlers.safesend import *
from storage.sql import DSQL
from aiogram import F
from aiogram.types import Message

@dp.message(F.text)
async def echo_handler(message: Message):

    user = session.short_init(message.chat.id)
    if user.text != None:
        user.text = program.commands(user.text, message.text)
    elif user.text == None:
        user.text = program.clear(message.text)

    DSQL.putin(user.id, user.text)
    await answer(message, user.text)
