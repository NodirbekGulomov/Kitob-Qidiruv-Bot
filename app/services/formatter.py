async def format_books(books: list[type[str, str, str, int]]) -> str:
    text = "----------------"
    for name, author, genre, year in books:
        text += (
            f"\n\n"
            f"📚 Book: {name}\n\n"
            f"✍️ Author: {author}\n"
            f"📂 Genre: {genre}\n"
            f"📅 Year: {year}\n\n"
            f"----------------"
        )

    return text
