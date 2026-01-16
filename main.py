import asyncio
from bot import bot,dp
from session import session
from handlers import commands, text

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(e) 