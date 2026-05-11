from aiogram import Router, F
from aiogram.types import Message

from app.db.commands import get_books_by_name, get_books_by_author
from app.services.formatter import format_books

router = Router()


@router.message(F.text.startswith("/kitob"))
async def search_handler(message: Message) -> None:
    if message.text:
        book = message.text.replace("/kitob", "").strip()
        await message.answer(text=await format_books(await get_books_by_name(book)))


@router.message(F.text.startswith("/muallif"))
async def search_by_author_handler(message: Message) -> None:
    if message.text:
        author = message.text.replace("/muallif", "").strip()
        await message.answer(text=await format_books(await get_books_by_author(author)))
