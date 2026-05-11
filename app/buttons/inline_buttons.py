from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

search_selection_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Search by name", callback_data="search_by_name")],
        [InlineKeyboardButton(text="Search by author", callback_data="search_by_author")],
    ]
)
