from ratelimiter import limiter

async def safe_send(send_func, *args, **kwargs):
    try:
        limiter.acquire()
        result = await send_func(*args, **kwargs)
        print(f"[SAFE_SEND] {send_func.__name__}: {limiter.score}")
        return result
    except Exception as e:
        print(f"[ERROR] safe_send: {e}\n{args}\n{send_func}")
        return None


async def answer(message, text):
    await safe_send(message.answer, text)
