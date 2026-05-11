from app.db.commands import clean_books_table
from app.db.models import create_books_table
from app.services.add_initial_information import add_initial_information


def init_db() -> None:
    create_books_table()
    clean_books_table()
    add_initial_information()
