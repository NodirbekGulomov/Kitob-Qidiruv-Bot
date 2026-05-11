from app.db.commands import clean_books_table
from app.db.models import create_books_table


def init_db() -> None:
    create_books_table()
    clean_books_table()
