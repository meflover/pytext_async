from ratelimiter import limiter
from bot import bot
async def safe_send(send_func, *args, **kwargs):
    """Асинхронная обёртка над отправкой с контролем лимитов"""
    try:
        limiter.acquire()
        result = await send_func(*args, **kwargs)
        print(f"[SAFE_SEND] {send_func.__name__}: {limiter.score}")
        return result
    except Exception as e:
        print(f"[ERROR] safe_send: {e}\n{args}\n{send_func}")
        return None


async def answer(id_, text):
    await safe_send(bot.send_message,id_,text)
async def reply(reply, text):
    await safe_send(reply, text)


async def dropvoice(user_id, file_id):
    await safe_send(bot.send_voice, user_id, file_id)

async def dropkrug(user_id, file_id):
    await safe_send(bot.send_video_note, user_id, file_id)

async def dropaudio(user_id, file_id):
    await safe_send(bot.send_audio, user_id, file_id)

async def dropgif(user_id, file_id):
    await safe_send(bot.send_animation, user_id, file_id)

async def dropmedia(user_id, media):
    await safe_send(bot.send_media_group, user_id, media)
async def dropphoto_a(user_id, photo_id, text =''):
    await safe_send(bot.send_photo, user_id, photo_id, caption=text, parse_mode='HTML')

async def dropphoto(user_id, photo_id, text=''):
    await safe_send(bot.send_photo, user_id, photo_id, caption=text)

async def dropb(user_id, one_time, buttons, text):
    """Создаёт клавиатуру и отправляет сообщение"""

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=one_time)
    markup.add(*[types.KeyboardButton(button) for button in buttons])
    await safe_send(bot.send_message, user_id, text, reply_markup=markup)