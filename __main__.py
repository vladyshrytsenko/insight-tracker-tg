import asyncio
import logging
from typing import NoReturn

from aiogram import Bot, Dispatcher

from .config import Config
from .handlers.start import router as start_router
from .handlers.today import router as today_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main() -> NoReturn:
    """
    Main function to initialize and start the Telegram bot.
    
    Validates configuration, sets up the bot and dispatcher,
    includes routers, and starts polling.
    """
    try:
        # Validate configuration
        Config.validate()
        
        # Initialize bot and dispatcher
        bot = Bot(token=Config.TELEGRAM_BOT_TOKEN)
        dp = Dispatcher()
        
        # List of routers for easy maintenance
        routers = [start_router, today_router]
        for router in routers:
            dp.include_router(router)
        
        logger.info("Bot started. Press Ctrl+C to stop.")
        
        # Start polling
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
    