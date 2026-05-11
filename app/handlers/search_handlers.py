from aiogram import Router, F
from aiogram.types import Message

from app.db.commands import get_books_by_name, get_books_by_author
from app.services.formatter import format_books

router = Router()


@router.message(F.text)
async def search_handler(message: Message) -> None:
    if message.text:

        name, what = message.text.split("-")

        if what.endswith("kitob nomini"):
            await message.answer(text=await format_books(await get_books_by_name(name)))
            return
        elif what.endswith("muallif nomini"):
            await message.answer(text=await format_books(await get_books_by_author(name)))
            return

        text = (
            "nom - kitob nomini\n"
            "yoki\n"
            "nom - muallif nomini\n"
            "yuqoridagi formatda kiriting."
        )

        await message.answer(text=text)
