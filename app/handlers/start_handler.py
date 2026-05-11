from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    text = (
        "Assalomu alaykum.\n\n"
        "Kitob qidirish uchun.\n"
        "/kitob nomini\n"
        "yoki\n"
        "/muallif nomini\n"
        "yuboring."
    )
    await message.answer(text=text)
