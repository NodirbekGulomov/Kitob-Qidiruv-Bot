import asyncio

from app.bot import tg_bot
from app.db.init import init_db
from app.dispatcher import dp


async def main():
    init_db()
    print("Bot is running...")
    await dp.start_polling(tg_bot)


if __name__ == "__main__":
    asyncio.run(main())
