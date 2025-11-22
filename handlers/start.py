from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    """Handle /start command."""
    text = (
        "🤖 Welcome to Gambling Traffic Analytics Bot!\n\n"
        "This bot helps you analyze today's Facebook Ads performance for gambling campaigns.\n\n"
        "Commands:\n"
        "/today - Get today's stats, KPIs, and AI analysis\n\n"
        "Make sure your .env file is configured with API keys."
    )
    await message.reply(text)
    