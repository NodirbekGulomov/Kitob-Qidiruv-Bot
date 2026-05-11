from app.db.base import get_connection


def clean_books_table() -> None:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM books
        """)


async def add_book(name: str, author: str, genre: str, year: int) -> None:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO books (name, author, genre, year) VALUES (?, ?, ?, ?)
        """, (name, author, genre, year))


async def get_books_by_name(name: str) -> list[tuple[str, str, str, int]]:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT name, author, genre, year FROM books WHERE name = ?
        """, (name,))
        return cur.fetchall()


async def get_books_by_author(author: str) -> list[tuple[str, str, str, int]]:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT name, author, genre, year FROM books WHERE author = ?
        """, (author,))
        return cur.fetchall()
