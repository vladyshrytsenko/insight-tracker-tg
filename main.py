import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import Config
from handlers.start import router as start_router
from handlers.today import router as today_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    # Validate configuration
    Config.validate()

    # Initialize bot and dispatcher
    bot = Bot(token=Config.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()

    # Include routers
    dp.include_router(start_router)
    dp.include_router(today_router)

    logger.info("Bot started. Press Ctrl+C to stop.")

    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    