from aiogram import Dispatcher

from app.handlers.start_handler import router as start_router
from app.handlers.search_handlers import router as search_router

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(search_router)
