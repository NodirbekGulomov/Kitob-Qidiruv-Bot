async def format_books(books: list[tuple[str, str, str, int]]) -> str:
    if not books:
        return "❌ Hech qanday kitob topilmadi"

    text = "----------------------------------------------------------------"

    for name, author, genre, year in books:
        text += (
            f"\n\n"
            f"📚 Book: {name}\n\n"
            f"✍️ Author: {author}\n"
            f"📂 Genre: {genre}\n"
            f"📅 Year: {year}\n\n"
            f"----------------------------------------------------------------"
        )

    return text
